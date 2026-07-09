# Project Brief

The assignment and vision. Authoritative for **what** we're building and why. For **how** content is written, see `content_conventions.md`; for structure, `architecture.md`.

## The problem

The author maintains a YouTube playlist of gamedev videos (200+, growing) collected while developing his own games (a UE5 stealth-horror project, a commercial UE5 locomotion component, a web point-and-click engine). The playlist has become unsearchable: finding *that one idea from that one video* means hunting for the right video, then the right minute. Knowledge is trapped.

## The solution

Turn the playlist into **skripta** — the Czech term for self-authored student study notes: distilled, explained, cross-linked, searchable. Not transcripts. Not video summaries. A textbook the author writes for himself (with agent help), where each chapter *teaches an idea* and cites the videos it came from with clickable timestamp links.

A second source feeds the same site: the author's own project journals and AI-conversation summaries (incubator postmortems, architecture debates, release planning). These become **Zápisky** — anonymized, distilled lessons from real development practice.

## The three documents

1. **Teorie her** (`docs/teorie/`) — game design theory: mechanics, loops/chains, player psychology, scope, production wisdom, creative process.
2. **Praxe v UE5** (`docs/praxe/`) — hands-on Unreal Engine 5: editor workflows, Blueprint patterns, systems (terrain, animation, rendering), optimization.
3. **Zápisky** (`docs/zapisky/`) — lessons from the author's own projects: what happened (anonymized), what it taught, how it connects to theory/practice chapters.

Plus the **Rejstřík** (`docs/rejstrik.md`) — a growing glossary of professional terminology (English terms, Czech explanations). Doubles as a study tool: the author is explicitly training industry vocabulary.

## Audience

Primarily the author — future self returning to game development with recharged energy. Secondarily: Czech-speaking self-taught gamedev learners, once published. Write for a smart practitioner, not a beginner tutorial reader: assume programming literacy, explain gamedev-specific concepts properly.

## What "done well" looks like

- Full-text search finds an idea in seconds; a timestamp link lands in the right minute of the source video.
- A chapter is worth reading even without watching the video — it explains, contextualizes, and adds honest caveats (e.g. engine-version dependence, debatable performance claims).
- Terms encountered anywhere on the site have hover tooltips and a glossary entry with context links.
- Creators get visible credit and traffic (links to their channels), never content substitution.

## Out of scope

- Hosting or re-publishing any video content, thumbnails, or transcript text.
- Covering topics with no source in the playlist or inbox (no padding chapters from general knowledge alone; general knowledge *supports* explanation of sourced ideas).
- Perfect coverage. Batch quality > batch size; an unprocessed video is better than a shallow chapter.

## Why these decisions (short)

- **Ideas over videos as the unit:** searchability and pedagogy — and it keeps published text transformative rather than derivative (licensing).
- **Czech content, English terms:** the author thinks in Czech and needs the English vocabulary — both goals in one format.
- **MkDocs Material over a custom app:** content is Markdown; search, navigation, light theme, and Pages deploy come free; zero code to maintain in a knowledge repo.
- **Zápisky anonymized by principle:** identities are not important for the idea; the repo is public.
