# Profiling: měření místo odhadů

Optimalizace bez měření je hádání a hádání v Unrealu skoro nikdy nevyjde — protože příčina bývá o dvě patra jinde, než kde se problém projeví. Tahle kapitola je o **metodě**: jak zjistit, co brzdí, jak si test připravit tak, aby se dal zopakovat, a jak poznat, kdy má nález opustit tvůj stůl a jít za někým jiným.

Konkrétní zásahy — co s tím pak dělat — jsou v [Optimalizaci scény](optimalizace.md) a [Texturách a DLSS](textury-a-dlss.md). Tady jde o krok, který jim předchází a bez kterého jsou obojí střelbou naslepo.

---

## Rozhodovací strom: `stat unit` řekne, kterým nástrojem pokračovat

**Zdroj:** [Technical Artist's Guide to Profiling in Unreal Engine](https://www.youtube.com/watch?v=mCZRHljYnZA) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~33 min, Unreal Fest Orlando 2025 · + [What's Causing my Frame Rate to Drop? - Stat Profiling](https://www.youtube.com/watch?v=nQdsY2a-Fn8) · [NumenBrothers](https://www.youtube.com/channel/UCVt_pROr36liiGeN3NXLRZw) · ~6 min, případovka

**Shrnutí:** Než sáhneš po jakémkoli profileru, potřebuješ vědět, **co je úzké hrdlo** — a na to stačí jeden příkaz. `stat unit` ukáže čtyři čísla (frame, game, draw, GPU) a **to, které se blíží k frame, je tvoje brzda**. Z toho pak plyne nástroj: game nebo draw → Unreal Insights, GPU → `profileGPU` nebo dedikovaný GPU debugger. Háček, kvůli kterému se ten krok nesmí přeskočit: **vizuální debug režimy tě neuvedou k bottlenecku** — dají se optimalizovat celý den, aniž by se framerate hnul.

### Rozpad myšlenky

**Proč zrovna takhle** [(5:35)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=335s): autorka mluví k technickým artistům a popisuje jejich typickou past — *„umělci jsou vizuální lidé, takže tíhnou k debug režimům, jenže ty ti neřeknou nic o bottlenecku. Můžeš celý den optimalizovat kvůli konkrétnímu debug režimu, a když to není to úzké hrdlo, neuvidíš žádnou změnu snímkování."*

**Rozhodovací strom** [(14:59)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=899s) je jádro celé myšlenky a vejde se do tabulky:

| co je blízko `frame` | co to znamená | čím pokračovat |
|---|---|---|
| **game** | úzké hrdlo je **herní vlákno** (CPU) | Unreal Insights trace |
| **draw** | úzké hrdlo je **render vlákno** (taky CPU) | Unreal Insights trace |
| **GPU** | úzké hrdlo je **GPU** | `profileGPU`, případně PIX / Razor |

Protože ta čísla mezi snímky poskakují, vyplatí se je vidět v grafu — `stat unit graph` nakreslí v rohu obrazovky průběh v barvách odpovídajících panelu.

**A pak se hypotéza ještě jednou ověří v traci** [(20:24)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=1224s), protože to nic nestojí: velký prázdný úsek v GPU stopě a nabité herní vlákno pod ním znamená přesně to, co čekáš — *„GPU stojí, protože nemá co dělat; CPU pořád vymýšlí, co se má vykreslit."* Opačný obrázek (nabité GPU, herní vlákno plné `wait for task` a `idle`) ukazuje na GPU.

**Celý postup na jednom reálném případu** [(0:02)](https://www.youtube.com/watch?v=nQdsY2a-Fn8&t=2s) je nejlepší doprovod k té tabulce, jaký v playlistu je. Hra běží stabilně 40–45 FPS, oheň se šíří — a **po dvaceti vteřinách spadne o 15 FPS**. Postup autora krok za krokem:

1. **`stat detail`** (nebo panel v levém horním rohu → Engine → Detail). Vidí červené **game thread**. *„To je vlastně dobrá zpráva — bál jsem se, že to bude GPU."*
2. **`stat game`** — o patro hlouběji. Zásek je celý v **blueprint time**.
3. **`stat startfile`**, nechat běžet aspoň deset vteřin, **`stat stopfile`**.
4. **Tools → Session Frontend → Profiler**, načíst soubor ze `saved/profiling`. Vybrat rozsah snímků a číst **průměr** (u nepravidelných záseků naopak maximum).
5. **Rozbalovat strom po nejdražší větvi**: game thread (35 ms/tick) → frame time → world tick → tick group → tick function tasks — až na konkrétní funkci.
6. Viník: **`on fire check`** na hierarchickém instancovaném meshi, **18 ms**.

Příčina je v zpětném pohledu banální a přesně to je na ní poučné: funkce procházela **každou instanci foliage každý tick** a ptala se, jestli hoří. Oprava: držet **samostatné pole hořících instancí**. Autorovo shrnutí sedí — *„v retrospektivě to bylo dost zřejmé"*, jenže bez profileru by hledal v ohni, ne ve foliage.

> **Pozn.:** Ten rozhodovací strom je nejpřenositelnější věc celé kapitoly a platí i mimo Unreal: **napřed zjisti, který rozpočet je vyčerpaný, teprve pak otevírej nástroj.** Godotí strana knihovny má tutéž disciplínu popsanou u [měřicího stolu](../godot/kompozice.md#kolik-nodu-je-moc-zmereno) a u [rozdílu mezi `_process` a fyzikou](../godot/projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek); rozdíl je jen v tom, že UE má pro každou vrstvu vlastní nástroj, takže volba nástroje **je** první rozhodnutí. Za pozornost stojí i to, že `draw` (render vlákno) je **taky CPU** — což je klasické nedorozumění: „vysoký draw" nesvádí na grafiku, ale na to, kolik práce dá frame připravit.

**Souvislosti:** [Reprodukovatelný test](#reprodukovatelny-test-bez-nej-neporovnas-nic) *(další krok)* · [Co říká GPU profiler](#co-rika-gpu-profiler-a-co-v-nem-nenajdes) · [Optimalizace: co blokuje hlavní vlákno](optimalizace.md#druha-osa-optimalizace-co-blokuje-hlavni-vlakno) · [Godot: co skutečně stojí výkon](../godot/projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek) · [Rejstřík: Frame time](../rejstrik.md#frame-time) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights)

---

## Co je v herním vlákně a co v renderovacím

**Zdroj:** [Automated Performance Profiling for Local Workflows](https://www.youtube.com/watch?v=bfkbwXVMtn8) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~116 min, Inside Unreal (engine programátor)

**Shrnutí:** Rozhodovací strom výše řekne, **které z těch čtyř čísel** je tvoje brzda. Tahle myšlenka je patro pod ním: **co se do každého z nich vlastně počítá.** Bez toho se dá strom projít správně a pak optimalizovat úplně špatnou věc. Háček, na kterém uvázne skoro každý: **renderovací vlákno není GPU čas.** Je to čas, který **procesor** stráví přípravou práce pro GPU — a šetří se na něm jinými zásahy než na GPU.

### Rozpad myšlenky

**Herní vlákno** [(24:58)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=1498s) je všechno, co bys označil za „tvoji hru": *„herní logika, AI, fyzika, blueprinty, jakákoli gameplay logika, kterou máš"*. Když ti tohle číslo přeroste renderovací vlákno, jsi **CPU-bound** a příčina je skoro jistě v kódu, který jsi napsal.

**Renderovací vlákno** [(26:33)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=1593s) je ta část, kterou lidé čtou špatně: *„tohle není přesně GPU čas. Je to čas, který CPU stráví přípravou vykreslovacích příkazů pro GPU."* Konkrétně se tam odehrává:

- **culling** — kreslíš-li deset tisíc objektů, příkazy pro ně se musí připravit, i když jich na obrazovce uvidíš zlomek; někdo je musí zahodit, a ten někdo je procesor;
- **výběr LODů** — které úrovni detailu odpovídá který objekt podle vzdálenosti;
- **sestavení a odeslání draw callů** — *„připravovat a odesílat draw cally je cena, o které musíš vědět."*

**GPU čas** je pak teprve skutečná práce grafiky: rasterizace, shadery, post-process, ray tracing.

**A jedna vlastnost, kterou je potřeba znát, protože z ní plyne latence** [(28:05)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=1685s): **snímky CPU a GPU nejsou zarovnané.** Procesor smí běžet napřed — odešle příkazy a hned začne počítat další snímek, zatímco GPU pořád zpracovává ten předchozí. To je přesně to, co [potrubí snímku](frame-pacing.md#snimek-neni-fronta-je-to-potrubi) popisuje z druhé strany.

**Paměť jako průřezová vrstva** [(28:51)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=1731s), která se do těch čtyř čísel promítne nepřímo: dojde-li paměť, spustí se **garbage collection**; na PC začne systém odkládat na disk (*„a i s SSD je to pomalejší než hlavní paměť"*); na mobilu a části konzolí **odkládání neexistuje vůbec**. K tomu poznámka, která pro PC platí dvojnásob: *„jsou lidi se čtyřmi giga paměti a lidi se čtyřiašedesáti"* — takže „kolik mám paměti" není vlastnost hry, ale vlastnost cílového publika.

> **Pozn.:** Nejcennější důsledek téhle anatomie je nenápadný a přehlíží ho skoro každý: **LODy a culling nešetří jenom GPU.** Šetří i procesor, protože se na něm ta rozhodnutí dělají — takže „mám málo trojúhelníků, LODy nepotřebuju" je špatná úvaha, jakmile je objektů hodně. Druhá věc, kvůli které tahle myšlenka stojí před praxí: **stejný symptom má dvě různé léčby.** Padá ti snímkování a `draw` je vysoko? Neřeš shadery, řeš **počet objektů, ze kterých se rozhodnutí dělá**. Padá ti snímkování a vysoko je `GPU`? Pak teprve shadery a rozlišení. Zaměnit ta dvě patra znamená optimalizovat celý den bez efektu — což je táž past jako [debug režimy místo bottlenecku](#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat), jen o krok dál. A vlastní poznámka k té paměti: je to jediná položka ze čtyř, která **neroste plynule** — nedojde, nedojde, a pak dojde a spadne ti to všechno naráz. Proto se hlídá jinak než čas: [vodočtem, ne průměrem](gpu-pamet.md#pooly-a-jejich-vodocty).

**Souvislosti:** [Rozhodovací strom](#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Tvůj kód v profileru není vidět](#tvuj-kod-v-profileru-neni-videt) · [Potrubí snímku](frame-pacing.md#snimek-neni-fronta-je-to-potrubi) · [Insights jako disciplína](mereni-automaticky.md#insights-jako-disciplina-od-symptomu-ke-pricine) *(šíření úzkého hrdla mezi vlákny)* · [Optimalizace: co blokuje hlavní vlákno](optimalizace.md#druha-osa-optimalizace-co-blokuje-hlavni-vlakno) · [Rejstřík: Herní vlákno](../rejstrik.md#herni-vlakno) · [Rejstřík: Renderovací vlákno](../rejstrik.md#renderovaci-vlakno) · [Rejstřík: Draw call](../rejstrik.md#draw-call) · [Bojovka: timeline přesunuté do Niagary](gpu-pruchod.md#bojovka-pro-desetilety-hardware-rozpocet-po-castech-a-co-se-v-nem-naslo) *(práce převedená z herního vlákna na renderovací)* · [Mass a ECS: proč objekty zpomalují](mass-ecs.md#proc-objekty-zpomaluji-pamet-kterou-nactes-a-zahodis) *(kde herní vlákno čeká na paměť)*

---


## Reprodukovatelný test: bez něj neporovnáš nic

**Zdroj:** [Technical Artist's Guide to Profiling in Unreal Engine](https://www.youtube.com/watch?v=mCZRHljYnZA) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~33 min, Unreal Fest Orlando 2025

**Shrnutí:** Profilování má dvě fáze a druhá je náročnější než první: **najít problém** je jedna věc, **ověřit, že tvoje oprava pomohla**, druhá. K tomu potřebuješ dva záznamy, které se liší **jedinou věcí** — a to v běžící hře nenastane samo. Kapitola je proto o tom, co všechno se musí umlčet: čas, počasí, vítr, animace, a hlavně **postava**. Háček, který se snadno přehlédne: měřicí bod není jen pozice, ale i **natočení kamery**.

### Rozpad myšlenky

**Kde vůbec měřit** [(6:25)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=385s). Autorčin tým si postavil **mapu výkonu** — build stroj pravidelně sbírá data v bodech, které do mapy kdokoli přidá, a ke každému uloží časy herního vlákna, render vlákna a GPU. Slouží ke dvěma věcem naráz: najít nejhorší místa, a **porovnávat záznamy v čase**, tedy chytat regrese.

**Příprava záznamu** [(7:57)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=477s) má pár kroků, které vypadají jako formality a nejsou:

- **Spusť Unreal Insights dřív než hru.** Pozdní připojení může data poškodit.
- **Používej development build**, ne test — v testu je většina informací vystřižená. A počítej s tím, že development build **není přesně reprezentativní**.
- **Zapni `trace.stop`, dokud hledáš to místo.** Hledání trvá klidně deset minut a bez toho vyrobíš gigabajty dat, ve kterých pak nenajdeš, co hledáš.

**Měřicí bod je pozice *a* natočení** [(9:31)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=571s): *„když se dívám takhle, výkon je v pohodě; když se otočím sem, je to hodně špatné."* Uložit se dá příkazem **`bugit`**, který zaznamená obojí.

**A teď to, co se musí umlčet** [(11:51)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=711s), protože A/B test znamená, že se ve snímku **změnila jen ta jedna věc**: denní doba · počasí, vítr, vlhkost · jakýkoli okolní pohyb a houpání · animovaná geometrie. A hlavně: *„největší věc, která se ti po obrazovce hýbe, je nejspíš samotná postava"* — tým si na to udělal vlastní příkaz **`hide player`** (přes cheat manager), s praktickou výhradou, že **se musí schovat i všechny komponenty**.

Autorka k tomu ale hned přidává protiváhu, která z toho dělá poctivou radu: **vypínáš-li věci, vypínáš i jejich cenu.** Než to uděláš, ověř, že to, co umlčuješ, není zrovna to drahé — jinak si naměříš scénu, která ve hře neexistuje.

**Drobnosti, které šetří hodiny:** `slomo 0` pauzne hru, takže se dá zamířit na konkrétní snímek — a dají se navázat na klávesy (`slomo 1`, `0.1`, `0.01` na numerické klávesnici) přes `DefaultInput.ini` pro tým nebo lokální `UserInput.ini` pro sebe [(13:24)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=804s). **Console Variables Editor** dovolí dávkovat příkazy místo ťukání po jednom.

**A značky v traci** [(17:18)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=1038s): `trace bookmark` a `trace screenshot` zapíchnou do grafu značku, takže v tisících snímků najdeš ten svůj. Tým si k tomu do herního HUD přidal **číslo snímku**, aby se dalo video nahrávky spárovat s tracem — *„vidíš-li v traci spoustu fyziky a na snímku velký výbuch, hned víš, na čem jsi."*

> **Pozn.:** Tohle je fakticky **vědecký experiment se všemi jeho nároky** — kontrolní podmínky, jediná měněná proměnná, opakovatelnost — a stojí za to to takhle pojmenovat, protože pak je jasné, proč se ty přípravy nedají vynechat. Nejčastější chyba v praxi není špatný nástroj, ale **porovnávání dvou záznamů, které se lišily víc věcmi**; výsledek pak vypadá jako zlepšení a je to šum. Praktický doplněk, který přednáška nemá: **ulož si i příkazovou řádku a verzi buildu.** Za týden nebudeš vědět, jestli jsi tehdy měřil s jinou scalability nebo na jiném changelistu — a bez toho se výsledky nedají srovnat, i když jinak byly připravené správně.

**Souvislosti:** [Rozhodovací strom](#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Nález není hotová práce](#nalez-neni-hotova-prace-predani) · [Godot: kolik nodů je moc](../godot/kompozice.md#kolik-nodu-je-moc-zmereno) *(týž nárok na kontrolní vzorek)* · [Rejstřík: A/B test](../rejstrik.md#ab-test) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights)

---

## Co říká GPU profiler a co v něm nenajdeš

**Zdroj:** [UE5: Profilers Explained](https://www.youtube.com/watch?v=tuAtGaVqcSM) · [Dallas Drapeau](https://www.youtube.com/channel/UCatEMsDp-qF_bix_1ST2llw) · ~36 min, výklad · + [How to Analyze your Level Performance - Profiler Tutorial](https://www.youtube.com/watch?v=HOcXWZY044E) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~4 min, tutoriál

**Shrnutí:** GPU profiler (`profileGPU`, nebo `Ctrl+Shift+,`) vypíše, kolik milisekund sežrala která fáze vykreslování — a jeho hlavní problém je, že **ty položky nikdo nevysvětlí**. Kapitola je překlad těch řádků do češtiny: co je base pass, co Nanite visual buffer, proč jsou Lumen a ambient occlusion pod jedním řádkem a co znamená *render virtual shadow maps non-Nanite*. Háček, kvůli kterému nestačí: **kód v něm neuvidíš** — blueprint, který ti bere patnáct snímků, tu nebude.

### Rozpad myšlenky

**Než začneš, srovnej si očekávání** [(3:09)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=189s), protože podle autora je *„zklamání z výkonu často ne proto, že engine nedělá, co má, ale kvůli očekávání."* Dokumentace k Lumenu má cílové hodnoty přímo napsané: **Epic scalability míří na 30 FPS, High na 60**. Běží-li ti hra na High v šedesáti, **dělá přesně to, co má**. A z toho plyne otázka, kterou si podle něj musí položit každý, kdo míří výš: *„někdy je největší otázka optimalizace, jestli je pro tebe ten engine vůbec ten pravý"* — chceš-li 120 FPS, UE5 s dynamickým GI a Nanitem ti bude klást odpor.

**Druhá kalibrace: framerate v editoru je skoro jedno** [(8:36)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=516s). *„Netrap se rozdílem mezi 83 a 87 snímky v editoru — hráč to neuvidí. Důležité je, jak to běží, když dáš Play."*

**Jak se s tím pracuje** [(9:24)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=564s): otevřít, **dvojklik na sloupec Duration**, aby se nejdražší věci vysypaly nahoru, a jít odshora. Ten druhý, čtyřminutový tutoriál dělá totéž a přidává praktickou drobnost [(1:35)](https://www.youtube.com/watch?v=HOcXWZY044E&t=95s): horní barevný pruh dá **hrubý přehled** (největší barva = největší žrout), spodní strom pak detail.

**Slovníček položek**, který je vlastní hodnotou toho videa:

- **Base pass** — základní vykreslení geometrie.
- **Nanite visual buffer** [(22:47)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=1367s) — všechno kolem Nanitu; uvnitř *software rasterized* / *hardware triangles* / *patches* / **tesselated**, což je Nanite displacement. Na tenhle řádek většinou **neexistuje konzolová páka** — jediná cesta je **míň geometrie**.
- **Diffuse indirect a AO** [(18:50)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=1130s) — pozor, tohle **nejsou jen stíny**: je to celý Lumen (nepřímé osvětlení, ambient occlusion, skylight, screen probes) v jednom součtu.
- **Shadow depth** [(17:16)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=1036s) — virtual shadow maps. A tady je konkrétní past: řádek **render virtual shadow maps non-Nanite** znamená **další průchod navíc** pro všechno, co Nanite nemá. Je-li vysoký, máš ve scéně hodně ne-Nanite geometrie — a autor rovnou jmenuje, co to v jeho scéně je: **průsvitné assety a vodní plochy**, které Nanite nepodporuje.
- **Post-process** — Bloom, lens flares, temporal super resolution. Řádek si často **říká jménem konzolové proměnné** (`anti-aliasing quality = 2`), takže víš, co zkusit snížit.
- **Lights** [(14:06)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=846s) — bývá to jeden z největších žroutů, hlavně v interiérech; páky jsou zmenšit attenuation radius, vypnout vrhání stínů, nebo světla ubrat.

**Obecné pravidlo, jak z toho udělat postup**: většina řádků odpovídá **konzolové proměnné stejného jména**, takže se dá zkusit snížit a hned vidět dopad [(19:36)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=1176s). Autor ale u toho hned přidává protiváhu, která je nejlepší věta celého videa [(22:00)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=1320s): *„optimalizace není o vypínání věcí. Je to o rovnováze mezi vizuální věrností a výkonovými mantinely cílového hardwaru."* Vypneš-li hardware ray tracing, získáš pár snímků a scéna vypadá jinak — a někdy je správná odpověď zapnout to zpátky a hledat jinde.

**A ta hranice** [(32:15)](https://www.youtube.com/watch?v=tuAtGaVqcSM&t=1935s): *„tohle v GPU profileru neuvidíš."* Trhavý framerate způsobený blueprinty se v něm neobjeví — proto autor postupuje v pořadí **view modes → GPU profiler → Insights**, a Insights nechává naposledy, protože je nejnepříjemnější na čtení a zároveň jediné místo, kde uvidíš CPU. Tentýž závěr má i minutový tutoriál: *„profileGPU nezachytí, co dělají blueprinty na pozadí."*

> **Pozn.:** Za pozornost stojí autorova rada, která zní banálně a v praxi se ignoruje: **čti dokumentaci k systému, který ladíš.** Stránky k Lumenu a Nanitu mají nejen cílové framerate, ale i **hotové bloky konzolových proměnných pro jednotlivé platformy**, které se dají zkopírovat rovnou do `ini`. To je rychlejší cesta k rozumnému výchozímu stavu než ladění po jedné hodnotě. A jeden praktický detail z jeho vlastní zkušenosti, který se hodí znát: **profiler občas ukáže nesmysl** (jednou mu hlásil 3 ms na světlech, po restartu byly pryč) — u výsledku, který nedává smysl, se vyplatí engine restartovat a změřit znovu, než začneš opravovat.

**Souvislosti:** [Rozhodovací strom](#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) *(kdy sem vůbec chodit)* · [Optimalizace scény](optimalizace.md#proc-jsou-levely-pomale-od-instanci-po-data-layers) *(co s tím dělat)* · [Nanite, nebo LODy?](optimalizace.md#nanite-nebo-lody) · [Osvětlení](osvetleni.md) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Rejstřík: Virtual Shadow Maps](../rejstrik.md#virtual-shadow-maps) · [Rejstřík: Draw call](../rejstrik.md#draw-call)

---

## Čísla, se kterými se dá srovnávat

**Zdroj:** [Profiling with Pirates: Performance Plundered from a Real Game](https://www.youtube.com/watch?v=CYvLn-tYRag) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~45 min, Unreal Fest Chicago 2026

**Shrnutí:** Dva lidé z Epicu profilují **skutečnou rozpracovanou hru** a mimochodem řeknou to, co se v tutoriálech nikde nedozvíš: **kolik čeho je moc.** Kolik `UObject`ů je v pořádku, kolik shading binů je moc, jak dlouho smí trvat garbage collection. Háček, který dělá celou přednášku použitelnou: ty prahy nejsou teoretické — jsou to hodnoty, u kterých se prezentujícímu *„zkřiví obličej"*, když je uvidí v cizím záznamu.

### Rozpad myšlenky

**Kolik `UObject`ů** [(17:27)](https://www.youtube.com/watch?v=CYvLn-tYRag&t=1047s) je nejcennější stupnice celé přednášky, protože **počet objektů přímo určuje, jak dlouho trvá garbage collection**:

| počet `UObject`ů | verdikt |
|---|---|
| do ~100 000 | *„budu mít radost"* |
| ~200 000 | *„víte, co děláte"* |
| ~300–700 000 | *„nic hrozného, ale nejspíš se na to podívejte"* — počítej s jedním zahozeným snímkem za minutu |
| ~1 000 000 | *„něco děláte špatně"* |
| 2 000 000 | **engine spadne** — tabulka objektů se nezvětšuje |

A důrazné varování k poslednímu řádku: *„viděl jsem studia, která si ten limit ve zdrojácích zvýšila. Nedělejte to. Není to řešení."*

**Jak se ta čísla zjistí** [(19:46)](https://www.youtube.com/watch?v=CYvLn-tYRag&t=1186s) — a tohle je nářadí, které stojí za zapamatování:

- **`obj list`** vypíše počty objektů po třídách (výchozí řazení podle velikosti; **`-countsort`** řadí podle počtu, což je to, co chceš při ladění GC).
- **`obj list class=<třída>`** vypíše každý objekt té třídy s plnou cestou; **`-csv`** to vysype k dalšímu zpracování.
- **`obj refs shortest name=<plná cesta>`** [(12:50)](https://www.youtube.com/watch?v=CYvLn-tYRag&t=770s) vypíše **řetězy referencí, které objekt drží v paměti** — podle autora nejlepší nástroj na hledání toho, proč se něco neuvolňuje.

**Reálný nález, který ta čísla ilustruje**: hra měla v main menu 123 000 objektů, v čerstvé hře 300 000 a v pozdní hře **761 000**. Půlka z nich byly **UI objekty** — 132 000 overlay slotů, 69 000 overlayů, 65 000 obrázků — protože každá struktura měla **předalokované všechny widgety**. Oprava podle autora *„na jeden den"*: stavět UI objekty až když jsou potřeba a pak je recyklovat.

**Řetěz referencí jako diagnóza** [(13:36)](https://www.youtube.com/watch?v=CYvLn-tYRag&t=816s): main menu odkazovalo na game mode → game state → globální datový asset, který za sebou táhl **8 300 balíčků (2,5 GB)** a načítal se **5 vteřin**. Autor tomu říká **reference hell** a pointa je, že se tím fakticky načítá velký kus hry kvůli hlavnímu menu. Ještě zajímavější je následek [(14:22)](https://www.youtube.com/watch?v=CYvLn-tYRag&t=862s): při přechodu do hry se **9 000 balíčků načetlo podruhé**, protože je mezitím garbage collector uklidil — plýtvání, které vzniklo přesně tím, že se odkaz na globální asset držel na špatném místě.

**Fyzika, kterou nikdo nechtěl** [(25:12)](https://www.youtube.com/watch?v=CYvLn-tYRag&t=1512s) je nejlepší příklad výchozí hodnoty, která nikoho netrápí, dokud ji nezměří: budovatelská hra bez fyziky měla **58 000 fyzikálních těles každý snímek** a **10 vteřin startu** padlo na jejich vytváření. Příčina: *„fyzika je v Unrealu zapnutá defaultně. Chceme, aby to fungovalo nováčkům."* Oprava: skript, který projde statické meshe a fyziku vypne.

**Shading biny** [(35:18)](https://www.youtube.com/watch?v=CYvLn-tYRag&t=2118s) jsou GPU protějšek téhož: jsou to *„Nanitová verze draw callů"* a **každý materiál ve scéně potřebuje vlastní** — každá materiálová instance, konstantní i dynamická — s minimem **3 mikrosekundy na GPU**. Naměřeno bylo ~2 100 raster binů a ~4 000 shading binů; cílová hodnota podle autora: **~50 raster binů a ~1 000 shading binů**. Doporučení, které z toho plyne, je architektonické: *„materiálové vrstvy nejsou Photoshop layers ani Niagara moduly"* — lepší je **pevná topologie materiálu** a znovupoužité instance, kterým se hodnoty předávají přes custom primitive data, material parameter collections nebo per-instance custom data.

**A jedno nastavení, které mění, co vlastně měříš** [(7:26)](https://www.youtube.com/watch?v=CYvLn-tYRag&t=446s): autor profiluje na 64jádrovém stroji a přidává si **`-corelimit 14`**, protože *„podle Steam hardware survey má polovina spotřebitelských CPU šest jader nebo míň"* — bez toho by měřil scénář, který u hráčů nenastane. K tomu **trace kanál `counters`**, který do Insights přidá čísla, jež se jinak těžko shánějí: dostupná a použitá paměť, počet primitiv, počet draw callů po cullingu, **počet `UObject`ů**, počet aktivních fyzikálních těles, počet světel.

> **Pozn.:** Nejvíc si z téhle přednášky bereme **existenci prahů**. Většina rad o optimalizaci má tvar „tohle je drahé, dělej toho míň", což se nedá použít k rozhodnutí — kdežto „760 tisíc objektů je moc, 200 tisíc je v pořádku" ano. Vyplatí se tedy sbírat čísla, ne dojmy: **rozpočet ve frame time**, počet objektů, počet draw callů, počet binů. Zároveň platí autorova věta, kterou opakuje jako refrén: *„nikdy nehádej — vždycky zjisti co, proč a jak."* A jedna vlastní výhrada: prahy jsou vázané na verzi enginu a cílový hardware, takže je ber jako **řádovou orientaci**, ne jako normu; sám autor to říká pro případ, že video někdo uvidí za pár let.

**Souvislosti:** [Rozhodovací strom](#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Nález není hotová práce](#nalez-neni-hotova-prace-predani) · [Optimalizace scény](optimalizace.md#proc-jsou-levely-pomale-od-instanci-po-data-layers) · [Godot: čísla mají meze](../godot/pripadovka-systemy.md#cisla-maji-meze-overflow-a-nepresnost-floatu) *(jiné tvrdé stropy, tatáž logika)* · [Rejstřík: Garbage collection](../rejstrik.md#garbage-collection) · [Rejstřík: Shading bin](../rejstrik.md#shading-bin) · [Rejstřík: Hard reference](../rejstrik.md#hard-reference)

---

## Tvůj kód v profileru není vidět

**Zdroj:** [Automated Performance Profiling for Local Workflows](https://www.youtube.com/watch?v=bfkbwXVMtn8) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~116 min, Inside Unreal (engine programátor)

**Shrnutí:** Předchozí myšlenky předpokládají, že v profileru **uvidíš, kde se čas ztrácí**. U vlastního kódu to není zdarma. Funkce, kterou jsi napsal, se v traci **neobjeví, dokud ji sám neoznačíš** — a to je nejčastější důvod, proč se hledá hodinu v enginu místo ve vlastní práci. Háček navrch: i když ji uvidíš, **bez představy o tom, co má stát, ti to číslo nic neřekne.**

### Rozpad myšlenky

**Označení vlastního rozsahu** [(55:29)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=3329s) je jeden makro řádek — `TRACE_CPUPROFILER_EVENT_SCOPE` — a autorova rada zní: *„myslíš-li si, že děláš práci, která je na ten čas dost těžká, přidej si ten profilovací scope, ať máš snadno vidět, kde přesně čas trávíš."* Bez něj se ta práce schová do nějakého obecného enginového bloku a v traci prostě není. Praktické pravidlo: **označuj při psaní, ne až při hledání** — v okamžiku, kdy funkci píšeš, víš nejlíp, jestli je drahá.

**Blueprint proti C++ v profileru** [(58:15)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=3495s) je jediné místo, kde se toho v celé knihovně o tomhle srovnání dozvíš — a je to méně, než by člověk čekal: *„optimalizuješ-li blueprinty, bude to vypadat trochu jinak, protože v Insights dostaneš blueprintové události místo C++ volání. Vyber si jed. Postup optimalizace zůstává v tomhle ohledu stejný."* Jeden praktický rozdíl přece jen zazní: po změně C++ se přeloží jen ten soubor, kdežto **u blueprintů se musí znovu cookovat**.

**A druhá polovina, bez které je měření k ničemu** [(1:10:46)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=4246s): *„vidět ty metriky je skoro stejně důležité jako mít aspoň základní představu o tom, co od čeho čekáš, že bude stát — protože jinak se podíváš na něco, co trvá vteřinu, a řekneš si: no… já nevím, jestli to tak dlouho trvat má."* Autoři to hned poctivě omezí: **žádná univerzální tabulka neexistuje**, protože ta představa závisí na stroji i na cílové platformě. Nedá se tedy opsat — dá se jen **vypěstovat měřením vlastního projektu**, a proto se s ním má začít dřív, než něco hoří.

**A důvod, proč se to vyplatí dělat, i když teď nic nehoří**, formuluje autor jako obranu proti sobě samému [(34:22)](https://www.youtube.com/watch?v=bfkbwXVMtn8&t=2062s): *„když neměřím, tak něco pushnu a za půl roku to vybouchne a já přemýšlím, jestli jsem to udělal já. To radši nechci být přistižen."*

> **Pozn.:** „Tvůj kód není vidět, dokud ho neoznačíš" je věc, která se nedá odvodit ze zkušenosti — buď ji někdo řekne, nebo se profiluje naslepo. A má nepříjemnou vlastnost: **profiler nevypadá, že něco skrývá.** Ukáže plný, věrohodný strom, ve kterém tvoje drahá funkce prostě splynula s enginem — takže nehledáš dál, protože si myslíš, že vidíš všechno. To je horší než chybějící nástroj. Nejužitečnější zobecnění je ale ta druhá půlka: **číslo bez očekávání není informace.** Tohle platí daleko za profilingem a je to důvod, proč má [reprodukovatelný test](#reprodukovatelny-test-bez-nej-neporovnas-nic) a [srovnávací čísla](#cisla-se-kterymi-se-da-srovnavat) v téhle kapitole tolik místa — teprve druhé měření je měření. A pro sólo vývojáře jedna praktická útěcha: ta „základní představa" nemusí být z tabulek. Stačí **jednou proměřit skoro prázdný projekt** a máš krajní bod, ke kterému se dá vztáhnout všechno další; ostatně přesně to doporučuje i [automatizovaný benchmark](mereni-automaticky.md#benchmark-z-level-sequence-mereni-jako-soucast-prace).

**Souvislosti:** [Co je v herním vlákně a co v renderovacím](#co-je-v-hernim-vlakne-a-co-v-renderovacim) · [Reprodukovatelný test](#reprodukovatelny-test-bez-nej-neporovnas-nic) · [Čísla, se kterými se dá srovnávat](#cisla-se-kterymi-se-da-srovnavat) · [Benchmark z level sequence](mereni-automaticky.md#benchmark-z-level-sequence-mereni-jako-soucast-prace) · [Programátorské návyky](../teorie/programatorske-navyky.md) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights) · [Rejstřík: Trace channel](../rejstrik.md#trace-channel)

---


## Nález není hotová práce: předání

**Zdroj:** [Technical Artist's Guide to Profiling in Unreal Engine](https://www.youtube.com/watch?v=mCZRHljYnZA) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~33 min, Unreal Fest Orlando 2025

**Shrnutí:** Poslední třetina přednášky je o věci, kterou technické materiály obvykle vynechají: **co s nálezem, když ho máš.** Autorka to formuluje z praxe — *„jako tech artist najdeš tu drahou věc a řekneš si ‚vždyť je to tady', jenže content creator ani programátor s tou informací hned nic neudělají."* Kapitola je proto o dvou hranicích: **kdy přestat kopat** a **co musí obsahovat předávka**, aby druhá strana nezačala od nuly.

### Rozpad myšlenky

**Kdy přestat** [(22:46)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=1366s) je rozhodnutí, na kterém se dá ztratit dny. Autorčino kritérium je pěkně praktické: **je pod nálezem vidět obsah?** Vidíš-li ve stromu konkrétní drahý objekt, který je ve scéně tisíckrát, máš adresáta — a klidně i tým, protože u něj bývá tag. **Není-li tam žádný obsah** (v jejím příkladu 28,6 ms v renderu bez viditelné příčiny), je čas předat to specialistovi. Její zdůvodnění je efektivní, ne rezignované: *„nedoporučovala bych tech artistům trávit čas učením se celého fyzikálního systému, když je mnohem efektivnější to předat dál."*

**Rozpočty jako předpoklad** [(21:59)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=1319s): bez nich nepoznáš, jestli je nález nález. *„Odhadneš, že tady je asi 10 ms fyziky. Porovnáš to s rozpočtem, kde fyzika má dvě tři milisekundy — a řekneš si moment, tohle je drahé."* Rozpočet je tedy nástroj **rozhodování**, ne reportingu, a je potřeba mít ho pro CPU i GPU.

**Předávka** [(29:10)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=1750s) má u nich podobu kontrolního seznamu, který stojí za převzetí skoro doslova: **stručné shrnutí problému** · **odkaz na ticket** · **základní analýza** (*„jako tech artist se netrap tím, že nevíš přesně, proč je fyzika drahá — udělej, co umíš"*) · **platforma**, a na PC i **model GPU** · **jasné kroky k reprodukci** · **changelist buildu** · **číslo snímku** v traci · **co nejvíc médií** (screenshoty, video) · **screenshot traci se zvýrazněným místem** · a **cesta k souboru traci** na síti.

**A infrastruktura kolem** [(28:22)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=1702s): jeden **společný kanál** na diskuzi nad nálezy (než se z nich stanou tickety), **šablona ticketu** s předvyplněnými poli — připravená s producentem, aby stačilo kliknout — a **dashboard** rozdělený po týmech s burndown grafem, *„aby se ty optimalizace opravdu hýbaly dopředu"*.

**A vrstva, která tomu všemu předchází** [(1:37)](https://www.youtube.com/watch?v=mCZRHljYnZA&t=97s), protože nejlevnější profiling je ten, který nemusíš dělat: **validace assetů**. Data validation plugin kontroluje při vstupu do editoru jednoduchou i složitou kolizi, počet materiálů a vrstev, hustotu meshe a strop polygonů. Spouští se ručně z content browseru, **vynuceně při odevzdání** (a výsledek se zapíše do popisu changelistu) a **každou noc na build stroji** s výpisem do týmového kanálu. Vedle toho **Asset Audit** a **Statistics** dají tabulku assetů (polygony, materiály, rozměry, Nanite ano/ne) a **počty instancí za běhu**; obojí umí export do CSV, takže se z toho dá skriptem udělat metrika s barevným kódováním — *„aby content creator hned viděl, kam zaměřit úsilí."*

> **Pozn.:** Tahle myšlenka je důvod, proč kapitola nekončí u nástrojů. **Profiling je z poloviny komunikační disciplína**, protože nálezy skoro nikdy neopravuje ten, kdo je našel — a nález bez reprodukce, buildu a kontextu se v cizí frontě rozpadne na „nedokázal jsem to zopakovat". Souvisí to s tím, co má knihovna popsané u [dokumentace jako auditu](../zapisky/dokumentace-jako-audit.md): zapsat nález není administrativa, je to podmínka toho, aby se s ním dalo něco udělat. A ta validační vrstva je totéž o patro dřív — **levnější než hledat drahé assety je nepustit je dovnitř**, což je táž logika jako [nástroj, který hlídá konzistenci dat](../godot/projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate).

**Souvislosti:** [Reprodukovatelný test](#reprodukovatelny-test-bez-nej-neporovnas-nic) *(co musí být v předávce doložené)* · [Dokumentace jako audit](../zapisky/dokumentace-jako-audit.md) · [Organizace projektu](organizace-projektu.md#content-browser-podle-epicu-feature-foldery-developers-a-redirectory) · [Plánovací nástroje](../teorie/planovani-nastroje.md#kanban-karty-zleva-doprava-a-jeden-vlastnik-na-kartu) · [Rejstřík: Data validation](../rejstrik.md#data-validation) · [Rejstřík: Telemetrie](../rejstrik.md#telemetrie)
