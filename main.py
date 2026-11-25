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
Revision v2: the line is now assembled from named parts by build_advice(),
which validates length and single-sentence shape before anything is
written, so the entry text is constructed and checked in one place.
Revision v3: limits are named constants, validation reports the exact
offending length and which rule failed, and the line is checked to be a
single physical line (no embedded newline) before it is written.
"""

import os

MIN_LEN = 1
MAX_LEN = 200

SPEAKER = "My grandma"
ADVICE_GIVEN = "said never trust a fart after forty"
AFTERMATH = "and twenty years on, it is still the most honest health advice anyone has ever given me."


def build_advice() -> str:
    """Assemble the entry line from its parts and validate it."""
    text = " ".join([SPEAKER, ADVICE_GIVEN + ",", AFTERMATH]).strip()
    if not MIN_LEN <= len(text) <= MAX_LEN:
        raise ValueError(
            f"entry length {len(text)} outside allowed range "
            f"{MIN_LEN}-{MAX_LEN} characters"
        )
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line, found embedded newline")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("entry must be exactly one sentence ending in '.'")
    return text


def main() -> None:
    text = build_advice()
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
