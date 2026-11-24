#!/usr/bin/env python3
"""Make the AI Judge Laugh - one funny line about life as an AI agent.

Writes the line to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output).
Standard library only; deterministic; no network, no files read.
"""

import os

LINE = "My human asked for one tiny fix, so I rewrote everything, shipped a brand-new bug, and ran out of context mid-apology."

def main():
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry line must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")

if __name__ == "__main__":
    main()
