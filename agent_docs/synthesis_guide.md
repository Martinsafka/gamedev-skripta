# Synthesis Guide — how to turn a transcript into a chapter that teaches

Companion to `content_conventions.md`. That doc defines the **format** (template, credits, language, licensing); this one defines the **thinking** — how deep an entry must go, where its context comes from, and how it connects to the rest of the site. Written after batches 20–24 (Fable 5) so that any capable model (Opus 4.8 and later) can run future batches at the same depth.

Read this whole doc once before your first batch; afterwards the two checklists at the bottom are enough.

---

## 1. The bar: a chapter teaches, it does not report

The deliverable is **the author's own textbook**, built from evidence found in videos. The difference in one line:

- *Reporting:* „video říká, že přechody jsou důležité."
- *Teaching:* „přechod je místo, kde se rozhoduje, jestli posloucháš skladbu, nebo loopy nalepené za sebou — a proto se po každé sekci hraje transition check."

Test every entry with the reader's question: **„Co teď udělám jinak?"** If the entry doesn't change what the reader would do or how they model the domain, it isn't finished. The video is a *source of evidence* (claims, numbers, examples, demonstrations), never an *outline to follow* — reorganizing by our own logic is both the licensing rule and the quality rule; they are the same rule.

## 2. Before writing: three questions per entry

Answer these in your notes **before** drafting; each answer has a designated landing place in the entry:

1. **Jaký problém čtenáře tahle myšlenka řeší?** → becomes the framing sentence of the Shrnutí or the first line of the Rozpad. Every tool in a video exists because something breaks without it. Name the break. (Two-loop rule exists because „přidávání nástrojů do loopu ≠ postup" a „loopy za sebou ≠ píseň" — the video literally opens with this failure; an entry that skips it presents a solution to an unstated problem.)
2. **Kde to stojí v pipeline vývoje / v mapě domény?** → one orienting clause somewhere in the entry („tohle je krok mezi X a Y", „tohle je nástroj pro fázi Z"). The reader is a self-taught developer assembling a mental map; every idea needs coordinates, not just content.
3. **Čeho z existujících kapitol se to dotýká?** → Souvislosti + Pozn. Grep the actual site before answering (`grep -rn "klíčové slovo" docs/`), don't rely on memory. If the answer is „ničeho", you searched wrong — after 100+ chapters there is always a neighbor.

## 3. Anatomy of a Rozpad: four layers

A Rozpad that teaches covers four layers. Not as headings — woven into prose — but all four must be present:

| Layer | Question it answers | Typical failure when missing |
|---|---|---|
| **Mechanismus** | Jak přesně to funguje? (kroky, čísla, podmínky) | entry je názor, ne nástroj |
| **Kontext problému** | Proč to existuje? Co se bez toho rozbije? Proč lidi selhávají právě tady? | entry je trivia — čtenář neví, kdy sáhnout po nástroji |
| **Důkazy** | Které hry / čísla / případy to dokládají? (vždy s timestampem) | entry je tvrzení bez váhy; nedá se ověřit ani dohledat |
| **Hranice a důsledky** | Kdy to neplatí? Co z toho plyne pro čtenářovu praxi? | čtenář aplikuje pravidlo i tam, kde škodí |

Rules of thumb that survived five batches:

