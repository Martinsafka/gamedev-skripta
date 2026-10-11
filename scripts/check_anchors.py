#!/usr/bin/env python3
"""Check in-site anchor links in docs/ against the ids of the built site.

Covers both kinds: cross-page `[x](../teorie/scope.md#frag)` and same-page
`[x](#frag)`. Every fragment must exist as an `id="…"` in the target page's
built HTML (site/<dir>/<slug>/index.html), so the slugs come from MkDocs
itself, not from a re-implementation. External http(s) links are skipped.

Run it right after the build (synthesis_guide → per-batch checklist, item 6):

    .venv/bin/mkdocs build --strict
    .venv/bin/python -I scripts/check_anchors.py

Prints `file:line` for every broken link plus a summary; exits 1 on any
problem, 2 when site/ has not been built.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
SITE = ROOT / "site"
LINK = re.compile(r"\]\(([^)\s]*?)#([^)\s]+)\)")
ID = re.compile(r'id="([^"]+)"')

_ids = {}


def ids_for(md: Path):
    """Ids in the built page of a docs/ markdown file, or None when it was not built."""
    rel = md.relative_to(DOCS)
    html = SITE / rel.parent / ("" if rel.stem == "index" else rel.stem) / "index.html"
    if html not in _ids:
        _ids[html] = set(ID.findall(html.read_text(encoding="utf-8"))) if html.exists() else None
    return _ids[html]


def problem_of(md: Path, target: str, frag: str):
    tgt = (md.parent / target).resolve() if target else md
    if not tgt.is_file():
        return "missing file"
    try:
        ids = ids_for(tgt)
    except ValueError:
        return "target outside docs/"
    if ids is None:
        return "page not built"
    return None if frag in ids else "no such id"


def main() -> int:
    if not (SITE / "index.html").exists():
        print("site/ is not built; run .venv/bin/mkdocs build --strict first")
        return 2
    total = bad = same_page = 0
    for md in sorted(DOCS.rglob("*.md")):
        text = md.read_text(encoding="utf-8")
        for m in LINK.finditer(text):
            target, frag = m.groups()
            if target.startswith(("http://", "https://")):
                continue
            total += 1
            same_page += not target
            problem = problem_of(md, target, frag)
            if problem:
                bad += 1
                line = text.count("\n", 0, m.start()) + 1
                print(f"{md.relative_to(ROOT)}:{line}: {target}#{frag}: {problem}")
    print(f"checked {total} anchor links ({total - same_page} cross-page, {same_page} same-page), {bad} problems")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
