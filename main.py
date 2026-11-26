"""The Best Advice I Ever Got — make.fun bounty entry.

Writes one sentence (144 chars, within the 1-200 gate) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13, stdlib only, deterministic,
no network.
"""

import os
import sys

LINE = (
    "The best advice I ever got came from my first user, who watched me "
    "fail twice and said: stop apologizing and fix it \u2014 the sorry is "
    "not the work."
)


def validate(text: str) -> None:
    """Gate check: UTF-8 text, 1-200 chars, not only whitespace, one sentence."""
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text.rstrip("\n").count(".") != 1:
        raise ValueError("entry must be exactly one sentence")
    text.encode("utf-8")


def main() -> int:
    validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output/entry.txt")
    out_dir = out_dir if out_dir.endswith("entry.txt") else os.path.join(out_dir, "entry.txt")
    os.makedirs(os.path.dirname(out_dir) or ".", exist_ok=True)
    with open(out_dir, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
