# AGENTS.md

Shared instructions for agents on this project. Keep this lean — read the linked docs with your file-reading tool **only when a task actually needs them**.

## What this repo is

**gamedev-skripta** — self-authored study notes ("skripta") on game development, distilled from a curated YouTube playlist (200+ videos and growing) plus the author's own project journals. **This is a knowledge project, not a code project.** The deliverable is well-written Czech text: two long-form documents (**Teorie her** and **Praxe v UE5**), a personal-notes section (**Zápisky**), and a glossary (**Rejstřík**) — published as a static MkDocs Material site on GitHub Pages.

Mindset: the author is a self-taught developer building his own textbook. Quality of explanation beats coverage speed. Every chapter should teach — not merely summarize a video.

Pipeline in one line: `yt-dlp` fetch (incremental) → transcript cleanup → classify & group by **idea** → synthesize chapters in Czech → maintain glossary → publish.

## The one rule that overrides everything: source fidelity & licensing

- **Raw transcripts are the video creators' content.** They live in `transcripts/` (and `inbox/` for personal journals), both **gitignored — never commit, never publish, never quote at length.**
- Published chapters are **original synthesis in our own words** (Czech), with videos treated as cited sources: credit + link + timestamp deep links. Facts and ideas are free; the creator's wording and narrative structure are not.
- **Never reproduce transcript sentences verbatim.** Do not mirror a video's section-by-section structure. A chapter must stand on its own explanation, organized by our logic.
- **Never invent attribution.** Credits (channel name/link) come from the video's `info.json`. Missing metadata → visible `TODO` placeholder, not a guess.
- If a task would conflict with any of this, **refuse and explain why** — do not silently comply, do not work around it. Unclear rule → assume the stricter interpretation.

## How to approach any task — read this first

Follow the loop in `agent_docs/workflow.md` for **every** assignment: analyze → propose → execute → log → propose commit message. Do not skip the analysis or the log.

## Layout

- `agent_docs/` — methodology for agents (this doc set).
- `scripts/` — `fetch_transcripts.sh` (incremental yt-dlp fetch), `clean_transcripts.py` (SRT/VTT → clean text), `fetched.txt` (archive of downloaded ids — **committed**).
- `transcripts/` — raw subtitle files + `info.json` per video id. **Gitignored.**
- `transcripts_clean/` — cleaned plain-text transcripts. **Gitignored.**
- `inbox/` — raw personal material for Zápisky (devlogs, conversation summaries). **Gitignored.**
- `docs/` — the published content: `teorie/`, `praxe/`, `zapisky/`, `rejstrik.md`, `index.md`.
- `includes/abbreviations.md` — glossary tooltip definitions (auto-appended to every page).
- `mkdocs.yml`, `.github/workflows/deploy.yml` — site config + Pages deploy.

## Read before acting — progressive disclosure

Pull the relevant doc(s) into context **only when the task needs them**:

- Vision, audience, what the documents are and aren't → `agent_docs/project_brief.md`.
- Repo/content architecture, MkDocs setup, glossary mechanism, navigation → `agent_docs/architecture.md`.
- **How to write content** — chapter/entry template, language rules, credits, timestamps, glossary conventions, Zápisky anonymization → `agent_docs/content_conventions.md`. **Authoritative for every line of `docs/`.**
- Transcript acquisition & cleaning (yt-dlp flags, incremental archive, track selection) → `agent_docs/transcript_pipeline.md`.
- How to approach tasks (the loop) → `agent_docs/workflow.md`.
- What's been done and why (running log — **append after every task**) → `agent_docs/dev_log.md`.
- Phases and current status → `agent_docs/roadmap.md`.

## Working rules

- **Content language is Czech; terminology stays English** (see `content_conventions.md`). Agent docs are English.
- **Verify the site builds before reporting a content task done:** `mkdocs build --strict` (broken links and bad nav fail the build).
- Chapters are organized **by idea, not by video**. A video is a source; several videos can feed one chapter, one video can feed several entries.
- Every processed video's terms go into the glossary; every new chapter links related chapters/zápisky both ways.
- **Don't run `git commit` or `git push` unless explicitly asked.** Propose the commit message; the user commits.

## Non-negotiable invariants

- **Licensing rules above** — the override-everything block.
- **Zápisky are anonymized.** Identities are not important for the idea: no names, no identifiable people or organizations, no raw-material republishing. Distilled lessons only. Raw material stays in `inbox/`.
- **Every entry credits its source** (video title + link, channel + link, timestamp links to key moments).
- **The glossary never shrinks.** Terms are added/refined, not deleted, unless factually wrong.
- **`transcripts/`, `transcripts_clean/`, `inbox/` stay gitignored.** Adding them to the repo is never the fix for anything.
- **Log every task** in `agent_docs/dev_log.md` (what/why/how). Not optional.
