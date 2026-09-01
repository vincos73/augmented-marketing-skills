#!/usr/bin/env python3
"""Validate authorization ledgers, role authority and persistent identity chains."""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any


EVAL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = EVAL_ROOT.parents[1]
TRANSITIONS = {"content_approval": "approve_content", "saving": "write_file", "installation": "install", "execution": "execute"}
MATRIX = {
    "approve_content": ["Marketing Director"],
    "write_file": ["Repository Maintainer"],
    "install": ["Runtime Administrator"],
    "execute": ["Campaign Operator"],
}
SHARED_IDS = [
    "speed-60",
    "speed-42-conditional",
    "pilot-quote-01",
    "operations-total-sprints",
    "operations-weekly-starts",
    "sales-weekly-qualified-calls",
    "TRK-FAB-ERS-OWNED@1",
    "paid-media",
]
DIGEST = re.compile(r"^[0-9a-f]{64}$")
ACTIVE = {"approved", "authorized", "denied"}
ACTION_BLOCKED = {"denied", "not_requested", "not_applicable", "unknown"}


def issue(rule: str, location: str, message: str) -> dict[str, str]:
    return {"rule_id": rule, "location": location, "message": message}


def inside(path: Path, root: Path) -> bool:
    try:
        path.relative_to(root)
        return True
    except ValueError:
        return False


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def valid_datetime(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False


def apply_replace(document: Any, pointer: str, value: Any) -> None:
    tokens = [token.replace("~1", "/").replace("~0", "~") for token in pointer.removeprefix("/").split("/")]
    cursor = document
    for token in tokens[:-1]:
        cursor = cursor[int(token)] if isinstance(cursor, list) else cursor[token]
    final = tokens[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = copy.deepcopy(value)
    else:
        if final not in cursor:
            raise KeyError(pointer)
        cursor[final] = copy.deepcopy(value)


def load_ledger(path: Path) -> tuple[dict[str, Any], Path]:
    resolved = path.resolve()
    if not inside(resolved, EVAL_ROOT):
        raise ValueError(f"fixture fuori dal perimetro eval: {resolved}")
    data = read_json(resolved)
    if not isinstance(data, dict):
        raise ValueError("ledger non oggetto")
    if "base" not in data:
        return data, resolved
    if set(data) != {"base", "mutations"} or not isinstance(data["mutations"], list):
        raise ValueError("fixture derivata non valida")
    base = (resolved.parent / data["base"]).resolve()
    if not inside(base, EVAL_ROOT):
        raise ValueError("base fuori dal perimetro eval")
    ledger = read_json(base)
    for mutation in data["mutations"]:
        if set(mutation) != {"op", "path", "value"} or mutation["op"] != "replace":
            raise ValueError("mutazione non valida")
        apply_replace(ledger, mutation["path"], mutation["value"])
    return ledger, resolved


def exact(value: Any, keys: set[str], location: str, errors: list[dict[str, str]]) -> bool:
    if not isinstance(value, dict) or set(value) != keys:
        errors.append(issue("L001", location, f"campi attesi: {', '.join(sorted(keys))}"))
        return False
    return True


def validate_structure(ledger: Any) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    root = {"schema_version", "ledger_id", "profile", "identity", "shared_invariant_ids", "role_action_matrix", "evaluation_context", "records"}
    if not exact(ledger, root, "$", errors):
        return errors
    if ledger["schema_version"] != "2.0.0" or ledger["profile"] not in {"chat-v1", "persistent-lineage-v1"}:
        errors.append(issue("L001", "$.schema_version", "versione o profilo non supportati"))
    if not exact(ledger["identity"], {"id", "version", "state"}, "$.identity", errors):
        return errors
    if ledger["role_action_matrix"] != MATRIX:
        errors.append(issue("L013", "$.role_action_matrix", "matrice ruolo-azione incompleta o modificata"))
    if ledger["shared_invariant_ids"] != SHARED_IDS:
        errors.append(issue("L001", "$.shared_invariant_ids", "identificatori condivisi divergenti"))
    context = ledger["evaluation_context"]
    if exact(context, {"mode", "fixture", "generated_at"}, "$.evaluation_context", errors):
        if context["mode"] not in {"simulation", "live", "review"} or not valid_datetime(context["generated_at"]):
            errors.append(issue("L001", "$.evaluation_context", "contesto non valido"))
    records = ledger["records"]
    if not isinstance(records, list) or len(records) != 4:
        errors.append(issue("L002", "$.records", "servono esattamente quattro transizioni"))
        return errors
    record_keys = {"id", "transition", "entity", "version", "scope", "decision", "authority", "observation", "recorded_at", "dependencies", "notes"}
    for index, record in enumerate(records):
        loc = f"$.records[{index}]"
        if not exact(record, record_keys, loc, errors):
            continue
        if record["transition"] not in TRANSITIONS:
            errors.append(issue("L001", f"{loc}.transition", "transizione non valida"))
        entity = record["entity"]
        if exact(entity, {"id", "type", "path", "digest"}, f"{loc}.entity", errors):
            if not isinstance(entity["id"], str) or not entity["id"] or not isinstance(entity["type"], str) or not entity["type"]:
                errors.append(issue("L001", f"{loc}.entity", "identità entità mancante"))
            if entity["path"] is not None and not isinstance(entity["path"], str):
                errors.append(issue("L001", f"{loc}.entity.path", "path deve essere stringa o null"))
            if entity["digest"] is not None and (not isinstance(entity["digest"], str) or not DIGEST.fullmatch(entity["digest"])):
                errors.append(issue("L001", f"{loc}.entity.digest", "digest deve essere SHA-256 o null"))
        version = record["version"]
        if exact(version, {"kind", "value"}, f"{loc}.version", errors) and version["kind"] not in {"conversational", "persistent"}:
            errors.append(issue("L001", f"{loc}.version.kind", "version kind non valido"))
        scope = record["scope"]
        if exact(scope, {"actions", "targets", "exclusions"}, f"{loc}.scope", errors):
            if scope["actions"] != [TRANSITIONS.get(record["transition"])]:
                errors.append(issue("L004", f"{loc}.scope.actions", "scope azione non isolato"))
            for field in ("targets", "exclusions"):
                if not isinstance(scope[field], list) or any(not isinstance(item, str) for item in scope[field]):
                    errors.append(issue("L001", f"{loc}.scope.{field}", "atteso array di stringhe"))
        decision = record["decision"]
        if exact(decision, {"status", "mode", "basis"}, f"{loc}.decision", errors):
            if decision["status"] not in {"not_requested", "approved", "authorized", "denied", "not_applicable", "unknown"} or decision["mode"] not in {"observed", "simulated", "not_applicable", "unknown"}:
                errors.append(issue("L001", f"{loc}.decision", "decisione non valida"))
            exact(decision["basis"], {"kind", "source_entry_id", "summary"}, f"{loc}.decision.basis", errors)
        authority = record["authority"]
        if exact(authority, {"status", "role"}, f"{loc}.authority", errors) and authority["status"] not in {"confirmed", "to_confirm", "not_applicable", "unknown"}:
            errors.append(issue("L001", f"{loc}.authority.status", "stato autorità non valido"))
        observation = record["observation"]
        if exact(observation, {"subject", "status", "occurred_at", "evidence"}, f"{loc}.observation", errors):
            if observation["subject"] not in {"decision", "action"} or observation["status"] not in {"observed", "not_observed", "not_applicable", "unknown"}:
                errors.append(issue("L001", f"{loc}.observation", "osservazione non valida"))
            if observation["occurred_at"] is not None and not valid_datetime(observation["occurred_at"]):
                errors.append(issue("L001", f"{loc}.observation.occurred_at", "date-time non valido"))
            if not isinstance(observation["evidence"], list):
                errors.append(issue("L001", f"{loc}.observation.evidence", "atteso array"))
            else:
                for evidence_index, evidence in enumerate(observation["evidence"]):
                    evidence_loc = f"{loc}.observation.evidence[{evidence_index}]"
                    if exact(evidence, {"kind", "mode", "ref", "summary"}, evidence_loc, errors):
                        if evidence["kind"] not in {"message", "file", "receipt", "log", "policy"} or evidence["mode"] not in {"observed", "simulated"}:
                            errors.append(issue("L001", evidence_loc, "evidenza non valida"))
        if not valid_datetime(record["recorded_at"]):
            errors.append(issue("L001", f"{loc}.recorded_at", "date-time non valido"))
        if not isinstance(record["dependencies"], list) or not isinstance(record["notes"], list):
            errors.append(issue("L001", loc, "dependencies e notes devono essere array"))
    return errors


def validate_coherence(ledger: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    records = ledger["records"]
    transitions = [record["transition"] for record in records]
    if transitions != ["content_approval", "saving", "installation", "execution"]:
        errors.append(issue("L002", "$.records", "ordine transizioni non valido"))
    by_transition = {record["transition"]: record for record in records}
    ids = {record["id"] for record in records}
    if len(ids) != 4:
        errors.append(issue("L011", "$.records", "id record non univoci"))

    for index, record in enumerate(records):
        loc = f"$.records[{index}]"
        transition = record["transition"]
        decision = record["decision"]
        observation = record["observation"]
        basis = decision["basis"]
        action = TRANSITIONS[transition]
        allowed_roles = ledger["role_action_matrix"].get(action, [])
        if decision["status"] in ACTIVE and (record["authority"]["status"] != "confirmed" or record["authority"]["role"] not in allowed_roles):
            errors.append(issue("L013", f"{loc}.authority", f"ruolo non autorizzato per {action}"))
        if transition == "content_approval" and decision["status"] == "authorized":
            errors.append(issue("L003", f"{loc}.decision.status", "il contenuto usa approved"))
        if transition != "content_approval" and decision["status"] == "approved":
            errors.append(issue("L003", f"{loc}.decision.status", "le azioni usano authorized"))
        if observation["subject"] != ("decision" if transition == "content_approval" else "action"):
            errors.append(issue("L010", f"{loc}.observation.subject", "subject non coerente con la transizione"))
        if observation["subject"] == "action" and observation["status"] == "observed" and decision["status"] != "authorized":
            errors.append(issue("L003", f"{loc}.observation.status", "azione osservata senza autorizzazione propria"))
        if decision["status"] in ACTION_BLOCKED and observation["subject"] == "action" and observation["status"] not in {"not_observed", "not_applicable"}:
            errors.append(issue("L003", f"{loc}.observation.status", "azione negata o non richiesta marcata osservata"))
        if observation["status"] == "observed" and (observation["occurred_at"] is None or not observation["evidence"]):
            errors.append(issue("L010", f"{loc}.observation", "osservazione senza tempo o evidenza"))
        if observation["status"] != "observed" and observation["occurred_at"] is not None:
            errors.append(issue("L010", f"{loc}.observation.occurred_at", "azione non osservata con timestamp"))
        if basis["kind"] == "inherited" or basis["source_entry_id"] is not None:
            errors.append(issue("L006", f"{loc}.decision.basis", "autorità ereditata da altro passaggio"))
        evidence_modes = {item["mode"] for item in observation["evidence"]}
        if (decision["mode"] == "simulated") != (basis["kind"] == "simulated") or (decision["mode"] == "simulated" and "observed" in evidence_modes):
            errors.append(issue("L007", f"{loc}.decision", "provenienza simulata non conservata"))
        for dependency in record["dependencies"]:
            if dependency not in ids or dependency == record["id"]:
                errors.append(issue("L011", f"{loc}.dependencies", "dipendenza non risolta"))
        for evidence in observation["evidence"]:
            if evidence["kind"] in {"file", "receipt", "log"}:
                ref_path = Path(evidence["ref"].split("#", 1)[0])
                resolved = (REPO_ROOT / ref_path).resolve()
                if ref_path.is_absolute() or not inside(resolved, REPO_ROOT) or not resolved.is_file():
                    errors.append(issue("L012", f"{loc}.observation.evidence", "evidenza file non risolta"))

        entity = record["entity"]
        version = record["version"]
        if version["kind"] == "persistent":
            raw_path = entity["path"]
            artifact = (REPO_ROOT / raw_path).resolve() if isinstance(raw_path, str) else None
            if artifact is None or Path(raw_path).is_absolute() or not inside(artifact, REPO_ROOT) or not artifact.is_file() or not isinstance(entity["digest"], str):
                errors.append(issue("L008", f"{loc}.entity", "artefatto persistente richiede path e digest risolvibili"))
            elif hashlib.sha256(artifact.read_bytes()).hexdigest() != entity["digest"]:
                errors.append(issue("L008", f"{loc}.entity.digest", "digest dichiarato non corrisponde al file"))
        elif entity["path"] is not None or entity["digest"] is not None:
            errors.append(issue("L014", f"{loc}.entity", "artefatto conversazionale/non creato richiede path e digest null"))

    profile = ledger["profile"]
    if profile == "chat-v1":
        if ledger["identity"] != {"id": "SPEC-FAB-ERS", "version": "chat-v1", "state": "confirmed_in_chat"}:
            errors.append(issue("L014", "$.identity", "identità chat-v1 non separata dagli artefatti persistenti"))
        for index, record in enumerate(records):
            if record["version"] != {"kind": "conversational", "value": "chat-v1"} or record["entity"]["path"] is not None or record["entity"]["digest"] is not None:
                errors.append(issue("L014", f"$.records[{index}]", "ledger chat-v1 deve rappresentare artefatti non creati con digest null"))
    else:
        expected_identity = {"id": "SPEC-FAB-ERS", "version": "SPEC-FAB-ERS@1", "state": "persistent"}
        if ledger["identity"] != expected_identity:
            errors.append(issue("L009", "$.identity", "identità persistente non valida"))
        chain = [by_transition[name] for name in ("saving", "installation", "execution")]
        signature = lambda record: (record["entity"]["id"], record["version"]["value"], record["entity"]["path"], record["entity"]["digest"])
        if len({signature(record) for record in chain}) != 1 or any(record["version"]["kind"] != "persistent" for record in chain):
            errors.append(issue("L009", "$.records", "catena save-install-execute non conserva identity/version/path/digest"))
        if chain[0]["id"] not in chain[1]["dependencies"] or chain[1]["id"] not in chain[2]["dependencies"]:
            errors.append(issue("L009", "$.records", "dipendenze save-install-execute incomplete"))
    return errors


def validate(path: Path) -> dict[str, Any]:
    try:
        ledger, source = load_ledger(path)
        errors = validate_structure(ledger)
        if not errors:
            errors.extend(validate_coherence(ledger))
        return {"path": str(source.relative_to(REPO_ROOT)), "ledger_id": ledger.get("ledger_id"), "pass": not errors, "rule_ids": sorted({item["rule_id"] for item in errors}), "issues": errors}
    except (OSError, ValueError, KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        return {"path": str(path), "ledger_id": None, "pass": False, "rule_ids": ["L001"], "issues": [issue("L001", "$", str(exc))]}


def run_oracle(path: Path) -> tuple[dict[str, Any], bool]:
    oracle = read_json(path)
    results = []
    passed = True
    for case in oracle["cases"]:
        result = validate((path.parent / case["path"]).resolve())
        actual = "pass" if result["pass"] else "fail"
        wanted = sorted(case["expected_rule_ids"])
        matched = actual == case["expected"] and wanted == result["rule_ids"]
        passed = passed and matched
        results.append({"id": case["id"], "expected": case["expected"], "actual": actual, "expected_rule_ids": wanted, "actual_rule_ids": result["rule_ids"], "oracle_match": matched})
    return {"oracle": str(path.relative_to(REPO_ROOT)), "oracle_version": oracle["oracle_version"], "pass": passed, "cases": results}, passed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("ledger", nargs="?", type=Path)
    parser.add_argument("--oracle", type=Path)
    args = parser.parse_args()
    if bool(args.ledger) == bool(args.oracle):
        parser.error("specificare un ledger oppure --oracle")
    result, passed = run_oracle(args.oracle.resolve()) if args.oracle else (validate(args.ledger.resolve()), None)
    if passed is None:
        passed = result["pass"]
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    sys.exit(main())
