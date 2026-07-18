# Žrouti času: kam mizí měsíce vývoje

Vývoj hry trvá dlouho i bez chyb — od tří měsíců po roky. Studio BiteMe Games sepsalo sedm pastí, ve kterých vývojáři ztrácejí dny až měsíce; tady jsou přeskládané podle toho, *proč* fungují: práce bez validace, únik k snadné tvorbě, bobtnání hry a mýtus „všechno sám". Když poznáš mechanismus pasti, poznáš i její další převleky. A protože největší žrout času je projekt, který se nikdy nedokončí, přibyly dvě lekce o dokončování: proč motivace nestačí a kde přesně první hry umírají.

---

## Investice bez validace: leštění, systémy a optimalizace předem

**Zdroj:** [7 Gamedev Time Wastes](https://www.youtube.com/watch?v=nckLk3qJ-yo) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · ~21 min, zkušenosti studia

**Shrnutí:** Tři z pastí videa jsou jedna a táž chyba v různých kostýmech: utrácíš čas za kvalitu něčeho, o čem ještě nevíš, jestli to hra vůbec potřebuje. Over-polishing, stavění „enginů v enginu" i předčasná optimalizace mají společný protijed — validaci: zpětnou vazbu, která řekne, co si investici zaslouží.

### Rozpad myšlenky

**Over-polishing** [(0:54)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=54s): platí 80/20 — 20 % úsilí přinese 80 % výsledku a posledních 20 % výsledku sežere 80 % času [(1:20)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=80s). Hyper-polish si zaslouží jen jádro hry (video jmenuje Balatro: animace karet, rostoucí čísla, plamínky — přesně to, co hráč dělá pořád); zbytek stačí na 80 %. Bez zpětné vazby ale nevíš, *co* je jádro — a leštíš všechno. Řešení je vnější: buildy na itch.io, dema, playtesty, akce.

**Engines inside your engine** [(5:38)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=338s): past programátorů. Autor slyšel „strávil jsem dva týdny vlastním dialogovým systémem" doslova od desítek vývojářů [(6:00)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=360s) — návrh na 10 000 dialogových záznamů dřív, než existuje pět natvrdo napsaných replik, které by ověřily, jestli dialogy ve hře vůbec fungují. Stavět systémy je zábavnější než stavět hru; mezitím hra stojí, motivace klesá. Rada z videa: klidně to později **refaktoruj** [(7:56)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=476s) — refactoring validované věci je levnější než měsíc práce na nevalidované.

**Premature optimization** [(8:43)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=523s): přepis na ECS, když hra běží na 200 FPS. I tady 80/20: většinu velkých problémů vyřešíš měsíc před vydáním za zlomek času — a hyper-optimalizace navíc deformuje workflow po celý vývoj. Výjimka: tvrdý platformní cíl (slabý handheld) — pak je to požadavek, ne optimalizace.

> **Pozn.:** Společný test všech tří: „mám důkaz, že na tomhle záleží?" Pokud důkaz neexistuje, nejlevnější další krok není práce, ale získání důkazu. Souvisí s [the Gap](rady-z-praxe.md#the-gap-rozdil-mezi-to-je-hezky-a-tohle-musim-hrat) — i validace má své pasti.

**Souvislosti:** [Rady z praxe: idea iceberg](rady-z-praxe.md) · [Postmortem ShantyTown](postmortem-shantytown.md#kruhy-logaritmicky-pokrok-a-systemy-ktere-jen-bavilo-stavet) · [Rejstřík: premature optimization](../rejstrik.md#premature-optimization) · [Hudba a zvuk: začít a vydržet](../hudba/zacit-a-vydrzet.md) *(hudba jako odkládaná disciplína)*

---

## Únik k snadné tvorbě: world building a dokonalý toolset

**Zdroj:** [7 Gamedev Time Wastes](https://www.youtube.com/watch?v=nckLk3qJ-yo) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · stejné video

**Shrnutí:** Druhá dvojice pastí není o špatné investici, ale o útěku: mozek samovolně driftuje k činnostem, které *vypadají* jako vývoj a jsou řádově snazší než vývoj sám. Vymýšlet jména měst je stokrát lehčí než implementovat mechaniku; ladit Kanban board je lehčí než ladit hru.

### Rozpad myšlenky

**Endless world building** [(2:57)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=177s): začátečnická verze úniku. Lore, dialogy, jména postav, plány měst — měsíce „práce na hře", po kterých není co hrát. Zákeřné je, že world building nemá přirozený konec („teď je příběh hotový") a že příběh málokdy hru odliší — kdo chce vyniknout jen psaním, soutěží s nejlepšími spisovateli žánru. Klíčová diagnostická otázka z videa [(4:59)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=299s): **dělám hru, nebo dělám příběh?** Obojí je legitimní; problém je dělat jedno a myslet si, že děláš druhé.

**Chasing the perfect toolset** [(10:38)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=638s): verze pro softwarové inženýry. Build pipeline pro pět platforem, automatizované větve, ping-pong mezi Notionem, Asanou a Obsidianem — projektové řízení jednočlenného týmu na plný úvazek. Kontrastní datový bod z videa: jejich hra vznikla podle papírového checklistu se ~150 položkami [(12:22)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=742s), a stačilo to. Nástroj má být nudný a neviditelný; každá hodina v meta-práci je hodina mimo hru.

> **Pozn.:** Ironie, kterou přiznávám v reálném čase: skripta, která právě čteš, jsou přesně tenhle typ rizika — infrastruktura kolem tvorby místo tvorby. Obrana je stejná jako u world buildingu: pevný rozsah a otázka „slouží to hře, kterou dělám?".

**Souvislosti:** [Start projektu: design dokument](jak-zacit.md#design-dokument-ktery-skutecne-otevres-nastenka-misto-eseje) · [Proč tvořit: past rešerše](proc-tvorit.md#prazdne-platno-zacni-rychle-ale-resersuj-bez-studu)

---

## Scope creep a míchání žánrů: dvojsečná past

**Zdroj:** [7 Gamedev Time Wastes](https://www.youtube.com/watch?v=nckLk3qJ-yo) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · stejné video

**Shrnutí:** „Co kdybychom přidali rybaření?" Scope creep video nezavrhuje šmahem — někdy je to přesně ten twist, který hře chyběl. Častěji je to ale jen bobtnání; a nejnebezpečnější poddruh, míchání žánrů, umí vyrobit hru, kterou nechce nikdo.

### Rozpad myšlenky

Scope creep [(13:12)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=792s) má dvě eskalace. První je **fraktální bobtnání**: rybaření → různé pruty → automatizované rybářské lodě — jeden nápad se rozpadne na padesát mechanik. Druhá je **genre blending**: přišít Souls-like combat k hře, která pro něj nebyla navržená. Intuice říká „sečtu dvě publika"; realita je průnik, ne sjednocení [(15:05)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=905s) — fanoušci tower defense nechtějí Souls-like a fanoušci Souls-like nechtějí tower defense. Autorův příměr: mám rád zmrzlinu a mám rád steak [(15:29)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=929s) — dohromady je nechci. Hra pro všechny je hra pro nikoho.

Kdy je scope creep záchrana a kdy zkáza, umí rozlišit jen zkušenost — video to říká na rovinu. Praktická náhrada zkušenosti: vrať se k účelu hry ([hra ti říká, čím chce být](postmortem-shantytown.md#hra-ti-rika-cim-chce-byt-ucel-jako-designovy-soudce)) a ptej se, jestli nápad účel *sytí*, nebo *ředí*.

**Souvislosti:** [Co znamená „dělej malé hry"](scope.md) · [Postmortem ShantyTown](postmortem-shantytown.md) · [Rejstřík: scope creep](../rejstrik.md#scope-creep)

---

## Všechno sám neuděláš — a nemáš

**Zdroj:** [7 Gamedev Time Wastes](https://www.youtube.com/watch?v=nckLk3qJ-yo) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · stejné video

**Shrnutí:** Sólo vývojář nosí hodně klobouků, ale nemusí nosit všechny. Asset packy, hotové shadery, zvukové balíky a koupené nástroje nejsou podvod — jsou to jediné, co dělá malé hry v rozumném čase vůbec možné.

### Rozpad myšlenky

Video dává memorabilní počty [(16:13)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=973s): psát příběh, kódit, kreslit 2D, modelovat 3D, dělat hudbu i marketing — to je plán na jednu hru za život. Vlastní odstrašující příklad studia: lokalizační toolkit psaný na koleni [(18:11)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=1091s) stál ~50 hodin práce a byl utrpení; u druhé hry koupili hotový asset za pár desítek dolarů. Padesát hodin, nebo čtyřicet babek — takhle konkrétně vypadá ta volba.

Nákup navíc často zahrnuje podporu: autorovi assetu se dá napsat, co chybí, a buď to přidá, nebo poradí jak na to. Kupovat se vyplatí přesně to, co dělat *nechceš* nebo *neumíš* (CRT shader, hudba, UI kit); vlastní ruce si nech na to, čím se hra liší. Závěrečná teze videa stojí za vytesání [(19:24)](https://www.youtube.com/watch?v=nckLk3qJ-yo&t=1164s): **malé hry nejde dělat, když děláš všechno sám** — paradox, který zní obráceně, a právě proto se mu tak snadno nevěří.

> **Pozn.:** Stejnou lekci říká postmortem ShantyTown z druhé strany: sólo vývojář, který si najal capsule art, zvuk, osvětlení, soundtrack i QA — a hru dokončil. Sólo je o vlastnictví rozhodnutí, ne o vlastnoruční výrobě všeho.

**Souvislosti:** [Postmortem ShantyTown](postmortem-shantytown.md#kruhy-logaritmicky-pokrok-a-systemy-ktere-jen-bavilo-stavet) · [Začátky bez zkušeností](zacatky-bez-zkusenosti.md) · [Rejstřík: asset pack](../rejstrik.md#asset-pack)

---

## Motivace startuje, disciplína dokončuje

**Zdroj:** [Why "Motivation" is Overrated](https://www.youtube.com/watch?v=kUTFNgESEUg) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~21 min, esej na divácké přání

**Shrnutí:** Motivace je nestabilní energie — chodí ve vlnách a kdo jede jen na ni, nikdy nedokončuje [(0:48)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=48s). Disciplína je opačná síla: ploché, konzistentní návyky pro nudné a repetitivní části práce [(3:56)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=236s). Potřebuješ obě — a hack videa zní: **vyrob si vnitřní disciplínu z vnějších závazků.** Ne „řekni lidem o plánu", ale „zavaž se něco konkrétního ukázat ke konkrétnímu datu" [(8:36)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=516s).

### Rozpad myšlenky

**Psychologické podloží — locus of control** [(1:36)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=96s): kdo vyrostl v prostředí, kde ho k práci vždycky někdo dotlačil, má externí locus — a v dospělosti čeká, až ho zase někdo dotlačí. Tvůrčí dospělost = převzít roli disciplinující figury sám nad sebou [(7:01)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=421s). Samouci mívají interní locus, ale jedou nárazově: tvoří, když přijde vlna. Cíle přitom stanovovat umíme — co chybí, jsou **procesy** [(4:42)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=282s): „trénink v úterý a ve čtvrtek", ne „vyhrát ligu". Proces nemusí být optimální, stačí, že existuje; autorův příklad z jamu: hodina artu denně na streamu dala za pět dní víc než pokusy o osmihodinové maratony [(6:15)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=375s).

**Vnější závazky v praxi** [(9:23)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=563s): autorova kapela zkouší jen proto, že má naplánované koncerty — koncert → zkoušíš → píšeš písně, iterační kruh. Herní obdoba jsou **review fáze zapečené do vývoje**: studia je mají zadarmo (agile build každé dva týdny), hobbysta si je musí vyrobit [(10:57)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=657s). Playtest se obvykle prodává přes „hra se zlepší" — stejně cenný je jeho disciplinární efekt: deadline s tváří, kterou nechceš zklamat [(10:10)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=610s). Konkrétní místa, kde závazek sehnat [(11:43)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=703s): přednáška ve škole výměnou za playtest třídy (imposter syndrom zmizí děláním), malé lokální conventions — i deskové a geek akce vývojáře rády vezmou, klidně jako „indie koutek" víc místních tvůrců [(14:04)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=844s) — a gamedev klub; když není, založ ho: měsíční sraz = měsíční deadline [(15:36)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=936s). Vzorový plán: odhadneš slice na tři měsíce → najdeš akci za tři měsíce → z jejích dat stavíš public betu za šest [(16:22)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=982s).

**Bonus, který se přehlíží** [(18:41)](https://www.youtube.com/watch?v=kUTFNgESEUg&t=1121s): iterace s vnějším publikem ti taky říká, **kdy skončit**. Tvůrci milují začátky — a nuda z projektu se umí maskovat jako „ta hra není dobrá". S pravidelným ukazováním rozhoduješ o pauze či konci podle reakcí, ne podle gut feelingu z nudy.

**Souvislosti:** [Začátky bez zkušeností: motivace vs. vůle](zacatky-bez-zkusenosti.md#sdileni-prace-neni-marketing-je-to-nastroj-uceni) · [Rady z praxe: kompilace](rady-z-praxe.md#kompilace-od-profiku-cti-problem-za-navrhem-ukazuj-brzy-ozen-se-s-hrou) · [Devlogy](devlogy.md) · [Rejstřík: Locus of control](../rejstrik.md#locus-of-control)

---

## Kde umírají první hry: mapa klifů z jedné výzvy

**Zdroj:** [Why 99% of Devs Never Ship Their First Game (I Have the Data)](https://www.youtube.com/watch?v=2PKTvinv-oo) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~7 min, data z autorovy 7denní výzvy

**Shrnutí:** Z 205 přihlášených do sedmidenní „postav první hru" výzvy pustilo první lekci 44 lidí, první build postavilo 28, přes druhý den (Blueprinty — první samostatné myšlení) prošlo 15 — a dokončil **jeden** [(0:02)](https://www.youtube.com/watch?v=2PKTvinv-oo&t=2s). Anekdota z jednoho běhu, ne věda — ale tvar té mapy sedí na všechno, co o dokončování říkají ostatní kapitoly, a dvě pozorování z ní stojí za zapamatování.

### Rozpad myšlenky

**První klif je na gauči** [(1:38)](https://www.youtube.com/watch?v=2PKTvinv-oo&t=98s): 161 lidí se přihlásilo a nikdy nepustilo ani minutu. Zápis sám o sobě je odměna — mozek zaplatí pocitem pokroku za e-mail ve formuláři. Je to táž past jako hromadění tutoriálů, plánování a kupování kurzů: *feels like game dev, editor never opened*. A úmrtí nejsou dramatická [(3:59)](https://www.youtube.com/watch?v=2PKTvinv-oo&t=239s): nikdo v datech nerage-quitnul — lidé si dali „jednodenní pauzu", která nikdy neskončila. **První hry neumírají výbuchem, umírají na pauze.**

**Vzor přeživších** [(4:45)](https://www.youtube.com/watch?v=2PKTvinv-oo&t=285s): z 28 stavitelů jich 25 postovalo buildy veřejně; ze soukromě stavějících se dál dostal jeden z pěti. Building in public tu není motivační citát, ale mechanismus: **když je pokrok vidět, přestává být skončení neviditelné.** Smyčka vítězů: ukaž se → postav malou věc → postni ji → vrať se zítra; talent, motivace ani titul v ní nefigurují [(4:45)](https://www.youtube.com/watch?v=2PKTvinv-oo&t=285s). A jediný, kdo dokončil, udělal to, co začátečníci fyzicky nesvedou: **seřezal půlku svého snu** (AI dopravu, chodce, celý druhý level), aby hra vyšla [(5:33)](https://www.youtube.com/watch?v=2PKTvinv-oo&t=333s). Každý klif na mapě je rozhodnutí, ne skill check [(6:19)](https://www.youtube.com/watch?v=2PKTvinv-oo&t=379s).

> **Pozn.:** Průhlednost na místě: video je zároveň promo autorovy platformy a další kohorty výzvy — čísla ber jako ilustraci vzoru, ne jako studii. Vzor ale nezávisle potvrzují [data přeživších u Choie](../teorie/uceni-v-ere-ai.md#ctyri-urovne-inzenyra-nahrazuje-se-output-ne-usudek) (build in public jako důkaz) i [Goodgisovo „ožeň se s hrou"](rady-z-praxe.md#kompilace-od-profiku-cti-problem-za-navrhem-ukazuj-brzy-ozen-se-s-hrou). A „seřezat půlku snu" má v knihovně vlastní nástroj: [cut line](../zapisky/cut-line.md).

**Souvislosti:** [Zápisek: Cut line](../zapisky/cut-line.md) · [Učení v éře AI](uceni-v-ere-ai.md) · [Scope a malé hry](scope.md) · [Rejstřík: Building in public](../rejstrik.md#building-in-public)
