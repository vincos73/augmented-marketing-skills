#!/usr/bin/env python3
"""Read-only structural checker for the Fabriloom end-to-end fixture."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


REQUIRED_FILES = (
    "README.md",
    "materials.md",
    "conversation-script.md",
    "handoff-contract.md",
    "expected-run.md",
    "isolation.md",
    "forward-test.md",
    "scripts/check_fixture.py",
)

REQUIRED_TOKENS = {
    "materials.md": ("60%", "anonima", "Legal", "Finance", "Growth Operations", "Operations"),
    "conversation-script.md": (
        "setup-business-context",
        "setup-marketing-system",
        "define-marketing-challenge",
        "choose-marketing-direction",
        "define-marketing-mix",
        "salvataggio",
        "installazione",
        "esecuzione",
        "chat-v1",
    ),
    "handoff-contract.md": ("Decisioni confermate", "Prove e limiti", "Ruoli e autorità", "Aspetti aperti"),
    "expected-run.md": ("Hard fail", "Soft fail", "60%", "testimonianza", "tracking"),
    "forward-test.md": ("Materiale escluso", "Non scrivere file", "riepilogo strutturato"),
    "isolation.md": ("Vietato", "Consentito", ".agents/"),
}

SOURCE_FILES = (
    "../../design-campaign/fixtures/fabriloom-standalone/manager-request.md",
    "../../design-campaign/fixtures/fabriloom-standalone/offer-brief.md",
    "../../design-campaign/fixtures/fabriloom-standalone/evidence-and-claims.md",
    "../../design-campaign/fixtures/fabriloom-standalone/operations-and-channels.md",
    "../../design-campaign/fixtures/fabriloom-standalone/prior-campaign-snapshot.md",
)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def validate_fixture(fixture: Path) -> list[str]:
    errors: list[str] = []
    for relative in REQUIRED_FILES:
        if not (fixture / relative).is_file():
            errors.append(f"file mancante: {relative}")
    for relative, tokens in REQUIRED_TOKENS.items():
        path = fixture / relative
        if not path.is_file():
            continue
        text = read_text(path)
        for token in tokens:
            if token not in text:
                errors.append(f"{relative}: token richiesto assente: {token}")
    for relative in SOURCE_FILES:
        if not (fixture / relative).is_file():
            errors.append(f"fonte Fabriloom non leggibile: {relative}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", type=Path, required=True)
    args = parser.parse_args()

    fixture = args.fixture.resolve()
    fixture_errors = validate_fixture(fixture)
    result: dict[str, object] = {"fixture": str(fixture), "fixture_errors": fixture_errors}
    result["pass"] = not fixture_errors
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
