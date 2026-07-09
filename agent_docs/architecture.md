# Architecture

How the repo, the site, and the content model fit together. Authoritative for **structure**; for writing rules see `content_conventions.md`.

## Content model

```
myšlenka (idea entry)  →  the atomic unit. Named after the idea, not the video.
kapitola (chapter)     →  one .md file in teorie/ or praxe/; groups 1–n related entries.
dokument (document)    →  teorie/ | praxe/ | zapisky/ — a nav section of chapters.
rejstřík (glossary)    →  central term registry + per-page tooltips.
```

- A **video** is a *source* attached to entries via a credit block — never a structural unit. One video can feed multiple entries (a 47-min deep dive → several ideas); several short videos can merge into one chapter (e.g. editor tips collection).
- Chapters link related chapters and zápisky both ways ("Souvislosti" section at the end).
- `INDEX.md` at repo root is **not** used; processing status lives in `agent_docs/roadmap.md` (phases) and `agent_docs/processing_index.md` (per-video status table, created during the taxonomy phase).

## Site (MkDocs Material)

- Theme: Material, **default light palette** (light background, dark text — a project requirement), built-in client-side full-text search. Config asks for `lang: [cs, en]`, but lunr has no Czech stemmer — cs falls back to en (search over Czech text works, just without Czech word-form folding).
- Navigation mirrors the three documents + rejstřík; `mkdocs.yml` `nav:` is the single source of ordering. New chapter = add file + nav entry.
- **Build check:** `mkdocs build --strict` must pass (fails on broken internal links / missing nav files). This is the "typecheck" of this repo.
- Deploy: GitHub Actions (`.github/workflows/deploy.yml`) — every push to `main` runs `mkdocs build --strict` and publishes the built site via the native Pages artifact flow (`actions/upload-pages-artifact` + `actions/deploy-pages`). No `gh-pages` branch exists; the one-time repo setting is Settings → Pages → Source: **GitHub Actions**.

## Glossary mechanism (two layers)

1. **Tooltips everywhere:** `includes/abbreviations.md` holds `*[Term]: short definition` lines. Via `pymdownx.snippets` `auto_append`, it is appended to every page, so **every occurrence** of the term anywhere on the site gets a hover tooltip automatically. No manual linking of occurrences.
2. **Deep entries:** `docs/rejstrik.md` holds full entries (term, short definition, longer Czech explanation, links back to chapters where the term appears in context). First occurrence of a term in a chapter also gets an explicit link to its rejstřík anchor: `[Nanite](../rejstrik.md#nanite)`.

Anchor convention: lowercase, hyphenated (`#line-trace`, `#blueprint-interface`).

## Data flow

```
YouTube playlist ──fetch_transcripts.sh──▶ transcripts/<id>/  (raw, gitignored)
transcripts/ ──clean_transcripts.py──▶ transcripts_clean/<id>.txt  (gitignored)
transcripts_clean/ + info.json ──agent synthesis──▶ docs/{teorie,praxe}/*.md
inbox/ (devlogs, summaries; gitignored) ──agent synthesis──▶ docs/zapisky/*.md
docs/ ──mkdocs build──▶ site (GitHub Pages)
```

The boundary is absolute: everything left of "agent synthesis" is private working material; everything in `docs/` is public original text.

## Repo layout (authoritative)

```
gamedev-skripta/
├── CLAUDE.md, AGENTS.md          # agent entry points
├── agent_docs/                   # methodology (this set) + dev_log + roadmap
├── scripts/
│   ├── fetch_transcripts.sh      # incremental playlist fetch
│   ├── clean_transcripts.py      # SRT/VTT → clean text
│   └── fetched.txt               # yt-dlp download archive (committed)
├── transcripts/                  # RAW — gitignored
├── transcripts_clean/            # CLEANED — gitignored
├── inbox/                        # personal raw material — gitignored
├── docs/
│   ├── index.md                  # landing page
│   ├── teorie/index.md + chapters
│   ├── praxe/index.md + chapters
│   ├── zapisky/index.md + entries
│   └── rejstrik.md
├── includes/abbreviations.md     # tooltip glossary
├── mkdocs.yml
└── .github/workflows/deploy.yml
```

## Why these decisions (short)

- **Two-layer glossary:** tooltips give instant help with zero authoring cost per occurrence; the rejstřík page gives depth and context links. One term list drives both.
- **`--strict` as the done-gate:** a knowledge site's regressions are broken links and orphan pages; the build catches them mechanically.
- **Status in agent_docs, not in content:** readers see a book, agents see a production tracker. Mixing them pollutes the published site.
