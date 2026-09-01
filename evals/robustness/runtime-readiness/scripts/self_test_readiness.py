#!/usr/bin/env python3
"""Exercise readiness false promotions and full ephemeral positive paths."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import shutil
import stat
import subprocess
import tempfile
import warnings
import zipfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[4]
CHECKER = ROOT / "scripts" / "check_readiness.py"
REPORT = ROOT / "candidate-readiness.json"
ALLOWLIST = REPO / "evals/behavioral-provenance/runtime-allowlist.json"
PROVENANCE_SELFTEST = REPO / "evals/behavioral-provenance/scripts/self_test_provenance.py"
RUNNER = REPO / "evals/robustness/run_robustness.py"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def import_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"modulo non caricabile: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def artifact(package_id: str, candidate_id: str, kind: str = "packaged_candidate") -> dict[str, Any]:
    return {"id": package_id, "kind": kind, "source_candidate_id": candidate_id}


def evidence(ref: str, kind: str, verification: str = "external_verified") -> dict[str, str]:
    return {"scope": "external", "kind": kind, "ref": ref, "verification": verification}


def add_index(index: dict[str, Any], ref: str, kind: str, path: Path) -> None:
    index["evidence"].append({"ref": ref, "kind": kind, "path": str(path.resolve()), "sha256": digest(path)})


def update_index(index: dict[str, Any], ref: str, path: Path) -> None:
    entry = next(item for item in index["evidence"] if item["ref"] == ref)
    entry["path"] = str(path.resolve())
    entry["sha256"] = digest(path)


def set_gate(report: dict[str, Any], gate_id: str, state: str, record_ids: list[str]) -> None:
    gate = next(item for item in report["candidate_readiness"]["gates"] if item["id"] == gate_id)
    gate["state"] = state
    gate["evidence_record_ids"] = record_ids


def build_package(root: Path, report: dict[str, Any], allowlist: dict[str, Any]) -> tuple[Path, Path, Path]:
    candidate = report["candidate"]
    candidate_id = candidate["candidate_id"]
    package_id = "ams-next-beta-packaged-candidate-selftest"
    package_root = root / "package-root"
    skills_root = package_root / "skills"
    skills_root.mkdir(parents=True)
    for skill in allowlist["skills"]:
        shutil.copytree(REPO / skill["path"], skills_root / skill["skill_id"])
    package_manifest = {
        "schema_version": "1.0.0",
        "package_id": package_id,
        "source_candidate_id": candidate_id,
        "source_base_commit": candidate["source_base_commit"],
        "suite_version": candidate["suite_base_version"],
        "skills": [
            {key: skill[key] for key in ("sequence", "skill_id", "skill_version", "skill_sha256")}
            for skill in allowlist["skills"]
        ],
    }
    manifest_path = package_root / "manifest.json"
    write(manifest_path, package_manifest)
    archive_path = root / "candidate.zip"
    with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in sorted(item for item in package_root.rglob("*") if item.is_file()):
            archive.write(path, path.relative_to(package_root).as_posix())
    candidate["package_state"] = "packaged_candidate"
    candidate["package"] = {
        "package_id": package_id,
        "artifact_kind": "packaged_candidate",
        "source_candidate_id": candidate_id,
        "manifest_ref": "external://package/manifest",
        "manifest_sha256": digest(manifest_path),
        "archive_sha256": digest(archive_path),
    }
    return package_root, manifest_path, archive_path


def build_candidate_ready(root: Path) -> tuple[dict[str, Any], dict[str, Any], dict[str, Path]]:
    report = copy.deepcopy(load(REPORT))
    allowlist = load(ALLOWLIST)
    candidate = report["candidate"]
    candidate_id = candidate["candidate_id"]
    package_root, package_manifest_path, archive_path = build_package(root, report, allowlist)
    package = candidate["package"]
    package_id = package["package_id"]
    index: dict[str, Any] = {"schema_version": "1.0.0", "evidence": []}
    paths: dict[str, Path] = {"package_root": package_root, "package_manifest": package_manifest_path, "archive": archive_path}

    provenance = import_module("readiness_provenance_builder", PROVENANCE_SELFTEST)
    capture_path, raw_path, snapshot_path = provenance.build_capture(root / "behavioral-capture")
    behavior_ref = "external://behavioral-capture/candidate-nine-skill"
    behavior_proof = root / "behavioral-proof.json"
    write(behavior_proof, {
        "schema_version": "1.0.0", "evidence_kind": "behavioral_capture", "candidate_id": candidate_id,
        "source_base_commit": candidate["source_base_commit"], "candidate_manifest_ref": candidate["candidate_manifest_ref"],
        "candidate_manifest_sha256": digest(ALLOWLIST), "surface_id": "codex-desktop",
        "capture_manifest_path": str(capture_path), "capture_manifest_sha256": digest(capture_path),
        "raw_path": str(raw_path), "raw_sha256": digest(raw_path),
        "snapshot_path": str(snapshot_path), "snapshot_sha256": digest(snapshot_path)
    })
    add_index(index, behavior_ref, "behavioral_capture", behavior_proof)
    paths.update({"behavior_proof": behavior_proof, "capture": capture_path, "raw": raw_path, "snapshot": snapshot_path})

    package_observed_id = "EV-PACKAGE-CANDIDATE-OBSERVED"
    report["evidence_records"].append({
        "id": package_observed_id, "axis": "release", "artifact": artifact(package_id, candidate_id), "surface": None,
        "state": "observed_unverified", "outcome": "pass", "prerequisite_record_ids": ["EV-STATIC-CANDIDATE-REVIEW-013"],
        "evidence": [evidence("external://operator-observation/package-candidate", "manual_observation", "unverified")],
        "observations": {"scenario": "package_candidate_observed"}, "limitations": []
    })
    behavior_id = "EV-CANDIDATE-NINE-SKILL-PROVENANCE"
    report["evidence_records"].append({
        "id": behavior_id, "axis": "behavior",
        "artifact": {"id": candidate_id, "kind": "source_candidate", "source_candidate_id": None},
        "surface": "codex-desktop", "state": "provenance_verified", "outcome": "pass",
        "prerequisite_record_ids": ["EV-STATIC-CANDIDATE-REVIEW-013", "EV-FORWARD-REVIEW-DEBRIEF-COMPACTION"],
        "evidence": [evidence(behavior_ref, "behavioral_capture")],
        "observations": {"scenario": "candidate_nine_skill_verified", "skill_count": 9}, "limitations": []
    })

    issue_ref = "external://issue-register/candidate-package"
    issue_proof = root / "issue-register.json"
    write(issue_proof, {
        "schema_version": "1.0.0", "evidence_kind": "issue_register", "candidate_id": candidate_id,
        "package_id": package_id, "package_archive_sha256": package["archive_sha256"],
        "source_system": "external-issue-tracker-export", "exported_at": "2026-09-01T16:00:00+02:00", "issues": []
    })
    add_index(index, issue_ref, "issue_register", issue_proof)
    issue_id = "EV-CANDIDATE-ISSUE-REGISTER"
    report["evidence_records"].append({
        "id": issue_id, "axis": "release", "artifact": artifact(package_id, candidate_id), "surface": None,
        "state": "provenance_verified", "outcome": "pass",
        "prerequisite_record_ids": ["EV-STATIC-CANDIDATE-REVIEW-013", package_observed_id],
        "evidence": [evidence(issue_ref, "issue_register")],
        "observations": {"release_check": "issue_register", "open_p0": 0, "open_p1": 0}, "limitations": []
    })

    parity_ref = "external://package-parity/candidate-package"
    parity_proof = root / "package-parity.json"
    write(parity_proof, {
        "schema_version": "1.0.0", "evidence_kind": "package_parity", "candidate_id": candidate_id,
        "package_id": package_id, "package_archive_sha256": package["archive_sha256"],
        "source_base_commit": candidate["source_base_commit"], "candidate_manifest_ref": candidate["candidate_manifest_ref"],
        "candidate_manifest_sha256": digest(ALLOWLIST), "package_manifest_ref": package["manifest_ref"],
        "package_root_path": str(package_root.resolve()),
        "package_manifest_path": str(package_manifest_path.resolve()), "package_manifest_sha256": package["manifest_sha256"],
        "verified_at": "2026-09-01T16:10:00+02:00"
    })
    add_index(index, parity_ref, "package_parity", parity_proof)
    checksum_ref = "external://checksum/candidate-package"
    checksum_proof = root / "checksum.json"
    write(checksum_proof, {
        "schema_version": "1.0.0", "evidence_kind": "checksum", "candidate_id": candidate_id,
        "package_id": package_id, "package_archive_sha256": package["archive_sha256"],
        "package_manifest_sha256": package["manifest_sha256"], "package_root_path": str(package_root.resolve()),
        "archive_path": str(archive_path.resolve()), "archive_sha256": package["archive_sha256"],
        "verified_at": "2026-09-01T16:15:00+02:00"
    })
    add_index(index, checksum_ref, "checksum", checksum_proof)
    paths.update({"issue_proof": issue_proof, "parity_proof": parity_proof, "checksum_proof": checksum_proof})
    package_record_id = "EV-CANDIDATE-PACKAGE-INTEGRITY"
    report["evidence_records"].append({
        "id": package_record_id, "axis": "release", "artifact": artifact(package_id, candidate_id), "surface": None,
        "state": "provenance_verified", "outcome": "pass",
        "prerequisite_record_ids": ["EV-STATIC-CANDIDATE-REVIEW-013", package_observed_id],
        "evidence": [evidence(parity_ref, "package_parity"), evidence(checksum_ref, "checksum")],
        "observations": {"release_check": "package_integrity"}, "limitations": []
    })

    set_gate(report, "nine-skill-candidate-provenance", "satisfied", [behavior_id])
    set_gate(report, "no-open-p0-p1", "satisfied", [issue_id])
    set_gate(report, "package-parity-checksum", "satisfied", [package_record_id])
    report["candidate_readiness"]["ready"] = True
    index_path = root / "evidence-index.json"
    write(index_path, index)
    paths["index"] = index_path
    return report, index, paths


def promote_later(root: Path, report: dict[str, Any], index: dict[str, Any], paths: dict[str, Path]) -> None:
    allowlist = load(ALLOWLIST)
    candidate = report["candidate"]
    candidate_id = candidate["candidate_id"]
    package = candidate["package"]
    package_id = package["package_id"]
    for surface in report["runtime_surfaces"]:
        surface_id = surface["id"]
        observed_id = f"EV-RUNTIME-OBSERVED-{surface_id.upper()}"
        report["evidence_records"].append({
            "id": observed_id, "axis": "runtime", "artifact": artifact(package_id, candidate_id), "surface": surface_id,
            "state": "observed_unverified", "outcome": "pass", "prerequisite_record_ids": ["EV-STATIC-CANDIDATE-REVIEW-013"],
            "evidence": [evidence(f"external://operator-observation/{surface_id}-package", "manual_observation", "unverified")],
            "observations": {"scenario": "runtime_package_observed"}, "limitations": []
        })
        install_ref = f"external://install/{surface_id}"
        install_path = root / f"install-{surface_id}.json"
        write(install_path, {
            "schema_version": "1.0.0", "evidence_kind": "install_receipt", "candidate_id": candidate_id,
            "package_id": package_id, "package_archive_sha256": package["archive_sha256"], "surface_id": surface_id,
            "install_event_id": f"install-{surface_id}", "captured_at": "2026-09-01T17:00:00+02:00", "installed": True
        })
        add_index(index, install_ref, "install_receipt", install_path)
        load_ref = f"external://runtime-load/{surface_id}"
        load_path = root / f"load-{surface_id}.json"
        write(load_path, {
            "schema_version": "1.0.0", "evidence_kind": "runtime_load_capture", "candidate_id": candidate_id,
            "package_id": package_id, "package_archive_sha256": package["archive_sha256"], "surface_id": surface_id,
            "load_event_id": f"load-{surface_id}", "captured_at": "2026-09-01T17:05:00+02:00",
            "loaded_skill_ids": [item["skill_id"] for item in allowlist["skills"]], "loaded": True
        })
        add_index(index, load_ref, "runtime_load_capture", load_path)
        runtime_id = f"EV-RUNTIME-VERIFIED-{surface_id.upper()}"
        report["evidence_records"].append({
            "id": runtime_id, "axis": "runtime", "artifact": artifact(package_id, candidate_id, "installed_package"),
            "surface": surface_id, "state": "runtime_loaded_verified", "outcome": "pass",
            "prerequisite_record_ids": ["EV-STATIC-CANDIDATE-REVIEW-013", observed_id],
            "evidence": [evidence(install_ref, "install_receipt"), evidence(load_ref, "runtime_load_capture")],
            "observations": {"installed": True, "loaded": True}, "limitations": []
        })
        surface.update({
            "artifact": artifact(package_id, candidate_id, "installed_package"), "state": "runtime_loaded_verified",
            "outcome": "pass", "evidence_record_ids": [runtime_id], "candidate_installed_verified": True,
            "runtime_loaded_verified": True, "limitations": []
        })

    pilot_ref = "external://pilot/candidate-package"
    pilot_path = root / "pilot.json"
    write(pilot_path, {
        "schema_version": "1.0.0", "evidence_kind": "pilot_record", "candidate_id": candidate_id,
        "package_id": package_id, "package_archive_sha256": package["archive_sha256"], "surface_id": "codex-desktop", "participant_role": "marketer",
        "completed_at": "2026-09-01T18:00:00+02:00",
        "sessions": [{"session_id": "pilot-session", "tasks_completed": 3, "started_at": "2026-09-01T17:10:00+02:00", "finished_at": "2026-09-01T18:00:00+02:00"}],
        "completed": True, "outcome": "pass"
    })
    add_index(index, pilot_ref, "pilot_record", pilot_path)
    pilot_id = "EV-PILOT-VERIFIED-CANDIDATE"
    report["evidence_records"].append({
        "id": pilot_id, "axis": "pilot", "artifact": artifact(package_id, candidate_id, "installed_package"), "surface": "codex-desktop",
        "state": "pilot_verified", "outcome": "pass",
        "prerequisite_record_ids": ["EV-CANDIDATE-NINE-SKILL-PROVENANCE", "EV-CANDIDATE-ISSUE-REGISTER", "EV-CANDIDATE-PACKAGE-INTEGRITY", "EV-RUNTIME-VERIFIED-CODEX-DESKTOP"],
        "evidence": [evidence(pilot_ref, "pilot_record")], "observations": {"real_marketer": True}, "limitations": []
    })
    report["pilot"].update({
        "state": "pilot_verified", "outcome": "pass", "artifact_id": package_id,
        "artifact_kind": "installed_package", "source_candidate_id": candidate_id, "surface_id": "codex-desktop",
        "evidence_record_ids": [pilot_id], "real_marketer_verified": True
    })
    for gate in report["later_promotion"]["gates"]:
        gate["state"] = "satisfied"
    report["later_promotion"]["ready"] = True
    write(paths["index"], index)
    paths["pilot_proof"] = pilot_path


def save_case(root: Path, name: str, report: dict[str, Any], index: dict[str, Any]) -> tuple[Path, Path]:
    report_path = root / f"{name}-report.json"
    index_path = root / f"{name}-index.json"
    write(report_path, report)
    write(index_path, index)
    return report_path, index_path


def replace_proof(root: Path, index: dict[str, Any], ref: str, proof: dict[str, Any], name: str) -> None:
    path = root / f"{name}.json"
    write(path, proof)
    update_index(index, ref, path)


def rebind_package_case(
    root: Path,
    report: dict[str, Any],
    index: dict[str, Any],
    paths: dict[str, Path],
    root_mutation: str | None = None,
    zip_mutation: str | None = None,
) -> None:
    package_root = root / "package-root"
    shutil.copytree(paths["package_root"], package_root)
    if root_mutation == "rogue":
        rogue = package_root / "skills/rogue"
        rogue.mkdir()
        (rogue / "SKILL.md").write_text("name: rogue\n", encoding="utf-8")
    elif root_mutation == "missing":
        next((package_root / "skills").glob("*/SKILL.md")).unlink()
    elif root_mutation == "symlink":
        (package_root / "skills/rogue-link").symlink_to(package_root / "manifest.json")

    archive_path = root / "candidate.zip"
    if zip_mutation in {"from-root", "missing"}:
        skipped = False
        with zipfile.ZipFile(archive_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            for path in sorted(item for item in package_root.rglob("*") if item.is_file() and not item.is_symlink()):
                if zip_mutation == "missing" and path.name == "SKILL.md" and not skipped:
                    skipped = True
                    continue
                archive.write(path, path.relative_to(package_root).as_posix())
    else:
        shutil.copy2(paths["archive"], archive_path)
        if zip_mutation in {"rogue", "traversal", "duplicate", "symlink"}:
            with warnings.catch_warnings():
                warnings.simplefilter("ignore", UserWarning)
                with zipfile.ZipFile(archive_path, "a", compression=zipfile.ZIP_DEFLATED) as archive:
                    if zip_mutation == "rogue":
                        archive.writestr("skills/rogue/SKILL.md", "name: rogue\n")
                    elif zip_mutation == "traversal":
                        archive.writestr("../rogue.txt", "rogue")
                    elif zip_mutation == "duplicate":
                        archive.writestr("manifest.json", (package_root / "manifest.json").read_bytes())
                    else:
                        info = zipfile.ZipInfo("skills/rogue-link")
                        info.external_attr = (stat.S_IFLNK | 0o777) << 16
                        archive.writestr(info, "../manifest.json")

    package = report["candidate"]["package"]
    package["archive_sha256"] = digest(archive_path)
    refs = {
        "external://issue-register/candidate-package": "issue",
        "external://package-parity/candidate-package": "parity",
        "external://checksum/candidate-package": "checksum",
    }
    for ref, label in refs.items():
        source = Path(next(item for item in index["evidence"] if item["ref"] == ref)["path"])
        proof = load(source)
        proof["package_archive_sha256"] = package["archive_sha256"]
        if label == "parity":
            proof["package_root_path"] = str(package_root.resolve())
            proof["package_manifest_path"] = str((package_root / "manifest.json").resolve())
        elif label == "checksum":
            proof["package_root_path"] = str(package_root.resolve())
            proof["archive_path"] = str(archive_path.resolve())
            proof["archive_sha256"] = package["archive_sha256"]
        replace_proof(root, index, ref, proof, f"{label}-proof")


def main() -> int:
    checker = import_module("readiness_checker_selftest", CHECKER)
    failures: list[str] = []
    counts = {"positive": 0, "negative": 0}
    with tempfile.TemporaryDirectory(prefix="ams-readiness-selftest-") as temp:
        root = Path(temp)
        candidate_report, base_index, paths = build_candidate_ready(root / "base")
        later_report = copy.deepcopy(candidate_report)
        later_index = copy.deepcopy(base_index)
        promote_later(root / "base", later_report, later_index, paths)

        def run_case(name: str, report: dict[str, Any], index: dict[str, Any] | None, expected_pass: bool, expected_candidate: bool, expected_later: bool, required_rules: set[str]) -> None:
            counts["positive" if expected_pass else "negative"] += 1
            report_path, index_path = save_case(root, name, report, index or {"schema_version": "1.0.0", "evidence": []})
            outcome = checker.validate(report_path, index_path if index is not None else None)
            actual = set(outcome["rule_ids"])
            ok = outcome["pass"] is expected_pass and outcome["candidate_ready"] is expected_candidate and outcome["later_promotion_ready"] is expected_later and required_rules.issubset(actual)
            if not ok:
                failures.append(f"{name}: pass={outcome['pass']} candidate={outcome['candidate_ready']} later={outcome['later_promotion_ready']} rules={sorted(actual)}")
            else:
                print(f"PASS {name}: {sorted(actual)}")

        run_case("positive-current-no-index", copy.deepcopy(load(REPORT)), None, True, False, False, set())
        run_case("positive-candidate-ready", copy.deepcopy(candidate_report), copy.deepcopy(base_index), True, True, False, set())
        run_case("positive-later-promotion", copy.deepcopy(later_report), copy.deepcopy(later_index), True, True, True, set())

        for name, root_mutation, zip_mutation, expected_rules in (
            ("reject-rogue-skill-root-only", "rogue", None, {"M023"}),
            ("reject-rogue-skill-zip-only", None, "rogue", {"M024"}),
            ("reject-rogue-skill-root-and-zip", "rogue", "from-root", {"M023", "M024"}),
            ("reject-missing-package-file", "missing", None, {"M023"}),
            ("reject-package-root-symlink", "symlink", None, {"M023"}),
            ("reject-zip-symlink", None, "symlink", {"M024"}),
            ("reject-missing-zip-file", None, "missing", {"M024"}),
            ("reject-zip-path-traversal", None, "traversal", {"M024"}),
            ("reject-zip-duplicate-entry", None, "duplicate", {"M024"}),
        ):
            report = copy.deepcopy(candidate_report)
            index = copy.deepcopy(base_index)
            rebind_package_case(root / name, report, index, paths, root_mutation, zip_mutation)
            run_case(name, report, index, False, False, False, expected_rules)

        resolved_report = copy.deepcopy(candidate_report)
        resolved_index = copy.deepcopy(base_index)
        resolved_proof = load(paths["issue_proof"])
        package_id = resolved_report["candidate"]["package"]["package_id"]
        resolved_proof["issues"] = [
            {"id": "ISSUE-P0", "priority": "P0", "status": "closed", "package_id": package_id},
            {"id": "ISSUE-P1", "priority": "P1", "status": "resolved", "package_id": package_id},
        ]
        replace_proof(root, resolved_index, "external://issue-register/candidate-package", resolved_proof, "resolved-critical-issues")
        run_case("positive-resolved-critical-statuses", resolved_report, resolved_index, True, True, False, set())

        for name, source_system in (
            ("reject-source-system-self-asserted", "self_asserted"),
            ("reject-source-system-self-asserted-trailing-space", "self_asserted "),
            ("reject-source-system-case-variant", "Self_Asserted"),
            ("reject-source-system-whitespace-only", "   "),
            ("reject-source-system-unknown", "unknown-exporter"),
        ):
            report = copy.deepcopy(candidate_report)
            index = copy.deepcopy(base_index)
            proof = load(paths["issue_proof"])
            proof["source_system"] = source_system
            replace_proof(root, index, "external://issue-register/candidate-package", proof, name)
            run_case(name, report, index, False, False, False, {"M019"})

        for name, priority, remove_priority in (
            ("reject-issue-priority-critical", "critical", False),
            ("reject-issue-priority-trailing-space", "P0 ", False),
            ("reject-issue-priority-null", None, False),
            ("reject-issue-priority-missing", None, True),
        ):
            report = copy.deepcopy(candidate_report)
            index = copy.deepcopy(base_index)
            proof = load(paths["issue_proof"])
            issue_item = {"id": f"ISSUE-{name}", "priority": priority, "status": "open", "package_id": report["candidate"]["package"]["package_id"]}
            if remove_priority:
                issue_item.pop("priority")
            proof["issues"] = [issue_item]
            replace_proof(root, index, "external://issue-register/candidate-package", proof, name)
            run_case(name, report, index, False, False, False, {"M019"})

        for status in ("open", "in_progress", "reopened", "blocked", "unknown", "accepted_risk"):
            report = copy.deepcopy(candidate_report)
            index = copy.deepcopy(base_index)
            proof = load(paths["issue_proof"])
            proof["issues"] = [{"id": f"ISSUE-{status}", "priority": "P0", "status": status, "package_id": report["candidate"]["package"]["package_id"]}]
            replace_proof(root, index, "external://issue-register/candidate-package", proof, f"issue-{status}")
            run_case(f"reject-critical-status-{status}", report, index, False, False, False, {"M019"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        proof = load(paths["issue_proof"])
        proof["issues"] = [{"id": "ISSUE-missing-status", "priority": "P1", "package_id": report["candidate"]["package"]["package_id"]}]
        replace_proof(root, index, "external://issue-register/candidate-package", proof, "issue-missing-status")
        run_case("reject-critical-missing-status", report, index, False, False, False, {"M019"})

        report = copy.deepcopy(candidate_report)
        report["candidate_readiness"]["gates"].append(copy.deepcopy(report["candidate_readiness"]["gates"][0]))
        run_case("reject-identical-duplicate-readiness-gate", report, copy.deepcopy(base_index), False, False, False, {"M012"})

        report = copy.deepcopy(candidate_report)
        report["candidate_readiness"]["required_gate_ids"].append(report["candidate_readiness"]["required_gate_ids"][0])
        run_case("reject-identical-duplicate-required-gate-id", report, copy.deepcopy(base_index), False, False, False, {"M012"})

        report = copy.deepcopy(candidate_report)
        issue_record = next(item for item in report["evidence_records"] if item["id"] == "EV-CANDIDATE-ISSUE-REGISTER")
        issue_record["id"] = "   "
        set_gate(report, "no-open-p0-p1", "satisfied", ["   "])
        run_case("reject-whitespace-record-id-referenced-by-gate", report, copy.deepcopy(base_index), False, False, False, {"M001", "M011"})

        report = copy.deepcopy(candidate_report)
        report["candidate"]["package_state"] = "not_built"
        report["candidate"]["package"] = None
        run_case("reject-candidate-ready-package-not-built", report, copy.deepcopy(base_index), False, False, False, {"M020"})

        report = copy.deepcopy(later_report)
        report["candidate"]["package_state"] = "not_built"
        report["candidate"]["package"] = None
        run_case("reject-later-ready-package-not-built", report, copy.deepcopy(later_index), False, False, False, {"M020"})

        report = copy.deepcopy(candidate_report)
        behavior = next(item for item in report["evidence_records"] if item["id"] == "EV-CANDIDATE-NINE-SKILL-PROVENANCE")
        behavior["evidence"] = [evidence("external://issue-register/candidate-package", "issue_register")]
        run_case("reject-high-kind-for-wrong-axis", report, copy.deepcopy(base_index), False, False, False, {"M015"})

        report = copy.deepcopy(later_report)
        for item in report["evidence_records"]:
            if item["state"] == "runtime_loaded_verified":
                item["outcome"] = "fail"
        for surface in report["runtime_surfaces"]:
            surface["outcome"] = "fail"
        run_case("reject-runtime-outcome-fail", report, copy.deepcopy(later_index), False, False, False, {"M003", "M008"})

        report = copy.deepcopy(later_report)
        next(item for item in report["evidence_records"] if item["id"] == "EV-PILOT-VERIFIED-CANDIDATE")["outcome"] = "fail"
        report["pilot"]["outcome"] = "fail"
        run_case("reject-pilot-outcome-fail", report, copy.deepcopy(later_index), False, False, False, {"M003", "M009"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        proof = load(paths["behavior_proof"])
        capture = load(paths["capture"])
        capture["events"] = capture["events"][:8]
        capture_path = root / "capture-eight-events.json"
        write(capture_path, capture)
        proof["capture_manifest_path"] = str(capture_path.resolve())
        proof["capture_manifest_sha256"] = digest(capture_path)
        replace_proof(root, index, "external://behavioral-capture/candidate-nine-skill", proof, "behavior-eight-proof")
        run_case("reject-behavior-eight-skills", report, index, False, False, False, {"M016"})

        for name, key, value in (
            ("reject-behavior-candidate-divergence", "candidate_id", "different-candidate"),
            ("reject-behavior-surface-divergence", "surface_id", "codex-cli"),
            ("reject-behavior-manifest-digest-divergence", "candidate_manifest_sha256", "f" * 64),
        ):
            report = copy.deepcopy(candidate_report)
            index = copy.deepcopy(base_index)
            proof = load(paths["behavior_proof"])
            proof[key] = value
            replace_proof(root, index, "external://behavioral-capture/candidate-nine-skill", proof, name)
            run_case(name, report, index, False, False, False, {"M016"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        provenance = import_module("readiness_provenance_digest_mutation", PROVENANCE_SELFTEST)
        capture_path, raw_path, snapshot_path = provenance.build_capture(root / "skill-digest-capture")
        provenance.mutate_skill_digest(capture_path, raw_path, snapshot_path)
        proof = load(paths["behavior_proof"])
        proof.update({
            "capture_manifest_path": str(capture_path), "capture_manifest_sha256": digest(capture_path),
            "raw_path": str(raw_path), "raw_sha256": digest(raw_path),
            "snapshot_path": str(snapshot_path), "snapshot_sha256": digest(snapshot_path)
        })
        replace_proof(root, index, "external://behavioral-capture/candidate-nine-skill", proof, "behavior-skill-digest-divergence")
        run_case("reject-behavior-skill-digest-divergence", report, index, False, False, False, {"M016"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        proof = {"schema_version": "1.0.0", "evidence_kind": "package_parity", "candidate_id": report["candidate"]["candidate_id"], "pass": True}
        replace_proof(root, index, "external://package-parity/candidate-package", proof, "self-asserted-parity")
        run_case("reject-self-asserted-package-parity", report, index, False, False, False, {"M001"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        proof = load(paths["parity_proof"])
        proof["package_id"] = "different-package"
        replace_proof(root, index, "external://package-parity/candidate-package", proof, "unbound-parity")
        run_case("reject-parity-not-bound-to-package", report, index, False, False, False, {"M020"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        proof = load(paths["checksum_proof"])
        proof["package_id"] = "different-package"
        replace_proof(root, index, "external://checksum/candidate-package", proof, "unbound-checksum")
        run_case("reject-checksum-not-bound-to-package", report, index, False, False, False, {"M020"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        next(item for item in index["evidence"] if item["ref"] == "external://checksum/candidate-package")["sha256"] = "0" * 64
        run_case("reject-external-index-digest-mismatch", report, index, False, False, False, {"M007"})

        for name, ref, key, value, expected in (
            ("reject-install-timestamp-without-timezone", "external://install/codex-desktop", "captured_at", "2026-09-01T17:00:00", {"M017"}),
            ("reject-install-after-load", "external://install/codex-desktop", "captured_at", "2026-09-01T17:10:00+02:00", {"M025"}),
            ("reject-empty-install-event-id", "external://install/codex-desktop", "install_event_id", "", {"M021"}),
            ("reject-duplicate-event-id-across-surfaces", "external://install/codex-cli", "install_event_id", "install-codex-desktop", {"M021"}),
        ):
            report = copy.deepcopy(later_report)
            index = copy.deepcopy(later_index)
            source = Path(next(item for item in index["evidence"] if item["ref"] == ref)["path"])
            proof = load(source)
            proof[key] = value
            replace_proof(root, index, ref, proof, name)
            run_case(name, report, index, False, False, False, expected)

        for name, mutation, expected in (
            ("reject-pilot-timestamp-without-timezone", "naive", {"M018"}),
            ("reject-pilot-session-reversed", "reversed", {"M018"}),
            ("reject-duplicate-pilot-session-id", "duplicate", {"M021"}),
            ("reject-pilot-start-before-runtime-load", "started_before_load", {"M025"}),
            ("reject-pilot-completed-before-runtime-load", "completed_before_load", {"M025"}),
        ):
            report = copy.deepcopy(later_report)
            index = copy.deepcopy(later_index)
            ref = "external://pilot/candidate-package"
            source = Path(next(item for item in index["evidence"] if item["ref"] == ref)["path"])
            proof = load(source)
            if mutation == "naive":
                proof["completed_at"] = "2026-09-01T18:00:00"
            elif mutation == "reversed":
                proof["sessions"][0]["started_at"] = "2026-09-01T17:30:00+02:00"
                proof["sessions"][0]["finished_at"] = "2026-09-01T17:00:00+02:00"
            elif mutation == "duplicate":
                proof["sessions"].append(copy.deepcopy(proof["sessions"][0]))
            elif mutation == "started_before_load":
                proof["sessions"][0]["started_at"] = "2026-09-01T17:04:00+02:00"
            else:
                proof["completed_at"] = "2026-09-01T17:04:00+02:00"
                proof["sessions"][0]["started_at"] = "2026-09-01T16:30:00+02:00"
                proof["sessions"][0]["finished_at"] = "2026-09-01T17:00:00+02:00"
            replace_proof(root, index, ref, proof, name)
            run_case(name, report, index, False, False, False, expected)

        report = copy.deepcopy(later_report)
        pilot_record = next(item for item in report["evidence_records"] if item["id"] == "EV-PILOT-VERIFIED-CANDIDATE")
        pilot_record["prerequisite_record_ids"].remove("EV-RUNTIME-VERIFIED-CODEX-DESKTOP")
        run_case("reject-pilot-without-runtime-installed", report, copy.deepcopy(later_index), False, False, False, {"M006"})

        report = copy.deepcopy(load(REPORT))
        report["candidate"]["source_base_commit"] = "0" * 40
        run_case("reject-candidate-commit-divergence", report, None, False, False, False, {"M026"})

        report = copy.deepcopy(load(REPORT))
        report["candidate"]["suite_base_version"] = "0.0.0-divergent"
        run_case("reject-candidate-suite-version-divergence", report, None, False, False, False, {"M026"})

        report = copy.deepcopy(load(REPORT))
        report["candidate"]["candidate_id"] = "different-source-candidate"
        run_case("reject-candidate-id-divergence", report, None, False, False, False, {"M026"})

        report = copy.deepcopy(load(REPORT))
        report["candidate"]["campaign_review_version"] = "9.9.9"
        run_case("reject-campaign-review-version-divergence", report, None, False, False, False, {"M026"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        malformed_capture = root / "malformed-capture.json"
        malformed_capture.write_text("{", encoding="utf-8")
        proof = load(paths["behavior_proof"])
        proof["capture_manifest_path"] = str(malformed_capture.resolve())
        proof["capture_manifest_sha256"] = digest(malformed_capture)
        replace_proof(root, index, "external://behavioral-capture/candidate-nine-skill", proof, "malformed-secondary-proof")
        run_case("reject-malformed-secondary-json", report, index, False, False, False, {"M022"})

        report = copy.deepcopy(candidate_report)
        index = copy.deepcopy(base_index)
        invalid_utf8_proof = root / "invalid-utf8-external-proof.json"
        invalid_utf8_proof.write_bytes(b"\xff\xfe\xfa")
        issue_entry = next(item for item in index["evidence"] if item["ref"] == "external://issue-register/candidate-package")
        issue_entry["path"] = str(invalid_utf8_proof.resolve())
        issue_entry["sha256"] = digest(invalid_utf8_proof)
        run_case("reject-invalid-utf8-external-proof", report, index, False, False, False, {"M007"})

        report = copy.deepcopy(candidate_report)
        report_path, _unused_index_path = save_case(root, "invalid-utf8-external-index", report, base_index)
        invalid_utf8_index = root / "invalid-utf8-external-index.json"
        invalid_utf8_index.write_bytes(b"\xff\xfe\xfa")
        outcome = checker.validate(report_path, invalid_utf8_index)
        counts["negative"] += 1
        if outcome["pass"] or outcome["candidate_ready"] or outcome["later_promotion_ready"] or "M007" not in outcome["rule_ids"]:
            failures.append(f"reject-invalid-utf8-external-index: {outcome}")
        else:
            print(f"PASS reject-invalid-utf8-external-index: {outcome['rule_ids']}")

        report = copy.deepcopy(later_report)
        next(item for item in report["evidence_records"] if item["id"] == "EV-STATIC-CANDIDATE-REVIEW-013")["evidence"][0]["ref"] = "evals/robustness/runtime-readiness/missing-regression.json"
        run_case("invalid-matrix-never-exposes-ready", report, copy.deepcopy(later_index), False, False, False, {"M004"})

        current_cli = subprocess.run(["python3", str(CHECKER)], cwd=REPO, capture_output=True, text=True)
        positive_report_path, positive_index_path = save_case(root, "cli-positive", candidate_report, base_index)
        verified_cli = subprocess.run(["python3", str(CHECKER), "--report", str(positive_report_path), "--external-evidence-index", str(positive_index_path)], cwd=REPO, capture_output=True, text=True)
        if current_cli.returncode != 0 or verified_cli.returncode != 0:
            failures.append("cli-modes: checker senza indice o con indice verificato non operativo")
        else:
            print("PASS cli-current-without-index-and-verified-with-index")

        runner = import_module("readiness_runner_cli_selftest", RUNNER)
        without_index = runner.readiness_checker_args(None)
        with_index = runner.readiness_checker_args(paths["index"])
        runner_help = subprocess.run(["python3", str(RUNNER), "--help"], cwd=REPO, capture_output=True, text=True)
        if "--external-evidence-index" in without_index or with_index[-2:] != ["--external-evidence-index", str(paths["index"].resolve())] or "--readiness-evidence-index" not in runner_help.stdout:
            failures.append("runner-cli-forwarding: modalità senza indice o inoltro esplicito non corretti")
        else:
            print("PASS runner-cli-without-index-and-forwarded-readiness-index")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        return 1
    print(f"SELF-TEST PASS: matrice prudente, {counts['negative']} regressioni e {counts['positive']} percorsi positivi effimeri; nessun artefatto persistito")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
