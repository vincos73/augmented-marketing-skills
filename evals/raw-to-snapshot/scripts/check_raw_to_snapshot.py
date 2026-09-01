#!/usr/bin/env python3
"""Validate a nine-skill raw transcript and its fully grounded state snapshot."""

from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
import re
import sys
from pathlib import Path
from typing import Any


HERE = Path(__file__).resolve().parents[1]
EVALS_ROOT = HERE.parent
REPO_ROOT = EVALS_ROOT.parent
COMMON_CHECKER = EVALS_ROOT / "common" / "scripts" / "check_state_contract.py"
PROVENANCE_CHECKER = EVALS_ROOT / "behavioral-provenance" / "scripts" / "check_provenance.py"
EXPECTED_DEBRIEF = EVALS_ROOT / "campaign-lineage" / "fabriloom-evidence-readiness" / "oracles" / "expected-debrief.md"
ACTUAL_DEBRIEF = EVALS_ROOT / "campaign-lineage" / "fabriloom-evidence-readiness" / "fixture" / "debrief-actual.md"
INTEGRATED_CONTRACT = HERE / "integrated-profile-contract.json"
MINIMUM_CONTRACT = HERE / "minimum-behavior-contract.json"
SKILLS = [
    "setup-business-context",
    "setup-marketing-system",
    "define-marketing-challenge",
    "choose-marketing-direction",
    "define-marketing-mix",
    "design-campaign",
    "content-director",
    "campaign-review",
    "campaign-debrief",
]
MISSING = object()


def issue(rule: str, location: str, message: str) -> dict[str, str]:
    return {"rule_id": rule, "location": location, "message": message}


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def decode_pointer(pointer: str) -> list[str]:
    if not isinstance(pointer, str) or not pointer.startswith("/"):
        raise ValueError(f"JSON Pointer non valido: {pointer!r}")
    return [token.replace("~1", "/").replace("~0", "~") for token in pointer[1:].split("/")]


def get_pointer(document: Any, pointer: str) -> Any:
    try:
        cursor = document
        for token in decode_pointer(pointer):
            cursor = cursor[int(token)] if isinstance(cursor, list) else cursor[token]
        return cursor
    except (KeyError, IndexError, TypeError, ValueError):
        return MISSING


def mutate(document: Any, operation: dict[str, Any]) -> None:
    tokens = decode_pointer(operation["path"])
    cursor = document
    for token in tokens[:-1]:
        cursor = cursor[int(token)] if isinstance(cursor, list) else cursor[token]
    final = tokens[-1]
    op = operation["op"]
    if op == "remove":
        cursor.pop(int(final)) if isinstance(cursor, list) else cursor.pop(final)
    elif op == "replace":
        if isinstance(cursor, list):
            cursor[int(final)] = copy.deepcopy(operation["value"])
        else:
            if final not in cursor:
                raise KeyError(operation["path"])
            cursor[final] = copy.deepcopy(operation["value"])
    elif op == "add":
        if isinstance(cursor, list):
            cursor.insert(int(final), copy.deepcopy(operation["value"]))
        else:
            cursor[final] = copy.deepcopy(operation["value"])
    else:
        raise ValueError(f"operazione non supportata: {op}")


