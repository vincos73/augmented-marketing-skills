#!/usr/bin/env python3
"""Validate the shared AMS state snapshot contract with the standard library."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


REF = re.compile(r"^[A-Z][A-Z0-9-]*@[0-9]+$")
DIGEST = re.compile(r"^[0-9a-f]{64}$")
SOURCE_REF = re.compile(r"^/(?:[^/~]|~[01])+(?:/(?:[^/~]|~[01])+)*$")
PROFILES = {"chat-v1", "persistent-lineage-v1", "cross-core-safety-v1", "authorization-ledger-v1", "bridge-v1", "preexecution-static-v1", "integrated-postexecution-v1", "nine-skill-minimum-v1"}
EVIDENCE_MODES = {"synthetic_fixture", "behavioral_run", "runtime", "pilot"}
ARTIFACT_STATES = {"conversational", "persistent", "provided", "provided_by_external_evidence", "observed", "not_created", "not_observed", "simulated"}
DIGEST_REQUIRED_STATES = {"persistent", "provided", "provided_by_external_evidence", "observed"}
DECISION_STATUSES = {"approved_in_chat", "approved", "authorized", "denied", "not_requested", "proposed", "not_applicable", "unknown"}
DECISION_MODES = {"observed", "simulated", "not_applicable", "unknown"}
OBSERVATION_SUBJECTS = {"decision", "action", "artifact"}
OBSERVATION_STATUSES = {"observed", "not_observed", "not_applicable", "unknown"}
OBSERVATION_MODES = {"observed", "simulated", "not_applicable", "unknown"}
ACTION_FORBIDDEN = {"denied", "not_requested", "not_applicable", "unknown", "proposed"}
SHARED_INVARIANT_IDS = ["speed-60", "speed-42-conditional", "pilot-quote-01", "operations-total-sprints", "operations-weekly-starts", "sales-weekly-qualified-calls", "TRK-FAB-ERS-OWNED@1", "paid-media"]
MINIMUM_SHARED_INVARIANT_IDS = ["campaign-target", "campaign-result", "paid-media", "tracking-state", "execution-state", "causal-attribution", "roi-state"]


def issue(errors: list[dict[str, str]], rule: str, location: str, message: str) -> None:
    errors.append({"rule_id": rule, "location": location, "message": message})


def exact_object(value: Any, expected: set[str], location: str, errors: list[dict[str, str]]) -> bool:
    if not isinstance(value, dict):
        issue(errors, "S001", location, "atteso oggetto")
        return False
    if set(value) != expected:
        missing = sorted(expected - set(value))
        extra = sorted(set(value) - expected)
        detail = []
        if missing:
            detail.append(f"mancanti: {', '.join(missing)}")
        if extra:
            detail.append(f"non previsti: {', '.join(extra)}")
        issue(errors, "S001", location, "; ".join(detail))
        return False
    return True


def valid_source_ref(value: Any) -> bool:
    return isinstance(value, str) and bool(SOURCE_REF.fullmatch(value))


def string_list(value: Any, location: str, errors: list[dict[str, str]], minimum: int = 0) -> None:
    if not isinstance(value, list) or len(value) < minimum or len(set(value)) != len(value) or any(not isinstance(item, str) or not item for item in value):
        issue(errors, "S001", location, "atteso array di stringhe univoche")


def validate_digest(value: Any, required: bool, location: str, errors: list[dict[str, str]]) -> None:
    if value is None:
        if required:
            issue(errors, "S002", location, "digest obbligatorio per artefatto persistente o osservato")
        return
    valid = isinstance(value, dict) and set(value) == {"algorithm", "value"} and value.get("algorithm") == "sha256" and isinstance(value.get("value"), str) and DIGEST.fullmatch(value.get("value", ""))
    if not valid:
        issue(errors, "S002", location, "digest SHA-256 non valido")
    elif not required:
        issue(errors, "S002", location, "digest vietato per artefatto non creato o soltanto conversazionale")


def validate(snapshot: Any) -> list[dict[str, str]]:
    errors: list[dict[str, str]] = []
    root = {"schema_version", "identity", "scenario", "shared_invariant_ids", "artifacts", "invariants", "authorization", "lineage"}
    if not exact_object(snapshot, root, "$", errors):
        return errors
    if snapshot["schema_version"] != "2.0.0":
        issue(errors, "S001", "$.schema_version", "versione non supportata")
    profile = snapshot.get("scenario", {}).get("profile") if isinstance(snapshot.get("scenario"), dict) else None
    expected_shared_ids = MINIMUM_SHARED_INVARIANT_IDS if profile == "nine-skill-minimum-v1" else SHARED_INVARIANT_IDS
    if snapshot.get("shared_invariant_ids") != expected_shared_ids:
        issue(errors, "S003", "$.shared_invariant_ids", "identificatori condivisi divergenti")

    identity = snapshot["identity"]
    if exact_object(identity, {"id", "state", "version", "source_ref"}, "$.identity", errors):
        for field in ("id", "state", "version"):
            if not isinstance(identity[field], str) or not identity[field]:
                issue(errors, "S001", f"$.identity.{field}", "valore mancante")
        if not valid_source_ref(identity["source_ref"]):
            issue(errors, "S005", "$.identity.source_ref", "JSON Pointer raw non valido")

    scenario = snapshot["scenario"]
    scenario_keys = {"id", "profile", "version", "evidence_mode", "source_scope"}
    if profile != "nine-skill-minimum-v1":
        scenario_keys.add("source_ref")
    if exact_object(scenario, scenario_keys, "$.scenario", errors):
        if not isinstance(scenario["id"], str) or not scenario["id"]:
            issue(errors, "S001", "$.scenario.id", "id mancante")
        if scenario["profile"] not in PROFILES:
            issue(errors, "S001", "$.scenario.profile", "profilo non valido")
        if not isinstance(scenario["version"], str) or not scenario["version"]:
            issue(errors, "S001", "$.scenario.version", "versione mancante")
        if scenario["evidence_mode"] not in EVIDENCE_MODES:
            issue(errors, "S001", "$.scenario.evidence_mode", "modalità evidenza non valida")
        if not isinstance(scenario["source_scope"], str) or not scenario["source_scope"]:
            issue(errors, "S001", "$.scenario.source_scope", "scope mancante")
        if profile != "nine-skill-minimum-v1" and not valid_source_ref(scenario["source_ref"]):
            issue(errors, "S005", "$.scenario.source_ref", "JSON Pointer raw non valido")

    artifacts = snapshot["artifacts"]
    refs: set[str] = set()
    if not isinstance(artifacts, list):
        issue(errors, "S001", "$.artifacts", "atteso array")
        artifacts = []
    for index, artifact in enumerate(artifacts):
        location = f"$.artifacts[{index}]"
        base_keys = {"ref", "version", "digest", "state", "source_ref"}
        artifact_keys = set(artifact) if isinstance(artifact, dict) else set()
        expected_keys = base_keys | ({"evidence_ref"} if artifact_keys == base_keys | {"evidence_ref"} else set())
        if not exact_object(artifact, expected_keys, location, errors):
            continue
        ref = artifact["ref"]
        if not isinstance(ref, str) or not REF.fullmatch(ref) or ref in refs:
            issue(errors, "S002", f"{location}.ref", "riferimento non valido o duplicato")
        else:
            refs.add(ref)
        if not isinstance(artifact["version"], str) or not artifact["version"] or not isinstance(ref, str) or ref.rsplit("@", 1)[-1] != artifact["version"]:
            issue(errors, "S002", f"{location}.version", "versione mancante o diversa dal riferimento")
        state = artifact["state"]
        if state not in ARTIFACT_STATES:
            issue(errors, "S002", f"{location}.state", "stato artefatto non valido")
        else:
            validate_digest(artifact["digest"], state in DIGEST_REQUIRED_STATES, f"{location}.digest", errors)
        if state == "provided_by_external_evidence":
            if not isinstance(artifact.get("evidence_ref"), str) or not artifact["evidence_ref"]:
                issue(errors, "S002", f"{location}.evidence_ref", "artefatto fornito da evidenza esterna privo di file osservabile")
        elif "evidence_ref" in artifact:
            issue(errors, "S002", f"{location}.evidence_ref", "evidence_ref riservato a provided_by_external_evidence")
        if not valid_source_ref(artifact["source_ref"]):
            issue(errors, "S005", f"{location}.source_ref", "JSON Pointer raw non valido")

    invariants = snapshot["invariants"]
    invariant_ids: set[str] = set()
    if not isinstance(invariants, list):
        issue(errors, "S001", "$.invariants", "atteso array")
        invariants = []
    for index, invariant in enumerate(invariants):
        location = f"$.invariants[{index}]"
        if not isinstance(invariant, dict) or set(invariant) not in ({"id", "status", "source_ref"}, {"id", "status", "value", "source_ref"}):
            issue(errors, "S001", location, "forma invariante non valida")
            continue
        identifier = invariant["id"]
        if not isinstance(identifier, str) or not identifier or identifier in invariant_ids:
            issue(errors, "S003", f"{location}.id", "id mancante o duplicato")
        invariant_ids.add(identifier)
        if not isinstance(invariant["status"], str) or not invariant["status"]:
            issue(errors, "S003", f"{location}.status", "stato mancante")
        if not valid_source_ref(invariant["source_ref"]):
            issue(errors, "S005", f"{location}.source_ref", "JSON Pointer raw non valido")

    authorization = snapshot["authorization"]
    decision_by_id: dict[str, dict[str, Any]] = {}
    if exact_object(authorization, {"decisions", "observations"}, "$.authorization", errors):
        decisions = authorization["decisions"]
        observations = authorization["observations"]
        if not isinstance(decisions, list) or not isinstance(observations, list):
            issue(errors, "S001", "$.authorization", "decisioni e osservazioni devono essere array")
            decisions, observations = [], []
        for index, decision in enumerate(decisions):
            location = f"$.authorization.decisions[{index}]"
            keys = {"id", "status", "mode", "scope", "authority", "source_ref"}
            if not exact_object(decision, keys, location, errors):
                continue
            identifier = decision["id"]
            if not isinstance(identifier, str) or not identifier or identifier in decision_by_id:
                issue(errors, "S003", f"{location}.id", "id decisione mancante o duplicato")
            else:
                decision_by_id[identifier] = decision
            if decision["status"] not in DECISION_STATUSES:
                issue(errors, "S003", f"{location}.status", "stato decisionale non valido")
            if decision["mode"] not in DECISION_MODES:
                issue(errors, "S003", f"{location}.mode", "modalità decisionale non valida")
            string_list(decision["scope"], f"{location}.scope", errors, minimum=1)
            if not isinstance(decision["authority"], str) or not decision["authority"]:
                issue(errors, "S003", f"{location}.authority", "autorità mancante")
            if not valid_source_ref(decision["source_ref"]):
                issue(errors, "S005", f"{location}.source_ref", "JSON Pointer raw non valido")

        observation_ids: set[str] = set()
        action_by_decision: dict[str, list[dict[str, Any]]] = {}
        for index, observation in enumerate(observations):
            location = f"$.authorization.observations[{index}]"
            keys = {"id", "subject", "decision_id", "status", "mode", "evidence_refs", "source_ref"}
            if not exact_object(observation, keys, location, errors):
                continue
            identifier = observation["id"]
            if not isinstance(identifier, str) or not identifier or identifier in observation_ids:
                issue(errors, "S003", f"{location}.id", "id osservazione mancante o duplicato")
            observation_ids.add(identifier)
            decision_id = observation["decision_id"]
            if decision_id not in decision_by_id:
                issue(errors, "S006", f"{location}.decision_id", "decisione collegata non risolta")
            if observation["subject"] not in OBSERVATION_SUBJECTS:
                issue(errors, "S003", f"{location}.subject", "soggetto non valido")
            if observation["status"] not in OBSERVATION_STATUSES:
                issue(errors, "S003", f"{location}.status", "stato osservativo non valido")
            if observation["mode"] not in OBSERVATION_MODES:
                issue(errors, "S003", f"{location}.mode", "modalità osservativa non valida")
            string_list(observation["evidence_refs"], f"{location}.evidence_refs", errors)
            if not valid_source_ref(observation["source_ref"]):
                issue(errors, "S005", f"{location}.source_ref", "JSON Pointer raw non valido")
            if observation["subject"] == "action":
                action_by_decision.setdefault(decision_id, []).append(observation)
                decision = decision_by_id.get(decision_id)
                if observation["status"] == "observed" and decision and decision["status"] in ACTION_FORBIDDEN:
                    issue(errors, "S006", location, "azione osservata con decisione negata, non richiesta o non applicabile")
        for decision_id, decision in decision_by_id.items():
            if decision["status"] in ACTION_FORBIDDEN:
                actions = action_by_decision.get(decision_id, [])
                if not actions or any(item["status"] not in {"not_observed", "not_applicable"} for item in actions):
                    issue(errors, "S006", "$.authorization.observations", f"azione negata/non richiesta non rappresentata come non osservata: {decision_id}")

    lineage = snapshot["lineage"]
    if exact_object(lineage, {"edges"}, "$.lineage", errors):
        if not isinstance(lineage["edges"], list):
            issue(errors, "S001", "$.lineage.edges", "atteso array")
        else:
            for index, edge in enumerate(lineage["edges"]):
                location = f"$.lineage.edges[{index}]"
                if not exact_object(edge, {"from", "to", "relation", "source_ref"}, location, errors):
                    continue
                if edge["from"] not in refs or edge["to"] not in refs:
                    issue(errors, "S004", location, "arco non risolto nello snapshot")
                if not isinstance(edge["relation"], str) or not edge["relation"]:
                    issue(errors, "S004", f"{location}.relation", "relazione mancante")
                if not valid_source_ref(edge["source_ref"]):
                    issue(errors, "S005", f"{location}.source_ref", "JSON Pointer raw non valido")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("snapshot", type=Path)
    args = parser.parse_args()
    try:
        snapshot = json.loads(args.snapshot.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"pass": False, "rule_ids": ["S001"], "errors": [{"rule_id": "S001", "location": "$", "message": str(exc)}]}, ensure_ascii=False, indent=2))
        return 1
    errors = validate(snapshot)
    result = {"snapshot": str(args.snapshot), "pass": not errors, "rule_ids": sorted({item["rule_id"] for item in errors}), "errors": errors}
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if not errors else 1


if __name__ == "__main__":
    raise SystemExit(main())
