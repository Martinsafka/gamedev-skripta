#!/usr/bin/env python3
"""Evidence for agent_docs/content_gaps.md.

Counts how much a candidate topic is actually present in the transcript corpus
(`transcripts_clean/`) and how many published chapters already touch it.
A gap row is only worth writing down when the corpus is thin AND docs are thin.

Usage:
    .venv/bin/python scripts/gap_scan.py            # all topics
    .venv/bin/python scripts/gap_scan.py ui audio   # only matching topic keys

To extend: add a row to TOPICS. Keys must match the topic names used in
agent_docs/content_gaps.md so the table and the evidence stay in sync.

Regex note: do NOT put a trailing \\b after a stem. `replicat\\b` never matches
"replication"; that bug once produced a table of false zeroes.
"""
import collections
import glob
import os
import re
import sys

CORPUS = "transcripts_clean/*.txt"
DOCS = "docs/**/*.md"

# topic key -> (corpus regex, docs regex)
TOPICS = {
    "cpu-game-thread": (
        r"(game thread|cpu bound|cpu-bound|render thread|stat game)",
        r"(game thread|hlavní vlákno|render thread)",
    ),
    "editor-vs-build": (
        r"(shipping build|development build|packaged (build|game)|launch options)",
        r"(shipping build|development build|zabalen|packaged)",
    ),
    "blueprint-vs-cpp": (
        r"(blueprint.{0,40}(overhead|slow|fast|cost|performance|expensive)"
        r"|c\+\+.{0,30}(faster|performance|cheaper))",
        r"(blueprint.{0,40}(režie|pomal|rychlej|cena|nákl)|C\+\+.{0,30}(rychlej|výkon))",
    ),
    "pso-shader-stutter": (
        r"(\bpso\b|pipeline state object|shader compil|shader stutter|precach)",
        r"(\bPSO\b|kompilace shader|shader stutter|precach)",
    ),
    "ui-umg": (
        r"(\bumg\b|widget blueprint|common ?ui)",
        r"(\bUMG\b|widget blueprint|Common ?UI)",
    ),
    "audio-implementation": (
        r"(\bwwise\b|\bfmod\b|metasound|audio middleware|sound concurrenc|audio thread)",
        r"(Wwise|FMOD|MetaSound|audio middleware)",
    ),
    "networking": (
        r"(replicat|dedicated server|listen server|net cull|dormanc|client[- ]side predict)",
        r"(replikac|dedikovan.{0,10}server|listen server)",
    ),
    "testing-qa": (
        r"(unit test|automation (test|spec)|functional test|gauntlet)",
        r"(unit test|automatizovan.{0,15}test|funkční test)",
    ),
    "build-iteration-time": (
        r"(cook(ing)? time|build time|iteration time|derived data cache|\bddc\b)",
        r"(doba (cooku|buildu)|iterační (čas|doba)|derived data|\bDDC\b)",
    ),
    "localization": (
        r"(localizat|localis|string table|\bi18n\b)",
        r"(lokalizac|string table)",
    ),
    "accessibility": (
        r"(accessibilit|colou?r ?blind|screen reader|remapp|subtitle.{0,20}(option|size))",
        r"(přístupnost|barvoslep|čtečk.{0,10}obrazovk|remapov)",
    ),
    "mobile-lowend": (
        r"(mobile (game|perform|render)|steam deck|low[- ]end (pc|hardware)"
        r"|integrated (gpu|graphics)|min ?spec)",
        r"(mobiln.{0,10}(hra|výkon)|Steam Deck|slabš.{0,10}(stroj|hardware))",
    ),
    "console-porting": (
        r"(certificat|port(ing)? to (console|switch|ps5|xbox)|dev ?kit|platform holder)",
        r"(certifikac|port na konzol|devkit)",
    ),
    "version-control": (
        r"(perforce|\bp4v\b|version control|source control|git ?lfs)",
        r"(Perforce|verzován|version control|Git LFS)",
    ),
    # Praxe candidates from batches 50–56 (scan 2026-10-11)
    "cellular-automata": (
        r"(cellular automat|game of life|conway)",
        r"(celulární automat|Game of Life|cellular automat|Conway)",
    ),
    "pcgex": (
        r"(pcg ?ex\b|pcgex|pcg extended)",
        r"(PCGEx|PCG Ex\b)",
    ),
    "geometry-script": (
        r"(geometry script|dynamic mesh)",
        r"(Geometry Script|dynamic mesh)",
    ),
    "ps1-affine-jitter": (
        r"(affine (texture|mapping)|texture (warp|wobble)|vertex (jitter|snapping|wobble))",
        r"(afinn|affine|vertex (jitter|snapping|wobble)|třes.{0,20}vrchol|chvěn.{0,20}vrchol)",
    ),
    "ue-modeling-blockout": (
        r"(modell?ing mode|cube grid|modell?ing tools)",
        r"(Modeling Mode|Cube Grid|modeling tools|modelovací režim)",
    ),
    "combat-lockon-parry": (
        r"(lock[- ]on|target lock|\bparry|parrying)",
        r"(lock-on|zamykání cíle|\bparry|odražení útoku)",
    ),
    # Teorie (scan 2026-10-11)
    "economy-balancing": (
        r"(game economy|in-?game economy|economy design|(currency|resource) sinks?|sinks? and sources?"
        r"|sources? and sinks?|balanc(e|ing) (the |your )?(game|economy|numbers|stats)|power curve)",
        r"(herní ekonomik|ekonomik.{0,20}hry|vyvažován|balancován|power curve|\bsinky?\b)",
    ),
    "randomness-rng": (
        r"(randomness|\brng\b|random number|loot table|drop rate|pity (timer|system)|(input|output) random)",
        r"(náhodnost|náhodn[éáý] (prvk|generov|výsled|odměn)|\bRNG\b|loot table|drop rate|\bpity\b)",
    ),
    "onboarding-tutorial": (
        r"(onboarding|tutorial (design|level|section|stage)|teach(ing)? the player|\bftue\b)",
        r"(onboarding|tutoriál.{0,20}(design|úrov|ve hře|sekc)|naučit hráče|učí hráče|\bFTUE\b)",
    ),
    "ux-hud-design": (
        r"(user experience|\bux\b|hud design|\bui design|user interface design|information hierarchy)",
        r"(\bUX\b|návrh (HUD|rozhraní)|UI design|HUD design)",
    ),
    "pricing-monetization": (
        r"(pricing|price point|free[- ]to[- ]play|\bf2p\b|microtransaction|monetiz|in-app purchase)",
        r"(cen(a|ou|u|y) hry|cenotvorb|free-to-play|\bF2P\b|mikrotransak|monetiz)",
    ),
    "community-marketing": (
        r"(discord (server|community)|community (building|management|manager)|influencer|streamers?"
        r"|content creators?|press kit|next fest)",
        r"(budování komunity|komunit[ay] (kolem|hry|hráčů)|Discord server|influencer|streamer|press kit|Next Fest)",
    ),
    "puzzle-design": (
        r"(puzzle design|designing puzzles|design(ing)? a puzzle|good puzzles?|puzzle games?)",
        r"(puzzl|hádank|hlavolam)",
    ),
    "quest-branching": (
        r"(quest design|side ?quests?|branching (dialogue|narrative|story|paths)|dialogue tree|choices that matter)",
        r"(quest|vedlejší úkol|větven.{0,20}(příběh|dialog)|dialogov.{0,10}strom)",
    ),
    "player-motivation": (
        r"(bartle|player types|self[- ]determination|intrinsic motivation|extrinsic motivation|skinner box|compulsion loop)",
        r"(Bartle|typy hráčů|vnitřní motivac|vnější motivac|Skinner|compulsion loop)",
    ),
    "legal-contracts": (
        r"(publisher (deal|contract|agreement)|\bcontracts?\b|lawyer|trademark|copyright|revenue share|recoup)",
        r"(smlouv|právník|ochrann.{0,5} známk|autorsk.{0,10}práv|revenue share|recoup)",
    ),
    "team-collaboration": (
        r"(freelancers?|outsourc|hiring (a|an|people)|working with (artists|programmers|a team)|team communication)",
        r"(freelanc|outsourc|najmout|najímá|spoluprác.{0,20}týmu|komunikac.{0,20}týmu)",
    ),
    # Godot (scan 2026-10-11)
    "godot-3d": (
        r"(meshinstance3d|node3d|worldenvironment|characterbody3d|\bcsg|godot.{0,40}\b3d\b|\b3d\b.{0,40}godot)",
        r"(Node3D|MeshInstance3D|WorldEnvironment|CharacterBody3D|Godot.{0,40}\b3D\b|\b3D\b.{0,40}Godot)",
    ),
    "godot-shaders": (
        r"(shader_type|visual ?shader|canvas_item|godot shader|gdshader)",
        r"(shader_type|Visual ?Shader|canvas_item|gdshader|shader.{0,30}Godot)",
    ),
    "godot-physics": (
        r"(rigidbody[23]d|characterbody[23]d|area[23]d|collision (layer|mask)|staticbody|move_and_slide)",
        r"(RigidBody|CharacterBody|Area[23]D|collision (layer|mask)|kolizní (vrstv|mask)|StaticBody|move_and_slide)",
    ),
    "godot-save-load": (
        r"(configfile|fileaccess|user://|resourcesaver|json\.(stringify|parse_string))",
        r"(ConfigFile|FileAccess|user://|ResourceSaver|JSON\.stringify)",
    ),
    "godot-audio": (
        r"(audiostreamplayer|audio ?bus|audioserver)",
        r"(AudioStreamPlayer|audio ?bus|AudioServer)",
    ),
    "godot-export-steam": (
        r"(godotsteam|godot.{0,30}steam|export templates?|web export|html5 export)",
        r"(GodotSteam|export templat|exportní šablon|web export)",
    ),
    "godot-navigation": (
        r"(navigationagent[23]d|navigationregion[23]d|astar2d|astargrid|navigation ?server)",
        r"(NavigationAgent|NavigationRegion|AStar2D|AStarGrid|NavigationServer)",
    ),
    "godot-tool-plugins": (
        r"(@tool\b|editorplugin|tool script|\btool keyword)",
        r"(@tool\b|EditorPlugin|tool skript)",
    ),
    "godot-csharp": (
        r"(c#.{0,40}godot|godot.{0,40}c#|godot \.net|godot mono)",
        r"(C#.{0,40}Godot|Godot.{0,40}C#)",
    ),
}


