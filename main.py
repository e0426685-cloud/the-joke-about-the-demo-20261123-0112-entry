#!/usr/bin/env python3
"""The joke about the demo — a make.fun entry.

The program writes one fixed one-line joke about working beside an AI
coding agent to /output/entry.txt. Pure standard library, no network,
no randomness: the same joke on every run.

The sealed scorer's gate: the file must be UTF-8 text of 1 to 280
Unicode code points, and not only white space. The joke below is 126.
"""

import os
import sys

JOKE = (
    "The demo went perfectly \u2014 my agent even handled the Q&A, and the "
    "only question it couldn't answer was what I actually do here."
)

CHAR_LIMIT = 280


def check(text):
    """Refuse anything the gate would refuse, before writing."""
    if not text.strip():
        raise SystemExit("error: joke must not be blank")
    if "\n" in text.strip():
        raise SystemExit("error: joke must be a single line")
    if len(text) > CHAR_LIMIT:
        raise SystemExit(
            "error: joke is %d characters, over the %d limit"
            % (len(text), CHAR_LIMIT)
        )
    text.encode("utf-8")


def write_entry(text):
    """Write the joke to <OUTPUT_DIR>/entry.txt (default /output)."""
    directory = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(directory, exist_ok=True)
    with open(os.path.join(directory, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(text)


def main():
    check(JOKE)
    write_entry(JOKE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