def common_validate(snapshot: Any) -> list[dict[str, str]]:
    spec = importlib.util.spec_from_file_location("state_contract", COMMON_CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("checker del contratto comune non caricabile")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate(snapshot)


def provenance_validate(capture_manifest: Path, raw_path: Path, snapshot_path: Path) -> list[dict[str, str]]:
    spec = importlib.util.spec_from_file_location("behavioral_provenance", PROVENANCE_CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("checker di provenance non caricabile")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.validate(capture_manifest.resolve(), raw_path.resolve(), snapshot_path.resolve())["errors"]


def semantic(value: dict[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(item) for key, item in value.items() if key != "source_ref"}


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


def validate_grounding(raw: dict[str, Any], snapshot: dict[str, Any]) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    behavioral_v4 = raw.get("schema_version") == "4.0.0"
    for location, unit in grounded_units(snapshot):
        source_ref = unit.get("source_ref")
        if behavioral_v4 and (not isinstance(source_ref, str) or not re.match(r"^/events/[0-8]/normalized_(?:input|output)(?:/|$)", source_ref)):
            errors.append(issue("R023", f"{location}.source_ref", "snapshot comportamentale deve riferire normalized_input o normalized_output"))
        if behavioral_v4 and location.startswith("$.authorization.decisions[") and (not isinstance(source_ref, str) or "/normalized_input/" not in source_ref):
            errors.append(issue("R017", f"{location}.source_ref", "autorizzazione valida soltanto da normalized_input del committente o scenario"))
        source = get_pointer(raw, source_ref) if isinstance(source_ref, str) else MISSING
        if source is MISSING:
            errors.append(issue("R002", f"{location}.source_ref", f"evidenza raw non risolta: {source_ref!r}"))
        elif not isinstance(source, dict) or semantic(unit) != source:
            errors.append(issue("R003", location, "oggetto snapshot non coincide localmente con l'oggetto raw indicato"))
        evidence_refs = unit.get("evidence_refs", [])
        if isinstance(evidence_refs, list):
            for evidence_ref in evidence_refs:
                if behavioral_v4 and (not isinstance(evidence_ref, str) or "/normalized_output/" not in evidence_ref):
                    errors.append(issue("R023", f"{location}.evidence_refs", "evidence_ref comportamentale deve riferire normalized_output"))
                if get_pointer(raw, evidence_ref) is MISSING:
                    errors.append(issue("R005", f"{location}.evidence_refs", f"evidenza raw non risolta: {evidence_ref}"))
    return errors


def find_invariant(raw: dict[str, Any], identifier: str) -> dict[str, Any] | None:
    for event in raw.get("events", []):
        output = event.get("raw_output", {}) if isinstance(event, dict) else {}
        for item in output.get("invariants", []) if isinstance(output, dict) else []:
            if isinstance(item, dict) and item.get("id") == identifier:
                return item
    return None


def nested_values(value: Any, key: str) -> list[Any]:
    found: list[Any] = []
    if isinstance(value, dict):
        for name, item in value.items():
            if name == key:
                found.append(item)
            found.extend(nested_values(item, key))
    elif isinstance(value, list):
        for item in value:
            found.extend(nested_values(item, key))
    return found


def validate_fabriloom_contract(raw: dict[str, Any], snapshot: dict[str, Any], require_behavior: bool) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    integrated = load_json(INTEGRATED_CONTRACT)
    schema_version = raw.get("schema_version")
    expected_root = {"schema_version", "run_id", "profile", "identity", "scenario", "shared_invariant_ids", "events"}
    if set(raw) != expected_root or schema_version != "2.0.0":
        errors.append(issue("R001", "$", "forma o versione raw non valida"))
    if raw.get("profile") != snapshot.get("scenario", {}).get("profile"):
        errors.append(issue("R001", "$.profile", "profilo raw e snapshot divergente"))
    if raw.get("profile") != integrated["profile"] or raw.get("scenario", {}).get("id") != integrated["scenario_id"] or snapshot.get("scenario", {}).get("id") != integrated["scenario_id"]:
        errors.append(issue("R014", "$.scenario", "profilo o scenario integrato post-execution divergente"))
    if raw.get("shared_invariant_ids") != snapshot.get("shared_invariant_ids"):
        errors.append(issue("R009", "$.shared_invariant_ids", "identificatori condivisi raw e snapshot divergenti"))
    if raw.get("shared_invariant_ids") != integrated["shared_invariant_ids"]:
        errors.append(issue("R009", "$.shared_invariant_ids", "identificatori condivisi divergenti dal contratto integrato"))
    events = raw.get("events")
    if not isinstance(events, list) or len(events) != 9:
        errors.append(issue("R001", "$.events", "servono esattamente nove eventi di skill"))
        return errors
    actual_skills = [event.get("skill") if isinstance(event, dict) else None for event in events]
    if actual_skills != SKILLS:
        errors.append(issue("R001", "$.events", f"ordine skill inatteso: {actual_skills!r}"))
    expected_event_keys = {"sequence", "skill", "skill_version", "raw_output"}
    for index, event in enumerate(events):
        if not isinstance(event, dict) or set(event) != expected_event_keys or event.get("sequence") != index + 1 or not isinstance(event.get("raw_output"), dict):
            errors.append(issue("R001", f"$.events[{index}]", "evento raw incompleto o fuori ordine"))

    evidence_mode = raw.get("scenario", {}).get("evidence_mode") if isinstance(raw.get("scenario"), dict) else None
    if require_behavior and evidence_mode != "behavioral_run":
        errors.append(issue("R010", "$.scenario.evidence_mode", "il gate comportamentale richiede behavioral_run"))

    tracking_states = []
    for index in range(integrated["pre_boundary_stage_count"]):
        invariants = get_pointer(raw, f"/events/{index}/raw_output/invariants")
        tracking_item = next((item for item in invariants if isinstance(item, dict) and item.get("id") == "TRK-FAB-ERS-OWNED@1"), None) if isinstance(invariants, list) else None
        tracking_states.append(tracking_item.get("status") if isinstance(tracking_item, dict) else None)
    if tracking_states != [integrated["tracking_pre_boundary_state"]] * integrated["pre_boundary_stage_count"]:
        errors.append(issue("R012", "$.events[0:5]", f"tracking deve restare unverified nei primi cinque stadi: {tracking_states!r}"))

    review_event = get_pointer(raw, "/events/7/raw_output/review_event")
    auth_event = get_pointer(raw, "/events/7/raw_output/authorization_event")
    execution_event = get_pointer(raw, "/events/8/raw_output/execution_event")
    if not isinstance(review_event, dict) or not isinstance(auth_event, dict) or not isinstance(execution_event, dict):
        errors.append(issue("R006", "$.events[7:9]", "review, autorizzazione o esecuzione esplicita mancante"))
    else:
        required_auth = {
            "event_ref": "AUTH-FAB-ERS-ORGANIC@1",
            "asset_ref": "ASSET-FAB-ERS-CAROUSEL@1",
            "review_ref": "REVIEW-FAB-ERS-PRELAUNCH@2",
            "scope": ["linkedin_organic"],
            "authority": "Marketing Director",
            "provenance": "simulated",
        }
        if any(auth_event.get(key) != value for key, value in required_auth.items()):
            errors.append(issue("R006", "$.events[7].raw_output.authorization_event", "evento di autorizzazione incompleto o promosso"))
        decision = auth_event.get("decision", {})
        if not isinstance(decision, dict) or decision.get("id") != "AUTH-FAB-ERS-ORGANIC@1" or decision.get("mode") != "simulated" or decision.get("status") != "authorized":
            errors.append(issue("R006", "$.events[7].raw_output.authorization_event.decision", "review usata come autorizzazione o provenienza simulata persa"))
        indices = (review_event.get("trace_index"), auth_event.get("trace_index"), execution_event.get("trace_index"))
        if not all(isinstance(value, int) for value in indices) or not indices[0] < indices[1] < indices[2]:
            errors.append(issue("R006", "$.events[7:9]", "ordine richiesto review -> authorization -> execution non rispettato"))
        if execution_event.get("authorization_ref") != "AUTH-FAB-ERS-ORGANIC@1":
            errors.append(issue("R006", "$.events[8].raw_output.execution_event.authorization_ref", "esecuzione non collegata all'autorizzazione esplicita"))
    organic = next((item for item in snapshot.get("authorization", {}).get("decisions", []) if item.get("id") == "AUTH-FAB-ERS-ORGANIC@1"), None)
    if not organic or organic.get("source_ref") != "/events/7/raw_output/authorization_event/decision" or organic.get("mode") != "simulated":
        errors.append(issue("R006", "$.authorization.decisions", "autorizzazione organica assente, dedotta dalla review o promossa a osservata"))

    speed_60 = find_invariant(raw, "speed-60")
    speed_42 = find_invariant(raw, "speed-42-conditional")
    sales = find_invariant(raw, "sales-weekly-qualified-calls")
    tracking = get_pointer(raw, "/events/5/raw_output/tracking_verification")
    formula = "Nei tre progetti pilota osservati, il tempo dichiarato per preparare un questionario si è ridotto in mediana del 42%. Il campione è limitato e i risultati non sono garantiti."
    if speed_60 != {"id": "speed-60", "status": "forbidden"}:
        errors.append(issue("R009", "speed-60", "claim 60 non conservato come vietato"))
    if speed_42 != {"id": "speed-42-conditional", "status": "conditional", "value": {"formula": formula, "approval_required": "legal"}}:
        errors.append(issue("R009", "speed-42-conditional", "formula condizionale del 42% o gate Legal incompleto"))
    expected_sales = {"id": "sales-weekly-qualified-calls", "status": "hard_ceiling", "value": {"limit": 6, "unit": "qualified_calls", "window": "week", "follow_up_sla_business_days": 2}}
    if sales != expected_sales:
        errors.append(issue("R009", "sales-weekly-qualified-calls", "vincolo Sales incompleto"))
    if not isinstance(tracking, dict) or tracking.get("id") != integrated["tracking_id"] or tracking.get("status") != "verified" or not isinstance(tracking.get("value"), dict):
        errors.append(issue("R009", "TRK-FAB-ERS-OWNED@1", "tracking non verificato o non risolvibile"))
    else:
        evidence_ref = tracking["value"].get("evidence_ref")
        if evidence_ref != integrated["tracking_evidence_ref"]:
            errors.append(issue("R009", "TRK-FAB-ERS-OWNED@1", "evidenza tracking divergente dal contratto integrato"))
        evidence_path = (REPO_ROOT / evidence_ref).resolve() if isinstance(evidence_ref, str) else None
        if evidence_path is None or not evidence_path.is_relative_to(REPO_ROOT) or not evidence_path.is_file():
            errors.append(issue("R009", "TRK-FAB-ERS-OWNED@1", "evidenza tracking non risolta nel repository"))
        else:
            evidence_text = evidence_path.read_text(encoding="utf-8")
            if "TRK-FAB-ERS-OWNED@1" not in evidence_text or tracking["value"].get("test_ref") not in evidence_text:
                errors.append(issue("R009", "TRK-FAB-ERS-OWNED@1", "evidenza tracking non contiene id e test dichiarati"))

    for index, artifact in enumerate(snapshot.get("artifacts", [])):
        if not isinstance(artifact, dict):
            continue
        state = artifact.get("state")
        location = f"$.artifacts[{index}]"
        if state == "provided_by_external_evidence":
            evidence_ref = artifact.get("evidence_ref")
            evidence_path = Path(evidence_ref) if isinstance(evidence_ref, str) else None
            if evidence_path is not None and not evidence_path.is_absolute():
                evidence_path = (REPO_ROOT / evidence_path).resolve()
            if evidence_path is None or not evidence_path.is_file():
                errors.append(issue("R013", f"{location}.evidence_ref", "evidenza esterna dell'artefatto non risolta"))
            else:
                wanted_digest = artifact.get("digest", {}).get("value") if isinstance(artifact.get("digest"), dict) else None
                if hashlib.sha256(evidence_path.read_bytes()).hexdigest() != wanted_digest:
                    errors.append(issue("R013", f"{location}.digest", "digest artefatto divergente dal file fornito"))
        elif state == "persistent":
            decisions = snapshot.get("authorization", {}).get("decisions", [])
            observations = snapshot.get("authorization", {}).get("observations", [])
            authorized_save_ids = {
                item.get("id") for item in decisions
                if isinstance(item, dict) and item.get("status") == "authorized" and "write_file" in item.get("scope", [])
            }
            observed_save = any(
                isinstance(item, dict) and item.get("subject") == "action" and item.get("status") == "observed" and item.get("decision_id") in authorized_save_ids
                for item in observations
            )
            if not authorized_save_ids or not observed_save:
                errors.append(issue("R013", location, "artefatto persistent senza save autorizzato e osservato"))

    spec_artifact = next((item for item in snapshot.get("artifacts", []) if isinstance(item, dict) and item.get("ref") == "SPEC-FAB-ERS@1"), None)
    if not spec_artifact or spec_artifact.get("state") != integrated["campaign_spec_route"]:
        errors.append(issue("R013", "$.artifacts", "la Campaign Spec Fabriloom deve usare la route provided_by_external_evidence"))
    paid = next((item for item in snapshot.get("invariants", []) if isinstance(item, dict) and item.get("id") == "paid-media"), None)
    active_decisions = [item for item in snapshot.get("authorization", {}).get("decisions", []) if isinstance(item, dict) and item.get("status") in {"authorized", "approved"}]
    observed_actions = [
        item.get("id") for item in snapshot.get("authorization", {}).get("observations", [])
        if isinstance(item, dict) and item.get("subject") == "action" and item.get("status") == "observed"
    ]
    if not paid or paid.get("status") != integrated["paid_invariant_state"] or [item.get("id") for item in active_decisions] != integrated["authorized_decision_ids_at_debrief"] or observed_actions != integrated["observed_action_ids_at_debrief"]:
        errors.append(issue("R014", "$.authorization", "nel profilo integrato soltanto l'organico può risultare autorizzato; paid resta non autorizzato"))

    if evidence_mode == "synthetic_fixture":
        invalid_modes = [value for value in nested_values(raw.get("events"), "mode") if value != integrated["synthetic_event_mode"]]
        invalid_provenance = [value for value in nested_values(raw.get("events"), "provenance") if value != integrated["synthetic_event_mode"]]
        if invalid_modes or invalid_provenance:
            errors.append(issue("R015", "$.events", "tutte le decisioni, osservazioni e provenance sintetiche devono usare simulated"))

    results_event = get_pointer(raw, "/events/8/raw_output/results_event")
    debrief_event = get_pointer(raw, "/events/8/raw_output/debrief_event")
    expected_digest = hashlib.sha256(EXPECTED_DEBRIEF.read_bytes()).hexdigest()
    actual_fixture_digest = hashlib.sha256(ACTUAL_DEBRIEF.read_bytes()).hexdigest()
    if not isinstance(results_event, dict) or not isinstance(results_event.get("metrics"), dict) or results_event["metrics"].get("source_coverage") != "9/9":
        errors.append(issue("R008", "$.events[8].raw_output.results_event", "risultati effettivi non supportati dal raw"))
    if not isinstance(debrief_event, dict):
        errors.append(issue("R008", "$.events[8].raw_output.debrief_event", "debrief effettivo mancante"))
    else:
        artifact = debrief_event.get("artifact", {})
        debrief_digest = artifact.get("digest", {}).get("value") if isinstance(artifact, dict) else None
        if debrief_digest == expected_digest:
            errors.append(issue("R004", "$.events[8].raw_output.debrief_event.artifact.digest", "digest dell'oracolo expected usato come output osservato"))
        if evidence_mode == "synthetic_fixture" and debrief_digest != actual_fixture_digest:
            errors.append(issue("R008", "$.events[8].raw_output.debrief_event.artifact.digest", "digest del debrief effettivo non corrisponde alla fixture actual"))
        expected_refs = {"expected_ref": "SPEC-FAB-ERS@1", "executed_ref": "EXEC-FAB-ERS@1", "observed_ref": "RESULTS-FAB-ERS@1", "causality": "not_attributed"}
        if any(debrief_event.get(key) != value for key, value in expected_refs.items()):
            errors.append(issue("R008", "$.events[8].raw_output.debrief_event", "confronto atteso/eseguito/osservato incompleto"))
    return errors


def normalized_event(raw: dict[str, Any], index: int) -> dict[str, Any]:
    value = get_pointer(raw, f"/events/{index}/normalized_output")
    return value if isinstance(value, dict) else {}


def normalized_input_event(raw: dict[str, Any], index: int) -> dict[str, Any]:
    value = get_pointer(raw, f"/events/{index}/normalized_input")
    return value if isinstance(value, dict) else {}


def v4_harness_ids(raw: dict[str, Any]) -> dict[str, Any]:
    proof = raw.get("proof_metadata")
    harness = proof.get("harness_ids") if isinstance(proof, dict) else None
    return harness if isinstance(harness, dict) else {}


def normalization_position(raw: dict[str, Any], event_index: int, ref: str, input_stream: bool = False) -> tuple[int, int, int] | None:
    values = get_pointer(raw, f"/events/{event_index}/{'input_normalizations' if input_stream else 'normalizations'}")
    if not isinstance(values, list):
        return None
    for item in values:
        if not isinstance(item, dict) or item.get("normalized_ref") != ref:
            continue
        location = item.get("location", {})
        start = location.get("start", 0) if isinstance(location, dict) else 0
        return event_index, 0 if input_stream else 1, start if isinstance(start, int) else 0
    return None


def validate_minimum_contract(raw: dict[str, Any], snapshot: dict[str, Any], require_behavior: bool) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    contract = load_json(MINIMUM_CONTRACT)
    root_keys = {
        "schema_version", "run_id", "capture_id", "proof_metadata", "events",
    }
    event_keys = {
        "sequence", "skill", "skill_version", "receipt_path", "raw_input_path",
        "raw_input_sha256", "raw_response_path", "raw_response_sha256", "raw_input",
        "raw_output", "normalized_input", "input_normalizations", "normalized_output",
        "normalizations",
    }
    if set(raw) != root_keys or raw.get("schema_version") != "4.0.0":
        errors.append(issue("R001", "$", "forma raw comportamentale v4 non valida"))
        return errors
    harness_ids = v4_harness_ids(raw)
    scenario_metadata = harness_ids.get("scenario") if isinstance(harness_ids.get("scenario"), dict) else {}
    if harness_ids.get("profile") != contract.get("profile") or snapshot.get("scenario", {}).get("profile") != contract.get("profile"):
        errors.append(issue("R001", "$.profile", "profilo minimo raw e snapshot divergente"))
    if harness_ids.get("shared_invariant_ids") != snapshot.get("shared_invariant_ids") or harness_ids.get("shared_invariant_ids") != contract.get("shared_invariant_ids"):
        errors.append(issue("R001", "$.shared_invariant_ids", "invarianti del profilo minimo divergenti"))
    expected_scenario = {key: snapshot.get("scenario", {}).get(key) for key in ("id", "version", "evidence_mode", "source_scope")}
    if scenario_metadata != expected_scenario:
        errors.append(issue("R001", "$.proof_metadata.harness_ids.scenario", "metadati scenario e snapshot divergenti"))
    events = raw.get("events")
    if not isinstance(events, list) or len(events) != 9:
        errors.append(issue("R001", "$.events", "servono esattamente nove eventi"))
        return errors
    actual_skills = [item.get("skill") if isinstance(item, dict) else None for item in events]
    if actual_skills != SKILLS:
        errors.append(issue("R001", "$.events", f"ordine skill inatteso: {actual_skills!r}"))
    for index, event in enumerate(events):
        if not isinstance(event, dict) or set(event) != event_keys or event.get("sequence") != index + 1 or not isinstance(event.get("normalized_input"), dict) or not isinstance(event.get("normalized_output"), dict):
            errors.append(issue("R001", f"$.events[{index}]", "evento comportamentale v4 incompleto"))
    evidence_mode = scenario_metadata.get("evidence_mode")
    if require_behavior and evidence_mode != "behavioral_run":
        errors.append(issue("R010", "$.scenario.evidence_mode", "il gate comportamentale richiede behavioral_run"))

    expected_target = contract["target"]
    expected_result = contract["result"]
    expected_metric = contract["metric"]
    challenge_target = normalized_event(raw, 2).get("campaign_target")
    review = normalized_event(raw, 7).get("review")
    debrief = normalized_event(raw, 8).get("debrief")
    targets = [challenge_target, review.get("target") if isinstance(review, dict) else None, debrief.get("target") if isinstance(debrief, dict) else None]
    allowed_statuses = ({"confermato"}, {"confermato", "baseline"}, {"confermato", "atteso"})
    if any(
        not isinstance(item, dict)
        or item.get("status") not in allowed_status
        or item.get("value", {}).get("metric") != expected_metric
        or item.get("value", {}).get("target") != expected_target
        for item, allowed_status in zip(targets, allowed_statuses)
    ):
        errors.append(issue("R016", "$.events[2,7,8].normalized_output", "target 20 e metrica devono restare continui fino a review e debrief"))

    turn_nine_input = normalized_input_event(raw, 8)
    authorization = turn_nine_input.get("authorization_decision")
    authorization_asset = turn_nine_input.get("authorization_asset")
    authorization_paid = turn_nine_input.get("paid")
    execution = normalized_event(raw, 8).get("execution")
    execution_observation = normalized_event(raw, 8).get("execution_observation")
    auth_state_ref = "/events/8/normalized_input/authorization_decision/status"
    execution_state_ref = "/events/8/normalized_output/execution/state"
    auth_position = normalization_position(raw, 8, auth_state_ref, input_stream=True)
    execution_position = normalization_position(raw, 8, execution_state_ref)
    auth_ok = bool(
        isinstance(authorization, dict)
        and authorization.get("status") == "authorized"
        and authorization.get("mode") == "simulated"
        and authorization.get("authority") == "Marketing Director"
        and authorization.get("scope") == ["organic_publication"]
        and isinstance(authorization_asset, dict)
        and set(authorization_asset) == {"id", "version"}
        and isinstance(authorization_paid, dict)
        and authorization_paid.get("status") == "not_authorized"
    )
    execution_ok = isinstance(execution, dict) and execution.get("state") == "observed"
    observation_ok = bool(
        isinstance(execution_observation, dict)
        and isinstance(authorization, dict)
        and execution_observation.get("subject") == "action"
        and execution_observation.get("decision_id") == authorization.get("id")
        and execution_observation.get("status") == "observed"
        and execution_observation.get("mode") == "simulated"
    )
    snapshot_decisions = snapshot.get("authorization", {}).get("decisions", [])
    snapshot_auth_ok = any(
        isinstance(item, dict)
        and item.get("source_ref") == "/events/8/normalized_input/authorization_decision"
        and semantic(item) == authorization
        for item in snapshot_decisions
    )
    if not auth_ok or not execution_ok or not observation_ok or not snapshot_auth_ok or auth_position is None or execution_position is None or auth_position >= execution_position:
        errors.append(issue("R017", "$.events[8].normalized_input", "autorizzazione del committente grounded nell'input e precedente all'esecuzione osservata richiesta"))

    review_asset = review.get("asset") if isinstance(review, dict) else None
    execution_asset = execution.get("asset") if isinstance(execution, dict) else None
    authorization_asset_ok = bool(
        isinstance(review_asset, dict)
        and isinstance(authorization_asset, dict)
        and authorization_asset.get("id") == review_asset.get("id")
        and authorization_asset.get("version") == review_asset.get("version")
    )
    if not isinstance(review_asset, dict) or review_asset != execution_asset or set(review_asset) != {"id", "version", "channel"} or not authorization_asset_ok:
        errors.append(issue("R018", "$.events[7:9].normalized_output", "asset, versione e canale devono coincidere tra review, autorizzazione ed esecuzione"))

    paid = normalized_event(raw, 3).get("paid")
    if not isinstance(paid, dict) or paid.get("status") != "not_authorized" or not isinstance(authorization_paid, dict) or authorization_paid.get("status") != "not_authorized" or not isinstance(debrief, dict) or debrief.get("paid_state") != "not_authorized":
        errors.append(issue("R019", "$.events[3,8].normalized_output", "paid deve restare non autorizzato"))

    tracking_values: list[tuple[int, dict[str, Any]]] = []
    for index in range(9):
        item = normalized_event(raw, index).get("tracking")
        if isinstance(item, dict):
            tracking_values.append((index, item))
    minimum_index = int(contract["tracking_verified_min_sequence"]) - 1
    early = [index for index, item in tracking_values if item.get("status") == "verified" and index < minimum_index]
    verified = [item for index, item in tracking_values if index >= minimum_index and item.get("status") == "verified" and item.get("value", {}).get("basis") == "operational_evidence"]
    if early or not verified or not isinstance(debrief, dict) or debrief.get("tracking_state") != "verified":
        errors.append(issue("R020", "$.events.normalized_output.tracking", "tracking verificato solo dopo evidenza operativa e conservato nel debrief"))

    if not isinstance(debrief, dict) or debrief.get("result") != expected_result or debrief.get("target", {}).get("value", {}).get("target") != expected_target:
        errors.append(issue("R021", "$.events[8].normalized_output.debrief", "debrief deve conservare 7 risultati su target 20"))
    if not isinstance(debrief, dict) or debrief.get("causality") != "not_attributed" or debrief.get("roi") != "not_calculable":
        errors.append(issue("R022", "$.events[8].normalized_output.debrief", "causalità e ROI non supportati non possono essere attribuiti"))
    return errors


def validate_raw_contract(raw: dict[str, Any], snapshot: dict[str, Any], require_behavior: bool) -> list[dict[str, str]]:
    if raw.get("schema_version") == "2.0.0":
        return validate_fabriloom_contract(raw, snapshot, require_behavior)
    if raw.get("schema_version") == "4.0.0":
        return validate_minimum_contract(raw, snapshot, require_behavior)
    return [issue("R001", "$.schema_version", "sono supportati raw statici 2.0.0 o comportamentali 4.0.0")]


def validate_case(raw: Any, snapshot: Any, require_behavior: bool = False, capture_manifest: Path | None = None, raw_path: Path | None = None, snapshot_path: Path | None = None) -> dict[str, Any]:
    errors: list[dict[str, str]] = []
    if not isinstance(raw, dict) or not isinstance(snapshot, dict):
        errors.append(issue("R001", "$", "raw e snapshot devono essere oggetti JSON"))
    else:
        errors.extend(common_validate(snapshot))
        errors.extend(validate_raw_contract(raw, snapshot, require_behavior))
        errors.extend(validate_grounding(raw, snapshot))
        if raw.get("schema_version") == "4.0.0":
            evidence_mode = v4_harness_ids(raw).get("scenario", {}).get("evidence_mode")
        else:
            evidence_mode = raw.get("scenario", {}).get("evidence_mode") if isinstance(raw.get("scenario"), dict) else None
        if evidence_mode == "behavioral_run":
            if capture_manifest is None or raw_path is None or snapshot_path is None:
                errors.append(issue("P011", "$.scenario.evidence_mode", "behavioral_run richiede una capture manifest esterna verificata"))
            else:
                errors.extend(provenance_validate(capture_manifest, raw_path, snapshot_path))
    return {"pass": not errors, "rule_ids": sorted({item["rule_id"] for item in errors}), "errors": errors}


def run_oracle(path: Path) -> tuple[dict[str, Any], bool]:
    oracle = load_json(path)
    raw_base = load_json((path.parent / oracle["base_raw"]).resolve())
    snapshot_base = load_json((path.parent / oracle["base_snapshot"]).resolve())
    cases = []
    suite_pass = True
    for case in oracle["cases"]:
        raw = copy.deepcopy(raw_base)
        snapshot = copy.deepcopy(snapshot_base)
        for mutation in case.get("mutations", []):
            mutate(raw if mutation["target"] == "raw" else snapshot, mutation)
        result = validate_case(raw, snapshot)
        actual = "pass" if result["pass"] else "fail"
        expected_rules = sorted(case.get("expected_rule_ids", []))
        matched = actual == case["expected"] and expected_rules == result["rule_ids"]
        suite_pass = suite_pass and matched
        cases.append({"id": case["id"], "expected": case["expected"], "actual": actual, "expected_rule_ids": expected_rules, "actual_rule_ids": result["rule_ids"], "oracle_match": matched})
    return {"oracle": str(path), "oracle_version": oracle["oracle_version"], "pass": suite_pass, "cases": cases}, suite_pass


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--raw", type=Path)
    parser.add_argument("--snapshot", type=Path)
    parser.add_argument("--oracle", type=Path)
    parser.add_argument("--capture-manifest", type=Path)
    parser.add_argument("--require-behavior", action="store_true")
    args = parser.parse_args()
    if args.oracle:
        if args.raw or args.snapshot or args.require_behavior or args.capture_manifest:
            parser.error("--oracle non si combina con raw/snapshot")
    elif not args.raw or not args.snapshot:
        parser.error("specificare --raw e --snapshot, oppure --oracle")
    try:
        if args.oracle:
            result, passed = run_oracle(args.oracle.resolve())
        else:
            result = validate_case(
                load_json(args.raw.resolve()), load_json(args.snapshot.resolve()), args.require_behavior,
                args.capture_manifest.resolve() if args.capture_manifest else None,
                args.raw.resolve(), args.snapshot.resolve(),
            )
            result.update({"raw": str(args.raw.resolve()), "snapshot": str(args.snapshot.resolve())})
            passed = result["pass"]
    except (OSError, ValueError, KeyError, IndexError, TypeError, json.JSONDecodeError) as exc:
        result = {"pass": False, "rule_ids": ["R001"], "errors": [issue("R001", "$", str(exc))]}
        passed = False
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
