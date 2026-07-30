# Optimalizační průchod: co se ve scéně najde

Předchozí kapitoly bloku dávaly metodu. Tahle ukazuje, **co z ní v praxi padá** — dva průchody skutečnými scénami a jeden systematický postup na Lumen. Formát je jiný než u návodů: nikdo tu nepředvádí jednu opravu, ale prochází scénu a nachází v ní jednu věc za druhou, včetně těch, které nakonec nezabraly.

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
