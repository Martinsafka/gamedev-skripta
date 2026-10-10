# Content gaps — what to look for next

**Purpose.** The playlists were curated before we knew what the library would need. This file tracks the other direction: topics the documents *should* cover but the corpus can't answer, so the next fetch is driven by a question instead of a playlist.

**Two different problems live here, and mixing them wastes work:**

- **Re-read** — the corpus already has the material, it was just written up from another angle. Costs reading time, no download. Usually the better deal.
- **Fetch** — the corpus genuinely doesn't contain it. Needs a targeted search, a new `fetch_transcripts.sh` run, and a new block of `processing_index.md` rows.

`scripts/gap_scan.py` tells the two apart. Run it before adding or promoting a row:

```
.venv/bin/python scripts/gap_scan.py            # all topics
.venv/bin/python scripts/gap_scan.py ui audio   # only matching keys
```

Rule of thumb it prints: **corpus under ~15 hits with no single source above ~5 → genuinely absent.** Corpus rich but docs thin → re-read, don't download.

## How to maintain this

1. **Add a row** whenever a synthesis batch, an audit, or a reader question surfaces something the library can't answer. A hunch is enough to add it — evidence is what promotes it.
2. **Back it with numbers.** Add the topic's key + regexes to `TOPICS` in `scripts/gap_scan.py`, run it, paste the counts into the Evidence column. Keep the key identical in both files.
3. **Tick it off** in the Status column when the material lands in `docs/`, and name the chapter. A gap is closed by published text, not by downloaded transcripts.
4. **Drop rows honestly.** `✗` with a reason is a valid outcome — some gaps aren't worth filling for a solo-dev audience, and a dropped row saves the next session from re-deciding.

Status: `☐` open · `⏳` sources fetched, synthesis pending · `☑` done (name the chapter) · `✗` dropped (say why)

---

## Table

Evidence format: `corpus hits/videos · docs hits/chapters` as of the last scan (2026-10-10, after the fourth-wave fetch; previous scan 2026-07-31).

