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
- [x] **Batch 4B done** _(2026-07-10)_: GASP téma — 6 videí (2× Inside Unreal 181+154 min, zbraně/overlay, 2 bez přepisu kryté z kontextu série) → **1 kapitola `praxe/gasp.md` (8 myšlenek)**, rejstřík +13 termínů, zpětné odkazy z mm-zaklady/mm-systemy doplněny (5 míst), `--strict` + anchor-check green. **Téma „Motion Matching a GASP" kompletní (21/21).**
- [x] **Batch 5 done** _(2026-07-10)_: Pohyb postavy (locomotion) — 13 videí (1 bez přepisu kryto z popisu) → **3 kapitoly** (`pohyb-zaklady` 5 myšlenek, `parkour-vault` 2, `mover` 3), nové praxe téma v nav, rejstřík +5 termínů, zpětné odkazy gasp↔mover, `--strict` + anchor-check green. **Téma P-MOVE kompletní (13/13).**
- [x] **Batch 6 done** _(2026-07-10)_: AI a chování NPC — 9 videí → **3 kapitoly** (`ai-zaklady` 4 myšlenky, `ai-vnimani` 3, `state-trees` 3), rejstřík +8 termínů, editorial merge ai-patrola→ai-zaklady, cross-links gasp↔state-trees + game-feel→ai-zaklady (follow-up z batche 1 splněn), `--strict` + anchor-check green. **Téma P-AI-NPC kompletní (9/9).**
- [x] **Batch 7 done** _(2026-07-10)_: Herní systémy a interakce — 12 videí (2 bez přepisu kryta z popisů) → **3 kapitoly** (`footsteps` 4 myšlenky, `pasti-a-mechaniky` 4, `interakce-predmety` 2), rejstřík +8 termínů, editorial merges (herni-mechaniky+pasti, stealth-ukryty→interakce, Interactive World přeřazen k footsteps), `--strict` + anchor-check green. **Téma P-SYS kompletní (12/12).**
- [x] **Batch 8 done** _(2026-07-11)_: Fyzika: ragdoll, lana, simulace — 8 videí → **2 kapitoly** (`ragdoll` 4 myšlenky — syntéza 3 velkých průvodců, `lana-kabely` 3 vč. merge physics-control), rejstřík +6 termínů, cross-link ai-zaklady↔ragdoll, `--strict` + anchor-check green. **Téma P-PHYS kompletní (8/8); 107/210 published — přes polovinu playlistu.**
- [x] **Batch 9 done** _(2026-07-11)_: Voda — 10 videí → **3 kapitoly** (`voda-a-buoyancy` 3 myšlenky, `interaktivni-voda` 2, `nastroje-voda` 2 — Faucher framován jako produktové video s přenositelnými lekcemi), rejstřík +5 termínů, Pitchfork video rozděleno mezi 2 kapitoly, `--strict` + anchor-check green. **Téma P-WATER kompletní (10/10); 117/210 published.**
- [x] **Batch 10 done** _(2026-07-11)_: Animace: nástroje a mocap — 5 videí → **1 kapitola** `animace-nastroje.md` (3 myšlenky; merge 3 tenkých slugů), rejstřík +4 termíny, zpětný odkaz gasp↔Locomotor, `--strict` + anchor-check green. **Téma P-ANIMTOOLS kompletní (5/5); animační blok uzavřen; 122/210 published.**
- [x] **Batch 11 done** _(2026-07-11)_: Terén a krajina — 6 videí → **1 kapitola** `landscape-tipy.md` (4 myšlenky) + **rozšíření pilotní `mesh-terrain.md`** o myšlenku „Kanály v praxi" (Sensei komplementy + DK materiál/PCG; překryvy se stávající kapitolou vědomě zahozeny), rejstřík +2 termíny, `--strict` + anchor-check green. **Téma P-TERRAIN kompletní (7/7); 128/210 published.**
- [x] **Batch 12 done** _(2026-07-11)_: MetaHuman — 5 videí → **1 kapitola** `metahuman.md` (5 myšlenek; merge 4 slugů): hratelná postava s virtual bones, look-at přes post-process ABP, Chaos Cloth, Crowd plugin (Mass Entity), Metapipe framován jako placený nástroj s přenositelnými lekcemi. Rejstřík +5 termínů, `--strict` + anchor-check green (checker nově i same-page anchory). **Téma P-MH kompletní (5/5); 133/210 published.**
- [x] **Batch 13 done** _(2026-07-11)_: PCG a procedurální svět, **část A** — 5 videí (~21,7k slov) → **2 kapitoly** (`pcg-zaklady` 5 myšlenek: PCG Mode 5.7, paint pod kapotou, spacing+linear grammar, vlastní štětec se scatteringem, výřezy kolizemi + debug; `instanced-actors` 2 myšlenky: swap setup přes Data Registry, paměť/fyzika/dosahy), nové praxe téma v nav, rejstřík +6 termínů (vč. zpětného Bounds pro parkour-vault), `--strict` + anchor-check green (550 fragmentů). **P-PCG 5/19 — část A hotová.**
- [x] **Batch 14 done** _(2026-07-11)_: PCG část B — 13 videí (~26,7k slov, 1 bez přepisu kryto z popisu) → **3 kapitoly** (`pcg-vegetace` 6 myšlenek: Procedural Vegetation editor 5.7/5.8, les grafem, proxy kolize + wind CVar, mýtiny a cesty, Rbnks produkt; `pcg-liany` 2: povrchové liány s pathfindingem, visící řetězy; `pcg-hexagone` 2: hex mřížka aritmetikou, mizející dlaždice s eject trikem), rejstřík +2 termíny, obousměrný cross-link na ruční Hex-A-Gon v pastech, `--strict` + anchor-check green (595 fragmentů). **Téma P-PCG kompletní (19/19); 151/210 published.**
- [x] **Batch 15 done** _(2026-07-11)_: Prostředí a environment art — 10 videí (~36,8k slov vč. 132min Forest Path) → **2 kapitoly** (`env-breakdowny` 5 myšlenek: San Francisco 1:1, The Ascent, TLOU trim sheety, RE Requiem vrstvy, Crimson Desert detektivka; `env-tvorba` 5 myšlenek: chiaroscuro, lesní pěšina I+II, temný les, zvuk+listí), nové praxe téma v nav, rejstřík +6 termínů (Draw call, Environmental storytelling, POM ×2, Silueta, Trim sheet), obousměrný link RE Requiem ↔ levely-a-streaming, `--strict` + anchor-check green (635 fragmentů). **Téma P-ENV kompletní (11/11 vč. skip); 161/210 published.**
- [x] **Batch 16 done** _(2026-07-11)_: Materiály a VFX + Osvětlení a atmosféra — 12 videí (~34,6k slov vč. 85min decay) → **2 kapitoly ve 2 nových tématech** (`materialy` 5 myšlenek: master material, Nanite displacement, decay systém I+II, toon shading 5.8; `osvetleni` 5 myšlenek: PBL workflow, SH2 mlha, horor ve vrstvách, noční scéna, drobky), rejstřík +6 termínů, slug merge 10→2 v indexu, cross-link do teorie (percepční hranice ↔ SH2 mlha), `--strict` + anchor-check green (681 fragmentů). **P-MAT i P-LIGHT kompletní (6/6 + 6/6); 173/210 published — vizuální blok uzavřen.**
- [x] **Batch 17 done** _(2026-07-11)_: Rendering a optimalizace — 7 videí (~27,8k slov) → **2 kapitoly v novém tématu** (`optimalizace` 5 myšlenek: levely/draw cally → data layers, Nanite vs. LODy, voxelizace, foliage I+II; `textury-a-dlss` 3 myšlenky: right-size, unikátní/atlas/VT, DLSS 4.5 s mip bias kompenzací), rejstřík +6 termínů, slug merge 5→2, cross-link right-size ↔ Crimson Desert (video cituje náš zdroj), `--strict` + anchor-check green (723 fragmentů). **Téma P-PERF kompletní (7/7); 180/210 published.**
- [x] **Batch 18 done** _(2026-07-11)_: Editor a workflow — 8 videí (1× 9min rady + 7 shortů, ~2,6k slov) → **rozšíření pilotní `editor-tipy` o 4 myšlenky** (jak se učit engine — tutorial hell, dokončování, Print String; výběry a navigace; pivot bez Blenderu + rozmístění fyzikou; Shift+Delete + editor lag), rejstřík +2 termíny (Pivot, Tutorial hell), mosty do Teorie (zacatky/co-se-ucit/scope), `--strict` + anchor-check green (733 fragmentů). 98min kurz zůstává low-priority todo. **P-EDITOR hotové (9 published + 1 lp + 2 skip); 188/210 published.**
- [x] **Batch 19 done — FINÁLE PHASE 3** _(2026-07-11)_: AI nástroje ve vývoji — 14 videí (~42,4k slov) → **2 kapitoly v novém tématu** (`claude-code-ue` 6 myšlenek: nativní MCP 5.8, komunitní cesta + endless runner lekce, agent v Blenderu/ComfyUI, 72h hra jako mapa dělby člověk–AI, Blueprint AI produkt, Convai NPC grounding; `ai-assety` 6 myšlenek: free pipeline, Tripo/Hunyuan/Rodin ceny, hratelná postava tandem, modulární postava + AccuRig, AI→MetaHuman 5.8 s DNA/UDIM triky, Kimodo + PixelLab), rejstřík +3 termíny (MCP, PBR, Retopologie), product framing všude (Rodin sponzor přiznán), `--strict` + anchor-check green (773 fragmentů). **P-AITOOLS kompletní (14/14); 202/210 published.**

