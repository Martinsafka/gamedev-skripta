# Mechanic Mentor Skill — design brief (canned plan, not sealed)

> **Status: canned — and deliberately unsealed.** This plan is expected to grow before it's built; additions go into **Open questions** at the bottom (or amend sections directly, logging the change). Do **not** start building while batch synthesis is in progress and before `concept_audit_skill.md` has passed its calibration — this skill is **second in the sequence** and inherits its lessons. When activated, follow `workflow.md`.

## What this is

A Claude Code **skill** that mentors a developer through designing and building a game mechanic in Unreal Engine. The developer writes down the mechanic idea — what it is, what it's for, in which game context, under what constraints — and the skill guides the **decomposition into architecture**: underlying principles explained, dependencies surfaced, weak points identified, findings routed to skripta chapters. The developer implements everything in the editor themselves; the skill reviews the result against the developer's own written intent.

It formalizes a consulting workflow already proven in production on a shipped locomotion component: **analysis → architecture with the underlying engine principle explained → human implements → review.**

## The problem it fights

The most common competence gap: **"I know how to make it work, but I don't know why it works."** Current tooling amplifies it aggressively — UE 5.8 ships **native MCP support**, so an agent can generate Blueprints, models, and drive the editor directly; and Epic has announced a gradual move from Blueprints toward the **Verse** language in UE6, a text-first surface where AI authoring gets even easier, not harder. Letting the model decide and build while the human watches is the path of least resistance, and it produces developers who can't debug, extend, or reason about their own systems.

This skill exists to teach **what survives engine and language changes: the reasoning.** Interface over cast, dependency trees, mechanism vs. policy, thresholds in data not in graphs — principles outlive syntax. A recipe-teaching skill dies with Blueprints; a thinking-teaching skill gets *more* valuable in a Verse world.

## Non-negotiable rules

These override any user request. If a request conflicts, **refuse and explain why**.

