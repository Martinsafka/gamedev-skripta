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

### ✅ Phase 0: Scaffold verification _(done 2026-07-09)_

- [x] Repo initialized from the delivered skeleton; `pilot/` raw files moved under `transcripts/` (gitignored), `.gitignore` created & verified against `AGENTS.md` boundaries.
- [x] mkdocs-material installed (project `.venv` — Homebrew Python is PEP-668 managed); `mkdocs build --strict` passes locally (0 warnings); tooltips verified in built HTML. Visual `mkdocs serve` eyeball folds into Phase 1 review.
- [x] `scripts/fetch_transcripts.sh`: real `PLAYLIST_URL` set; full playlist fetched (210 unique videos, 0 errors, all with `info.json`); `clean_transcripts.py` → 203 clean transcripts (7 videos lack an English track).
- [x] **`TODO` credit placeholders filled** in all 5 pilot chapters from `info.json` (channel names + URLs).
- [x] GitHub Pages enabled (Settings → Pages → GitHub Actions); deploy workflow green; site live: https://martinsafka.github.io/gamedev-skripta/
- [x] Dev log entry.

### ✅ Phase 1: Pilot review _(done 2026-07-09)_

- [x] User reviews the 5 pilot chapters against expectations (structure, tone, depth, timestamp usefulness). Verdict: content approved; concern raised that a flat chapter list won't scale to 200+ videos.
- [x] Structure adjusted per feedback: collapsible navigation tree (document → téma → kapitola) via `navigation.indexes`; convention recorded in `architecture.md` (chapters stay flat on disk, topic grouping lives only in nav). Pilot topics provisional until taxonomy.

### ✅ Phase 2: Taxonomy _(done 2026-07-09)_

- [x] Full playlist fetched (210 unique videos; done in Phase 0) and cleaned (203 transcripts; 7 videos lack an English track).
- [x] `agent_docs/processing_index.md` created: table of every video (id, title, channel, duration, track quality) with proposed document + téma + chapter-slug assignment.
- [x] Chapter skeleton (téma tree) proposed and **approved by user 2026-07-09**: Teorie 6 témat (incl. „Rešerše: slovanská mytologie") / Praxe 17 témat; 5 news/promo videos → skip, 2 beginner courses → low priority.

### ▶ NEXT UP — Phase 3: Batch synthesis _(the long haul)_

- [ ] Themed batches processed per the index; glossary grows with each batch; every batch = dev log entry + green `--strict` build.
- [ ] Processing index kept current (status column: `todo / drafted / published`).
- [x] **Batch 1 done** _(2026-07-09)_: Teorie — Tvůrčí proces a mindset + Nápad, scope a plánování + Základy designu. 16 videos → **13 new chapters**, rejstřík +27 terms, `--strict` green. Editorial merge: combat-feel + game-feel → one chapter (`game-feel.md`).
- [x] **Batch 2 done** _(2026-07-09)_: Teorie dokončení — Level design + Vydání a marketing + Rešerše: slovanská mytologie. 11 videos → **9 new chapters**, rejstřík +15 terms, `--strict` green. Editorial merges: 4 level-design videa → 2 kapitoly (vedeni-hrace, prostor-a-hranice). **Teorie document is now complete** except: 1 CS video (čeká na cs-subtitle pipeline), 1 skip (news). T-MYTH adds no glossary terms (rejstřík = craft terminology; bestiář chapter is the domain reference).
- [x] **Batch 3 done** _(2026-07-09)_: Praxe — Blueprint architektura a organizace projektu. 12 videos → **7 new chapters**, rejstřík +19 terms, praxe nav restructured to approved taxonomy (pilot chapters re-homed), `--strict` green. Low-priority 76min beginner course (`dB-pS8PHALY`) stays todo.
- [x] **Batch 4A done** _(2026-07-10)_: Motion Matching část — mm-zaklady (8 videí → 1 kapitola, 4 myšlenky) + mm-systemy (7 videí → 1 kapitola, 3 myšlenky). Rejstřík +13 MM terms, praxe nav +téma „Motion Matching a GASP", `--strict` green. Batch rozdělen na dvě sezení na žádost uživatele.
- [ ] **Batch 4B next:** GASP téma — 4 videa s přepisem (vč. 2× Inside Unreal, 181 + 154 min, ~57k slov) + 2 bez přepisu (cover shooter série — dokrýt z kontextu). → `praxe/gasp.md`; poté doplnit odkazy na gasp.md z mm-zaklady/mm-systemy (teď jen plain-text zmínky).

### Phase 4 — Zápisky

- [ ] `inbox/` workflow exercised end-to-end: first devlog/summary distilled, anonymized, cross-linked.
- [ ] Standing cadence agreed (zápisky added as material arrives).

### Later / ideas

- [ ] Rejstřík-driven quiz export (terms + definitions as spaced-repetition source).
- [ ] Per-chapter "co si vyzkoušet" exercise blocks.
- [ ] Czech-video support check (`--sub-langs` extension) if the playlist gains Czech sources.