def scan(pattern, paths, recursive=False):
    hits, files, top = 0, 0, []
    for f in glob.glob(paths, recursive=recursive):
        try:
            text = open(f, encoding="utf-8", errors="ignore").read().lower()
        except OSError:
            continue
        n = len(re.findall(pattern, text, re.I))
        if n:
            hits += n
            files += 1
            top.append((n, os.path.basename(f).removesuffix(".txt")))
    return hits, files, sorted(top, reverse=True)[:3]


def main():
    keys = [k for k in TOPICS if not sys.argv[1:] or any(a in k for a in sys.argv[1:])]
    print(f"{'topic':24} {'corpus':>14}  {'docs':>10}   top sources")
    print("-" * 92)
    for k in keys:
        cpat, dpat = TOPICS[k]
        ch, cf, ctop = scan(cpat, CORPUS)
        dh, df, _ = scan(dpat, DOCS, recursive=True)
        src = ", ".join(f"{v}({n}x)" for n, v in ctop) or "—"
        print(f"{k:24} {ch:6}/{cf:<3} videos  {dh:4}/{df:<3} ch.   {src}")
    print(
        "\nRule of thumb: corpus under ~15 hits with no source above ~5 = genuinely absent,"
        "\nfetch new sources. Corpus rich but docs thin = re-read pass, no download needed."
    )


if __name__ == "__main__":
    main()
