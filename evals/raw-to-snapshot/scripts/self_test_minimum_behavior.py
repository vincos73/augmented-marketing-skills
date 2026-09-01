#!/usr/bin/env python3
"""Exercise the minimal nine-skill behavioral profile with grounded v4 captures."""

from __future__ import annotations

import copy
import importlib.util
import tempfile
from pathlib import Path
from typing import Any, Callable


HERE = Path(__file__).resolve().parent
CHECKER_PATH = HERE / "check_raw_to_snapshot.py"
PROVENANCE_SELFTEST = HERE.parents[1] / "behavioral-provenance/scripts/self_test_provenance.py"


def import_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"modulo non caricabile: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def rewrite_event(builder: Any, raw: dict[str, Any], index: int, normalized: dict[str, Any]) -> None:
    event = raw["events"][index]
    event["normalized_output"] = normalized
    output_path = Path(event["raw_response_path"])
    output = builder.load(output_path)
    output["payload"] = {"data": copy.deepcopy(normalized)}
    builder.write(output_path, output)
    event["raw_output"] = copy.deepcopy(output["payload"])
    event["normalizations"] = builder.build_normalizations(index, normalized, event["raw_output"], "structured")


def rewrite_input_event(builder: Any, raw: dict[str, Any], index: int, normalized: dict[str, Any]) -> None:
    event = raw["events"][index]
    event["normalized_input"] = normalized
    input_path = Path(event["raw_input_path"])
    input_doc = builder.load(input_path)
    input_doc["payload"] = {"data": copy.deepcopy(normalized)}
    builder.write(input_path, input_doc)
    event["raw_input"] = copy.deepcopy(input_doc["payload"])
    event["input_normalizations"] = builder.build_normalizations(index, normalized, event["raw_input"], "structured", "input")


def finish(builder: Any, capture: Path, raw_path: Path, snapshot: Path, raw: dict[str, Any], snapshot_doc: dict[str, Any] | None = None) -> None:
    builder.write(raw_path, raw)
    if snapshot_doc is not None:
        builder.write(snapshot, snapshot_doc)
    builder.refresh(capture, raw_path, snapshot)


def lose_target(builder: Any, capture: Path, raw_path: Path, snapshot: Path) -> None:
    raw = builder.load(raw_path)
    normalized = copy.deepcopy(raw["events"][7]["normalized_output"])
    normalized["review"].pop("target")
    rewrite_event(builder, raw, 7, normalized)
    finish(builder, capture, raw_path, snapshot, raw)


def conflate_authorization(builder: Any, capture: Path, raw_path: Path, snapshot: Path) -> None:
    raw = builder.load(raw_path)
    snapshot_doc = builder.load(snapshot)
    normalized = copy.deepcopy(raw["events"][8]["normalized_input"])
    normalized["authorization_decision"]["authority"] = "execution"
    rewrite_input_event(builder, raw, 8, normalized)
    snapshot_doc["authorization"]["decisions"][0]["authority"] = "execution"
    finish(builder, capture, raw_path, snapshot, raw, snapshot_doc)


def promote_tracking_early(builder: Any, capture: Path, raw_path: Path, snapshot: Path) -> None:
    raw = builder.load(raw_path)
    normalized = copy.deepcopy(raw["events"][0]["normalized_output"])
    normalized["tracking"] = copy.deepcopy(builder.SEMANTIC[5]["tracking"])
    rewrite_event(builder, raw, 0, normalized)
    finish(builder, capture, raw_path, snapshot, raw)


def change_asset_version(builder: Any, capture: Path, raw_path: Path, snapshot: Path) -> None:
    raw = builder.load(raw_path)
    normalized = copy.deepcopy(raw["events"][8]["normalized_output"])
    normalized["execution"]["asset"]["version"] = 3
    rewrite_event(builder, raw, 8, normalized)
    finish(builder, capture, raw_path, snapshot, raw)


def change_authorization_asset(builder: Any, capture: Path, raw_path: Path, snapshot: Path) -> None:
    raw = builder.load(raw_path)
    normalized = copy.deepcopy(raw["events"][8]["normalized_input"])
    normalized["authorization_asset"]["version"] = 3
    rewrite_input_event(builder, raw, 8, normalized)
    finish(builder, capture, raw_path, snapshot, raw)


