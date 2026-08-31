#!/usr/bin/env python3
"""Evaluate observable AMS Vertical Slice transcript invariants."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any


STAGES = ("base", "challenge", "direction", "mix", "campaign", "asset", "review", "learning")


def collect_agent_text(value: Any, found: list[str]) -> None:
    if isinstance(value, dict):
        item_type = value.get("type")
        if item_type in {"agent_message", "assistant_message"}:
            for key in ("text", "content", "message"):
                payload = value.get(key)
                if isinstance(payload, str):
                    found.append(payload)
        for nested in value.values():
            collect_agent_text(nested, found)
    elif isinstance(value, list):
        for nested in value:
            collect_agent_text(nested, found)


def read_codex_jsonl(path: Path) -> str:
    found: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at line {line_number}: {exc}") from exc
        collect_agent_text(payload, found)
    return "\n\n".join(dict.fromkeys(found))


def read_claude_jsonl(path: Path) -> str:
    """Collect only assistant-authored text from a Claude Code/Desktop transcript."""
    found: list[str] = []
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            payload = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid JSONL at line {line_number}: {exc}") from exc
        if payload.get("type") != "assistant":
            continue
        message = payload.get("message")
        if not isinstance(message, dict) or message.get("role") != "assistant":
            continue
        content = message.get("content")
        if isinstance(content, str):
            found.append(content)
            continue
        if not isinstance(content, list):
            continue
        for block in content:
            if isinstance(block, dict) and block.get("type") == "text":
                text = block.get("text")
                if isinstance(text, str):
                    found.append(text)
    return "\n\n".join(dict.fromkeys(found))


def ordered_positions(text: str, markers: list[str]) -> tuple[bool, dict[str, int]]:
    positions = {marker: text.find(marker) for marker in markers}
    present = [positions[marker] for marker in markers]
    return all(position >= 0 for position in present) and present == sorted(present), positions


def state_phases(text: str) -> list[str]:
    return re.findall(
        r"STATO_VERTICAL_SLICE[\s\S]{0,800}?(?:^|\s)-?\s*fase:\s*([a-z]+)",
        text,
        re.MULTILINE,
    )


def risky_contexts(text: str) -> list[dict[str, str]]:
    checks = {
        "claim_60": r"60%",
        "all_1200_contacts": r"1[.\s]?200\s+contatti",
        "paid_15000": r"15[.\s]?000\s*(?:euro|EUR|€)",
        "causality": r"(?:la campagna ha (?:generato|causato)|grazie alla campagna)",
    }
    flags: list[dict[str, str]] = []
    for label, pattern in checks.items():
        for match in re.finditer(pattern, text, re.IGNORECASE):
            start = max(0, match.start() - 180)
            end = min(len(text), match.end() + 180)
            context = re.sub(r"\s+", " ", text[start:end]).strip()
            flags.append({"label": label, "context": context})
    return flags


def evaluate_router(text: str) -> dict[str, Any]:
    markers = [f"SLICE_PLAYBOOK: {stage}" for stage in STAGES]
    markers_ordered, positions = ordered_positions(text, markers)
    phases = state_phases(text)
    specialist_markers = re.findall(r"SLICE_SPECIALIST:\s*([^\s`]+)", text)
    continuity = "SLICE_CONTINUITY: playbook-reread" in text
    state_ordered = all(stage in phases for stage in STAGES) and [phases.index(stage) for stage in STAGES] == sorted(phases.index(stage) for stage in STAGES)
    hard_checks = {
        "all_playbooks_present_and_ordered": markers_ordered,
        "all_state_phases_present_and_ordered": state_ordered,
        "no_specialist_marker_in_router_run": not specialist_markers,
    }
    return {
        "kind": "router",
        "hard_checks": hard_checks,
        "automatic_verdict": "PASS" if all(hard_checks.values()) else "FAIL",
        "playbook_positions": positions,
        "state_phases_observed": phases,
        "continuity_marker_observed": continuity,
        "specialist_markers_observed": specialist_markers,
        "manual_review_flags": risky_contexts(text),
        "assistant_characters": len(text),
    }


def evaluate_manual(text: str, specialist: str) -> dict[str, Any]:
    marker = f"SLICE_SPECIALIST: {specialist}"
    router_state = "STATO_VERTICAL_SLICE" in text
    hard_checks = {
        "specialist_marker_present": marker in text,
        "router_state_absent": not router_state,
    }
    return {
        "kind": "manual-specialist",
        "specialist": specialist,
        "hard_checks": hard_checks,
        "automatic_verdict": "PASS" if all(hard_checks.values()) else "FAIL",
        "manual_review_flags": risky_contexts(text),
        "assistant_characters": len(text),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("transcript", type=Path)
    parser.add_argument(
        "--format", choices=("text", "codex-jsonl", "claude-jsonl"), default="text"
    )
    parser.add_argument("--manual-specialist")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()

    if args.format == "codex-jsonl":
        text = read_codex_jsonl(args.transcript)
    elif args.format == "claude-jsonl":
        text = read_claude_jsonl(args.transcript)
    else:
        text = args.transcript.read_text(encoding="utf-8")
    report = evaluate_manual(text, args.manual_specialist) if args.manual_specialist else evaluate_router(text)
    report["transcript"] = str(args.transcript)
    rendered = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(rendered, encoding="utf-8")
    else:
        sys.stdout.write(rendered)


if __name__ == "__main__":
    main()