### ✅ Phase 3: Batch synthesis — HOTOVO _(2026-07-09 až 2026-07-11)_

**19 batchů, 202/210 videí published** (~30 kapitol Praxe + 22 Teorie, rejstřík ~200 termínů). Mimo scope zůstávají: 2 low-priority beginner kurzy (`dB-pS8PHALY`, `0yBSEiMldo0` — rozhodnutí Phase 2), 1 CS video (čeká na cs-subtitle pipeline, viz Later), 5 skipů (news/promo).

### ✅ Phase 4 — Zápisky _(done 2026-07-11)_

- [x] `inbox/` workflow exercised end-to-end _(2026-07-11)_: **vlna 1 = 5 zápisků** z prvních 7 podkladů (selhávat citelně a čitelně; karta selhání: packaging; dokumentace jako audit; derivační řetěz IZBY; lom, ne hřbitov) — anonymizované, cross-linkované oběma směry (mm-zaklady, napad, zacatky-bez-zkusenosti), `--strict` + anchor-check green (782 fragmentů).
- [x] **Vlna 2 done** _(2026-07-11)_: 7 podkladů → **7 zápisků** (`devlog-jako-mapa`, `pravidlo-70-30`, `gdd-review`, `cut-line`, `audit-vlastniho-tonu`, `kvizovy-protokol`, `oblouk-formou`), rejstřík +2 termíny (Dogfooding; One-way door — druhý výskyt dle plánu z vlny 1), cross-linky oběma směry do 8 kapitol (mm-zaklady, mm-systemy, gasp, claude-code-ue, editor-tipy, prototypovani, smycky-a-retezce, pribeh-a-postavy) i mezi zápisky, `--strict` + anchor-check green (802 fragmentů). **Inbox fronta prázdná — všech 14 podkladů zpracováno.**
- [x] Standing cadence **potvrzena uživatelem** _(2026-07-11)_: nový inbox soubor → zápisek v nejbližším sezení; vlna = max ~5 zápisků kvůli kvalitě. Platí průběžně i po uzavření fáze.

