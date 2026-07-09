# Content Conventions

Authoritative for **every line published in `docs/`**. If a draft conflicts with this doc, the draft is wrong.

## Language

- **Body text: Czech.** Natural, direct, professional — the author's own study notes, not marketing copy. Occasional light humor is fine; padding is not.
- **Terminology: English**, exactly as the industry and the UE5 editor use it (Line Trace, Event Tick, Nanite, value chain). Never translate a term the editor shows in English. Established Czech equivalents may appear alongside on first use: „smyčka (loop)".
- Formatting: standard Markdown; bold for key statements, inline code for editor paths/nodes/settings (`Class Settings → Interfaces`), blockquotes only for the author's own margin notes (see Pozn. below).

## The entry template (myšlenka)

Every idea entry inside a chapter follows this structure:

```markdown
## Název myšlenky            <!-- named after the IDEA, in Czech -->

**Zdroj:** [Video Title](https://www.youtube.com/watch?v=ID) · [Channel Name](channel_url) · délka, typ (tutoriál / esej / tip)

**Shrnutí:** 2–4 sentences. What the idea is and why it matters. A reader who
stops here should still take away the point.

### Rozpad myšlenky          <!-- the teaching part; own structure, own words -->

Detailed explanation organized by OUR logic (concept → mechanics → consequences
→ pitfalls), NOT by the video's narrative order. Add context the video lacks:
why it works, when it breaks, how it relates to other chapters. Timestamp
deep links at the moments a reader would want to see:
[(4:33)](https://www.youtube.com/watch?v=ID&t=273s)

> **Pozn.:** Author-voice margin note — honest caveats (version dependence,
> debatable claims, our own experience). Optional but encouraged.

**Souvislosti:** links to related chapters, zápisky, rejstřík terms.
```

Rules:

- **Name entries after ideas, never after videos.** "Interakce přes overlap místo per-tick trace", not "How to Line Trace Without Event Tick".
- **Shrnutí is self-sufficient**; Rozpad is where depth lives.
- **Timestamp links** (`&t=SECONDSs`) at every moment worth jumping to — this is the project's core searchability promise. Compute seconds from the cleaned transcript's `t=` markers.
- **Credit block is mandatory and complete**: video link + channel link. Channel name/URL come from the video's `info.json` (`channel`, `channel_url`). Missing → `<!-- TODO: credit z info.json -->` placeholder, never a guess.
- A chapter merging several videos still keeps one credit block per entry/source.

## Licensing guardrails (restated from AGENTS.md — they win every conflict)

- Synthesis in own words only. **No verbatim transcript sentences.** If a specific formulation matters, paraphrase and attribute ("autor videa razí pravidlo…").
- **Do not mirror the video's structure.** Reorganize by concept. A reader should learn the idea; watching the video should still offer something extra (the demonstration).
- Auto-captions garble technical terms — **fix them from context** (e.g. "spalunky" → Spelunky, "rogike" → roguelike, "teslation" → tessellation). The transcript is evidence of what was said, not ground truth for spelling.
- Facts stated only by the video (new engine features, version specifics) are reported as the video's teaching, with a Pozn. flag where verification is pending — never silently "improved" from the agent's assumptions.

## Rejstřík conventions

- Terms in **English**, explanation in **Czech**. Format per entry in `docs/rejstrik.md`:
  `### Term` → one-line definition (bold) → 2–5 sentence explanation → „Kde se s tím potkáš:" links to chapters.
- Every entry's term also gets a `*[Term]: one-line Czech definition` line in `includes/abbreviations.md` (tooltips). Keep the one-liner under ~120 characters.
- **When processing any video: extract new terms, add both layers.** The glossary grows with content, never as a bulk import.
- Alphabetical order within `rejstrik.md`. Anchors: lowercase-hyphenated.
- Multi-word terms work in tooltips (`*[Blueprint Interface]: …`) — prefer the exact casing used in text.

## Zápisky conventions

- Source material arrives in `inbox/` (gitignored): devlogs, AI-conversation summaries, postmortems.
- Published zápisek = **distilled lesson**, structured: Kontext (anonymized, minimal) → Co se stalo → Co si z toho beru → Souvislosti (links to teorie/praxe chapters).
- **Anonymization is absolute: identities are not important for the idea.** No personal names, no organization names, no dates/places that identify, no quotes from other people. "kolegyně z komunitní organizace" is fine; anything traceable is not. When in doubt, generalize further.
- Zápisky may disagree with theory chapters — real experience beats received wisdom; link the tension explicitly ("teorie říká X, v praxi nás potkalo Y").
- Cross-link both ways: the zápisek lists related chapters; touched chapters gain a „Souvislosti" link back.

## Tone calibration (the whole site)

Write like a sharp senior colleague explaining to another senior: no filler ("v dnešní době…"), no hedging walls, no bullet-point dumps where prose teaches better. Bullets only for genuinely enumerable things (settings lists, step sequences). Humor sparingly, in Pozn. blocks or chapter intros — never at a creator's expense.
