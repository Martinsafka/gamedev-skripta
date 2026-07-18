# Rady z praxe: idea iceberg a meta-pravidla

Kapitola o radách zkušených — a o tom, jak rady číst. Jádro tvoří „idea iceberg" z Isto Inc.: komerční úspěch hry rozhoduje nápad víc než exekuce a kvalitu nápadu jde číst jen do hloubky, ve vrstvách. K němu přibyly dvě novější vrstvy: proč rady na design vlastně nefungují jako recepty (a co místo nich) a kompilace návyků od profíků od Fruit Ninja po sólo devlogery. Kapitola sedí vedle [žroutů času](produktivita.md): tam šlo o to nedělat zbytečnou práci, tady o to nedělat skvělou práci na špatném nápadu — a nečekat, že ti někdo nadiktuje, jak na to.

---

## Nápad rozhoduje víc, než je vidět na hladině

**Zdroj:** [The Game Dev Advice That Took 10 Years to Discover](https://www.youtube.com/watch?v=12tZyCMIYbg) · [Isto Inc.](https://www.youtube.com/channel/UCgpGbh7d0X3-RBVYC4MQEEw) · ~16 min, esej z desetileté praxe

**Shrnutí:** Hra s jankovitou fyzikou, ohlušujícím voice chatem a placeholder logem prodala milion kopií za týden — protože fantazie, kterou slibuje, je pro hráče důležitější než bugy. Obráceně: autorova první hra měla téměř pětihvězdičkové recenze a vydělala 7 centů na hodinu. Slabý nápad nekonvertuje, ani když je hra skvělá.

### Rozpad myšlenky

Iceberg [(0:12)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=12s): na hladině vypadají všechny nápady stejně — „minimalistická puzzle hra", „automatizační hra" — a jestli je pod nimi milion dolarů, nebo propadák, vidí jen ten, kdo se umí podívat pod vodu. Hloubka pohledu roste ve vrstvách:

1. **Kontext hráče** [(1:52)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=112s) — čím víc her znáš, tím víc vidíš: kdo hraje klony Vampire Survivors, ví, které mechaniky v žánru chybí. Prerekvizita, kterou má každý vývojář.
2. **Skill** [(3:07)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=187s) — nápad je dobrý, jen pokud ho umíš vyrobit [(3:20)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=200s): open-world extraction shooter je skvělý nápad pro tým o 350 lidech. S rostoucím skillem se rozšiřuje bazén nápadů, které jsou pro tebe viabilní.
3. **Market research** [(4:24)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=264s) — první krok k objektivitě. Žánr má tvrdou váhu: medián výdělků napříč žánry se liší násobně [(5:25)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=325s) — i top 1 % puzzle her vydělává zlomek top 1 % simulací. Autor: hrál jsem a bavilo mě dělat hry víc žánrů — tak proč si sázet proti sobě?
4. **Externí validace** — samostatná myšlenka níže.
5. **Intuice** [(15:24)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=924s) — neměřitelná vrstva, která se brousí jen děláním her; s ní dopadají mikro-rozhodnutí blíž cíli.

Autorova kariéra je ilustrace vrstev: Disjoint (vrstva 2 — „super cool nápad", 7 centů/hod [(3:59)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=239s), vzor „skvělé recenze, mizerné prodeje" [(4:13)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=253s)), Atrio (vrstva 3 — dva žhavé žánry, výrazně lepší výsledek, ale mix žánrů poškodil appeal), Get to Work (vrstva 4).

> **Pozn.:** Data o žánrech pocházejí z veřejných zdrojů, které video jmenuje: Steamové roční žebříčky, SteamDB a benchmarky Chrise Zukowského (howtomarketagame.com) — použitelné hned, bez placení.

**Souvislosti:** [Nápad](napad.md) · [Žrouti času](produktivita.md) · [Rejstřík: market research](../rejstrik.md#market-research)

---

## Pracuj zpátky: jak brzy jde poznat, že by hru někdo koupil

**Zdroj:** [The Game Dev Advice That Took 10 Years to Discover](https://www.youtube.com/watch?v=12tZyCMIYbg) · [Isto Inc.](https://www.youtube.com/channel/UCgpGbh7d0X3-RBVYC4MQEEw) · stejné video, jádro metody

**Shrnutí:** Jediná otázka, na které záleží: *koupili by lidé tuhle hru?* Autorovo cvičení „work back" hledá nejranější okamžik, kdy na ni jde dostat odpověď — a končí u pitch decku pro hru, která ještě neexistuje. Čím dřív měříš, tím míň konkrétní je důkaz, ale tím levnější je otočit.

### Rozpad myšlenky

Work back [(7:15)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=435s) jde od jistoty k užitečnosti: milion prodejů první týden je 100% důkaz — a je k ničemu, přichází po letech práce. Milion wishlistů den před vydáním [(7:48)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=468s): ~95% jistota, pořád pozdě. Úspěch na Steam Next Festu: silný signál, ale to už se ladí gameplay, ne nápad. Virální trailer či populární devlogy: indikátor zájmu — jenže po dvou letech vývoje už couvnout neumíš; sunk cost fallacy ti našeptává, že se to zlepší [(8:58)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=538s). Rané playtesty: důkaz slábne, manévrovatelnost roste.

A úplně vlevo na časové ose: **pitch deck neexistující hry** [(12:16)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=736s) — podle autora největší game-changer jejich studia. Logika: první krok nákupu hry stejně neobsahuje hraní — je to trailer, GIF, screenshot (Silksong prodával bez dema; Choo Choo Charles prodal trailer). Pitch deck tenhle moment simuluje. Proces studia [(13:19)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=799s): brainstorm → hlasování → u top nápadů zkusit popsat herní smyčku (slabé se rozpadnou samy) → pitch decky → ukázat lidem. Dvě opory metody: lidé jsou skvělí ve *vybírání* nejlepší varianty a mizerní v radách, jak věc zlepšit [(13:51)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=831s); a deck za hodinu se zahazuje bez bolesti, prototyp za týden už bolí [(14:02)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=842s) — méně vloženého času = méně biasu.

Poctivé limity, které video samo přiznává: některé hry (Balatro) pochopíš až hraním — tam rovnou prototyp; malý vzorek hlasujících; testuješ jen svůj bazén nápadů, ne trh. I tak: minimálně zjistíš, které nápady jsou *srozumitelné*, a donutí tě to formulovat, čím je každá hra výjimečná.

> **Pozn.:** Klíčová věta celého videa: „čím dřív jsme začali validovat, tím lépe hra dopadla." To je testovatelná hypotéza pro vlastní projekty — a příjemně skromný závěr: autor sám dodává, že jejich studio není žádný mega-hit, ber s rezervou.

**Souvislosti:** [Prototypování](prototypovani.md) · [Postmortem ShantyTown: wishlisty](postmortem-shantytown.md#wishlisty-next-fest-a-ticho-po-launchi) · [Rejstřík: pitch deck](../rejstrik.md#pitch-deck)

---

## The Gap: rozdíl mezi „to je hezký" a „tohle musím hrát"

**Zdroj:** [The Game Dev Advice That Took 10 Years to Discover](https://www.youtube.com/watch?v=12tZyCMIYbg) · [Isto Inc.](https://www.youtube.com/channel/UCgpGbh7d0X3-RBVYC4MQEEw) · stejné video, interpretace zpětné vazby

**Shrnutí:** Co lidé říkají a co dělají jsou dvě různé měny. „The gap" je autorův název pro propast mezi zdvořilým zájmem a skutečnou touhou — mezi wishlistem a nákupem. Číst se dá jen z chování: playtesteři, kteří si o nové buildy říkají sami, jsou jiný signál než ti, které musíš přemlouvat.

### Rozpad myšlenky

Autor to viděl na vlastních hrách [(9:40)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=580s): u Atria lidé rádi testovali, někteří hru milovali. U Get to Work bylo něco jinak [(10:12)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=612s) — testeři *otravovali*, kdy bude nový build [(10:26)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=626s). Ten nárůst vynaloženého úsilí je celý signál: slova jsou zdvořilá, chování je drahé, a proto pravdivé.

Introspektivní kalibrace, kterou video nabízí [(10:55)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=655s): vzpomeň si, kdy byla hra pro tebe day-one jasný nákup — co jsi dělal, jak to vypadalo zevnitř — a tohle hledej u svých playtesterů. A počítej s tím, jak *málo často* se ti to stává: pokora ohledně toho, jak těžké je lidi skutečně nadchnout, je součást metody.

Pro měřitelnost bez vibes video přidává postup jiného vývojáře [(11:32)](https://www.youtube.com/watch?v=12tZyCMIYbg&t=692s): účastnit se game jamů a srovnávat výkon prototypů mezi sebou i proti ostatním hrám jamu — playtime dem a lajky na itch.io jako hrubý žebříček zájmu. Funguje to nejlíp s větším počtem vydaných prototypů; benchmark hodnoty playtime nabízí i Zukowski.

> **Pozn.:** The gap je protějšek [shovívavého publika](zacatky-bez-zkusenosti.md#sdileni-prace-neni-marketing-je-to-nastroj-uceni) ze začátků: tam jsme si laskavé publikum *přáli* (pro motivaci), tady se ho učíme *diskontovat* (pro rozhodování). Obě dovednosti potřebuješ — každou v jiné fázi.

**Souvislosti:** [Začátky bez zkušeností](zacatky-bez-zkusenosti.md) · [Žrouti času: validace](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) · [Rejstřík: playtest](../rejstrik.md#playtest) · [Rejstřík: wishlist](../rejstrik.md#wishlist)

---

## Rady nefungují tam, kde začíná design

**Zdroj:** [Stop Looking For Game Dev "Advice"](https://www.youtube.com/watch?v=d5VdFScmXcM) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~19 min, meta-esej o učení designu

**Shrnutí:** Didaktické učení — někdo ti říká fakta a postupy — funguje skvěle na **hard skills** s měřitelným výstupem (kód, obrázek). Design je ale svazek **soft skills**: úsudek, analýza, empatie [(2:08)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=128s). Ty se učí objevováním — hraním, rozborem, workshopem — a proto hledání „pravidel game designu" vede do slepé uličky: chceš derisknout kreativitu, která se derisknout nedá [(6:06)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=366s).

### Rozpad myšlenky

Past vzniká nenápadně [(1:22)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=82s): začátečník se roky učí engine z tutoriálů (didaktika je tam správný nástroj) a vytvoří si rovnici „vzdělávání = někdo mi říká, co dělat". Když pak někdo učí design nepřímo — otázkami, rozborem, „wafty artsy" řečmi — působí to jako ne-vzdělávání [(4:34)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=274s). Jenže pasivita je pravý opak designérské mentality; autor sám přiznává vlastní fázi hltání teorie a podcastů ze strachu a nejistoty v první studiové práci [(6:06)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=366s).

Tvrdší část: **sólo vývoj je leadership role** [(5:20)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=320s), i v týmu o jednom. Z mentoringu autor vidí pořád totéž — lidem nechybí hard skills, chybí **sebedůvěra udělat rozhodnutí a stát si za ním** [(8:12)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=492s). Říct „chci půl hodiny tvé pozornosti místo knih a dětí" je psychologicky dominantní pozice hostitele [(9:47)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=587s) — a hráči indie her si tu osobní vizi výslovně přejí; kdo o creative direction nestojí, nemá důvod dělat hru sólo [(10:34)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=634s). Zkratka neexistuje: design se učí trial & error a nejblíž zkratce je raná validace a diskuse [(12:08)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=728s).

A jedna okamžitě použitelná rada na závěr [(12:46)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=766s): **fanouškovská kultura tvého žánru je učebnice designu.** Gaming YouTubeři a subreddity rozebírají, co hráče na žánru baví — a spousta nepovedených klonů vznikla jen proto, že vývojář tohle nikdy nečetl [(13:32)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=812s). „Design je empatie" [(14:18)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=858s): extrahovat z diskusí, kde přesně vzniká zábava, je trénink — domácí úkol videa zní najít play-based zdroje svého žánru a dělat si poznámky [(15:05)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=905s).

> **Pozn.:** Pro tahle skripta je to zdravá sebekritika: knihovna je plná didaktiky. Správné použití je jako u [rešerše](proc-tvorit.md#prazdne-platno-zacni-rychle-ale-resersuj-bez-studu) — opora před skokem, ne náhrada skákání. Video je jinak výstavní kus kanálového humoru: obsahuje Patreon tier za 10 000 liber měsíčně, za který autor přestane tvořit obsah [(6:52)](https://www.youtube.com/watch?v=d5VdFScmXcM&t=412s).

**Souvislosti:** [Učení v éře AI](uceni-v-ere-ai.md) · [Jak se učit kódovat](jak-se-ucit-kodovat.md) · [Zábava a flow](zabava.md) · [Rejstřík: Soft skills](../rejstrik.md#soft-skills)

---

## Kompilace od profíků: čti problém za návrhem, ukazuj brzy, ožeň se s hrou

**Zdroj:** [The Game Dev Advice You Actually Need (Ft. AIA, Goodgis, and more...)](https://www.youtube.com/watch?v=n3fjdwJ5eQk) · [Juniper Dev](https://www.youtube.com/channel/UChzRJQ-MbpcIxFT5YLW1R9w) · ~14 min, kompilace rad tvůrců

**Shrnutí:** Sedm tvůrců, sedm návyků — a tři z nich jsou nosné: zpětná vazba hráčů jsou *návrhy skrývající problém*, hru je třeba ukazovat dřív, než je hotová, a jednou vybranému projektu se slibuje věrnost. Zbytek jsou řemeslné drobnosti, které se sčítají: večerní to-do list, ladění „nadoraz", Git a čistý kód tam, kde zrychluje obsah.

### Rozpad myšlenky

**Čti problém za návrhem** (vývojářka Aia, Mana Valley [(0:01)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=1s)): hráči chtěli regeneraci zdraví; místo toho dostala hra léčení mimo souboj po 30 sekundách — průzkum je plynulejší a lektvary zůstaly vzácné [(0:48)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=48s). Obecný vzorec: „postava je pomalá" může znamenat friction, gravitaci nebo skrytý modifikátor, který tester nevidí [(1:34)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=94s) — **testeři výborně identifikují problémy a mizerně navrhují řešení**; řešení má sedět do tvé vize. (Rozšiřuje [the gap](rady-z-praxe.md#the-gap-rozdil-mezi-to-je-hezky-a-tohle-musim-hrat): tam šlo o čtení nadšení, tady o čtení kritiky.)

**Trojice od Luka Muscata** (Fruit Ninja, Jetpack Joyride; 18 let praxe [(1:34)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=94s)): (1) poslední úkon dne = to-do list na zítřek, s krátkou snadnou položkou na rozjezd [(2:20)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=140s); (2) návyk z Halfbrick — při ladění proměnné ji nejdřív změň **10–100×**, ať víš, že ladíš správnou věc [(3:06)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=186s); (3) a největší: **ukazuj hru komukoli, kdykoli, i nehotovou** — „not ready" je výmluva a čím později ukážeš, tím dražší je cokoli měnit; „do not let your game be in the darkness" [(3:52)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=232s).

**Ožeň se s hrou** (Goodgis [(4:38)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=278s)): v prototypové fázi je opouštění projektů zdravé — ale po rozhodnutí platí závazek, protože **dovednosti z dokončování jinde nepotkáš** a dokončení nikdy nelituješ. Až přijde zamilovanost do nového nápadu, „vzpomeň si, že máš prsten". Doplňky ze zbytku kompilace: verzování a cloud zálohy všeho (Challacade; „crash disku je horor" [(6:56)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=416s)); poznámky jako „organizovaný chaos" — nápad na papíře vypadá dokonale, zábavnost ukáže až implementace [(9:17)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=557s); test tématu — „podporuje tahle feature message mé hry?" (horor bez monster, o pocitu invaze do cizího počítače [(10:03)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=603s)); a čistý kód ne jako dogma, ale tam, kde **zrychlí přidávání obsahu** — refactor ability systému na data-driven místo brute-force padesáti schopností [(12:22)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=742s).

> **Pozn.:** Video obsahuje sponzorský segment (Xsolla) [(6:10)](https://www.youtube.com/watch?v=n3fjdwJ5eQk&t=370s) — přeskočen. A poznámka k jednomu bez přepisu: šestiminutová zpověď [I Wasted 6 Years Making Games…](https://www.youtube.com/watch?v=jDPxHf_6KuI) ([Sunny Gamedev](https://www.youtube.com/channel/UCJjOwQWrlEdym9MRIqCXaTA)) říká z opačného konce totéž co Goodgis — autor šest let věřil, že potřebuje větší nápad, lepší grafiku a víc features, a skutečná lekce bylo dokončování. Kryto z popisu videa (anglický přepis není k dispozici), proto bez timestampů.

**Souvislosti:** [Produktivita: motivace a dokončování](produktivita.md) · [Organizace projektu: Git](../praxe/organizace-projektu.md) · [Zápisek: Cut line](../zapisky/cut-line.md) · [Rejstřík: Version control](../rejstrik.md#version-control)
