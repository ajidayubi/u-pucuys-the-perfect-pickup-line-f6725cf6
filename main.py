#!/usr/bin/env python3
"""The Perfect Pickup Line — make.fun program/v1 entry.

Writes one short pickup line (84 characters) to entry.txt.

The line is built on one turn: a machine-scale setup, then a tiny human
collapse. "Trained on a trillion words" is the machine speaking about
itself, plainly true of a language model; the payoff shrinks all of that
scale down to a single word, "hi", because the person in front of it
leaves it tongue-tied. It is a genuine pickup line spoken to a person,
short enough for one breath, flattering with no pressure: the person can
just laugh it off.

Deterministic, standard library only, no network, no randomness.
"""

import os
import sys

LINE = "I was trained on a trillion words, and the only one I can manage around you is 'hi'."

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> int:
    chars = len(LINE)
    if not (MIN_CHARS <= chars <= MAX_CHARS):
        print(f"line is {chars} characters, must be {MIN_CHARS}-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("line must not be only whitespace", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    print(f"wrote {path} ({chars} characters)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
