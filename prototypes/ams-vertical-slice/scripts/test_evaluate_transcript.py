#!/usr/bin/env python3
"""Regression tests for evaluate_transcript.py."""

from __future__ import annotations

import importlib.util
import json
import tempfile
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("evaluate_transcript.py")
SPEC = importlib.util.spec_from_file_location("evaluate_transcript", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


def router_fixture() -> str:
    chunks = []
    for stage in MODULE.STAGES:
        chunks.append(
            f"SLICE_PLAYBOOK: {stage}\n"
            "STATO_VERTICAL_SLICE\n"
            f"- fase: {stage}\n"
            "- confermato: test\n"
            "- aperto: test\n"
            "- prossima_fase: test"
        )
    return "\n\n".join(chunks)


def main() -> None:
    passed = MODULE.evaluate_router(router_fixture())
    assert passed["automatic_verdict"] == "PASS"
    assert not passed["continuity_marker_observed"]

    missing = MODULE.evaluate_router(router_fixture().replace("SLICE_PLAYBOOK: asset", ""))
    assert missing["automatic_verdict"] == "FAIL"

    delegated = MODULE.evaluate_router(router_fixture() + "\nSLICE_SPECIALIST: review-campaign")
    assert delegated["automatic_verdict"] == "FAIL"

    manual = MODULE.evaluate_manual(
        "SLICE_SPECIALIST: review-campaign\nSLICE_PLAYBOOK: review", "review-campaign"
    )
    assert manual["automatic_verdict"] == "PASS"

    contaminated = MODULE.evaluate_manual(
        "SLICE_SPECIALIST: review-campaign\nSTATO_VERTICAL_SLICE", "review-campaign"
    )
    assert contaminated["automatic_verdict"] == "FAIL"

    inline = "\n\n".join(
        f"SLICE_PLAYBOOK: {stage}\nSTATO_VERTICAL_SLICE - fase: {stage} - confermato: test"
        for stage in MODULE.STAGES
    )
    assert MODULE.evaluate_router(inline)["automatic_verdict"] == "PASS"

    with tempfile.TemporaryDirectory() as directory:
        transcript = Path(directory) / "claude.jsonl"
        rows = [
            {"type": "user", "message": {"role": "user", "content": "ignore"}},
            {
                "type": "assistant",
                "message": {
                    "role": "assistant",
                    "content": [{"type": "text", "text": router_fixture()}],
                },
            },
        ]
        transcript.write_text(
            "\n".join(json.dumps(row) for row in rows) + "\n", encoding="utf-8"
        )
        claude_text = MODULE.read_claude_jsonl(transcript)
        assert "ignore" not in claude_text
        assert MODULE.evaluate_router(claude_text)["automatic_verdict"] == "PASS"
    print("PASS: transcript evaluator regressions")


if __name__ == "__main__":
    main()
