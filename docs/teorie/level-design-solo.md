# Level design pro sólo vývojáře

Většina obsahu o level designu vzniká jako příprava na kariéru v AAA studiu, kde level designér dostane hotovou hru, sadu pravidel a tým kolem sebe. Sólo vývojář má opačnou situaci: hru teprve vymýšlí, pravidla si musí napsat sám a nikdo mu neřekne, kdy je čas přestat prototypovat a začít stavět. Indie Game Clinic proto neradí, *jak* dělat levely, ale **jak číst cizí rady o level designu** — a k tomu přidává rozlišení, které tuhle fázi vývoje řídí: kde končí game design a začíná content.

---

## Game design vs. level design: co je vlastně content

**Zdroj:** [Game vs Level Design [explained with Golf and Robots]](https://www.youtube.com/watch?v=R7N1XUKL5JE) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~20 min, analýza hry

**Shrnutí:** Hra se skládá z **gameplaye** (mechaniky a systémy — co hráč dělá) a **contentu** (všeho, co se dá opakovat s variacemi — levely, nepřátelé, příběh, odemykatelné věci). Rozdíl není akademický: **levely testují hráčovo porozumění mechanikám**, takže je nemůžeš navrhnout dřív, než víš, jaké momenty chceš vyrábět. Nejčastější chyba indie vývojářů je výroba hory contentu do hry, která ještě není hotová.

### Rozpad myšlenky

Video otevírá citátem, který se mylně připisuje Marku Twainovi — „golf je zkažená procházka" — a dělá z něj překvapivě funkční definici [(1:04)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=64s): **jednoduchá cesta z A do B, zkomplikovaná překážkami a obstrukčními pravidly, je v podstatě všechen game design**. Odtud plyne i dělba práce: **golf je hra, golfové hřiště je level** [(2:37)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=157s). Vynález golfu teprve otevřel možnost hřišť — a dnes si golf bez hřiště neumíme představit, i když jedno bez druhého vzniknout muselo. Minigolf to dokládá z druhé strany [(3:24)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=204s): stejný core gameplay, ale level design diktuje, že si vystačíš s putterem.

Definice contentu je širší, než se čeká [(1:51)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=111s): **cokoli, co jde opakovat s variacemi, aby hráč strávil ve hře víc času** — levely, varianty nepřátel, příběh, kosmetika, odemykatelné věci. Ve velkých studiích to dělají úplně jiní lidé než ti, kdo navrhují interaktivitu, a to z praktického důvodu: **levely obvykle nejde navrhnout, dokud nevíš, o čem hra je**, protože jejich úkolem je testovat hráčovo porozumění mechanikám tak, jak jsou postupně zaváděny [(2:37)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=157s).

Praktický důsledek je varování, které autor vidí opakovaně v hrách posílaných na analýzu [(3:24)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=204s): **vývojáři se ženou do výroby spousty contentu, než je hra na content připravená**. „Je těžké dělat levely, když nevíš, jaké momenty výzvy, tajemství nebo novosti chceš hráči dát" [(4:11)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=251s). Video to ilustruje smyšlenou historkou o skotském šlechtici, který si prý v roce 1332 postavil osmnáctijamkové hřiště dřív, než byl vynalezen golf — a později přizná, že si toho pána vymyslel [(11:20)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=680s). Obraz ale sedí: hřiště bez pravidel hry je jen zvláštně posekaná louka.

> **Pozn.:** Tohle je konkrétní důvod, proč [tři brány prototypování](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce) staví plnou produkci až za vertical slice — plná produkce **je** výroba contentu. A rozlišení gameplay/content dává i praktické kritérium pro [scope](scope.md#mala-hra-jedna-mechanika-ne-zmenseny-skyrim): u malé hry se neškrtají mechaniky, škrtá se content.

**Souvislosti:** [Prototypování: tři brány](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce) · [Scope: malá hra = jedna mechanika](scope.md#mala-hra-jedna-mechanika-ne-zmenseny-skyrim) · [Herní art: prostředí je 90 % obrazovky](art-pipeline.md#prostredi-je-90-obrazovky-a-musi-mluvit) *(kdo greybox převezme a co s ním udělá)* · [Rejstřík: content](../rejstrik.md#content)

---

## Téma ospravedlňuje mechaniky — a landmark musí být jediný svého druhu

**Zdroj:** [Game vs Level Design [explained with Golf and Robots]](https://www.youtube.com/watch?v=R7N1XUKL5JE) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · druhá půlka analýzy

**Shrnutí:** Analyzovaná hra je golf, kde hrajete robota — a to není náhoda ani rozmar: **robot je alibi pro mechaniky, které by jinak působily jako berličky** (let, boost, simulované zkušební rány, herní rozhraní uvnitř fikce). Zajímavější je ale kritika, která přijde vzápětí: téma prostoupilo mechaniky, ale **nedostalo se do level designu** — a video na tom ukazuje dvě přenositelná pravidla o orientaci v prostoru.

### Rozpad myšlenky

Princip, na kterém hra vyhrává [(5:43)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=343s): **vyber téma nebo setting, který pomůže ospravedlnit podivná pravidla nutná k tomu, aby hra byla zábavná**. Robotí tělo dává důvod k létání i k boostu, dělá srozumitelnými zkušební rány, které si můžeš zkusit „nanečisto", a **usazuje rozhraní dovnitř světa hry** místo aby viselo nad ním. Autor to shrnuje větou, kterou stojí za to si pamatovat [(6:31)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=391s): **„je praktické být robot, co umí létat, v golfové hře — stejně jako je praktické být nesmrtelný v roguelike, který se opakuje ve smyčce."**

Kritika je o to zajímavější, že směřuje na *nevyužitou* příležitost [(7:17)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=437s): pouštní hřiště by mohlo klidně být na Zemi. Sci-fi téma neovlivnilo tvar terénu ani kompozici, takže **hra si sama upřela wow efekt, který by dostala zadarmo** — „nestavíme to ve skutečném světě, nemáme omezení skutečných architektů hřišť" [(11:20)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=680s).

A z toho plynou dvě pravidla o orientaci, která platí v jakémkoli otevřeném prostoru:

- **Opakovaný objekt přestává být landmark** [(8:51)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=531s). Satelitní talíře rozeseté po panoramatu vypadají dobře, ale protože jich je víc stejných, **hráči nepomůžou určit, kde je** — a objekt tím ztratil funkci, kterou mohl mít. Video na to má dokonalý obraz: **je to rozdíl mezi hledáním Eiffelovky ve městě a hledáním mrakodrapu.**
- **Měřítko dělá dvě práce najednou** [(9:39)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=579s): jeden nebo dva obří orientační body na mapu dodají wow efekt **a zároveň** usnadní rozlišit jednotlivé části úrovně a snížit riziko, že hráč zabloudí. Estetické a funkční se tu nepere — jde o totéž rozhodnutí.

Poslední vrstva kritiky se týká doručení obsahu [(12:54)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=774s): hra má příběhový režim, ve kterém se dlouho nehraje golf. A protože hra **nosí golf v názvu i brandingu**, hráči, kteří kvůli němu přišli, musí golf dostat brzy [(17:20)](https://www.youtube.com/watch?v=R7N1XUKL5JE&t=1040s). Závěr videa je proto neobvyklý: mechaniky jsou solidní, prezentace vyleštěná — **problémem je struktura a pořadí, v jakém hra svůj content podává**.

> **Pozn.:** „Téma jako alibi pro mechaniku" je táž technika jako [omezení potřebuje herní alibi](scope.md#omezeni-potrebuje-herni-alibi), jen obráceně: tam fikce ospravedlňuje, co ve hře **není**, tady ospravedlňuje, co v ní **je** navíc. A pravidlo o jedinečnosti landmarku doplňuje [landmark napřed](prostor-a-hranice.md#jeskyne-ktera-se-hraje-landmark-napred-detail-nakonec) o podmínku, kterou je snadné porušit kopírováním assetu.

**Souvislosti:** [Scope: omezení potřebuje herní alibi](scope.md#omezeni-potrebuje-herni-alibi) · [Prostor a hranice: landmark napřed](prostor-a-hranice.md#jeskyne-ktera-se-hraje-landmark-napred-detail-nakonec) · [Ludotematický soulad](ludonarativni-soulad.md#zanr-je-gameplay-tema-je-jazyk-a-tema-uci-hru-za-tebe) · [Rejstřík: landmark](../rejstrik.md#landmark)

---

## Nejsi následovník: jak číst cizí pravidla o level designu

**Zdroj:** [Level Design Approaches for Solo Devs](https://www.youtube.com/watch?v=OLXn6YYAk7M) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~21 min, přednáška

**Shrnutí:** Rady o level designu jsou většinou psané pro člověka, který bude levely dělat pro cizí hru. Sólo vývojář je ale **design lead svého projektu**, takže jeho úkolem není cizí pravidla dodržovat, ale **napsat si vlastní** — a u každého převzatého pravidla vědět, jakému zážitku hráče slouží. Romerova slavná pravidla pro Doom video ukazuje ne jako předpis, ale jako důkaz, že si takový seznam každý dělá sám.

### Rozpad myšlenky

Nejdřív terminologické pročištění, bez kterého se rady čtou špatně [(2:21)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=141s): populární videa typu „12 tipů pro level design" bývají ve skutečnosti o **environmentálním artu a technice** (occlusion culling, nenačítání věcí za dveřmi). Jsou to dobré tipy, jen nejsou level design. Proč se to plete [(3:09)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=189s): nováček se musí učit hlavně technikálie, a tak si osvojí dojem, že **design znamená postavit něco v enginu**. Video proti tomu staví ostrou hranici: **„level design je o funkčnosti v gameplayi; art je o tom udělat to koherentní a přitažlivé."**

Jádro přednášky je ale metodické [(11:43)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=703s): „nasbíráš informace z různých přednášek a **potřebuješ přístup, jak je zpracovat** — protože když děláš vlastní hru sám, **jsi vedoucí a musíš se chovat jako vedoucí, ne jako následovník**. To je podstata role design leada: definovat pravidla projektu tak, aby byl konzistentní a dával smysl." Nástroj k tomu je jediná otázka [(12:29)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=749s): **jakému cíli v hráčově zážitku tohle pravidlo slouží?**

Na Romerových osmi pravidlech pro Doom to video předvádí [(9:22)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=562s) — a rovnou varuje, že je nepředkládá jako univerzální zákony:

1. **Změň výšku podlahy, když měníš texturu podlahy.**
2. **Používej speciální okrajové textury** mezi segmenty zdí a dveřmi, aby byla čitelná geometrie.
3. **Buď přísný na zarovnání textur** — s jednou vědomou výjimkou: **u tajných dveří zarovnání schválně naruš**, ať má hráč vodítko [(10:56)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=656s).
4. **Kontrast všude**: světlé versus tmavé místnosti, otevřené versus stísněné.
5. **Vidí-li hráč ven, měl by se tam dostat** — autor to čte skoro jako profesní hrdost: v levelu nemá být nic falešného.
6. **Několik tajných oblastí v každém levelu.**
7. **Veď flow tak, aby se hráč do míst vracel** a lépe pochopil prostor jako trojrozměrný celek.
8. **Snadno rozpoznatelné landmarky na několika místech** kvůli navigaci.

Když se pak zeptáš, čemu ta pravidla slouží [(12:29)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=749s), vyjde srozumitelná mapa: **pocit dovednosti a úspěchu**, **čitelnost a navigace** (proto jsou i zdánlivě „artové" body ve skutečnosti designové), **střídání zájmu a nudy** a **budování světa**. Tím se z osmi cizích pravidel stane šablona, podle které si napíšeš vlastní.

Odtud plyne i obecnější stanovisko [(13:18)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=798s): lidé chtějí univerzální „vždycky dělej tohle" — někdy proto, že jejich zkušenost se vzděláváním spočívala v přebírání pravidel. **„Umění a design tak nefungují — a nefunguje tak ani informatika nebo inženýrství."** Jediné, co je podle autora skutečně univerzální, je **lidská psychologie a chování** [(14:04)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=844s). Ukázkou je „flow" hráčů: pohybují se prostorem **jako voda, ne v pravých úhlech** — chtějí prozkoumat každý kout, protože nechtějí přijít o poklad nebo tajemství [(14:51)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=891s). Jenže — a tohle je pointa — **je to chování řízené obsahem hry: když hra hráče naučí, že v koutech nikdy nic není, přestanou je prohledávat** [(15:37)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=937s).

> **Pozn.:** „Nasbírej rady, ale rozhodni sám" je totéž stanovisko, jaké zaznívá v [teorie designu je mapa, ne návod](zaklady.md#teorie-designu-je-mapa-ne-navod) a v [radách, které nefungují tam, kde začíná design](rady-z-praxe.md#rady-nefunguji-tam-kde-zacina-design). Tři různá videa, jedna teze — v knihovně je to jedna z nejlépe doložených.

**Souvislosti:** [Základy: teorie designu je mapa](zaklady.md#teorie-designu-je-mapa-ne-navod) · [Rady z praxe: kde končí platnost rad](rady-z-praxe.md#rady-nefunguji-tam-kde-zacina-design) · [Vedení hráče](vedeni-hrace.md#scripted-events-veci-se-maji-stat-ve-spravnou-chvili) · [Rejstřík: graybox](../rejstrik.md#graybox)

---

## Graybox, beautiful corners a první level nakonec

**Zdroj:** [Level Design Approaches for Solo Devs](https://www.youtube.com/watch?v=OLXn6YYAk7M) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · procesní část přednášky

**Shrnutí:** Sólo vývojář nemá oddělení, které by ho oddělilo od pokušení zkrášlovat level dřív, než ví, jestli funguje. Proto potřebuje procesní pravidla: **drž iterační cykly krátké**, dovol si **jeden krásný kout** místo krásného celku, **první level dělej poslední** a rozvrhni si obsah dřív, než ho začneš vyrábět. K tomu jedno realistické pravidlo o rozpočtu radosti.

### Rozpad myšlenky

Proč se v profesionálním procesu odděluje graybox od artu [(3:56)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=236s): **abys si nevyrobil problémy později**. Když prostředí zkrášlíš dřív, než ho pořádně otestuješ, každá pozdější změna je dražší — pracuješ s mnohem větším počtem objektů a navíc se ti do hotové věci zamotají emoce. Autor z toho dělá obecnější zákon [(4:42)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=282s): **„jedno z nejdůležitějších pravidel vývoje her je držet iterační cykly co nejkratší"** — a cokoli tě ve změnách zpomaluje, je problém, dokud nevíš, že hra je dobrá.

Námitku sólo vývojáře („nemám oddělení, dělám všechno") ale bere vážně a jmenuje dva legitimní důvody, proč se to stejně děje [(5:29)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=329s): **stejně musíš vyřešit art style a pipeline** (jak vypadá strom, jak kámen — tak proč to nedat rovnou do levelu), a **hotová hezká věc tě drží při chuti**, což je u člověka bez manažera zásadní. Řešení není zákaz, ale rozpočet [(6:16)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=376s): **pracuj v poměru zhruba 2:1 nebo 3:1 — dvě až tři věci, které hra potřebuje, a jedna, kterou děláš pro radost.** A když ta radostná věc začne dělat problémy, udělej si radost něčím jiným.

Za tím stojí rámec, který video používá i jinde [(6:16)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=376s): každá hra potřebuje **nepořádnou kreativní experimentaci** i **strukturovaný strategický přístup**. Hra ze samé experimentace se buď nedokončí, nebo bude chaotická; **hra ze samé strategie bude nudný klon bez čehokoli vlastního**.

Nástroje, kterými se to řídí:

- **Beautiful corner** [(7:02)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=422s): zavedená praxe, kdy je celá hra v grayboxu a **jediný malý kus je dotažený do cílové kvality** — „mikro vertical slice", jedna místnost jako art prototyp. Umožní ověřit vizuální cíl, aniž bys zabetonoval celou hru.
- **„Finish your first level last"** [(7:49)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=469s), citát Johna Romera. Takhle vznikl i první svět Maria — byl postavený jako poslední. Video přidává střízlivé vysvětlení: **není to moudro, je to logika. Udělej střed hry a začátek dělej později, až víš, do čeho vlastně hráče uvádíš.**
- **Plánovací tabulka obsahu** [(8:35)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=515s): rozvrh, kde jsou v řádcích levely a ve sloupcích **prostředí** (aby se střídalo a hra nebyla vizuálně nudná), **téma levelu**, **stoupající obtížnost** a **mechaniky**, které se v tom levelu poprvé objeví. Dá ti to pohled na celkový tok hry dřív, než vyrobíš první kus.

Nakonec konkrétní ukázka toho, jak jemné rozhodování level design je [(17:57)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=1077s): schody. Sejdeš-li po nich přímo do místnosti, **vcházíš naslepo** a všechno vidíš až uvnitř; postavíš-li je tak, že nejdřív dojdeš na vyhlídkový bod, **dostane hráč možnost si prostor prohlédnout a rozhodnout se**. A protože schody jsou z dálky špatně vidět, je potřeba **je telegrafovat** — nechat je vyčnívat, aby je hráč zaregistroval včas [(18:44)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=1124s). Ani tady video neříká, která varianta je správná: říká, že **si musíš vybrat a pak to dělat konzistentně**.

> **Pozn.:** „Level je současně čtyři věci" je nejlepší shrnutí toho, proč je to tak těžké [(15:37)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=937s): je to **místo** (simulace prostoru), **zážitek** (emoce v sekvenci: souboj, ticho, střetnutí, puzzle), **cíl** (hráč musí vědět, o co jde — a cíl smí občas zmizet a znovu se objevit, aby vznikla úleva) a **jazyk** (nekonzistence mate). Mimochodem právě proto jsou sci-fi a fantasy dungeony pro malé týmy praktičtější [(17:11)](https://www.youtube.com/watch?v=OLXn6YYAk7M&t=1031s): u abstraktního prostoru nemusíš řešit, „kde je v dungeonu záchod nebo kde ve vesmírné lodi sídlí personální oddělení".

**Souvislosti:** [Prototypování: iterační spirála](prototypovani.md#iteracni-spirala-ke-stredu-nevede-rychly-pruh) *(tentýž princip krátkých cyklů na úrovni celého projektu)* · [Herní art: prostředí a greybox pipeline](art-pipeline.md#prostredi-je-90-obrazovky-a-musi-mluvit) · [Žrouti času: leštění bez validace](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) · [Rejstřík: beautiful corner](../rejstrik.md#beautiful-corner) · [Rejstřík: graybox](../rejstrik.md#graybox)

---

## Nástroj tvaruje level: co udělá editor s tvým designem

**Zdroj:** [Creating an In-Game Level Editor | Indie Devlog #9](https://www.youtube.com/watch?v=nAXMHOWliAA) · [Game Endeavor](https://www.youtube.com/channel/UCLweX1UtQjRjj7rs_0XQ2Eg) · ~8 min, devlog (2020)

**Shrnutí:** Devlog o stavbě vlastního level editoru obsahuje jedno pozorování, které přesahuje techniku: **nástroj, ve kterém level stavíš, tiše rozhoduje o tom, jaký level vznikne.** Autor si všiml, že když pracuje po jednotlivých scénách, začne stavět „aby byla scéna plná" — a výsledná cesta byla mnohem delší, než zamýšlel.

### Rozpad myšlenky

Situace je běžná [(0:46)](https://www.youtube.com/watch?v=nAXMHOWliAA&t=46s): hra měla samostatné scény, mezi kterými se přechází, a autor chtěl souvislý svět. Technicky to znamená rozdělit svět na **chunky, které se dynamicky načítají kolem hráče** — a nejdřív to zkoušel řešit uvnitř editoru enginu.

Zajímavé je, co ho k vlastnímu nástroji donutilo [(2:19)](https://www.youtube.com/watch?v=nAXMHOWliAA&t=139s). Když stavěl po scénách, přistihl se, že **vyrábí oblasti jen proto, aby zaplnil prostor**: fokus byl „vyplnit několik chunků", ne „jaké to bude z hráčovy perspektivy". Výsledek objevil, až když si celek zazoomoval — **cesta z města do dungeonu byla mnohem delší, než čekal**. Diagnóza je přesná a přenositelná: **byl omezený na jednotlivé buňky, takže jeho mysl řešila „jak vyplnit tuhle scénu", místo „jaký zážitek tímhle úsekem vzniká"**. Co chtěl místo toho: **jedno velké plátno, na které se svět maluje jako obraz**.

Zbytek devlogu je konkrétní ukázka, jak vypadá **nástroj postavený na míru vlastnímu workflow**, a stojí za pozornost svou skromností. Nejžádanější funkcí byla **velikost štětce** [(2:19)](https://www.youtube.com/watch?v=nAXMHOWliAA&t=139s) — v editoru enginu jde položit jedna dlaždice po druhé, „což je u pixel artu jako kreslit obrázek pixel po pixelu", a autor scény staví perem a tabletem stejně jako kresbu. K tomu klávesová zkratka na gumu, protože „nejspíš mažu víc, než kreslím". A přiznání, které se do devlogů obvykle nepíše [(3:08)](https://www.youtube.com/watch?v=nAXMHOWliAA&t=188s): implementace je **„hodně slepená dohromady a omezuje mě na velikosti, které si ručně určím — ale je to všechno, co teď potřebuju, a zabralo to pár minut, takže si nestěžuju"**. Rozhraní editoru je stejně střídmé: „není důvod to dělat složitější" [(3:56)](https://www.youtube.com/watch?v=nAXMHOWliAA&t=236s).

Druhý motiv je motivační: autorovým prvním setkáním s vývojem her byl herní editor a **plánuje editor dát i hráčům** [(3:56)](https://www.youtube.com/watch?v=nAXMHOWliAA&t=236s). Zdůvodnění je hezky obrácené: **„dělat hru snů je fajn, ale protože ji navrhuju sám, budu o ní vědět všechno. Těším se hrát věci, které vytvoříte vy — ty budou pro mě nové."**

> **Pozn.:** Video je z roku 2020 a technická část (chunk loading, práce s dlaždicemi, vlákna versus hlavní smyčka) je vázaná na tehdejší verzi jednoho enginu — přenosné je z ní hlavně to, že **načítání po částech se dá rozložit do snímků**, když zamrzávání trápí. Zajímavá poznámka mimochodem [(5:32)](https://www.youtube.com/watch?v=nAXMHOWliAA&t=332s): přechody mezi scénami nejsou jen technický kompromis — **pomáhají hráči stavět si mentální mapu světa** tím, že si všímá, kde k nim dochází.

**Souvislosti:** [Plánovací nástroje: kanban](planovani-nastroje.md#kanban-karty-zleva-doprava-a-jeden-vlastnik-na-kartu) *(jiný nástroj, tentýž efekt na práci)* · [Prostor a hranice](prostor-a-hranice.md#jeskyne-ktera-se-hraje-landmark-napred-detail-nakonec) · [Level streaming v UE](../praxe/levely-a-streaming.md) *(chunky a načítání v praxi)* · [Rejstřík: level streaming](../rejstrik.md#level-streaming)
