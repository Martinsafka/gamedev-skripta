# Problem-Solving Workflow

Follow this loop for **every** task. Don't skip analysis or the log.

## 1. Analyze the assignment

- Re-read the request. Identify what's actually being asked and what "done" looks like.
- Read the relevant `agent_docs/` doc(s) for the area you're touching (progressive-disclosure list in `AGENTS.md`). Don't load everything.
- For content tasks: read the **cleaned transcript(s)** in `transcripts_clean/` fully before writing a word. Check `info.json` for credit data. Check `agent_docs/processing_index.md` for the video's assigned chapter/theme (taxonomy phase output).
- If anything is **missing, ambiguous, or needs an editorial decision the user should make → ask before writing.** A wrong chapter split costs more than a question. State assumptions inline.

## 2. Propose

- For content: outline the chapter — which entries (ideas), what each teaches, which document/chapter it lands in, which existing chapters it links to. For batches, propose the batch plan first (which videos → which chapters).
- For pipeline/infra: outline the change and its blast radius.
- Respect the **invariants** in `AGENTS.md` (licensing, anonymization, credits, gitignore boundaries). If the task seems to require breaking one, **stop and flag it**.
- **Don't over-produce.** A tight chapter that teaches beats a long one that catalogs. Match depth to the idea's weight — a 100-word editor tip does not get a 800-word entry.
- For non-trivial structural changes (new chapter categories, nav reshuffles, template changes), get a quick nod before executing.

## 3. Execute

- Write per `content_conventions.md` — template, language, credits, timestamps.
- Update the glossary (both layers) with new terms from the material.
- Add cross-links both ways (new chapter ↔ related chapters/zápisky).
- Update `mkdocs.yml` nav and `agent_docs/processing_index.md` status.
- **Run `mkdocs build --strict`** before considering it done.

## 4. Log

- Append an entry to `agent_docs/dev_log.md`: **what** (chapters/entries/terms added), **why**, **how** (grouping decisions, tricky transcript issues, anything the next session needs). **Mandatory, not optional.**

## 5. Propose a commit message

- Concise subject + short body (what/why). Match the repo's existing style.
- **Don't run `git commit` or `git push` unless explicitly asked.** The user commits.

## 6. Point to the next step

- When a task completes a phase chunk in `agent_docs/roadmap.md`, propose what to tackle next and tick the relevant checkboxes.
