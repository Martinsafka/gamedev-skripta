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

### 2026-07-09 — Phase 3 batch 2: Teorie dokončení — level design + marketing + mytologie (Claude Code)

**What:** 11 videos → **9 new teorie chapters**: T-LEVEL — `vedeni-hrace` (scripted events + recall priming), `prostor-a-hranice` (cave blockout + map boundaries); T-MARKET — `co-prodava` (Tyroller: experience > hook, 4 pilíře, 7 strategií), `steam-stranka` (BiteMe checklist ve 3 vrstvách), `prvni-dojem`, `devlogy`; T-MYTH — `slovanska-monstra` (bestiář, 11 bytostí), `slovanske-ritualy` (masopust East/South/West), `slovansky-folklor` (Vasilisa — anatomie pohádky). Rejstřík +15 terms (affordance, blockout, capsule, cold open, recall priming, trigger volume, soft boundary…), tooltips now 67 lines. Nav +3 témata; processing index 11 rows → published (32 total); „budoucí téma/kapitola" placeholdery z batche 1 nahrazeny reálnými odkazy (proc-tvorit, pribeh-a-postavy, smycky-a-retezce). `--strict` + anchor-check green. **Teorie document complete** (zbývá 1 CS video na cs-titulky, 1 skip).

**Why:** Phase 3 batch 2 per roadmap; user go-ahead.

**How:** Dvě editorial merges: 4 drobná level-design videa (766–1083 slov) → 2 kapitoly po 2 myšlenkách, párované funkčně (vedení v čase × práce s prostorem) — samostatné kapitoly by byly příliš tenké; index ukazuje na sdílené soubory. T-MYTH psáno jako rešerše settingu: standardní šablona entry, ale s „designovýma očima" (bytosti jako stavové automaty s pravidly; rituály jako dramaturgie festivalu; pohádkový útěk jako reciprocity mechanika). Auto-titulky slovanská jména masakrují („Lei"→lešij, „Kashet"→Kostěj, „Pudnit"→polednice, „Zmegarinich"→Zmej Gorynyč…) — opraveno z kontextu, v kapitole na to upozorněno. **Rozhodnutí: T-MYTH nepřidává rejstříkové termíny** — rejstřík je craft terminologie (EN termín + CZ výklad); mytologické bytosti by ho ředily a bestiář kapitola sama je doménová reference. Nav klíč s dvojtečkou („Rešerše: slovanská mytologie") vyžaduje quotovaný YAML klíč.

**Follow-ups:** Batch 3 = první Praxe batch; navrženy dvě varianty (Blueprint architektura — foundational, vs. Motion Matching/GASP — autorovo těžiště, 2 videa bez přepisu pokryjí se z kontextu série). U MM/GASP batche počítat s delšími transkripty (2× Inside Unreal, 150+ min). CS video mytologie stále čeká na cs-subtitle rozšíření fetch pipeline (Later item v roadmapě).

### 2026-07-09 — Phase 3 batch 1: Teorie — mindset + nápad/scope + základy designu (Claude Code)

