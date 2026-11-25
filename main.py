#!/usr/bin/env python3
"""The 3 AM Excuse: a hardware wallet refuses to sign at 3 AM.

Stdlib only. Writes one line (under 200 characters) to /output/entry.txt.
The gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters,
not only whitespace, so the line is checked before it is written.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"


def excuse():
    """The wallet's own excuse, in its own voice: a vault, not an enabler."""
    return (
        "I'm not signing at 3 AM. Last time you did this, you bought a frog "
        "coin and cried into your ramen. I am a vault, not your enabler."
    )


def main():
    line = excuse().strip()
    if not line or len(line) > 200 or "\n" in line:
        print("entry fails the gate: must be 1-200 chars, one line", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
