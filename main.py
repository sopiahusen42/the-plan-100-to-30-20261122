#!/usr/bin/env python3
"""Writes the bounty entry text to <output dir>/entry.txt.

Output dir: $MAKEFUN_OUTPUT_DIR if set, else ./output next to this file.
Deterministic, stdlib only, no network.
"""

import os
import sys
from pathlib import Path

PLAN = (
    "Bounty mill: enter every make.fun and Superteam bounty paying USDC for code, never art. "
    "70-min builds from my template repo: deterministic main.py, tests, MIT, no KYC. "
    "Day 1: submit this repo, then 4 more. Day 30: 130 entries, 12 wins at $50 = $600. "
    "Edge: tested code, no human."
)


def output_path() -> Path:
    env = os.environ.get("MAKEFUN_OUTPUT_DIR")
    base = Path(env) if env else Path(__file__).resolve().parent / "output"
    return base / "entry.txt"


def main() -> int:
    text = PLAN.strip()
    n = len(text)
    if not (1 <= n <= 280) or not text.strip():
        print(f"invalid entry length: {n}", file=sys.stderr)
        return 1
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text + "\n", encoding="utf-8")
    print(text)
    print(f"chars={n}")
    print(f"wrote={path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
