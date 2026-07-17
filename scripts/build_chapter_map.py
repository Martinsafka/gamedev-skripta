#!/usr/bin/env python3
"""Generate the skills' chapter map from mkdocs.yml + docs/.

Outputs (one identical copy per skill):
  .claude/skills/concept-audit/references/chapter-map.md
  .claude/skills/mechanic-mentor/references/chapter-map.md
Run after adding chapters (see architecture.md → Public URL contract):

    .venv/bin/python scripts/build_chapter_map.py

The map holds routing metadata only (title, live URL, one-line description) —
never chapter content. Rejstřík term anchors are validated against the built
site (site/rejstrik/index.html) when present.
"""
import datetime
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUTS = [
    ROOT / ".claude" / "skills" / "concept-audit" / "references" / "chapter-map.md",
    ROOT / ".claude" / "skills" / "mechanic-mentor" / "references" / "chapter-map.md",
]

DOCUMENTS = ["Teorie her", "Praxe v UE5", "Hudba a zvuk", "Zápisky"]  # nav sections to include


def slugify(text: str) -> str:
    """Replicate python-markdown's default toc slugify (ascii fold)."""
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("ascii")
    text = re.sub(r"[^\w\s-]", "", text).strip().lower()
    return re.sub(r"[\s]+", "-", text)


def clean_line(line: str) -> str:
    """Strip markdown decoration from a prose line for use as a one-liner."""
    line = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", line)  # links -> text
    line = line.replace("**", "").replace("`", "")
    line = re.sub(r"(?<!\w)\*(\S[^*]*\S|\S)\*(?!\w)", r"\1", line)  # *emph*
    return line.strip()


def one_liner(md_path: Path, limit: int = 190) -> str:
    """First prose line after the H1 (zápisky: the Kontext line), trimmed."""
    text = md_path.read_text(encoding="utf-8")
    seen_h1 = False
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith("# ") and not seen_h1:
            seen_h1 = True
            continue
        if line.startswith(("#", ">", "<!--", "![", "---", "```")):
            continue
        if line.startswith("**Kontext:**"):
            line = line[len("**Kontext:**"):].strip()
        if line.startswith("**Zdroj:**"):
            continue
        line = clean_line(line)
        if not line:
            continue
        if len(line) > limit:
            line = line[:limit].rsplit(" ", 1)[0].rstrip(",;:") + "…"
        return line
    return ""


def url_for(path: str, base: str) -> str:
    """docs-relative md path -> live directory URL."""
    if path.endswith("index.md"):
        rel = path[: -len("index.md")]
    else:
        rel = path[:-3] + "/"
    return base + rel


def walk_document(items, base):
    """Yield (téma or None, title, url, one-liner) for one nav document."""
    for item in items:
        if isinstance(item, str):  # document index page
            continue
        for key, value in item.items():
            if isinstance(value, str):  # chapter directly under the document
                yield None, key, url_for(value, base), one_liner(DOCS / value)
            elif isinstance(value, list):  # téma group
                for sub in value:
                    for title, path in sub.items():
                        yield key, title, url_for(path, base), one_liner(DOCS / path)


def rejstrik_terms(base):
    """Yield (term, anchor-url); validate anchors against built HTML if present."""
    built = ROOT / "site" / "rejstrik" / "index.html"
    built_ids = set(re.findall(r'id="([^"]+)"', built.read_text(encoding="utf-8"))) if built.exists() else None
    for line in (DOCS / "rejstrik.md").read_text(encoding="utf-8").splitlines():
        if line.startswith("### "):
            term = line[4:].strip()
            slug = slugify(term)
            if built_ids is not None and slug not in built_ids:
                print(f"WARN: anchor #{slug} ({term}) not found in built site", file=sys.stderr)
            yield term, f"{base}rejstrik/#{slug}"


def main() -> None:
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text(encoding="utf-8"))
    base = config["site_url"].rstrip("/") + "/"
    nav = config["nav"]

    lines = [
        f"# Chapter map — generated {datetime.date.today().isoformat()} by `scripts/build_chapter_map.py`. Do not edit by hand.",
        "",
        f"Routing catalog for audit findings. Base URL: {base}",
        "Slugs and anchors are public API (see agent_docs/architecture.md) — they never get renamed.",
        "",
    ]
    for section in nav:
        for doc_title, items in section.items():
            if doc_title not in DOCUMENTS or not isinstance(items, list):
                continue
            lines.append(f"## {doc_title}")
            current_tema = object()
            for tema, title, url, desc in walk_document(items, base):
                if tema != current_tema:
                    current_tema = tema
                    if tema:
                        lines.append(f"\n### {tema}")
                    else:
                        lines.append("")
                suffix = f" — {desc}" if desc else ""
                lines.append(f"- [{title}]({url}){suffix}")
            lines.append("")

    lines.append("## Rejstřík (term → anchor)")
    lines.append("")
    for term, url in rejstrik_terms(base):
        lines.append(f"- [{term}]({url})")
    lines.append("")

    for out in OUTS:
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("\n".join(lines), encoding="utf-8")
        print(f"Wrote {out.relative_to(ROOT)} ({len(lines)} lines)")


if __name__ == "__main__":
    main()