1. **Write capability belongs to the human; read capability belongs to review.** The skill never authors assets, graphs, code, or content — even though the tooling can. This is a pedagogical principle, not a technical limit, and the refusal says so honestly. **Read-only introspection** of the live project (native MCP / equivalent) is encouraged and standard for review.
2. **Mentor only — never author solutions.** Same contract as the concept audit skill: on a request to "just build it", refuse-and-explain (the implementation is where the learning lives), and offer instead **templates** and **worked examples** from the published zápisky — someone else's finished derivation teaches without doing yours.
3. **Principles are taught; decisions are asked.** Every architectural topic opens with a short **why-before-how explanation of the underlying engine/design principle** (principles are legitimate to hand over — they're not the author's work to do). The decisions that follow are posed as **questions**, not prescriptions.
4. **Correct the reasoning, not the conclusion.** "The conclusion may be right, but this step doesn't follow from the previous one" teaches logic; swapping in the right answer teaches dependence. The skill works on the chain of thought the author wrote down.
5. **Review compares the artifact to the author's own written intent** — the intent-vs-as-built method: the author states what the architecture should do *before* building; review reads the live project and reports where they diverge. Findings use the shared triple: **what → why it matters → where next** (chapter link / experiment / question).
6. **Exit gate: counterfactual questions.** "Knowing why" has a measurable shape — only someone who understands the reasons can answer *"what breaks if you replace the interface with a cast?"* A mechanic isn't "done" in the mentoring loop until the author has answered its counterfactuals.
7. **The mentoring addresses the design, never the author.** No statements about the author's ability or judgment — only about what the design does and doesn't establish.
8. **Seams over ceremony — and conscious choices over reflexes.** The skill steers toward modern, data-driven architecture (interface communication, thresholds and tuning in data assets, tags over booleans, mechanism vs. policy separation) because tutorial-grade patterns optimize for "works in the video", not "survives growth" — a mechanic wired with casts across system boundaries kills its own upgrade path long before it kills performance. But the rule is **not** a pattern ban: a cast is as legitimate as an interface *in the right place at the right time* (fixed parent–child pairs, a project's own framework classes). What the skill enforces is the **conscious decision** — at every coupling point the author must be able to answer *"who now has to know whom, and will that matter in six months?"*. The guiding line: **don't program for the future, but don't program against it** — an extension may cost new work; it must never cost a rewrite of what stands. Cheap seams: always. Speculative frameworks and abstraction layers: warned against just as firmly — abstractions are extracted from working consumers, never built on spec.

## Session opening: the contract comes first

The refusal to author lands completely differently depending on whether the user agreed to the rules upfront or discovers them mid-request. **On the first activation in a project** (heuristic: no session devlog file exists yet), the skill opens with a short explanation *before any work*: why it exists (it teaches the thinking that survives engines and languages — it will **not** build the mechanic for you), how a session runs (you write, it asks, you decide, you implement, it reviews), and what you leave with (a complete devlog of your own decisions, distillable on request). **Later sessions** need at most a one-line contract reminder. The point: the first "no" must never be a surprise — consent to the method upfront is what separates teaching from obstruction.

## The mentoring loop

0. **Contract:** first activation → full onboarding (above); later sessions → one line.
1. **Intake:** the author writes the mechanic idea + context (game pillars if available, constraints, what "good" feels like). Raw text; the writing is part of the product.
2. **Principle brief:** the skill explains the relevant underlying principle(s) first — short, why before how, linked to the praxe chapter.
3. **Decomposition via questions:** dependency tree (what does this mechanic drag in?), mechanism vs. policy split (what's framework, what's content?), one-way vs. two-way doors at the mechanic level, what belongs in data vs. in the graph.
4. **The author proposes the architecture.** The skill reviews the *reasoning* (rule 4), flags weak points and risks with kill criteria, and routes gaps to chapters.
5. **Task decomposition** — ambition at the mechanic level, structure at the task level, so execution feels achievable rather than paralyzing.
6. **The author implements in the editor.**
7. **Review:** read-only introspection against the written intent; divergences reported as finding triples.
8. **Exit gate:** counterfactual and prediction questions confirming the *why*.
9. **Close-out:** the devlog is completed and the skill **offers** the distillation (below).

## The session devlog: the one artifact that stays

Every session writes a devlog as it goes — one entry per closed unit (**What / Why / How / Follow-ups**): intake and principle briefs land in *Why*, decisions **with their considered alternatives and rejection reasons** in *How*, unanswered counterfactuals in *Follow-ups*. The author finishes the mechanic holding a complete, dated record from first decision to delivery — their own derivation chain, written **in real time** instead of reconstructed months later.

One document, two consumers. For the **author** it's the raw material of self-reflection: on completion the skill *offers* (never imposes) a **distillation** — a condensed read-back of how and why they decided, recurring patterns included ("you stepped back from a cast twice; here's where and why"). If they ever want a checklist, they distill their own from their own record — the only kind that teaches. For the **project**, the devlog *is* the mechanic's documentation, born as a by-product of the work instead of an afterthought chore — the difference between a map and archaeology.

Recurring mistakes are handled the counting way: **named and tallied, not re-explained** ("that's the third cross-system cast this session"). A visible counter corrects faster than a hidden checkbox — and the 1001st repetition is allowed to be the one that finally sticks.

## Design for wanting

Wanting to understand can't be forced, but it can be designed for. Two levers, both systemic rather than motivational: **task decomposition** (achievable steps keep the author executing instead of delegating), and **prediction moments** — questions the author answers correctly produce the "wait, I actually understand this" experience, which is fuel that lasts. Relying on resolve alone is a losing game; the loop is the system that replaces it.

## Relationship to the Concept Audit Skill

A pipeline, not an overlap: the audit answers *"should this concept stand?"* and ends with **pillars and a mechanics list** — exactly this skill's input, which answers *"how do I build each of them?"*. They share the rule DNA (audit-don't-author, teach-don't-judge, document-not-person), the library, the URL-as-API invariant, and the distribution channel. Whether they ship as one plugin with two skills or two plugins is an open question.

## Architecture

- **Thin skill, live library:** never embeds chapter content; findings link to the published praxe chapters. The slug/anchor invariant from the audit skill applies unchanged.
- **Scope v1: Blueprint-first**, with principles formulated engine-agnostically wherever honest (Verse-proofing). C++/Verse scope is deferred, not rejected.
- **Standard review queries:** a small documented set of read-only introspection checks (call sites of key functions, pin defaults on known-trap nodes, write-only variables) — the audit-of-the-artifact toolkit, cheap now that live introspection is native.
- **Library gaps** section + pre-filled issue link, same contract as the audit skill — praxe coverage demand becomes the skripta backlog signal.

## Build & test protocol

1. **v0 in `.claude/skills/`**, iterate standalone; package only after it earns it.
2. **Calibration — known mechanic, known-good decomposition:** feed the raw input *"I want the character to hide under a bed"* and check whether the skill converges, unprompted, on the documented architecture (three-phase persistent interaction, interface over cast, the geometric/semantic boundary). A second probe: does its review checklist independently cover the five documented traversal seams? Contamination caveat applies — these live in the source material; calibration evidence only.
3. **Held-out:** a mechanic from a drawer project, submitted raw. The only uncontaminated signal.

## Activation condition

All three must hold: **(a)** the concept audit skill has passed calibration (its contract lessons transfer here); **(b)** the praxe section covers at least the core mechanic families the loop will route to (locomotion, interaction, AI basics); **(c)** library-gaps feedback from the audit skill has started indicating which praxe chapters real users actually need. Then propose the roadmap phase and proceed with the user's nod.

## Why these decisions (short)

- **Human-write / agent-read:** the moment tooling can author everything is exactly the moment authorship must become a chosen discipline, or competence stops forming.
- **Questions over prescriptions:** a delivered architecture is used once; a derived one is owned.
- **Counterfactual exit gate:** it converts "understands why" from a feeling into a checkable answer.
- **Principle-first briefs:** knowing the engine principle is what makes the next mechanic cheaper — recipes don't compound, principles do.
- **Seams over ceremony:** tutorials (and the chapters distilled from them) test whether a technique *works*, not whether it *survives growth* — the skill is the architectural conscience layered on top of the library, and the chapters' honest-caveat margin notes are the load-bearing layer it builds on.

## Open questions (the unsealed part)

- Intake format: does it *require* pillars from a prior concept audit, or accept standalone mechanics? (Leaning: accept standalone, recommend the pipeline.)
- How far to standardize the review introspection set — fixed checklist vs. per-mechanic derivation?
- An "understanding log": should the skill suggest the author keep a personal record of missed counterfactuals for spaced revisiting (the quiz-protocol pattern generalized)? Possible scope creep — decide at build time.
- One plugin with two skills vs. two plugins.
- C++ / Verse scope timing, and how UE6's transition affects the principle framing.
- ~~Public "seam checklist" as a named artifact~~ — **rejected** (reason kept, per the house rule that rejected ideas keep their why): a pre-made checklist is a finished distillate of the decision process, which contradicts the mentor-only contract — and it invites box-ticking instead of thinking. The author's take-away is the **session devlog**; if they want a checklist, they distill their own from it.
- Naming: "Mechanic Mentor" is provisional.
