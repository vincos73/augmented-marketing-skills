#!/usr/bin/env python3
"""Run validator fixtures and canonical-example checks."""

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
VALIDATOR = ROOT / "scripts" / "validate_svg.py"


def run(path):
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(path)],
        capture_output=True,
        text=True,
        check=False,
    )


def main():
    valid_files = sorted((ROOT / "tests").glob("valid*.svg"))
    invalid_files = sorted((ROOT / "tests").glob("invalid*.svg"))
    examples = sorted((ROOT / "assets" / "examples").glob("*.svg"))
    failures = []

    for path in valid_files + examples:
        result = run(path)
        if result.returncode != 0:
            failures.append(f"doveva passare: {path.name}: {result.stdout.strip()}")

    for path in invalid_files:
        result = run(path)
        if result.returncode == 0:
            failures.append(f"doveva fallire: {path.name}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    print(
        f"OK: {len(valid_files)} fixture valide, "
        f"{len(invalid_files)} fixture invalide e {len(examples)} esempi canonici"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
