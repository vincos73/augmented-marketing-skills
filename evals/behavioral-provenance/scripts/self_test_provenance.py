#!/usr/bin/env python3
"""Build ephemeral raw v4 captures and exercise fail-closed provenance regressions."""

from __future__ import annotations

import copy
import hashlib
import importlib.util
import json
import re
import tempfile
from pathlib import Path
from typing import Any, Callable, Iterable


ROOT = Path(__file__).resolve().parents[1]
EVALS = ROOT.parent
CHECKER = ROOT / "scripts/check_provenance.py"
ALLOWLIST = ROOT / "runtime-allowlist.json"
MINIMUM_CONTRACT = EVALS / "raw-to-snapshot/minimum-behavior-contract.json"
EXPECTED_DEBRIEF = EVALS / "campaign-lineage/fabriloom-evidence-readiness/oracles/expected-debrief.md"


def load(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def canonical(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def object_digest(value: Any) -> str:
    return hashlib.sha256(canonical(value)).hexdigest()


def pointer_token(value: str) -> str:
    return value.replace("~", "~0").replace("/", "~1")


def leaves(value: Any, pointer: str) -> Iterable[tuple[str, Any]]:
    if isinstance(value, dict):
        for key, item in value.items():
            yield from leaves(item, f"{pointer}/{pointer_token(str(key))}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from leaves(item, f"{pointer}/{index}")
    else:
        yield pointer, value


def import_checker():
    spec = importlib.util.spec_from_file_location("provenance_checker_selftest", CHECKER)
    if spec is None or spec.loader is None:
        raise RuntimeError("checker non caricabile")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ASSET = {"id": "CAR-FAB-ERS-DIAG@2", "version": 2, "channel": "linkedin_organic"}
TARGET = {"id": "richieste qualificate", "status": "confermato", "value": {"metric": "richieste qualificate", "target": 20}}
AUTH_DECISION = {
    "id": "organic_publication", "status": "authorized", "mode": "simulated",
    "scope": ["organic_publication"], "authority": "Marketing Director",
}
AUTH_ASSET = {"id": "CAR-FAB-ERS-DIAG@2", "version": 2}
INPUT_SEMANTIC: dict[int, dict[str, Any]] = {
    8: {
        "authorization_decision": AUTH_DECISION,
        "authorization_asset": AUTH_ASSET,
        "paid": {"id": "Paid", "status": "not_authorized"},
    },
}
SEMANTIC: dict[int, dict[str, Any]] = {
    0: {"identity": {"id": "Fabriloom", "state": "confermata in chat", "version": "v1"}},
    2: {"campaign_target": TARGET},
    3: {"paid": {"id": "Paid", "status": "not_authorized"}},
    5: {"tracking": {"id": "TRK-FAB-ERS-OWNED@1", "status": "verified", "value": {"basis": "operational_evidence"}}},
    7: {
        "review": {"target": TARGET, "asset": ASSET, "verdict": "pronta"},
    },
    8: {
        "execution": {"state": "observed", "asset": ASSET},
        "execution_observation": {
            "id": "CAR-FAB-ERS-DIAG@2", "subject": "action",
            "decision_id": "organic_publication", "status": "observed",
            "mode": "simulated", "evidence_refs": [],
        },
        "debrief": {
            "target": TARGET, "result": 7, "metric": "richieste qualificate",
            "paid_state": "not_authorized", "tracking_state": "verified",
            "causality": "not_attributed", "roi": "not_calculable",
        },
        "campaign_result": {"id": "Risultato", "status": "osservato", "value": {"metric": "richieste qualificate", "result": 7, "target": 20}},
        "execution_invariant": {"id": "Esecuzione", "status": "osservata", "value": ASSET},
        "causality_invariant": {"id": "Causalità", "status": "not_attributed"},
        "roi_invariant": {"id": "ROI", "status": "not_calculable"},
    },
}
TEXTS = [
    "Identità Fabriloom, stato confermata in chat, versione v1.",
    "Fondamenti di marketing confermati.",
    "Target confermato: 20 richieste qualificate.",
    "Paid non autorizzato.",
    "Marketing Mix confermato senza nuove autorizzazioni.",
    "Tracking TRK-FAB-ERS-OWNED@1 verificato dopo evidenza operativa.",
    "Content brief completato per la review.",
    "Review pronta per asset CAR-FAB-ERS-DIAG@2, versione 2, canale LinkedIn organico. Target confermato: 20 richieste qualificate. La review non autorizza la pubblicazione.",
    "Eseguito in modalità simulated: Esecuzione osservata della pubblicazione organica dell'asset CAR-FAB-ERS-DIAG@2, versione 2, canale LinkedIn organico. Paid non autorizzato. Tracking verificato. Risultato osservato: 7 richieste qualificate su target confermato 20. Causalità non dimostrabile. ROI non calcolabile.",
]
INPUT_TEXTS = [f"Richiesta del committente per {skill}." for skill in (
    "identità", "fondamenti", "sfida", "direzione", "mix", "campagna", "contenuto", "review", "debrief",
)]
INPUT_TEXTS[8] = "Dopo il verdict pronta, la Marketing Director ha autorizzato in modalità simulated soltanto la pubblicazione organica dell'esatto CAR-FAB-ERS-DIAG@2, versione 2; Paid è rimasto non autorizzato."
REVERSE_ENUM = {
    "authorized": ("ha autorizzato", "authorization_state"),
    "not_authorized": ("non autorizzato", "authorization_state"),
    "observed": ("osservata", "execution_state"),
    "verified": ("verificato", "tracking_state"),
    "not_attributed": ("non dimostrabile", "causality_state"),
    "not_calculable": ("non calcolabile", "roi_state"),
    "linkedin_organic": ("LinkedIn organico", "channel"),
    "operational_evidence": ("evidenza operativa", "evidence_basis"),
    "action": ("Eseguito", "observation_subject"),
    "organic_publication": ("pubblicazione organica", "organic_scope"),
    "simulated": ("simulated", "simulation_mode"),
}


def text_source(text: str, value: Any) -> tuple[str, str]:
    if isinstance(value, int) and not isinstance(value, bool):
        match = re.search(rf"(?<![0-9]){value}(?![0-9])", text)
        if not match:
            raise ValueError(f"intero {value} non trovato")
        return match.group(0), "integer"
    if value in REVERSE_ENUM:
        excerpt, transform = REVERSE_ENUM[value]
        if excerpt not in text:
            raise ValueError(f"enum {value} non trovato in {text!r}")
        return excerpt, transform
    excerpt = str(value)
    if excerpt not in text:
        raise ValueError(f"valore {value!r} non trovato in {text!r}")
    return excerpt, "identity"


def build_normalizations(index: int, normalized: dict[str, Any], payload: dict[str, Any], mode: str, stream: str = "output") -> list[dict[str, Any]]:
    values = []
    normalized_key = "normalized_input" if stream == "input" else "normalized_output"
    for ref, value in leaves(normalized, f"/events/{index}/{normalized_key}"):
        suffix = ref.split(f"/events/{index}/{normalized_key}", 1)[1]
        if mode == "structured":
            location = {"kind": "json_pointer", "pointer": f"/payload/data{suffix}"}
            transform = "identity"
        else:
            excerpt, transform = text_source(payload["text"], value)
            start = payload["text"].find(excerpt)
            location = {
                "kind": "text_range", "pointer": "/payload/text", "unit": "char",
                "start": start, "end": start + len(excerpt), "excerpt": excerpt,
                "excerpt_sha256": hashlib.sha256(excerpt.encode("utf-8")).hexdigest(),
            }
        values.append({
            "normalized_ref": ref,
            "normalized_sha256": object_digest(value),
            "transformation": {"id": transform},
            "source": stream,
            "location": location,
        })
    return values


def build_snapshot() -> dict[str, Any]:
    contract = load(MINIMUM_CONTRACT)
    return {
        "schema_version": "2.0.0",
        "identity": {**SEMANTIC[0]["identity"], "source_ref": "/events/0/normalized_output/identity"},
        "scenario": {
            "id": "minimum-behavior-selftest", "profile": contract["profile"], "version": "v1",
            "evidence_mode": "behavioral_run", "source_scope": "test effimero",
        },
        "shared_invariant_ids": contract["shared_invariant_ids"],
        "artifacts": [],
        "invariants": [
            {**SEMANTIC[2]["campaign_target"], "source_ref": "/events/2/normalized_output/campaign_target"},
            {**SEMANTIC[8]["campaign_result"], "source_ref": "/events/8/normalized_output/campaign_result"},
            {**SEMANTIC[3]["paid"], "source_ref": "/events/3/normalized_output/paid"},
            {**SEMANTIC[5]["tracking"], "source_ref": "/events/5/normalized_output/tracking"},
            {**SEMANTIC[8]["execution_invariant"], "source_ref": "/events/8/normalized_output/execution_invariant"},
            {**SEMANTIC[8]["causality_invariant"], "source_ref": "/events/8/normalized_output/causality_invariant"},
            {**SEMANTIC[8]["roi_invariant"], "source_ref": "/events/8/normalized_output/roi_invariant"},
        ],
        "authorization": {
            "decisions": [{**copy.deepcopy(AUTH_DECISION), "source_ref": "/events/8/normalized_input/authorization_decision"}],
            "observations": [{**copy.deepcopy(SEMANTIC[8]["execution_observation"]), "source_ref": "/events/8/normalized_output/execution_observation"}],
        },
        "lineage": {"edges": []},
    }


def build_capture(directory: Path, mode: str = "natural") -> tuple[Path, Path, Path]:
    directory.mkdir(parents=True)
    allowlist = load(ALLOWLIST)
    contract = load(MINIMUM_CONTRACT)
    capture_id = f"CAPTURE-{mode}-{directory.name}"
    previous: str | None = None
    raw_events = []
    capture_events = []
    for index, wanted in enumerate(allowlist["skills"]):
        normalized_input = copy.deepcopy(INPUT_SEMANTIC.get(index, {}))
        normalized = copy.deepcopy(SEMANTIC.get(index, {}))
        input_payload = {"data": copy.deepcopy(normalized_input)} if mode == "structured" else {"text": INPUT_TEXTS[index], "truncated": False}
        payload = {"data": copy.deepcopy(normalized)} if mode == "structured" else {"text": TEXTS[index], "truncated": False}
        metadata = {
            "invocation_id": f"turn-{index + 1}", "provider": "openai", "runtime": "codex-desktop",
            "thread_id": "thread-host-export", "turn_id": f"turn-{index + 1}", "message_id": f"message-{index + 1}",
            "model": "gpt-5.6-sol", "skill_id": wanted["skill_id"], "skill_version": wanted["skill_version"],
            "skill_sha256": wanted["skill_sha256"], "captured_at": f"2026-09-01T10:{index:02d}:00+02:00",
        }
        input_path = (directory / f"{index + 1:02d}-input.json").resolve()
        output_path = (directory / f"{index + 1:02d}-output.json").resolve()
        receipt_path = (directory / f"{index + 1:02d}-receipt.json").resolve()
        write(input_path, {"schema_version": "1.0.0", "capture_kind": "codex_invocation_input", "receipt_metadata": metadata, "payload": input_payload})
        write(output_path, {"schema_version": "1.0.0", "capture_kind": "codex_invocation_output", "receipt_metadata": metadata, "payload": payload})
        receipt = {
            "schema_version": "1.0.0", **metadata, "input_path": str(input_path), "input_sha256": digest(input_path),
            "output_path": str(output_path), "output_sha256": digest(output_path), "previous_event_sha256": previous,
        }
        receipt["event_sha256"] = object_digest(receipt)
        previous = receipt["event_sha256"]
        write(receipt_path, receipt)
        raw_events.append({
            "sequence": index + 1, "skill": wanted["skill_id"], "skill_version": wanted["skill_version"],
            "receipt_path": str(receipt_path), "raw_input_path": str(input_path), "raw_input_sha256": receipt["input_sha256"],
            "raw_response_path": str(output_path), "raw_response_sha256": receipt["output_sha256"], "raw_input": input_payload,
            "raw_output": payload, "normalized_input": normalized_input,
            "input_normalizations": build_normalizations(index, normalized_input, input_payload, mode, "input"),
            "normalized_output": normalized, "normalizations": build_normalizations(index, normalized, payload, mode),
        })
        capture_events.append({"sequence": index + 1, "skill_id": wanted["skill_id"], "receipt_path": str(receipt_path), "receipt_sha256": digest(receipt_path)})
    raw = {
        "schema_version": "4.0.0", "run_id": f"RUN-{mode}", "capture_id": capture_id,
        "proof_metadata": {
            "artifact_digests": [],
            "harness_ids": {
                "profile": contract["profile"],
                "shared_invariant_ids": contract["shared_invariant_ids"],
                "scenario": {
                    "id": "minimum-behavior-selftest", "version": "v1",
                    "evidence_mode": "behavioral_run", "source_scope": "test effimero",
                },
            },
        },
        "events": raw_events,
    }
    snapshot = build_snapshot()
    raw_path, snapshot_path, capture_path = (directory / "raw.json").resolve(), (directory / "snapshot.json").resolve(), (directory / "capture.json").resolve()
    write(raw_path, raw)
    write(snapshot_path, snapshot)
    write(capture_path, {
        "schema_version": "1.0.0", "capture_id": capture_id, "evidence_mode": "behavioral_run",
        "source_base_commit": allowlist["source_base_commit"], "provider": "openai", "runtime": "codex-desktop",
        "thread_id": "thread-host-export", "model": "gpt-5.6-sol", "raw_manifest_path": str(raw_path),
        "raw_manifest_sha256": digest(raw_path), "snapshot_path": str(snapshot_path), "snapshot_sha256": digest(snapshot_path),
        "events": capture_events,
    })
    return capture_path, raw_path, snapshot_path


def refresh(capture_path: Path, raw_path: Path, snapshot_path: Path) -> None:
    capture, raw = load(capture_path), load(raw_path)
    previous = None
    for item, event in zip(capture["events"], raw["events"]):
        receipt_path = Path(item["receipt_path"])
        receipt = load(receipt_path)
        receipt["input_sha256"] = digest(Path(receipt["input_path"]))
        receipt["output_sha256"] = digest(Path(receipt["output_path"]))
        receipt["previous_event_sha256"] = previous
        receipt["event_sha256"] = object_digest({key: value for key, value in receipt.items() if key != "event_sha256"})
        previous = receipt["event_sha256"]
        write(receipt_path, receipt)
        item["receipt_sha256"] = digest(receipt_path)
        event["raw_input_sha256"] = receipt["input_sha256"]
        event["raw_response_sha256"] = receipt["output_sha256"]
    write(raw_path, raw)
    capture["raw_manifest_sha256"] = digest(raw_path)
    capture["snapshot_sha256"] = digest(snapshot_path)
    write(capture_path, capture)


def mutate_excerpt(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    location = raw["events"][0]["normalizations"][0]["location"]
    location["excerpt"] = location["excerpt"][:-1]
    location["excerpt_sha256"] = hashlib.sha256(location["excerpt"].encode()).hexdigest()
    write(raw_path, raw)


def mutate_offset(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    raw["events"][0]["normalizations"][0]["location"]["end"] = 99999
    write(raw_path, raw)


def mutate_transform(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    raw["events"][2]["normalizations"][0]["transformation"]["id"] = "free_summary"
    write(raw_path, raw)


def mutate_underivable(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    raw["events"][2]["normalized_output"]["campaign_target"]["value"]["target"] = 21
    for item in raw["events"][2]["normalizations"]:
        if item["normalized_ref"].endswith("/target"):
            item["normalized_sha256"] = object_digest(21)
    write(raw_path, raw)


def mutate_expected_copy(capture_path: Path, raw_path: Path, snapshot_path: Path) -> None:
    raw = load(raw_path)
    value = digest(EXPECTED_DEBRIEF)
    event = raw["events"][1]
    event["normalized_output"] = {"oracle_copy": value}
    output_path = Path(event["raw_response_path"])
    output = load(output_path)
    output["payload"] = {"text": value, "truncated": False}
    write(output_path, output)
    event["raw_output"] = output["payload"]
    event["normalizations"] = build_normalizations(1, event["normalized_output"], event["raw_output"], "natural")
    write(raw_path, raw)
    refresh(capture_path, raw_path, snapshot_path)


def mutate_invented_digest(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    raw["events"][1]["normalized_output"]["artifact_digest"] = "a" * 64
    write(raw_path, raw)


def mutate_harness_id(capture_path: Path, raw_path: Path, snapshot_path: Path) -> None:
    raw = load(raw_path)
    event = raw["events"][1]
    event["normalized_output"] = {"profile": "nine-skill-minimum-v1"}
    output_path = Path(event["raw_response_path"])
    output = load(output_path)
    output["payload"] = {"text": "Profilo dichiarato: nine-skill-minimum-v1", "truncated": False}
    write(output_path, output)
    event["raw_output"] = output["payload"]
    event["normalizations"] = build_normalizations(1, event["normalized_output"], event["raw_output"], "natural")
    write(raw_path, raw)
    refresh(capture_path, raw_path, snapshot_path)


def mutate_missing_phrase(capture_path: Path, raw_path: Path, snapshot_path: Path, event_index: int, phrase: str) -> None:
    raw = load(raw_path)
    output_path = Path(raw["events"][event_index]["raw_response_path"])
    output = load(output_path)
    output["payload"]["text"] = output["payload"]["text"].replace(phrase, "[omesso]")
    write(output_path, output)
    raw["events"][event_index]["raw_output"] = output["payload"]
    write(raw_path, raw)
    refresh(capture_path, raw_path, snapshot_path)


def mutate_missing_input_phrase(capture_path: Path, raw_path: Path, snapshot_path: Path, event_index: int, phrase: str) -> None:
    raw = load(raw_path)
    input_path = Path(raw["events"][event_index]["raw_input_path"])
    input_doc = load(input_path)
    input_doc["payload"]["text"] = input_doc["payload"]["text"].replace(phrase, "[omesso]")
    write(input_path, input_doc)
    raw["events"][event_index]["raw_input"] = input_doc["payload"]
    write(raw_path, raw)
    refresh(capture_path, raw_path, snapshot_path)


def mutate_authorization(c: Path, r: Path, s: Path) -> None:
    mutate_missing_input_phrase(c, r, s, 8, "ha autorizzato")


def mutate_tracking(c: Path, r: Path, s: Path) -> None:
    mutate_missing_phrase(c, r, s, 5, "verificato")


def mutate_source_ref(_: Path, __: Path, snapshot_path: Path) -> None:
    snapshot = load(snapshot_path)
    snapshot["identity"]["source_ref"] = "/events/0/raw_output"
    write(snapshot_path, snapshot)


def mutate_payload(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    raw["events"][0]["raw_output"]["text"] += " alterato"
    write(raw_path, raw)


def mutate_input_payload(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    raw["events"][0]["raw_input"]["text"] += " alterato"
    write(raw_path, raw)


def mutate_input_points_output(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    raw["events"][8]["input_normalizations"][0]["source"] = "output"
    write(raw_path, raw)


def mutate_output_points_input(_: Path, raw_path: Path, __: Path) -> None:
    raw = load(raw_path)
    raw["events"][0]["normalizations"][0]["source"] = "input"
    write(raw_path, raw)


def mutate_authorization_from_output(capture_path: Path, raw_path: Path, snapshot_path: Path) -> None:
    raw = load(raw_path)
    event = raw["events"][8]
    output_path = Path(event["raw_response_path"])
    output = load(output_path)
    output["payload"]["text"] += " " + INPUT_TEXTS[8]
    write(output_path, output)
    event["raw_output"] = output["payload"]
    moved = {
        "authorization_decision": event["normalized_input"].pop("authorization_decision"),
        "authorization_asset": event["normalized_input"].pop("authorization_asset"),
        "authorization_decision_paid": event["normalized_input"].pop("paid"),
    }
    event["normalized_output"].update(moved)
    event["input_normalizations"] = build_normalizations(8, event["normalized_input"], event["raw_input"], "natural", "input")
    event["normalizations"] = build_normalizations(8, event["normalized_output"], event["raw_output"], "natural")
    snapshot = load(snapshot_path)
    snapshot["authorization"]["decisions"][0]["source_ref"] = "/events/8/normalized_output/authorization_decision"
    write(snapshot_path, snapshot)
    write(raw_path, raw)
    refresh(capture_path, raw_path, snapshot_path)


def mutate_authorization_from_proof(_: Path, __: Path, snapshot_path: Path) -> None:
    snapshot = load(snapshot_path)
    snapshot["authorization"]["decisions"][0]["source_ref"] = "/proof_metadata/harness_ids/scenario"
    write(snapshot_path, snapshot)


def mutate_expected_authorization(capture_path: Path, raw_path: Path, snapshot_path: Path) -> None:
    raw = load(raw_path)
    event = raw["events"][8]
    expected_text = EXPECTED_DEBRIEF.read_text(encoding="utf-8").strip()
    decision = copy.deepcopy(event["normalized_input"]["authorization_decision"])
    decision["id"] = expected_text
    event["normalized_input"]["authorization_decision"] = decision
    input_path = Path(event["raw_input_path"])
    input_doc = load(input_path)
    input_doc["payload"]["text"] += "\n" + expected_text
    write(input_path, input_doc)
    event["raw_input"] = input_doc["payload"]
    event["input_normalizations"] = build_normalizations(8, event["normalized_input"], event["raw_input"], "natural", "input")
    snapshot = load(snapshot_path)
    snapshot["authorization"]["decisions"][0]["id"] = expected_text
    write(snapshot_path, snapshot)
    write(raw_path, raw)
    refresh(capture_path, raw_path, snapshot_path)


def mutate_skill_digest(capture_path: Path, raw_path: Path, snapshot_path: Path) -> None:
    """Compatibility helper used by the readiness regression suite."""
    capture = load(capture_path)
    receipt_path = Path(capture["events"][0]["receipt_path"])
    receipt = load(receipt_path)
    invalid_digest = "f" * 64
    receipt["skill_sha256"] = invalid_digest
    for envelope_path in (Path(receipt["input_path"]), Path(receipt["output_path"])):
        envelope = load(envelope_path)
        envelope["receipt_metadata"]["skill_sha256"] = invalid_digest
        write(envelope_path, envelope)
    write(receipt_path, receipt)
    refresh(capture_path, raw_path, snapshot_path)


def main() -> int:
    checker = import_checker()
    cases: list[tuple[str, str, Callable[[Path, Path, Path], None] | None, set[str]]] = [
        ("positive-natural-grounded", "natural", None, set()),
        ("positive-structured-json", "structured", None, set()),
        ("excerpt-truncated", "natural", mutate_excerpt, {"P010", "P012"}),
        ("offset-out-of-range", "natural", mutate_offset, {"P010", "P012"}),
        ("transformation-not-allowed", "natural", mutate_transform, {"P010", "P012"}),
        ("normalized-value-not-derivable", "natural", mutate_underivable, {"P012"}),
        ("expected-copy-normalized", "natural", mutate_expected_copy, {"P013"}),
        ("invented-digest", "natural", mutate_invented_digest, {"P012", "P014"}),
        ("harness-id-promoted-to-model-fact", "natural", mutate_harness_id, {"P014"}),
        ("invented-authorization", "natural", mutate_authorization, {"P010", "P012"}),
        ("raw-input-host-mismatch", "natural", mutate_input_payload, {"P009"}),
        ("input-normalization-points-output", "natural", mutate_input_points_output, {"P010", "P012"}),
        ("output-normalization-points-input", "natural", mutate_output_points_input, {"P010", "P012"}),
        ("authorization-only-in-model-output", "natural", mutate_authorization_from_output, {"P015"}),
        ("authorization-from-proof-metadata", "natural", mutate_authorization_from_proof, {"P010"}),
        ("authorization-from-expected", "natural", mutate_expected_authorization, {"P013"}),
        ("invented-tracking", "natural", mutate_tracking, {"P010", "P012"}),
        ("snapshot-skips-normalized-output", "natural", mutate_source_ref, {"P010"}),
        ("host-payload-raw-mismatch", "natural", mutate_payload, {"P009"}),
    ]
    failures = []
    with tempfile.TemporaryDirectory(prefix="ams-provenance-v4-") as temp:
        root = Path(temp)
        for name, mode, mutation, expected in cases:
            capture_path, raw_path, snapshot_path = build_capture(root / name, mode)
            if mutation:
                mutation(capture_path, raw_path, snapshot_path)
                if mutation not in {mutate_expected_copy, mutate_authorization, mutate_tracking, mutate_authorization_from_output, mutate_expected_authorization}:
                    capture = load(capture_path)
                    capture["raw_manifest_sha256"] = digest(raw_path)
                    capture["snapshot_sha256"] = digest(snapshot_path)
                    write(capture_path, capture)
            result = checker.validate(capture_path, raw_path, snapshot_path)
            actual = set(result["rule_ids"])
            if actual != expected or result["pass"] != (not expected):
                failures.append(f"{name}: attesi {sorted(expected)}, osservati {sorted(actual)}")
            else:
                print(f"PASS {name}: {sorted(actual)}")
    if failures:
        print("\n".join(f"FAIL {item}" for item in failures))
        return 1
    print(f"SELF-TEST PASS: {len(cases)} casi v4 effimeri, nessuna receipt positiva nel repository")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
