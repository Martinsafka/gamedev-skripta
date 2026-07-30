# Paměť GPU: virtuální textury, pooly a nový profiler

Video paměť neroste tak rychle jako nároky na ni — a přibývají systémy, které z ní ukrajují (distance fields, Lumen, virtuální stíny, runtime virtuální textury). Odpovědí celého oboru je **virtualizace**: držet v paměti jen tu část dat, na kterou se zrovna kouká. Tahle kapitola vysvětluje, co to znamená, jak se to nastavuje a jak se zjistí, kolik toho vlastně potřebuješ.

Na konec patří nástroj, který k tomu vznikl: **přestavěný GPU profiler v 5.6**, jehož nová čísla umí rozlišit tři věci, které dřív splývaly — kdy GPU pracuje, kdy čeká na sebe a kdy čeká na tebe.

Nadřazená kapitola je [Rozpočet snímku](rozpocet-snimku.md); paměťovou stranu textur z pohledu autora řeší [Textury a DLSS](textury-a-dlss.md).

---

## Virtualizace: kniha, ze které čteš jen otevřenou stránku

**Zdroj:** [Optimizing UE5: Advanced Rendering, Graphics Performance, and Memory Management](https://www.youtube.com/watch?v=dj4kNnj4FAQ) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, Unreal Fest 2024

**Shrnutí:** Přednášející si všímá, že se slovo „virtual" v názvech enginových funkcí odbývá — *„prostě to přeskočíme"* — a přitom je to ta podstatná část. Vysvětlí ji na knize: čtečka nepotřebuje v paměti všechny stránky, jen tu otevřenou, kus okolí v nižší kvalitě a o zbytku skoro nic. Háček, který mění praxi: **virtuální textury nejsou jen pro 4K a víc** — ta myšlenka je stejná past jako „Nanite je jen pro milionové meshe".

### Rozpad myšlenky

**Definice, která se dá použít** [(3:07)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=187s): *„virtualizace znamená vyrobit řídkou verzi něčeho, abychom v pracovní paměti drželi a používali jen ty kousky, které potřebujeme."* Kniha je k tomu dobrý model, protože obsahuje i tu méně zřejmou část: **stránky vedle té otevřené se drží taky, ale v nižším rozlišení**, protože se v nich může rychle listovat.

**Proč to bylo nutné** [(4:40)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=280s): dřív se řešily hlavně textury a meshe; dnes si o VRAM říkají distance fields, Lumen, virtuální stíny a runtime virtuální textury naráz — a *„velikosti pamětí nerostly stejným tempem jako nároky na ně."* Největší žrout byly textury, takže se virtualizovaly první.

**Kolik to dělá, na skutečném projektu** [(7:02)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=422s). V architektonické ukázkové scéně:

| metrika | hodnota |
|---|---|
| klasický streaming pool (výchozí) | 2 000 MB |
| skutečně potřebná část z něj | **95 MB** |
| paměť virtuálních textur (fyzická + page table) | **~500 MB** |
| **mip 0 všech virtuálních textur na disku** | **22 GB** |

Tedy: 22 gigabajtů zdrojových dat se vykreslí z půl gigabajtu paměti. *„Bez streamování by to byl out-of-memory crash."*

**Dva druhy a jejich obchod** [(7:50)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=470s), formulované jako protiklad, který se dobře pamatuje: **streaming virtual textures šetří paměť za marginální cenu výkonu, runtime virtual textures šetří výkon za cenu paměti.** Runtime zná většina lidí z terénu; streamingové jsou podle přednášejícího **nedoceněné, protože působí děsivě**.

**Past, kvůli které se tomu vyhýbají**, je pravdivá, ale řešitelná: zapnout virtuální streamování na textuře nestačí — v materiálu se musí přepnout **sampler type** na virtuální variantu (virtual color, virtual grayscale, virtual normal…), a **jakmile je parametr virtuální, nesmí do něj přijít neviruální textura**. Zní to jako lavina ruční práce. Odpověď: **Convert to Virtual Texture** [(10:58)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=658s) projde reference nahoru, přepne sampler typy a pak i všechny ostatní textury, které do těch parametrů vstupují. Dá se filtrovat velikostí — *„512 možná nechceš, pod 128 rozhodně ne."*

**Tři věci, na které je lepší myslet dopředu** než konvertovat zpětně:

1. **Rozhodni se první den.** Zpětná konverze je funkční, ale něco se v ní přehlédne.
2. **Založ výchozí virtuální textury** pro každý sampler typ (default virtual color, default virtual normal…), aby v rodičovských materiálech nebyly tvrdé reference na konkrétní textury.
3. **Hlídej virtual texture stacks** [(12:30)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=750s) — počet **unikátních UV kombinací** v materiálu. Tři různá dláždění = tři stacky, protože pro každý se musí zvlášť vyhodnotit zpětná vazba. Vzorkovat víc textur toutéž UV kombinací stack **nepřidá**; přidat normálce jiné dláždění ano.

**Cena, kterou za to platíš**, je pojmenovaná poctivě z obou stran. Na CPU je nutné spočítat, které mipy a dlaždice nahrát — *„není to nijak extrémní a hodně z toho běží mimo herní vlákno."* Na GPU je to **indirekce**: nejdřív se vzorkuje page table, aby se zjistilo, kde dlaždice v paměti leží. U běžného materiálu zanedbatelné; u řetězu „virtuální flow mapa vyhledá virtuální texturu, která vyhledá virtuální texturu" už ne. A závěr, který zaznívá i jinde v knihovně: *„neber automaticky za dané, že když používáš streamingové virtuální textury, budeš mít špatný CPU profil. Vyzkoušej to. Tvůj projekt ti řekne, kde je problém."*

> **Pozn.:** Ta věta o „jen pro vysoké rozlišení" je nejcennější přenositelná část, protože popisuje **opakující se vzorec, jak se v týmech usadí nepravda o nástroji**: funkce se představí na extrémním příkladu (Nanite na milionovém meshi, virtuální textury na 8K), lidé si z příkladu odvodí podmínku použití, a pak funkci nepoužívají tam, kde by pomohla nejvíc. Vyplatí se to hlídat u každé nové enginové funkce: **ptej se, co je skutečná podmínka, ne co bylo na ukázce.** Vlastní doplněk k „rozhodni se první den": to rozhodnutí je hlavně o **výchozích materiálech a jejich sampler typech** — ne o texturách. Textury se dají převést hromadně kdykoli; přepsat sto materiálových instancí, které se mezitím rozjely po projektu, je práce úplně jiného řádu. To je táž logika jako u [nastavení, která se dají udělat jen v CL1](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1).

**Souvislosti:** [Pooly a jejich vodočty](#pooly-a-jejich-vodocty) *(kolik jich vlastně potřebuješ)* · [Textury a DLSS: unikátní textury, atlas, nebo virtual textures?](textury-a-dlss.md#unikatni-textury-atlas-nebo-virtual-textures) · [Rozpočet snímku: prvních 16,66 ms](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Rejstřík: Virtual texture](../rejstrik.md#virtual-texture) · [Rejstřík: Mip mapa](../rejstrik.md#mip-mapa) · [Rejstřík: Virtual texture stack](../rejstrik.md#virtual-texture-stack)

---

## Pooly a jejich vodočty

**Zdroj:** [Optimizing UE5: Advanced Rendering, Graphics Performance, and Memory Management](https://www.youtube.com/watch?v=dj4kNnj4FAQ) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, Unreal Fest 2024

**Shrnutí:** Paměť v UE5 není jeden pytel, ale **sada oddělených poolů** — a každý má výchozí velikost, která byla zvolená pro cizí projekt. Kapitola je o tom, jak zjistit, kolik z každého potřebuješ (engine ti to řekne sám, když ho k tomu donutíš), a jak vypadá, když se do poolu nevejdeš. Háček: **příliš velký pool je stejná chyba jako příliš malý**, jen tišší.

### Rozpad myšlenky

**Trik s příliš velkým náklaďákem** [(15:40)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=940s). Výchozí `r.Streaming.PoolSize` je 2 000 MB a v ukázkovém projektu se z něj používá stovka. Postup: **zmenšuj ho a nech engine, ať křičí.** Se zapnutými screen messages se v levém horním rohu objeví *streaming pool over budget* i s tím, o kolik — a tím máš vodočet, tedy skutečnou maximální potřebu, změřenou průchodem hry.

**Virtuální textury mají poolů víc** [(17:13)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=1033s), a to **zvlášť pro každý kompresní formát** (DXT5, BC4 a další) — což je věc, kterou nikdo nečeká. Od 5.4 na to existuje mechanismus: engine si během session vede **transient pool list** s dosaženými maximy a v rohu obrazovky připomíná *resizing virtual texture streaming pool*. Postup je pak mechanický: **opsat vodočty z transient listu do fixed poolu** v nastavení projektu (tedy do `DefaultEngine.ini`). V přednášce vyšlo DXT5 (base color) na 105 MB a BC4 na 39 MB. Poznámka z praxe: **auto-grow se vyplatí v editoru vypnout**, protože při každém zvětšení zadrhne.

**Jak vypadá pool, do kterého se nevejdeš**, popisuje autorovým příměrem: *„nechceš vozit oblázek pick-upem — ale taky nechceš vozit balvan v kupé."* Konkrétně: u klasického streamování **spadne rozlišení mipy**, u virtuálních textur se **textura z poolu vyhodí úplně** a začne problikávat.

**Nástroj, který to celé ukáže naráz** [(18:46)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=1126s): **Render Resource Viewer** (5.4) vypíše všechno, co scéna drží ve video paměti — page pool virtuálních textur, streamovací pool Nanitu, historii TSR, fyzické textury po kompresních typech, page table. *„Protože už to nejsou jen textury a meshe."*

**Dvě čísla ke streamování virtuálních textur, která se hodí znát** [(19:32)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=1172s):

- **`r.VT.FeedbackFactor`** — zpětná vazba se sbírá zhruba z **jednoho pixelu ze šestnácti**, s jitterem.
- **`r.VT.PageFreeThreshold`** — jak dlouho se stránka drží po tom, co zmizela z pohledu. Důvod je hezky konkrétní: otočíš-li se doleva a hned zpátky doprava, není čas texturu znovu nahrát.

A **tichý příznak, že je něco špatně**: `stat virtualtexturing` a v něm rostoucí **unmapped requests ve statické scéně**. Nehýbe-li se kamera, mělo by se to ustálit; roste-li to, kombinace feedback factoru, počtu stacků a počtu textur nestíhá pokrýt to, co je vidět, a vypadávají viditelné textury.

> **Pozn.:** Nejužitečnější věc téhle myšlenky je **postup, ne hodnoty**: zmenšuj pool, dokud si engine nestěžuje, a to je tvoje číslo. Je to obrácený směr než obvyklá praxe („narazil jsem na strop, zvětším pool") a je lepší, protože ti dá **měřenou horní mez místo odhadu s rezervou**. Zapadá to přesně mezi [prahy z profilování skutečné hry](profiling.md#cisla-se-kterymi-se-da-srovnavat) a [rozpočtovou logiku](rozpocet-snimku.md#rozpocet-je-penezenka-ne-cil): peníze, které nikde neutratíš, nejsou úspora — jsou to peníze, které chybí jinde. Jedna vlastní výhrada: **vodočet je jen tak dobrý jako průchod, kterým jsi ho naměřil.** Projdeš-li při měření polovinu hry, dostaneš maximum poloviny hry — takže tohle měření patří do [automatizovaného nočního běhu](profiling.md#nalez-neni-hotova-prace-predani), ne do jednorázové seance před vydáním.

**Souvislosti:** [Virtualizace](#virtualizace-kniha-ze-ktere-ctes-jen-otevrenou-stranku) · [Busy, wait, idle](#busy-wait-idle-co-rika-novy-gpu-profiler) · [Profiling: čísla, se kterými se dá srovnávat](profiling.md#cisla-se-kterymi-se-da-srovnavat) · [Textury a DLSS: right-size](textury-a-dlss.md#right-size-ne-vsechno-si-zaslouzi-4k) · [Rejstřík: Streaming pool](../rejstrik.md#streaming-pool) · [Rejstřík: Virtual texture](../rejstrik.md#virtual-texture)

---

## Busy, wait, idle: co říká nový GPU profiler

**Zdroj:** [New GPU Profiler and RHI Submission Pipeline](https://www.youtube.com/watch?v=vnbARZHccpQ) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~46 min, Unreal Fest Stockholm 2025 (principal rendering programmer, RHI tým)

**Shrnutí:** V 5.6 se `stat GPU`, `profileGPU` a Insights **přestavěly na společný zdroj dat**, takže si konečně navzájem odpovídají. Praktičtější je ale to, co přibylo: GPU už dávno nemá jednu frontu, a nový profiler to poprvé ukazuje — s rozlišením na **busy, wait a idle**. Háček, kvůli kterému se to vyplatí znát: **nenulový idle na GPU je diagnóza CPU**, ne grafiky.

### Rozpad myšlenky

**Předpoklad: GPU má víc front** [(0:50)](https://www.youtube.com/watch?v=vnbARZHccpQ&t=50s). Zhruba deset let mají GPU **grafickou frontu** (celá rasterizační pipeline plus compute) a jednu či víc **compute front** (jen compute shadery). Běží souběžně a sdílejí výpočetní jednotky. Když jedna produkuje data pro druhou, synchronizují se **fences** — a z toho vznikají **bubliny**: fronta stojí, protože čeká na signál.

**Tři sloupce a jak se čtou** [(5:36)](https://www.youtube.com/watch?v=vnbARZHccpQ&t=336s):

| sloupec | co znamená | jak to číst |
|---|---|---|
| **busy** | skutečná práce (běží command listy a shadery) | tohle vidíš i ve starších verzích |
| **wait** | fronta čeká na fence z jiné fronty | na compute frontě je vysoký běžně a **není to samo o sobě špatně**; na grafické frontě by měl být blízko nule |
| **idle** | GPU **došla práce od CPU** | nenulová hodnota = jsi aspoň částečně **CPU-bound** |

Ten třetí sloupec je nový a v Unrealu nikdy předtím nebyl. Je možný proto, že moderní API přesně vědí, kdy se práce odeslala a kdy se dokončila. Výhrada k jeho čtení: měř na **test buildu**, jinak nenulový idle jen znamená, že CPU brzdí editor.

**A jedna past při sčítání** [(7:54)](https://www.youtube.com/watch?v=vnbARZHccpQ&t=474s): protože fronty běží souběžně, **čísla z jednotlivých stránek se nesmí sčítat**. Celkový GPU čas snímku je `stat GPU time`, což je **sjednocení busy časů přes všechny fronty** — a je to zároveň číslo, kterým se řídí [dynamické rozlišení](frame-pacing.md#jak-to-vidi-hrac-360p-upscaling-a-stutter).

**`profileGPU`: dvě věci, které se hodí vědět** [(9:36)](https://www.youtube.com/watch?v=vnbARZHccpQ&t=576s). Nově vypisuje **exkluzivní i inkluzivní** časy a dělá **jednu tabulku na frontu**. A důležitá výhrada k měření konkrétního průchodu: **vypni async compute** (`r.RDG.AsyncCompute 0`), protože překrývající se práce na obou frontách si navzájem zkresluje časy. Drobnost, která umí ublížit čitelnosti: tabulka kreslí rámečky unicode znaky a některé editory je nezarovnají — pak pomůže jiný font, nebo přepnutí na ASCII.

**V Insights je to teprve užitečné** [(11:56)](https://www.youtube.com/watch?v=vnbARZHccpQ&t=716s): jedna časová osa na frontu, **zarovnaná s CPU**, s vyznačenými busy/wait/idle úseky — a **šipky závislostí mezi fencemi**, které se zobrazí kliknutím na značku. Vidíš tedy tok práce z CPU do GPU a zpět, a kde přesně vzniká bublina.

**Dvě páky, o kterých se jinde nedočteš** [(29:16)](https://www.youtube.com/watch?v=vnbARZHccpQ&t=1756s). Práce pro GPU se překládá v takzvaných **translate chains** a jejich šířka se ladí dvěma proměnnými: `r.RHICommand.ParallelTranslate.MaxCommandsPerTranslate` (kdy se řetěz uzavře a začne nový) a `...CombineSingleAndParallel`. Pravidlo je jednoduché: **na stroji s víc jádry jít do šířky, na omezeném naopak.** A jedna past pro ty, kdo píšou renderovací kód: **použití immediate command listu vynutí jednovláknový překlad** — bublina v potrubí. V RDG průchodech tedy ber základní typ command listu, ne immediate.

**A funkce, která se hodí, až bude zle** [(42:30)](https://www.youtube.com/watch?v=vnbARZHccpQ&t=2550s): **breadcrumby** teď procházejí celým systémem — jsou vidět na render vláknu, v paralelních RDG průchodech, na RHI vlákně, na GPU i v PIXu. Praktický důsledek: **crash v paralelním průchodu ti nově řekne, ve kterém průchodu** (dřív call stack končil u obecné task graph funkce), a při pádu GPU se z persistentního bufferu vytáhne, **kam až se snímek dostal**. Podezřelí jsou nejvíc zanořené uzly, které jsou ještě aktivní — s výhradou, že *„některý hardware hlásí dokončení práce, i když ještě doopravdy hotová není."*

> **Pozn.:** Za pozornost stojí, že tři sloupce nahradily jedno číslo — a **rozdělily jednu otázku na tři různé**. Dřív „GPU trvá 12 ms" mohlo znamenat cokoli; teď busy/wait/idle rozlišuje *dělám moc práce* od *špatně to plánuju* od *nedostávám práci dost rychle*, a každá z těch tří vede jinam. Je to tentýž posun, jaký v knihovně dělá [rozhodovací strom podle `stat unit`](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat), jen o patro níž. Praktická rada, kterou z přednášky odvozuju sám: **z celého toho hlubokého ponoru do RHI si laik odnese jednu položku — sloupec idle.** Zbytek je pro lidi, kteří píšou renderovací kód. Ale idle je něco, co může přečíst kdokoli, a odpovídá na otázku, kterou si klade každý: *„je moje hra brzděná grafikou, nebo procesorem?"*

**Souvislosti:** [Pooly a jejich vodočty](#pooly-a-jejich-vodocty) · [Profiling: rozhodovací strom](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Potrubí snímku](frame-pacing.md#snimek-neni-fronta-je-to-potrubi) *(tatáž logika na CPU straně)* · [Nanite: rozhodovací strom](nanite-do-hloubky.md#rozhodovaci-strom-je-to-vis-buffer-nebo-base-pass) · [Rejstřík: RHI](../rejstrik.md#rhi) · [Rejstřík: Async compute](../rejstrik.md#async-compute) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights)
