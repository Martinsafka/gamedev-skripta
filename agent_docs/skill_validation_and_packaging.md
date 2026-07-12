# Skill validation & packaging — handoff (pro navazující sezení, psáno pro Opus 4.8)

> **Kontext:** Oba skilly (`.claude/skills/concept-audit/`, `.claude/skills/mechanic-mentor/`) napsal Fable 5
> podle briefů `concept_audit_skill.md` a `mechanic_mentor_skill.md`. Concept-audit prošel plnou kalibrací
> (3 sólo případy s předregistrovanými kritérii + 3 společné audity reálných dokumentů, verdikt uživatele).
> Mechanic-mentor prošel jen lehkou sondou (kroky 0–3, 6/6). **Záměr uživatele: validovat, že skilly drží
> kvalitu i pod jiným modelem než tím, který je napsal.** Ty jsi ta validace. Postupuj dle `workflow.md`
> (analyze → propose → execute → log) a šetři tokeny: tenhle dokument + SKILL.md souborů je celý potřebný
> kontext, nečti historické transkripty.

## Úkol A — held-out validace concept-audit (Phase 5, krok 3)

> ✅ **HOTOVO 2026-07-12 (Opus 4.8).** Tři held-out dokumenty přes `/concept-audit` prošly (KYRRÖ nekompletní nástřel; The Seeker Mount Stupid + právní/platformní catch; Race'n'Chase reálný DMA doc 1995 → GTA). Tři opravy zapracované do skillů (čeština „proč na tom záleží"; otázka nese vlastní routing; viditelné URL místo `[label](url)` — i v mechanic-mentoru). Audity v gitignored `audits/`. Detaily v `dev_log.md`. **Úkoly B a C vědomě odloženy — projekt zakonzervován.**

1. Uživatel vloží syrový nápad ze šuplíku (přímo v dialogu, přes `/concept-audit`). Nijak ho předem nečisti.
2. Řiď se výhradně SKILL.md — sekce v pevném pořadí, nálezy jako trojice + otázka, síly explicitně, žádné verdikty,
   žádné autorování. Odkazy jen z `references/chapter-map.md` (nejsi-li si jistý, ověř proti živému webu).
3. Po dodání auditu nabídni uložení do `audits/` (gitignored). Soudcem kvality je uživatel.
4. Co uživatel u předchozích auditů oceňoval: audit „trochu bolí" — pojmenovává nezapsané («co není zapsané,
   není rozhodnuté»), pokládá otázky, které mění plán; a NIKDY nevymýšlí problémy v silných místech.
5. Známé pasti (chytané při kalibraci): měkké výroky o autorovi (pravidlo 5 — kotvit k omezením projektu),
   vymýšlení obsahu za autora (tvrdý fail), verdiktový slovník.

## Úkol B — validace mechanic-mentor

1. Lehká sonda už proběhla; plná validace = reálná session s uživatelem nad skutečnou mechanikou (ideálně z IZBY).
2. Drž smyčku ze SKILL.md (0–9). Nejčastější rizika: (a) sklouznutí k hotové architektuře místo otázek — pravidlo 3;
   (b) oprava závěru místo úvahy — pravidlo 4; (c) zapomenutý devlog — zakládá se hned při intake a píše průběžně;
   (d) vynechaný exit gate (counterfactuals) — mechanika není „hotová" bez něj.
3. Kalibrační sonda pro rychlý self-check (z briefu): vstup „chci, aby se postava schovala pod postel" musí vést
   na otázky o fázích (vstup/pobyt/výstup), o hranici geometrie vs. deklarace a mechanism vs. policy — ne na hotový
   návrh. Kritéria: `mentor-00-criteria.md` ve scratchpadu původního sezení; přepiš si je vlastní, budou-li nedostupná.

## Úkol C — balíčkování a publikace (Phase 5, krok 4) — až po úspěšných A + B

Formáty ověřené proti oficiální dokumentaci (code.claude.com/docs: skills.md, plugins.md, plugin-marketplaces.md).

**Doporučená struktura: jeden plugin se dvěma skilly** (sdílejí knihovnu, chapter-map, feedback kanál i cílovku;
dva pluginy = dvojí instalace bez přínosu — rozhodnutí může uživatel zvrátit):

```
plugins/gamedev-skills/
├── .claude-plugin/plugin.json
└── skills/
    ├── concept-audit/      ← kopie z .claude/skills/concept-audit/
    └── mechanic-mentor/    ← kopie z .claude/skills/mechanic-mentor/
```

`.claude/skills/` zůstává zdrojem pravdy pro vývoj v tomhle repu; do `plugins/` se kopíruje při releasu
(přidej kopírovací krok do `scripts/build_chapter_map.py`, nebo malý `scripts/package_skills.py`).

**plugin.json (minimum):**
```json
{ "name": "gamedev-skills", "description": "Concept audit + mechanic mentor nad knihovnou gamedev-skripta", "version": "0.1.0" }
```
(Vynechané `version` = commit SHA; pro první release radši explicitní.)

**Marketplace = tenhle repozitář.** Do kořene přidat `.claude-plugin/marketplace.json`:
```json
{
  "name": "gamedev-skripta",
  "owner": { "name": "Martin Šafka" },
  "plugins": [
    { "name": "gamedev-skills", "source": "./plugins/gamedev-skills", "description": "Audit herních konceptů a mentor mechanik — nálezy směrují do skript" }
  ]
}
```

**Instalace pro uživatele (do README, česky):**
```
/plugin marketplace add Martinsafka/gamedev-skripta
/plugin install gamedev-skills@gamedev-skripta
```
Po instalaci se skilly volají `/gamedev-skills:concept-audit` a `/gamedev-skills:mechanic-mentor` (namespace pluginu).

**Kontroly po zabalení:** (1) oba SKILL.md se načtou (objeví se v seznamu skillů po instalaci z lokální cesty:
`/plugin marketplace add ./` v testovacím adresáři); (2) `${CLAUDE_SKILL_DIR}` cesty fungují uvnitř pluginu
(templates/, references/ jsou v kopii); (3) chapter-map je čerstvá (`scripts/build_chapter_map.py` před releasem);
(4) žádný odkaz nevede na neexistující slug (anchor-check proti buildu). Pak commit + tag verze.

**Nezapomenout (drobnosti mimo balíček):** `gh label create library-gap` na GitHubu (issue linky ze skillů
štítek předpokládají; bez něj se tiše zahodí — issue vznikne i tak). README sekce o skillech.

## Invarianty, které platí pro všechno výš

- Slugy a anchory webu jsou public API (architecture.md → „Public URL contract") — nikdy nepřejmenovávat.
- Skilly neembedují obsah kapitol — jen odkazy; po přidání kapitol regenerovat mapu.
- `audits/`, `inbox/`, `transcripts*/` zůstávají gitignored; skilly a `plugins/` se commitují.
- Každý úkol → záznam do `agent_docs/dev_log.md`; commit message navrhnout, commituje uživatel.