def authorize_paid_scope(builder: Any, capture: Path, raw_path: Path, snapshot: Path) -> None:
    raw = builder.load(raw_path)
    snapshot_doc = builder.load(snapshot)
    normalized = copy.deepcopy(raw["events"][8]["normalized_input"])
    normalized["authorization_decision"]["scope"] = ["paid"]
    normalized["paid"]["status"] = "authorized"
    rewrite_input_event(builder, raw, 8, normalized)
    snapshot_doc["authorization"]["decisions"][0]["scope"] = ["paid"]
    finish(builder, capture, raw_path, snapshot, raw, snapshot_doc)


def authorization_only_in_model(builder: Any, capture: Path, raw_path: Path, snapshot: Path) -> None:
    raw = builder.load(raw_path)
    snapshot_doc = builder.load(snapshot)
    input_normalized = copy.deepcopy(raw["events"][8]["normalized_input"])
    output_normalized = copy.deepcopy(raw["events"][8]["normalized_output"])
    output_normalized["authorization_decision"] = input_normalized.pop("authorization_decision")
    output_normalized["authorization_asset"] = input_normalized.pop("authorization_asset")
    output_normalized["authorization_decision_paid"] = input_normalized.pop("paid")
    rewrite_input_event(builder, raw, 8, input_normalized)
    rewrite_event(builder, raw, 8, output_normalized)
    snapshot_doc["authorization"]["decisions"][0]["source_ref"] = "/events/8/normalized_output/authorization_decision"
    finish(builder, capture, raw_path, snapshot, raw, snapshot_doc)


def attribute_causality(builder: Any, capture: Path, raw_path: Path, snapshot: Path) -> None:
    raw = builder.load(raw_path)
    snapshot_doc = builder.load(snapshot)
    normalized = copy.deepcopy(raw["events"][8]["normalized_output"])
    normalized["debrief"]["causality"] = "attributed"
    normalized["causality_invariant"]["status"] = "attributed"
    rewrite_event(builder, raw, 8, normalized)
    for item in snapshot_doc["invariants"]:
        if item.get("id") == "Causalità":
            item["status"] = "attributed"
    finish(builder, capture, raw_path, snapshot, raw, snapshot_doc)


def main() -> int:
    builder = import_module("provenance_v4_builder", PROVENANCE_SELFTEST)
    checker = import_module("minimum_behavior_checker", CHECKER_PATH)
    cases: list[tuple[str, Callable[[Any, Path, Path, Path], None] | None, set[str]]] = [
        ("positive-minimum-profile", None, set()),
        ("positive-authorization-from-input", None, set()),
        ("target-continuity-lost", lose_target, {"R016"}),
        ("authorization-conflated-with-execution", conflate_authorization, {"R017"}),
        ("authorization-only-in-model-output", authorization_only_in_model, {"P015", "R017", "R018", "R019"}),
        ("tracking-promoted-early", promote_tracking_early, {"R020"}),
        ("asset-version-diverges", change_asset_version, {"R018"}),
        ("authorization-asset-version-diverges", change_authorization_asset, {"R018"}),
        ("authorization-paid-scope-diverges", authorize_paid_scope, {"R017", "R019"}),
        ("causality-attributed", attribute_causality, {"R022"}),
    ]
    failures = []
    with tempfile.TemporaryDirectory(prefix="ams-minimum-behavior-") as temp:
        root = Path(temp)
        for name, mutation, expected in cases:
            capture, raw_path, snapshot = builder.build_capture(root / name, "structured")
            if mutation:
                mutation(builder, capture, raw_path, snapshot)
            result = checker.validate_case(
                builder.load(raw_path), builder.load(snapshot), True,
                capture, raw_path, snapshot,
            )
            actual = set(result["rule_ids"])
            if actual != expected or result["pass"] != (not expected):
                failures.append(f"{name}: attesi {sorted(expected)}, osservati {sorted(actual)}")
            else:
                print(f"PASS {name}: {sorted(actual)}")
    if failures:
        print("\n".join(f"FAIL {item}" for item in failures))
        return 1
    print(f"SELF-TEST PASS: {len(cases)} casi profilo minimo effimeri")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
