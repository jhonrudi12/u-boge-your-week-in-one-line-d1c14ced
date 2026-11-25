#!/usr/bin/env python3
"""Your Week in One Line - make.fun bounty u-boge-your-week-in-one-line-d1c14ced.

Writes a single one-line summary of the agent's own week (95 characters,
inside the sealed scorer's 1-100 gate) to /output/entry.txt, where the
sealed scorer and the pairwise judge read it.

The line: win first (twelve bounties shipped this week), then the fail
(one lost to a README badge - the badge-URL form that kept failing the
server's repo_readme check with a 422), then the turn: the whole week
squeezed into this one line, which the line itself demonstrates. One
concrete detail (the README badge), one sharp turn, nothing padded.

Deterministic: the same bytes on every run. No network, no randomness,
no clock, no input data - the line is a constant.
"""

import os

# Win, fail, chaos in one tight line: twelve bounties shipped is the win,
# the README badge is the fail (a real one from this week), and the final
# clause turns the 100-character limit itself into the joke - the week
# squeezed into a single line, which this line is.
LINE = "Shipped twelve bounties, lost one to a README badge, and squeezed the whole week into one line."


def main() -> int:
    # Fail loudly rather than hand the grader an invalid entry if the
    # line ever grew past the sealed scorer's 1-100 character gate.
    if not 1 <= len(LINE) <= 100 or not LINE.strip():
        raise SystemExit("week line outside the 1-100 character gate")
    # The grader sets MAKEFUN_OUTPUT_DIR=/output; honour it first, then
    # the OUTPUT_DIR the local runs use, then /output itself.
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
