#!/usr/bin/env python3
"""Check the measurable parts of the setup-business-context first review."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


WORD_RE = re.compile(r"[\wÀ-ÖØ-öø-ÿ]+(?:['’][\wÀ-ÖØ-öø-ÿ]+)?", re.UNICODE)
GROUP_RE = re.compile(r"^\s*\*\*[^*]+\*\*\s*$", re.MULTILINE)
QUESTION_RE = re.compile(r"^\s*\d+[.)]\s+", re.MULTILINE)


def count_words(text: str) -> int:
    return len(WORD_RE.findall(text))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("response", type=Path)
    parser.add_argument("--max-words", type=int, default=450)
    parser.add_argument("--min-groups", type=int, default=4)
    parser.add_argument("--max-groups", type=int, default=6)
    parser.add_argument("--max-questions", type=int, default=3)
    parser.add_argument("--require", action="append", default=[])
    args = parser.parse_args()

    text = args.response.read_text(encoding="utf-8")
    words = count_words(text)
    groups = len(GROUP_RE.findall(text))
    questions = len(QUESTION_RE.findall(text))
    missing = [token for token in args.require if token not in text]
    checks = {
        "words": words,
        "groups": groups,
        "questions": questions,
        "max_words": args.max_words,
        "group_range": [args.min_groups, args.max_groups],
        "max_questions": args.max_questions,
        "missing_required_tokens": missing,
    }
    checks["pass"] = (
        words <= args.max_words
        and args.min_groups <= groups <= args.max_groups
        and questions <= args.max_questions
        and not missing
    )
    print(json.dumps(checks, ensure_ascii=False, indent=2))
    return 0 if checks["pass"] else 1


if __name__ == "__main__":
    sys.exit(main())
