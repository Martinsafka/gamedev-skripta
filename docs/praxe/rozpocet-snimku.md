# Rozpočet snímku: kolik máš a kde se ztrácí

Šedesát snímků za sekundu znamená **16,66 ms na všechno** — herní logiku, animace, fyziku, síť, přípravu scény, draw cally a vykreslení. Tahle kapitola je o tom, jak s tím číslem zacházet jako s penězi: kolik jich je, kdy se rozdávají (dřív, než tušíš), kde se nejčastěji ztrácejí — a proč GPU nesnáší malé trojúhelníky, i když má výkon na miliardy operací.

Předchází tomu [Profiling](profiling.md) — bez měření je tohle jen teorie. Co s nálezem dělat pak, řeší [Optimalizace scény](optimalizace.md). A vnímanou plynulost, která s rozpočtem souvisí, ale není totéž, má [Potrubí snímku](frame-pacing.md).

---

## Rozpočet je peněženka, ne cíl

**Zdroj:** [Maximizing Your Game's Performance in Unreal Engine](https://www.youtube.com/watch?v=GuIav71867E) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~42 min, Unreal Fest 2022

**Shrnutí:** Přednášející vede celou přednášku na jedné analogii: **16,66 ms je částka, kterou máš na snímek, a optimalizace je rozhodování, za co ji utratíš.** Z toho plyne odpověď na nejčastější otázku („kdy mám optimalizovat?"), na kterou obvykle nikdo neodpoví jinak než „ne moc brzo" — a jedno pořadí kroků, které se v praxi pořád obchází, i lidmi, kteří ho znají. Háček: **rozpočet nemáš jen jeden.** Máš ho zvlášť pro CPU a GPU, a fakticky pro každé jádro a subsystém cílové platformy.

### Rozpad myšlenky

**Ta analogie** [(3:55)](https://www.youtube.com/watch?v=GuIav71867E&t=235s) stojí a padá s tím, že se rozpočet dá **utratit celý**, a to je v pořádku: *„některé funkce vypadají skvěle, ale jsou drahé. Můžeš se prostě rozhodnout, kdy se to vyplatí."* Svatba se 16 tisíci: manžel či manželka chce 10 z nich na catering a 6 na všechno ostatní — a pro někoho to **za to stojí**. Totéž s Lumenem: je drahý, a pro některá studia je přesto správná volba.

**Kolik z rozpočtu si smíš vzít, závisí na platformě** [(4:41)](https://www.youtube.com/watch?v=GuIav71867E&t=281s), a tenhle rozpad je praktičtější než jakákoli obecná rada:

| platforma | kolik rozpočtu utratit | proč |
|---|---|---|
| **konzole** | skoro celý | hardware je známý a dobře chlazený |
| **PC** | s rezervou | konfigurací je nekonečno — a **rozpočet ovládá hráč**, ne ty (posuvníky v nastavení) |
| **mobil** | s rezervou navíc | tepelný throttling (není tam ventilátor) a výdrž baterie |

Ten řádek o PC má ještě jeden důsledek, který přednáška zmiňuje jen mimochodem a stojí za vytažení: většina hráčů si nastavení **ladit nebude** — takže buď udělej autodetekci hardwaru, nebo nastav výchozí hodnoty s dost velkou rezervou, aby to jelo rovnou.

**Kdy optimalizovat** [(6:26)](https://www.youtube.com/watch?v=GuIav71867E&t=386s) rozebírá tak, že nejdřív odmítne absolutní znění pravidla. *„Premature optimization is the root of all evil — a je to pravda a souhlasím s tím. Jenže je to velmi absolutní výrok, a víme, kdo mluví jen v absolutních výrocích."* (Sithové.) Jeho verze: **neoptimalizuj předčasně, ale zůstaň si výkonu vědomý.** Konkrétně: nedělej mikrooptimalizace v kódu (`--i` místo `i--` ve for cyklu — *„čitelnost kódu je priorita číslo jedna"*) a **běží-li ti hra na cílovém hardwaru v šedesáti, jsi hotový**.

A kdy tedy začít? *„Když se to objeví v profileru."* Postup je pak vždycky stejný: **nejnižší visící ovoce** — největší dopad za nejmenší práci — pak zopakovat, a takhle až do vydání. Právě proto se nemá utrácet čas na mikrooptimalizace: *„v celkovém obrazu neudělají rozdíl."*

**Pořadí, které se pořád obchází** [(8:47)](https://www.youtube.com/watch?v=GuIav71867E&t=527s): **co → proč → jak.** Co je pomalé (to ti řekne profiler, protože co žere čas, tam se ukáže) → proč je to pomalé → a teprve pak jak to spravit. A pak přijde ta poctivá část: *„někteří z nejlepších lidí, s kterými jsem pracoval — a taky já sám — jdou často hned na ‚proč'. Uvidí něco pomalého a začnou to naslepo spravovat. Často mají pravdu. Zvlášť když jsou hodně senior a už to viděli. Ale někdy pravdu nemají a spraví něco, co rozbité nebylo."* Tesařská verze: **měř dvakrát, řež jednou.**

**Milisekundy, ne FPS** [(14:48)](https://www.youtube.com/watch?v=GuIav71867E&t=888s) je detail, který mění, jak se o výkonu vůbec dá mluvit: *„radši bych, aby mi lidi říkali ‚snímek se zpomalil o 15 milisekund'. Protože když mi někdo řekne, že hra ztratila pět snímků za sekundu, znamená to různé věci podle toho, jaký byl framerate."* Ze 120 je to nepostřehnutelná odchylka, z dvaceti čtvrtina rozpočtu. **Milisekundy jsou vždycky pravda.**

**A kdy přestat** [(18:39)](https://www.youtube.com/watch?v=GuIav71867E&t=1119s) má stejně praktickou definici. Po opravě prokletých bodových světel v Lyře (attenuation radius 5 000 přes celý level a zapnuté vrhání stínů — dvě čísla, 30 → 60 FPS) se vrátí do profileru: *„a ta ostatní se už ani neukážou. Takhle poznáme, že máme přestat optimalizovat — už to v profileru není."*

> **Pozn.:** Ta peněženka je nejlepší rámec, jak o výkonu mluvit s někým, kdo není programátor — protože **odstraňuje moralizování**. „Lumen je drahý" znamená v rozpočtové řeči „Lumen stojí X milisekund, máš 16,66, rozhodni se" — a to je věta, po které se dá vést rozhovor, ne hádka. Za pozornost stojí i skladba přednášky: pořadí **co → proč → jak** dostal divák vytištěné na papír, aby si ho položil na stůl. To zní jako vtip a je to reakce na skutečné selhání — pořadí lidé znají a stejně ho nepoužijí, protože jim intuice napovídá „proč" dřív, než změří „co". Jedna vlastní výhrada k řádku o PC: **rezerva není konstanta.** U hry, kterou hráči budou hrát na integrované grafice, je rozpočet fakticky poloviční, a to je rozhodnutí o [scope](../teorie/scope.md#design-by-constraint-krabice-napred-napad-dovnitr), ne o nastavení.

**Souvislosti:** [Prvních 16,66 ms se rozdává v CL1](#prvnich-1666-ms-se-rozdava-v-cl1) *(kdy se ten rozpočet fakticky utratí)* · [Profiling: rozhodovací strom](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Profiling: čísla, se kterými se dá srovnávat](profiling.md#cisla-se-kterymi-se-da-srovnavat) · [Rejstřík: Frame time](../rejstrik.md#frame-time) · [Rejstřík: Premature optimization](../rejstrik.md#premature-optimization)

---

## Prvních 16,66 ms se rozdává v CL1

**Zdroj:** [How to Start Your Project at 60 FPS and Keep It There](https://www.youtube.com/watch?v=DxBKmQ-0kfw) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~50 min, Unreal Fest Chicago 2026 · + [UE5 Optimization Made Easy: Fundamentals](https://www.youtube.com/watch?v=zVNViTNHHdA) · [Dallas Drapeau](https://www.youtube.com/channel/UCatEMsDp-qF_bix_1ST2llw) · ~36 min, výklad

**Shrnutí:** Principal technical artist z Epicu má nezvyklý formát: **ukáže první changelist projektu.** Nastavení, pluginy a dva `.ini` soubory, které se dají udělat jen jednou — než projekt otevře druhý člověk. Nejsilnější poznatek celé přednášky je přitom takhle malý: **výchozí nastavení enginu je pro nováčky, ne pro tvůj 60 FPS projekt** — včetně scalability, která je nastavená na *Epic*, což je 30 FPS režim. Háček: v editoru se tím pádem díváš na jinou hru, než jakou chceš dodat.

### Rozpad myšlenky

**Než začneš: cílový framerate je designové rozhodnutí** [(1:37)](https://www.youtube.com/watch?v=zVNViTNHHdA&t=97s). Druhý zdroj otevírá otázkou, na kterou podle něj většina vývojářů neodpoví: *„jaký je tvůj cílový framerate? Ne každá hra je stavěná na 120 snímků. Ne každá hra je stavěná ani na 60."* A rozpad ukazuje, že to není číslo v dokumentu, ale volba pracovního postupu:

| cíl | co z toho plyne |
|---|---|
| **120 FPS** | jednoduchá geometrie, **pečené osvětlení**, LODy, trim sheety |
| **60 FPS** | kombinace jednoduché a složité geometrie; **dynamické osvětlení je možné** (a tím pádem denní cyklus) |
| **~45 FPS** | kinematická hra na hraně tech dema — Nanite listí, plná geometrie, hodně detailu |

Zvlášť pojmenovaná past: **nedávej do hry 8K textury**, s kterými přicházejí Megascan assety.

**Změny, které se dají udělat jen v prvním changelistu** [(5:25)](https://www.youtube.com/watch?v=DxBKmQ-0kfw&t=325s). Tři nastavení a bonus:

- **Zakázat UMG bindings.** Legacy mechanismus, spouští se každý snímek. A dá se zakázat úplně — v nastavení editoru pro editor utility widgety i pro herní widgety se **property binding rule** nastaví na *prevent*, a pak už to nikdo v projektu nepoužije. *„Vidím je ve vašich Insights tracích. Prosím, nepoužívejte je."*
- **Collision complexity → use simple collision as complex collision.** Proč to bolí, je řetěz dvou opomenutí: kdo nenastaví počet LODů na Nanite meshi, nemá **fallback mesh** — a fallback mesh je právě to, co se použije na komplexní kolizi. Komplexní kolize na dvoumilionovém Megascan kameni je velmi drahá.
- **Prázdná startovní mapa editoru**, aby se editor otevíral rychleji. Zdůvodnění je zajímavější než to nastavení: *„čím rychleji můžeš iterovat, tím lepší to nakonec bude pro projekt."*
- **Pluginy:** zapnout **data validation** a **asset referencing restrictions** (druhý zajistí, že nikdo neodkáže na svůj developer content z hlavní mapy). A vypnout ty, které nepoužiješ — třeba providery verzování, které v týmu nepoužíváte.

**Soapbox o defaultech** [(7:47)](https://www.youtube.com/watch?v=DxBKmQ-0kfw&t=467s) je nejpřenositelnější věc celé přednášky. Přednášející ví, že by všechny primitive komponenty měly mít vypnuté *evaluate world position offset* — a vysvětluje, proč to Epic přesto nezmění: *„nechci, aby malý Timmy, co se učí Unreal poprvé, nevěděl, proč jeho world position offset shader nefunguje."* Závěr: **engine je nastavený pro učení, ne pro produkci — takže se u velkých her spousta věcí vypíná a mění na opt-in.**

**Scalability: v editoru se díváš na 30 FPS verzi hry** [(10:55)](https://www.youtube.com/watch?v=DxBKmQ-0kfw&t=655s). Všechny rendering skupiny jsou ve výchozím stavu na *Epic* — a **Epic je režim pro 30 snímků**. Kdokoli si může kliknout na *High*, ale protože je to první changelist a projekt ještě nikdo neotevřel, dá se to udělat **za všechny**: do `DefaultEditorSettings.ini` se zapíše sekce se scalability skupinami nastavenými na `2` (= High), a od té chvíle každý, kdo projekt otevře, vidí 60 FPS verzi. Uživatelské změny se ukládají jinam (do `Engine/Saved/Config`), takže se dá kdykoli resetovat na tenhle základ.

**A `DefaultDeviceProfiles.ini`** [(12:29)](https://www.youtube.com/watch?v=DxBKmQ-0kfw&t=749s), který je podle přednášejícího **povinný**, chceš-li 60 FPS. Device profily jsou hierarchické a dá se v nich přenastavit každá console variable i texture LOD group naráz. Nejdůležitější obsah je **rozlišovací žebřík**, poznatek z tech dema The Witcher 4:

1. **Primární rozlišení dynamicky mezi ~800 a 1080** (`r.DynamicRes`, `r.ScreenPercentage`) — tady se renderuje všechno, co závisí na rozlišení.
2. **TSR upscaluje na sekundární rozlišení 1440** (`r.SecondaryScreenPercentage.GameViewport = 75`). Důvod pro tuhle mez: TSR zvládá dvojnásobek, takže z 1080 na 4K, ale **pod ~1080 začíná být ztráta kvality vidět**.
3. **Prostorový upscale na finální 4K**, kde se překlopí na back buffer a **UI se kreslí v plné velikosti snímku** (`r.Upscale.Quality`).
4. **Rozpočet dynamického rozlišení = 16 ms**, min/max screen percentage 55–75.

Jeho vlastní shrnutí: *„je-li něco, co si vyfotíte, tak tohle. Soustředíme se na renderování menšího množství kvalitnějších pixelů a pak děláme sekundární upscaling."* Praktická past na konec: engine **sám nevybere** 60 FPS profil — musíš mít něco, co ho zvolí (device profile selector plugin, nebo pro pokročilé logika v `ULyraSettingsLocal`).

**A poslední položka na seznamu je rozpočet sám** [(45:53)](https://www.youtube.com/watch?v=DxBKmQ-0kfw&t=2753s), a je zajímavá tím, jak je otevřená: *„musím mít rozpočty, protože mi pomůžou určit, co optimalizovat — a kdy neoptimalizovat. A budu si muset rozmyslet, jestli má být cíl ve snímcích za sekundu, v procentu zmeškaných VSynců, v dynamickém rozlišení, nebo v milisekundách. To dělám hodně, hodně brzo, abych se k tomu vždycky mohl vrátit."* Tedy: **není jedna správná metrika, ale musíš si vybrat dřív, než začneš.**

> **Pozn.:** Tahle myšlenka má tvar, který se v knihovně opakuje pod jinými jmény: **některá rozhodnutí jsou levná jen na začátku.** Scalability za celý tým, device profily, verzování, struktura složek — [nástroje zvolené na nultý den](../teorie/jak-zacit.md#version-control-od-nulteho-dne) a [vlastnictví napřed, složky potom](../godot/projekt-a-vykon.md#vlastnictvi-napred-slozky-potom-main-game-jako-koordinator) jsou přesně tenhle typ. Nejcennější je ale ta věta o malém Timmym, protože pojmenovává něco obecnějšího než Unreal: **výchozí hodnoty jakéhokoli nástroje jsou optimalizované pro první hodinu použití, ne pro tisící.** Nedá se z toho odvodit „změň všechno", ale dá se z toho odvodit **prohlédni si defaulty, než na nich postavíš projekt** — a hlavně: zjisti, které z nich se dají změnit jen teď. Vlastní doplněk, který přednáška nemá: **zapiš si k tomu changelistu odůvodnění.** Za rok bude `r.SecondaryScreenPercentage.GameViewport = 75` vypadat jako náhodné číslo a někdo ho zvýší.

**Souvislosti:** [Rozpočet je peněženka](#rozpocet-je-penezenka-ne-cil) · [View modes: kde se ztrácí](#view-modes-kde-se-ztraci-nez-otevres-profiler) · [Textury a DLSS: right-size](textury-a-dlss.md#right-size-ne-vsechno-si-zaslouzi-4k) · [Optimalizace: Nanite, nebo LODy?](optimalizace.md#nanite-nebo-lody) · [Rejstřík: Device profile](../rejstrik.md#device-profile) · [Rejstřík: Scalability groups](../rejstrik.md#scalability-groups) · [Rejstřík: TSR](../rejstrik.md#tsr)

---

## View modes: kde se ztrácí, než otevřeš profiler

**Zdroj:** [UE5 Optimization Made Easy: Fundamentals](https://www.youtube.com/watch?v=zVNViTNHHdA) · [Dallas Drapeau](https://www.youtube.com/channel/UCatEMsDp-qF_bix_1ST2llw) · ~36 min, výklad · + [Maximizing Your Game's Performance in Unreal Engine](https://www.youtube.com/watch?v=GuIav71867E) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · Unreal Fest 2022, praktické příklady

**Shrnutí:** Optimalizační view modes jsou nejlevnější diagnostika, jakou UE má — a půlka z nich se nepoužívá, protože nikdo neřekl, co v nich hledat. Kapitola je ten chybějící legendový list: co znamená která barva, jaká je obvyklá příčina a jaká náprava. Háček, na který autor sám naráží hned v úvodu: **návody na optimalizaci si často vyrobí umělý problém** ve scéně, která nemá s tvojí nic společného — a pak ti prodají řešení, které jsi znal.

### Rozpad myšlenky

**Ta úvodní kritika** [(0:03)](https://www.youtube.com/watch?v=zVNViTNHHdA&t=3s) je důvod, proč tuhle myšlenku vůbec bereme: *„framerate se často umělé sníží způsobem, který umělec nebo programátor už umí spravit, a předvádí se to ve scéně, která nemá s tvojí nic společného — a ty se pak snažíš narvat jejich čtvercový kolík do své"* díry. Odtud jeho rámec: **nedávám rybu, dávám rybářský prut.**

**Legenda k view modes**, sestavená z obou zdrojů:

| view mode | co hledáš | obvyklá příčina | náprava |
|---|---|---|---|
| **Light complexity** | co nejvíc modré; bílé a fialové plochy = zle | příliš velký **attenuation radius** a překryv světel | zmenšit radius, vypnout vrhání stínů, ubrat světla |
| **Shader complexity** | převážně zelená | vrstvy a procedurální systémy v materiálu; **průhlednost je drahá vždy** | méně parametrů, textur a vrstev — ale ne pod úroveň, kde efekt přestane fungovat |
| **Quad overdraw** | překryvy geometrie | rozdělené assety (dům z jednotlivých fošen), maskované listí, fog cardy | slučovat aktéry, LODy, menší hustota |
| **Nanite overdraw** | totéž pro Nanite | maskované listí místo plné geometrie | plná geometrie, sloučené meshe |
| **Required texture resolution** | bílá = správně; násobky nad/pod | 8K textury na malých propech | right-sizing podle **vzdálenosti, ze které to hráč vidí** |
| **Raster bin** | co nejvíc assetů ve **stejném binu** | mix assetů z různých packů, každý s vlastním materiálem | společný materiál, textury do UDIMů, variace přes per-instance data |
| **VSM cached pages** | šedá (5.5+) / zelená (5.4 a starší) | listí s **invalidation behavior = Auto** a world position offset | přepnout na *rigid* nebo *static* — cenou je, že stíny přestanou houpat |
| **Mesh LOD coloration** | plynulý přechod barev se vzdáleností | zapomenuté listí, které zůstalo na LOD 0 do nekonečna | zkontrolovat po každém přepínání Nanite ↔ LODy |

**Nejčastější viník má jméno a je to attenuation radius.** Oba zdroje na něj narazili nezávisle. V prvním případě [(9:18)](https://www.youtube.com/watch?v=zVNViTNHHdA&t=558s) to byl jeden malý oheň ze stažené sady s radiusem **32 000**, který rozsvítil celý level. Ve druhém [(17:52)](https://www.youtube.com/watch?v=GuIav71867E&t=1072s) tucet bodových světel s radiusem 5 000 a zapnutým vrháním stínů — po zmenšení na 100 a vypnutí stínů **30 → 60 FPS, a scéna vypadá identicky**. Praktický důsledek pro cizí assety: **po importu zkontroluj attenuation radius světel.**

**Overdraw vysvětlené v jedné větě** [(18:00)](https://www.youtube.com/watch?v=zVNViTNHHdA&t=1080s): engine kreslí odzadu dopředu, takže čím víc věcí je naskládaných za sebou, tím víc pixelů se spočítá a zahodí. Odtud rada, která zní jako detail modelování a je to výkonové rozhodnutí: **stavíš-li dům z jednotlivých fošen, po dokončení je slouč.**

**A ta hranice, kterou si autor sám nastaví** [(17:09)](https://www.youtube.com/watch?v=zVNViTNHHdA&t=1029s) je nejpoctivější věta videa: *„snížíš komplexitu, jak můžeš, ale jen na určitou mez. Chceš se dostat do bodu, kde vyvažuješ optimalizaci proti tomu, jak to vypadá."* A závěrem: *„optimalizace není mávnutí kouzelnou hůlkou. Málokdy zaškrtneš checkbox a magicky získáš maximum snímků. Dávej pozor na tutoriály, které tvrdí přesně to. Optimalizace je častěji detektivní práce."*

> **Pozn.:** Řádek o **raster binech** je v té tabulce nejméně známý a nejvíc přenositelný, protože ukazuje **cenu rozmanitosti, ne množství**: dvě stě kamenů ze stejného materiálu je levnějších než dvacet kamenů z dvaceti materiálů. To je táž logika jako u [shading binů](profiling.md#cisla-se-kterymi-se-da-srovnavat) a u [draw callů](../rejstrik.md#draw-call) — a je to nejčastější tichá daň za skládání scény z několika stažených sad. Vlastní výhrada k řádku o VSM: **vypnutí invalidace není zdarma, jen se za to platí jinou valutou.** Houpající se stíny listí jsou u hry, kde je bouře součástí atmosféry, součástí produktu — a pak je správná odpověď hledat úspory jinde. To je přesně to rozhodování z [rozpočtové peněženky](#rozpocet-je-penezenka-ne-cil).

**Souvislosti:** [Profiling: co říká GPU profiler](profiling.md#co-rika-gpu-profiler-a-co-v-nem-nenajdes) *(další krok po view modes)* · [Optimalizace: voxelizace proti overdraw](optimalizace.md#voxelizace-nanite-listi-bez-overdraw) · [Textury a DLSS: right-size](textury-a-dlss.md#right-size-ne-vsechno-si-zaslouzi-4k) · [Materiály: master material](materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh) · [Rejstřík: Overdraw](../rejstrik.md#overdraw) · [Rejstřík: Raster bin](../rejstrik.md#raster-bin) · [Rejstřík: Virtual Shadow Maps](../rejstrik.md#virtual-shadow-maps)

---

## Proč malé trojúhelníky ničí GPU

**Zdroj:** [When Optimisations Work, But for the Wrong Reasons](https://www.youtube.com/watch?v=hf27qsQPRLQ) · [SimonDev](https://www.youtube.com/channel/UCEwhtpXrg5MmwlH04ANpL8A) · ~22 min, výklad grafického inženýra

**Shrnutí:** LODy a impostory fungují — to ví každý. Vysvětlení, které většina lidí má, je „méně vrcholů, méně práce", a autor (grafický inženýr s dvaceti lety praxe) ukáže, že **to vysvětlení není špatné, jen nevysvětluje, proč je efekt tak nepoměrně velký.** Skutečná příčina je v tom, jak je GPU postavené: nejmenší jednotka, se kterou pracuje, je **čtverec 2×2 pixely**. Háček, který z toho plyne: **trojúhelník menší než ten čtverec znamená, že se 75 % práce vypočítá a zahodí.**

### Rozpad myšlenky

**Nejdřív ta záhada** [(5:34)](https://www.youtube.com/watch?v=hf27qsQPRLQ&t=334s), postavená tak, aby intuice selhala nahlas. Fullscreen efekt s drahým pixel shaderem na 1920×1080 běží **100 FPS** — to je 2 miliony pixelů, každý s hromadou práce. Pak autor udělá „něco hloupého": jeden quad na každý pixel, tedy ~4 miliony trojúhelníků, s **prakticky prázdným** vertex shaderem. A framerate **katastrofálně spadne**. Když už zvládne miliony pixelů s drahým shaderem, proč ho položí pár milionů triviálních vrcholů?

**Proč intuice selhává**: od roku 2004 (Xenos v Xboxu 360, Nvidia s Teslou kolem 2006) mají GPU **unified shader architecture** — výpočetní jednotky se dynamicky dělí mezi vertex a pixel práci. Kdyby šlo jen o počet operací, vrcholy a pixely by byly zaměnitelné a rozdíl by nebyl.

**Kde se to láme: 2×2 quad** [(10:55)](https://www.youtube.com/watch?v=hf27qsQPRLQ&t=655s). Po rasterizaci se práce pixel shaderu neplánuje po jednotlivých pixelech, ale po **čtvercích 2×2**. Důvod je hardwarový a rozumný: čtverec 2×2 má **právě tak dost informace na výpočet gradientů textur** pro mip mapping, a přitom se dá implementovat jednoduše. *„Takže to dělá v podstatě každý."*

Z toho plyne odpověď na otázku „a co když nakreslím trojúhelník menší než ten čtverec?" — **GPU to udělá, ale výsledek zahodí.** Konkrétně v tom případě 75 % práce. A dělá to pořád, jen si toho většinou nevšimneš: **každý quad na hranici trojúhelníku** obsahuje pixely uvnitř i venku, a GPU spočítá celý quad. To je *„přirozený důsledek renderování"* a nedá se s tím nic dělat. **Co ovlivnit můžeš, je jaké trojúhelníky GPU podstrčíš.**

**Topologie meshe, nejen počet trojúhelníků** [(14:06)](https://www.youtube.com/watch?v=hf27qsQPRLQ&t=846s). Autor cituje experiment Emila Perssona (grafický inženýr v Epicu, ve grafických kruzích známý jako *humus*): tentýž mesh triangulovaný různě, **při konstantní ploše a konstantním počtu trojúhelníků**, má různý výkon. Nejlépe vyšel přístup s maximální plochou trojúhelníků, nejhůř dlouhé tenké trojúhelníky — protože ty mají špatné **quad utilization**. Praktický dopad: *„konkrétní způsob, jakým je mesh triangulovaný, má velmi přímý dopad na výkon."*

**A druhý strop: primitive assembly** [(17:24)](https://www.youtube.com/watch?v=hf27qsQPRLQ&t=1044s). Z whitepaperu AMD k architektuře RDNA autor vytáhne větu, která je celé záhadě jádrem: každá **primitive unit** dokáže do rasterizéru poslat **jeden primitiv za takt** (a culling zvládne dva). Takže i extrémně výkonné GPU je **shora omezené rychlostí, jakou umí trojúhelníky předat dál** — a zahltíš-li ho miliony malých, hladovíš tím pozdější fáze potrubí. *„Tuna výkonu se splachuje do záchodu."*

**A tím se to celé zavře** [(20:10)](https://www.youtube.com/watch?v=hf27qsQPRLQ&t=1210s): teď už víš, proč LODy a impostory fungují tak dobře — GPU není dobré v renderování mikrotrojúhelníků a věnuje jim nepoměrné množství výkonu, *„který mohl být použitý na to, aby něco jiného vypadalo lépe."* A rovnou z toho vypadne, **proč Nanite existuje v té podobě, v jaké existuje**: prezentace *Nanite, a Deep Dive* ze SIGGRAPHu 2021 potvrzuje totéž (GPU jsou postavená s ohledem na paralelní pixely, ne trojúhelníky; moderní GPU umí nastavit ~4 trojúhelníky za takt) — a proto Epic napsal pro mikrotrojúhelníky **vlastní softwarový rasterizér**.

> **Pozn.:** Tohle je nejcennější kus teorie v celé kapitole, protože **mění, co považuješ za drahé**. Bez něj zní „hodně trojúhelníků" jako problém množství a odpověď je „ubrat polygony". S ním je vidět, že problém je **poměr velikosti trojúhelníku k pixelu** — což je jiná věta a jiná náprava: LODy a impostory nejsou úspora dat, jsou to nástroje, jak držet trojúhelníky dost velké. Zároveň je to nejlepší doklad autorovy vlastní teze z titulku: **optimalizace, které fungují ze špatných důvodů, tě zradí u prvního netypického případu.** Kdo si myslí, že LOD je o počtu vrcholů, nebude tušit, proč mu vysoká hustota geometrie v dálce bolí i po přechodu na Nanite — a proč se v [rozpadu GPU snímku](profiling.md#co-rika-gpu-profiler-a-co-v-nem-nenajdes) na Nanite visual buffer nedá zatlačit žádnou konzolovou proměnnou. A jedna praktická vlastní poznámka: **tenhle jev je i důvod, proč se nevyplácí modelovat detail, který skončí pod jedním pixelem.** Nezmizí — zdraží.

**Souvislosti:** [Optimalizace: Nanite, nebo LODy?](optimalizace.md#nanite-nebo-lody) · [Optimalizace: voxelizace proti overdraw](optimalizace.md#voxelizace-nanite-listi-bez-overdraw) · [View modes](#view-modes-kde-se-ztraci-nez-otevres-profiler) · [Profiling: čísla, se kterými se dá srovnávat](profiling.md#cisla-se-kterymi-se-da-srovnavat) · [Rejstřík: Quad utilization](../rejstrik.md#quad-utilization) · [Rejstřík: Impostor](../rejstrik.md#impostor) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Rejstřík: Overdraw](../rejstrik.md#overdraw)
