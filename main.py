"""The Dog Ate My Homework: Funniest Excuse.

Writes a single line (under 200 characters) in which a dog explains
why the homework got eaten, to $MAKEFUN_OUTPUT_DIR/entry.txt.

Pure Python stdlib. Deterministic: the same line on every run.
"""

import os

EXCUSE = (
    "The homework sat there all evening whispering 'bet you won't,' "
    "so I ate it. I have never backed down from a piece of paper in my life."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
