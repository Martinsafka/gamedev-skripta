# Vedení hráče: scripted events a recall priming

Dvě techniky, kterými level designér řídí hráčův zážitek, aniž by mu cokoli řekl napřímo: **scripted events** rozhodují, *kdy* se věci stanou, a **recall priming** rozhoduje, *co si hráč v pravou chvíli vybaví*. Obě pracují s toutéž měnou — hráčovou pozorností — a obě jsou neviditelné přesně tehdy, když fungují.

---

## Scripted events: věci se mají stát ve správnou chvíli

**Zdroj:** [How AAA Level Designers Create Gameplay Moments](https://www.youtube.com/watch?v=tRBGGuh1ajY) · [Gabriel Fuentes](https://www.youtube.com/channel/UCvbm6PppZ3gmIyznJPayhSA) · ~5 min, breakdown z vlastního projektu

**Shrnutí:** Level design nejsou jen layouty a combat prostory — velká část řemesla je režie momentů: skriptované události, které se spustí, když hráč splní podmínku [(0:34)](https://www.youtube.com/watch?v=tRBGGuh1ajY&t=34s). Bez nich je level statická kulisa, která na hráče nereaguje; s nimi má pacing, příběhové beaty a překvapení. Cíl není, aby se věci děly náhodně — ale ve správný čas [(1:28)](https://www.youtube.com/watch?v=tRBGGuh1ajY&t=88s).

### Rozpad myšlenky

Základní nástroj je **trigger volume** [(0:39)](https://www.youtube.com/watch?v=tRBGGuh1ajY&t=39s): hráč vstoupí do zóny → něco se stane. Co přesně, je paleta level designéra: rozhovor NPC, změna hudby, otevření cesty, cinematika. Video ukazuje tři vzory použití:

- **Vyprávění bez zastavení hry** [(1:37)](https://www.youtube.com/watch?v=tRBGGuh1ajY&t=97s): vstup na tržiště spustí konverzaci NPC — hráč jde dál, svět působí živě a expozice přichází mimochodem, ne v cutscéně, která mu sebere ovládání.
- **Audio jako informační kanál** [(2:10)](https://www.youtube.com/watch?v=tRBGGuh1ajY&t=130s): stealth hry hrají rozpoznatelný zvuk, když tě nepřítel zahlédne; hudba houstne při nízkém zdraví [(2:30)](https://www.youtube.com/watch?v=tRBGGuh1ajY&t=150s). Hráč většinu přechodů vědomě nezaznamená — a přesto se podle nich rozhoduje (kryj se, ustup, hledej lékárničku), bez jediného UI prvku.
- **Cinematiky v místě, ne v čase** [(3:03)](https://www.youtube.com/watch?v=tRBGGuh1ajY&t=183s): sekvence se spouští, když hráč *dojde* na správné místo — rozhodnutí „kde má ten moment být" je designové, trigger je jen doručovací mechanismus.

Nejcennější rada videa je pořadí otázek [(3:41)](https://www.youtube.com/watch?v=tRBGGuh1ajY&t=221s): začátečníci skočí do Blueprintů; level designér se nejdřív ptá — *jaký zážitek tvořím? co má hráč cítit? jakou informaci dostat? co má udělat dál?* S odpověďmi je skriptování triviální; bez nich je to jen technika bez obsahu. Event slouží zážitku, ne obráceně.

**Souvislosti:** [Recall priming](#recall-priming-nachystej-vzpominku-driv-nez-bude-potreba) níže · [Game feel a imerze](game-feel.md) · [Rejstřík: trigger volume](../rejstrik.md#trigger-volume) · [Rejstřík: pacing](../rejstrik.md#pacing)

---

## Recall priming: nachystej vzpomínku dřív, než bude potřeba

**Zdroj:** [Recall Priming as a Level Design Technique](https://www.youtube.com/watch?v=Y2QBzdaMAAI) · [TimDoesLevelDesign](https://www.youtube.com/channel/UCTjhFJvDYh1uWT0705LAKFg) · ~5 min, technika s praktickou ukázkou

**Shrnutí:** Hráči se u puzzlů nezasekávají proto, že jsou hloupí, ale proto, že si v pravou chvíli nevybaví správný nástroj [(0:12)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=12s). Recall priming = rozmístit do prostředí nenápadné nápovědy, které potřebnou vzpomínku aktivují těsně před tím, než ji hráč bude potřebovat. Hráč se nezasekne — a řešení si připíše sám sobě.

### Rozpad myšlenky

Psychologický základ [(0:46)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=46s): informace v hlavě nezmizela, jen k ní chybí klíč — jako když ti reklama na auta připomene, žes nechal klíče v autě [(0:59)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=59s). Selhání téhle paměti ve hrách: Sonic 3 a barel, na kterém hráči hodiny skáčou, místo aby rytmicky mačkali nahoru/dolů [(0:27)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=27s); Crimson Desert a ruiny, kde řešení stojí na mechanice pálení keřů, kterou hra nikde poblíž nepřipomene [(1:24)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=84s) — hráč zkouší desítky schopností a frustrovaně odchází.

Praktická ukázka nápravy [(3:07)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=187s) je učebnicová trojvrstvá kaskáda: puzzle vyžaduje spálit liány pochodní. Před puzzle místnost autor předřadí **tmavou jeskyni** — tma donutí hráče vytáhnout pochodeň; do jeskyně rozmístí **hořlavé liány, do kterých hráč zaručeně vrazí** [(3:22)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=202s) — pochodeň je zapálí a *aktivně* připomene, že oheň pálí vegetaci; a v samotné puzzle místnosti hoří **pochodně na stěnách** [(3:36)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=216s) jako podprahová pojistka. Když hráč dorazí k liánám, řešení „samo" naskočí — a pocit chytrosti patří jemu [(4:08)](https://www.youtube.com/watch?v=Y2QBzdaMAAI&t=248s).

> **Pozn.:** Tohle je mechanismus, proč „zaseknutí na puzzlu" skoro nikdy nespravíš nápovědou v UI — ta pocit chytrosti ukradne. Priming je oprava *prostředím*: neříká řešení, jen zvedá dostupnost správné vzpomínky. Pro stealth adventuru s environmentálním pozorováním je to přímo domácí technika — a krásně se skládá s [tajnými řetězci](smycky-a-retezce.md#retezec-nese-emocni-oblouk): priming řídí, co si hráč vybaví, tajný řetězec odměňuje, že si toho všiml.

**Souvislosti:** [Smyčky a řetězce](smycky-a-retezce.md) · [Prostor: blockout a hranice](prostor-a-hranice.md) · [Rejstřík: recall priming](../rejstrik.md#recall-priming) · [Rejstřík: affordance](../rejstrik.md#affordance)