| Stav | Téma | Evidence | Kam by to patřilo | Co hledat na YouTube |
|---|---|---|---|---|
| ☐ **P1** | **UI a UMG v UE** | 36/16 · **1/1** | nové téma v Praxi | **Čtvrtá vlna (2026-10-10)** přinesla zdroje jen pro **UI ve světě** — diegetické menu (`CDf-5lp4yxQ`), health bary nad hlavou, cena in-world widgetů → `praxe/ui-ve-svete.md`, dávka 50. Jádro UMG a Common UI dál chybí a nárůst čísel dělají hlavně okrajové zdroje (beginner kurz, automotive HMI). Největší díra v celé Praxi — 57 kapitol a ani jedna o rozhraní. Hledat: `UMG best practices`, `Common UI Unreal`, `UI performance Unreal`, `widget reflector`. Unreal Fest má na tohle přednášky každý rok; Epicova série „Inside Unreal" taky. |
| ☐ **P1** | **PSO a kompilace shaderů** | 13/6 · 9/2 | `praxe/frame-pacing.md` nebo vlastní | Nejčastější příčina škubání ve vydané hře a knihovna o tom neví nic. Hledat: `PSO precaching Unreal Engine`, `shader compilation stutter UE5`, `bundled PSO cache`. Pozor na stáří — do 5.2 to fungovalo jinak, ber jen 5.3+. |
| ☐ **P1** | **Blueprint proti C++: cena** | **8/8** · 1/1 | `praxe/principy-architektury.md` | Otázka, kterou položí každý začátečník, a korpus na ni nemá odpověď. Hledat: `blueprint vs c++ performance`, `blueprint nativization` (pozor: zrušená featura, ber jako historii), `blueprint VM overhead`. Ideálně zdroj s měřením, ne s názorem. |
| ☐ P2 | **Zvuk: implementace v UE** | **2/1** · 17/5 | rozšířit `hudba/sound-design-ve-hre.md` nebo nové v Praxi | Knihovna umí zvuk *vyrobit*, ne *zapojit*. Hledat: `MetaSounds tutorial`, `Wwise Unreal integration`, `sound concurrency Unreal`, `audio optimization UE5`. MetaSound je nativní, začal bych tam. |
| ☐ P2 | **Automatizované testy a QA** | **6/3** · 3/1 | `teorie/programatorske-navyky.md` | CI/CD v knihovně je, testy ne. Hledat: `Unreal automation testing`, `functional tests UE5`, `Gauntlet framework`. Pro sólo vývojáře stačí úzký záběr: smoke test na zabalený build. |
| ☐ P2 | **Doba buildu a iterace** | **12/8** · 3/1 | `praxe/organizace-projektu.md` | Čtvrtá vlna: `BJ8gQQmJJ-U` (Project Health, Epic) bere iterační časy a CI/CD jako ukazatel zdraví projektu → `organizace-projektu.md`, dávka 48 — ukazatel, ne postup. Čas, který sólo vývojář ztrácí nejvíc a nikdy ho neměří. Hledat: `Unreal cook time optimization`, `DDC shared cache`, `iteration time Unreal`, `live coding UE5`. |
| ☐ P2 | **Mobil a slabý hardware** | 34/22 · 7/7 | `praxe/rozpocet-snimku.md` | Čtvrtá vlna: jedna případovka — `Pkd7-ouyb-M` (2XKO, bojovka pro slabý hardware) → `gpu-pruchod.md`, dávka 48. Rozprostřené zmínky, žádný zdroj to neučí. Steam Deck je pro indie relevantnější než telefon — hledat: `Steam Deck optimization Unreal`, `scalability settings low end`, `mobile renderer UE5`. |
| ☐ P3 | **Lokalizace** | **10/7** · 12/8 | `teorie/vydani-hry.md` | Zmínky ano („lokalizuj do čínštiny, prodá to"), postup ne. Hledat: `Unreal localization dashboard`, `string tables UE5`, `indie game localization workflow`. |
| ☐ P3 | **Přístupnost** | **12/7** · 8/5 | `teorie/obtiznost.md` nebo vlastní | Knihovna to má jen jako typografii a obtížnost. Hledat: `game accessibility guidelines`, `colorblind modes implementation`, `subtitle best practices games`. Existuje kvalitní materiál od AbleGamers a GAConf. |
| ☐ P3 | **Port na konzole a certifikace** | 18/9 · **1/1** | `teorie/vydani-hry.md` | Hledat: `console certification indie`, `porting Unreal to Switch`, `TRC / XR requirements`. Nízká priorita — týká se malé části publika a rychle zastarává. |
| ☐ P3 | **Multiplayer jako téma** | 94/37 · **5/3** | vlastní téma v Praxi | Čtvrtá vlna: `_jRLlTDqoGI` (Chaos Mover v síti — resimulace, input decay) → `mover.md`, dávka 51; pořád spíš vlastnost systému než lekce. Vysoké číslo je klamné: skoro všechno jsou GASP/Mover streamy, kde je replikace *vlastnost*, ne lekce. Hledat: `Unreal replication basics`, `client-side prediction`, `dedicated server indie`. Zvážit, jestli to vůbec patří do dokumentu pro sólo vývojáře. |
| ☑ | **CPU a hlavní vlákno** | 224/23 · 24/10 | `praxe/profiling.md` ×2 | **Re-read, ne fetch** — materiál ležel v přečtených zdrojích (`bfkbwXVMtn8`). Vyšly z toho **dvě myšlenky, ne kapitola**: dvě třetiny odhadované díry už byly napsané v `profiling.md` a `mereni-automaticky.md`, jen jinými slovy, než na jaká se ptal scan. Dávka 46. |
| ✗ | **Editor proti zabalenému buildu** | 24/9 · 15/12 | — | **Falešný poplach.** Při re-readu se ukázalo, že celá spouštěcí sada včetně `-noverifygc` už je v `praxe/gpu-pruchod.md#profilovat-cizi-hru-priprava-ktera-rozhoduje`. Scan to neviděl, protože docs o tom píšou česky jinými slovy. Poučení pro další řádky: **než se řádek povýší na P1, přečti cílovou kapitolu, ne jen počty zásahů.** |
| ✗ | **Verzování v UE (Perforce)** | 63/18 · 45/17 | — | Není to díra. Korpus i dokumenty to pokrývají dost pro sólo vývojáře (`teorie/planovani-nastroje.md`, `teorie/solo-vyvoj.md`); Perforce je nástroj pro tým, ne pro jednoho člověka. |

---

## Two lessons this file exists to prevent

**„Zpracované" není „vytěženo".** 100 % published řádků v `processing_index.md` neznamená 100 % pokrytých témat. Dvouhodinový stream se dá zpracovat na jednu myšlenku a zbytek v něm zůstane ležet. Než se objedná nový fetch, patří se spustit `gap_scan.py` — ten rozdíl uvidí.

**Absence tématu není důkaz, že nechybí.** Playlist byl sestavený dřív, než bylo jasné, co dokument potřebuje; nemůže obsahovat odpovědi na otázky, které v té době nikdo nepoložil. Řádky sem proto patří přidávat i bez důkazu — evidence rozhoduje o pořadí práce, ne o tom, jestli se má díra vůbec zapsat.