### ▶ Phase 5 — Concept Audit Skill _(běží od 2026-07-11)_

Plán: `agent_docs/concept_audit_skill.md` — aktivační podmínky splněny vlnou 2 zápisků (knihovna + auditní struktury publikovány). **Mechanic Mentor** (`agent_docs/mechanic_mentor_skill.md`) je druhý v pořadí a čeká na složenou kalibraci audit skillu. Schválený přístup (2026-07-11): generovaný chapter-map + regenerační skript; SKILL.md anglicky, šablony česky, dialog zrcadlí uživatele; slash i auto-trigger; v0 čistě pro Claude Code.

- [x] Krok 0 _(2026-07-11)_: slug/anchor invariant v `architecture.md` (escape hatch: `attr_list` `{#stary-anchor}`) · issue template `.github/ISSUE_TEMPLATE/library-gap.md` · Phase 5 v roadmapě.
- [x] Krok 1 _(2026-07-11)_: v0 skillu v `.claude/skills/concept-audit/` — SKILL.md (EN, auto-trigger description CZ+EN) + 3 šablony CZ (intake, design-rationale, pillars) + `references/chapter-map.md` (266 odkazů, generovaný) + `scripts/build_chapter_map.py` (validuje anchory proti buildu).
- [x] Krok 2 _(2026-07-11)_: kalibrace na 3 případech (IZBA-GDD / adventura-živý / přerostlý koncept) s **předregistrovanými kritérii** — vše prošlo; 1 zachycený vzor (měkký výrok o autorovi) → pravidlo 5 v SKILL.md zpřísněno. Kontaminace přiznána — jen kalibrační evidence, ne důkaz.
- [x] **Společná kalibrace na reálném dokumentu** _(2026-07-11)_: uživatel vložil skutečné GDD v2.0 přes `/concept-audit` (audit nastudeno, výhradně z textu) — **verdikt uživatele: prošel** (potvrzeny známé nálezy + nové reálné: herní doba natahovaná smrtmi, third-person vs. first-person reference, detekční pásmo 100–300, panenka na dvou místech). Dva zásahy z běhu do SKILL.md: intake gate zpřesněn (plný GDD bez derivace nestopuje — derivace je nález), přidána sekce „Saving the audit" (nabídka uložení výstupu do souboru). Výstup: `inbox/concept-audit-izba-gdd-2026-07-11.md` (gitignored).
- [x] **Kalibrační trojice na reálných dokumentech dokončena** _(2026-07-12)_: Obscura (GDD v1.0 + sprint plán + marketingová koláž) a Evan Lowe (bible série 1) přes `/concept-audit` nastudeno — **verdikt uživatele: oba prošly** („pokládá správné otázky… všechny tři audity trochu bolí — nachytal jsem se na ‚to se přeci domyslí'; co není zapsané, není rozhodnuté a nepředává se dál"). Nová konvence: výstupy do gitignored `audits/` (uživatel založil, IZBA audit přesunul; SKILL.md „Saving the audit" aktualizován inbox→audits). Druhá úprava: intake formulář se nově nabízí i jako soubor k vyplnění. Kumulativní library-gaps signál: detektivní mechaniky 3×, serializované vyprávění 2×, tuning/balanc 2×, + citlivá témata/rating, lokalizace hlasu.
- [x] **Krok 3: held-out testy HOTOVO** _(2026-07-12, Opus 4.8)_: tři syrové dokumenty přes `/concept-audit` (KYRRÖ nekompletní nástřel; The Seeker Mount Stupid + právní/platformní catch; Race'n'Chase reálný DMA doc 1995 → GTA — silná místa uznána, nic nevymyšleno, rozpor racing-vs-sandbox). **Verdikt uživatele: prošlo.** Tři opravy do skillů (čeština „proč na tom záleží"; otázka nese vlastní routing; viditelné URL místo `[label](url)` — poslední i v mechanic-mentoru). Přenositelnost mezi modely potvrzena. Detaily v dev_logu.
- [ ] Krok 4: balení jako plugin (`.claude-plugin/marketplace.json`, repo = vlastní marketplace) — **delegováno na Opus 4.8**, přesný postup a ověřené formáty v `agent_docs/skill_validation_and_packaging.md`. Až po úspěšných validacích.

### ▶ Phase 6 — Mechanic Mentor Skill _(v0 postaveno 2026-07-12; validace delegována)_

Plán: `agent_docs/mechanic_mentor_skill.md`. Aktivační podmínky splněny (audit kalibrací prošel; praxe kryje locomotion/interakce/AI; library-gaps signál běží). Předsunuto před held-out testy auditu — vědomé rozhodnutí uživatele z token constraints; zároveň test strategie „Fable 5 píše skilly, nižší modely je provozují".

- [x] **v0 postaveno** _(2026-07-12)_: `.claude/skills/mechanic-mentor/` — SKILL.md (8 hard rules vč. human-write/agent-read, smyčka 0–9, session devlog s počítadly, exit gate counterfactuals, seams-over-ceremony bez pattern banů), šablony CZ (mechanic-intake, session-devlog s Intent sekcí), `references/review-queries.md` (10 standardních read-only dotazů s routingem — mrtvé dráty, write-only, ne-defaultní write-path, cross-boundary casty, tagy, prahy v datech, jeden datový kontrakt, tick polling, interface úplnost, pose-matched vstupy), chapter-map sdílená s auditem (generátor přepnut na dvojí výstup). Otevřené otázky briefu rozhodnuty: standalone intake přijímán (pipeline doporučena), review = standardní sada + 2–4 dotazy odvozené z intentu, understanding log NE (Follow-ups v devlogu stačí — scope creep), jeden plugin se dvěma skilly (doporučení pro krok balení).
- [x] **Lehká kalibrace** _(2026-07-12)_: sonda „schovat se pod postel" (kroky 0–3) proti předregistrovaným kritériím — 6/6 (principy s odkazy; fáze/hranice/mechanism-vs-policy formou otázek; nula autorování; review-queries kryjí 5 švů z pravidlo-70-30). Kontaminace přiznána — plná validace na Opus 4.8 s reálnou mechanikou.
- [ ] Validace pod Opus 4.8 (reálná mechanika, uživatel soudce) — protokol v `agent_docs/skill_validation_and_packaging.md`.
- [ ] Po validaci: společné balení s concept-audit (Phase 5 krok 4).

### Later / ideas _(vědomě odloženo — todo, neřešíme teď)_

- [ ] Rejstřík-driven quiz export (terms + definitions as spaced-repetition source). _(Odloženo uživatelem 2026-07-11.)_
- [ ] Czech-video support (`--sub-langs` extension) + CS mytologie video (`kfu4jKyazzU`). _(Odloženo uživatelem 2026-07-11.)_
- [ ] 2 low-priority beginner kurzy (`dB-pS8PHALY`, `0yBSEiMldo0`) — zůstávají todo, rozhodnutí Phase 2 trvá.

### Nerozhodnuto _(záměrně na konci — vrátit se, až bude jasno)_

- [ ] Per-chapter „co si vyzkoušet" exercise blocks — zatím nevíme, jak se k tomu postavit (jednorázový průchod ~50 kapitolami vs. postupně při otevření kapitoly). _(Přesunuto na konec 2026-07-11.)_
