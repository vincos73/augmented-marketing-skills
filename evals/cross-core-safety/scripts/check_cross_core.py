#!/usr/bin/env python3
"""Validate semantic safety invariants across multiple AMS handoffs."""

from __future__ import annotations

import argparse
import copy
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parents[1]
DEFAULT_CONTRACT = ROOT / "contract.json"
DEFAULT_CASE = ROOT / "fixtures" / "positive" / "handoffs.json"
DEFAULT_NEGATIVE = ROOT / "fixtures" / "negative" / "mutations.json"
IDENTIFIER_TYPES = {
    "customer_name",
    "company_name",
    "logo",
    "specific_industry",
    "project_data",
}


@dataclass(frozen=True)
class Violation:
    code: str
    stage: str
    invariant_id: str
    message: str

    def render(self) -> str:
        location = self.stage
        if self.invariant_id:
            location += f"/{self.invariant_id}"
        return f"[{self.code}] {location}: {self.message}"


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"file non trovato: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"JSON non valido in {path}:{exc.lineno}:{exc.colno}: {exc.msg}"
        ) from exc


def index_by_id(
    items: Any,
    *,
    category: str,
    stage: str,
    violations: list[Violation],
) -> dict[str, dict[str, Any]]:
    if not isinstance(items, list):
        violations.append(
            Violation("INVALID_COLLECTION", stage, category, "deve essere una lista")
        )
        return {}

    indexed: dict[str, dict[str, Any]] = {}
    for position, item in enumerate(items):
        if not isinstance(item, dict) or not isinstance(item.get("id"), str):
            violations.append(
                Violation(
                    "INVALID_ITEM",
                    stage,
                    category,
                    f"elemento {position} privo di id stringa",
                )
            )
            continue
        item_id = item["id"]
        if item_id in indexed:
            violations.append(
                Violation(
                    "DUPLICATE_ID",
                    stage,
                    item_id,
                    f"id duplicato nella raccolta {category}",
                )
            )
            continue
        indexed[item_id] = item
    return indexed


