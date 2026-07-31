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
