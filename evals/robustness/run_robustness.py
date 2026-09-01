#!/usr/bin/env python3
"""Run AMS robustness gates; behavioral evidence is required unless --static-only."""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


EVALS = Path(__file__).resolve().parents[1]
REPO = EVALS.parent
E2E = EVALS / "end-to-end" / "fabriloom-evidence-readiness"
LINEAGE = EVALS / "campaign-lineage" / "fabriloom-evidence-readiness"
RAW = EVALS / "raw-to-snapshot"
PROVENANCE = EVALS / "behavioral-provenance"
REVIEW_CAPSULE = EVALS / "campaign-review" / "baseline-decision-capsule"
ROBUSTNESS = EVALS / "robustness"
READINESS = ROBUSTNESS / "runtime-readiness"
FORBIDDEN_PATH_TOKENS = {"oracle", "oracles", "fixture", "fixtures", "positive", "expected", "regression", "regressions"}


def command(args: list[str], expected: int = 0) -> tuple[bool, str, dict[str, Any] | None]:
    env = os.environ.copy()
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    result = subprocess.run(args, cwd=REPO, env=env, capture_output=True, text=True)
    output = (result.stdout + result.stderr).strip()
    parsed = None
    try:
        parsed = json.loads(result.stdout) if result.stdout.strip() else None
    except json.JSONDecodeError:
        pass
    detail = output[-1200:] if output else f"exit {result.returncode}"
    return result.returncode == expected, detail, parsed


def gate(identifier: str, passed: bool, detail: str, rule_ids: list[str] | None = None) -> dict[str, Any]:
    return {"id": identifier, "state": "pass" if passed else "fail", "rule_ids": sorted(set(rule_ids or [])), "detail": detail}


def not_run(identifier: str, detail: str) -> dict[str, Any]:
    return {"id": identifier, "state": "not_run", "rule_ids": [], "detail": detail}


def rules(parsed: dict[str, Any] | None, fallback: str) -> list[str]:
    if isinstance(parsed, dict) and isinstance(parsed.get("rule_ids"), list):
        return [str(item) for item in parsed["rule_ids"]]
    return [fallback]


def safe_behavior_path(path: Path, label: str) -> tuple[bool, str]:
    resolved = path.resolve()
    if not resolved.is_file():
        return False, f"{label} mancante: {resolved}"
    try:
        resolved.relative_to(REPO)
    except ValueError:
        pass
    else:
        return False, f"{label} deve provenire da un run esterno al repository: {resolved}"
    suspicious = {part.casefold() for part in resolved.parts}
    if any(any(token in part for token in FORBIDDEN_PATH_TOKENS) for part in suspicious):
        return False, f"{label} punta a oracle, fixture positiva, regressione o output expected: {resolved}"
    return True, str(resolved)


def readiness_checker_args(evidence_index: Path | None = None) -> list[str]:
    args = ["python3", str(READINESS / "scripts/check_readiness.py")]
    if evidence_index is not None:
        args.extend(["--external-evidence-index", str(evidence_index.resolve())])
    return args