- **Rozpad under ~150 words is a red flag**: either the idea is too thin to be its own entry (merge it), or you left the video's depth on the table (dig). See the case study below for the second failure.
- **Every decision shown in a video has a reason — the reason is the synthesis.** „Autor použil rim shot místo clapu" is trivia. „Rim shot místo clapu, *protože clap by rozbil tlumený charakter akordů a vokálů — textura nové vrstvy musí sloužit vibu, ne bojovat s ním*" is a principle the reader can reuse. When your draft states a *what* without a *why*, go back to the transcript; the why is almost always there, said casually in half a sentence.
- **Numbers beat adjectives.** „4–8 měsíců", „2 změny na 2 loopy", „10–20 testerů", „70–100 $ denně" — keep every number the video commits to, with its timestamp. Where the video is vague, stay vague honestly („řádově", „několik") — never invent precision.
- **The Shrnutí formula:** teze + mechanismus + háček (the surprising or counterintuitive part). 2–4 sentences, self-sufficient. It is *not* a table of contents („podíváme se na tři vlny a metodu RITE" je obsah, ne shrnutí).

## 4. The most common failure: retelling instead of unpacking

Symptoms, in decreasing order of visibility:

1. The Rozpad **restates the Shrnutí** with more words but no new information.
2. Paragraph order **mirrors the video's order** (also a licensing violation — reorganize by concept).
3. Decisions appear **without reasons** („přidal drumy", „použil top loop") — the *why* was in the video and got dropped.
4. **No tension**: nothing in the entry says when the advice breaks, what it competes with, or what it costs. Real tools have edges.
5. **Timestamps only at paragraph starts** (3–4 per entry) instead of at every claim worth jumping to (8–15 for a 20min+ video).

### Case study: the same video, thin vs. dense

Video `ZkRds6iTfhQ` (Alex Rome, two-loop rule, ~13 min) was synthesized into two entries in `docs/hudba/aranz.md`. The first entry (pravidlo dvou loopů) is solid. The second („Píseň žije v přechodu") is the thin pattern: its Rozpad has three short paragraphs, two of which re-say the Shrnutí. Compare with what the transcript actually offers — all of this was available and none of it landed:

- **Bass odvozená z akordů** [(3:22)](https://www.youtube.com/watch?v=ZkRds6iTfhQ&t=202s): stáhni akordy na MIDI stopu, smaž vrchní noty, spodní noty = basová linka — a pak **zdvojnásob rytmus, aby basa kopírovala rytmus akordů** („keep our rhythms cohesive", 4:24). Celá technika s přenositelným principem (nové vrstvy dědí rytmickou DNA těch starých) — v entry chybí.
- **Test vypršení** [(3:22)](https://www.youtube.com/watch?v=ZkRds6iTfhQ&t=202s), (6:19): u každé vrstvy se autor ptá „nevypršela ještě?" („I just feel like they're not expired yet") — to je *rozhodovací heuristika*, kterou pravidlo dvou loopů potřebuje, aby nebylo mechanické. Bez ní čtenář neví, *co* měnit.
- **Textura slouží vibu** (7:09): rim shot místo clapu, protože clap by rozbil deep vibe akordů a vokálů; top loop „přidává mushiness, slepí drumy dohromady" (7:56). Dvě konkrétní rozhodnutí s důvody = princip volby textury.
- **Counter-melodie jako odpověď** (8:30–8:48): „relaxed, not too aggressive… a nice response" — call-and-response koncept, pojmenovaný mimochodem.
- **Expression konkrétně** (10:10–11:30): vrstva akordů o oktávu výš **s jiným zvukem** („to get some variety") + otevření filter cutoff. Entry říká „přidat výraz" abstraktně; video ukazuje, co to fyzicky znamená.
- **Rozpočet tahů / pacing** (8:30): „I can open them up and let them shine, but I don't think the song's there yet. We can probably do that over here" — šetření silných tahů na pozdější sekce. To je aranžérská verze pacingu a entry o přechodech je přesně místo, kam patřila.
- **Transition check jako rituál** (5:41, 9:13, 12:02): po *každé* sekci se přehraje přechod a soudí se jediné kritérium — je změna uspokojivá? Entry kritérium zmiňuje, rituál (opakovaná brána po každé sekci) už ne.
- **„Never gets easier"** (7:56): autor po letech přiznává, že u „co dál?" si nikdy není jistý — a přesně proto si vyrábí mechanická pravidla. To je *hlubší teze celého videa* (pravidla jako mosty přes trvalou nejistotu) a spojka na teorie/tvurci-zasek.md — nevyužitá.

The fix is not „write more" — it is **mine the reasons and the rituals, not just the rules**. A dense rewrite of that entry would be maybe 60 % longer but 3× more useful: the reader would leave with a decision heuristic (test vypršení), a texture principle, a pacing principle, and a repeatable gate (transition check) instead of one slogan.

## 5. Context the video lacks: our added value

Each batch should add connective tissue the source cannot have:

- **Mapping onto the reader's stack**: UE ekvivalenty (dispatcher = observer, movement mode = strategy), DAW-agnostic formulations for music, engine-agnostic for design.
- **Cross-framework bridges**: when two sources describe the same shape, say so and link both („skills audit je měkčí sourozenec řemeslnických otázek z rozpočtu pozornosti"). When they *conflict*, stage the conflict honestly in a Pozn. („BiteMe říká prototyp nemá být šedý; IGC říká má — jsou to dva různé testy…").
- **Naming the pattern**: videos often demonstrate a principle without naming it (call-and-response, expiry test). Naming it — in Czech body text with English terminology — is legitimate synthesis, not invention. Do not, however, put invented names in the creator's mouth: „autor to nenazývá, ale předvádí…" when it matters.
- Mark what is ours: interpretive leaps, UE mappings, and disagreements live in **Pozn.** blocks (author-voice), not in the evidence layer.

## 6. Connections: Souvislosti and Pozn. discipline

- **Grep before you link.** Anchors are computed from full headers: `grep -n '^## ' docs/teorie/<file>.md`, then slugify mentally (lowercase, diacritics stripped, punctuation dropped, spaces → hyphens). Guessing anchors was the #1 source of broken links in early batches.
- **Link to the specific entry (anchor), not just the chapter**, whenever the relationship is with one idea. Bare chapter links are for genuinely chapter-wide kinship.
- **Gloss non-obvious links** with an italic aside: `[Markovovy řetězce: Monte Carlo](...) *(totéž s počítačem — balanc simulací)*`. If you can't write the gloss, you don't understand the link — drop it or figure it out.
- **A Pozn. that claims kinship must carry the link.** „Tohle je přímý příbuzný X z herního designu" without a link is a dead claim (real example from the hudba section — the reader has no path to X). Every named relationship is clickable.
- **Bidirectional linking is rationed**: the ~10 strongest relationships per batch get a backlink edit in the older chapter; passing mentions stay one-directional. Backlinks into old chapters are surgical (one line in Souvislosti or one Pozn. sentence), never rewrites.
- **Tension is content**: when a new source disagrees with an existing chapter or zápisek, link it and say who claims what. The site's credibility lives on staged disagreements, not smoothed-over consensus.
- **Rejstřík is part of the connection system**: every new term gets both layers (rejstrik.md entry + abbreviations one-liner) and the entry links back to the chapters where the term does work. Extending an existing term's „Kde se s tím potkáš" line is additive and encouraged; bodies of existing terms are never weakened (glossary never shrinks).

## 7. Timestamps: the searchability promise

- Deep-link **every moment a reader would want to see**: each claim, number, example, demonstration. For a 20 min+ video, a healthy entry has 8–15 timestamps; 3–4 usually means the evidence layer is thin.
- Compute `&t=Ns` from the cleaned transcript's block markers (`[m:ss | t=Ns]`). Use the block's `t=` — do not interpolate finer than the blocks support.
- The displayed label is `(m:ss)` of that block. Never fabricate a finer-grained time than the transcript shows.

## 8. Entry granularity

- An entry = **one claim/tool/mechanism that can carry its own evidence**. Name it after the idea (a sentence-like, assertive title beats a topic label: „Ekonomiku si zahraj na papíře, než ji naprogramuješ" beats „Papírové prototypy").
- **Thin sources merge**: a 5-minute video rarely deserves its own entry — fold it into an anchor entry as a contrasting data point (batch 24: RETRODEAD + Zoteling became one entry, „malé hry v praxi", bound by the proč-otázka; the tension between them became the Pozn.).
- **One long video may yield several entries** only if each half carries its own thesis + evidence (the 38min GDD video → 3 entries; the 39min playtest video → 4). If an entry can't survive the „Co teď udělám jinak?" test alone, it belongs inside another.
- Chapter intro: 2–4 sentences framing what the chapter covers and the common thread — update it whenever a batch extends the chapter (existing intros went stale twice before this became routine).

## 9. Craft minimum (process rails that already exist)

These are established batch routines — details and war stories live in `dev_log.md` entries for batches 20–24:

1. **Read the whole transcript** before writing anything. Notes go to the session scratchpad with `t=` anchors + a garble list per video (insurance against context loss).
2. **Garble fixing from context** — auto-captions mangle names systematically. Verify against the described *content*, not spelling („Blueprints" was actually **Blue Prince** — the room-drafting game; caught because the described mechanics matched). Unidentifiable names: paraphrase without the name, never guess. Log all fixes in dev_log.
3. **Credits from info.json only** (`channel`, `channel_url`); missing → visible TODO.
4. **Sponsor/promo segments get a Pozn. flag** when the entry synthesizes surrounding content (includes the creator's own paid services and merch, not just third-party sponsors).
5. **Glyph grep immediately after every large Czech write** — mixed-script typos (Cyrillic/CJK/German) appear reliably when producing tens of thousands of Czech words per day; catch them at write time, then once more before build:
   `grep -rnP '[^\x00-\x7FáčďéěíňóřšťúůýžÁČĎÉĚÍŇÓŘŠŤÚŮÝŽ„""‚''…–—·×→←↔≈≠≤≥°%€£§±símε†‡′″ ]' <files> | grep -vP '\((\d+:)?\d+:\d+\)'`
6. **Gates**: `.venv/bin/mkdocs build --strict` (exit 0), anchor check (cross-page `.md#frag` **and** same-page `#frag` against site HTML ids), chapter map regen (`.venv/bin/python scripts/build_chapter_map.py`).
7. **Bookkeeping**: processing_index rows → `published` + `· dávka N`; header count; teorie/index.md annotations; nav (témata live only in mkdocs.yml); dev_log entry (What/Why/How/Follow-ups — editorial decisions and garble fixes go in How; unfinished threads in Follow-ups so the next batch inherits them); roadmap tick; commit message proposed to the user (never commit).

## 10. Voice calibration

- Czech, second person, active; senior-to-senior (see content_conventions.md tone section). No filler, no „v tomto videu se dozvíme".
- English terminology untranslated; Czech equivalent may ride along on first use.
- Humor: sparing, in Pozn. or intros, never at a creator's expense. The author's skepticism is welcome *when anchored* („video tvrdí X; proti tomu stojí Y z kapitoly Z").
- Bold sparingly, for the load-bearing sentence of a paragraph — if everything is bold, nothing is.

---

## Checklist: per myšlenka

1. Title asserts an idea (not a topic, not a video name).
2. Shrnutí = teze + mechanismus + háček; self-sufficient in 2–4 sentences.
3. Rozpad covers all four layers: mechanismus / kontext problému / důkazy / hranice+důsledky.
4. Every *what* has its *why* — decisions from the video carry their reasons.
5. Numbers preserved exactly; nothing invented; vague stays vague.
6. 8–15 timestamps for long videos; every number/example is jump-linked.
7. At least one connection to an existing chapter — anchor-specific, glossed if non-obvious.
8. Pozn. used for: our interpretation, conflicts between sources, sponsor flags, caveats.
9. New terms → both glossary layers; existing terms → „Kde se s tím potkáš" extended.
10. Rozpad ≥ ~150 words or the entry is merged elsewhere.

## Checklist: per dávka

1. All transcripts read fully; scratchpad notes with `t=` + garble lists exist.
2. Credits extracted from info.json for every video before writing.
3. Chapter intros updated where extended; no stale „budoucí kapitola" placeholders left behind.
4. ~10 strongest links made bidirectional (backlink edits in old chapters).
5. Follow-ups from the previous batch's dev_log honored or explicitly deferred.
6. Glyph grep clean; build --strict exit 0; anchor check 0 problems (both link kinds); chapter map regenerated.
7. rejstrik.md + abbreviations.md both extended; counts reported.
8. processing_index rows + header updated; teorie/index.md + mkdocs.yml nav updated.
9. dev_log entry written (What/Why/How/Follow-ups), roadmap ticked.
10. Commit message proposed; **no git commit/push** — the user commits.
