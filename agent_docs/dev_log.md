# Dev Log

Running log of changes — the project's memory for future sessions. **Append a new entry after every task** (newest at the top). Keep entries concrete and skimmable, not verbose.

## How to write an entry

Each entry has: a dated title, then **What / Why / How** (and optional **Follow-ups**):

- **What** — what changed (chapters / entries / terms / files touched).
- **Why** — the goal or reason.
- **How** — approach taken, key decisions, tradeoffs, anything non-obvious the next session needs.
- **Follow-ups** — known gaps, TODOs, deferred items (optional).

---

<!-- Newest entries below. Add yours on top of the list. -->

### 2026-07-09 — Phase 0 part 2: full fetch, clean, pilot credits (Claude Code)

**What:** Real `PLAYLIST_URL` set (derived clean playlist URL from user's watch link). Full playlist fetched in a background task: 211 playlist entries → **210 unique videos** (id `xenwRup_sC4` is in the playlist twice), 0 yt-dlp errors, `info.json` for all; `scripts/fetched.txt` = 210 ids. `pilot/` raws moved under `transcripts/<id>/` beforehand (fresh fetch overwrote them under identical names — no duplicates). Cleaned → **203 transcripts** in `transcripts_clean/`; 7 videos have no English track (flag `bez přepisu` in the taxonomy phase): 1xj3nPEmHPw, 67-W5lCSD_0, Hd0od7sQdds, TZ-lhSHQjPU, kfu4jKyazzU, uPwV7dgokOQ, xYGz-oGAGkk. All 8 credit placeholders in the 5 pilot chapters filled from `info.json` (Brainless. / Indie Game Clinic / Doppelganger Studios / Matt Aspland / Aziel Arts). `REPLACE_GITHUB_USERNAME` replaced in `mkdocs.yml` (remote exists: Martinsafka). mkdocs-material installed into project `.venv` (Homebrew Python is PEP-668 externally managed; `.venv/` gitignored). `mkdocs build --strict`: exit 0, 0 warnings; abbr tooltips verified in built HTML.
**Why:** Phase 0 — make the machinery around the pilot chapters run end-to-end.
**How:** Fetch ran in background with output to a log outside the repo (~5k lines; 151 transient 429/backoff mentions, yt-dlp retried through all — keep `--sleep-requests 1`). Playlist listing reconciled against `fetched.txt` (only diff: the duplicate id). Search note: lunr has no Czech stemmer, `search.lang cs` falls back to `en` (recorded in architecture.md). `transcripts/PL-…/` holds the playlist's own info.json — harmless, gitignored.
**Follow-ups:** User: commit & push, enable Pages (Settings → Pages → Source: GitHub Actions), then paste the live URL into `README.md`. Visual `mkdocs serve` eyeball folds into Phase 1 pilot review. Next phase after that: taxonomy (`processing_index.md` over all 210 videos).

### 2026-07-09 — Phase 0 part 1: .gitignore + Pages deploy workflow (Claude Code)

**What:** Created the two infra files referenced by docs but missing from the skeleton: `.gitignore` (AGENTS.md boundaries — `transcripts/`, `transcripts_clean/`, `inbox/*` keeping `.gitkeep`, `pilot/`, `site/`; plus `.idea/`, `.DS_Store`, `__pycache__/`) and `.github/workflows/deploy.yml`. Resolved the Pages-setup contradiction (KICKOFF said gh-deploy → `gh-pages` branch; roadmap said Source: GitHub Actions) in favor of the **native Pages artifact flow**; aligned `architecture.md` and `KICKOFF.md` task 6 accordingly.
**Why:** User decision: source pushes to `main` only, Actions deploy from it. Native flow keeps generated HTML out of the repo entirely (no `gh-pages` branch) and the CI `mkdocs build --strict` doubles as the broken-link gate on every push.
**How:** Two-job workflow — build (checkout → setup-python 3.x → `pip install mkdocs-material` → `mkdocs build --strict` → upload `site/` as Pages artifact) + deploy (`actions/deploy-pages@v4`, `github-pages` environment); triggers: push to `main` + `workflow_dispatch`. Ignore rules verified with `git check-ignore -v` and `git status` (boundary dirs out, `inbox/.gitkeep` still trackable).
**Follow-ups:** Rest of Phase 0: move `pilot/` raws under `transcripts/`, local `--strict` build + serve eyeball, set real `PLAYLIST_URL` (waiting on user) + fetch/clean, fill credit TODOs from `info.json`, replace `REPLACE_GITHUB_USERNAME` in `mkdocs.yml`, push + enable Pages (Source: GitHub Actions).

### 2026-07-09 — Project scaffold + pilot synthesis (chat-Claude session)

**What:** Full repo skeleton: agent doc set (`AGENTS.md` + 6 agent_docs following the author's Pixin philosophy), pipeline scripts (`fetch_transcripts.sh` incremental via `--download-archive`; `clean_transcripts.py` with rolling-window dedupe, entity/noise stripping, paragraph timestamps), MkDocs Material config (light palette, cs+en search, two-layer glossary via `abbr` + snippets `auto_append`), Pages deploy workflow, and **5 pilot videos synthesized** into chapters: teorie/ 2 chapters (mindset of starting; loops→chains), praxe/ 3 chapters (overlap-driven interaction; Mesh Terrain 5.8 deep dive; editor tips collection), plus seeded `rejstrik.md` (~20 terms) and `includes/abbreviations.md`.
**Why:** Kickoff — turn the 200+-video playlist into searchable Czech skripta; pilot validates the entry template before batch processing.
**How:** Analyzed the author's existing Pixin agent docs and mirrored their philosophy (lean AGENTS.md entry, progressive disclosure, non-negotiable invariants with refuse-and-explain, mandatory dev log, propose-don't-commit). Key structural decision: **ideas as the atomic unit, videos as cited sources** — drives searchability, pedagogy, and licensing safety at once. Licensing boundary hardened: `transcripts*/` + `inbox/` gitignored; published text is Czech synthesis with credits + timestamp deep links, never transcript reproduction. Track-selection heuristic added after pilot evidence: regional manual tracks (en-GB) beat auto captions substantially (the chains video: 1.9k clean words from manual vs ~9k raw auto cues). The 47-min Mesh Terrain video was split into multiple idea entries within one chapter rather than one mega-entry.
**Follow-ups:** Credit blocks in pilot chapters carry `TODO` placeholders — pilot zip predates `--write-info-json`, so channel names/URLs are pending; Phase 0 re-fetch fills them (see roadmap). YouTube 429'd both the author's fetch and web verification attempts during this session — `--sleep-requests 1` stays mandatory. `processing_index.md` deliberately deferred to the taxonomy phase.
