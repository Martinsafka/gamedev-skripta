#!/usr/bin/env python3
"""Check docs/rejstrik.md: alphabetical order and the two glossary layers.

Order: the `### Term` entries must be sorted by key(term): diacritics dropped
(NFKD), lowercase, only a-z0-9 kept, so "B-roll" sorts as "broll", "Tónina" as
"tonina" and "A/B test" as "abtest". Equal keys keep their order. Czech
collation (ch after h) is deliberately not used, the terms are mostly English.
Batch glossary scripts insert with the same key.

Layers: every entry has a `*[Term]: …` tooltip in includes/abbreviations.md and
every tooltip has an entry, except the deliberate cases below. Entries must not
point at a neighbour by position („předchozí heslo", „viz výše"), because
sorting moves them; link the term instead.

    .venv/bin/python -I scripts/check_rejstrik.py          # check
    .venv/bin/python -I scripts/check_rejstrik.py --fix    # sort the entries in place

--fix only reorders whole entries (a `### ` header up to the next one) and
leaves their text untouched. Prints `file:line` for every problem plus a
summary; exits 1 on any problem left.
"""
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REJSTRIK = ROOT / "docs" / "rejstrik.md"
ABBR = ROOT / "includes" / "abbreviations.md"
# Deliberate differences between the layers.
NO_TOOLTIP = {"Anchor (marketing)", "Pivot (design)"}  # qualified second senses, text never writes the qualifier
NO_ENTRY = {"GDD"}  # tooltip-only alias of "Game Design Document"
POSITIONAL = re.compile(r"(předchozí|následující) heslo|viz (výše|níže)", re.I)


def key(term: str) -> str:
    t = unicodedata.normalize("NFKD", term).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]", "", t)


def split(text: str):
    """(intro lines, [(line number, entry lines)]); trailing blank lines are not part of an entry."""
    lines = text.split("\n")
    starts = [i for i, l in enumerate(lines) if l.startswith("### ")]
    entries = []
    for a, b in zip(starts, starts[1:] + [len(lines)]):
        chunk = lines[a:b]
        while chunk and not chunk[-1].strip():
            chunk.pop()
        entries.append((a + 1, chunk))
    return lines[:starts[0]], entries


def check():
    """(problems, number of entries, number of tooltips)."""
    rel, abbr_rel = REJSTRIK.relative_to(ROOT), ABBR.relative_to(ROOT)
    _, entries = split(REJSTRIK.read_text(encoding="utf-8"))
    terms = [(line, chunk[0][4:].strip()) for line, chunk in entries]
    problems = []
    for (prev_line, prev), (line, term) in zip(terms, terms[1:]):
        if key(term) < key(prev):
            problems.append(f'{rel}:{line}: "{term}" sorts before "{prev}" (line {prev_line})')
    for line, chunk in entries:
        for off, l in enumerate(chunk[1:], 1):
            if l.startswith(("# ", "## ")):
                problems.append(f"{rel}:{line + off}: heading inside the entry list")
            m = POSITIONAL.search(l)
            if m:
                problems.append(f'{rel}:{line + off}: positional reference "{m.group(0)}" breaks when entries move')
    for term, n in Counter(t for _, t in terms).items():
        if n > 1:
            problems.append(f'{rel}: duplicate entry "{term}" ({n}x)')
    tips = [(i + 1, l[2:l.index("]:")]) for i, l in enumerate(ABBR.read_text(encoding="utf-8").split("\n"))
            if l.startswith("*[") and "]:" in l]
    for term, n in Counter(t for _, t in tips).items():
        if n > 1:
            problems.append(f'{abbr_rel}: duplicate tooltip "{term}" ({n}x)')
    heads, tip_terms = {t for _, t in terms}, {t for _, t in tips}
    for line, term in terms:
        if term not in tip_terms and term not in NO_TOOLTIP:
            problems.append(f'{rel}:{line}: "{term}" has no tooltip in {abbr_rel}')
    for line, term in tips:
        if term not in heads and term not in NO_ENTRY:
            problems.append(f'{abbr_rel}:{line}: tooltip "{term}" has no entry')
    return problems, len(terms), len(tips)


def sort_entries() -> int:
    """Sort the entries in place; returns how many changed position."""
    text = REJSTRIK.read_text(encoding="utf-8")
    intro, entries = split(text)
    chunks = [chunk for _, chunk in entries]
    ordered = sorted(chunks, key=lambda c: key(c[0][4:]))
    out = "\n".join(intro) + "\n" + "\n\n".join("\n".join(c) for c in ordered) + ("\n" if text.endswith("\n") else "")
    REJSTRIK.write_text(out, encoding="utf-8")
    return sum(a is not b for a, b in zip(chunks, ordered))


def main() -> int:
    if "--fix" in sys.argv[1:]:
        problems, _, _ = check()
        blocking = [p for p in problems if "heading inside" in p or "positional reference" in p]
        if blocking:
            print("not sorting, fix these first:", *blocking, sep="\n")
            return 1
        print(f"sorted: {sort_entries()} entries changed position")
    problems, n_entries, n_tips = check()
    for p in problems:
        print(p)
    print(f"checked {n_entries} entries and {n_tips} tooltips, {len(problems)} problems")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
