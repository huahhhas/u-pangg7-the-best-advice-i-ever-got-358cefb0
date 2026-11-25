#!/usr/bin/env python3
"""The Best Advice I Ever Got entry.

Writes one original sentence (1-200 characters) about the best advice
the writer ever received, to /output/entry.txt. Pure stdlib; deterministic.

Draft v1: "My grandma told me never to trust a fart after forty, and twenty
years later it is still the most honest health advice anyone has ever
given me."
Revision: tightened "told me never to trust" -> "said never trust" and
"twenty years later" -> "twenty years on" so the line reads in one breath
and the punch lands on the last words.
"""

import os

ADVICE = "My grandma said never trust a fart after forty, and twenty years on, it is still the most honest health advice anyone has ever given me."


def main() -> None:
    text = ADVICE.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") == 1 and text.endswith("."), "entry must be one sentence"
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
