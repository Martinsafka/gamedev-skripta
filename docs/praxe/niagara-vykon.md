# Niagara: výkon částic

Částice jsou nejčastější tichý žrout v hotové hře, protože se přidávají na konci, po jednom efektu, a nikdy jich není „moc" — dokud jich není dvě stě naráz. Jádro kapitoly je přednáška konzultanta, který k projektům přichází **na konci produkce**, kdy je obsah odsouhlasený a nedá se měnit — takže se soustředí na to, co se dá spravit **bez zásahu do efektů**: kolik systémů vůbec tiká a jak jim říct, aby přestaly. Poslední myšlenka jde opačným směrem a ukazuje, jak Niagaru od začátku navrhnout levně: živý svět z tvorů, kteří na hráče reagují, ale nic nerozhodují.

Metodický základ je v [Profilingu](profiling.md) a [Rozpočtu snímku](rozpocet-snimku.md); praktický nález s Niagarou v cizí scéně (59 systémů, z toho 57 mimo obraz) je v [Optimalizačním průchodu](gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda).

---

## Diagnostika Niagary: pět statistik a jedna past

**Zdroj:** [Optimizing Niagara: a Practical Approach to Performant Worlds](https://www.youtube.com/watch?v=71c5yv-XeY8) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~47 min, Unreal Fest Orlando 2025 (senior technical artist, Tanglewood Games) · + [How I Optimized My Game to Over 200 FPS in UE5](https://www.youtube.com/watch?v=xr-2TrMUd9w) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~23 min, devlog (Niagara Debugger v praxi)

**Shrnutí:** Niagara je v profileru **rozprostřená napříč vlákny a na náhodných místech snímku** — protože kde se objeví, závisí na tom, co simulace zrovna dělá (čte kosti, čeká na GPU, vrací data zpátky). `stat unit` proto o částicích neřekne skoro nic a je potřeba pět specializovaných statistik. Háček, který stojí za celou myšlenkou: **bez `-statnamedevents` se Niagara v Unreal Insights vůbec neobjeví.**

### Rozpad myšlenky

**Žebřík statistik** [(4:42)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=282s), od hrubého k detailnímu:

| příkaz | co dá |
|---|---|
| `stat NiagaraOverview` | souhrn ceny na vláknech: render thread, game thread a **GT concurrent** (všechna worker vlákna) |
| `stat Niagara` | detail — které konkrétní volání se do těch součtů sčítají |
| `stat NiagaraSystems` | totéž **po systémech**, včetně cesty k assetu (nejrychlejší cesta k viníkovi) |
| `stat NiagaraEmitters` | po emitterech **a v jakém systému** — týž emitter může být problém v jednom systému a neškodný v druhém |

Ke `stat FPS` a `stat unit` přednášející dodává mírně provokativní poznámku, se kterou se dá souhlasit: *„nemáš-li je zapnuté pořád, děláš to špatně."*

**Číslo, které se nedá čít absolutně** [(4:42)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=282s) — a je to nejcennější kalibrace celé myšlenky. **GT concurrent bude vždycky relativně velký**, protože Niagara jde záměrně do šířky. Podstatné je, kolik jader ta šířka má k dispozici: *„máš-li šestnáctijádrovou bestii, to číslo se na výsledném framerate nemusí projevit vůbec. Jsi-li na Nintendo Switchi nebo máš čtyřjádro, tytéž čtyři milisekundy tě zasáhnou úplně jinak."*

**Druhá past ve čtení: render thread není jen renderování** [(5:29)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=329s). **Každá GPU simulace potřebuje GPU dispatch**, a ten se odehrává na render vlákně — takže částice mohou zdražovat render thread i tehdy, když je vůbec nevidíš.

**Niagara Debugger** [(7:50)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=470s) je autorův favorit, s jedním důležitým omezením: **funguje jen v editoru**, v zabaleném buildu ne. Dvě věci v něm stojí za znalost:

- **Debug HUD** — čísla jako jinde, ale navíc **stav systému ve škálování** a **GPU compute**, jehož cenu je jinak dost obtížné vidět. Plus zobrazení systémů ve světě, které odhalí *„tuny systémů v místech, kam ani nevidíš — třeba proto, že jsi vypnul renderer, ale systém pořád tiká."*
- **Effects Outliner** — sejme snímek a vypíše, **který aktér ten systém vlastní** a v jakém je stavu z hlediska poolingu. Právě to vlastnictví je věc, kterou statistiky nedají a bez které se nález nedá předat.

**A ta past s Insights** [(10:58)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=658s): *„než uděláš jakoukoli captureu pro Niagaru, musíš mít zapnuté `-statnamedevents`. Jinak se Niagara v záznamu neobjeví."* Přednášející u toho stráví polovinu svého pracovního času a dodává, proč to stojí za tu přípravu: **někdy Niagara vůbec není vinná a jen tak vypadá** — třeba když někdo spawnuje moc postav a všechny hoří naráz.

**Z praxe sólo vývojáře: Niagara Debugger** [(15:40)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=940s). `Tools → Debug → Niagara Debugger` a v nabídce u HUD volba *Show Overview* vypíše za běhu systémy ve scéně, kolik z nich je aktivních, jejich scalability, počty emitorů a částic i paměť [(16:27)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=987s). Na sólo hře z toho vyjdou tři nálezy, každý jiného druhu: efekt z Fabu, jehož počet aktivních instancí po každém použití **rostl a nikdy neklesal** — emitor spouštějící zvuk neměl *Kill Particles*, takže nikdy neumřel [(17:13)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=1033s), [(18:01)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=1081s); jedová stopa za nepřáteli, která se spawnovala pořád, i při pomalé chůzi, protože kontrolovala rychlost místo vzdálenosti od posledního spawnu [(19:34)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=1174s); a systémy s 20 000 částic, ze kterých stačilo udělat méně větších [(20:20)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=1220s). Žádný z těch nálezů by čtení milisekund samo neodhalilo — počty, které rostou, jsou vidět jen v přehledu.

> **Pozn.:** Nejpřenositelnější věc téhle myšlenky je ta kalibrace o jádrech: **absolutní milisekundy na paralelním vlákně nejsou metrika, dokud neřekneš na jakém stroji.** Přednášející si k tomu pro měření **omezil procesor na čtyři vlákna**, aby vůbec viděl, co se na slabším hardwaru děje — což je táž disciplína jako [`-corelimit 14`](profiling.md#cisla-se-kterymi-se-da-srovnavat) a stojí za převzetí. Druhá věc, kterou si odsud bereme, je hodnota **vlastnictví** v Effects Outlineru: statistika řekne „tenhle systém je drahý", ale nález se dá předat teprve tehdy, když víš, **který aktér ho spawnuje** — a to je přesně ta hranice, o které mluví [předávka nálezu](profiling.md#nalez-neni-hotova-prace-predani).

**Souvislosti:** [Effect type](#effect-type-jeden-asset-ktery-rozhoduje-o-vsem) *(co se s nálezem dělá)* · [Profiling: rozhodovací strom](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Optimalizační průchod: 59 systémů](gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights) · [Rejstřík: Particle system](../rejstrik.md#particle-system)

---

## Effect type: jeden asset, který rozhoduje o všem

**Zdroj:** [Optimizing Niagara: a Practical Approach to Performant Worlds](https://www.youtube.com/watch?v=71c5yv-XeY8) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~47 min, Unreal Fest Orlando 2025

**Shrnutí:** Effect type je podle přednášejícího *„páteř skoro všeho, o čem dnes mluvíme"* — jeden malý asset, který se přiřadí systému a řekne mu, kdy nemá tikat. Je to nejlepší poměr práce k výsledku v celé kapitole, protože **nevyžaduje sáhnout na obsah**. Háček, kvůli kterému stojí za pozornost i jeho druhá strana: **při tisících systémů se z něj sám stane problém.**

### Rozpad myšlenky

**Co všechno v něm je** [(14:55)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=895s) — a je to překvapivě hodně na jeden asset:

- **Cull update frequency** — kontrolovat jen při spawnu, každou sekundu, nebo každý tick. Volba závisí na kontextu: u krátkého efektu stačí spawn, u dlouhého ne.
- **Cull reaction** — *kill* (nadobro), *asleep* (deaktivovat a umět probudit) a varianty. Přednášející u toho poznamenává, že *asleep* je obvykle to, co chceš.
- **Significance handler** — kdo rozhodne, které instance přežijí strop. Vestavěné jsou **podle vzdálenosti** a **podle věku**, dá se dopsat vlastní v C++.
- **Max distance** — a tady je věcné upozornění, které se snadno přehlédne: *„tohle nemá nic společného s GPU. Tohle je čistě o tom, že přestaneme systém simulovat"* — tedy o ticku, ne o vykreslování.
- **Dva stropy instancí** — na úrovni effect typu a na úrovni systému. Tvrdé limity, o jejichž naplnění rozhoduje significance handler.
- **Cull proxy mode** — místo zrušení systému **použij už nasimulovanou kopii** jiné instance (hoří-li někde jiná pochodeň, vykresli ji podruhé). Poctivá výhrada: *„render thread pořád platíš. Nic není nikdy úplně zdarma."* Šetří se tick, ne kreslení.
- **Pre-cull check a visibility cull delay** — nespawnovat vůbec, není-li to v obraze; a jak dlouho po zmizení z obrazu čekat.

**Kolik to dělá** [(21:09)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=1269s), měřeno na 5v5 zápase v Lyře **se procesorem omezeným na čtyři vlákna** (a s vypnutými optimalizacemi, které tam Epic sám udělal): počet aktivních systémů **spadl na méně než polovinu**, hra vypadá **úplně stejně**, nejhorší zásek na render vlákně je **méně než poloviční**. Úspory: ~0,7 ms herní vlákno, **3,5 ms render vlákno**, 2,15 ms souběžná práce.

**Dva konkrétní návrhy**, které se dají převzít jako vzory [(22:43)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=1363s):

| effect type | pro co | nastavení |
|---|---|---|
| **one shot** | kroky, dopady, výhozy nábojnic, záblesky | **okamžitý visibility cull**, significance podle vzdálenosti, nízký strop instancí |
| **looping, gameplay critical** | zdravotní balíčky a podobné poutače | 5 instancí, significance podle vzdálenosti, **1 s zpoždění visibility cullu** |

To zpoždění má konkrétní důvod, který je poučnější než samo číslo: efekt má krátký rozjezd, takže při vykukování zpoza krytu by pořád naskakoval a mizel. *„Podíváš se jinam, cullne se; podíváš se zpátky, začne znovu."*

**A rozlišení, které tu je nejcennější** [(23:29)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=1409s): dopady kulek do prostředí jsou cullovatelné, ale **jiskra při zásahu hráče není** — to je *„gameplay critical effect"*. Kategorie tedy nejsou technické, ale **podle toho, jestli hráč tu informaci potřebuje**.

**Jak se to samo stane problémem** [(19:35)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=1175s) je nejpoctivější část přednášky. Na jednom projektu měli **asi 7 000 částicových systémů jen na padající listí ze stromů**, všechny na jednom effect typu — a *„kdykoli jsi do toho effect typu něco přidal, dostal jsi asi 30ms spike, protože significance manager musel projít všechno a obnovit to pole."* Autorův závěr: *„ano, může se to pokazit."*

> **Pozn.:** Na tomhle assetu je vzácné, že **řeší cizí obsah bez jeho úpravy** — což je situace, ve které se optimalizace fakticky dělá nejčastěji a o které se nejméně mluví. Nejhodnotnější věta ale není technická: **kategorie efektů se dělají podle toho, jestli hráč tu informaci potřebuje**, ne podle toho, jak jsou vyrobené. „Jiskra při zásahu hráče" a „jiskra při zásahu zdi" jsou technicky totéž a v rozpočtu dvě různé věci — a to je designové rozhodnutí, které musí udělat někdo, kdo ví, jak se hra hraje. A ještě jedna vlastní poznámka k těm sedmi tisícům listů: **strop instancí je levnější než significance manager.** Rozhodne-li se u každého systému, jestli je významný, platíš za to rozhodování; řekneš-li „maximálně patnáct", neplatíš za nic. U velkých počtů je proto lepší nejdřív omezit počet a teprve pak ladit významnost.

**Souvislosti:** [Diagnostika Niagary](#diagnostika-niagary-pet-statistik-a-jedna-past) · [Škálování a pooling](#skalovani-a-pooling-co-vypnout-a-co-recyklovat) · [Optimalizační průchod: 59 systémů](gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) · [Rejstřík: Effect type](../rejstrik.md#effect-type) · [Rejstřík: Significance handler](../rejstrik.md#significance-handler)

---

## Škálování a pooling: co vypnout a co recyklovat

**Zdroj:** [Optimizing Niagara: a Practical Approach to Performant Worlds](https://www.youtube.com/watch?v=71c5yv-XeY8) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~47 min, Unreal Fest Orlando 2025

**Shrnutí:** Effect type pracuje s celým systémem. Tahle myšlenka jde o patro dovnitř — **vypínat jednotlivé emittery**, navěsit to na kvalitativní úrovně s výjimkami po platformách, a k tomu dvě věci, které se týkají spawnování: **pooling** a **rozpočet na efekty**. Háček u obojího: **oboje má selhání, které se nedá uhádnout dopředu** — pooling žere paměť a rozpočet umí rozkmitat scénu.

### Rozpad myšlenky

**Emitter scalability** [(25:50)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=1550s) se zapíná v emitteru přepnutím *scalability mode* ze *system* na *self*, a pak dostaneš tatáž pole jako u effect typu, ale **pro jeden emitter**. Ukázka, na které je smysl vidět nejlépe: **táborák** má tři emittery — velký plamen, uhlíky odletující do vzduchu a kouřový sloup. *„Kouř potřebujeme, protože je důležitý na dálku. Velký plamen taky. Ale uhlíky nás za určitou vzdálenost nezajímají"* — takže se jim sjede spawn rate a pak se vypnou.

**Kvalitativní úrovně a výjimky** [(27:24)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=1644s). Škálování se váže na `fx.Niagara.QualityLevel`, který ve výchozím stavu kopíruje `sg.FXQuality` (0–4 = low až cinematic). Zajímavější je, co se s tím dá dělat:

- **Per-platform overrides** — *„nikdy nechci vidět Epic kvalitu na Nintendo Switchi"* nebo na Linuxu, protože se dodává na Steam Deck. Nastaví se to na úrovni assetu, ne v kódu.
- **Vypnout celý emitter nebo systém na dané úrovni** — přímo v Niagara editoru, s náhledem, co bude a nebude živé. Cena té alternativy je jasná: *„nemusíš obcházet všechny blueprinty, které ty systémy používají."*
- Editor **hlásí konflikty** ve stacku, když si dvě nastavení odporují.

**Pooling** [(29:45)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=1785s) je klasika z programování a Niagara ho má **předkonfigurovaný na 32 instancí** u každého systému — ale funguje jen tehdy, když ho **při spawnu vyžádáš**. Dva režimy: *auto release* (systém se po deaktivaci sám vrátí do zásoby — ideální pro krok, dopad, léčivý efekt) a *manual release* (musíš vrátit, ne zničit — pro věci jako „postava hoří", které se ukončují na konkrétní pokyn). Uděláš-li to špatně, **dostaneš varování** — a autor přiznává, že jich viděl hodně.

Tři výhrady, které z toho dělají rozhodnutí, ne samozřejmost:

1. **Přeteče-li zásoba, přebytek se nepooluje** — půjde do garbage collectoru jako dřív. Řešení, které to zavírá: **nastav strop instancí v effect typu na tutéž hodnotu**, a pak se přetéct nedá.
2. **Přednaplnění zásoby (pool prime) umí zaseknout**, načte-li se ve špatnou chvíli.
3. **Poolovat příliš mnoho stojí paměť.** *„Nikdy se nevyhrává úplně snadno."*

A rozlišení, kdy pooling **není** ta správná odpověď: u věcí spawnovaných v obrovském objemu (záblesky výstřelů) se místo něj používá [úplně jiný postup](#dve-cesty-jak-prestat-spawnovat-systemy).

**Rozpočet na efekty** [(34:25)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=2065s) je funkce, kterou autor podle svých slov moc nepoužívá — a rovnou říká proč: *„konfigurace je trochu nepořádná,"* protože rozpočty se zadávají v `ini` souborech. Princip je ale hezký: podle toho, jak blízko jsi rozpočtu na herní a render vlákno, se **dynamicky stahují cullovací vzdálenosti a stropy instancí**. Zapíná se `fx.Budget.Enabled` a `fx.BudgetInEditor.Enabled`. Nejagresivnější varianta je „nad 50 % rozpočtu nás kroky nezajímají vůbec".

**A jeho selhání**, které je poučné mimo Niagaru: *„culluješ hodně systémů, takže cena jde dolů, takže jsi teď pod rozpočtem — ale pod rozpočtem se smí spawnovat víc systémů. Takže spawnuješ víc a skončíš v cyklu nahoru, dolů, nahoru, dolů. Je zábavné se na to koukat."* Léčba je zpomalit **zotavení** rozpočtu (`fx.Budget.AdjustedUsageDecayRate`), ne zpřísnit strop.

> **Pozn.:** Ten rozkmitaný rozpočet je učebnicová **regulační smyčka bez hystereze** a stojí za pojmenování, protože se v hrách objevuje i jinde: dynamické rozlišení, LOD přepínání, adaptivní obtížnost. Pravidlo je vždycky totéž — **systém, který reaguje na svůj vlastní výstup, potřebuje asymetrii mezi zhoršením a zlepšením**; jinak osciluje. Právě proto tam Epic dal decay rate a ne jen práh. Druhá věc, kterou si odsud bereme, je autorova poctivost u poolingu: *„nic není nikdy zdarma"* zazní v přednášce třikrát u tří různých funkcí (cull proxy, pooling, pool prime) — a je to lepší rámec než seznam tipů, protože nutí ptát se, **čím se za každou úsporu platí**.

**Souvislosti:** [Effect type](#effect-type-jeden-asset-ktery-rozhoduje-o-vsem) · [Dvě cesty, jak přestat spawnovat systémy](#dve-cesty-jak-prestat-spawnovat-systemy) · [Rozpočet snímku: rozpočet je peněženka](rozpocet-snimku.md#rozpocet-je-penezenka-ne-cil) · [Rejstřík: Object pooling](../rejstrik.md#object-pooling) · [Rejstřík: FX budget](../rejstrik.md#fx-budget) · [Rejstřík: Effect type](../rejstrik.md#effect-type)

---

## Dvě cesty, jak přestat spawnovat systémy

**Zdroj:** [Optimizing Niagara: a Practical Approach to Performant Worlds](https://www.youtube.com/watch?v=71c5yv-XeY8) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~47 min, Unreal Fest Orlando 2025

**Shrnutí:** Předchozí myšlenky snižovaly počet systémů, které tikají. Tyhle dvě funkce jdou dál a řeší **cenu spawnování samotného** — jedna tím, že udělá emitter mnohem hloupější, druhá tím, že místo sta systémů běží jeden. Obě dávají pořádné úspory (řádově desetinásobek) a obě mají cenu, kterou je potřeba znát dopředu. Háček, který se snadno přehlédne: **navzájem se vylučují.**

### Rozpad myšlenky

**Lightweight emitters** [(37:33)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=2253s) jsou návrat k pevně dané funkčnosti — autor je popisuje jako ohlédnutí za starým Cascadem. Naměřené hodnoty na krocích deseti botů v Lyře jsou působivé:

| | běžný emitter | lightweight |
|---|---|---|
| herní vlákno | **1,3 ms** | **0,2 ms** |
| render vlákno | 0,3 ms | ~0,2 ms |
| GPU | nenulové | **nula** (nedispatchuje se) |
| paměť | 2,7 MB | **~0,27 MB** |

*„Jenom za kroky. To je šílené."* A cena: **jsou strašně omezené** — bez scratch padu, s minimální možností napojit data a bez dynamických vstupů. *„Ztratíš tu niagarovou pizzu ‚je to velký compute shader, udělám si v něm cokoli'."* Rozšířit se dají v C++, máš-li kolem sebe programátory.

**Niagara Data Channels** [(39:51)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=2391s) řeší tentýž problém obráceně: **gameplay do kanálu jen zapisuje data** a částice z nich spawnuje jeden jediný systém. Přednáška to ukazuje na střelbě — před nasazením poskočí herní vlákno až k **stovkám milisekund**, po nasazení je *„uprostřed levelu jediný systém"* a cena na herním vlákně je dramaticky dole. Render vlákno se nezmění, protože částic se kreslí stejně.

Dva druhy kanálu a rozdíl mezi nimi je praktický:

- **Global** — čte a zapisuje do něj všechno ve světě. Zajímavý vedlejší efekt: dá se přes něj **komunikovat mezi Niagarou a blueprinty** oběma směry.
- **Islands** — rozdělí svět na mřížku a systém poslouchá jen dění ve svém boxu, takže se nekomunikuje se všemi pořád.

Cena je tady jiná než u lightweight emitterů: **musíš sáhnout na obsah.** Systém se pro to staví záměrně (reader v systému, spawn conditional v emitteru, čtení payloadu při spawnu částice, plus modul *complete if unused*, který systém ukončí, když se do něj přestane zapisovat) a spawnuje se speciálním uzlem. Od 5.5 na to existuje průvodce — *„klikneš pravým, add spawn by data channel, a udělá to za tebe."*

**A ta neslučitelnost** [(46:06)](https://www.youtube.com/watch?v=71c5yv-XeY8&t=2766s): data channels a lightweight emittery **nejdou dohromady**, protože lightweight emitter neumí vlastní uzly. Přednáška končí referenční tabulkou rozdělenou podle toho, co je **gameplay critical** a co ne — a právě tady se to rozhodne: kritické efekty snesou plnou Niagaru s poolingem, u masově spawnovaných nekritických si vybereš jednu z těch dvou cest.

> **Pozn.:** Dvě různé odpovědi na tutéž otázku, které se navzájem vylučují, jsou v enginech častější, než se čeká — a tenhle případ je dobrá ukázka, **jak takové rozhodnutí udělat**: ne podle toho, co je rychlejší (obojí je rychlé), ale podle toho, **co v tom efektu ještě potřebuješ umět**. Potřebuješ-li předávat pozici zásahu, normálu a barvu, lightweight emitter to neumí a rozhodnuto je. Za pozornost stojí i to, že data channels **mění, kde ta logika bydlí**: efekt přestane být „věc, kterou spawnuješ" a stane se „věc, která poslouchá" — což je táž změna myšlení jako u event busu, jen pro částice — viz [event bus v Godotu](../godot/signaly.md#event-bus-kdyz-se-systemy-nemaji-cim-potkat). Praktický důsledek, který přednáška nezmiňuje: **tím se ta logika i hůř hledá.** Neexistující spawn se nedá najít fulltextem, takže patří do dokumentace projektu.

**Souvislosti:** [Škálování a pooling](#skalovani-a-pooling-co-vypnout-a-co-recyklovat) *(kdy stačí recyklovat)* · [Kroky a povrchy: Niagara Data Channel](footsteps.md#niagara-data-channel-castice-kroku-bez-stovky-systemu) *(týž nástroj na konkrétní úloze)* · [Effect type](#effect-type-jeden-asset-ktery-rozhoduje-o-vsem) · [Rejstřík: Lightweight emitter](../rejstrik.md#lightweight-emitter) · [Rejstřík: Niagara Data Channel](../rejstrik.md#niagara-data-channel)

---

## Živý svět z částic: tvorové, kteří poslouchají, ale nehlasují

**Zdroj:** [Building Living World Creatures with Niagara | Unreal Fest Chicago 2026](https://www.youtube.com/watch?v=pwpwy6m38bk) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~17 min, přednáška (Epic, technical FX, LEGO Fortnite)

**Shrnutí:** Nový biom LEGO Fortnite byl krásný a mrtvý — chyběly ryby, světlušky a žáby. Měly ale přibýt bez nových mechanik a běžet od slabého mobilu po silné PC. Odpověď byla Niagara místo animovaných aktérů a jedno pravidlo dohodnuté s designem, které stojí za převzetí: **tvorové smějí reagovat na hráče a svět, ale nesmějí nic rozhodovat — poslouchají, nehlasují.** Háček: řešení na GPU do hry nešla, protože na mobilu nemusí fungovat — a verze, která se vešla všude, stojí 0,15 ms.

### Rozpad myšlenky

**Pravidlo, které určilo techniku** [(0:50)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=50s): nulový gameplay význam — nic neblokuje, neodměňuje, nepodmiňuje; reagovat smí na denní dobu, počasí, polohu hráče, kameru i na to, kam svítí hráčova baterka. Díky tomu nemusí být tvorové aktéři. Lineární animace by znamenala ruční práci na každou variantu a okolí by nevnímala; animation blueprint by okolí vnímal, ale skeletal mesh s ABP na každého tvora znamená vyhodnocování póz na CPU, a to v tomhle měřítku na mobilu nejde [(1:37)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=97s). Niagara má přístup k datům scény (trojúhelníky, fyzikální objemy, scene depth, distance fields) a může být spíš **vizualizátor dat** než simulátor částic [(2:23)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=143s).

**Ryby: tři řešení a čísla** [(3:09)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=189s): hejno krouží kolem bodu, který se posouvá. Proti překážkám nestačí paprsek — je nekonečně tenký a proklouzne škvírou, kterou ryba neproleze. Na GPU se proto použije [sphere tracing](../rejstrik.md#sphere-tracing) přes [global distance field](../rejstrik.md#global-distance-field): hodnota pole je vzdálenost k nejbližšímu povrchu, tedy poloměr největší koule, která se na to místo vejde, a hotový modul částici od povrchu odtlačí [(3:56)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=236s), [(4:42)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=282s). Jenže distance fields ani GPU částice nemusí být na mobilu k dispozici [(5:29)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=329s). Do hry proto šla verze na CPU, která logiku přesune **z každé částice na úroveň systému**: jednou za smyčku (1–5 s) vybere náhodný bod (seed z počtu smyček — náhodně, ale reprodukovatelně), trasuje k němu a při překážce odečte poloměr hejna jako falešné tělo [(6:16)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=376s), [(7:04)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=424s). Čísla pro milion částic: distance field na GPU 2 ms; verze na CPU **0,15 ms na herním vlákně a žádná práce na GPU**, s pevnou cenou předem. Hlídání vzájemných srážek ryb přes neighbor grid by stálo kolem 1 GB paměti GPU [(7:50)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=470s), [(8:37)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=517s).

**Světlušky a nasazení ve velkém** [(8:37)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=517s): poloha hráče z material parameter collection, maska vlivu a odpudivý vektor — roj se před hráčem rozprchne. Ruční umístění do tisíců dlaždic ale nepřicházelo v úvahu [(9:25)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=565s). PCG proto vzorkuje body (třeba rovinu jezera) a přes interop plugin je posílá do [Niagara Data Channelu](../rejstrik.md#niagara-data-channel); vstupy systému (střed a hustota roje) se jen přepnou na data z PCG [(10:58)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=658s). Výsledek: **jeden systém pro všechny roje** místo mnoha Niagara aktérů a efekty, které jsou vždycky v souladu s generováním levelu — každé jezero v každé dlaždici, i v budoucích, má světlušky a ryby [(11:46)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=706s).

**Žáby a ostatní obory** [(12:32)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=752s): žabí jezírko, kvůli kterému přednáška vznikla — lekníny v kruhu se zjednodušeným vztlakem (jezera jsou rovná, takže tu jde vědomě o „oříznuté rohy") a žáby, které při každé smyčce skočí na nový cíl s interpolovanou polohou i rotací [(13:18)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=798s). Interpolace sama nenahradí ruční animaci, a proto **Niagara Summary View** vystavila zjednodušené parametry netechnickým kolegům: animátoři dostali křivky pojmenované tak, jak jim rozumějí, zvukaři háčky na zvuky [(14:05)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=845s). A když level design chtěl na hero mapě kolize na leknínech, jádro výpočtu zůstalo a změnily se jen vstupy [(14:51)](https://www.youtube.com/watch?v=pwpwy6m38bk&t=891s).

> **Pozn.:** Pravidlo „poslouchá, ale nehlasuje" je nejpřenositelnější kus přednášky a funguje i mimo Niagaru: **kosmetická vrstva světa smí číst herní stav, nikdy ho psát.** Díky tomu může běžet levněji, na jiném vlákně, s nižší přesností — nebo na slabé platformě vypadnout úplně, aniž by se rozbila hra. Je to stejná hranice, jakou Tyroller táhne mezi [simulací a zobrazením](principy-architektury.md#znovupouzitelne-kostky-a-lepidlo-70-ku-30). Technicky pak přednáška dokládá dvě věci, které tahle kapitola tvrdí z jiné strany: řešení na úrovni systému s pevnou cenou předem je předvídatelnější než práce na každé částici, a [data channel místo sta systémů](#dve-cesty-jak-prestat-spawnovat-systemy) se vyplatí. Výběr podle cílové platformy je přitom poctivý — nejvyšší věrnost na high-end PC přednáška nezakazuje, jen připomíná, že mobil ji nepotřebuje.

**Souvislosti:** [Dvě cesty, jak přestat spawnovat systémy](#dve-cesty-jak-prestat-spawnovat-systemy) · [Kroky a povrchy: Niagara Data Channel](footsteps.md#niagara-data-channel-castice-kroku-bez-stovky-systemu) · [PCG: základy a nástroje](pcg-zaklady.md) · [Znovupoužitelné kostky a lepidlo](principy-architektury.md#znovupouzitelne-kostky-a-lepidlo-70-ku-30) *(simulace odděleně od zobrazení)* · [Rejstřík: Niagara Data Channel](../rejstrik.md#niagara-data-channel) · [Rejstřík: Global Distance Field](../rejstrik.md#global-distance-field) · [Rejstřík: Sphere tracing](../rejstrik.md#sphere-tracing)
