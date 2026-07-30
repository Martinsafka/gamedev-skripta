# Nanite do hloubky: rasterizace, overdraw a stínová cache

[Optimalizace scény](optimalizace.md#nanite-nebo-lody) porovnává Nanite s LODy jako volbu. Tahle kapitola jde o patro níž: **jak Nanite doopravdy utrácí čas**, jak se ta útrata dá rozdělit na dvě různé věci (rasterizaci a stínování), proč se overdraw autoruje při stavbě assetů místo aby se opravoval potom — a kdo ve skutečnosti invaliduje stínovou cache, když ti stíny žerou milisekundy.

Na konci je téma, kterému se materiály od Epicu vyhýbají: **hlasitá kritika Nanitu** a to, co z ní po odečtení rétoriky zbývá.

Diagnostický základ je v [Profilingu](profiling.md) a [Rozpočtu snímku](rozpocet-snimku.md#view-modes-kde-se-ztraci-nez-otevres-profiler); bez rozpočtu je většina toho, co následuje, předčasná optimalizace.

---

## Rozhodovací strom: je to vis buffer, nebo base pass?

**Zdroj:** [Optimizing UE5: Advanced Rendering, Graphics Performance, and Memory Management](https://www.youtube.com/watch?v=dj4kNnj4FAQ) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, Unreal Fest 2024

**Shrnutí:** Senior technical artist z Epicu popisuje **postup ladění Nanitu**, a začíná ho nezvykle: otázkou, jestli je vůbec co ladit. *„Mluvil jsem s lidmi, kteří ladí scénu a říkají ‚musíme vyřešit ten problém s Nanitem'. Skvělé — jaký máš na Nanite rozpočet? Kolik milisekund z šestnácti jsi ochotný na Nanite utratit? Je Nanite nad tím? Fajn, teď se o tom můžeme bavit."* Odtud se strom větví na dvě různé útraty. Háček, který obrací zaběhnutou praxi: **overdraw view mode není detektor problému, ale nástroj na diagnózu problému, který už jsi změřil.**

### Rozpad myšlenky

**První větvení: rasterizace, nebo stínování?** [(29:39)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=1779s) Nanite utrácí na dvou místech a chovají se úplně jinak:

| položka v GPU profileru | co to je | čím se řídí |
|---|---|---|
| **Nanite visual buffer** | rasterizace — převod geometrie na pixely | kolik a jakých trojúhelníků, kolik programovatelné rasterizace |
| **Nanite base pass** | stínování rasterizovaných pixelů | počet shading binů a **cena materiálů** |

Ve vis bufferu se dá jít ještě o patro hlouběji: `r.Nanite.ShowMeshDrawEvents 1` rozdělí v profileru *draw geometry main pass* na **hardware rasterize** a **software rasterize** a uvnitř na **fixed function** (vše neprůhledné a nedeformující se) proti **programmable** (WPO, maskované materiály a spol.).

**Druhé větvení: binární hledání ve view modes** [(31:12)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=1872s). Je-li programovatelná rasterizace drahá, dvě view modes rozhodnou, která z jejích příčin to je:

1. **Evaluate WPO** — svítí-li scéna převážně červeně (tedy WPO se *nevyhodnocuje*) a přesto je programovatelná rasterizace drahá, WPO to není.
2. **Pixel programmable** — ukazuje maskované materiály, pixel depth offset a dynamický displacement. *„Wow, pixel programmable věcí je tu mnohem víc než těch, co vyhodnocují WPO — takže se první podívám na maskované materiály."*
3. Není-li ani jedno, zbývá **fixed function** — a **teprve tady** se sahá po overdraw.

**A ta oprava návyku** [(31:58)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=1918s), kvůli které tahle myšlenka v knihovně je: *„všímám si, že hodně lidí jde rovnou na Nanite visualization → overdraw a říká: tady je problém s výkonem Nanitu. A tak bych to nerad. Chci, abys ten view mode používal takhle: všiml jsem si výkonového problému a tohle je nástroj, kterým zjistím, odkud pochází. Neříká ti, že problém existuje."* Bílé pixely v overdraw view mode samy o sobě nejsou nález.

**Base pass má taky jen dvě příčiny** [(36:37)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2197s) a rozliší se stejně mechanicky: buď **počet shading binů** (`r.Nanite.ShowStats` vypíše celkový počet a počet prázdných — rozdíl je efektivní počet draw callů), nebo **drahé materiály**. *„A teprve pak se konečně můžeme bavit o výkonu materiálů."*

**Bonus, který od 5.4 dostáváš zadarmo**: stínování Nanitu se přesunulo do **compute shaderů**, takže se prázdné shading biny dají zkomprimovat a jejich režie z velké části zmizela — a přišlo **variable rate shading pro Nanite**, díky kterému se u čtverce 2×2 skutečně využijí všechny čtyři pixely místo čtyř samostatných průchodů. Podmínka: **materiál nesmí používat `DDX`/`DDY`**, protože explicitní derivace variable rate shading rozbíjejí. Kdo je hledá ručně, dělá zbytečnou práci — `r.Nanite.Visualize.Advanced 1` odemkne view mode **no derivative ops**, kde jsou červeně přesně ty materiály, které to dělají.

> **Pozn.:** Nejcennější věc téhle myšlenky není strom, ale **jeho vstupní podmínka**. „Máš na Nanite rozpočet?" je otázka, která zabije většinu diskuzí o výkonu dřív, než začnou — a je to táž otázka jako [rozpočet jako peněženka](rozpocet-snimku.md#rozpocet-je-penezenka-ne-cil), jen zaměřená na jeden systém. Za pozornost stojí i to, jak přesně ten výklad pojmenovává **chybu čtení nástroje**: overdraw view mode je barevný, dramatický a okamžitě srozumitelný, takže svádí k tomu, aby se používal jako detektor. Jenže **nástroj, který vypadá jako odpověď, ale je to jen mapa**, je zrádnější než nástroj, kterému nikdo nerozumí. Tohle platí i mimo Unreal: view modes ukazují *jev*, ne *cenu* — cenu ukazuje jen profiler.

**Souvislosti:** [Overdraw se autoruje](#overdraw-se-autoruje-ne-opravuje) *(co se s tím nálezem dělá)* · [Spor o Nanite](#spor-o-nanite-co-tvrdi-kritika-a-co-z-toho-plati) · [Rozpočet snímku: view modes](rozpocet-snimku.md#view-modes-kde-se-ztraci-nez-otevres-profiler) · [Profiling: co říká GPU profiler](profiling.md#co-rika-gpu-profiler-a-co-v-nem-nenajdes) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Rejstřík: Shading bin](../rejstrik.md#shading-bin) · [Rejstřík: Overdraw](../rejstrik.md#overdraw)

---

## Overdraw se autoruje, ne opravuje

**Zdroj:** [Optimizing UE5: Advanced Rendering, Graphics Performance, and Memory Management](https://www.youtube.com/watch?v=dj4kNnj4FAQ) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, Unreal Fest 2024 · + [Nanite Forest Optimisation in Unreal Engine 5](https://www.youtube.com/watch?v=uE4cGZjMfuY) · [Filgeck](https://www.youtube.com/channel/UC_vaEIlHfMxbskfXHdO3peQ) · ~21 min, praxe

**Shrnutí:** Nanite umí zahodit clustery, které nejsou vidět — ale **jen celé clustery**. A jestli se cluster dá zahodit, rozhoduje **topologie meshe**, tedy rozhodnutí, které padlo dávno před optimalizací. Kontejner z dlouhých tenkých trojúhelníků má celou stěnu ve dvou třech clusterech, takže stačí kousek jeho horní hrany a musí se rasterizovat celý — i s tím, co je za ním. Háček, kvůli kterému se tomu vyplatí rozumět: **tohle je preventivní opatření, ne oprava.**

### Rozpad myšlenky

**Jak culling clusterů selže** [(33:30)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2010s): přednášející ukáže dva lodní kontejnery za sebou. V drátěném modelu jsou stěny složené z **dlouhých tenkých trojúhelníků**, ve view mode *clusters* je celá stěna pár velkých clusterů. Důsledek: *„ten kontejner skoro úplně přemalovává ten druhý, protože ty clustery jsou částečně viditelné. I když jedu podél, vidím tu horní hranu — takže musím rasterizovat všechno pod ní."*

**Náprava, která není nastavením**: přednášející tytéž kontejnery **rovnoměrně přesíťoval** (geometry scripting, hrubě, jen na ukázku). Ve view mode *clusters* jsou teď clustery rozházené po celé ploše — a v overdraw view mode se kontejner vzadu **částečně cullne**, a dokonce **cullne částečně sám sebe**. Pravidlo: *„stavěj obsah s myšlenkou na cluster culling."*

**Dvě další chyby, které se dělají při skládání scény**, a obě jsou o rozvržení, ne o assetech:

- **Nemačkej meshe do sebe** [(35:04)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2104s). Clustery se cullují **podle bounds**, takže u těsně naskládaných objektů s prolínajícími se clustery culling nefunguje a overdraw naroste.
- **Greeble na velké ploché ploše je naopak v pořádku** [(35:50)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2150s): ta plocha všechno pod sebou zakryje. Hot spoty vzniknou jen při pohledu z ostrého úhlu podél ní.

**Praktický protějšek z reálného projektu** [(12:26)](https://www.youtube.com/watch?v=uE4cGZjMfuY&t=746s): autor lesní scény narazí na tutéž věc z opačné strany. Jeho rada zní kacířsky, dokud si nepřipomeneš, jak Nanite rasterizuje: *„Nanite si nerozumí s opacity maskou, takže je lepší vymodelovat každý list jako 3D geometrii."* Tedy **víc trojúhelníků výměnou za méně průhlednosti** — což je přesně obrácený instinkt, než jaký má většina lidí, a v Nanite světě je správný. Ke stejné rodině patří jeho `keep triangle percent` se zapnutým **preserve area** u vysokorozlišených meshů.

> **Pozn.:** Tahle myšlenka je nejlepší doklad toho, že **výkon je vlastnost autorského rozhodnutí, ne nastavení**. Topologii kontejneru nezmění žádná konzolová proměnná; buď je udělaná tak, aby se dala částečně cullnout, nebo není. Praktický důsledek pro tým: **cluster culling patří do style guide k modelování**, ne do optimalizačního sprintu na konci. Souvisí to přímo s [tím, proč malé trojúhelníky ničí GPU](rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu) — jen z druhé strany: tam šlo o velikost trojúhelníku vůči pixelu, tady o to, jak jsou trojúhelníky seskupené. Jedna vlastní výhrada k „modeluj listy jako geometrii": platí to pro Nanite listí a **neplatí** to univerzálně. U LOD pipeline je maskovaná plocha pořád levnější — takže je to rozhodnutí navázané na volbu systému, ne obecné pravidlo, a je potřeba ho v projektu udělat jednou a nahlas.

**Souvislosti:** [Rozhodovací strom](#rozhodovaci-strom-je-to-vis-buffer-nebo-base-pass) · [Kdo invaliduje stínovou cache](#kdo-invaliduje-stinovou-cache) · [Rozpočet snímku: proč malé trojúhelníky ničí GPU](rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu) · [Optimalizace: voxelizace proti overdraw](optimalizace.md#voxelizace-nanite-listi-bez-overdraw) · [Optimalizace: foliage I](optimalizace.md#foliage-optimalizace-i-kotva-vykonu-a-velka-trojka) · [Rejstřík: Overdraw](../rejstrik.md#overdraw) · [Rejstřík: Cluster culling](../rejstrik.md#cluster-culling)

---

## Kdo invaliduje stínovou cache

**Zdroj:** [Optimizing UE5: Advanced Rendering…](https://www.youtube.com/watch?v=dj4kNnj4FAQ) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~51 min, Unreal Fest 2024 · + [1-hour of Unreal GPU Optimization Tips & Tricks](https://www.youtube.com/watch?v=c2MH20OPSw0) · [Tom Looman](https://www.youtube.com/channel/UCnO-xQvmsO1WwKFq-5Pvj0Q) · ~62 min, praxe · + [Nanite Forest Optimisation](https://www.youtube.com/watch?v=uE4cGZjMfuY) · [Filgeck](https://www.youtube.com/channel/UC_vaEIlHfMxbskfXHdO3peQ) · ~21 min

**Shrnutí:** Virtual shadow maps stojí a padají s **cachováním**: stránky, které se nemění, se překreslovat nemusí. Celý výkon systému je tedy o jediné otázce — **kdo ti tu cache invaliduje**. A odpověď bývá překvapivá: nejde o pohybující se objekty, ale o **materiál**, který má někde zapnutou věc, o které nevíš. Háček: nejlevnější varianta je nechat stín houpat se jen tam, kde to hráč pozná.

### Rozpad myšlenky

**Reálný nález, na kterém je to nejlépe vidět** [(6:20)](https://www.youtube.com/watch?v=c2MH20OPSw0&t=380s). V ukázkové scéně od Megascans se **každá stránka jednoho velkého světla invaliduje každý snímek**, přestože se nic nehýbe. View mode *VSM → cached pages* to ukáže modře. Příčina se najde jinde: **Nanite visualization → Evaluate WPO** je celá zelená, tedy world position offset se vyhodnocuje na všem. V master materiálu od Megascans je material function s **contact shadows** a pixel depth offsetem — a **bez nastavené WPO disabled distance** to znamená trvalou invalidaci. Po obejití: **shadow depth 1,7 → 1,0 ms**, vizuálně beze změny. Ověřeno čísly přes `r.Shadow.Virtual.ShowStats` (dynamic cache 65 → dynamic invalidators 65 a zpět).

Praktická drobnost, na kterou se snadno narazí: **ty statistiky se nezobrazí bez `r.ShaderPrint 1`.**

**Totéž o patro dřív, v lesní scéně** [(13:12)](https://www.youtube.com/watch?v=uE4cGZjMfuY&t=792s): stromy ve větru přepočítávají stín každý snímek. Náprava je jedno pole — **shadow cache invalidation behavior → Rigid** (výchozí *Auto* nechává WPO invalidovat), ať už ve foliage nástroji nebo v PCG grafu. Cena je poctivě pojmenovaná: **stíny přestanou houpat**. Autor k tomu dodává druhou polovinu řešení — **WPO disabled distance** (u něj 20 000 pro stromy, výrazně méně pro trávu), takže vzdálené stromy vítr přestane zajímat úplně.

**Co se změnilo v 5.4 a proč to dává smysl** [(44:21)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2661s): dřív platilo, že co jednou invalidovalo cache, zůstalo napořád „dynamické" — takže strom, od kterého ses vzdálil za jeho WPO disabled distance, se pořád kreslil do dynamických stránek, i když už neinvalidoval nic. Nově se to po čase vrací mezi statické; práh řídí `r.Shadow.Virtual.Cache.StaticSeparate.FrameStaticThreshold`. Logika je stejná jako u [stránek virtuálních textur](gpu-pamet.md#pooly-a-jejich-vodocty): **přepnutí tam a zpět něco stojí, takže se nechává chvíli doznít.**

**Druhá změna v 5.4 a artefakt, podle kterého ji poznáš** [(45:56)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2756s): dřív objekt s WPO invalidoval stránky **po celé délce svého stínu**, tedy při nízkém slunci extrémně daleko — což je proti intuici, protože WPO disabled distance by měla platit i na stín. Nově se disabled distance zaokrouhlí nahoru na nejbližší clip map úroveň a dál se stránky neinvalidují. Přednášející si k tomu naschvál vyrobil artefakt: s `r.Shadow.Virtual.ClipmapWPODisableDistance.LODBias 0` se **půlka stínu hýbe a půlka stojí**. *„Kdybys to někdy uviděl, teď víš, co to je."*

**A pořadí, ve kterém se to má ladit** [(47:29)](https://www.youtube.com/watch?v=dj4kNnj4FAQ&t=2849s), je nejužitečnější věta celé myšlenky: *„než začneš optimalizovat VSM a invalidace, začni u Nanite vis bufferu."* Vykreslení virtuálních stínů je totiž **taky Nanite průchod** — v GPU profileru pod *shadow depths → render virtual shadow maps → Nanite draw geometry*. Optimalizace vis bufferu se tím pádem projeví dvakrát.

> **Pozn.:** Tahle myšlenka má nejlepší poměr užitku k pracnosti z celé kapitoly: **jedno pole v materiálu nebo ve foliage nastavení, desetiny milisekundy, nulová vizuální ztráta.** Zároveň dobře ilustruje, proč se cizí assety musí kontrolovat: obě nalezené příčiny přišly z **hotového obsahu** (Megascans master materiál, foliage s výchozím *Auto*) — tedy z míst, kam nikdo nekouká, protože „to je přece od Epicu". Praktické pravidlo, které z toho plyne a přednášky ho neříkají nahlas: **po importu jakékoli sady se podívej na Evaluate WPO a na cached pages, ještě než začneš stavět.** Souvisí to s [attenuation radiusem u cizích světel](rozpocet-snimku.md#view-modes-kde-se-ztraci-nez-otevres-profiler) — je to tentýž typ tiché daně za hotový obsah.

**Souvislosti:** [Rozhodovací strom](#rozhodovaci-strom-je-to-vis-buffer-nebo-base-pass) *(vis buffer se projeví i ve stínech)* · [Overdraw se autoruje](#overdraw-se-autoruje-ne-opravuje) · [Optimalizační průchod](gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) · [Osvětlení](osvetleni.md) · [Rejstřík: Virtual Shadow Maps](../rejstrik.md#virtual-shadow-maps) · [Rejstřík: WPO](../rejstrik.md#wpo)

---

## Spor o Nanite: co tvrdí kritika a co z toho platí

**Zdroj:** [Epic's Unreal Optimization Disaster | Why Nanite Tanks Performance!](https://www.youtube.com/watch?v=M00DGjAP-mU) · [Threat Interactive](https://www.youtube.com/channel/UC2ksme4hP4Nx97ilFTQ0K0Q) · ~13 min, polemika · + protipozice z [Optimizing UE5](https://www.youtube.com/watch?v=dj4kNnj4FAQ) a [When Optimisations Work, But for the Wrong Reasons](https://www.youtube.com/watch?v=hf27qsQPRLQ)

**Shrnutí:** Zbytek téhle kapitoly stojí na materiálech od Epicu. Tahle myšlenka je tu proto, že **existuje hlasitá opoziční pozice** a stojí za to vědět, co přesně tvrdí — a co z toho po odečtení rétoriky zbývá. Jádro tvrzení: *„šestimilionová scéna běžela o 50 % rychleji bez Nanitu"*, a mechanismem je [quad overdraw](rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu). Háček, který z toho dělá poučnou položku: **mechanismus je doložený a nezávisle potvrzený, ale závěr z něj neplyne automaticky.**

### Rozpad myšlenky

**Co se tvrdí** [(1:35)](https://www.youtube.com/watch?v=M00DGjAP-mU&t=95s). Autor vytáhl scénu z hry osmé generace (přes 6 milionů trojúhelníků), importoval ji do Unrealu a naměřil, že **bez Nanitu běží o polovinu rychleji**. Vysvětlení, které k tomu dává, je technicky správné a v knihovně už zaznělo z úplně jiného zdroje: vývojáři her osmé generace **autorovali LODy tak, aby držely quad overdraw pod kontrolou**, což Nanitu chybí.

Součástí videa je i **legenda k overdraw view mode**, která se jinde těžko shání: tmavě modrá = quad plně využitý · světle modrá = zahozena čtvrtina · tmavě zelená = polovina · světle zelená = **75 % výkonu zahozeno**. V jeho referenční scéně bylo asi 45 % quadů plně využitých.

**Test, který je na tom nejzajímavější** [(4:43)](https://www.youtube.com/watch?v=M00DGjAP-mU&t=283s): postavil za objekty krychli, aby aktivoval všechny vzorkovací body, a měřil růst ceny. Bez Nanitu přidala krychle **28 %** ke geometrickým časům, s Nanitem **41 %** — a základní čas byl **11 ms proti 50 ms**. Tedy nejen strmější růst, ale i vyšší výchozí bod.

**Metodická kritika, která je nejcennější přenositelnou částí** [(5:29)](https://www.youtube.com/watch?v=M00DGjAP-mU&t=329s). Autor rozebírá populární srovnání „Nanite = 15 → 50 FPS" a ukáže, že testující **neměl zapnuté žádné LODy**, měl zapnuté **virtual shadow maps** (které Epic sám dokumentuje jako pomalejší na ne-Nanite meshích) a **netušil, jaký overdraw ty meshe vyrábějí**. Tedy: srovnával Nanite ne s dobře udělanou alternativou, ale s nejhorším možným případem. Přirovnává to k srovnávání upscaleru s rozbitým antialiasingem: *„najednou máš řešení problému, který nemusel existovat."*

**A jedna věcná námitka k pro-Nanite argumentu** [(7:03)](https://www.youtube.com/watch?v=M00DGjAP-mU&t=423s): draw cally. Nanite je ruší, to je pravda — ale slučování meshů je uměl řešit i předtím. Problém podle něj je, že **slučování v Unrealu slučuje i LOD logiku**, takže se dají slučovat jen objekty blízko sebe místo těch, o kterých víš, že budou v paměti spolu.

**Co proti tomu stojí.** Materiál od Epicu ve stejné dávce popisuje, že se overdraw u Nanitu dá **výrazně ovlivnit topologií a rozvržením** ([cluster culling](#overdraw-se-autoruje-ne-opravuje)), a že od 5.4 zmizela velká část režie prázdných shading binů a přišlo variable rate shading. A z [nezávislého výkladu o quad utilization](rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu) plyne, že Epic si softwarový rasterizér pro mikrotrojúhelníky napsal **právě proto**, že tenhle problém zná.

> **Pozn.:** Tuhle položku bereme jako **cvičení v oddělení mechanismu od závěru**. Mechanismus (quad overdraw, cena mikrotrojúhelníků, VSM navržené pro Nanite) je doložený a potvrzuje ho i grafický inženýr bez vztahu k tomuhle sporu. Závěr „Nanite je horší" z něj ale neplyne, protože obě strany srovnávají něco jiného: kritika porovnává Nanite s **ručně vyladěnými LODy z AAA produkce**, obhajoba s **tím, co studio reálně dodá** při daném rozpočtu času. Obojí může být pravda naráz — a rozhodnutí pak nezávisí na tom, kdo má lepší benchmark, ale na tom, **kolik autorské práce si můžeš dovolit**. Zároveň je poctivé říct, co na tom zdroji nesedí: je **silně rétorický** (název, slova jako „lež" a „disaster"), obsahuje spekulace o motivech firem, které nejsou doložitelné, a přechází v návrh vlastního AI řešení, které je zatím jen nápad. Metodická část ale platí bez ohledu na tón, a je vlastně tatáž, jakou má [reprodukovatelný test](profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic): **srovnání, ve kterém se liší víc věcí naráz, není důkaz ničeho** — a to platí i pro srovnání, která vyzní ve prospěch věci, kterou máš rád.

**Souvislosti:** [Rozpočet snímku: proč malé trojúhelníky ničí GPU](rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu) *(mechanismus nezávisle vysvětlený)* · [Overdraw se autoruje](#overdraw-se-autoruje-ne-opravuje) · [Optimalizace: Nanite, nebo LODy?](optimalizace.md#nanite-nebo-lody) · [Profiling: reprodukovatelný test](profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic) · [Rejstřík: Quad utilization](../rejstrik.md#quad-utilization) · [Rejstřík: Overdraw](../rejstrik.md#overdraw)
