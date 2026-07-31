# Automatizované měření: benchmark, který se spustí sám

Poslední kapitola bloku zavírá kruh k [Profilingu](profiling.md). Ten začínal větou „neodhaduj, měř" — tahle se ptá, co se stane, když se měření **přestane dělat ručně**: když je benchmark součástí buildu, výsledky se srovnávají mezi dny a regrese se najde v okně jednoho changelistu místo za rok.

Tři zdroje ze tří různých úhlů: **jak si postavit vlastní benchmark**, **jak číst Insights systematicky** a **jak trasovat, aniž bys utonul v datech**.

---

## Benchmark z level sequence: měření jako součást práce

**Zdroj:** [Automated Performance Profiling for Local Workflows](https://www.youtube.com/watch?v=bfkbwXVMtn8) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~116 min, Inside Unreal (engine programátor)

**Shrnutí:** Celý stream stojí na jedné ukázce: napsals funkci pohybu, chceš vědět, co stojí — a za pár minut z toho uděláš **opakovatelný test, který se spustí spolu s buildem** a vyplivne trace, tabulku a HTML report. Háček, kvůli kterému se to nedá odbýt nahrávkou hraní: **musí to volat tvůj skutečný kód, ne přehrávat pozice.**

### Rozpad myšlenky

**Tři druhy testu a co se pro co hodí** [(29:39)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=1779s):

| typ | pro co | poznámka |
|---|---|---|
| **statická kamera** | rozpad ceny mapy | *„nejsnadnější na nastavení a největší přínos za vynaložený čas"* — kamery namíříš na nabité oblasti a sleduješ, co s nimi dělá výměna materiálů či LODů |
| **sequence** | gameplay, opakovatelně | volá skutečné funkce, viz níž |
| **replay** | multiplayer | přesná rekonstrukce sezení, ale náročné na údržbu |

**Past, kterou stojí za to znát dřív, než ji nastražíš sám** [(35:55)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=2155s): nejsnazší cesta k opakovatelné sekvenci je **Take Recorder** — nahraješ hraní a přehraješ ho. Jenže *„nezasáhne to gameplay kód, protože se zaznamenávají transformy hráče"*. Chceš-li měřit funkci, kterou jsi napsal, nahrávka pohybu ti k tomu nepomůže.

**Co se dělá místo toho** [(37:29)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=2249s): v level sequence se založí **event track** typu *repeater* a jeho událost **zavolá tu funkci přímo** (v ukázce `Do Move` s hodnotou 1 — tedy totéž, co se stane po stisku šipky vpravo). Pět vteřin sekvence dá při 120 FPS **600 snímků** dat a **každý z nich prošel skutečným kódem**.

**Zbytek už je nastavení**: zapnout plugin *Automated Perf Testing*, v nastavení projektu spárovat mapu se sekvencí a pojmenovat test (jich může být celý seznam — pohyb, skok, střelba), a v **Project Launcheru** přidat k profilu build/cook/run úlohu *automated performance test*. *„Tohle kouzelné tlačítko spustí test, sesbírá data a vygeneruje ti reporty."* Cílová platforma se dá přepnout — takže tentýž test poběží na Androidu nebo na konzoli.

**Co z toho vypadne** [(1:00:34)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=3634s) a proč jsou to tři různé věci:

- **Insights trace** — na aktivní ladění, když víš, co hledáš.
- **Surové CSV** — každý snímek a jeho metriky; rychlejší na zpracování a *„můžeš se soustředit na metriky, které tě zajímají"*. Vhodné pro vlastní skripty.
- **HTML report** — histogram frame time a rozpad herního vlákna. *„Nepotřebuješ Insights, abys viděl trend."* V ukázce: před optimalizací **64 % snímků nad 16 ms**, po ní většina pod 12,5.
- A **logy** — takže když něco spadne, víš kde.

**Vrstva navrch, která z toho udělá zvyk** [(1:05:15)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=3915s): vlastní Python skript projde nasbíraná CSV a vypíše průměry čtyř metrik **napříč dny**. *„Pracuju na té funkci pár dní a chci vědět, jaký je trend."* To je ten rozdíl mezi profilováním jako událostí a profilováním jako součástí práce.

**Dvě věci, které v ukázce zazní mimochodem a nejsou samozřejmé.** Za prvé: nevidíš-li v traci, kde se čas ztrácí, **přidej si vlastní scope** (`TRACE_CPUPROFILER_EVENT_SCOPE`) — jinak tvoje drahá funkce v profileru prostě není. Za druhé: **Insights sám něco stojí**, takže při měření reálných čísel na konzoli se vyplatí pustit jen CSV profiler. *„Když se blížíš plné rychlosti hry, chceš odstranit všechny překážky a dostat číslo, které odpovídá skutečnosti."*

**A rada, kdy s tím začít** [(1:27:08)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=5228s), protože otázka „neoptimalizuji předčasně?" je namístě: nejdřív **cílené testy na věci, které se nebudou měnit** (u bojovky třeba sady pohybů v prázdné mapě — jen animace), a teprve až je první level hotový a stabilní, **jeden pořádný výkonový test**. Uzavře to smířlivě: *„myslíš-li na profilování od začátku a máš plán, jsi napřed před většinou."* Moderátor k tomu přidá dobrý nápad: **spusť to i na skoro prázdném projektu** — dostaneš krajní referenční bod, ke kterému se dá vztahovat všechno, co přibude.

> **Pozn.:** Nejcennější rozlišení celé myšlenky je **nahrávka proti volání**. Take Recorder vypadá jako správná odpověď a u vizuálních testů jí je — ale u gameplay měření je to **měření něčeho jiného, co vypadá stejně**, a to je nejhorší druh chyby v měření vůbec. Sourozenec téhle pasti je [srovnání, ve kterém se liší víc věcí naráz](profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic). Za pozornost stojí i to, jak se tím zavírá kruh z dávky 36: [předávka nálezu](profiling.md#nalez-neni-hotova-prace-predani) končila u Horde dashboardu jako „to nejlepší, co může být" — a tohle je ta samá disciplína **zmenšená na jednoho člověka a jeden den**, což je verze, kterou skutečně nasadíš. Vlastní výhrada k té ukázce: příklad je hodně učesaný (funkce se jmenuje `HeavyWork` a je v ní komentář „optimize me"), což autor sám s humorem přiznává. Realistický zisk je podle jeho vlastních slov **z 8,3 na 8,0 ms**, ne z 16 na 1 — a právě proto se ten trend musí sledovat automaticky, protože po desetinách se ručně měřit nedá.

**Souvislosti:** [Insights jako disciplína](#insights-jako-disciplina-od-symptomu-ke-pricine) · [Tracing bez utopení](#tracing-bez-utopeni-kanaly-sirka-pasma-a-scenare) · [Profiling: nález není hotová práce](profiling.md#nalez-neni-hotova-prace-predani) · [Profiling: reprodukovatelný test](profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic) · [Velké světy: sto tisíc aktérů](velke-svety.md#sto-tisic-akteru-co-unese-editor) *(tytéž photo tools v produkci)* · [Rejstřík: Take Recorder](../rejstrik.md#take-recorder) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights)

---

## Insights jako disciplína: od symptomu ke příčině

**Zdroj:** [Mastering Performance Analysis with Unreal Insights](https://www.youtube.com/watch?v=HQLYkwoDoT4) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~40 min, Unreal Fest Bali 2025 (software engineer, Epic Games Japan)

**Shrnutí:** Přednáška prochází Insights systematicky — od `stat unit` k herní­mu vláknu, render vláknu, GPU, a pak do dvou míst, kam se běžně nedohlédne: **worker vlákna** a **souborové I/O**. Nejcennější není žádný jednotlivý postup, ale opakovaný důraz na jednu věc: **dlouhý pruh v traci často neznamená práci, ale čekání na někoho jiného.** Háček: rozpoznat rozdíl je celá dovednost.

### Rozpad myšlenky

**Postup, který se dá zapamatovat** [(8:51)](https://www.youtube.com/watch?v=HQLYkwoDoT4&t=531s): seřadit snímky podle délky → najít ten nejdelší → přiblížit se na něj → najít vlákno s nejdelším pruhem → v něm nejdelší značku. A hned k tomu výhrada, která je jádrem celé myšlenky: **značky typu *idle* a *wait for task* ignoruj** — jsou to pasivní zdržení, ne práce.

**Pohled na řetěz, ne na jednu položku** [(16:46)](https://www.youtube.com/watch?v=HQLYkwoDoT4&t=1006s). Ukázka, na které je to nejlépe vidět: herní vlákno stihlo snímek za 27,1 ms, **render vlákno za 51,9 ms** — a proto se **další snímek herního vlákna zdrží**. Přednášející tomu říká *„učebnicový případ šíření úzkého hrdla mezi vlákny"* a vyvozuje z toho, že render vlákno se v takovém případě neoptimalizuje kvůli sobě, ale **aby ostatní mohla postoupit**.

Tentýž princip použije i na hranici mezi CPU a GPU: **trvá-li render vlákno déle než GPU, brzdí CPU; je-li to obráceně a render vlákno je dávno hotové, brzdí GPU.**

**Worker vlákna: kde se to skutečně děje** [(25:27)](https://www.youtube.com/watch?v=HQLYkwoDoT4&t=1527s) je nejužitečnější část přednášky, protože ukazuje **konkrétní klik**. Čeká-li herní vlákno na úlohu, klikneš na událost **hned vedle** té čekací a Insights zobrazí **šipku závislosti** — a na jejím konci je to, na co se čeká. V ukázce to byla aktualizace fyziky na worker vlákně; herní vlákno tedy nebylo úzké hrdlo. Druhý příklad: render vlákno čeká, než doběhnou úlohy render graph builderu — takže se optimalizují ty, ne render vlákno.

Rozdělení, které se hodí znát: **foreground** worker vlákna dělají časově citlivé úlohy a **umí zablokovat herní vlákno**; **background** vlákna dělají asynchronní načítání a AI.

**Context switche** [(29:22)](https://www.youtube.com/watch?v=HQLYkwoDoT4&t=1762s) — kanál, který ukáže, které vlákno běželo na kterém jádru. Dvě čtení: **jedno jádro obsazené jediným vláknem** může blokovat ostatní, a **příliš časté přepínání** je vlastní režie navíc. Otázka na konec: je zatížení jader vůbec vyvážené?

**Souborové I/O** [(31:06)](https://www.youtube.com/watch?v=HQLYkwoDoT4&t=1866s) — projeví se při načítání a v streamovaných úsecích. Připomínka, která vysvětluje, proč se to hledá jinde, než člověk čeká: **herní vlákno na disk nesahá**, vydá požadavek a obsluhuje ho vyhrazené I/O vlákno. Nástroje: *asset loading insights* (kdo se načítal a jak dlouho v každé fázi), *IO activity* (které soubory) a *IO store activity* (data po chuncích). Tři páky na zlepšení: **zrychlit blokující kroky** (typicky deserializaci), **zkrátit čekání** (menší soubory nebo jiné načasování) a **upravit rozložení assetů a velikost chunků**.

**Čtyři zásady na závěr** [(37:50)](https://www.youtube.com/watch?v=HQLYkwoDoT4&t=2270s), které stojí za doslovné převzetí: **začni daty, nehádej** · **nevěř dojmu, věř nástroji** · **řeš to, co má největší dopad** · **po každé změně změř znovu**. A postoj, který k tomu doporučuje: *„co mi asi uniká?"*

> **Pozn.:** Ta rada „ignoruj *idle* a *wait for task*" vypadá jako drobnost a je to nejčastější důvod, proč lidé v Insights hledají hodinu na špatném místě — [totéž z druhé strany](gpu-pamet.md#busy-wait-idle-co-rika-novy-gpu-profiler) říká nový GPU profiler svým sloupcem *wait*. Zobecněně: **v paralelním systému je nejdelší pruh podezřelý, ne usvědčený.** Nejpraktičtější věc odsud je ale ten **klik na sousední událost** kvůli šipce závislosti — je to konkrétní pohyb myší, který převede „něco tu čeká" na „čeká to na tohle", a přesně takové kroky v dokumentaci obvykle chybí. Poznámka k prameni: **automatický přepis téhle přednášky je hodně zkomolený** (přednášející mluví anglicky s japonským přízvukem a titulky komolí i názvy nástrojů), takže je tu zpracovaná konzervativně — bereme z ní strukturu postupu a ty čtyři zásady, ne přesné formulace.

**Souvislosti:** [Benchmark z level sequence](#benchmark-z-level-sequence-mereni-jako-soucast-prace) · [Tracing bez utopení](#tracing-bez-utopeni-kanaly-sirka-pasma-a-scenare) · [Profiling: rozhodovací strom](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Potrubí snímku](frame-pacing.md#snimek-neni-fronta-je-to-potrubi) · [Paměť GPU: busy, wait, idle](gpu-pamet.md#busy-wait-idle-co-rika-novy-gpu-profiler) · [Rejstřík: Context switch](../rejstrik.md#context-switch) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights)

---

## Tracing bez utopení: kanály, šířka pásma a scénáře

**Zdroj:** [Unreal Fest Stockholm 2025 Collection — High Performance Telemetry with Trace](https://www.youtube.com/watch?v=CijCVXa0wBQ&t=3847s) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · prostřední přednáška sestřihu (~30 min, Insights tým)

**Shrnutí:** Přednášející z týmu, který Insights vyvíjí, začne přiznáním obsaženým v podtitulu jeho přednášky — *pití z požárního hydrantu*: **zapneš-li v enginu všechno trasování, opravdu se v tom utopíš.** Kapitola je návod, jak z toho vybrat. Háček, který je zásadní a málokdo ho čeká: **přeteče-li trasovací vyrovnávací paměť, aplikace se zastaví** — žádné plynulé zhoršení, žádné zahazování dat.

### Rozpad myšlenky

**Jak je to postavené** [(1:05:41)](https://www.youtube.com/watch?v=CijCVXa0wBQ&t=3941s), protože bez toho nedávají další rady smysl: **trace log** je běhová knihovna, která zapisuje strukturované události do proudu dat; **trace analysis** ten proud parsuje; **Unreal Insights** to zobrazuje. Proud je **sebepopisný** — události začínají popisem svého tvaru, takže se dají měnit pole, aniž se znehodnotí staré záznamy. Zapisuje se **per vlákno do bufferu** (žádné zamykání mezi vlákny) a jeden worker to sbírá, komprimuje a posílá pryč.

Užitečný detail: **tail buffering** je kruhový buffer pevné velikosti, ze kterého se dá kdykoli udělat **snapshot** — takže se dá profilovat ad hoc, aniž bys předem věděl, že to budeš potřebovat.

**Kanály a předvolby** [(1:11:29)](https://www.youtube.com/watch?v=CijCVXa0wBQ&t=4289s) jsou hlavní páka. Kanály jsou po kategoriích (výkon, paměť, kontext, systémové) a nad nimi jsou **předvolby** podle scénáře — *default* je rozumný výběr pro výkon s nízkým dopadem, *memory* pro podrobné sledování paměti. A doporučení, které se hodí týmu: **vlastní předvolby se dají definovat v `ini` a sdílet mezi kolegy.**

**A to, co je na celé myšlence nejdůležitější** [(1:18:15)](https://www.youtube.com/watch?v=CijCVXa0wBQ&t=4695s): *„nestíhá-li worker vlákno objem dat, která trasuješ, začnou neodeslaná data spotřebovávat paměť. Používáme na to zásobník bloků — ale dosáhne-li nastaveného limitu, **aplikace se zastaví**. Momentálně neexistuje žádné plynulé zhoršení ani zahazování dat."* Druhý důsledek téhož: na stroji s málo jádry může být **worker vlákno tak vytížené kompresí, že ti zkreslí měřená data**.

**Tři typy událostí a jedna past** [(1:19:41)](https://www.youtube.com/watch?v=CijCVXa0wBQ&t=4781s). Běžné události mají zaručené pořadí jen v rámci vlákna; **synchronizované** nesou globální ID (dražší na analýzu); a **important** se drží v paměti po celou dobu běhu procesu, protože se musí znovu vyslat při každém novém spuštění trasování.

Odtud plyne past, kterou přednášející jmenuje výslovně [(1:23:34)](https://www.youtube.com/watch?v=CijCVXa0wBQ&t=5014s): **nedávej do dynamických jmen scopů index nebo číslo snímku.** Každé nové jméno vyrobí novou important událost, takže *„jejich objem poroste donekonečna"*. Potřebuješ-li vazbu na snímek, použij **kanál frames** — je mnohem levnější a Insights s ním umí korelovat.

**Cena jednotlivých kanálů**, shrnutá prakticky:

| kanál | cena | poznámka |
|---|---|---|
| **CPU** | levný — se statickými jmény | preferuj statické řetězce; dynamická se musí sledovat v mapě |
| **`-statnamedevents`** | přidá **hodně** událostí a část se překrývá | *„začni bez toho"* a zapni, až budeš potřebovat víc dat |
| **mem tag** (LLM) | nízká režie | jen po kategoriích — neřekne, co konkrétně alokuje |
| **mem alloc** | vysoká režie a velká šířka pásma | posílá call stacky ke každé alokaci |
| **task** | vysoká režie | zapínej, jen když řešíš problém s úlohami |
| **screenshot** | blokuje herní vlákno | nehodí se na každý snímek |
| **log** | levný, ale pozor na spam | roste s ukecaností logu |

**Tři obecné rady na závěr** [(1:28:07)](https://www.youtube.com/watch?v=CijCVXa0wBQ&t=5287s): **rozhodni se pro scénář předem a nemíchej je** — *„viděl jsem lidi používat podrobné sledování paměti spolu s měřením výkonu, jenže to sledování paměti ti ta výkonová data pořádně zkreslí"* · **nezapínej kanály, o kterých nevíš, co dělají** (dostával traces s kanálem, který slouží jen rewind debuggeru a k profilování nedává nic) · **používej předvolby.**

**Jak spustit paměťové trasování v praxi** *(doplněk z [krátkého tutoriálu](https://www.youtube.com/watch?v=qGma-I9PD1c) od [Spacemarine658](https://www.youtube.com/channel/UC0wsWmEHhv-PddR5rE5bhvA))* [(0:49)](https://www.youtube.com/watch?v=qGma-I9PD1c&t=49s): **Memory Insights se z editoru zapnout nedá** — musí se spustit z příkazové řádky. Nejpohodlnější je **dávkový soubor**, který pustí naráz `UnrealInsights.exe` i `UnrealEditor.exe` s týmiž parametry (bez toho druhého se nasbíraná data nespárují). Ke kanálu `memory` se vyplatí přidat **`metadata` a `assetmetadata`** — teprve pak Insights řekne, **co konkrétně** tu paměť alokuje, místo holých součtů. A při čtení záznamu jsou klíčem **bookmarky**: v zeleném textu nahoře poznáš *editor startup*, *files loading*, *PIE* a *PIE shutdown* — takže víš, kterou část záznamu vůbec máš číst. *„Všechno před tímhle je v podstatě k ničemu."*

A pro ty, kdo si chtějí trasovat vlastní kód: preferuj statické řetězce, existují **podmíněné časovače** (změř ten scope jen tehdy, když pole není prázdné), a chceš-li vlastní událost, **nakrm ji do stávajícího timing provideru** — *„vizualizaci pak dostaneš zadarmo."*

> **Pozn.:** To, že **přetečení znamená zastavení, ne degradaci**, je informace, kterou by běžný uživatel objevil až tím, že by mu build zamrzl při profilování — a nevěděl by proč. Za pozornost stojí i obecnější poučení: **měření není zdarma a jeho cena se dá změřit taky.** Trasovací worker soutěží o jádra s hrou, komprese kradou čas, zápis na disk soutěží s načítáním assetů — takže se dá vyrobit měření, které měří hlavně samo sebe. To je táž třída chyby jako [screen percentage, které jsi nenastavil](rozpocet-snimku.md#view-modes-kde-se-ztraci-nez-otevres-profiler)… jen o patro výš, protože tady zkresluje nástroj sám sebe. Nejpřenositelnější drobnost je **rada o dynamických jménech s číslem snímku**: zní jako mikroskopický detail a je to přesně ten druh rozhodnutí, které vypadá nevinně, roste lineárně s dobou běhu a projeví se až na dlouhé seanci. A **předvolby v `ini` sdílené v týmu** jsou levná věc, kterou skoro nikdo nedělá — přitom je to táž logika jako [scalability nastavená za celý tým](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1).

**Souvislosti:** [Insights jako disciplína](#insights-jako-disciplina-od-symptomu-ke-pricine) · [Benchmark z level sequence](#benchmark-z-level-sequence-mereni-jako-soucast-prace) · [Profiling: reprodukovatelný test](profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic) · [Telemetrie](telemetrie.md#vzdalena-analytika-trackedge-posthog) · [Rejstřík: Trace channel](../rejstrik.md#trace-channel) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights) · [Rejstřík: Telemetrie](../rejstrik.md#telemetrie)
