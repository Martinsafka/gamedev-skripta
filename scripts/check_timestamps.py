#!/usr/bin/env python3
"""Check timestamp deep links in docs/ against the local transcripts.

A link `[(m:ss)](https://www.youtube.com/watch?v=ID&t=Ns)` is valid when
  1. its label is m:ss / h:mm:ss of N (`1:04:09`, never `64:09`), and
  2. N is a block marker `[m:ss | t=Ns]` in transcripts_clean/ID.txt, or an
     exact cue start in the raw track named by that file's `# source_file:`
     header. Older entries (mostly July 2026) link cue starts; those are valid
     and more precise than blocks (content_conventions.md → Timestamp links).

Needs the gitignored transcripts_clean/ and transcripts/, so it is a local
gate, not a CI step. Run it on the touched chapters after every batch:

    .venv/bin/python -I scripts/check_timestamps.py                  # all of docs/
    .venv/bin/python -I scripts/check_timestamps.py docs/teorie/scope.md

Prints `file:line` for every bad link plus a summary; exits 1 on any problem.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[\((\d+(?::\d+){1,2})\)\]\(https://www\.youtube\.com/watch\?v=([\w-]{11})&t=(\d+)s\)")
MARK = re.compile(r"^\[\d+(?::\d+){1,2} \| t=(\d+)s\]", re.M)
CUE = re.compile(r"(\d{1,2}):(\d{2}):(\d{2})[.,]\d{3}\s*-->")

_starts = {}


def fmt(seconds: int) -> str:
    """Label format of clean_transcripts.fmt_ts."""
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def starts(vid: str):
    """(block starts, cue starts) of a video, or (None, None) without a transcript."""
    if vid not in _starts:
        clean = ROOT / "transcripts_clean" / f"{vid}.txt"
        if not clean.exists():
            _starts[vid] = (None, None)
            return _starts[vid]
        text = clean.read_text(encoding="utf-8")
        blocks = {int(t) for t in MARK.findall(text)}
        cues = set()
        src = re.search(r"^# source_file: (.+)$", text, re.M)
        raw = ROOT / "transcripts" / vid / src.group(1).strip() if src else None
        if raw and raw.exists():
            raw_text = raw.read_text(encoding="utf-8", errors="replace")
            cues = {int(h) * 3600 + int(m) * 60 + int(s) for h, m, s in CUE.findall(raw_text)}
        _starts[vid] = (blocks, cues)
    return _starts[vid]


def shown(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT))
    except ValueError:
        return str(path)


def main() -> int:
    files = [Path(a) for a in sys.argv[1:]] or sorted((ROOT / "docs").rglob("*.md"))
    total = bad = on_block = on_cue = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        for m in LINK.finditer(text):
            total += 1
            label, vid, t = m.group(1), m.group(2), int(m.group(3))
            blocks, cues = starts(vid)
            problems = []
            if label != fmt(t):
                problems.append(f"label {label} != {fmt(t)}")
            if blocks is None:
                problems.append("no transcript")
            elif t in blocks:
                on_block += 1
            elif t in cues:
                on_cue += 1
            else:
                problems.append("not a block or cue start")
            if problems:
                bad += 1
                line = text.count("\n", 0, m.start()) + 1
                print(f"{shown(f)}:{line}: ({label}) {vid} t={t}: " + "; ".join(problems))
    print(f"checked {total} timestamps ({on_block} on block starts, {on_cue} on exact cue starts), {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
