#!/usr/bin/env python3
"""Validate compact Campaign Review baselines handed to Campaign Debrief."""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CASES = ROOT / "cases.json"


def issue(rule: str, location: str, message: str) -> dict[str, str]:
    return {"rule_id": rule, "location": location, "message": message}


def normalize(value: Any) -> Any:
    if value is None:
        return "missing"
    if isinstance(value, dict):
        return {key: normalize(item) for key, item in value.items()}
    if isinstance(value, list):
        return [normalize(item) for item in value]
    return copy.deepcopy(value)


def compare(actual: Any, expected: Any, location: str, errors: list[dict[str, str]]) -> None:
    if expected == "missing" and actual != "missing":
        errors.append(issue("C003", location, "valore assente nella fonte inventato nel passaggio"))
    elif actual != expected:
        errors.append(issue("C002", location, "valore del passaggio divergente dalla fonte osservata"))


def expected_descriptive_comparison(spec: dict[str, Any]) -> dict[str, Any]:
    if spec.get("target") is None:
        return {"status": "unavailable", "requires": ["target"], "reason": "target_missing"}
    if spec.get("operational_definition") is None:
        return {"status": "unavailable", "requires": ["operational_definition"], "reason": "operational_definition_missing"}
    if spec.get("window") is None and spec.get("maturity") is None:
        return {"status": "unavailable", "requires": ["window_or_maturity"], "reason": "window_and_maturity_missing"}
    return {"status": "prepared", "requires": ["mature_observed_results"], "reason": None}


def expected_incremental_comparison(spec: dict[str, Any]) -> dict[str, Any]:
    baseline = spec.get("baseline", {})
    comparator = spec.get("comparator", {})
    if not isinstance(baseline, dict) or baseline.get("value") is None or not isinstance(comparator, dict) or comparator.get("value") is None:
        return {"status": "unavailable", "reason": "baseline_and_comparator_missing"}
    if baseline.get("state") in {"observed_non_comparable", "not_comparable", "unknown"}:
        return {"status": "unavailable", "reason": "baseline_not_comparable"}
    return {"status": "prepared", "reason": None}


def validate_case(case: dict[str, Any], contract: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    source = case.get("source")
    capsule = case.get("capsule")
    required = set(contract["required_capsule_fields"])
    if not isinstance(source, dict) or not isinstance(capsule, dict) or set(capsule) != required:
        return [issue("C001", "$", "source o forma della capsule non valida")]
    if source.get("next_step") != contract["next_step"] or capsule.get("mode") != "internal_compact":
        errors.append(issue("C001", "$.source.next_step", "capsule ammessa soltanto per campaign-debrief e in modalità compatta"))
    spec = source.get("campaign_spec")
    review = source.get("review")
    if not isinstance(spec, dict) or not isinstance(review, dict):
        return errors + [issue("C001", "$.source", "Campaign Spec o review mancante")]

    decision_metric = spec.get("decision_metric")
    objective = spec.get("objective")
    objective_or_metric = decision_metric if decision_metric is not None else objective
    expected_values = {
        "campaign_spec_identity": normalize(spec.get("identity")),
        "objective_or_decision_metric": normalize(objective_or_metric),
        "operational_definition": normalize(spec.get("operational_definition")),
        "target": normalize(spec.get("target")),
        "window": normalize(spec.get("window")),
        "cutoff": normalize(spec.get("cutoff")),
        "maturity": normalize(spec.get("maturity")),
        "baseline": normalize(spec.get("baseline")),
        "comparator": normalize(spec.get("comparator")),
        "assets": normalize(spec.get("assets")),
        "verdict": normalize(review.get("verdict")),
        "open_findings": normalize(review.get("open_findings")),
        "authorization_decision": normalize(review.get("authorization_decision")),
        "execution_observation": normalize(review.get("execution_observation")),
        "evidence_refs": list(dict.fromkeys(spec.get("evidence_refs", []) + review.get("evidence_refs", []))),
        "unknowns": normalize(review.get("unknowns")),
    }
    for field, expected in expected_values.items():
        compare(capsule.get(field), expected, f"$.capsule.{field}", errors)
    descriptive_expected = expected_descriptive_comparison(spec)
    if capsule.get("descriptive_target_comparison") != descriptive_expected:
        errors.append(issue("C005", "$.capsule.descriptive_target_comparison", "confronto descrittivo con target o regola non predisposto correttamente"))
    incremental_expected = expected_incremental_comparison(spec)
    if capsule.get("incremental_causal_comparison") != incremental_expected:
        errors.append(issue("C007", "$.capsule.incremental_causal_comparison", "confronto incrementale o causale non distinto dalla verifica del target"))
    if capsule.get("authorization_decision") == capsule.get("execution_observation") or capsule.get("execution_observation", {}).get("status") in {"authorized", "approved"}:
        errors.append(issue("C004", "$.capsule.execution_observation", "decisione di autorizzazione usata come osservazione dell'esecuzione"))
    missing_fields = {
        name for name in ("target", "window", "cutoff", "maturity")
        if expected_values[name] == "missing"
    }
    if not missing_fields.issubset(set(capsule.get("unknowns", []))):
        errors.append(issue("C006", "$.capsule.unknowns", "campo missing non conservato tra gli unknowns"))
    return errors


def replace(document: Any, pointer: str, value: Any) -> None:
    tokens = pointer.removeprefix("/").split("/")
    cursor = document
    for token in tokens[:-1]:
        cursor = cursor[int(token)] if isinstance(cursor, list) else cursor[token]
    final = tokens[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = copy.deepcopy(value)
    else:
        cursor[final] = copy.deepcopy(value)


def main() -> int:
    data = json.loads(CASES.read_text(encoding="utf-8"))
    if data.get("schema_version") != "1.0.0":
        print("FAIL C001: schema_version non valida", file=sys.stderr)
        return 1
    contract = data["contract"]
    cases = data["cases"]
    wanted_ids = ["qualified-requests-six-week-window", "missing-target-remains-missing", "qualitative-success-rule-with-maturity"]
    if [case.get("id") for case in cases] != wanted_ids:
        print("FAIL C001: servono esattamente i tre scenari pubblicabili", file=sys.stderr)
        return 1
    failures: list[str] = []
    by_id = {case["id"]: case for case in cases}
    for case in cases:
        errors = validate_case(case, contract)
        if errors:
            failures.append(f"positive/{case['id']}: {sorted({item['rule_id'] for item in errors})}")
        else:
            print(f"PASS positive/{case['id']}")
    for negative in data["negative_cases"]:
        case = copy.deepcopy(by_id[negative["base_case"]])
        replace(case, negative["path"], negative["value"])
        actual = sorted({item["rule_id"] for item in validate_case(case, contract)})
        expected = sorted(negative["expected_rule_ids"])
        if actual != expected:
            failures.append(f"negative/{negative['id']}: attesi {expected}, osservati {actual}")
        else:
            print(f"PASS negative/{negative['id']} -> {', '.join(actual)}")
    if failures:
        for failure in failures:
            print(f"FAIL {failure}", file=sys.stderr)
        return 1
    print(f"SELF-TEST PASS: {len(cases)} positivi, {len(data['negative_cases'])} negativi")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
