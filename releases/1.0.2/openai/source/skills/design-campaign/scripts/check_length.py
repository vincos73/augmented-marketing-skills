#!/usr/bin/env python3
"""Count a draft from stdin; print metadata only, with no file or network access."""
import argparse
import hashlib
import json
import sys


def count_words(text):
    return sum(any(character.isalnum() for character in token) for token in text.split())


def inspect_text(text, limit):
    count = count_words(text)
    return {
        "word_count": count,
        "max_words": limit,
        "within_limit": count <= limit,
        "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--max-words", type=int, required=True)
    args = parser.parse_args()
    if args.max_words < 1:
        parser.error("--max-words must be positive")
    result = inspect_text(sys.stdin.read(), args.max_words)
    print(json.dumps(result, ensure_ascii=False))
    return 0 if result["within_limit"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
