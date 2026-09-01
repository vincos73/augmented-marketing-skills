#!/usr/bin/env python3
"""Validate the static evidence boundary across the nine actual AMS skills."""

from __future__ import annotations

import json
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parents[1]
MANIFEST = HERE / "static-boundary-manifest.json"
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


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    try:
        boundary = load(MANIFEST)
        required = {"schema_version", "boundary_ref", "boundary_kind", "source_profile", "target_profile", "source_scenario_id", "target_scenario_id", "skills", "source_terminal_state", "target_entrypoint", "boundary_observation", "guards"}
        if set(boundary) != required or boundary["schema_version"] != 3:
            raise ValueError("forma static boundary non valida")
        if boundary["boundary_ref"] != "FABRILOOM-ERS-BRIDGE@1" or boundary["boundary_kind"] != "static_evidence_boundary":
            raise ValueError("identità static boundary non valida")
        if boundary["source_profile"] != "chat-v1" or boundary["target_profile"] != "integrated-postexecution-v1":
            raise ValueError("profili non distinti")
        if boundary["source_scenario_id"] != "FABRILOOM-ERS-PREEXEC-STATIC-V1" or boundary["target_scenario_id"] != "FABRILOOM-ERS-INTEGRATED-POSTEXEC-V1":
            raise ValueError("scenario pre-execution e post-execution non distinti")
        events = boundary["skills"]
        if not isinstance(events, list) or [item.get("skill") for item in events] != SKILLS or [item.get("sequence") for item in events] != list(range(1, 10)):
            raise ValueError("servono i nove nomi di skill reali nell'ordine corretto")
        for event in events:
            evidence = (HERE / event["evidence"]).resolve()
            if not evidence.is_file():
                raise ValueError(f"evidenza non risolta per {event['skill']}: {event['evidence']}")
            text = evidence.read_text(encoding="utf-8")
            if event["sequence"] <= 5 and event["skill"] not in text:
                raise ValueError(f"skill non osservabile nell'evidenza sorgente: {event['skill']}")
        source_text = (HERE / events[0]["evidence"]).resolve().read_text(encoding="utf-8")
        for token in ("chat-v1", "salvataggio negato", "esecuzione negata", "TRK-FAB-ERS-OWNED@1", "`unverified`"):
            if token not in source_text:
                raise ValueError(f"stato terminale sorgente non osservabile: {token}")
        lineage_path = (HERE / "../../campaign-lineage/fabriloom-evidence-readiness/lineage-manifest.json").resolve()
        artifacts = load(lineage_path)["artifacts"]
        target_refs = {artifacts[name]["ref"] for name in ("campaign_spec", "operations", "authorization", "execution", "results", "debrief")}
        target_refs.update(item["ref"] for item in artifacts["assets"])
        target_refs.update(item["ref"] for item in artifacts["reviews"])
        for field, ref in boundary["target_entrypoint"].items():
            if ref not in target_refs:
                raise ValueError(f"entrypoint non risolto: {field}={ref}")
        expected_terminal = {"conversation_version": "chat-v1", "content_state": "confirmed_in_chat", "canonical_save": "denied", "execution": "denied", "tracking_state": "unverified"}
        if boundary["source_terminal_state"] != expected_terminal:
            raise ValueError("stato terminale sorgente inatteso")
        observation = boundary["boundary_observation"]
        if observation.get("kind") != "static_evidence_boundary" or observation.get("status") != "observed":
            raise ValueError("confine statico non osservato esplicitamente")
        for evidence_ref in observation.get("evidence", []):
            if not (HERE / evidence_ref).resolve().is_file():
                raise ValueError(f"evidenza di confine non risolta: {evidence_ref}")
        expected_guards = {"source_to_target_requires_new_evidence": True, "implicit_promotion": "forbidden", "behavioral_run_claim": "not_observed", "runtime_claim": "not_observed", "pilot_claim": "not_observed"}
        if boundary["guards"] != expected_guards:
            raise ValueError("guard static boundary incompleti")
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print("PASS: static evidence boundary su nove skill reali")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
