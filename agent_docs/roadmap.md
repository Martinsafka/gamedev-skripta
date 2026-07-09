# Roadmap — gamedev-skripta

## Goal

Turn a 200+-video study playlist and the author's project journals into a published, searchable Czech knowledge base (Teorie her · Praxe v UE5 · Zápisky · Rejstřík) on GitHub Pages — a textbook the author returns to when creative energy returns.

## Principles (don't break these)

- Licensing & anonymization invariants (`AGENTS.md`) override delivery speed.
- Ideas are the unit; videos are sources.
- Quality of explanation > coverage speed. Every phase ships a *usable* site.
- Each task follows `workflow.md`: analyze → propose → execute → log → commit-message → point to next.

## Working cadence

After finishing a phase chunk, the agent **proposes the next step** and **ticks checkboxes** here. Batch sizes for Phase 3: 10–25 videos per session grouped by theme, agreed with the user up front.

---

### ▶ NEXT UP — Phase 0: Scaffold verification _(first Claude Code session)_

- [x] Repo initialized from the delivered skeleton; `pilot/` raw files moved under `transcripts/` (gitignored), `.gitignore` created & verified against `AGENTS.md` boundaries.
- [x] mkdocs-material installed (project `.venv` — Homebrew Python is PEP-668 managed); `mkdocs build --strict` passes locally (0 warnings); tooltips verified in built HTML. Visual `mkdocs serve` eyeball folds into Phase 1 review.
- [x] `scripts/fetch_transcripts.sh`: real `PLAYLIST_URL` set; full playlist fetched (210 unique videos, 0 errors, all with `info.json`); `clean_transcripts.py` → 203 clean transcripts (7 videos lack an English track).
- [x] **`TODO` credit placeholders filled** in all 5 pilot chapters from `info.json` (channel names + URLs).
- [ ] GitHub Pages enabled (Settings → Pages → GitHub Actions); deploy workflow green; site live.
- [x] Dev log entry.

### Phase 1 — Pilot review _(user + chat-Claude)_

- [ ] User reviews the 5 pilot chapters against expectations (structure, tone, depth, timestamp usefulness).
- [ ] Template/conventions adjusted per feedback; changes land in `content_conventions.md`.

### Phase 2 — Taxonomy _(one heavy session)_

- [ ] Full playlist fetched (delta on top of pilot); cleaned.
- [ ] `agent_docs/processing_index.md` created: table of every video (id, title, channel, duration, track quality) with proposed document + chapter assignment.
- [ ] Chapter skeleton for both documents proposed and approved by user (nav structure in `mkdocs.yml`).

### Phase 3 — Batch synthesis _(the long haul)_

- [ ] Themed batches processed per the index; glossary grows with each batch; every batch = dev log entry + green `--strict` build.
- [ ] Processing index kept current (status column: `todo / drafted / published`).

### Phase 4 — Zápisky

- [ ] `inbox/` workflow exercised end-to-end: first devlog/summary distilled, anonymized, cross-linked.
- [ ] Standing cadence agreed (zápisky added as material arrives).

### Later / ideas

- [ ] Rejstřík-driven quiz export (terms + definitions as spaced-repetition source).
- [ ] Per-chapter "co si vyzkoušet" exercise blocks.
- [ ] Czech-video support check (`--sub-langs` extension) if the playlist gains Czech sources.
