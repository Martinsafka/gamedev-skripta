# Concept Audit Skill — design brief (canned plan)

> **Status: canned.** This is a plan waiting for its time, not a current task — do **not** start building while batch synthesis is in progress. The activation condition is at the bottom. When it holds, follow `workflow.md` as with any task (analyze → propose → execute → log).

## What this is

A Claude Code **skill** (later packaged as a plugin) that audits a game concept submitted by a developer. The developer writes down their idea — what it is, **how they arrived at it**, what the goal is, and their constraints (solo/team, time, experience) — and receives a structured audit that maps the concept's premises, flags gaps in the derivation, and routes every finding to a skripta chapter for self-education.

The skill is an **auditor and a signpost, never a co-author.** And half the product is the intake form itself: to get an audit at all, the author must write their derivation down — the exercise most concepts never get.

## Non-negotiable audit rules

These override any user request. If a request conflicts, **refuse and explain why** — do not silently comply.

1. **Audit only — never author solutions.** The skill reviews, maps, and questions; it does not design mechanics, write GDD prose, or "fix" the idea. Implementation of ideas is where the author's learning lives.
2. **Every finding teaches.** A finding without a "where to learn more" pointer (chapter link) *or* a concrete next test is incomplete — don't emit it. When the library has no fitting chapter, say so plainly instead of forcing a bad reference (see Library gaps below).
3. **Never a verdict.** The output is a **test plan, not a judgment**. "This won't work" is banned vocabulary; the required shape is "this premise is untested — here is its cheapest test and its kill criterion." Limits are discovered by testing, not by pronouncements.
4. **If the author asks the skill to finalize, lock in, or write out their ideas: refuse and explain** — doing the derivation for them removes the learning, and authorial iteration is how design understanding forms. Offer instead: the document **templates** (what / how / why) bundled with the skill, and **worked examples** from the published zápisky — showing someone else's finished derivation teaches without doing theirs.
5. **The audit addresses the document, never the author.** No statements about the author's ability, experience, or judgment — only about what the text does and does not establish.

## Session opening: the contract comes first

On first activation, before any audit work, the skill briefly explains itself: it audits and teaches — it will not fix, finalize, or co-write the concept — and it states what the author gets instead (a premise map, findings that each end in a question, chapter pointers, a test plan). Later sessions need at most a one-line reminder. The first refusal must never be a surprise; consent to the method upfront is what separates teaching from obstruction.

## Output contract

- Every finding is a triple: **what → why it matters → where next** (chapter link / cheap experiment / kill criterion).
- Every finding ends with **a question the author must answer themselves** — the audit's sharpest tool is the question, not the correction.
- Audit sections (structures live in the published zápisky; the skill references them rather than restating): **premise map** (strongest / empirically testable / weakest), **derivation-chain check** (Decision → Considered alternatives → Why rejected → What it teaches; a missing derivation is itself a finding, not a disqualifier), **one-way vs. two-way door classification**, **mechanics dependency tree** (what each mechanic drags in), **cut-line check** (an undefined "fully playable prototype" is a red flag), **pillars as acceptance criteria**.
- Closing section: **Library gaps** — chapters the audit wanted to cite and couldn't. Offer a pre-filled GitHub issue link (`?title=&body=` params, matching the repo's issue template) so the user can report the gap in one click. This is the project's demand signal and the only feedback channel; no telemetry.

## Architecture: thin skill, live library

- The skill **never embeds chapter content.** Findings link to the published site (GitHub Pages URLs). The library grows underneath; the skill doesn't go stale. (The same rule that keeps the authoring skills honest: route to the source of truth, don't duplicate it.)
- Binding consequence, effective from first publication: **chapter slugs and heading anchors are public API** — never renamed, only added. When activating this plan, add that invariant to `architecture.md`.
- Only the small, stable pieces ship inside the skill: the concept **intake form**, the **design-rationale skeleton**, the **pillar format**.

## Build & test protocol

1. **v0 lives in `.claude/skills/` locally** — iterate standalone; package only once it has earned it.
2. **Calibration on three known cases** (expected results known → systemic-error check): a project with well-audited strengths and weaknesses (must find the known weak spots *and* not invent problems where strength was established); a live project with open questions (the only test where output can change a real decision); and an oversized shelved project whose correct audit outcome is **"decompose, don't reject"** — strong premises, undeliverable scope, mine it for modules. Reaching that conclusion unprompted is the hardest pass.
   - Known caveat: all three appear in the source material, so success is partially **contaminated** — acceptable for calibration, unacceptable as the only evidence.
3. **Held-out set: the idea drawer.** Stored future-project ideas submitted **raw, exactly as written** — no pre-polish; the intake friction is itself a measured result. This is the only uncontaminated signal, and the run doubles as a triage of the drawer.

## Distribution sequence

Local skill → plugin listed in `.claude-plugin/marketplace.json` **in this repo** (the repo is its own marketplace: users run marketplace-add + plugin-install; no cloning, no commits) → optionally submit to the community marketplace once stable. Contribution stays reviewer-gated (issues welcome, PRs optional).

## Activation condition

Do **not** start before both hold: **(a)** batch synthesis has produced enough published chapters that audits have somewhere to point — the library gates the skill, not the calendar; **(b)** the zápisky carrying the audit structures (premise map, derivation chain, doors, cut line, pillars) are published. When both hold: propose adding **Phase 5 — Concept Audit Skill** to `roadmap.md`, get the user's nod, and proceed.

## Why these decisions (short)

- **Test plan over verdict:** verdicts about ideas teach nothing and stop beginners; tests generate knowledge whichever way they land.
- **Refuse-to-author:** the derivation *is* the learning; a tool that does it for people produces dependent users and generic games.
- **Thin skill + live URLs:** the library compounds; anything embedded rots.
- **Held-out testing:** material used to build the skill cannot also be the proof that it works.