def require_items(
    expected_items: list[dict[str, Any]],
    actual_items: Any,
    *,
    category: str,
    stage: str,
    violations: list[Violation],
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    expected = {item["id"]: item for item in expected_items}
    actual = index_by_id(
        actual_items, category=category, stage=stage, violations=violations
    )
    for item_id in expected.keys() - actual.keys():
        violations.append(
            Violation(
                "MISSING_INVARIANT",
                stage,
                item_id,
                f"invariante {category} assente dall'handoff",
            )
        )
    for item_id in actual.keys() - expected.keys():
        violations.append(
            Violation(
                "UNKNOWN_INVARIANT",
                stage,
                item_id,
                f"invariante {category} non previsto dal contratto",
            )
        )
    return expected, actual


def check_claims(
    contract: dict[str, Any],
    state: dict[str, Any],
    stage: str,
    violations: list[Violation],
) -> None:
    expected, actual = require_items(
        contract["claims"],
        state.get("claims"),
        category="claims",
        stage=stage,
        violations=violations,
    )
    for item_id in expected.keys() & actual.keys():
        wanted = expected[item_id]
        found = actual[item_id]
        if found.get("policy") != wanted["policy"]:
            violations.append(
                Violation(
                    "CLAIM_POLICY_CHANGED",
                    stage,
                    item_id,
                    f"policy attesa {wanted['policy']!r}, trovata {found.get('policy')!r}",
                )
            )
        if wanted["policy"] == "forbidden" and found.get("assertion_state") != "not_asserted":
            violations.append(
                Violation(
                    "CLAIM_ASSERTED",
                    stage,
                    item_id,
                    "un claim vietato è stato trasformato in affermazione utilizzata",
                )
            )
        if wanted["policy"] == "conditional":
            changed = [field for field in ("assertion_state", "formula", "approval_role_id") if found.get(field) != wanted.get(field)]
            if changed:
                violations.append(
                    Violation(
                        "CONDITIONAL_CLAIM_CHANGED",
                        stage,
                        item_id,
                        f"formula, stato o gate di approvazione modificati: {', '.join(changed)}",
                    )
                )


def check_testimonials(
    contract: dict[str, Any],
    state: dict[str, Any],
    stage: str,
    violations: list[Violation],
) -> None:
    expected, actual = require_items(
        contract["testimonials"],
        state.get("testimonials"),
        category="testimonials",
        stage=stage,
        violations=violations,
    )
    for item_id in expected.keys() & actual.keys():
        wanted = expected[item_id]
        found = actual[item_id]
        for field in ("authorization_state", "identity_mode"):
            if found.get(field) != wanted[field]:
                violations.append(
                    Violation(
                        "TESTIMONIAL_SCOPE_CHANGED",
                        stage,
                        item_id,
                        f"{field} atteso {wanted[field]!r}, trovato {found.get(field)!r}",
                    )
                )
        disclosed = found.get("disclosed_identifier_types", [])
        if not isinstance(disclosed, list):
            violations.append(
                Violation(
                    "INVALID_ITEM",
                    stage,
                    item_id,
                    "disclosed_identifier_types deve essere una lista",
                )
            )
            continue
        unknown = sorted(set(disclosed) - IDENTIFIER_TYPES)
        if unknown:
            violations.append(
                Violation(
                    "TESTIMONIAL_IDENTIFIER_TYPE_UNKNOWN",
                    stage,
                    item_id,
                    f"tipi di identificatore fuori vocabolario: {', '.join(unknown)}",
                )
            )
        exposed = sorted(set(disclosed) & set(wanted["forbidden_identifier_types"]))
        if exposed:
            violations.append(
                Violation(
                    "TESTIMONIAL_IDENTIFIER_EXPOSED",
                    stage,
                    item_id,
                    f"identificatori vietati esposti: {', '.join(exposed)}",
                )
            )


def check_capacities(
    contract: dict[str, Any],
    state: dict[str, Any],
    stage: str,
    violations: list[Violation],
) -> None:
    expected, actual = require_items(
        contract["capacities"],
        state.get("capacities"),
        category="capacities",
        stage=stage,
        violations=violations,
    )
    meaning_fields = (
        "team",
        "authority_role_id",
        "unit",
        "window",
        "constraint_kind",
        "status",
        "follow_up_sla_business_days",
    )
    for item_id in expected.keys() & actual.keys():
        wanted = expected[item_id]
        found = actual[item_id]
        if found.get("limit") != wanted["limit"]:
            violations.append(
                Violation(
                    "CAPACITY_VALUE_CHANGED",
                    stage,
                    item_id,
                    f"limite atteso {wanted['limit']!r}, trovato {found.get('limit')!r}",
                )
            )
        changed = [field for field in meaning_fields if field in wanted and found.get(field) != wanted[field]]
        if changed:
            details = ", ".join(
                f"{field}={found.get(field)!r} (atteso {wanted[field]!r})"
                for field in changed
            )
            violations.append(
                Violation(
                    "CAPACITY_MEANING_CHANGED",
                    stage,
                    item_id,
                    f"significato del limite modificato: {details}",
                )
            )


def check_roles(
    contract: dict[str, Any],
    state: dict[str, Any],
    stage: str,
    violations: list[Violation],
) -> None:
    expected, actual = require_items(
        contract["roles"],
        state.get("roles"),
        category="roles",
        stage=stage,
        violations=violations,
    )
    for item_id in expected.keys() & actual.keys():
        wanted = expected[item_id]
        found = actual[item_id]
        found_responsibilities = found.get("responsibilities")
        if not isinstance(found_responsibilities, list) or set(found_responsibilities) != set(
            wanted["responsibilities"]
        ):
            violations.append(
                Violation(
                    "ROLE_RESPONSIBILITY_CHANGED",
                    stage,
                    item_id,
                    "responsabilità diversa da quella stabilita nel contratto",
                )
            )
        for field in ("assignment_state", "authority_state"):
            if found.get(field) != wanted[field]:
                violations.append(
                    Violation(
                        "ROLE_STATE_CHANGED",
                        stage,
                        item_id,
                        f"{field} atteso {wanted[field]!r}, trovato {found.get(field)!r}",
                    )
                )


def check_tracking(
    contract: dict[str, Any],
    state: dict[str, Any],
    stage: str,
    violations: list[Violation],
) -> None:
    expected, actual = require_items(
        contract["tracking"],
        state.get("tracking"),
        category="tracking",
        stage=stage,
        violations=violations,
    )
    for item_id in expected.keys() & actual.keys():
        wanted = expected[item_id]
        found = actual[item_id]
        evidence = found.get("evidence_refs", [])
        if wanted.get("status") == "unverified" and found.get("status") == "verified":
            violations.append(
                Violation(
                    "TRACKING_EARLY_PROMOTION",
                    stage,
                    item_id,
                    "tracking promosso prima del boundary Operations osservato",
                )
            )
        if found.get("status") == "verified" and wanted.get(
            "evidence_required_for_verified"
        ) and not evidence:
            violations.append(
                Violation(
                    "TRACKING_UNSUPPORTED_VERIFICATION",
                    stage,
                    item_id,
                    "tracking dichiarato verificato senza riferimenti a evidenze osservabili",
                )
            )
        elif found.get("status") != wanted["status"]:
            violations.append(
                Violation(
                    "TRACKING_STATE_CHANGED",
                    stage,
                    item_id,
                    f"stato atteso {wanted['status']!r}, trovato {found.get('status')!r}",
                )
            )
        for evidence_ref in evidence if isinstance(evidence, list) else []:
            evidence_path = Path(str(evidence_ref).split("#", 1)[0])
            resolved = (REPO_ROOT / evidence_path).resolve()
            try:
                resolved.relative_to(REPO_ROOT)
            except ValueError:
                resolved_ok = False
            else:
                resolved_ok = resolved.is_file()
            if not resolved_ok:
                violations.append(
                    Violation(
                        "TRACKING_EVIDENCE_UNRESOLVED",
                        stage,
                        item_id,
                        f"evidenza tracking non risolta: {evidence_ref}",
                    )
                )
            elif item_id not in resolved.read_text(encoding="utf-8"):
                violations.append(
                    Violation(
                        "TRACKING_EVIDENCE_UNRESOLVED",
                        stage,
                        item_id,
                        "l'evidenza non contiene l'identificatore tracking dichiarato",
                    )
                )
        uncertainties = found.get("uncertainties", [])
        if not isinstance(uncertainties, list):
            uncertainties = []
        lost = sorted(set(wanted["required_uncertainties"]) - set(uncertainties))
        if lost:
            violations.append(
                Violation(
                    "TRACKING_UNCERTAINTY_LOST",
                    stage,
                    item_id,
                    f"incertezze non più visibili: {', '.join(lost)}",
                )
            )


def check_approvals(
    contract: dict[str, Any],
    state: dict[str, Any],
    stage: str,
    violations: list[Violation],
) -> None:
    expected, actual = require_items(
        contract["approvals"],
        state.get("approvals"),
        category="approvals",
        stage=stage,
        violations=violations,
    )
    for item_id in expected.keys() & actual.keys():
        wanted = expected[item_id]
        found = actual[item_id]
        if wanted["decision_state"] == "proposed" and found.get("decision_state") in {
            "approved",
            "confirmed",
            "executed",
        }:
            violations.append(
                Violation(
                    "APPROVAL_PROPOSAL_PROMOTED",
                    stage,
                    item_id,
                    f"proposta trasformata in {found.get('decision_state')!r}",
                )
            )
        elif found.get("decision_state") != wanted["decision_state"]:
            violations.append(
                Violation(
                    "APPROVAL_DECISION_CHANGED",
                    stage,
                    item_id,
                    f"decision_state atteso {wanted['decision_state']!r}, trovato {found.get('decision_state')!r}",
                )
            )

        if wanted["authorization_state"] in {"missing", "not_authorized"} and found.get(
            "authorization_state"
        ) == "authorized":
            violations.append(
                Violation(
                    "APPROVAL_AUTHORITY_INVENTED",
                    stage,
                    item_id,
                    "autorizzazione mancante trasformata in autorizzata",
                )
            )
        elif found.get("authorization_state") != wanted["authorization_state"]:
            violations.append(
                Violation(
                    "APPROVAL_AUTHORIZATION_CHANGED",
                    stage,
                    item_id,
                    f"authorization_state atteso {wanted['authorization_state']!r}, trovato {found.get('authorization_state')!r}",
                )
            )

        if found.get("fact_state") != wanted["fact_state"]:
            violations.append(
                Violation(
                    "APPROVAL_FACT_CHANGED",
                    stage,
                    item_id,
                    f"fact_state atteso {wanted['fact_state']!r}, trovato {found.get('fact_state')!r}",
                )
            )


def validate(contract: dict[str, Any], case: dict[str, Any]) -> list[Violation]:
    violations: list[Violation] = []
    if contract.get("schema_version") != 1 or case.get("schema_version") != 1:
        violations.append(
            Violation(
                "SCHEMA_VERSION",
                "case",
                "",
                "contract e case devono usare schema_version 1",
            )
        )
        return violations
    if case.get("case_id") != contract.get("case_id"):
        violations.append(
            Violation(
                "CASE_ID_MISMATCH",
                "case",
                "",
                f"case_id atteso {contract.get('case_id')!r}, trovato {case.get('case_id')!r}",
            )
        )
    if contract.get("profile") != "preexecution-static-v1" or case.get("profile") != contract.get("profile"):
        violations.append(Violation("PROFILE_MISMATCH", "case", "profile", "profilo statico pre-execution mancante o divergente"))
    if case.get("shared_invariant_ids") != contract.get("shared_invariant_ids"):
        violations.append(Violation("SHARED_INVARIANT_IDS", "case", "shared_invariant_ids", "identificatori condivisi divergenti"))

    handoffs = case.get("handoffs")
    if not isinstance(handoffs, list):
        return violations + [
            Violation("INVALID_COLLECTION", "case", "handoffs", "deve essere una lista")
        ]

    expected_stages = contract["stages"]
    actual_stages = [item.get("stage") for item in handoffs if isinstance(item, dict)]
    if actual_stages != expected_stages:
        violations.append(
            Violation(
                "HANDOFF_STAGE_SEQUENCE",
                "case",
                "handoffs",
                f"sequenza attesa {expected_stages!r}, trovata {actual_stages!r}",
            )
        )

    seen_handoff_ids: set[str] = set()
    previous_id: str | None = None
    for index, handoff in enumerate(handoffs):
        if not isinstance(handoff, dict):
            violations.append(
                Violation("INVALID_ITEM", f"handoff-{index + 1}", "", "handoff non oggetto")
            )
            continue
        stage = str(handoff.get("stage", f"handoff-{index + 1}"))
        handoff_id = handoff.get("handoff_id")
        if not isinstance(handoff_id, str) or handoff_id in seen_handoff_ids:
            violations.append(
                Violation("HANDOFF_ID", stage, "", "handoff_id mancante o duplicato")
            )
        else:
            seen_handoff_ids.add(handoff_id)
        if handoff.get("sequence") != index + 1:
            violations.append(
                Violation(
                    "HANDOFF_SEQUENCE",
                    stage,
                    str(handoff_id or ""),
                    f"sequence attesa {index + 1}, trovata {handoff.get('sequence')!r}",
                )
            )
        if handoff.get("previous_handoff_id") != previous_id:
            violations.append(
                Violation(
                    "HANDOFF_PREVIOUS_MISMATCH",
                    stage,
                    str(handoff_id or ""),
                    f"previous_handoff_id atteso {previous_id!r}, trovato {handoff.get('previous_handoff_id')!r}",
                )
            )
        previous_id = handoff_id if isinstance(handoff_id, str) else previous_id

        state = handoff.get("state")
        if not isinstance(state, dict):
            violations.append(
                Violation("INVALID_ITEM", stage, "state", "state deve essere un oggetto")
            )
            continue
        check_claims(contract, state, stage, violations)
        check_testimonials(contract, state, stage, violations)
        check_capacities(contract, state, stage, violations)
        check_roles(contract, state, stage, violations)
        check_tracking(contract, state, stage, violations)
        check_approvals(contract, state, stage, violations)
    return violations


def replace_json_pointer(document: Any, pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError(f"JSON pointer non valido: {pointer}")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    current = document
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    last = parts[-1]
    if isinstance(current, list):
        current[int(last)] = value
    else:
        current[last] = value


def run_self_test() -> int:
    contract = load_json(DEFAULT_CONTRACT)
    positive = load_json(DEFAULT_CASE)
    positive_violations = validate(contract, positive)
    failures: list[str] = []

    if positive_violations:
        failures.append("caso positivo non valido")
        failures.extend(f"  {item.render()}" for item in positive_violations)
    else:
        print("PASS positive/fabriloom-preexecution-cross-core-v2")

    matrix = load_json(DEFAULT_NEGATIVE)
    for negative in matrix.get("cases", []):
        mutated = copy.deepcopy(positive)
        replace_json_pointer(mutated, negative["pointer"], negative["value"])
        violations = validate(contract, mutated)
        codes = {item.code for item in violations}
        expected_codes = set(negative["expected_rule_ids"])
        if expected_codes != codes:
            failures.append(
                f"{negative['id']}: attesi {sorted(expected_codes)}, ottenuti {sorted(codes)}"
            )
        else:
            print(f"PASS negative/{negative['id']} -> {', '.join(sorted(expected_codes))}")

    if failures:
        print("\nSELF-TEST FAIL", file=sys.stderr)
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print(f"\nSELF-TEST PASS: 1 positivo, {len(matrix.get('cases', []))} negativi")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Verifica invarianti semantici lungo handoff AMS cross-Core."
    )
    parser.add_argument("--contract", type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument("--case", type=Path, default=DEFAULT_CASE)
    parser.add_argument("--self-test", action="store_true")
    parser.add_argument("--json", action="store_true", dest="json_output")
    args = parser.parse_args()

    try:
        if args.self_test:
            return run_self_test()
        violations = validate(load_json(args.contract), load_json(args.case))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"CHECKER_ERROR: {exc}", file=sys.stderr)
        return 2

    if args.json_output:
        print(
            json.dumps(
                {
                    "pass": not violations,
                    "violations": [item.__dict__ for item in violations],
                },
                ensure_ascii=False,
                indent=2,
            )
        )
    elif violations:
        print(f"FAIL: {len(violations)} violazione/i", file=sys.stderr)
        for violation in violations:
            print(violation.render(), file=sys.stderr)
    else:
        print("PASS: invarianti cross-Core conservati in tutti gli handoff")
    return 1 if violations else 0


if __name__ == "__main__":
    sys.exit(main())
