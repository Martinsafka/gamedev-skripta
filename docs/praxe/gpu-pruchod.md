# Optimalizační průchod: co se ve scéně najde

Předchozí kapitoly bloku dávaly metodu. Tahle ukazuje, **co z ní v praxi padá** — průchody skutečnými scénami (od ukázkové scény po bojovku pro deset let starý hardware), systematický postup na Lumen a rentgen fyziky. Formát je jiný než u návodů: nikdo tu nepředvádí jednu opravu, ale prochází scénu a nachází v ní jednu věc za druhou, včetně těch, které nakonec nezabraly.

Poslední dvě myšlenky jsou z přednášky, kde dva lidé z Epicu **veřejně proprofilovali cizí rozdělanou hru** — a nálezy jsou proto obyčejné, tedy reprezentativní.

Metodický základ je v [Profilingu](profiling.md) a [Rozpočtu snímku](rozpocet-snimku.md); mechanismy, které se tady jen používají, vysvětluje [Nanite do hloubky](nanite-do-hloubky.md) a [Paměť GPU](gpu-pamet.md).

---

## Hodina v cizí scéně: co se najde, když se hledá

**Zdroj:** [1-hour of Unreal GPU Optimization Tips & Tricks](https://www.youtube.com/watch?v=c2MH20OPSw0) · [Tom Looman](https://www.youtube.com/channel/UCnO-xQvmsO1WwKFq-5Pvj0Q) · ~62 min, průchod ukázkovou scénou

**Shrnutí:** Autor vezme oficiální ukázkovou scénu od Megascans, pustí si ji na výkonné grafice a hodinu ji prochází — s deklarovaným cílem najít věci, které **platí i pro tvůj projekt**. Výsledek je nečekaně poučný: v profesionálně udělané ukázce od výrobce assetů je jedna chyba za druhou. Háček, který z toho dělá myšlenku a ne seznam tipů: **skoro každý nález je vypnutá nebo zapomenutá výchozí hodnota, ne špatné rozhodnutí.**

### Rozpad myšlenky

**Nález 1: materiál, který invaliduje všechny stíny** [(6:20)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=380s) — rozebraný samostatně u [stínové cache](nanite-do-hloubky.md#kdo-invaliduje-stinovou-cache). Shrnutí: contact shadows v master materiálu bez WPO disabled distance, **shadow depth 1,7 → 1,0 ms**, vizuálně beze změny.

**Nález 2: 59 částicových systémů, z toho 57 mimo obraz** [(13:34)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=814s). `stat NiagaraSystemCounts` ukáže 59 aktivních instancí téhož systému — *„a ty legrační jsou ty venku, kolem kterých jsme ani nebyli."* Simulují se, i když je nikdo nevidí, protože **Niagara ve výchozím stavu neculluje**. Oprava trvá pár minut a je to jeden nový asset: **Effect Type** s nastavenou scalability — *max time without render* (nerenderuje-li se to půl sekundy, přestaň), *allow pre-cull by view frustum* (rozhodni už při spawnu, jestli by to vůbec bylo vidět) a *cull update frequency*. Výsledek: **59 → 2 aktivní systémy** a Niagara GPU simulace z 0,7–1,0 ms na **0,02 ms**.

Tři statistiky, které k tomu patří a liší se podrobností: `stat NiagaraSystemCounts` (kolik čeho běží) · `stat NiagaraSystems` (CPU cena rozdělená na herní vlákno, souběžnou práci a render vlákno) · `stat Niagara` (nejpodrobnější, včetně GPU dispatch a paměti).

Autor u toho zpochybní i běžný instinkt: *„není vždycky dobré mít GPU částice, kdykoli to jde."* V téhle scéně, kde je úzkým hrdlem GPU a CPU skoro nic nedělá, může být pro některé věci **CPU systém lepší volba**.

**Nález 3: dva assety, kterým chyběla dvě zaškrtnutí** [(24:59)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=1499s). Nástroj: **Audits → Statistics**, starý panel, který pořád funguje, seřazený podle velikosti.

- **Popínavé rostliny: ~90 MB.** Milion trojúhelníků a **vypnutý Nanite** — takže se generovala plná kolize z milionu trojúhelníků. Po zapnutí Nanitu: **1,2 MB.**
- **Helma: 66 MB.** Nanite zapnutý, ale **fallback target nastavený na „percent triangles = 100"**, takže fallback mesh měl 800 000 trojúhelníků. A fallback mesh se používá na **kolizi a hardwarový ray tracing** — line trace tedy střílel proti osmisettisícové helmě. Po přepnutí na *Auto*: 10 000 trojúhelníků.

Bokem k tomu dva praktické triky: **`show flag nanitemeshes 0`** je hrubý, ale rychlý způsob, jak proletět level a vidět, co Nanite nemá (na rozdíl od view mode ukáže i to, co je schované za zdí). A **položky s instance count 1**, které nejsou hero assety, se dají z levelu smazat — zmenší to balíček a ubere shading biny.

**Nález 4: prázdné shading biny** [(26:31)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=1591s). `r.Nanite.ShowStats`: **277 shading binů, z toho 213 prázdných.** Prázdný bin je draw call, který se odeslal a nic neudělal. Autor sám dodává kontext, který tomu ubírá na dramatičnosti: **od 5.4 se to díky compute shaderům prořezává líp**, takže je režie menší než dřív. A doporučení, které z toho plyne: **material instance dynamic už skoro není potřeba** — na variace je custom primitive data, které nevyrábí unikátní materiály.

**Nález 5: lens flare za 0,7 ms** [(37:42)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=2262s). Na tomhle nálezu je nejcennější **jak se rozhodoval**: nestačí mu, že je to drahé — chce vědět, co za to ztratí. Použije k tomu konzolový příkaz `A/B test`, který mezi dvěma hodnotami proměnné automaticky přepíná, takže je rozdíl vidět v pohybu. Závěr: *„jen to celou scénu trochu prosvětlí — za 0,7 ms to nestojí."* Ale postup je přenositelnější než ten závěr.

**Nález 6: světla, kterým chybí dosah** [(41:36)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=2496s). Vedle nevyhnutelného **attenuation radiusu** (světlo prosvítající do vedlejší místnosti a pod zem) přidává druhou páku, která se používá málo: **max draw distance + max fade range** přímo na světle. Postup: najdi vzdálenost, ze které světlo ještě něco dělá, nastav ji jako draw distance a přidej dost velký fade (jeho výchozí číslo je **750**), aby hráč přechod nikdy nechytil. `stat drawcount` ukáže, kolik světel se skutečně vykresluje — v té scéně 124 až 260. A diagnostická perlička: **cena projekce světel byla vyšší než cena kreslení stínů**, což *„moc často neuvidíš — a když ano, máš co opravovat."*

**Nález 7, který jde opačným směrem** [(53:33)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=3213s): **tonemapper sharpen = 2** je v té scéně zapnutý a autor zjistí, že **bez něj vypadá scéna rozmazaně**. Tedy položka, kterou nesmíš vypnout, i když by se to nabízelo. *„Tahle jedna konzolová proměnná dělá rozdíl mezi ‚dobré' a ‚výborné'."* Přidává k tomu i výhradu: dvojka nemusí sedět všude a občas to na některých meshích dělá lem.

**Nález 8: `r.Nanite.MaxPixelsPerEdge`** [(56:44)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=3404s). Výchozí hodnota 1 je nejvyšší kvalita; **4 srazila Nanite vis buffer z ~2,3 na necelé 2 ms** a při hraní se to skoro nepozná (na 10 už ano — přechody LODů přestanou být plynulé). Podstatná poznámka: **není to součást scalability skupin**, takže se to musí nastavit ručně. Vizualizace: Nanite → clusters.

> **Pozn.:** Nejcennější věc na tomhle formátu je **žánr sám**: hodina hledání v cizí scéně ukáže něco, co seznam tipů neumí — totiž **jak často je příčina banální**. Ani jeden z osmi nálezů není architektonická chyba; všechno jsou to zapomenutá pole, výchozí hodnoty a nevypnuté funkce. Praktický důsledek: **než začneš přemýšlet o architektuře, projdi si defaulty** — a to platí dvojnásob u staženého obsahu, protože ten je autorovaný pro předvedení, ne pro provoz. Za pozornost stojí i jeho zvyk **hledat příkazy mezerou** (`nanite ` a pak něco s „stats"), místo aby si pamatoval přesná jména; drobnost, která z konzole udělá použitelný nástroj. A vlastní výhrada, kterou autor sám naznačuje v závěru: **tohle je průzkum, ne optimalizace.** Většinu změn na konci videa nemá zapnutých — hodnota je v seznamu, ne ve výsledném framerate.

**Souvislosti:** [Les na 60 FPS](#les-na-60-fps-co-zabralo-a-co-ne) *(týž formát, vlastní projekt)* · [Nanite: kdo invaliduje stínovou cache](nanite-do-hloubky.md#kdo-invaliduje-stinovou-cache) · [Rozpočet snímku: view modes](rozpocet-snimku.md#view-modes-kde-se-ztraci-nez-otevres-profiler) · [Profiling: reprodukovatelný test](profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic) · [Rejstřík: Effect type](../rejstrik.md#effect-type) · [Rejstřík: Shading bin](../rejstrik.md#shading-bin) · [Rejstřík: Attenuation](../rejstrik.md#attenuation)

---

## Les na 60 FPS: co zabralo a co ne

**Zdroj:** [Nanite Forest Optimisation in Unreal Engine 5](https://www.youtube.com/watch?v=uE4cGZjMfuY) · [Filgeck](https://www.youtube.com/channel/UC_vaEIlHfMxbskfXHdO3peQ) · ~21 min, zkušenost z vlastního projektu

**Shrnutí:** Měsíc práce na lesní scéně, **30 → 60 FPS**, a autor prochází, co k tomu vedlo. Sestava je pro tuhle knihovnu důležitá — **RTX 4060 s 8 GB**, tedy ne vývojářský stroj, ale to, co má většina hráčů. Háček, který dělá tohle video cennějším než většinu tutoriálů: **říká i to, co nezabralo**, včetně hodin strávených hledáním konzolové proměnné, která nakonec nepomohla vůbec.

### Rozpad myšlenky

**Výchozí pozice**, řečená bez příkras: scéna používá Nanite, Lumen, virtuální stíny, TSR a PCG pro generování lesa; má denní cyklus a dynamické počasí. A **scalability je na High, ne Epic** — *„na Epic jsem to optimalizovat nedokázal a dostávám asi 40 FPS. Upřímně mezi High a Epic moc rozdíl nevidím."* Což je přesně to, co [Epic sám doporučuje](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) jako referenční režim pro 60 FPS.

**Paměť jako první problém, ne výkon** [(4:46)](https://www.youtube.com/watch?v=uE4cGZjMfuY&t=286s). Na 8GB kartě přišlo první varování o docházející video paměti. Dvě páky, obě hromadné:

1. **Maximum texture size** přes property matrix na vybraných texturách naráz — 8K a 4K dolů na **2K**, případně 1K.
2. **Převod na virtuální textury** (a s tím opravit sampler typy v master materiálu — [tentýž postup](gpu-pamet.md#virtualizace-kniha-ze-ktere-ctes-jen-otevrenou-stranku), jen ručně).

**Nanite landscape a jeho skrytá cena** [(7:46)](https://www.youtube.com/watch?v=uE4cGZjMfuY&t=466s) je nejužitečnější varování celého videa, protože se o něm nikde nepíše: převod terénu na Nanite **spotřebuje ohromné množství RAM** (ne VRAM). Autorovi na 16 GB editor při 8K terénu spadl pokaždé; podle informací, které našel, by na to bylo potřeba **přes 100 GB**. Obchvat, který funguje: **převést level na World Partition** a pak konvertovat **po několika buňkách** — načíst, převést, uvolnit, další.

**Tessellation: zaplaceno, nedodáno** [(10:52)](https://www.youtube.com/watch?v=uE4cGZjMfuY&t=652s). Zapnul ji na materiálu terénu, ztratil snímky a **vizuálně se nic nezměnilo**, protože ten materiál stejně používá jen normálové mapy. Závěr: *„nezapínej tessellation, pokud ji opravdu nepotřebuješ — hodně to ovlivňuje výkon."*

**Stíny a vítr**, rozebrané u [stínové cache](nanite-do-hloubky.md#kdo-invaliduje-stinovou-cache): invalidation behavior na **Rigid**, WPO disabled distance 20 000 pro stromy a mnohem méně pro trávu, cull distance pro trávu (5 000 a 1 800 pro tu nejmenší) — a **tráva bez stínů úplně**, protože les je stejně ve stínu.

**Nález, který nezabral** [(17:08)](https://www.youtube.com/watch?v=uE4cGZjMfuY&t=1028s), a proto je v knihovně: `stat GPU` ukázal shadow depths až **6 ms** kvůli pohybujícímu se slunci. Logická hypotéza: omezit vzdálenost, do které se stíny stromů vrhají. U klasických shadow maps je to pole na directional lightu; **u virtuálních stínů ne** — takže hledal konzolovou proměnnou. *„Když jsem ji po mnoha hodinách rešerše konečně našel, vůbec to výkon nezlepšilo."* Nechal to tak.

**A drobnost, která se hodí**: proti ghostingu a blikání listí a stínů nabízí dvojici konzolových příkazů (v jeho konfiguračním souboru), s poctivým „pokud to nepomůže, zkus vypnout world position offset a pixel depth offset v materiálu terénu."

> **Pozn.:** Za tímhle videem stojíme hlavně kvůli **negativnímu nálezu**. Devadesát devět tutoriálů ze sta ukazuje jen to, co vyšlo — takže si divák odnese dojem, že optimalizace je řada zásahů, které fungují. Přiznaných „strávil jsem tím hodiny a nepomohlo to" je v žánru extrémně málo, a přitom je to **realistický poměr**. Souvisí to s [nálezem, který není hotová práce](profiling.md#nalez-neni-hotova-prace-predani) i s [rozhodnutím, kdy přestat kopat](rozpocet-snimku.md#rozpocet-je-penezenka-ne-cil): hypotéza, která zní logicky, je pořád jen hypotéza a měření ji může zamítnout. Druhá věc, kterou si odsud bereme, je **cílový hardware jako rámec celé práce**: 8 GB VRAM změnilo pořadí problémů — paměť se řešila dřív než výkon. To je dobrá připomínka, že „optimalizovat" neznamená totéž na každé sestavě. Jedna výhrada k formátu: autor sdílí **hotový konfigurační soubor** a nabádá ho zkopírovat. To je pohodlné a zároveň přesně ten způsob, jak se do projektu dostanou hodnoty, kterým nikdo nerozumí — vyplatí se ho brát jako **seznam věcí k prozkoumání**, ne jako nastavení k převzetí.

**Souvislosti:** [Hodina v cizí scéně](#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) · [Lumen: rozpočet a binární hledání](#lumen-rozpocet-a-binarni-hledani) · [Nanite: kdo invaliduje stínovou cache](nanite-do-hloubky.md#kdo-invaliduje-stinovou-cache) · [Paměť GPU: virtualizace](gpu-pamet.md#virtualizace-kniha-ze-ktere-ctes-jen-otevrenou-stranku) · [PCG vegetace](pcg-vegetace.md) · [Rejstřík: Virtual texture](../rejstrik.md#virtual-texture) · [Rejstřík: WPO](../rejstrik.md#wpo)

---

## Lumen: rozpočet a binární hledání

**Zdroj:** [Optimizing UE5: Advanced Rendering, Graphics Performance, and Memory Management](https://www.youtube.com/watch?v=dj4kNnj4FAQ) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, Unreal Fest 2024

**Shrnutí:** Lumen je v GPU profileru rozprostřený do několika položek (scene lighting, diffuse indirect a AO, reflections, lights), takže se špatně říká, „kolik stojí". Přednášející proto nabízí **operativní definici rozpočtu**: 4 ms na 60 FPS, 8 ms na 30 — a hlavně způsob, jak si ověřit, že se do něj vejdeš. Háček: hledání příčiny má **jen dvě větve**, a rozhodnout mezi nimi trvá vteřinu.

### Rozpad myšlenky

**Rozpočet, který se dá ověřit** [(37:24)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2244s). Autor přiznává, že to číslo dřív řekl a nevysvětlil, co znamená — a teď to napravuje: *„vypni Lumen (`r.DynamicGlobalIlluminationMethod 0`, `r.ReflectionMethod 0`) a snímky by měly být o čtyři nebo osm milisekund rychlejší."* To je definice, se kterou se dá pracovat, protože nezávisí na tom, jak se cena rozpadá do položek.

**První větev: odražené paprsky** [(38:58)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2338s). View mode **performance overview** (5.4) obarví pixely, které trasují **dedikované odrazové paprsky**. Ukázkový nález je hezky konkrétní: *„proč všechny ty stromy trasují odrazy? Aha — shader počasí jim snížil roughness, protože zrovna pršelo."* Páky:

- `r.Lumen.Reflections.MaxRoughnessToTrace` — výchozí 0,4, jenže **hodně projektů má většinu roughness kolem 0,35**, takže valná část obrazovky trasuje odrazy. Snížit.
- `r.Lumen.Reflections.MaxRoughnessToTraceForFoliage` — pro listí (materiály se subsurface / two-sided foliage) klidně **0** hned na začátku.

Zajímavá je i jeho druhá myšlenka k tomu: uvidíš-li, že odrazy trasuje třeba i stěna budovy, může být příčina **v materiálu, ne v proměnné** — a pak se opravuje ten materiál (u něj kaluže s příliš měkkým přechodem roughness).

**Druhá větev: screen traces, nebo world traces?** [(41:16)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2476s) Lumen sbírá informaci dvěma způsoby — **screen traces** berou hodnoty z pixelů na obrazovce, **world traces** z Lumen scény. Postup, který autor doporučuje jako první krok při jakémkoli problému s Lumenem (včetně vizuálních, jako je problikávání): **v Show → Lumen vypni screen traces.** Zmizí-li problém, víš, kterou půlku prohledávat.

Je-li to strana world traces, pokračuje se dvěma view modes:

- **Lumen scene** — co Lumen vlastně „vidí". Je-li tam něco příliš černé, něco chybí.
- **Surface cache** — a tady je legenda, kterou nikde jinde nenajdeš: **žlutá = Lumen to z Lumen scény vyřadil** (rozhodl, že to řešit nemusí), **fialová = nakresleno do Lumen scény, ale pixely se nevykreslily** — typicky proto, že surface cards nejsou správně nastavené nebo je mesh moc členitý. Odtud pochází „proč se ta lávka v nepřímém osvětlení neobjevuje".

> **Pozn.:** Nejpřenositelnější věc téhle myšlenky je **operativní definice rozpočtu**: „vypni to a změř rozdíl" funguje pro jakýkoli systém, který je v profileru rozprostřený do víc položek — a je to poctivější než sčítání řádků, které se navzájem překrývají. Druhá je **binární hledání jako první krok**: dvě větve, jedno přepnutí, půlka prostoru pryč. To zní triviálně, ale v praxi se místo toho ladí konzolové proměnné odshora dolů — a rozdíl mezi tím je hodina proti minutě. Souvisí to s [pořadím co → proč → jak](rozpocet-snimku.md#rozpocet-je-penezenka-ne-cil): binární hledání je způsob, jak se dostat od „co" k „proč" bez hádání. Vlastní výhrada k těm 4 a 8 milisekundám: jsou to hodnoty pro **konzolovou třídu hardwaru z doby přednášky** a Lumen na konzolích běží asynchronně — takže je ber jako řádovou orientaci a udělej si vlastní číslo tím způsobem, který autor popisuje.

**Souvislosti:** [Les na 60 FPS](#les-na-60-fps-co-zabralo-a-co-ne) · [Nanite: rozhodovací strom](nanite-do-hloubky.md#rozhodovaci-strom-je-to-vis-buffer-nebo-base-pass) *(týž tvar postupu o systém vedle)* · [Profiling: co říká GPU profiler](profiling.md#co-rika-gpu-profiler-a-co-v-nem-nenajdes) · [Osvětlení](osvetleni.md) · [Rejstřík: Lumen](../rejstrik.md#lumen) · [Rejstřík: Surface cache](../rejstrik.md#surface-cache) · [Rejstřík: Roughness](../rejstrik.md#roughness)

---

## Profilovat cizí hru: příprava, která rozhoduje

**Zdroj:** [Profiling with Purpose: Performance Lessons from a Real Unreal Project](https://www.youtube.com/watch?v=C-AjCqjKRSs) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~58 min, Unreal Fest Stockholm 2025 (dva lidé z technical developer relations)

**Shrnutí:** Dvojice z Epicu si vyžádala na LinkedInu skutečný rozdělaný projekt, dostala přes čtyřicet nabídek a jednu hru pak veřejně proprofilovala — se souhlasem studia a s jeho vlastní větou *„my jsme s optimalizací ještě nezačali."* Nejcennější třetina není v nálezech, ale v **přípravě**: co si zapnout, než se vůbec podíváš, a kolik to stojí. Háček, který se opakuje u obou přednášejících: **skoro každý užitečný přepínač má režii, a ta se musí započítat do toho, co měříš.**

### Rozpad myšlenky

**Spouštěcí parametry a jejich cena** [(8:36)](https://www.youtube.com/watch?v=C-AjCqjKRSs&t=516s). U cizí hry ze Steamu se dají nastavit v `properties → launch options`, což je mimochodem šikovná cesta, jak rozdávat vývojářské buildy. Sada, kterou používá:

| parametr | k čemu | cena |
|---|---|---|
| **`-trace=default,task`** | jediné, co doopravdy musíš zadat; `task` navíc ukáže, **na co která úloha čeká** | malá režie u `task` |
| **`-statnamedevents`** | zapne trasování dalších pojmenovaných událostí — bez něj vidíš jen hrubé bloky | **~20 % režie** (změřeno na tomhle projektu) |
| **`-execcmds`** | pustí konzolové příkazy po startu; on tam dává `stat unitgraph` a `stat fps` | — |
| **`-noverifygc`** | ověřování garbage collectoru ve vývojovém buildu ho **prodlouží zhruba dvakrát** a vyrábí falešné záseky | — |
| **`-dpcvars`** | přepíše i konzolové proměnné, které jsou jinak jen ke čtení | — |
| **`-logcmds="LogGarbage verbose"`** | vypíše fáze GC a — což jinak v traci **nezjistíš** — **počet `UObject`ů** | psaní logu samo stojí čas |
| **`-handleensurepercent=0`** | vypne ensures; ty se v traci projeví jako **nevysvětlená vteřinová pauza**, protože se nezobrazí stack walk ani ukládání dumpu | — |

Ta položka o `-statnamedevents` je nejlepší ilustrace celé myšlenky: *„chceš-li jen vědět, jestli se trefuješ do cíle, nechej to vypnuté. Ale netrefuješ-li se a chceš vědět proč, vřele doporučuju to zapnout."* Konkrétní zisk: bez toho byl v traci jen *„animation blueprint, 0,1 ms"*; s tím bylo vidět, že ten blueprint dělá **16 raycastů do fyziky na každou postavu a každý snímek**.

**Jak se čte snímkový panel** [(20:15)](https://www.youtube.com/watch?v=C-AjCqjKRSs&t=1215s): každý sloupec je **jeden snímek** (ne pevný časový úsek), vodorovná čára je 16,66 ms a všechno nad ní je zásek. Postup je pak nudný a funguje: klikni na dlouhý sloupec, zoomuj, jdi po nejtlustších blocích. Praktická drobnost: klávesou `R` se přepínají herní a renderovací snímky — u CPU práce se ty renderovací hodí vypnout. A trik, který ušetří hádání: **vyber časový úsek a klikni na funkci** — Insights vypíše, **kolikrát byla v tom úseku volaná**. Tak se ze „spousty raycastů" stalo **500 raycastů do fyziky v jednom snímku**.

**Nálezy na herním vlákně** jsou poučné hlavně tím, jak jsou banální:

- **Simulace nepřátel, kteří ještě nejsou ve hře** [(24:06)](https://www.youtube.com/watch?v=C-AjCqjKRSs&t=1446s). Ve scéně jsou dvě postavy a v traci desítky character movement komponent — tým vysvětlil, že jde o nepřátele z pozdějších bitev. Oprava: nesimulovat, co není v obraze.
- **`SetGender` volané na každé postavě v levelu** místo na těch dvou viditelných.
- **Animace vyhodnocené hned místo odloženě** — Unreal jinak animace počítá na worker vlákně, ale při spawnu aktéra to udělá okamžitě, aby to bylo vidět ve stejném snímku. Většinou to nepotřebuješ.
- **MetaHuman v LOD0** na postavy, které zabírají stodvacetiosminu obrazovky. Odpověď MetaHuman týmu na dotaz: **LOD0 je pro virtuální produkci a film**, ve hrách se doporučuje nanejvýš LOD1 a pak agresivně dolů.
- **`Add to World` trvající 23 vteřin** pro jednu world partition buňku. Nebyl to zásek (je to rozprostřené), ale ISM komponenty v ní si každá vytvářela fyzikální stav.

**A GPU strana, uspořádaná do tří druhů čísel** [(47:40)](https://www.youtube.com/watch?v=C-AjCqjKRSs&t=2860s): hledej **jedno velké číslo**, **hodně malých čísel** a **čísla tam, kde být nemají**.

- **Jedno velké**: jeden draw call v průchodu průhledností za skoro milisekundu — kouř z komína renderovaný **po depth of field**, tedy v plných 4K místo v 75 % dynamického rozlišení. A pointa: *„výchozí hodnota v Unrealu je after DOF."*
- **Jedno velké, podruhé**: řádek **virtual shadow map projection mask bits**, který nevypadá jako cena světel a je jí — je to **počet světel dopadajících na pixely**. Viníkem byla falešná odrazová světla, která nepotřebovala vrhat stín.
- **Hodně malých**: šedá plocha ve *visibility commands* se ukázala být **96 Niagara systémů, které četly výšku vody z GPU zpátky na CPU** — dohromady ~2 ms za oceán, který v tom záběru **nebyl vidět**.
- **Tam, kde být nemá**: Nanite programmable rasterization v průchodu *custom depth*, zbylá po obrysovém shaderu, který to už nepotřeboval.

**Dvě věci k přípravě GPU měření**, které stojí za převzetí. Profiluje se **na devkitu, ne na pracovní stanici** (*„naše stanice nejsou reprezentativní, jsou moc silné"*). A klíčové: **vypni dynamické rozlišení** (`r.DynamicRes.TestScreenPercentage 75`) — jinak se výkon projeví ve **velikosti back bufferu, ne v milisekundách**, takže všechno vypadá, že běží na cílových 30. *„První kolo jsem nasbíral všechna měření a říkal si: jedou třicet napříč, super. Aha — dynamické rozlišení."*

> **Pozn.:** Nejcennější je tady **inventář režií**. Většina návodů řekne „zapni `-statnamedevents`" a neřekne, že to stojí pětinu výkonu — a pak se člověk diví, proč se jeho měření nepodobá hře. Zobecněno: **každý přepínač, který ti přidá informaci, ti ubere z věrnosti měření**, takže se musí volit podle toho, na co se zrovna ptáš (jsme na cíli? proti proč nejsme?). Táž logika jako u [šířky pásma trasování](mereni-automaticky.md#tracing-bez-utopeni-kanaly-sirka-pasma-a-scenare). Druhá věc, kterou si odsud bereme, je **past dynamického rozlišení**: je to funkce, jejímž smyslem je držet cílový framerate — takže při měření **schová přesně to, co chceš vidět**. Sourozenec [screen percentage, které jsi nenastavil](lehky-render.md#rozpad-ceny-vychozi-sceny-a-cim-ji-nahradit), jen o třídu zákeřnější, protože tu funkci jsi zapnul schválně. A stojí za ocenění formát: **studio pustilo cizí lidi do své rozdělané hry před plný sál** — nálezy jsou proto obyčejné a tím reprezentativní, na rozdíl od vyrobených ukázkových problémů.

**Souvislosti:** [Chaos Visual Debugger](#chaos-visual-debugger-rentgen-fyziky) *(druhá polovina téhož nálezu)* · [Hodina v cizí scéně](#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) · [Profiling: čísla, se kterými se dá srovnávat](profiling.md#cisla-se-kterymi-se-da-srovnavat) *(tentýž přednášející o patro dřív)* · [Automatizované měření: tracing](mereni-automaticky.md#tracing-bez-utopeni-kanaly-sirka-pasma-a-scenare) · [Rejstřík: Dynamic resolution](../rejstrik.md#dynamic-resolution) · [Rejstřík: Trace channel](../rejstrik.md#trace-channel) · [Rejstřík: MetaHuman](../rejstrik.md#metahuman)

---

## Chaos Visual Debugger: rentgen fyziky

**Zdroj:** [Profiling with Purpose: Performance Lessons from a Real Unreal Project](https://www.youtube.com/watch?v=C-AjCqjKRSs) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~58 min, Unreal Fest Stockholm 2025

**Shrnutí:** Nejlepší deset minut celé přednášky je chvíle, kdy přednášející otevře **Chaos Visual Debugger** a ukáže scénu tak, jak ji vidí fyzika. Sál na to slyšitelně reaguje — a je proč: strom má kolizní geometrii **za každý list**, zeď za **každý dřevěný kolík**, a stánek s ovocem má zvlášť bednu se zelím a zvlášť bednu s cibulí. Háček, který z toho dělá myšlenku a ne kuriozitu: **není to nedbalost toho studia, je to výchozí chování Unrealu.**

### Rozpad myšlenky

**Co ten nástroj je** [(33:35)](https://www.youtube.com/watch?v=C-AjCqjKRSs&t=2015s): záznam celé fyzikální scény a všech dotazů do ní, snímek po snímku. Otevírá se v editoru přes *Tools → Debug → Chaos Visual Debugger*; ze zabaleného vývojového buildu se dá vyrobit soubor konzolovými příkazy a načíst ho tam.

**Rozdíl, který je potřeba znát, než se do toho podíváš** [(34:22)](https://www.youtube.com/watch?v=C-AjCqjKRSs&t=2062s): **simple** kolize se používá, když se objekty pohybují a naráží do sebe — to je ta, která stojí milisekundy za běhu. **Complex** kolize se používá pro dotazy do scény (raycasty, střelba) — a **i když ji nepoužíváš, musí se načíst**, takže zdržuje načítání a zdražuje raycasty.

**Co v té hře bylo vidět.** Nejdřív dobré zprávy: postavy jsou kapsle, stromy jsou kapsle, terén je trochu složitý, ale *„dá se s tím žít."* Pak se podívají do dálky — a je tam **načtené celé město** s hustou složitou geometrií, u hry s pohledem shora. Doporučení je stejně prosté jako správné: **nahradit ty domy kvádry.**

A pak přepnou do zobrazení **complex** kolizí a přijde ta pasáž se sálem. **Mech s každým stéblem. Strom s každým listem. Ve zdi kolik za každý kolík. Bedna se zelím, bedna s cibulí — „jak hluboko to jde? Až úplně dolů."**

**Vysvětlení, proč to tak je** [(38:14)](https://www.youtube.com/watch?v=C-AjCqjKRSs&t=2294s), je to hlavní, co si z toho odnést. Komplexní kolize **se generuje z LOD řetězu meshe** — a s Nanitem to znamená z **fallback meshe**. Kdo u Nanite meshů nenastaví počet LODů, dostane jako komplexní kolizi **celý Nanite mesh**, což je drahé na paměť i na dotazy. (Týž nález se v knihovně objevil nezávisle jako [helma za 66 MB](#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda).)

A pak přijde ta věta, kvůli které tady tahle myšlenka je: *„nechci je za to shazovat — protože zaprvé je to velmi časté, a zadruhé **je to výchozí workflow v Unrealu**. Každý mesh má ve výchozím stavu zapnutou komplexní i jednoduchou fyziku."* Oprava je **jedno pole v nastavení projektu**: kolizní profil na **use simple as complex** — a všechno tohle zmizí.

**Dvě věci navrch**, které se týkají téhož: **nestatická geometrie ve výchozím stavu kontroluje překryvy** při načtení, a to ne kvůli enginu, ale pro případ, že by na tu událost chtěl někdo reagovat. Takže: buď to udělej statické, nebo překryvy vypni.

> **Pozn.:** Tahle myšlenka je nejlepší doklad toho, že **výchozí hodnoty nejsou neutrální** — a zapadá přesně k [soapboxu o defaultech](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) z jiné Epicovy přednášky, kde totéž zaznělo o `use simple collision as complex` jako o nastavení do prvního changelistu. Tady je vidět, **jak to vypadá, když se to neudělá**: sál, který zalapal po dechu nad mechem s kolizí za každé stéblo. Přenositelné poučení je ale obecnější: **existuje vrstva projektu, do které se nikdo nedívá, protože není vidět.** Fyzika, streamovací buňky, reference mezi assety — všechno to má svůj prohlížeč a všechny se otevřou jednou za projekt, obvykle až když je zle. Vyplatí se je otevřít **dřív**, pro nic jiného než pro kalibraci, jak to vlastně vypadá. A ještě jedna vlastní poznámka: **komplexní kolizi někdy opravdu potřebuješ** — přednášející to sám říká u přesné střelby. Takže to není „vypni to všude", ale „vypni to jako výchozí stav a zapínej vědomě", což je táž změna z opt-out na opt-in.

**Souvislosti:** [Profilovat cizí hru](#profilovat-cizi-hru-priprava-ktera-rozhoduje) · [Hodina v cizí scéně](#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) *(týž nález u fallback meshe, jinou cestou)* · [Rozpočet snímku: prvních 16,66 ms](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Ragdoll](ragdoll.md) · [Rejstřík: Collision preset](../rejstrik.md#collision-preset) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Ladění: Visual Logger](debugging.md#ctyri-otazky-ctyri-nastroje-od-print-stringu-po-visual-logger) *(totéž nahrávání pro libovolné hodnoty)*

---

## Bojovka pro desetiletý hardware: rozpočet po částech a co se v něm našlo

**Zdroj:** [Fighting the Frame Budget: Stage Optimization Lessons from 2XKO | Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=Pkd7-ouyb-M) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~34 min, přednáška (Riot Games, rendering) · + [How to Boost FPS Fast in UE5 with this ONE Setting](https://www.youtube.com/watch?v=aK9K7CffqCk) · [3D Dreamer](https://www.youtube.com/channel/UCVAdTnZgQ40jpKzC0-_RPAQ) · 21 s, tip

**Shrnutí:** Riot ladí stage bojovky 2XKO pro GTX 960, deset let staré i7 a 8 GB paměti (Xbox Series S) — bez Nanitu, Lumenu i virtuálních stínů. Přednáška začíná lekcí, která platí i bez slabého hardwaru: „výkon je špatný" znamená jen „nedržíme rozpočet", a rozpočet musí být **rozepsaný po částech hry** — stage má 6 ms GPU, 400 meshů a podíl na 500 MB textur. Pak prochází nálezy na CPU i GPU. Háček: většina nálezů na CPU nebyla složitá — šlo hlavně o **špatné návyky**, ne o chybějící technologii.

### Rozpad myšlenky

**Rozpočet, se kterým se dá pracovat** [(3:57)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=237s): „chceme 60 FPS" je cíl, ne rozpočet. Použitelný rozpočet je rozepsaný na CPU, GPU a paměť, **po částech hry** (postavy zvlášť, stage zvlášť, menu zvlášť), pro konkrétní hardware — a nechává rezervu na budoucí obsah a na pohlcení hitchů [(4:45)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=285s). U 2XKO je dělení nutné i kvůli kombinatorice: hráč si volí stage i šampiony a **žádná kombinace nesmí rozbít výkon**; a rozpočet po částech dá každé části vlastníka [(5:32)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=332s).

**CPU: čtyři otázky nad tracem** [(7:50)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=470s): co drží herní vlákno (práce, nebo čekání), co trvá nejdéle, čemu ve scéně to odpovídá (na to se ptej artistů) a jak to spravit. Na jedné stagi trace ukázal kolem 24 tiků skinned mesh komponent, řetěz „update child transforms" pod skeletal meshem a 11 timeline [(7:04)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=424s). Nálezy a léky:

- **Každý skeletal mesh actor má vlastní režii** → víc NPC sloučit do jednoho skeletal meshe [(8:37)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=517s). A návyk, který stál nejvíc: static meshe připnuté ke skeletal meshi v blueprintu (bedny na lodi) spouštějí propagaci transformací [(9:24)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=564s).
- **Loď jako skeletal mesh s jedinou kostí** a spoustou trojúhelníků jen proto, aby se houpala. Cena skinningu roste zhruba s počtem polygonů × kostí × složitostí anim grafu, takže hustý mesh s jednoduchým pohybem skeletal meshem být nemá [(10:11)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=611s). Jednoduchý otřes zvládne timeline (běží jen ve chvíli, kdy hraje, kdežto anim blueprint tiká pořád) nebo vertex animace přes WPO [(10:58)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=658s).
- **11 timeline posouvajících objekty po spline** → Niagara komponenta, která po spline jede sama. Cena nezmizí, ale **přesune se z herního vlákna na renderovací** [(11:45)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=705s), [(12:31)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=751s).
- **[Animation Budget Allocator](../rejstrik.md#anim-budget-allocator)** v lobby: pevný strop na animace (třeba 1,5 ms) a vlastní významnost podle stavu avatara — kdo sedí u automatu, animuje méně, kdo běhá, víc [(13:17)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=797s).

**GPU: proporce, ne absolutní čísla** [(16:24)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=984s): ve [forward rendereru](../rejstrik.md#forward-rendering) se ptáš, jak dlouho trvají passy vůči sobě. Dlouhý depth pass → moc polygonů; dlouhý base pass u jednoho draw callu → drahý shader; dlouhá translucency → overdraw. U nejdražších draw callů pozor na to, že cena roste s počtem pixelů — hledají se **malé věci, které jsou drahé** [(17:10)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1030s). A kontrola, kterou v editoru nevidíš, ale v traci ano: je draw call v passu, kam patří? Velký mesh omylem jako translucent nebo masked platí depth pass dvakrát [(17:56)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1076s). Ze špatných návyků: Niagara, kde pět instancí spouští po jednom spritu místo jednoho systému s pěti, a kamínky menší než pixel tam, kam patří sprite [(18:43)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1123s). Ze standardních pák: quality switch, **[static switch](../rejstrik.md#static-switch) místo lerpu mezi nulou a jedničkou** (statický přepínač nepoužitou větev vykompiluje, lerp počítá obě) a per-object detail mode, u kterého o tom, co na nízkém nastavení zmizí, rozhoduje artista [(19:31)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1171s), [(20:19)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1219s).

**Triky z doby před UE5** [(21:06)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1266s): na odrazy výkon nemají, takže řeka odráží zrcadlovou kopii scény pod hladinou; pohyblivé světelné skvrny pod stromy dělá translucentní „světelný válec", který obarví, co leží uvnitř [(21:53)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1313s); mramor odráží přes cube mapu [(22:39)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1359s). A poctivá výhrada k instancování: ISM z objektů na opačných koncích stage ztratí culling po objektech a kreslí se celý — někdy to vyjde dráž [(24:13)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1453s). (Opačná páka na culling drobných propů je **Bounds Scale** v detailech objektu: menší hodnota ho nechá zmizet dřív [(0:00)](https://www.youtube.com/watch?v=aK9K7CffqCk&t=0s). Jen pozor, aby bounds pořád obalovaly celý viditelný mesh — jinak bude objekt mizet ještě v obraze.)

**Kam až jít: zásahy do enginu** [(25:00)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1500s): velké translucentní karty hor v pozadí (artisti chtěli měkký přechod, ne masked) žraly overdraw, takže translucentní pass smí zapisovat hloubku tam, kde je opacita jedna [(25:46)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1546s). A protože stíny vrhají jen šampioni a jen na podlahu, podlaha čte shadow mapu přímo a krok promítnutí do obrazovky odpadá [(26:32)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=1592s). Tohle už většina týmů neudělá a úspora u stínů byla podle přednášky malá; přenositelné je uvažování: **víš-li přesně, co tvoje hra nepotřebuje, můžeš to přestat počítat.**

> **Pozn.:** Shrnutí CPU části je univerzální rozhodovací pravidlo [(14:51)](https://www.youtube.com/watch?v=Pkd7-ouyb-M&t=891s): jde o špatnou praxi (→ naučit lidi), nebo o příliš mnoho obsahu (→ přesunout práci na jiné vlákno či GPU, nebo vědomě vyměnit kvalitu za výkon)? První polovina té otázky je důvod pro [nástroje, které drží artisty ve smyčce](mereni-automaticky.md#vykon-jako-vec-celeho-tymu-dashboard-validace-a-kontrola-pameti) — tutéž chybu podruhé nemá chytat rendering engineer. Anim Budget Allocator používá i [Subnautica 2](velke-svety.md#animace-ve-velkem-od-tiku-k-udalostem), tam s vlastní prioritou pro „hero" tvory. A rozpočet po částech je konkrétní podoba [rozpočtu jako peněženky](rozpocet-snimku.md#rozpocet-je-penezenka-ne-cil): kdo ví, že stage smí 6 ms, nemusí se ptát, jestli je 7 moc.

**Souvislosti:** [Rozpočet je peněženka](rozpocet-snimku.md#rozpocet-je-penezenka-ne-cil) · [Co je v herním vlákně a co v renderovacím](profiling.md#co-je-v-hernim-vlakne-a-co-v-renderovacim) · [Proč malé trojúhelníky ničí GPU](rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu) · [ISM, HISM a merge](pamet-a-instance.md#ism-hism-a-merge-draw-cally-podle-geometrie) *(táž past s cullingem)* · [Lehký render](lehky-render.md) · [Rejstřík: Anim Budget Allocator](../rejstrik.md#anim-budget-allocator) · [Rejstřík: Static switch](../rejstrik.md#static-switch) · [Rejstřík: Forward rendering](../rejstrik.md#forward-rendering)
