#!/usr/bin/env python3
"""Check that declared generator inputs exclude oracles and evaluator artifacts."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
MANIFEST = ROOT / "evals" / "robustness" / "input-boundaries.json"


def main() -> int:
    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
        if manifest.get("schema_version") != 1:
            raise ValueError("versione manifest input non supportata")
        for package in manifest["packages"]:
            for relative in package["allowed"]:
                path = ROOT / relative
                if not path.is_file():
                    raise ValueError(f"input dichiarato mancante: {relative}")
                if any(token.casefold() in relative.casefold() for token in package["forbidden"]):
                    raise ValueError(f"input vietato dichiarato: {relative}")
            for forbidden in package["forbidden"]:
                if forbidden.casefold() in " ".join(package["allowed"]).casefold():
                    raise ValueError(f"filtro vietato non rispettato: {package['id']} / {forbidden}")
    except (OSError, KeyError, TypeError, json.JSONDecodeError, ValueError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    print(f"PASS: isolamento input per {len(manifest['packages'])} pacchetti")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
