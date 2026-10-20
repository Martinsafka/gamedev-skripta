# UE skills — complement to Epic's skills (working brief)

> **Status (2026-10-11): step 1 of 3 done.** Epic's public Claude Code plugin is inventoried and the known engine-native skills are listed. Step 2 needs a UE 5.8 editor on the user's UE machine; this Mac has no engine install. Follow `workflow.md` as with any task.

## Goal

User's decision 2026-10-11: agent skills that carry the best practices of the whole **Praxe v UE5** library into vibe coding with an agent in Unreal, primarily over MCP. Much will already be in Epic's skills, so the order is fixed: **inventory Epic's skills → compare with our chapters → build our skills only for what Epic lacks.** Nothing gets built before step 3 ends.

## Epic's skills — inventory

### Layer 1: the Claude Code plugin (public, MIT)

[`EpicGames/unreal-engine-skills-for-claude-code-plugin`](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin), version 3.1.1, commit `a6aa73a` (2026-09-17), listed at [claude.com/plugins](https://claude.com/plugins/unreal-engine-skills-for-claude-code) and installed from Anthropic's official marketplace as `unreal-engine-skills-for-claude-code@claude-plugins-official`. Read in full from a shallow clone in the session scratchpad. Nothing from it is stored in this repo; re-clone by the commit above.

| Part | Covers |
|---|---|
| `unreal-mcp` skill + `references/setup.md`, `references/operations.md` | Operating the editor over MCP: tool search (three meta-tools, toolsets discovered on demand), safety (recovery point before and after bulk changes, wait for compilation and rebuild through Live Coding, serialize dependent calls, treat anything but an explicit success as a stop, PIE changes behaviour), discovery of the project's Agent Skills (a relevant one overrides generic defaults), first-time setup, proxy, troubleshooting. |
| `unreal-skill` skill | Authoring UE-native Agent Skills (a Python class in a plugin, or a UAsset for project-only skills) and six principles: novel, collegial, flexible, durable, agnostic, parsimonious. |
| `create-toolset` skill | Authoring toolsets in C++ or Python: API design, documentation, error handling, tests. |
| SessionStart hook | Detects a UE project and injects a short context note. |

**Domain knowledge: none.** Nothing on performance, PCG, lighting, animation or architecture. The plugin is the operating manual; the domain skills live in the engine.

### Layer 2: engine-native Agent Skills (UE 5.8)

Registered in the editor through `ToolsetRegistry` and offered to any MCP client through the agent skill toolset (list, then load). Known so far from the [Python API reference](https://dev.epicgames.com/documentation/en-us/unreal-engine/python-api/class/AgentSkill) (Unreal Python 5.8, Experimental). The docs publish names and short descriptions only, **never the instructions**:

| Skill | Coverage per the docs |
|---|---|
| `DefaultOutdoorLightingSkill` | Adjusting the default outdoor lighting setup: sun, sky, clouds, fog, exposure. |
| `MaterialBasicsSkill` | Materials and Material Instances: creating, modifying, choosing between them. |
| `BlueprintBasicsSkill` | Name only (class index). |
| `PCGGraphGenerationSkill` | In the PCG toolset plugin; the class page now redirects to 404. |
| `NiagaraLevelPlacementSkill` | Putting an effect into a level only after searching existing systems, showing the matches and getting approval (search snippet; page now 404). |
| `NiagaraBlueprintInteropSkill` | Effects driven from Blueprint at runtime: spawning, parameter wiring, reuse (search snippet). |
| `NiagaraCleanupSkill` | Finding unused modules, unused user parameters and leftover state in a Niagara System (search snippet). |
| `DataflowGraphEditingSkill` | Name only. |

**The list is incomplete.** The docs class index could not be scanned reliably and two class pages return 404. The authoritative list and the instruction texts come from a running editor (step 2).

## Triage: our Praxe chapters vs. Epic

| Domain | Our chapters | Epic counterpart | Status |
|---|---|---|---|
| Lighting | `osvetleni`, `megalights` | `DefaultOutdoorLightingSkill` | overlap possible on outdoor sun, sky, fog, exposure |
| Materials | `materialy`, `textury-a-dlss` | `MaterialBasicsSkill` | basics may overlap; our chapters go further |
| Blueprint | `komunikace-blueprintu`, `principy-architektury`, `interakce-bez-event-ticku`, `gameplay-tags` | `BlueprintBasicsSkill` | unknown until the text is in |
| PCG | `pcg-zaklady`, `pcg-vegetace`, `pcg-mesta`, `pcg-liany`, `pcg-hexagone` | `PCGGraphGenerationSkill` (+ the PCG primitives plugin from the Unreal Fest talk in `mcp-v-editoru`) | compare in step 3 |
| Niagara | `niagara-vykon` | three Niagara workflow skills | ours is performance; small overlap expected (reuse) |
| Chaos / Dataflow | `destrukce-a-latky` | `DataflowGraphEditingSkill` | unknown |
| Agent operation | `mcp-v-editoru`, `claude-code-ue` | `unreal-mcp` | operation covered by Epic; agent failure modes in UE content are not |
| **Everything else** | **55 chapters**: performance and profiling, GASP and animation, NPC AI, world building, gameplay systems, saving, project organization, debugging, … | none known | **gap: goes straight to our skills** |

17 of the 72 Praxe chapters sit in overlap domains; 55 have no known Epic counterpart.

## Steps

1. ✅ **Inventory** _(2026-10-11)_: layer 1 read in full, layer 2 from the docs.
2. ☐ **Dump the engine-native skills** from a UE 5.8 editor with `AllToolsets` enabled, so every toolset plugin registers its skills. In Claude Code connected over MCP: list the skills through the agent skill toolset, load each one, write name, path or class, description and the full instructions verbatim into one Markdown file, change nothing else. The file goes to `epic_skills/` (gitignored: UE EULA content, never commit, never quote into our text).
3. ☐ **Compare idea by idea, only in the overlap domains.** Each H2 idea of the 17 chapters (heading + Shrnutí, deeper only where needed) against Epic's instructions → covered / partial / missing / conflicting. A conflict gets a note saying whether it is version drift or a real disagreement between our source and Epic. Output: a matrix in this file, then a proposal for the skill set (split, form, pilot). Estimated cost: tens of thousands of tokens.

## Constraints already known

- Follow Epic's six principles (`unreal-skill`). "Durable" and "agnostic" mean: no tool names, property names only where verified for the version, no references to models or harnesses.
- Rules are distilled from our chapters, never from transcripts. Each rule links to its chapter section, which holds the full reasoning and the video credit.
- Our own readings („Toto čtení je naše") go in only marked as heuristics; promo segments never.
- Distribution form is open: a Claude Code plugin (works without the editor, e.g. writing C++ in an IDE), UE-native Agent Skills (found by any MCP client; Epic's `unreal-mcp` lets a relevant project skill override defaults), or both generated from one source.
- These skills author content and mechanic-mentor never does (its hard rule 1). Keep them in separate plugins.
- The existing skills only link to chapters (`skill_validation_and_packaging.md`). These must carry the rules themselves, so they need a staleness check against their source sections.

## Docs accuracy follow-ups found during the inventory (not done)

- `docs/praxe/claude-code-ue.md:157` says native MCP cannot run Python scripts (a video's claim). Epic's README now lists a programmatic toolset that runs Python inside the editor. Find the version that added it, then add a Pozn.
- `docs/praxe/mcp-v-editoru.md:74`: the context overflow from tool descriptions. Epic's server now defaults to tool search (three meta-tools), which the webinar mentioned only as under consideration.
- `docs/praxe/mcp-v-editoru.md:43`: required plugins. The README names ModelContextProtocol and AllToolsets; our chapter lists three including Editor Tool Set. Check against current documentation.