**What:** 16 videos synthesized into **13 new teorie chapters** (~15k words of Czech): T-MIND — `proc-tvorit`, `jak-zacit`, `co-se-ucit`, `produktivita`, `rady-z-praxe`, `postmortem-shantytown`; T-SCOPE — `napad` (2 videos), `scope` (2 videos), `prototypovani`; T-DESIGN — `zaklady`, `zabava`, `game-feel` (2 videos merged), `pribeh-a-postavy`. Rejstřík +27 terms in both layers (tooltips now 52 lines); `mkdocs.yml` nav grouped into the 3 témata; `teorie/index.md` rewritten; processing index: 16 rows → `published` (stats: 21 published), pilot chapters gained back-links to new chapters. `mkdocs build --strict` green; all internal anchor fragments additionally validated by a slugify-checker script (0 errors — strict doesn't check anchors).

**Why:** Phase 3 batch 1 per roadmap; user go-ahead „pokračuj batchem 1".

**How:** Chapter map = approved index slugs, with one editorial deviation: `combat-feel` + `game-feel` (two ~2k-word devlogs about the same idea — „pocit ze hry") merged into one chapter with two entries; separate files would have been too thin. Timestamp workflow worth keeping: paragraph markers in clean transcripts give the neighborhood, then grep the raw SRT for the exact cue second of each key phrase — precise deep links at ~1 bash call per chapter. The listicle video (7 Time Wastes) was reorganized by failure *mechanism* into 4 entries rather than mirroring its 1–7 list (licensing rule). Entries synthesizing two sources carry both credit blocks. Auto-caption garbles fixed from context (Chants of Sennaar, Raph Koster, Csíkszentmihályi, Fields of Mistria, Megabonk…); one game name ("Moonsh…") was unverifiable → described generically instead of guessing. Tooltip terms kept Capitalized per existing convention — Czech inflection limits tooltip hits regardless; the rejstřík page is the primary layer.

**Follow-ups:** Batch 2 proposed in roadmap: finish Teorie — Level design (4) + Vydání a marketing (4) + Rešerše mytologie (3 EN; the CS video waits on the cs-subtitle pipeline extension, a Later item). Two low-priority beginner-course videos stay `todo`. When the praxe „AI a chování NPC" batch lands, cross-link it from `game-feel.md` (context steering).

### 2026-07-09 — Phase 2 closed: téma tree approved (Claude Code)

**What:** User approved the téma tree as proposed (6+17 témat), the mythology-as-Rešerše decision, and the skip/low-priority flags (5 news/promo → `skip`, 2 beginner courses stay `todo` low-priority). Index updated accordingly; Phase 2 ticked off; Phase 3 batch 1 agreed: **Teorie — mindset + scope + design (~17 todo videos)**.
**Why:** Approval gate before batch synthesis, per roadmap.
**How:** Decisions captured via structured questions; index edits mechanical (`skip?` → `skip`, header note). Bez-přepisu handling: Czech mythology video waits for cs-subtitle pipeline extension (Later item); 2 GASP cover-shooter parts will be covered from series context during the MM/GASP batch; rest decided per-topic.

### 2026-07-09 — Phase 2: taxonomy — processing index + téma tree proposal (Claude Code)

**What:** Classified all 210 videos and generated `agent_docs/processing_index.md` (status, video+link, channel, duration, track, word count, téma, chapter slug, notes; grouped by document → téma). Proposed téma tree: Teorie 6 topics / 31 videos, Praxe 17 topics / 179 videos (counts in the index header).
**Why:** Phase 2 deliverable — the map that batch synthesis (Phase 3) will follow; user approves the tree before any batch starts.
**How:** Metadata extracted from `info.json` into a TSV; classification from titles/channels with transcript peeks for 4 ambiguous videos (RE9 video = wall-stop locomotion tweak; „10X immersive" = game-feel devlog → teorie). Assignments authored as a compact TSV (id → téma/slug/note) and joined by a generator script — the index is regenerable. Notable clusters: Motion Matching/GASP is the biggest praxe topic (21, matches the author's locomotion work); a 4-video **Slavic mythology** cluster (game-setting research, not gamedev craft) got a provisional téma „Rešerše: slovanská mytologie" under Teorie — flagged for user decision. Flagged 7 videos as skip?/low-priority (news/promo/beginner courses). 7 videos bez přepisu noted (1 is Czech — cs-subtitle fetch is a Later roadmap item).
**Follow-ups:** User to approve/adjust the tree + decide: mythology section, skip-flagged videos, handling of bez-přepisu videos. After approval: tick the roadmap box, then plan Phase 3 batch #1 (proposal: „Teorie kompletní" or „Motion Matching a GASP" first).

### 2026-07-09 — Phase 1: pilot review → collapsible topic navigation (Claude Code)

**What:** User verdict on the pilot: content approved; concern that a flat chapter list becomes unreadable at 200+ videos. Implemented a collapsible nav tree **document → téma → kapitola**: `mkdocs.yml` features swap (`navigation.sections` → `navigation.indexes`), nav restructured with provisional topic groups (Teorie: „Tvůrčí proces a mindset", „Základy designu"; Praxe: „Blueprint vzory", „Terén a svět", „Editor a workflow"), document index pages regrouped by topic. Content model in `architecture.md` gains the `téma` level.
**Why:** Findability at scale — the core concern before batch synthesis starts.
**How:** Key decision: **topics exist only in `mkdocs.yml` nav; chapter files stay flat** in their document folder. Re-assigning a chapter to another téma is a nav-only change — no file moves, no broken relative links (matters for rejstřík anchors and cross-chapter links). Verified in built HTML: document titles link to their index pages inside nested collapsible items; `--strict` green. Pilot topics are provisional — the real téma tree is the Phase 2 taxonomy deliverable, approved by the user.
**Follow-ups:** `inbox/` material is currently unstructured (distilled Claude-conversation threads); future devlogs will arrive pre-sorted per project.

### 2026-07-09 — Phase 0 complete: site live (Claude Code)

**What:** User pushed, enabled Pages (Source: GitHub Actions), workflow green, site live. Live URL added to `README.md`; last Phase 0 checkbox ticked; roadmap ▶ NEXT UP moved to Phase 1 (pilot review).
**Why:** Closes Phase 0 — the whole scaffold now runs end-to-end, from fetch to published site.
**How:** Trivial edits only. Reminded the user that raw personal material for Zápisky belongs in `inbox/` (gitignored — never pushed).

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