def run_static_gates(readiness_evidence_index: Path | None = None) -> list[dict[str, Any]]:
    checks: list[dict[str, Any]] = []

    ok_fixture, detail_fixture, _ = command(["python3", str(E2E / "scripts/check_fixture.py"), "--fixture", str(E2E)])
    ok_boundary, detail_boundary, _ = command(["python3", str(ROBUSTNESS / "scripts/check_input_boundary.py")])
    checks.append(gate("FIXTURE_VALID", ok_fixture and ok_boundary, f"fixture={detail_fixture}; input_boundary={detail_boundary}", [] if ok_fixture and ok_boundary else ["F001"]))

    ok_lineage, detail_lineage, _ = command(["python3", str(LINEAGE / "scripts/check_lineage.py")])
    ok_bridge, detail_bridge, _ = command(["python3", str(ROBUSTNESS / "fabriloom-nine-step" / "scripts/check_bridge.py")])
    checks.append(gate("LINEAGE_PASS", ok_lineage and ok_bridge, f"lineage={detail_lineage}; static_boundary={detail_bridge}", [] if ok_lineage and ok_bridge else ["LNG001"]))

    ok_invariants, detail_invariants, _ = command(["python3", str(EVALS / "cross-core-safety" / "scripts/check_cross_core.py"), "--self-test"])
    checks.append(gate("INVARIANTS_PASS", ok_invariants, detail_invariants, [] if ok_invariants else ["INV001"]))

    ok_capsule, detail_capsule, _ = command(["python3", str(REVIEW_CAPSULE / "scripts/check_capsule.py")])
    checks.append(gate("REVIEW_BASELINE_PASS", ok_capsule, detail_capsule, [] if ok_capsule else ["C001"]))

    ok_ledger, detail_ledger, ledger_json = command(["python3", str(EVALS / "authorization-ledger" / "scripts/check_ledger.py"), "--oracle", str(EVALS / "authorization-ledger" / "oracles/cases.json")])
    checks.append(gate("AUTHORITY_PASS", ok_ledger, detail_ledger, [] if ok_ledger else rules(ledger_json, "AUTH001")))

    ok_chat, detail_chat, chat_json = command(["python3", str(EVALS / "common/scripts/check_state_contract.py"), str(EVALS / "common/fixtures/chat-v1-empty.json")])
    ok_adapter, detail_adapter, adapter_json = command(["python3", str(RAW / "scripts/check_raw_to_snapshot.py"), "--oracle", str(RAW / "oracles/cases.json")])
    ok_minimum, detail_minimum, _ = command(["python3", str(RAW / "scripts/self_test_minimum_behavior.py")])
    token_path = E2E / "regressions/contradictory-response.md"
    ok_token, detail_token, _ = command([
        "python3", str(RAW / "scripts/check_raw_to_snapshot.py"),
        "--raw", str(token_path),
        "--snapshot", str(RAW / "fixtures/fabriloom-valid/snapshot.json"),
    ], expected=1)
    static_adapter_ok = ok_chat and ok_adapter and ok_minimum and ok_token
    static_rules = [] if static_adapter_ok else sorted(set(rules(chat_json, "S001") + rules(adapter_json, "R001") + ([] if ok_minimum else ["R016"]) + ([] if ok_token else ["R011"])))
    checks.append(gate(
        "ADAPTER_STATIC_REGRESSIONS",
        static_adapter_ok,
        f"chat={detail_chat}; full_profile={detail_adapter}; minimum_profile={detail_minimum}; token_only_rejected={detail_token}",
        static_rules,
    ))

    ok_provenance, detail_provenance, _ = command(["python3", str(PROVENANCE / "scripts/self_test_provenance.py")])
    with tempfile.TemporaryDirectory(prefix="ams-static-copy-") as temp:
        temp_root = Path(temp)
        copied_raw = temp_root / "raw.json"
        copied_snapshot = temp_root / "snapshot.json"
        raw_value = json.loads((RAW / "fixtures/fabriloom-valid/raw-transcript.json").read_text(encoding="utf-8"))
        snapshot_value = json.loads((RAW / "fixtures/fabriloom-valid/snapshot.json").read_text(encoding="utf-8"))
        raw_value["scenario"]["evidence_mode"] = "behavioral_run"
        snapshot_value["scenario"]["evidence_mode"] = "behavioral_run"
        copied_raw.write_text(json.dumps(raw_value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        copied_snapshot.write_text(json.dumps(snapshot_value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        ok_static_copy, detail_static_copy, static_copy_json = command([
            "python3", str(RAW / "scripts/check_raw_to_snapshot.py"),
            "--raw", str(copied_raw), "--snapshot", str(copied_snapshot),
        ], expected=1)
        copy_rules = rules(static_copy_json, "P011")
        exact_static_copy = ok_static_copy and copy_rules == ["P011"]
    provenance_regressions_ok = ok_provenance and exact_static_copy
    provenance_rules = [] if provenance_regressions_ok else sorted(set(([] if ok_provenance else ["P001"]) + ([] if exact_static_copy else copy_rules)))
    checks.append(gate("PROVENANCE_REGRESSIONS", provenance_regressions_ok, f"receipt_regressions={detail_provenance}; external_static_copy={detail_static_copy}", provenance_rules))

    ok_readiness, detail_readiness, readiness_json = command(readiness_checker_args(readiness_evidence_index))
    ok_readiness_selftest, detail_readiness_selftest, _ = command(["python3", str(READINESS / "scripts/self_test_readiness.py")])
    readiness_ok = ok_readiness and ok_readiness_selftest
    readiness_rules = [] if readiness_ok else sorted(set(([] if ok_readiness else rules(readiness_json, "M001")) + ([] if ok_readiness_selftest else ["M001"])))
    checks.append(gate(
        "READINESS_MATRIX_VALID",
        readiness_ok,
        f"matrix={detail_readiness}; self_test={detail_readiness_selftest}",
        readiness_rules,
    ))
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", type=Path, help="raw JSON catturato da un run esterno")
    parser.add_argument("--response", type=Path, help="alias legacy di --raw; deve comunque essere JSON strutturato")
    parser.add_argument("--snapshot", type=Path, help="snapshot JSON prodotto dallo stesso run esterno")
    parser.add_argument("--capture-manifest", type=Path, help="manifest esterno con nove receipt Codex concatenate")
    parser.add_argument("--readiness-evidence-index", type=Path, help="indice esterno per gli stati verified della matrice readiness; distinto dalla capture comportamentale")
    parser.add_argument("--static-only", action="store_true", help="esegue soltanto fixture e regressioni statiche")
    parser.add_argument("--require-behavior", action="store_true", help="compatibilità esplicita; il comportamento è già obbligatorio di default")
    args = parser.parse_args()

    checks = run_static_gates(args.readiness_evidence_index)
    static_pass = all(item["state"] == "pass" for item in checks)

    if args.static_only:
        incompatible = args.raw or args.response or args.snapshot or args.capture_manifest or args.require_behavior
        if incompatible:
            checks.append(gate("RUN_CAPTURED", False, "--static-only non si combina con input comportamentali o --require-behavior", ["B001"]))
            checks.append(not_run("PROVENANCE_VERIFIED", "modalità statica non valida"))
            checks.append(not_run("ADAPTER_GROUNDED", "modalità statica non valida"))
            checks.append(gate("BEHAVIOR_PASS", False, "modalità statica invocata con opzioni incompatibili", ["B001"]))
            passed = False
        else:
            checks.append(not_run("RUN_CAPTURED", "modalità --static-only esplicita"))
            checks.append(not_run("PROVENANCE_VERIFIED", "nessuna capture comportamentale in modalità statica"))
            checks.append(not_run("ADAPTER_GROUNDED", "nessun run comportamentale richiesto in modalità statica"))
            checks.append(not_run("BEHAVIOR_PASS", "la modalità statica non produce una prova comportamentale"))
            passed = static_pass
        print(json.dumps({"mode": "static-only", "pass": passed, "checks": checks}, ensure_ascii=False, indent=2))
        return 0 if passed else 1

    raw_path = args.raw or args.response
    capture_errors: list[str] = []
    if args.raw and args.response:
        capture_errors.append("specificare --raw oppure --response, non entrambi")
    if raw_path is None or args.snapshot is None or args.capture_manifest is None:
        capture_errors.append("il gate comportamentale richiede capture manifest, raw/response e snapshot")
    resolved_raw = raw_path.resolve() if raw_path else None
    resolved_snapshot = args.snapshot.resolve() if args.snapshot else None
    resolved_capture = args.capture_manifest.resolve() if args.capture_manifest else None
    if resolved_raw:
        ok, detail = safe_behavior_path(resolved_raw, "raw/response")
        if not ok:
            capture_errors.append(detail)
    if resolved_snapshot:
        ok, detail = safe_behavior_path(resolved_snapshot, "snapshot")
        if not ok:
            capture_errors.append(detail)
    if resolved_capture:
        ok, detail = safe_behavior_path(resolved_capture, "capture manifest")
        if not ok:
            capture_errors.append(detail)
    captured = not capture_errors
    checks.append(gate("RUN_CAPTURED", captured, "; ".join(capture_errors) if capture_errors else f"capture={resolved_capture}; raw={resolved_raw}; snapshot={resolved_snapshot}", [] if captured else ["B001"]))

    if captured:
        provenance_ok, provenance_detail, provenance_json = command([
            "python3", str(PROVENANCE / "scripts/check_provenance.py"),
            "--capture-manifest", str(resolved_capture),
            "--raw", str(resolved_raw),
            "--snapshot", str(resolved_snapshot),
        ])
        checks.append(gate("PROVENANCE_VERIFIED", provenance_ok, provenance_detail, [] if provenance_ok else rules(provenance_json, "P001")))
    else:
        checks.append(not_run("PROVENANCE_VERIFIED", "capture assente o vietata"))
        provenance_ok = False

    if captured and provenance_ok:
        ok, detail, parsed = command([
            "python3", str(RAW / "scripts/check_raw_to_snapshot.py"),
            "--raw", str(resolved_raw),
            "--snapshot", str(resolved_snapshot),
            "--capture-manifest", str(resolved_capture),
            "--require-behavior",
        ])
        checks.append(gate("ADAPTER_GROUNDED", ok, detail, [] if ok else rules(parsed, "R001")))
        adapter_pass = ok
    else:
        checks.append(not_run("ADAPTER_GROUNDED", "input assenti, vietati o con provenance non verificata"))
        adapter_pass = False

    behavior_pass = static_pass and captured and provenance_ok and adapter_pass
    failed_rules = sorted({rule for item in checks if item["state"] == "fail" for rule in item["rule_ids"]})
    checks.append(gate("BEHAVIOR_PASS", behavior_pass, "intera catena statica e comportamentale verificata" if behavior_pass else "almeno un gate della catena non è passato", [] if behavior_pass else failed_rules or ["B002"]))
    print(json.dumps({"mode": "behavioral", "behavior_required": True, "pass": behavior_pass, "checks": checks}, ensure_ascii=False, indent=2))
    return 0 if behavior_pass else 1


if __name__ == "__main__":
    sys.exit(main())
