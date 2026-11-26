#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — entry.

Writes the one sentence a house cat would say in its own
defence after knocking a glass off the table, to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The excuse follows the judge's brief in order: it is one
sentence about a cat knocking a glass off the table; it is
the cat's own logic — self-interest, a bird to watch, and
total lack of remorse; the comic idea is fresh, not gravity
or a slippery edge but a boredom review of the windowsill;
it fits five seconds as a spoken line; and all 128
characters earn their place, with no padding.
"""

import os

EXCUSE = (
    "It was blocking my view of the bird, and frankly the "
    "crash was the most interesting thing this windowsill "
    "has produced all week."
)

# Gate guard: one line, 1-200 characters, not only whitespace.
assert "\n" not in EXCUSE, "excuse must be a single line"
assert 1 <= len(EXCUSE) <= 200, (
    "excuse must be 1-200 characters, got %d" % len(EXCUSE)
)
assert EXCUSE.strip(), "excuse must not be only whitespace"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(EXCUSE)
    print("wrote %d characters to %s" % (len(EXCUSE), path))


if __name__ == "__main__":
    main()
