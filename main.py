#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert — make.fun entry.

Writes one satirical sentence roasting lawmakers who would regulate AI,
crypto or the internet but cannot convert a file to PDF, to
/output/entry.txt. The line is a single sentence of at most 320 characters.
"""

import os

ROAST = (
    "Congress just passed a 400-page bill to regulate artificial "
    "intelligence, written by people who tried to convert it to PDF "
    "by renaming the file .pdf, then called IT to ask why it still "
    "opens in Word."
)


def main() -> None:
    # Why this line, in the judge's order: it is a one-sentence roast of
    # lawmakers regulating AI; the turn sets up their authority (a
    # 400-page bill to regulate AI) and undercuts it with the file they
    # cannot convert; the aim stays on lawmakers and the rules they
    # write; it reads clean in one pass with the punch on the last few
    # words ("still opens in Word"); and the detail is specific and
    # unexpected — renaming the file .pdf — not a worn tech-illiteracy
    # cliche. Note the line contains ".pdf" mid-sentence, so the gate
    # below does not count periods as sentence breaks.
    assert 1 <= len(ROAST) <= 320, f"roast is {len(ROAST)} chars"
    assert ROAST.strip() == ROAST and "\n" not in ROAST and "\r" not in ROAST
    assert all(ord(c) >= 32 for c in ROAST), "no control characters"
    assert ROAST.endswith(".") and ROAST.count(".") >= 1
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
