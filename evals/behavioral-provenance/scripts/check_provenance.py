#!/usr/bin/env python3
"""Verify external Codex receipts, immutable host payloads and grounded normalization."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[1]
EVALS_ROOT = ROOT.parent
REPO_ROOT = EVALS_ROOT.parent
ALLOWLIST_PATH = ROOT / "runtime-allowlist.json"
RECEIPT_KEYS = {
    "schema_version", "invocation_id", "provider", "runtime", "thread_id",
    "turn_id", "message_id", "model", "skill_id", "skill_version",
    "skill_sha256", "input_path", "input_sha256", "output_path",
    "output_sha256", "captured_at", "previous_event_sha256", "event_sha256",
}
CAPTURE_KEYS = {
    "schema_version", "capture_id", "evidence_mode", "source_base_commit",
    "provider", "runtime", "thread_id", "model", "raw_manifest_path",
    "raw_manifest_sha256", "snapshot_path", "snapshot_sha256", "events",
}
CAPTURE_EVENT_KEYS = {"sequence", "skill_id", "receipt_path", "receipt_sha256"}
ENVELOPE_KEYS = {"schema_version", "capture_kind", "receipt_metadata", "payload"}
METADATA_KEYS = {
    "invocation_id", "provider", "runtime", "thread_id", "turn_id",
    "message_id", "model", "skill_id", "skill_version", "skill_sha256", "captured_at",
}
RAW_ROOT_KEYS_V4 = {
    "schema_version", "run_id", "capture_id", "proof_metadata", "events",
}
RAW_EVENT_KEYS_V4 = {
    "sequence", "skill", "skill_version", "receipt_path", "raw_input_path",
    "raw_input_sha256", "raw_response_path", "raw_response_sha256", "raw_input",
    "raw_output", "normalized_input", "input_normalizations", "normalized_output",
    "normalizations",
}
NORMALIZATION_KEYS = {"normalized_ref", "normalized_sha256", "transformation", "source", "location"}
PROOF_METADATA_KEYS = {"artifact_digests", "harness_ids"}
HARNESS_ID_KEYS = {"profile", "shared_invariant_ids", "scenario"}
SCENARIO_METADATA_KEYS = {"id", "version", "evidence_mode", "source_scope"}
FORBIDDEN_MODEL_METADATA_KEYS = {
    "capture_id", "run_id", "harness_id", "harness_ids", "profile",
    "shared_invariant_ids", "scenario_id",
}

ENUM_TRANSFORMS: dict[str, dict[str, str]] = {
    "authorization_state": {
        "autorizzato": "authorized", "autorizzata": "authorized", "ha autorizzato": "authorized",
        "non autorizzato": "not_authorized", "non autorizzata": "not_authorized",
        "paid non autorizzati": "not_authorized", "nessun paid": "not_authorized",
        "paid è rimasto non autorizzato": "not_authorized",
    },
    "execution_state": {
        "osservato": "observed", "osservata": "observed", "eseguito": "observed",
        "eseguita": "observed", "non osservato": "not_observed", "non osservata": "not_observed",
        "non eseguito": "not_observed", "non eseguita": "not_observed",
    },
    "tracking_state": {
        "verificato": "verified", "verificata": "verified", "non verificato": "unverified",
        "non verificata": "unverified", "verificati": "verified", "verificate": "verified",
    },
    "causality_state": {
        "non dimostrabile": "not_attributed", "non dimostrata": "not_attributed",
        "non attribuita": "not_attributed",
    },
    "roi_state": {"non calcolabile": "not_calculable"},
    "channel": {
        "linkedin organico": "linkedin_organic", "pubblicazione organica": "linkedin_organic",
    },
    "evidence_basis": {
        "evidenza operativa": "operational_evidence",
        "prontezza del sistema: verificata": "operational_evidence",
    },
    "target_state": {
        "confermato": "confermato", "confermata": "confermato",
        "baseline decisionale": "baseline", "atteso": "atteso",
    },
    "observation_subject": {"eseguito": "action", "eseguita": "action"},
    "organic_scope": {"pubblicazione organica": "organic_publication"},
    "simulation_mode": {"simulated": "simulated", "simulata": "simulated"},
}
ALLOWED_TRANSFORMS = {"identity", "integer", *ENUM_TRANSFORMS}


def issue(rule: str, location: str, message: str) -> dict[str, str]:
    return {"rule_id": rule, "location": location, "message": message}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def file_digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def object_digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def event_digest(receipt: dict[str, Any]) -> str:
    return object_digest({key: value for key, value in receipt.items() if key != "event_sha256"})


def valid_datetime(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).tzinfo is not None
    except ValueError:
        return False


def inside_repo(path: Path) -> bool:
    try:
        path.resolve().relative_to(REPO_ROOT.resolve())
        return True
    except ValueError:
        return False


def external_file(value: Any, location: str, errors: list[dict[str, str]]) -> Path | None:
    if not isinstance(value, str) or not value:
        errors.append(issue("P004", location, "percorso esterno mancante"))
        return None
    path = Path(value)
    if not path.is_absolute() or inside_repo(path) or not path.is_file():
        errors.append(issue("P004", location, "il file deve esistere, essere assoluto e restare fuori dal repository"))
        return None
    return path.resolve()


def get_pointer(document: Any, pointer: Any) -> Any:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise KeyError(pointer)
    cursor = document
    for token in pointer[1:].split("/"):
        token = token.replace("~1", "/").replace("~0", "~")
        cursor = cursor[int(token)] if isinstance(cursor, list) else cursor[token]
    return cursor


def package_digest(path: Path) -> str:
    rows: list[bytes] = []
    for file_path in sorted(item for item in path.rglob("*") if item.is_file()):
        relative = file_path.relative_to(path)
        if "__pycache__" in relative.parts or file_path.name == ".DS_Store":
            continue
        rows.append(str(relative).encode("utf-8") + b"\0" + file_digest(file_path).encode("ascii") + b"\n")
    return hashlib.sha256(b"".join(rows)).hexdigest()


def validate_source(allowlist: dict[str, Any], errors: list[dict[str, str]]) -> None:
    for index, skill in enumerate(allowlist.get("skills", [])):
        path = (REPO_ROOT / skill.get("path", "")).resolve()
        if not path.is_dir() or not path.is_relative_to(REPO_ROOT):
            errors.append(issue("P003", f"$.allowlist.skills[{index}].path", "package skill sorgente non risolto"))
            continue
        actual = package_digest(path)
        if actual != skill.get("skill_sha256"):
            errors.append(issue("P003", f"$.allowlist.skills[{index}].skill_sha256", f"digest package sorgente divergente: {actual}"))
        skill_file = path / "SKILL.md"
        text = skill_file.read_text(encoding="utf-8") if skill_file.is_file() else ""
        name_match = re.search(r"(?m)^name:\s*([^\n]+)$", text)
        version_match = re.search(r"(?m)^\s*version:\s*[\"']?([^\"'\n]+)[\"']?\s*$", text)
        source_name = name_match.group(1).strip().strip("\"'") if name_match else None
        source_version = version_match.group(1).strip() if version_match else None
        if source_name != skill.get("skill_id") or source_version != skill.get("skill_version"):
            errors.append(issue("P003", f"$.allowlist.skills[{index}]", "name o version non coincide con il front matter sorgente"))


def grounded_units(snapshot: dict[str, Any]) -> list[tuple[str, dict[str, Any]]]:
    units: list[tuple[str, dict[str, Any]]] = []
    values = [("$.identity", snapshot.get("identity"))]
    if snapshot.get("scenario", {}).get("profile") != "nine-skill-minimum-v1":
        values.append(("$.scenario", snapshot.get("scenario")))
    for location, value in values:
        if isinstance(value, dict):
            units.append((location, value))
    for category in ("artifacts", "invariants"):
        values = snapshot.get(category, [])
        if isinstance(values, list):
            units.extend((f"$.{category}[{index}]", value) for index, value in enumerate(values) if isinstance(value, dict))
    authorization = snapshot.get("authorization", {})
    if isinstance(authorization, dict):
        for category in ("decisions", "observations"):
            values = authorization.get(category, [])
            if isinstance(values, list):
                units.extend((f"$.authorization.{category}[{index}]", value) for index, value in enumerate(values) if isinstance(value, dict))
    lineage = snapshot.get("lineage", {})
    if isinstance(lineage, dict) and isinstance(lineage.get("edges"), list):
        units.extend((f"$.lineage.edges[{index}]", value) for index, value in enumerate(lineage["edges"]) if isinstance(value, dict))
    return units


def pointer_token(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def leaf_values(value: Any, pointer: str) -> Iterable[tuple[str, Any]]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield from leaf_values(item, f"{pointer}/{pointer_token(str(key))}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from leaf_values(item, f"{pointer}/{index}")
    else:
        yield pointer, value


def normalize_phrase(value: str) -> str:
    return " ".join(value.casefold().strip().split())


def apply_transform(identifier: Any, source: Any) -> tuple[bool, Any]:
    if identifier not in ALLOWED_TRANSFORMS:
        return False, None
    if identifier == "identity":
        return True, source
    if identifier == "integer":
        if isinstance(source, int) and not isinstance(source, bool):
            return True, source
        if isinstance(source, str) and re.fullmatch(r"[0-9]+", source.strip()):
            return True, int(source.strip())
        return False, None
    if not isinstance(source, str):
        return False, None
    mapped = ENUM_TRANSFORMS[identifier].get(normalize_phrase(source))
    return (mapped is not None), mapped


def locate_source(output_doc: Any, source: Any, location: str, errors: list[dict[str, str]]) -> Any:
    if not isinstance(source, dict) or source.get("kind") not in {"json_pointer", "text_range"}:
        errors.append(issue("P010", location, "localizzazione deve usare json_pointer o text_range"))
        return None
    pointer = source.get("pointer")
    if not isinstance(pointer, str) or not pointer.startswith("/payload"):
        errors.append(issue("P010", f"{location}.pointer", "la fonte deve restare nel payload host originale"))
        return None
    try:
        located = get_pointer(output_doc, pointer)
    except (KeyError, IndexError, TypeError, ValueError):
        errors.append(issue("P010", f"{location}.pointer", "JSON pointer host non risolto"))
        return None
    if source["kind"] == "json_pointer":
        if set(source) != {"kind", "pointer"}:
            errors.append(issue("P010", location, "campi json_pointer inattesi"))
            return None
        return located
    expected = {"kind", "pointer", "unit", "start", "end", "excerpt", "excerpt_sha256"}
    if set(source) != expected or not isinstance(located, str):
        errors.append(issue("P010", location, "text_range incompleto o fonte non testuale"))
        return None
    start, end, unit = source.get("start"), source.get("end"), source.get("unit")
    excerpt = source.get("excerpt")
    if not isinstance(start, int) or not isinstance(end, int) or start < 0 or end <= start or unit not in {"char", "byte"} or not isinstance(excerpt, str):
        errors.append(issue("P010", location, "offset text_range non validi"))
        return None
    try:
        if unit == "char":
            if end > len(located):
                raise ValueError("offset char fuori range")
            actual = located[start:end]
        else:
            encoded = located.encode("utf-8")
            if end > len(encoded):
                raise ValueError("offset byte fuori range")
            actual = encoded[start:end].decode("utf-8")
    except UnicodeDecodeError:
        errors.append(issue("P010", location, "offset byte spezza una sequenza UTF-8"))
        return None
    except ValueError as exc:
        errors.append(issue("P010", location, str(exc)))
        return None
    if actual != excerpt or source.get("excerpt_sha256") != hashlib.sha256(excerpt.encode("utf-8")).hexdigest():
        errors.append(issue("P010", location, "excerpt alterato, troncato o con digest divergente"))
        return None
    return actual


def forbidden_expected_fingerprints() -> tuple[set[str], set[str]]:
    digests: set[str] = set()
    texts: set[str] = set()
    for path in EVALS_ROOT.rglob("*"):
        if not path.is_file():
            continue
        lowered_parts = {part.casefold() for part in path.parts}
        if not ({"oracle", "oracles"} & lowered_parts) and "expected" not in path.name.casefold():
            continue
        try:
            data = path.read_bytes()
        except OSError:
            continue
        digests.add(hashlib.sha256(data).hexdigest())
        try:
            text = data.decode("utf-8").strip()
        except UnicodeDecodeError:
            continue
        if text:
            texts.add(text)
    return digests, texts


def scan_proof_fields(value: Any, location: str, errors: list[dict[str, str]]) -> None:
    if isinstance(value, dict):
        for key, item in value.items():
            lowered = key.casefold()
            if lowered in FORBIDDEN_MODEL_METADATA_KEYS or lowered in {"digest", "sha256"} or lowered.endswith(("_digest", "_sha256")):
                errors.append(issue("P014", f"{location}.{key}", "digest e metadati harness non sono fatti osservati"))
            scan_proof_fields(item, f"{location}.{key}", errors)
    elif isinstance(value, list):
        for index, item in enumerate(value):
            scan_proof_fields(item, f"{location}[{index}]", errors)


def validate_normalized_stream(
    raw: dict[str, Any],
    documents: dict[int, Any],
    normalized_key: str,
    normalizations_key: str,
    source_kind: str,
    expected_digests: set[str],
    expected_texts: set[str],
    errors: list[dict[str, str]],
) -> set[str]:
    coverage: set[str] = set()
    for index, event in enumerate(raw.get("events", [])):
        if not isinstance(event, dict):
            continue
        normalized = event.get(normalized_key)
        values = event.get(normalizations_key)
        if not isinstance(normalized, dict) or not isinstance(values, list):
            errors.append(issue("P010", f"$.raw.events[{index}]", f"{normalized_key} e {normalizations_key} sono obbligatori"))
            continue
        scan_proof_fields(normalized, f"$.raw.events[{index}].{normalized_key}", errors)
        if source_kind == "output" and any(key in normalized for key in {"authorization", "authorization_decision", "authorization_asset"}):
            errors.append(issue("P015", f"$.raw.events[{index}].{normalized_key}", "l'output del modello non può creare o promuovere autorizzazioni"))
        wanted_leaves = dict(leaf_values(normalized, f"/events/{index}/{normalized_key}"))
        seen: set[str] = set()
        for position, normalization in enumerate(values):
            loc = f"$.raw.events[{index}].{normalizations_key}[{position}]"
            if not isinstance(normalization, dict) or set(normalization) != NORMALIZATION_KEYS:
                errors.append(issue("P010", loc, "normalizzazione incompleta"))
                continue
            if normalization.get("source") != source_kind:
                errors.append(issue("P010", f"{loc}.source", f"normalizzazione {source_kind} collegata al flusso opposto"))
                continue
            ref = normalization.get("normalized_ref")
            if not isinstance(ref, str) or ref in seen or ref not in wanted_leaves:
                errors.append(issue("P010", f"{loc}.normalized_ref", f"riferimento foglia mancante, duplicato o esterno a {normalized_key}"))
                continue
            seen.add(ref)
            value = wanted_leaves[ref]
            if normalization.get("normalized_sha256") != object_digest(value):
                errors.append(issue("P010", f"{loc}.normalized_sha256", "digest del valore normalizzato divergente"))
            transform = normalization.get("transformation")
            transform_id = transform.get("id") if isinstance(transform, dict) and set(transform) == {"id"} else None
            if transform_id not in ALLOWED_TRANSFORMS:
                errors.append(issue("P012", f"{loc}.transformation", "trasformazione assente o non consentita"))
                continue
            source_value = locate_source(documents.get(index), normalization.get("location"), f"{loc}.location", errors)
            ok, derived = apply_transform(transform_id, source_value)
            if not ok or canonical(derived) != canonical(value):
                errors.append(issue("P012", loc, "valore normalizzato non derivabile deterministicamente dalla fonte host"))
            if isinstance(value, str) and (value in expected_digests or value.strip() in expected_texts):
                errors.append(issue("P013", ref, f"contenuto expected/oracle promosso a {normalized_key}"))
            coverage.add(ref)
        missing = sorted(set(wanted_leaves) - seen)
        if missing:
            errors.append(issue("P012", f"$.raw.events[{index}].{normalized_key}", f"foglie senza grounding: {missing}"))
    return coverage


def validate_normalized_content(raw: dict[str, Any], snapshot: dict[str, Any], input_docs: dict[int, Any], output_docs: dict[int, Any], errors: list[dict[str, str]]) -> None:
    expected_digests, expected_texts = forbidden_expected_fingerprints()
    coverage = validate_normalized_stream(raw, input_docs, "normalized_input", "input_normalizations", "input", expected_digests, expected_texts, errors)
    coverage.update(validate_normalized_stream(raw, output_docs, "normalized_output", "normalizations", "output", expected_digests, expected_texts, errors))

    for unit_location, unit in grounded_units(snapshot):
        ref = unit.get("source_ref")
        if not isinstance(ref, str) or not re.match(r"^/events/[0-8]/normalized_(?:input|output)(?:/|$)", ref):
            errors.append(issue("P010", f"{unit_location}.source_ref", "lo snapshot può riferire soltanto normalized_input o normalized_output"))
            continue
        if unit_location.startswith("$.authorization.decisions[") and "/normalized_input/" not in ref:
            errors.append(issue("P015", f"{unit_location}.source_ref", "una decisione di autorizzazione deve provenire dall'input host del committente o scenario"))
            continue
        try:
            source = get_pointer(raw, ref)
        except (KeyError, IndexError, TypeError, ValueError):
            errors.append(issue("P010", f"{unit_location}.source_ref", "source_ref normalizzato non risolto"))
            continue
        if not isinstance(source, dict):
            errors.append(issue("P010", f"{unit_location}.source_ref", "source_ref snapshot deve indicare un oggetto normalizzato"))
            continue
        source_leaves = {pointer for pointer, _ in leaf_values(source, ref)}
        if not source_leaves.issubset(coverage):
            errors.append(issue("P010", f"{unit_location}.source_ref", "oggetto snapshot non interamente grounded"))
        for evidence_ref in unit.get("evidence_refs", []) if isinstance(unit.get("evidence_refs"), list) else []:
            if not isinstance(evidence_ref, str) or not re.match(r"^/events/[0-8]/normalized_(?:input|output)(?:/|$)", evidence_ref):
                errors.append(issue("P010", f"{unit_location}.evidence_refs", "evidence_ref deve restare in normalized_input o normalized_output"))


def result(errors: list[dict[str, str]]) -> dict[str, Any]:
    return {"pass": not errors, "rule_ids": sorted({item["rule_id"] for item in errors}), "errors": errors}


def validate(capture_path: Path, raw_path: Path | None = None, snapshot_path: Path | None = None) -> dict[str, Any]:
    errors: list[dict[str, str]] = []
    try:
        allowlist = load_json(ALLOWLIST_PATH)
        validate_source(allowlist, errors)
        capture_resolved = capture_path.resolve()
        capture = load_json(capture_resolved)
        if not isinstance(capture, dict) or set(capture) != CAPTURE_KEYS or capture.get("schema_version") != "1.0.0" or capture.get("evidence_mode") != "behavioral_run":
            errors.append(issue("P001", "$", "forma capture manifest non valida"))
            return result(errors)
        if inside_repo(capture_resolved):
            errors.append(issue("P004", "$capture", "capture manifest comportamentale deve restare fuori dal repository"))
        if capture.get("source_base_commit") != allowlist.get("source_base_commit"):
            errors.append(issue("P003", "$.source_base_commit", "commit sorgente non consentito"))
        allowed_runtimes = {(item["provider"], item["runtime"]) for item in allowlist.get("provider_runtime_allowlist", [])}
        if (capture.get("provider"), capture.get("runtime")) not in allowed_runtimes:
            errors.append(issue("P002", "$.provider/runtime", "provider/runtime non presente in allowlist"))
        manifest_raw = external_file(capture.get("raw_manifest_path"), "$.raw_manifest_path", errors)
        manifest_snapshot = external_file(capture.get("snapshot_path"), "$.snapshot_path", errors)
        supplied_raw = raw_path.resolve() if raw_path else manifest_raw
        supplied_snapshot = snapshot_path.resolve() if snapshot_path else manifest_snapshot
        if manifest_raw and (capture.get("raw_manifest_sha256") != file_digest(manifest_raw) or supplied_raw != manifest_raw):
            errors.append(issue("P005", "$.raw_manifest_sha256", "raw manifest path o digest divergente"))
        if manifest_snapshot and (capture.get("snapshot_sha256") != file_digest(manifest_snapshot) or supplied_snapshot != manifest_snapshot):
            errors.append(issue("P005", "$.snapshot_sha256", "snapshot path o digest divergente"))
        if supplied_raw is None or supplied_snapshot is None or not supplied_raw.is_file() or not supplied_snapshot.is_file():
            errors.append(issue("P004", "$", "raw manifest o snapshot non risolto"))
            return result(errors)
        raw, snapshot = load_json(supplied_raw), load_json(supplied_snapshot)
        if not isinstance(raw, dict) or set(raw) != RAW_ROOT_KEYS_V4 or raw.get("schema_version") != "4.0.0" or raw.get("capture_id") != capture.get("capture_id"):
            errors.append(issue("P001", "$.raw", "raw v4 incompleto o non collegato alla capture"))
            return result(errors)
        proof_metadata = raw.get("proof_metadata")
        harness_ids = proof_metadata.get("harness_ids") if isinstance(proof_metadata, dict) else None
        scenario_metadata = harness_ids.get("scenario") if isinstance(harness_ids, dict) else None
        proof_metadata_ok = bool(
            isinstance(proof_metadata, dict)
            and set(proof_metadata) == PROOF_METADATA_KEYS
            and isinstance(proof_metadata.get("artifact_digests"), list)
            and isinstance(harness_ids, dict)
            and set(harness_ids) == HARNESS_ID_KEYS
            and isinstance(harness_ids.get("profile"), str)
            and isinstance(harness_ids.get("shared_invariant_ids"), list)
            and isinstance(scenario_metadata, dict)
            and set(scenario_metadata) == SCENARIO_METADATA_KEYS
        )
        if not proof_metadata_ok:
            errors.append(issue("P014", "$.raw.proof_metadata", "proof_metadata deve separare harness_ids e artifact_digests"))
        if not proof_metadata_ok or scenario_metadata.get("evidence_mode") != "behavioral_run" or snapshot.get("scenario", {}).get("evidence_mode") != "behavioral_run":
            errors.append(issue("P011", "$.scenario.evidence_mode", "behavioral_run non verificabile dalla capture"))
        allowed_skills = allowlist.get("skills", [])
        capture_events, raw_events = capture.get("events"), raw.get("events")
        if not isinstance(capture_events, list) or not isinstance(raw_events, list) or len(capture_events) != 9 or len(raw_events) != 9:
            errors.append(issue("P001", "$.events", "servono esattamente nove eventi"))
            return result(errors)
        used_paths: set[Path] = {capture_resolved, supplied_raw, supplied_snapshot}
        previous_hash: str | None = None
        input_docs: dict[int, Any] = {}
        output_docs: dict[int, Any] = {}
        for index, (wanted, captured, raw_event) in enumerate(zip(allowed_skills, capture_events, raw_events)):
            loc = f"$.events[{index}]"
            if not isinstance(captured, dict) or set(captured) != CAPTURE_EVENT_KEYS or not isinstance(raw_event, dict) or set(raw_event) != RAW_EVENT_KEYS_V4:
                errors.append(issue("P001", loc, "evento capture o raw v4 incompleto"))
                continue
            if captured.get("sequence") != index + 1 or raw_event.get("sequence") != index + 1 or captured.get("skill_id") != wanted.get("skill_id") or raw_event.get("skill") != wanted.get("skill_id") or raw_event.get("skill_version") != wanted.get("skill_version"):
                errors.append(issue("P003", loc, "ordine, id o versione skill divergente dall'allowlist"))
            receipt_path = external_file(captured.get("receipt_path"), f"{loc}.receipt_path", errors)
            input_path = external_file(raw_event.get("raw_input_path"), f"{loc}.raw_input_path", errors)
            output_path = external_file(raw_event.get("raw_response_path"), f"{loc}.raw_response_path", errors)
            for path in (receipt_path, input_path, output_path):
                if path is not None:
                    if path in used_paths:
                        errors.append(issue("P004", loc, f"file riusato tra eventi o ruoli: {path}"))
                    used_paths.add(path)
            if receipt_path is None or input_path is None or output_path is None:
                continue
            if captured.get("receipt_sha256") != file_digest(receipt_path):
                errors.append(issue("P006", f"{loc}.receipt_sha256", "digest file receipt divergente"))
            receipt = load_json(receipt_path)
            if not isinstance(receipt, dict) or set(receipt) != RECEIPT_KEYS or receipt.get("schema_version") != "1.0.0" or not valid_datetime(receipt.get("captured_at")):
                errors.append(issue("P001", f"{loc}.receipt", "receipt incompleta o timestamp senza timezone"))
                continue
            if receipt.get("event_sha256") != event_digest(receipt):
                errors.append(issue("P006", f"{loc}.receipt.event_sha256", "event_sha256 non ricomputabile"))
            if receipt.get("previous_event_sha256") != previous_hash:
                errors.append(issue("P007", f"{loc}.receipt.previous_event_sha256", "catena receipt interrotta"))
            previous_hash = receipt.get("event_sha256")
            if any(receipt.get(key) != wanted.get(key) for key in ("skill_id", "skill_version", "skill_sha256")):
                errors.append(issue("P003", f"{loc}.receipt", "identità o digest skill divergente dall'allowlist"))
            if (receipt.get("provider"), receipt.get("runtime")) not in allowed_runtimes:
                errors.append(issue("P002", f"{loc}.receipt", "provider/runtime receipt non consentito"))
            for key in ("provider", "runtime", "thread_id", "model"):
                if receipt.get(key) != capture.get(key):
                    errors.append(issue("P008", f"{loc}.receipt.{key}", "metadato receipt divergente dalla capture"))
            if receipt.get("input_path") != str(input_path) or receipt.get("output_path") != str(output_path):
                errors.append(issue("P004", f"{loc}.receipt", "path receipt divergenti dal raw manifest"))
            input_actual, output_actual = file_digest(input_path), file_digest(output_path)
            if receipt.get("input_sha256") != input_actual or raw_event.get("raw_input_sha256") != input_actual:
                errors.append(issue("P005", f"{loc}.input_sha256", "digest input divergente"))
            if receipt.get("output_sha256") != output_actual or raw_event.get("raw_response_sha256") != output_actual:
                errors.append(issue("P005", f"{loc}.output_sha256", "digest output divergente"))
            if raw_event.get("receipt_path") != str(receipt_path):
                errors.append(issue("P009", f"{loc}.receipt_path", "receipt raw e capture divergenti"))
            input_doc, output_doc = load_json(input_path), load_json(output_path)
            input_docs[index] = input_doc
            output_docs[index] = output_doc
            metadata = {key: receipt.get(key) for key in METADATA_KEYS}
            for kind, document in (("codex_invocation_input", input_doc), ("codex_invocation_output", output_doc)):
                if not isinstance(document, dict) or set(document) != ENVELOPE_KEYS or document.get("schema_version") != "1.0.0" or document.get("capture_kind") != kind or document.get("receipt_metadata") != metadata:
                    errors.append(issue("P008", f"{loc}.{kind}", "metadati host non coincidono con la receipt"))
            if input_doc.get("payload") != raw_event.get("raw_input"):
                errors.append(issue("P009", f"{loc}.raw_input", "raw_input non coincide byte-semantically con il payload host"))
            if output_doc.get("payload") != raw_event.get("raw_output"):
                errors.append(issue("P009", f"{loc}.raw_output", "raw_output non coincide byte-semantically con il payload host"))
        validate_normalized_content(raw, snapshot, input_docs, output_docs, errors)
    except (OSError, ValueError, KeyError, IndexError, TypeError, UnicodeDecodeError, json.JSONDecodeError) as exc:
        errors.append(issue("P001", "$", str(exc)))
    return result(errors)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--capture-manifest", type=Path, required=True)
    parser.add_argument("--raw", type=Path)
    parser.add_argument("--snapshot", type=Path)
    args = parser.parse_args()
    if bool(args.raw) != bool(args.snapshot):
        parser.error("--raw e --snapshot vanno forniti insieme")
    outcome = validate(args.capture_manifest, args.raw, args.snapshot)
    print(json.dumps(outcome, ensure_ascii=False, indent=2))
    return 0 if outcome["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
