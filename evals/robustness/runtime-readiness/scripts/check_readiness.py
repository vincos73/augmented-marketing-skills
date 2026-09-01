#!/usr/bin/env python3
"""Validate the public AMS runtime/readiness matrix without promoting unverified evidence."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import stat
import subprocess
import zipfile
from datetime import datetime
from pathlib import Path, PurePosixPath
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
REPO = Path(__file__).resolve().parents[4]
DEFAULT_REPORT = ROOT / "candidate-readiness.json"
PROVENANCE_CHECKER = REPO / "evals/behavioral-provenance/scripts/check_provenance.py"
RAW_CHECKER = REPO / "evals/raw-to-snapshot/scripts/check_raw_to_snapshot.py"
CODEX_PLUGIN_MANIFEST = REPO / ".codex-plugin/plugin.json"
CLAUDE_PLUGIN_MANIFEST = REPO / "claude/.claude-plugin/plugin.json"
HIGH_STATES = {"provenance_verified", "runtime_loaded_verified", "pilot_verified"}
AXIS_STATES = {
    "source": {"not_run", "static_only"},
    "behavior": {"not_run", "observed_unverified", "provenance_verified"},
    "runtime": {"not_run", "observed_unverified", "runtime_loaded_verified"},
    "release": {"not_run", "observed_unverified", "provenance_verified"},
    "pilot": {"not_run", "observed_unverified", "pilot_verified"},
}
INTERNAL_KINDS = {"static_structure", "static_regression"}
HIGH_KIND_MAP = {
    ("behavior", "provenance_verified"): {"behavioral_capture"},
    ("runtime", "runtime_loaded_verified"): {"install_receipt", "runtime_load_capture"},
    ("pilot", "pilot_verified"): {"pilot_record"},
}
SURFACE_IDS = {"codex-desktop", "codex-cli", "claude-local", "claude-cloud"}
SURFACE_RUNTIME = {
    "codex-desktop": ("openai", "codex-desktop"),
    "codex-cli": ("openai", "codex-cli"),
}
READINESS_GATE_IDS = {
    "static-suite",
    "compacted-forward",
    "nine-skill-candidate-provenance",
    "no-open-p0-p1",
    "package-parity-checksum",
}
OWNER_ROLES = {"quality owner", "runtime validation owner", "release owner", "pilot owner"}
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
COMMIT_RE = re.compile(r"^[0-9a-f]{40}$")
UUID_RE = re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I)
RESOLVED_CRITICAL_STATUSES = {"closed", "resolved"}
ISSUE_PRIORITIES = {"P0", "P1", "P2", "P3"}
ISSUE_REGISTER_EXPORTERS = {"external-issue-tracker-export"}


def issue(rule_id: str, location: str, message: str) -> dict[str, str]:
    return {"rule_id": rule_id, "location": location, "message": message}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def package_digest(path: Path) -> str:
    rows: list[bytes] = []
    for file_path in sorted(item for item in path.rglob("*") if item.is_file()):
        relative = file_path.relative_to(path)
        if "__pycache__" in relative.parts or file_path.name == ".DS_Store":
            continue
        rows.append(str(relative).encode("utf-8") + b"\0" + file_digest(file_path).encode("ascii") + b"\n")
    return hashlib.sha256(b"".join(rows)).hexdigest()


def zip_skill_digest(archive: zipfile.ZipFile, prefix: str) -> str:
    rows: list[bytes] = []
    normalized = prefix.rstrip("/") + "/"
    for name in sorted(item for item in archive.namelist() if item.startswith(normalized) and not item.endswith("/")):
        relative = name[len(normalized):]
        if "__pycache__" in Path(relative).parts or Path(relative).name == ".DS_Store":
            continue
        digest = hashlib.sha256(archive.read(name)).hexdigest()
        rows.append(relative.encode("utf-8") + b"\0" + digest.encode("ascii") + b"\n")
    return hashlib.sha256(b"".join(rows)).hexdigest()


def valid_datetime(value: Any) -> bool:
    return parse_datetime(value) is not None


def parse_datetime(value: Any) -> datetime | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None
    except ValueError:
        return None


def canonical_identifier(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and value == value.strip()


def canonical_identifier_list(value: Any) -> bool:
    return (
        isinstance(value, list)
        and all(canonical_identifier(item) for item in value)
        and len(value) == len(set(value))
    )


def safe_load_json(path: Path, location: str, errors: list[dict[str, str]]) -> Any | None:
    try:
        return load_json(path)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        errors.append(issue("M022", location, f"JSON secondario non valido: {exc}"))
        return None


def expected_package_tree(manifest: dict[str, Any]) -> tuple[dict[str, Path | None], set[str]]:
    files: dict[str, Path | None] = {"manifest.json": None}
    directories = {"skills"}
    for skill in manifest.get("skills", []):
        source = (REPO / str(skill.get("path", ""))).resolve()
        skill_prefix = f"skills/{skill.get('skill_id')}"
        directories.add(skill_prefix)
        for current, dirnames, filenames in os.walk(source, followlinks=False):
            current_path = Path(current)
            relative_dir = current_path.relative_to(source)
            if relative_dir.parts:
                directories.add(f"{skill_prefix}/{relative_dir.as_posix()}")
            for dirname in dirnames:
                child = current_path / dirname
                if child.is_symlink():
                    raise ValueError(f"symlink sorgente vietato: {child}")
            for filename in filenames:
                child = current_path / filename
                if child.is_symlink():
                    raise ValueError(f"symlink sorgente vietato: {child}")
                if "__pycache__" in child.relative_to(source).parts or child.name == ".DS_Store":
                    continue
                relative = child.relative_to(source).as_posix()
                files[f"{skill_prefix}/{relative}"] = child
    return files, directories


def validate_root_tree(
    root: Path,
    package_manifest_path: Path,
    manifest: dict[str, Any],
    location: str,
    errors: list[dict[str, str]],
) -> tuple[dict[str, Path | None], set[str]] | None:
    try:
        expected_files, expected_dirs = expected_package_tree(manifest)
    except (OSError, ValueError) as exc:
        errors.append(issue("M023", location, str(exc)))
        return None
    actual_files: set[str] = set()
    actual_dirs: set[str] = set()
    symlinks: list[str] = []
    for current, dirnames, filenames in os.walk(root, followlinks=False):
        current_path = Path(current)
        for dirname in list(dirnames):
            child = current_path / dirname
            relative = child.relative_to(root).as_posix()
            if child.is_symlink():
                symlinks.append(relative)
                dirnames.remove(dirname)
            else:
                actual_dirs.add(relative)
        for filename in filenames:
            child = current_path / filename
            relative = child.relative_to(root).as_posix()
            if child.is_symlink():
                symlinks.append(relative)
            else:
                actual_files.add(relative)
    if symlinks or actual_files != set(expected_files) or actual_dirs != expected_dirs or package_manifest_path != root / "manifest.json":
        errors.append(issue("M023", location, f"albero package non esatto; symlink={sorted(symlinks)}, file_extra={sorted(actual_files - set(expected_files))}, file_mancanti={sorted(set(expected_files) - actual_files)}, dir_extra={sorted(actual_dirs - expected_dirs)}, dir_mancanti={sorted(expected_dirs - actual_dirs)}"))
        return None
    for relative, source in expected_files.items():
        if source is not None and (root / relative).read_bytes() != source.read_bytes():
            errors.append(issue("M023", f"{location}/{relative}", "byte package divergenti dalla sorgente candidata"))
            return None
    return expected_files, expected_dirs


def validate_zip_tree(
    archive_path: Path,
    root: Path,
    expected_files: dict[str, Path | None],
    expected_dirs: set[str],
    location: str,
    errors: list[dict[str, str]],
) -> bool:
    try:
        with zipfile.ZipFile(archive_path) as archive:
            infos = archive.infolist()
            names = [info.filename for info in infos]
            if len(names) != len(set(names)):
                errors.append(issue("M024", location, "entry ZIP duplicate"))
                return False
            file_names: set[str] = set()
            dir_names: set[str] = set()
            for info in infos:
                name = info.filename
                path = PurePosixPath(name)
                mode = info.external_attr >> 16
                if not name or "\\" in name or path.is_absolute() or ".." in path.parts or stat.S_ISLNK(mode):
                    errors.append(issue("M024", location, f"entry ZIP vietata: {name}"))
                    return False
                normalized = name.rstrip("/")
                if info.is_dir():
                    dir_names.add(normalized)
                else:
                    file_names.add(name)
            if file_names != set(expected_files) or not dir_names.issubset(expected_dirs):
                errors.append(issue("M024", location, f"set ZIP non esatto; file_extra={sorted(file_names - set(expected_files))}, file_mancanti={sorted(set(expected_files) - file_names)}, dir_extra={sorted(dir_names - expected_dirs)}"))
                return False
            for relative in expected_files:
                if archive.read(relative) != (root / relative).read_bytes():
                    errors.append(issue("M024", f"{location}/{relative}", "root package e ZIP divergenti"))
                    return False
    except (OSError, KeyError, RuntimeError, zipfile.BadZipFile) as exc:
        errors.append(issue("M024", location, f"ZIP non verificabile: {exc}"))
        return False
    return True


def inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def exact_keys(value: Any, expected: set[str], location: str, errors: list[dict[str, str]]) -> bool:
    if not isinstance(value, dict):
        errors.append(issue("M001", location, "oggetto richiesto"))
        return False
    if set(value) != expected:
        errors.append(issue("M001", location, f"campi attesi {sorted(expected)}, osservati {sorted(value)}"))
        return False
    return True


def scan_public(value: Any, location: str, errors: list[dict[str, str]]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            if key.casefold() in {"thread_id", "turn_id", "message_id", "private_path"}:
                errors.append(issue("M002", f"{location}.{key}", "identificatore host o path privato vietato nel report"))
            scan_public(item, f"{location}.{key}", errors)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            scan_public(item, f"{location}[{index}]", errors)
    elif isinstance(value, str):
        if any(token in value for token in ("/Users/", "/home/", "file://")) or re.match(r"^[A-Za-z]:\\", value):
            errors.append(issue("M002", location, "path privato vietato nel report pubblicabile"))
        if UUID_RE.search(value):
            errors.append(issue("M002", location, "identificatore UUID vietato nel report pubblicabile"))


def load_external_index(path: Path | None, errors: list[dict[str, str]]) -> dict[str, dict[str, Any]]:
    if path is None:
        return {}
    resolved = path.resolve()
    if not resolved.is_file() or inside(resolved, REPO):
        errors.append(issue("M007", "$external_index", "l'indice delle evidenze deve essere un file esterno al repository"))
        return {}
    try:
        data = load_json(resolved)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        errors.append(issue("M007", "$external_index", str(exc)))
        return {}
    if not exact_keys(data, {"schema_version", "evidence"}, "$external_index", errors):
        return {}
    if data.get("schema_version") != "1.0.0" or not isinstance(data.get("evidence"), list):
        errors.append(issue("M007", "$external_index", "schema_version o evidence non validi"))
        return {}
    result: dict[str, dict[str, Any]] = {}
    for index, entry in enumerate(data["evidence"]):
        location = f"$external_index.evidence[{index}]"
        if not exact_keys(entry, {"ref", "kind", "path", "sha256"}, location, errors):
            continue
        ref = entry.get("ref")
        if not canonical_identifier(ref) or not ref.startswith("external://") or ref in result:
            errors.append(issue("M007", f"{location}.ref", "riferimento esterno assente, duplicato o non neutrale"))
            continue
        result[ref] = entry
    return result


def external_material(
    proof: dict[str, Any],
    path_key: str,
    digest_key: str | None,
    location: str,
    errors: list[dict[str, str]],
    directory: bool = False,
) -> Path | None:
    value = proof.get(path_key)
    if not isinstance(value, str) or not Path(value).is_absolute():
        errors.append(issue("M007", f"{location}.{path_key}", "path esterno assoluto richiesto"))
        return None
    path = Path(value).resolve()
    valid = path.is_dir() if directory else path.is_file()
    if not valid or inside(path, REPO):
        errors.append(issue("M007", f"{location}.{path_key}", "materiale esterno assente o interno al repository"))
        return None
    if digest_key is not None:
        wanted = proof.get(digest_key)
        if directory or not SHA256_RE.fullmatch(str(wanted or "")) or file_digest(path) != wanted:
            errors.append(issue("M007", f"{location}.{digest_key}", "digest del materiale esterno divergente"))
            return None
    return path


def expected_skill_set(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "sequence": item.get("sequence"),
            "skill_id": item.get("skill_id"),
            "skill_version": item.get("skill_version"),
            "skill_sha256": item.get("skill_sha256"),
        }
        for item in manifest.get("skills", [])
    ]


def package_matches(proof: dict[str, Any], candidate: dict[str, Any], package: dict[str, Any] | None) -> bool:
    return bool(
        package
        and proof.get("candidate_id") == candidate.get("candidate_id")
        and proof.get("package_id") == package.get("package_id")
        and proof.get("package_archive_sha256") == package.get("archive_sha256")
    )


def register_identifier(context: dict[str, Any], bucket: str, value: Any, location: str, errors: list[dict[str, str]]) -> bool:
    if not canonical_identifier(value) or value in context[bucket]:
        errors.append(issue("M021", location, "identificatore non canonico, vuoto o riusato"))
        return False
    context[bucket].add(value)
    return True


def verify_external(
    evidence: dict[str, Any],
    index: dict[str, dict[str, Any]],
    artifact: dict[str, Any],
    surface: str | None,
    candidate: dict[str, Any],
    manifest: dict[str, Any],
    package: dict[str, Any] | None,
    record_id: str,
    proof_context: dict[str, Any],
    location: str,
    errors: list[dict[str, str]],
) -> bool:
    start_errors = len(errors)
    ref = evidence.get("ref")
    entry = index.get(ref)
    if entry is None:
        errors.append(issue("M007", location, "evidenza verificata non risolta dall'indice esterno"))
        return False
    if entry.get("kind") != evidence.get("kind"):
        errors.append(issue("M007", location, "tipo di prova divergente dall'indice esterno"))
        return False
    try:
        path = Path(entry["path"]).resolve()
    except (TypeError, OSError):
        errors.append(issue("M007", location, "path esterno non valido"))
        return False
    if not path.is_file() or inside(path, REPO) or not SHA256_RE.fullmatch(str(entry.get("sha256", ""))):
        errors.append(issue("M007", location, "file esterno assente, interno al repository o senza digest valido"))
        return False
    if file_digest(path) != entry["sha256"]:
        errors.append(issue("M007", location, "digest dell'evidenza esterna divergente"))
        return False
    try:
        proof = load_json(path)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, TypeError, ValueError) as exc:
        errors.append(issue("M007", location, f"prova esterna non leggibile: {exc}"))
        return False
    kind = evidence.get("kind")
    if not isinstance(proof, dict) or proof.get("schema_version") != "1.0.0" or proof.get("evidence_kind") != kind:
        errors.append(issue("M007", location, "schema o evidence_kind della prova esterna divergente"))
        return False
    if kind == "behavioral_capture":
        keys = {
            "schema_version", "evidence_kind", "candidate_id", "source_base_commit",
            "candidate_manifest_ref", "candidate_manifest_sha256", "surface_id",
            "capture_manifest_path", "capture_manifest_sha256", "raw_path", "raw_sha256",
            "snapshot_path", "snapshot_sha256",
        }
        if not exact_keys(proof, keys, location, errors):
            return False
        manifest_path = (REPO / str(candidate.get("candidate_manifest_ref", ""))).resolve()
        identity_ok = (
            proof.get("schema_version") == "1.0.0"
            and proof.get("evidence_kind") == kind
            and proof.get("candidate_id") == candidate.get("candidate_id")
            and proof.get("source_base_commit") == candidate.get("source_base_commit")
            and proof.get("candidate_manifest_ref") == candidate.get("candidate_manifest_ref")
            and proof.get("candidate_manifest_sha256") == file_digest(manifest_path)
            and proof.get("surface_id") == surface
        )
        if not identity_ok:
            errors.append(issue("M016", location, "capture non legata a candidata, commit, manifest e superficie esatti"))
            return False
        capture = external_material(proof, "capture_manifest_path", "capture_manifest_sha256", location, errors)
        raw = external_material(proof, "raw_path", "raw_sha256", location, errors)
        snapshot = external_material(proof, "snapshot_path", "snapshot_sha256", location, errors)
        if not capture or not raw or not snapshot:
            return False
        capture_doc = safe_load_json(capture, f"{location}.capture_manifest_path", errors)
        if not isinstance(capture_doc, dict):
            return False
        provider_runtime = SURFACE_RUNTIME.get(str(surface))
        events = capture_doc.get("events", []) if isinstance(capture_doc, dict) else []
        if not isinstance(events, list) or any(not isinstance(item, dict) for item in events):
            errors.append(issue("M016", location, "eventi capture non strutturati"))
            return False
        if (
            provider_runtime is None
            or (capture_doc.get("provider"), capture_doc.get("runtime")) != provider_runtime
            or capture_doc.get("source_base_commit") != candidate.get("source_base_commit")
            or [(item.get("sequence"), item.get("skill_id")) for item in events]
            != [(item.get("sequence"), item.get("skill_id")) for item in manifest.get("skills", [])]
        ):
            errors.append(issue("M016", location, "capture host divergente da superficie o set delle nove skill candidate"))
            return False
        provenance = subprocess.run(
            ["python3", str(PROVENANCE_CHECKER), "--capture-manifest", str(capture), "--raw", str(raw), "--snapshot", str(snapshot)],
            cwd=REPO, capture_output=True, text=True,
        )
        grounded = subprocess.run(
            ["python3", str(RAW_CHECKER), "--capture-manifest", str(capture), "--raw", str(raw), "--snapshot", str(snapshot), "--require-behavior"],
            cwd=REPO, capture_output=True, text=True,
        )
        if provenance.returncode != 0 or grounded.returncode != 0:
            errors.append(issue("M016", location, "capture esterna non supera provenance e grounding completi"))
        receipt_times: list[datetime] = []
        for index_number, event in enumerate(events):
            receipt_value = event.get("receipt_path") if isinstance(event, dict) else None
            if not isinstance(receipt_value, str):
                errors.append(issue("M022", f"{location}.events[{index_number}]", "receipt path mancante"))
                continue
            receipt_doc = safe_load_json(Path(receipt_value), f"{location}.events[{index_number}].receipt", errors)
            captured = parse_datetime(receipt_doc.get("captured_at")) if isinstance(receipt_doc, dict) else None
            if captured is None:
                errors.append(issue("M025", f"{location}.events[{index_number}].captured_at", "timestamp host timezone-aware richiesto"))
            else:
                receipt_times.append(captured)
        if len(receipt_times) == len(events) and receipt_times:
            proof_context["record_times"].setdefault(record_id, []).append(max(receipt_times))
    elif kind == "runtime_load_capture":
        keys = {"schema_version", "evidence_kind", "candidate_id", "package_id", "package_archive_sha256", "surface_id", "load_event_id", "captured_at", "loaded_skill_ids", "loaded"}
        if not exact_keys(proof, keys, location, errors):
            return False
        load_time = parse_datetime(proof.get("captured_at"))
        event_ok = register_identifier(proof_context, "event_ids", proof.get("load_event_id"), f"{location}.load_event_id", errors)
        if not package_matches(proof, candidate, package) or proof.get("surface_id") != surface or proof.get("loaded") is not True or load_time is None or not event_ok or proof.get("loaded_skill_ids") != [item["skill_id"] for item in expected_skill_set(manifest)]:
            errors.append(issue("M017", location, "capture di load non legata a package, superficie e nove skill esatte"))
        elif package is not None:
            key = (package.get("package_id"), surface)
            proof_context["load_times"][key] = load_time
            proof_context["record_times"].setdefault(record_id, []).append(load_time)
    elif kind == "install_receipt":
        keys = {"schema_version", "evidence_kind", "candidate_id", "package_id", "package_archive_sha256", "surface_id", "install_event_id", "captured_at", "installed"}
        if not exact_keys(proof, keys, location, errors):
            return False
        install_time = parse_datetime(proof.get("captured_at"))
        event_ok = register_identifier(proof_context, "event_ids", proof.get("install_event_id"), f"{location}.install_event_id", errors)
        if not package_matches(proof, candidate, package) or proof.get("surface_id") != surface or proof.get("installed") is not True or install_time is None or not event_ok:
            errors.append(issue("M017", location, "receipt di installazione non legata a package e superficie esatti"))
        elif package is not None:
            key = (package.get("package_id"), surface)
            proof_context["install_times"][key] = install_time
            proof_context["record_times"].setdefault(record_id, []).append(install_time)
    elif kind == "pilot_record":
        keys = {"schema_version", "evidence_kind", "candidate_id", "package_id", "package_archive_sha256", "surface_id", "participant_role", "completed_at", "sessions", "completed", "outcome"}
        if not exact_keys(proof, keys, location, errors):
            return False
        sessions = proof.get("sessions")
        completed_time = parse_datetime(proof.get("completed_at"))
        sessions_ok = isinstance(sessions, list) and bool(sessions)
        parsed_sessions: list[tuple[datetime, datetime]] = []
        if sessions_ok:
            for session in sessions:
                if not isinstance(session, dict) or set(session) != {"session_id", "tasks_completed", "started_at", "finished_at"}:
                    sessions_ok = False
                    break
                start = parse_datetime(session.get("started_at"))
                finish = parse_datetime(session.get("finished_at"))
                id_ok = register_identifier(proof_context, "session_ids", session.get("session_id"), f"{location}.session_id", errors)
                if not id_ok or not isinstance(session.get("tasks_completed"), int) or session["tasks_completed"] <= 0 or start is None or finish is None or completed_time is None or start > finish or finish > completed_time:
                    sessions_ok = False
                    break
                parsed_sessions.append((start, finish))
        if not package_matches(proof, candidate, package) or proof.get("surface_id") != surface or proof.get("participant_role") != "marketer" or proof.get("completed") is not True or proof.get("outcome") != "pass" or completed_time is None or not sessions_ok:
            errors.append(issue("M018", location, "record pilot non dimostra una sessione completata da marketer sul package esatto"))
        else:
            proof_context["record_times"].setdefault(record_id, []).append(completed_time)
            proof_context["pilot_sessions"][record_id] = {
                "surface": surface,
                "package_id": proof.get("package_id"),
                "candidate_id": proof.get("candidate_id"),
                "completed_at": completed_time,
                "sessions": parsed_sessions,
            }
    elif kind == "issue_register":
        keys = {"schema_version", "evidence_kind", "candidate_id", "package_id", "package_archive_sha256", "source_system", "exported_at", "issues"}
        if not exact_keys(proof, keys, location, errors):
            return False
        issues = proof.get("issues")
        issues_ok = isinstance(issues, list)
        issue_ids: set[str] = set()
        if issues_ok:
            for item in issues:
                item_id = item.get("id") if isinstance(item, dict) else None
                if (
                    not isinstance(item, dict)
                    or set(item) != {"id", "priority", "status", "package_id"}
                    or package is None
                    or item.get("package_id") != package.get("package_id")
                    or not canonical_identifier(item_id)
                    or item_id in issue_ids
                    or item.get("priority") not in ISSUE_PRIORITIES
                    or not canonical_identifier(item.get("status"))
                ):
                    issues_ok = False
                    break
                issue_ids.add(item_id)
        unresolved_critical = [item for item in issues or [] if item.get("priority") in {"P0", "P1"} and item.get("status") not in RESOLVED_CRITICAL_STATUSES] if issues_ok else [None]
        exported_time = parse_datetime(proof.get("exported_at"))
        source_system = proof.get("source_system")
        if not package_matches(proof, candidate, package) or not canonical_identifier(source_system) or source_system not in ISSUE_REGISTER_EXPORTERS or exported_time is None or not issues_ok or unresolved_critical:
            errors.append(issue("M019", location, "registro non esportato, non legato al package o con P0/P1 aperti"))
        else:
            proof_context["record_times"].setdefault(record_id, []).append(exported_time)
    elif kind == "package_parity":
        keys = {"schema_version", "evidence_kind", "candidate_id", "package_id", "package_archive_sha256", "source_base_commit", "candidate_manifest_ref", "candidate_manifest_sha256", "package_manifest_ref", "package_root_path", "package_manifest_path", "package_manifest_sha256", "verified_at"}
        if not exact_keys(proof, keys, location, errors):
            return False
        manifest_path = (REPO / str(candidate.get("candidate_manifest_ref", ""))).resolve()
        root = external_material(proof, "package_root_path", None, location, errors, directory=True)
        package_manifest_path = external_material(proof, "package_manifest_path", "package_manifest_sha256", location, errors)
        if not package_matches(proof, candidate, package) or proof.get("source_base_commit") != candidate.get("source_base_commit") or proof.get("candidate_manifest_ref") != candidate.get("candidate_manifest_ref") or proof.get("candidate_manifest_sha256") != file_digest(manifest_path) or package is None or proof.get("package_manifest_ref") != package.get("manifest_ref") or not root or not package_manifest_path:
            errors.append(issue("M020", location, "parità non legata a candidata, manifest e package esatti"))
            return False
        package_manifest = safe_load_json(package_manifest_path, f"{location}.package_manifest_path", errors)
        if not isinstance(package_manifest, dict):
            return False
        expected_manifest = {
            "schema_version": "1.0.0",
            "package_id": package.get("package_id"),
            "source_candidate_id": candidate.get("candidate_id"),
            "source_base_commit": candidate.get("source_base_commit"),
            "suite_version": candidate.get("suite_base_version"),
            "skills": expected_skill_set(manifest),
        }
        verified_time = parse_datetime(proof.get("verified_at"))
        tree = validate_root_tree(root, package_manifest_path, manifest, location, errors)
        parity_ok = package_manifest == expected_manifest and tree is not None and package.get("manifest_sha256") == file_digest(package_manifest_path) and verified_time is not None
        for skill in manifest.get("skills", []):
            skill_root = root / "skills" / skill["skill_id"]
            parity_ok = parity_ok and skill_root.is_dir() and package_digest(skill_root) == skill["skill_sha256"]
        if not parity_ok:
            errors.append(issue("M020", location, "package root o manifest non hanno parità con le nove skill candidate"))
        else:
            proof_context["record_times"].setdefault(record_id, []).append(verified_time)
    elif kind == "checksum":
        keys = {"schema_version", "evidence_kind", "candidate_id", "package_id", "package_archive_sha256", "package_manifest_sha256", "package_root_path", "archive_path", "archive_sha256", "verified_at"}
        if not exact_keys(proof, keys, location, errors):
            return False
        archive_path = external_material(proof, "archive_path", "archive_sha256", location, errors)
        root = external_material(proof, "package_root_path", None, location, errors, directory=True)
        verified_time = parse_datetime(proof.get("verified_at"))
        tree = validate_root_tree(root, root / "manifest.json", manifest, location, errors) if root else None
        checksum_ok = bool(package_matches(proof, candidate, package) and archive_path and root and tree and verified_time is not None and proof.get("package_manifest_sha256") == package.get("manifest_sha256") and proof.get("archive_sha256") == package.get("archive_sha256")) if package else False
        if archive_path and root:
            try:
                expected_files, expected_dirs = expected_package_tree(manifest)
                zip_ok = validate_zip_tree(archive_path, root, expected_files, expected_dirs, location, errors)
            except (OSError, ValueError) as exc:
                errors.append(issue("M024", location, str(exc)))
                zip_ok = False
            checksum_ok = checksum_ok and zip_ok
        if not checksum_ok:
            errors.append(issue("M020", location, "checksum o contenuto archivio non coincidono con package e manifest"))
        else:
            proof_context["record_times"].setdefault(record_id, []).append(verified_time)
    else:
        errors.append(issue("M007", location, "tipo di evidenza verificata non supportato"))
    return len(errors) == start_errors


def validate_artifact(value: Any, location: str, errors: list[dict[str, str]]) -> dict[str, Any]:
    if not exact_keys(value, {"id", "kind", "source_candidate_id"}, location, errors):
        return {}
    if value.get("kind") not in {"source_candidate", "released_package", "packaged_candidate", "installed_package"}:
        errors.append(issue("M001", f"{location}.kind", "tipo artefatto non valido"))
    if not canonical_identifier(value.get("id")):
        errors.append(issue("M001", f"{location}.id", "id artefatto richiesto"))
    source_id = value.get("source_candidate_id")
    if source_id is not None and not canonical_identifier(source_id):
        errors.append(issue("M001", f"{location}.source_candidate_id", "source_candidate_id non valido"))
    return value


def validate_evidence(
    items: Any,
    axis: str,
    state: str,
    artifact: dict[str, Any],
    surface: str | None,
    observations: dict[str, Any],
    candidate: dict[str, Any],
    manifest: dict[str, Any],
    package: dict[str, Any] | None,
    record_id: str,
    proof_context: dict[str, Any],
    external_index: dict[str, dict[str, Any]],
    location: str,
    errors: list[dict[str, str]],
) -> bool:
    start_errors = len(errors)
    if not isinstance(items, list):
        errors.append(issue("M001", location, "elenco evidence richiesto"))
        return False
    if state != "not_run" and not items:
        errors.append(issue("M005", location, "uno stato eseguito richiede almeno un'evidenza"))
        return False
    if state == "not_run" and items:
        errors.append(issue("M003", location, "not_run non può avere evidenze"))
    kinds = {item.get("kind") for item in items if isinstance(item, dict)}
    required_kinds: set[str] | None = None
    if state in HIGH_STATES:
        required_kinds = HIGH_KIND_MAP.get((axis, state))
        if axis == "release" and state == "provenance_verified":
            profile = observations.get("release_check")
            required_kinds = {"issue_register"} if profile == "issue_register" else {"package_parity", "checksum"} if profile == "package_integrity" else None
        if required_kinds is None or kinds != required_kinds or len(items) != len(required_kinds):
            errors.append(issue("M015", location, f"tipi evidenza non ammessi per {axis}/{state}; richiesti {sorted(required_kinds or [])}"))
    elif state == "observed_unverified" and kinds != {"manual_observation"}:
        errors.append(issue("M015", location, "observed_unverified accetta soltanto manual_observation"))
    for index, evidence in enumerate(items):
        item_loc = f"{location}[{index}]"
        if not exact_keys(evidence, {"scope", "kind", "ref", "verification"}, item_loc, errors):
            continue
        scope = evidence.get("scope")
        kind = evidence.get("kind")
        ref = evidence.get("ref")
        verification = evidence.get("verification")
        if scope == "repository":
            if kind not in INTERNAL_KINDS or verification != "static_verified":
                errors.append(issue("M005", item_loc, "l'evidenza interna può provare soltanto struttura o regressioni statiche"))
                continue
            if axis != "source" or state != "static_only":
                errors.append(issue("M005", item_loc, "l'evidenza interna non può provare comportamento, runtime, release o pilot"))
                continue
            if not isinstance(ref, str) or not ref or Path(ref).is_absolute():
                errors.append(issue("M004", item_loc, "riferimento repository relativo richiesto"))
                continue
            resolved = (REPO / ref).resolve()
            if not inside(resolved, REPO) or not resolved.is_file():
                errors.append(issue("M004", item_loc, "evidenza repository non risolvibile"))
        elif scope == "external":
            if not isinstance(ref, str) or not ref.startswith("external://") or any(token in ref for token in ("/Users/", "/home/", "thread")):
                errors.append(issue("M002", item_loc, "riferimento esterno non neutrale"))
                continue
            if state in HIGH_STATES:
                if verification != "external_verified":
                    errors.append(issue("M007", item_loc, "uno stato verificato richiede external_verified"))
                else:
                    verify_external(evidence, external_index, artifact, surface, candidate, manifest, package, record_id, proof_context, item_loc, errors)
            elif state == "observed_unverified":
                if verification != "unverified":
                    errors.append(issue("M003", item_loc, "observed_unverified richiede verification unverified"))
            else:
                errors.append(issue("M003", item_loc, "evidenza esterna incompatibile con lo stato"))
        else:
            errors.append(issue("M001", f"{item_loc}.scope", "scope evidenza non valido"))
    return len(errors) == start_errors


def has_record(records: dict[str, dict[str, Any]], ids: list[str], predicate) -> bool:
    return any(record_id in records and predicate(records[record_id]) for record_id in ids)


def validate(report_path: Path = DEFAULT_REPORT, external_index_path: Path | None = None) -> dict[str, Any]:
    errors: list[dict[str, str]] = []
    try:
        report = load_json(report_path)
    except (OSError, json.JSONDecodeError) as exc:
        return {"pass": False, "matrix_valid": False, "candidate_ready": False, "later_promotion_ready": False, "rule_ids": ["M001"], "errors": [issue("M001", "$", str(exc))]}

    scan_public(report, "$", errors)
    if not exact_keys(report, {"schema_version", "report_id", "as_of", "candidate", "evidence_records", "runtime_surfaces", "pilot", "candidate_readiness", "later_promotion"}, "$", errors):
        return result(errors, False, False)
    if report.get("schema_version") != "1.0.0":
        errors.append(issue("M001", "$.schema_version", "schema_version attesa 1.0.0"))

    candidate = report.get("candidate")
    candidate_keys = {"candidate_id", "artifact_kind", "source_base_commit", "suite_base_version", "plugin_version_changed", "campaign_review_version", "candidate_manifest_ref", "package_state", "package"}
    if not exact_keys(candidate, candidate_keys, "$.candidate", errors):
        candidate = {}
    candidate_id = candidate.get("candidate_id")
    if candidate.get("artifact_kind") != "source_candidate" or candidate.get("campaign_review_version") != "0.1.3" or candidate.get("plugin_version_changed") is not False or candidate.get("package_state") not in {"not_built", "packaged_candidate"}:
        errors.append(issue("M003", "$.candidate", "candidata sorgente, versione o package_state non validi"))
    if not COMMIT_RE.fullmatch(str(candidate.get("source_base_commit", ""))):
        errors.append(issue("M001", "$.candidate.source_base_commit", "commit base non valido"))
    manifest_ref = candidate.get("candidate_manifest_ref")
    if not isinstance(manifest_ref, str) or Path(manifest_ref).is_absolute() or not (REPO / manifest_ref).resolve().is_file() or not inside((REPO / manifest_ref).resolve(), REPO):
        errors.append(issue("M004", "$.candidate.candidate_manifest_ref", "manifesto candidato non risolvibile"))
        manifest: dict[str, Any] = {}
    else:
        manifest_value = safe_load_json((REPO / manifest_ref).resolve(), "$.candidate.candidate_manifest_ref", errors)
        manifest = manifest_value if isinstance(manifest_value, dict) else {}
    codex_plugin = safe_load_json(CODEX_PLUGIN_MANIFEST, "$.candidate.codex_plugin_manifest", errors)
    claude_plugin = safe_load_json(CLAUDE_PLUGIN_MANIFEST, "$.candidate.claude_plugin_manifest", errors)
    campaign_review_entries = [item for item in manifest.get("skills", []) if isinstance(item, dict) and item.get("skill_id") == "campaign-review"]
    expected_candidate_id = f"ams-nine-skill-candidate-campaign-review-v{candidate.get('campaign_review_version')}"
    identity_consistent = bool(
        manifest_ref == "evals/behavioral-provenance/runtime-allowlist.json"
        and manifest.get("source_base_commit") == candidate.get("source_base_commit")
        and len(campaign_review_entries) == 1
        and campaign_review_entries[0].get("skill_version") == candidate.get("campaign_review_version")
        and candidate.get("candidate_id") == expected_candidate_id
        and isinstance(codex_plugin, dict)
        and isinstance(claude_plugin, dict)
        and codex_plugin.get("version") == candidate.get("suite_base_version")
        and claude_plugin.get("version") == candidate.get("suite_base_version")
    )
    if not identity_consistent:
        errors.append(issue("M026", "$.candidate", "candidate id, commit, campaign-review o suite base divergono dai manifesti effettivi"))
    package_value = candidate.get("package")
    package: dict[str, Any] | None = None
    package_valid = False
    if candidate.get("package_state") == "not_built":
        if package_value is not None:
            errors.append(issue("M020", "$.candidate.package", "not_built richiede package null"))
    elif exact_keys(package_value, {"package_id", "artifact_kind", "source_candidate_id", "manifest_ref", "manifest_sha256", "archive_sha256"}, "$.candidate.package", errors):
        package = package_value
        package_valid = bool(
            package.get("artifact_kind") == "packaged_candidate"
            and package.get("source_candidate_id") == candidate_id
            and canonical_identifier(package.get("package_id"))
            and isinstance(package.get("manifest_ref"), str)
            and package.get("manifest_ref", "").startswith("external://")
            and SHA256_RE.fullmatch(str(package.get("manifest_sha256", "")))
            and SHA256_RE.fullmatch(str(package.get("archive_sha256", "")))
        )
        if not package_valid:
            errors.append(issue("M020", "$.candidate.package", "identità packaged_candidate incompleta o non legata alla sorgente"))

    external_index = load_external_index(external_index_path, errors)
    proof_context: dict[str, Any] = {
        "event_ids": set(),
        "session_ids": set(),
        "install_times": {},
        "load_times": {},
        "record_times": {},
        "pilot_sessions": {},
    }
    record_list = report.get("evidence_records")
    if not isinstance(record_list, list):
        errors.append(issue("M001", "$.evidence_records", "elenco richiesto"))
        record_list = []
    records: dict[str, dict[str, Any]] = {}
    record_valid: dict[str, bool] = {}
    record_keys = {"id", "axis", "artifact", "surface", "state", "outcome", "prerequisite_record_ids", "evidence", "observations", "limitations"}
    for index, record in enumerate(record_list):
        location = f"$.evidence_records[{index}]"
        if not exact_keys(record, record_keys, location, errors):
            continue
        record_id = record.get("id")
        if not canonical_identifier(record_id) or record_id in records:
            errors.append(issue("M001", f"{location}.id", "id record non canonico, assente o duplicato"))
            continue
        records[record_id] = record

    for record_id, record in records.items():
        location = f"$.evidence_records[{record_id}]"
        record_error_start = len(errors)
        axis = record.get("axis")
        state = record.get("state")
        if axis not in AXIS_STATES or state not in AXIS_STATES.get(axis, set()):
            errors.append(issue("M003", f"{location}.state", "stato non ammesso per l'asse"))
        outcome = record.get("outcome")
        if state == "not_run" and outcome != "not_run":
            errors.append(issue("M003", f"{location}.outcome", "not_run richiede outcome not_run"))
        if state != "not_run" and outcome not in {"pass", "fail", "issue_observed"}:
            errors.append(issue("M003", f"{location}.outcome", "outcome non valido"))
        if state in HIGH_STATES and outcome != "pass":
            errors.append(issue("M003", f"{location}.outcome", "uno stato verificato richiede outcome pass"))
        surface = record.get("surface")
        if surface is not None and surface not in SURFACE_IDS:
            errors.append(issue("M012", f"{location}.surface", "superficie runtime non valida"))
        artifact = validate_artifact(record.get("artifact"), f"{location}.artifact", errors)
        prerequisites = record.get("prerequisite_record_ids")
        if not canonical_identifier_list(prerequisites):
            errors.append(issue("M001", f"{location}.prerequisite_record_ids", "elenco prerequisiti non canonico o duplicato"))
            prerequisites = []
        unresolved = [item for item in prerequisites if item not in records or item == record_id]
        if unresolved:
            errors.append(issue("M006", f"{location}.prerequisite_record_ids", f"prerequisiti non risolti: {unresolved}"))
        if state == "observed_unverified" and artifact.get("kind") == "source_candidate":
            if not has_record(records, prerequisites, lambda item: item.get("axis") == "source" and item.get("state") == "static_only" and item.get("outcome") == "pass" and item.get("artifact", {}).get("id") == candidate_id):
                errors.append(issue("M006", f"{location}.prerequisite_record_ids", "l'osservazione della candidata richiede una regressione statica PASS"))
        if state == "provenance_verified":
            observed = has_record(records, prerequisites, lambda item: item.get("state") == "observed_unverified" and item.get("artifact", {}).get("id") in {artifact.get("id"), artifact.get("source_candidate_id")})
            static = has_record(records, prerequisites, lambda item: item.get("state") == "static_only" and item.get("outcome") == "pass" and item.get("artifact", {}).get("id") == candidate_id)
            if not observed or not static:
                errors.append(issue("M006", f"{location}.prerequisite_record_ids", "provenance_verified richiede osservazione precedente e static PASS"))
            if axis == "behavior" and (artifact.get("kind") != "source_candidate" or artifact.get("id") != candidate_id):
                errors.append(issue("M010", f"{location}.artifact", "provenance comportamentale deve riferire la sorgente candidata esatta"))
            if axis == "release" and (not package_valid or artifact.get("kind") != "packaged_candidate" or artifact.get("id") != package.get("package_id") or artifact.get("source_candidate_id") != candidate_id):
                errors.append(issue("M020", f"{location}.artifact", "gate release richiede packaged_candidate esatto"))
        if state == "runtime_loaded_verified":
            observed = has_record(records, prerequisites, lambda item: item.get("state") == "observed_unverified" and item.get("surface") == surface and item.get("artifact", {}).get("id") == (package.get("package_id") if package else None))
            static = has_record(records, prerequisites, lambda item: item.get("state") == "static_only" and item.get("outcome") == "pass" and item.get("artifact", {}).get("id") == candidate_id)
            if not observed or not static:
                errors.append(issue("M006", f"{location}.prerequisite_record_ids", "runtime_loaded_verified richiede osservazione dello stesso package sulla superficie e static PASS"))
            if not package_valid or artifact.get("kind") != "installed_package" or artifact.get("source_candidate_id") != candidate_id or artifact.get("id") != package.get("package_id"):
                errors.append(issue("M010", f"{location}.artifact", "la sorgente candidata non può essere dichiarata pacchetto installato o caricato"))
        if state == "pilot_verified" and (not package_valid or artifact.get("kind") != "installed_package" or artifact.get("id") != package.get("package_id") or artifact.get("source_candidate_id") != candidate_id or surface not in SURFACE_IDS):
            errors.append(issue("M018", f"{location}.artifact", "pilot_verified richiede installed_package e superficie esatti"))
        if state == "pilot_verified":
            behavior_ready = has_record(records, prerequisites, lambda item: item.get("axis") == "behavior" and item.get("state") == "provenance_verified" and item.get("outcome") == "pass" and item.get("artifact", {}).get("id") == candidate_id)
            issue_ready = has_record(records, prerequisites, lambda item: item.get("axis") == "release" and item.get("state") == "provenance_verified" and item.get("outcome") == "pass" and item.get("observations", {}).get("release_check") == "issue_register")
            package_ready = has_record(records, prerequisites, lambda item: item.get("axis") == "release" and item.get("state") == "provenance_verified" and item.get("outcome") == "pass" and item.get("observations", {}).get("release_check") == "package_integrity")
            runtime_ready = has_record(records, prerequisites, lambda item: item.get("axis") == "runtime" and item.get("state") == "runtime_loaded_verified" and item.get("outcome") == "pass" and item.get("surface") == surface and item.get("artifact", {}).get("id") == (package.get("package_id") if package else None))
            if not behavior_ready or not issue_ready or not package_ready or not runtime_ready:
                errors.append(issue("M006", f"{location}.prerequisite_record_ids", "pilot_verified richiede provenance, issue register, package integrity e runtime loaded coerente"))
        observations = record.get("observations") if isinstance(record.get("observations"), dict) else {}
        validate_evidence(record.get("evidence"), str(axis), str(state), artifact, surface, observations, candidate, manifest, package, record_id, proof_context, external_index, f"{location}.evidence", errors)
        if not isinstance(record.get("observations"), dict) or not isinstance(record.get("limitations"), list) or any(not isinstance(item, str) for item in record.get("limitations", [])):
            errors.append(issue("M001", location, "observations o limitations non validi"))
        record_valid[record_id] = len(errors) == record_error_start

    for record_id, record in records.items():
        prerequisites = record.get("prerequisite_record_ids", [])
        if record.get("state") in HIGH_STATES and any(not record_valid.get(item, False) for item in prerequisites):
            errors.append(issue("M006", f"$.evidence_records[{record_id}].prerequisite_record_ids", "uno stato verificato dipende da un record invalido"))
            record_valid[record_id] = False
        if record.get("state") == "runtime_loaded_verified":
            key = (record.get("artifact", {}).get("id"), record.get("surface"))
            install_time = proof_context["install_times"].get(key)
            load_time = proof_context["load_times"].get(key)
            if install_time is None or load_time is None or install_time > load_time:
                errors.append(issue("M025", f"$.evidence_records[{record_id}]", "cronologia runtime richiede install_at <= load_at"))
                record_valid[record_id] = False
        if record.get("state") == "pilot_verified":
            pilot_info = proof_context["pilot_sessions"].get(record_id)
            relevant = [item for item in prerequisites if records.get(item, {}).get("state") in {"provenance_verified", "runtime_loaded_verified"}]
            prerequisite_times = [max(proof_context["record_times"].get(item, [])) for item in relevant if proof_context["record_times"].get(item)]
            runtime_key = (record.get("artifact", {}).get("id"), record.get("surface"))
            runtime_loaded_at = proof_context["load_times"].get(runtime_key)
            sessions_after_load = bool(
                pilot_info
                and runtime_loaded_at is not None
                and pilot_info.get("surface") == record.get("surface")
                and pilot_info.get("package_id") == record.get("artifact", {}).get("id")
                and pilot_info.get("candidate_id") == record.get("artifact", {}).get("source_candidate_id")
                and pilot_info["completed_at"] >= runtime_loaded_at
                and all(start >= runtime_loaded_at for start, _finish in pilot_info["sessions"])
            )
            if pilot_info is None or len(prerequisite_times) != len(relevant) or any(time >= pilot_info["completed_at"] for time in prerequisite_times) or not sessions_after_load:
                errors.append(issue("M025", f"$.evidence_records[{record_id}]", "pilot e sessioni devono iniziare dopo il runtime load coerente e completarsi dopo tutti i prerequisiti"))
                record_valid[record_id] = False

    forward = [item for item in records.values() if item.get("observations", {}).get("scenario") == "review_to_debrief_compaction"]
    if len(forward) != 1:
        errors.append(issue("M014", "$.evidence_records", "serve un solo record Review→Debrief compattato"))
    else:
        item = forward[0]
        obs = item["observations"]
        valid_forward = (
            item.get("artifact", {}).get("id") == candidate_id
            and item.get("state") == "observed_unverified"
            and item.get("outcome") == "pass"
            and obs.get("independent_forward_test") is True
            and obs.get("context_compaction_observed") is True
            and obs.get("reviewer_and_debriefer_separate") is True
            and obs.get("observed_value") == 7
            and obs.get("target_value") == 20
            and obs.get("gap_to_target") == 13
            and obs.get("target_value") - obs.get("observed_value") == obs.get("gap_to_target")
            and obs.get("causal_claim_made") is False
        )
        if not valid_forward:
            errors.append(issue("M014", "$.evidence_records.forward", "forward compattato non conserva ruoli, 7/20, scarto 13 e divieto causale"))

    beta9 = [item for item in records.values() if item.get("observations", {}).get("scenario") == "beta9_nine_skill_manual_run"]
    if len(beta9) != 1:
        errors.append(issue("M014", "$.evidence_records", "serve un solo record manuale beta.9 a nove skill"))
    else:
        item = beta9[0]
        obs = item["observations"]
        if item.get("artifact", {}).get("id") == candidate_id or item.get("state") != "observed_unverified" or item.get("outcome") != "issue_observed" or obs.get("skill_count") != 9 or obs.get("objective_loss_observed") is not True or obs.get("behavior_pass_normalized") is not False:
            errors.append(issue("M014", "$.evidence_records.beta9", "il run beta.9 deve restare storico, observed_unverified e non BEHAVIOR_PASS della candidata"))

    surface_list = report.get("runtime_surfaces")
    if not isinstance(surface_list, list):
        errors.append(issue("M001", "$.runtime_surfaces", "elenco richiesto"))
        surface_list = []
    surfaces: dict[str, dict[str, Any]] = {}
    surface_keys = {"id", "display_name", "artifact", "state", "outcome", "evidence_record_ids", "candidate_installed_verified", "runtime_loaded_verified", "limitations"}
    for index, surface_item in enumerate(surface_list):
        location = f"$.runtime_surfaces[{index}]"
        if not exact_keys(surface_item, surface_keys, location, errors):
            continue
        surface_id = surface_item.get("id")
        if surface_id not in SURFACE_IDS or surface_id in surfaces:
            errors.append(issue("M012", f"{location}.id", "superficie assente, duplicata o non prevista"))
            continue
        surfaces[surface_id] = surface_item
        artifact = validate_artifact(surface_item.get("artifact"), f"{location}.artifact", errors)
        state = surface_item.get("state")
        outcome = surface_item.get("outcome")
        evidence_ids = surface_item.get("evidence_record_ids")
        if not canonical_identifier_list(evidence_ids) or any(item not in records for item in evidence_ids):
            errors.append(issue("M006", f"{location}.evidence_record_ids", "record di evidenza runtime non risolvibili"))
            evidence_ids = []
        if state == "not_run":
            if outcome != "not_run" or evidence_ids or surface_item.get("candidate_installed_verified") is not False or surface_item.get("runtime_loaded_verified") is not False:
                errors.append(issue("M003", location, "not_run non può dichiarare outcome, installazione, caricamento o evidenze"))
        elif state == "observed_unverified":
            matching = has_record(records, evidence_ids, lambda item: item.get("state") == "observed_unverified" and item.get("surface") == surface_id and item.get("artifact", {}).get("id") == artifact.get("id"))
            if outcome not in {"pass", "issue_observed", "fail"} or not matching:
                errors.append(issue("M008", location, "observed_unverified richiede un'osservazione esterna coerente con superficie e artefatto"))
            if surface_item.get("candidate_installed_verified") is not False or surface_item.get("runtime_loaded_verified") is not False:
                errors.append(issue("M010", location, "un'osservazione non verificata non prova installazione o caricamento"))
        elif state == "runtime_loaded_verified":
            matching = has_record(records, evidence_ids, lambda item: record_valid.get(item.get("id", ""), False) and item.get("state") == "runtime_loaded_verified" and item.get("outcome") == "pass" and item.get("surface") == surface_id and item.get("artifact", {}).get("id") == artifact.get("id"))
            if outcome != "pass" or not matching or surface_item.get("candidate_installed_verified") is not True or surface_item.get("runtime_loaded_verified") is not True:
                errors.append(issue("M008", location, "runtime_loaded_verified richiede prova esterna, installazione e caricamento verificati"))
            if not package_valid or artifact.get("kind") != "installed_package" or artifact.get("source_candidate_id") != candidate_id or artifact.get("id") != package.get("package_id"):
                errors.append(issue("M010", f"{location}.artifact", "una sorgente candidata non è un pacchetto runtime installato"))
        else:
            errors.append(issue("M003", f"{location}.state", "stato runtime non valido"))
    if set(surfaces) != SURFACE_IDS:
        errors.append(issue("M012", "$.runtime_surfaces", f"superfici attese {sorted(SURFACE_IDS)}"))

    readiness = report.get("candidate_readiness")
    candidate_ready = False
    gate_states: dict[str, str] = {}
    if exact_keys(readiness, {"target", "required_gate_ids", "gates", "ready", "next_step"}, "$.candidate_readiness", errors):
        required = readiness.get("required_gate_ids")
        gates = readiness.get("gates")
        if not canonical_identifier_list(required) or set(required) != READINESS_GATE_IDS or not isinstance(gates, list):
            errors.append(issue("M012", "$.candidate_readiness", "set dei gate readiness incompleto"))
            gates = []
        gate_map: dict[str, dict[str, Any]] = {}
        for index, item in enumerate(gates):
            location = f"$.candidate_readiness.gates[{index}]"
            if not exact_keys(item, {"id", "state", "evidence_record_ids", "owner_role"}, location, errors):
                continue
            if not canonical_identifier(item.get("id")) or item.get("id") in gate_map or item.get("id") not in READINESS_GATE_IDS:
                errors.append(issue("M012", f"{location}.id", "gate readiness duplicato o non previsto"))
                continue
            if item.get("owner_role") not in OWNER_ROLES:
                errors.append(issue("M001", f"{location}.owner_role", "ownership deve essere generica"))
            gate_map[item["id"]] = item
        if set(gate_map) != READINESS_GATE_IDS:
            errors.append(issue("M012", "$.candidate_readiness.gates", "mancano gate readiness"))
        support = {
            "static-suite": [record_id for record_id, item in records.items() if record_valid.get(record_id) and item.get("axis") == "source" and item.get("artifact", {}).get("id") == candidate_id and item.get("state") == "static_only" and item.get("outcome") == "pass"],
            "compacted-forward": [record_id for record_id, item in records.items() if record_valid.get(record_id) and item.get("artifact", {}).get("id") == candidate_id and item.get("state") in {"observed_unverified", "provenance_verified"} and item.get("outcome") == "pass" and item.get("observations", {}).get("scenario") == "review_to_debrief_compaction"],
            "nine-skill-candidate-provenance": [record_id for record_id, item in records.items() if record_valid.get(record_id) and item.get("axis") == "behavior" and item.get("artifact", {}).get("id") == candidate_id and item.get("state") == "provenance_verified" and item.get("outcome") == "pass" and item.get("observations", {}).get("skill_count") == 9],
            "no-open-p0-p1": [record_id for record_id, item in records.items() if package_valid and record_valid.get(record_id) and item.get("axis") == "release" and item.get("artifact", {}).get("id") == package.get("package_id") and item.get("state") == "provenance_verified" and item.get("outcome") == "pass" and item.get("observations", {}).get("release_check") == "issue_register"],
            "package-parity-checksum": [record_id for record_id, item in records.items() if package_valid and record_valid.get(record_id) and item.get("axis") == "release" and item.get("artifact", {}).get("id") == package.get("package_id") and item.get("state") == "provenance_verified" and item.get("outcome") == "pass" and item.get("observations", {}).get("release_check") == "package_integrity"],
        }
        for gate_id, item in gate_map.items():
            expected = "satisfied" if support[gate_id] else "pending"
            gate_states[gate_id] = item.get("state")
            evidence_ids = item.get("evidence_record_ids")
            evidence_ids_ok = canonical_identifier_list(evidence_ids)
            if item.get("state") != expected or not evidence_ids_ok or any(ref not in records for ref in evidence_ids if isinstance(ref, str)) or (expected == "satisfied" and evidence_ids_ok and not set(evidence_ids).intersection(support[gate_id])):
                errors.append(issue("M011", f"$.candidate_readiness.gates.{gate_id}", f"stato o evidenza del gate divergente; atteso {expected}"))
        candidate_ready = package_valid and bool(gate_map) and all(item.get("state") == "satisfied" for item in gate_map.values())
        if readiness.get("ready") is not candidate_ready:
            errors.append(issue("M011", "$.candidate_readiness.ready", "ready non coincide con i gate"))
        next_step = readiness.get("next_step")
        if not exact_keys(next_step, {"action", "owner_role", "expected_evidence"}, "$.candidate_readiness.next_step", errors) or next_step.get("owner_role") not in OWNER_ROLES:
            errors.append(issue("M001", "$.candidate_readiness.next_step", "prossimo passo o ownership non validi"))

    pilot = report.get("pilot")
    pilot_keys = {"state", "outcome", "artifact_id", "artifact_kind", "source_candidate_id", "surface_id", "evidence_record_ids", "prerequisite_gate_ids", "real_marketer_verified", "owner_role"}
    pilot_verified = False
    if exact_keys(pilot, pilot_keys, "$.pilot", errors):
        if pilot.get("owner_role") != "pilot owner":
            errors.append(issue("M009", "$.pilot", "pilot e ownership non riferiti alla candidata"))
        ids = pilot.get("evidence_record_ids")
        prereq_gates = pilot.get("prerequisite_gate_ids")
        if not canonical_identifier_list(ids) or any(item not in records for item in ids if isinstance(item, str)):
            errors.append(issue("M009", "$.pilot.evidence_record_ids", "evidenze pilot non risolvibili"))
            ids = []
        if not canonical_identifier_list(prereq_gates) or set(prereq_gates) != {"nine-skill-candidate-provenance", "no-open-p0-p1", "package-parity-checksum"}:
            errors.append(issue("M006", "$.pilot.prerequisite_gate_ids", "prerequisiti pilot incompleti"))
        if pilot.get("state") == "not_run":
            if pilot.get("outcome") != "not_run" or ids or pilot.get("real_marketer_verified") is not False or pilot.get("artifact_id") != candidate_id or pilot.get("artifact_kind") != "source_candidate" or pilot.get("source_candidate_id") is not None or pilot.get("surface_id") is not None:
                errors.append(issue("M009", "$.pilot", "pilot not_run non può dichiarare evidenze o verifica"))
        elif pilot.get("state") == "pilot_verified":
            matching = has_record(records, ids, lambda item: record_valid.get(item.get("id", ""), False) and item.get("axis") == "pilot" and item.get("state") == "pilot_verified" and item.get("outcome") == "pass" and item.get("surface") == pilot.get("surface_id") and item.get("artifact", {}).get("id") == pilot.get("artifact_id"))
            prereqs_ok = all(gate_states.get(item) == "satisfied" for item in pilot.get("prerequisite_gate_ids", []))
            identity_ok = package_valid and pilot.get("artifact_id") == package.get("package_id") and pilot.get("artifact_kind") == "installed_package" and pilot.get("source_candidate_id") == candidate_id and pilot.get("surface_id") in SURFACE_IDS
            if pilot.get("outcome") != "pass" or pilot.get("real_marketer_verified") is not True or not matching or not identity_ok:
                errors.append(issue("M009", "$.pilot", "pilot_verified richiede prova esterna di marketer reale"))
            if not prereqs_ok:
                errors.append(issue("M006", "$.pilot.prerequisite_gate_ids", "pilot_verified salta gate candidati non soddisfatti"))
            pilot_verified = bool(matching and prereqs_ok and identity_ok and pilot.get("outcome") == "pass" and pilot.get("real_marketer_verified") is True)
        else:
            errors.append(issue("M003", "$.pilot.state", "stato pilot non valido"))

    later = report.get("later_promotion")
    later_ready = False
    if exact_keys(later, {"target", "gates", "ready"}, "$.later_promotion", errors):
        later_gates = later.get("gates")
        gate_map: dict[str, dict[str, Any]] = {}
        if not isinstance(later_gates, list):
            errors.append(issue("M001", "$.later_promotion.gates", "elenco richiesto"))
            later_gates = []
        for index, item in enumerate(later_gates):
            location = f"$.later_promotion.gates[{index}]"
            if not exact_keys(item, {"id", "state", "required_surface_ids", "owner_role"}, location, errors):
                continue
            gate_id = item.get("id")
            if not canonical_identifier(gate_id) or gate_id in gate_map:
                errors.append(issue("M012", f"{location}.id", "gate di promozione duplicato o non canonico"))
                continue
            gate_map[gate_id] = item
            if item.get("owner_role") not in OWNER_ROLES:
                errors.append(issue("M001", f"{location}.owner_role", "ownership deve essere generica"))
        if set(gate_map) != {"cross-runtime-refresh", "real-marketer-pilot"}:
            errors.append(issue("M012", "$.later_promotion.gates", "gate di promozione incompleti"))
        else:
            cross = gate_map["cross-runtime-refresh"]
            cross_ok = bool(
                candidate_ready
                and package_valid
                and set(cross.get("required_surface_ids", [])) == SURFACE_IDS
                and set(surfaces) == SURFACE_IDS
                and all(
                    item.get("state") == "runtime_loaded_verified"
                    and item.get("outcome") == "pass"
                    and item.get("candidate_installed_verified") is True
                    and item.get("runtime_loaded_verified") is True
                    and item.get("artifact", {}).get("kind") == "installed_package"
                    and item.get("artifact", {}).get("id") == package.get("package_id")
                    and item.get("artifact", {}).get("source_candidate_id") == candidate_id
                    and has_record(records, item.get("evidence_record_ids", []), lambda record: record_valid.get(record.get("id", ""), False) and record.get("state") == "runtime_loaded_verified" and record.get("outcome") == "pass")
                    for item in surfaces.values()
                )
            )
            pilot_gate = gate_map["real-marketer-pilot"]
            if cross.get("state") != ("satisfied" if cross_ok else "pending"):
                errors.append(issue("M011", "$.later_promotion.gates.cross-runtime-refresh", "stato cross-runtime divergente"))
            if pilot_gate.get("state") != ("satisfied" if pilot_verified else "pending"):
                errors.append(issue("M011", "$.later_promotion.gates.real-marketer-pilot", "stato pilot divergente"))
            later_ready = bool(candidate_ready and cross_ok and pilot_verified)
            if later.get("ready") is not later_ready:
                errors.append(issue("M011", "$.later_promotion.ready", "ready non coincide con i gate successivi"))

    return result(errors, candidate_ready, later_ready)


def result(errors: list[dict[str, str]], candidate_ready: bool, later_ready: bool) -> dict[str, Any]:
    matrix_valid = not errors
    return {
        "pass": matrix_valid,
        "matrix_valid": matrix_valid,
        "candidate_ready": bool(candidate_ready and matrix_valid),
        "later_promotion_ready": bool(later_ready and matrix_valid),
        "rule_ids": sorted({item["rule_id"] for item in errors}),
        "errors": errors,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--report", type=Path, default=DEFAULT_REPORT)
    parser.add_argument("--external-evidence-index", type=Path)
    args = parser.parse_args()
    outcome = validate(args.report.resolve(), args.external_evidence_index.resolve() if args.external_evidence_index else None)
    print(json.dumps(outcome, ensure_ascii=False, indent=2))
    return 0 if outcome["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
