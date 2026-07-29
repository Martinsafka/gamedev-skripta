# Případovka: proces

Poslední kapitola sekce a nejosobnější. Autor v ní přiznává technickou zkratku, kterou platil dva roky, změní po třech letech žánr celé hry, a mimochodem řekne nahlas věc, kterou většina devlogů zamlčuje: **dlouhé projekty přinášejí náhodné návaly demoralizace** a on netuší, proč se o tom nemluví.

Kapitola je tu proto, že tohle je ta část řemesla, kterou se z tutoriálů nenaučíš — a která rozhoduje o tom, jestli hra vyjde.

---

## Zkratka, kterou zaplatíš dvakrát

**Zdroj:** [The Dangers of Taking Shortcuts (as a Game Dev)](https://www.youtube.com/watch?v=qkefNtAPjUE) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~20 min, devlog

**Shrnutí:** Autor **každý jednotlivý projektil ve hře naprogramoval zvlášť** — vlastní fyziku, vlastní animace, vlastní object pooling, dokonce mimo vestavěný fyzikální systém. Dva roky. Video je přiznání a rozbor toho, co ho to stálo, a je poučné hlavně ve **zdůvodnění, proč to dělal**: *„strávit třicet minut rychlým splácáním projektilu, abych ho mohl otestovat, je hrozně svůdné proti tomu, kolik práce by dal obecný systém."* Háček, který z toho dělá univerzální lekci: nezaplatil dvakrát čas — zaplatil **časem a nemožností přidat funkci**.

### Rozpad myšlenky

**Tři náklady**, seřazené podle toho, jak pozdě se projeví [(2:22)](https://www.youtube.com/watch?v=qkefNtAPjUE&t=142s):

1. **Čas.** Odhaduje *„padesát, šedesát, možná sto hodin"* ručního psaní chování projektilů za dva roky. Kdyby pokračoval, *„nevydám to do roku 2047"*.
2. **Neudržovatelnost**, a tady je ten konkrétní příklad, kvůli kterému video funguje [(3:09)](https://www.youtube.com/watch?v=qkefNtAPjUE&t=189s). Přidal do levelu **pohyblivé plošiny** — a lahvička hozená nepřítelem na ně **nereaguje**, protože na to při psaní té lahvičky nemyslel. Opravit jednu je snadné. Jenže *„co pak vejce toho druhého nepřítele? To taky nebude fungovat. A spory toho třetího?"* Musel by projít **každý projektil ve hře** a nic nevynechat, protože **nic nesdílejí**.
3. **Nemožnost přidat funkci** [(4:42)](https://www.youtube.com/watch?v=qkefNtAPjUE&t=282s). Chce dát hráčce schopnost **odrážet projektily** mečem. To by znamenalo implementovat odrážení **do každého projektilu zvlášť** — a protože si psal i fyziku ručně, *„není žádná záruka, že obecný odražeč, který postavím, bude fungovat s jakýmkoli projektilem"*. Funkce, která by ve sdíleném systému byla odpoledne, je takhle **prakticky neproveditelná**.

**Proč to udělal**, popisuje bez sebeobelhávání [(5:29)](https://www.youtube.com/watch?v=qkefNtAPjUE&t=329s): *„vzadu v hlavě jsem si vždycky říkal, že jednou budu potřebovat obecný systém — ale tohle je zatím prototypování, chci být rychlý a lehký, nechci uvíznout v pekle systémů. Někdy ten systém udělám, bude skvělý, ale teď to neřeš."* To je poctivý popis mechanismu, kterým vzniká technický dluh: **není to lenost, je to racionální rozhodnutí s nesprávně odhadnutou splatností.**

**Řešení** je jeden uzel — **obecný fyzikální controller projektilů** [(6:15)](https://www.youtube.com/watch?v=qkefNtAPjUE&t=375s) — který řídí veškerý pohyb, a jeho hodnota je v jedné větě: *„chceme podporovat pohyblivé plošiny? Naučíme to tenhle uzel a rázem to umí každý projektil ve hře."* Totéž pro odrážení. Z nastavitelných věcí stojí za zmínku hlavně **balistika** [(10:09)](https://www.youtube.com/watch?v=qkefNtAPjUE&t=609s): místo ladění rychlostí a gravitace zadáš **cíl, dobu letu a výšku oblouku** a systém si dopočítá zbytek. Rozdíl v ladění je zásadní — *„nemusím se babrat s tím, co udělá, když zvýším svislou rychlost o dvanáct; řeknu ‚chci, aby to letělo o kus rychleji'."* Autorovo hodnocení: *„je to o řády rychlejší."*

**A pak přijde ta nejlepší pointa** [(14:48)](https://www.youtube.com/watch?v=qkefNtAPjUE&t=888s). Jeden projektil měl **odskakovat od zdí** a autor na tom strávil *„nespočet hodin"* — zkoušel raycasty, ohraničující objemy, pokaždé to fungovalo a pak zase ne. Protože nepoužíval vestavěnou fyziku. V novém systému **odrážení prostě funguje**, včetně nastavitelné ztráty rychlosti při odrazu. Jeho komentář: *„je to fakt hezké a zároveň fakt otravné. Nevím, co jsem to dělal."*

> **Pozn.:** Nejcennější kus není „nedělejte zkratky" — to je banalita. Je to **jak se pozná, že splatnost dluhu nastala.** Autorovy tři signály se dají použít jako kontrolní seznam: (1) opakuješ tutéž opravu na víc místech, (2) nová vlastnost by znamenala projít všechny existující instance, (3) přistihneš se, že nový nápad **nezkusíš**, protože by to bylo moc práce. Ten třetí je nejzáludnější, protože **není vidět** — dluh se neprojeví jako chyba, ale jako **nápad, který jsi nikdy neměl**. A vlastní výhrada k tomu: prototypovat rychle a nečistě je pořád správně; chyba nebyla v tom, že první tři projektily napsal ručně, ale že u toho zůstal, **když už bylo jasné, že jich bude padesát**. Ta hranice se dá odhadnout dřív — a přesně o ní je [duplicita jako cena, ne hřích](kompozice.md#komponenta-ma-byt-sobecka-test-kamene).

**Souvislosti:** [Komponenta má být sobecká](kompozice.md#komponenta-ma-byt-sobecka-test-kamene) *(kdy je duplicita v pořádku a kdy ne)* · [Frame data](pripadovka-nepratele.md#frame-data-definuj-system-driv-nez-ho-postavis) *(týž autor, systém udělaný správně napoprvé)* · [Létající nepřátelé](pripadovka-nepratele.md#letajici-nepratele-ve-trech-verzich-donut-misto-bodu) · [Principy architektury](../praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Rejstřík: Premature optimization](../rejstrik.md#premature-optimization) · [Rejstřík: Iterace](../rejstrik.md#iterace)

---

## Změna žánru po třech letech

**Zdroj:** [After 3 Years, I'm Changing My Indie Game's Genre!](https://www.youtube.com/watch?v=R_bX6FeEUFw) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~15 min, esej

**Shrnutí:** Po třech letech vývoje mění lineární platformer na **metroidvanii**. Rozhodnutí spustila jedna věta jeho ženy — *„a proč ji teda neděláš?"* — pronesená v okamžiku, kdy si postěžoval, že by mu metroidvania sedla líp. Nejcennější na tom videu není samotný pivot, ale **anatomie zaseknutí, které mu předcházelo**: nechuť k level designu se u něj zacyklila do sestupné spirály, kterou si celou dobu vykládal jako „normální těžkou část vývoje".

### Rozpad myšlenky

**Spirála** [(0:47)](https://www.youtube.com/watch?v=R_bX6FeEUFw&t=47s) je popsaná přesně a stojí za to ji poznat u sebe: *„čím víc se mi nedaří složit něco, s čím bych byl spokojený, tím víc se začínám děsit práce na levelech. A to je začarovaný kruh, protože čím míň mě to baví, tím horší je výsledek. Pochybuju o sobě, všechno přehodnocuju. Když se necítím dobře, odvedu špatnou práci — a špatná práce mě cítit hůř."*

A tady je ten výklad, který ho držel na místě [(1:33)](https://www.youtube.com/watch?v=R_bX6FeEUFw&t=93s): *„říkal jsem si, že ty plíživé pochybnosti a mizející motivace jsou klasické potíže vývoje her. To je prostě ta těžká část. Když na tom budu dál dělat, vyřeším to."* Někdy to platí. Tady to byl **signál, že je špatně zadání, ne úsilí** — a rozeznat ty dva případy od sebe je asi nejtěžší dovednost v celém řemesle.

**Proč to původně metroidvania nebyla** [(2:19)](https://www.youtube.com/watch?v=R_bX6FeEUFw&t=139s): chtěl **malý projekt**, sám, do roka, včetně veškeré grafiky a hudby. Pak dostal práci, přešel na částečný úvazek, přibral výtvarníka — *„a protože se ke mně přidal tak skvělý výtvarník, pořád jsem rozšiřoval scope, aby zbytek hry odpovídal kvalitě té grafiky."* A přitom **nikdy nepřehodnotil to původní rozhodnutí**, které vzniklo za úplně jiných podmínek. To je jádro celé myšlenky: **rozhodnutí zestárlo, ale nikdo ho nepřezkoumal.**

**Pět důvodů pro** [(5:24)](https://www.youtube.com/watch?v=R_bX6FeEUFw&t=324s), a všechny mají tvar „věc, kterou už umím / mám / dělám a nemám kam dát":

- **Budování světa.** Patnáct let vedl Dungeons & Dragons a *„world building byl vždycky moje nejoblíbenější část"*. Lore pro hru měl napsané, ale do lineárních levelů ho nešlo dostat: *„vždycky to působilo mělce, jako bych jen odkazoval na nějaké pozadí."*
- **Design nepřátel.** Má propracované nepřátele, jenže v lineárním levelu se hráč nedá donutit s nimi bojovat jinak než zavřením dveří — a omezovat prostor jde proti volnosti pohybu, kterou postava má. Jeho vlastní shrnutí je nejlepší věta videa: *„je to, jako bych navrhl nepřátele pro metroidvanii a pak je nacpal do lineárních levelů, kam nesedí — a byl frustrovaný, že to nefunguje."*
- **Části, které se mu líbily.** Do lineárních levelů pořád propašovával **tajemství a odbočky** a *„byly to vždycky moje nejoblíbenější části"* — a přitom tam nepatřily.
- **Škálování obtížnosti.** Hra měla výběr levelů ve stylu Mega Mana, takže **boss musí být férový jako první i jako poslední** [(8:30)](https://www.youtube.com/watch?v=R_bX6FeEUFw&t=510s). Buď je moc těžký pro nováčky, nebo nudný pro zkušené. Škálování podle pořadí odmítá — *„fungovalo by to, ale jako herní mechanika mi to přijde špatně."*
- **Vlastní vkus.** Inspirace jsou Symphony of the Night, Hollow Knight a Mega Man X — u prvních dvou miluje **svět**, u třetího **mechaniku**. *„Zpětně mi přijde hrozně hloupé, že jsem stavěl svět jako Mega Man místo světa, který mě zajímá mnohem víc."*

**Jediný důvod proti** je poctivý a krátký [(10:48)](https://www.youtube.com/watch?v=R_bX6FeEUFw&t=648s): bude to **víc práce, dražší a delší**. Přijímá to s odůvodněním, které se za tři roky změnilo — původně dělal hru **jen pro sebe**, aby si dokázal, že to zvládne, *„a teď jsou tam lidi, co se na ni těší, a já je nechci zklamat."*

**A pak to nejlepší přiznání** [(11:35)](https://www.youtube.com/watch?v=R_bX6FeEUFw&t=695s): to rozhodnutí neudělal teď — **udělal ho před dvěma měsíci** a video natáčí až s odstupem. *„Jakmile jsem začal hru převádět, okamžitě to působilo jako správné rozhodnutí. Cítil jsem se úplně obrozený. Spousta problémů, o které jsem se měsíce mlátil hlavou, byla prostě pryč."* Že to říká zpětně, dělá z videa doklad, ne prohlášení.

> **Pozn.:** Tohle je učebnicový [pivot](../rejstrik.md#pivot-design) a stojí za srovnání se [scope kapitolou](../teorie/scope.md#pivot-kdyz-hra-nasla-jadro-jinde-nez-jsi-planoval), kde je popsaný obecně. Zajímavé je tu ale něco jiného: **diagnostickým příznakem nebyl výsledek, ale nechuť.** Autor uměl udělat „docela dobré" místnosti a přesto se práce děsil — a ten pocit byl **přesnější informací než ta kvalita**. To je nepohodlné zjištění, protože nechuť se špatně odlišuje od únavy a lenosti. Rozlišovací otázka, kterou z toho případu bereme: **je mi nepříjemná ta práce, nebo to, co z ní vzniká?** Když to druhé, není to o disciplíně. Za pozornost stojí i to, že rozhodnutí přišlo **zvenčí** — otázkou od někoho, kdo neznal historii projektu. Kdo je v projektu tři roky, nevidí předpoklady, na kterých stojí; [audit vlastního tónu](../zapisky/audit-vlastniho-tonu.md) i [GDD review](../zapisky/gdd-review.md) jsou o tomtéž.

**Souvislosti:** [Scope: pivot](../teorie/scope.md#pivot-kdyz-hra-nasla-jadro-jinde-nez-jsi-planoval) *(pivot jako obecný jev)* · [Nedělej malé hry, dělej systémy](../teorie/scope.md#nedelej-male-hry-delej-systemy) *(druhý pohled na tutéž otázku)* · [Mapa metroidvanie](pripadovka-level-a-mapa.md#mapa-metroidvanie-data-pohled-a-jedine-misto-pravdy) *(co z toho rozhodnutí vzniklo)* · [Tvůrčí zásek](../teorie/tvurci-zasek.md) · [Rejstřík: Pivot (design)](../rejstrik.md#pivot-design) · [Rejstřík: Scope creep](../rejstrik.md#scope-creep)

---

## Demoralizace, neviditelná práce a Git po roce

**Zdroj:** [Man, making a video game is hard | Devlog](https://www.youtube.com/watch?v=6v_gu8vbeQQ) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~15 min, devlog · + [Redesigning the Main Character of my Indie Game!](https://www.youtube.com/watch?v=HsWnv6rCiJ4) · týž kanál · ~25 min

**Shrnutí:** Tři věci, o kterých se v devlozích nemluví, protože se nedají ukázat na obrazovce. **Neviditelná práce**: přepis stavového automatu, který nikdo nevidí, ale bez kterého by další funkce trvaly dvakrát déle. **Demoralizace**: náhodné propady, o kterých si autor všímá, že je *„spousta devlogů, co sleduju, moc nezmiňuje"*. A **Git**, který si založil až po roce práce — s odůvodněním, které stojí za to slyšet.

### Rozpad myšlenky

**Neviditelná práce** [(0:51)](https://www.youtube.com/watch?v=6v_gu8vbeQQ&t=51s): den strávil přepisem stavového automatu, který řídí akce a animace postavy. Nová verze *„funguje mnohem líp"* a autor sám pojmenovává její problém jako komunikační: *„je to neviditelná práce — vůči vám i vůči zbytku týmu, protože nevidí, že se teď ty funkce dělají snadněji. Ale dělají, takže je to výhra."* Důkaz přišel hned: speciální útok, který předtím drhnul, šel po přepisu **výrazně snadněji**.

A jedna věta k načasování, která je proti běžné radě a má pravdu [(0:51)](https://www.youtube.com/watch?v=6v_gu8vbeQQ&t=51s): *„říkal jsem si, že je moc brzo v projektu na to, abych měl technický dluh."* To je použitelné kritérium — **dluh se nesplácí podle velikosti, ale podle fáze**: co brzdí v prvním roce, bude brzdit pětkrát víc ve třetím.

**Demoralizace** [(11:49)](https://www.youtube.com/watch?v=6v_gu8vbeQQ&t=709s) je nejcennější odstavec celého devlogu a stojí za doslovné převzetí: *„mám pocit, že spousta devlogů, co sleduju, o tomhle moc nemluví — delší projekty mají tendenci přinášet náhodné návaly pořádné demoralizace, kdy si říkáš ‚co to vlastně dělám'. Prostě to působí jako moc velký úkol, než aby se dala udělat opravdu celá hra."* Přidává i protilék, který u něj zabral: **den, kdy přišla nová grafika prostředí**, popisuje jako *„obrovské mentální vítězství a docela to člověka nabije"*. Vnější doklad postupu tedy funguje jinak než vlastní práce — a to je argument pro spolupráci a pro sdílení rozpracovaného.

**Git po roce** [(8:37)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=517s) je přiznání z jiného devlogu a je odzbrojující: *„fungoval jsem v riskantním režimu, kdy jedna chyba a přijdu o všechnu práci."* Zakládá repozitář, přidává i **reorganizaci projektu podle veřejného stylového průvodce** — a metodu volí zajímavou: **založí nový projekt a přenese do něj věci po jedné**, s pravidlem *„nevím-li, co to je, nebo nevidím-li pro to důvod, nechám to být"*. Import jako **filtr**, ne jako kopie.

**A jedna ukázka, proč se profiluje** [(3:57)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=237s): při načítání místností mu vznikaly velké záseky. Profiler ukázal drahé fyzikální volání, které nedávalo smysl — a příčina byla banální [(5:31)](https://www.youtube.com/watch?v=HsWnv6rCiJ4&t=331s): **všechny dlaždicové sady měl přepnuté na kinematický režim**, takže se při načtení každá dlaždice zpracovávala jako samostatné fyzikální těleso a jeden snímek trval **kolem 250 milisekund**. Oprava bylo jedno odškrtnutí. *„Připadám si jako pitomec, protože netuším, jak se to tam vzalo."*

> **Pozn.:** Ta trojice tvoří dohromady docela přesný obraz toho, co dlouhý projekt stojí **mimo kód**. Za pozornost stojí, že autorova nejúčinnější obrana proti demoralizaci není disciplína, ale **viditelný postup od někoho jiného** — což je mimochodem tentýž mechanismus, jaký [drží devlog jako formu](../zapisky/devlog-jako-mapa.md) a proč [sdílení rozpracovaného není marketing, ale nástroj](../teorie/zacatky-bez-zkusenosti.md#sdileni-prace-neni-marketing-je-to-nastroj-uceni). K tomu profilerovému nálezu doplníme obecnější pravidlo: **náhlá regrese výkonu má skoro vždycky konkrétní jednorázovou příčinu**, ne „hra je moc velká" — a profiler ji najde za deset minut, zatímco odhadování ji nenajde nikdy. Souvisí to s [tím, co skutečně stojí výkon](projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek).

**Souvislosti:** [Zkratka, kterou zaplatíš dvakrát](#zkratka-kterou-zaplatis-dvakrat) *(technický dluh, který nesplatil)* · [Devlog jako mapa](../zapisky/devlog-jako-mapa.md) · [Tvůrčí zásek](../teorie/tvurci-zasek.md) · [Git v Unrealu](../praxe/organizace-projektu.md#git-v-unrealu-verzovani-z-editoru-a-cesta-zpet-v-case) · [Rejstřík: Version control](../rejstrik.md#version-control) · [Rejstřík: Premature optimization](../rejstrik.md#premature-optimization)

---

## Playtester najde problém, ne řešení

**Zdroj:** [Game Dev Secrets: How to Playtest!](https://www.youtube.com/watch?v=TPEn3Ur__sQ) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~2 min

**Shrnutí:** Nejlepší dvouminutová ilustrace pravidla „testeři skvěle najdou problém a mizerně navrhnou řešení", jakou známe. Několik testerů autorovi nezávisle napsalo, že útoku dolů **chybí input buffer**. Jenže ten útok input buffer **má**. Pokušení je odepsat to jako „testeři nevědí, o čem mluví" — a byla by to chyba, protože **oni popsali řešení, ne problém**, a ten skutečný problém byl jinde a šel opravit.

### Rozpad myšlenky

**Situace** [(0:02)](https://www.youtube.com/watch?v=TPEn3Ur__sQ&t=2s): zpětná vazba od několika lidí zní rozumně, identifikuje konkrétní chybějící funkci — a je věcně nesprávná. Autorův posun je celý v jedné větě: *„jejich zpětná vazba je nesmírně cenná, jakmile si uvědomíme, že input buffer je řešení, ne problém."*

**Překlad zpátky na problém** [(0:48)](https://www.youtube.com/watch?v=TPEn3Ur__sQ&t=48s): co lidé zažili, bylo *„zmáčkl jsem tlačítko a nic se nestalo."* Když se to takhle formuluje, příčina se najde okamžitě — útok má **několik snímků nápřahu** a ten začíná už při stisku. Testeři mačkali **před** dopadem na bodce a **během nápřahu do nich narazili**, takže to působilo, jako by vstup zmizel.

**Oprava** je proto úplně jiná, než co navrhovali: **zkrátit nápřah** a **posunout hitbox na první snímek**. Autorovo přiznání je poctivé — *„nikdy by mě to nenapadlo, kdybych bral v úvahu jen ta jejich řešení místo problémů, které se snažili vyřešit."* A na závěr přidá i to, co navrhovali — „pro jistotu" okno bufferu trochu prodloužil.

**Použitelný postup**, který z toho plyne, se dá zapsat jako tři kroky: (1) **zaznamenej návrh doslova**, (2) **zeptej se, jaký zážitek k němu vedl**, (3) **hledej příčinu toho zážitku**, ne implementaci návrhu. Krok dvě je ten, který se přeskakuje — a bez něj se buď přijme špatné řešení, nebo se zahodí dobrá informace.

> **Pozn.:** Knihovna má tohle pravidlo popsané [z teoretické strany](../teorie/playtesting.md#moderovany-playtest-divej-se-co-delaji-ne-co-rikaji), a tenhle případ je jeho nejostřejší doklad, protože **návrh testerů byl technicky nesplnitelný — ta funkce už tam byla**. Bez překladu na problém by ta zpětná vazba vypadala jako šum. Zobecnění, které si bereme: **návrh řešení od hráče je stopa, ne zadání** — a čím konkrétnější ten návrh je, tím silnější stopu nese, protože prozrazuje, **co si hráč myslel, že se děje**. „Chybí input buffer" znamená „myslel jsem, že jsem zmáčkl včas", a to je informace, kterou by prosté „je to divné" nedalo.

**Souvislosti:** [Playtesting: dívej se, co dělají](../teorie/playtesting.md#moderovany-playtest-divej-se-co-delaji-ne-co-rikaji) · [Playtesting: nespolehlivý svědek](../teorie/playtesting.md#proc-testovat-nespolehlivy-svedek-vlastni-hry) · [Skok, který rozumí hráči](animace-a-pohyb.md#skok-ktery-rozumi-tomu-co-hrac-chtel) *(co input buffer dělá)* · [Rejstřík: Input buffering](../rejstrik.md#input-buffering) · [Rejstřík: Moderovaný playtest](../rejstrik.md#moderovany-playtest)

---

## Squeeze and release: hra bez stresu není hra

**Zdroj:** [Game Dev Secrets: Stress?](https://www.youtube.com/watch?v=1E5b-fOhfzc) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min

**Shrnutí:** Hry stresují hráče **schválně** — a rozdíl mezi dobrou a špatnou hrou není v množství stresu, ale v jeho **rytmu**. Princip se jmenuje **squeeze and release**: stiskni hráče výzvou, pak povol. A nejúčinnější formou povolení není odměna ani nový předmět, ale **checkpoint**.

### Rozpad myšlenky

**Obě krajnosti jsou špatně** [(0:02)](https://www.youtube.com/watch?v=1E5b-fOhfzc&t=2s), a autor to ukazuje doslova: hra bez překážek je *„úplně bezstresový zážitek — a proto není zábavná"*. Přidá překážky. *„Jejda, samý stres."* Tedy: **stres se přidává záměrně, protože je to nosič výzvy**, a hned nato je potřeba ho zase odebrat.

**Uvolnění má víc podob** — nový předmět, postup na vyšší úroveň — ale autor jednu vyzdvihuje: *„jednou z nejúčinnějších forem úlevy je checkpoint. Znáš ten pocit, když se po opravdu těžké plošinovkové pasáži dotkneš checkpointu? To je squeeze and release v akci."* Stojí za povšimnutí, že checkpoint **nedává nic** — jen ruší hrozbu ztráty. Uvolnění tedy nemusí být zisk; **stačí přestat hrozit**.

**A obě selhání** jsou symetrická [(0:49)](https://www.youtube.com/watch?v=1E5b-fOhfzc&t=49s): *„příliš stresu bez úlevy povede k frustraci a hráč skončí. Příliš úlevy bez dostatku stresu povede k nudě a hráč skončí."* Odtud autorova definice, která je odvážná a v jádru správná: **„jak dobře vyvážíš squeeze a release své hry, je v podstatě to, jak je zábavná."**

> **Pozn.:** Tenhle rám je velmi blízko [pětikrokovému cyklu napětí](../teorie/horor-design.md), jen zbavený hororové specifičnosti, a překrývá se i s [pacingem](../rejstrik.md#pacing) a s [flow](../rejstrik.md#flow) — příliš stresu je úzkost, příliš úlevy nuda, a mezi tím je pásmo, kde hra funguje. Co má autorova verze navíc, je **konkrétní páka**: checkpoint jako nejlevnější dostupný nástroj úlevy. Prakticky z toho plyne, že **rozmístění checkpointů není technické rozhodnutí, ale dramaturgické** — a že v pasáži, kde chceš držet napětí, se checkpoint vynechává schválně. Jde to i obrátit: postrádá-li tvoje hra rytmus, možná ti nechybí obsah, ale **místa, kde se dá vydechnout**.

**Souvislosti:** [Zábava a flow](../teorie/zabava.md) · [Horor design: cyklus napětí](../teorie/horor-design.md) · [Obtížnost a výzva](../teorie/obtiznost.md) · [Odznaky](pripadovka-systemy.md#odznaky-odmena-ktera-nezlehci-hru) *(odměna jako forma úlevy)* · [Rejstřík: Squeeze and release](../rejstrik.md#squeeze-and-release) · [Rejstřík: Pacing](../rejstrik.md#pacing) · [Rejstřík: Flow](../rejstrik.md#flow)

---

## Dvě věci o výkonu, které se pletou

**Zdroj:** [Game Dev Secrets: Increase your FPS by ten thousand percent!](https://www.youtube.com/watch?v=8_5Zrgek1p8) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~1 min · + [Game Dev Secrets: Async/Await/Ahelpme](https://www.youtube.com/watch?v=cuvW_dg9Y7c) · týž kanál · ~1 min

**Shrnutí:** Dvě minutová vysvětlení, která spolu souvisejí víc, než se zdá. **Time slicing**: drahý výpočet nemusí běžet každý snímek — stačí každý patnáctý, a z 10 FPS je zase 100. **Async není multithreading**: asynchronní kód běží **pořád na hlavním vlákně**, jen neblokuje. Obojí míří na tutéž věc: **hlavní vlákno je rozpočet a všechno v něm si bere svůj díl.**

### Rozpad myšlenky

**Time slicing** [(0:02)](https://www.youtube.com/watch?v=8_5Zrgek1p8&t=2s): autor dá šesti létajícím nepřátelům záměrně pomalý algoritmus hledání cesty a hra spadne na **sotva 10 FPS**. Pak ukáže, o co jde: *„během té pauzy sova spustila svůj pathfinding víc než stokrát. Nepotřebuje ho počítat tak často."* Řešení je pustit ho **každý patnáctý snímek**, tedy zhruba desetkrát za sekundu — což je *„pořád častěji, než je potřeba"* — a framerate je **zpátky nad 100**. Při dvou přepočtech za sekundu utáhne **třicet takových nepřátel**.

Pointa není v tom čísle, ale v otázce, kterou to otevírá: **jak často se ta věc musí opravdu přepočítat?** U hledání cesty je odpověď „párkrát za sekundu", protože cíl se za tři setiny sekundy nikam nepřesune. Táž otázka platí na dohled nepřátel, počítání vzdáleností, aktualizaci UI nebo kontrolu podmínek — a je to přesně ta úvaha, která u [Sealubbers snížila frekvenci brázdy za lodí z 60 na 20](projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek).

**Async není vlákno** [(0:02)](https://www.youtube.com/watch?v=cuvW_dg9Y7c&t=2s) odpovídá na otázku, kterou autor dostal po videu o multithreadingu, a odpověď je krátká: *„zní to, jako by to běželo na nějakém vlákně na pozadí — ale neběží. Je to jen neblokující."*

Rozdíl vysvětluje přes to, co se stane bez něj: skoro všechno ve hře běží na hlavním vlákně a je **blokující**, tedy *„dokud ten kód neskončí, hra nemůže přejít na další snímek"*. To je jedna z hlavních příčin propadů FPS. Asynchronní kód **běží tam pořád**, ale hra na něj **nečeká** — nedoběhl-li a hra chce další snímek, prostě ho udělá; systémy, které ten kód spustily, se **pozastaví bez blokování**, dokud jim nedá vědět, že skončil.

Autorovo uzavření je věcné: *„asynchronní kód se dá zkombinovat s vlákny na pozadí, ale sám o sobě multithreaded není."*

> **Pozn.:** Ty dvě věci dohromady dávají užitečný obraz: **hlavní vlákno je rozpočet 16,6 ms** a jsou jen tři způsoby, jak se do něj vejít — počítat **míň často** (time slicing), počítat **jinde** (vlákna), nebo **neblokovat** čekáním (async). Async je z nich nejsnáz zaměnitelný, protože zní jako paralelismus; **není** — je to způsob, jak nezdržovat čekáním na něco, co stejně trvá (načítání souboru, síťový dotaz). Kdo potřebuje snížit *výpočetní* zátěž, musí sáhnout po prvních dvou. Godotí strana téhle úvahy je popsaná u [_process versus timer](projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek), unrealí u [hlavního vlákna a multithreadingu](../praxe/optimalizace.md#druha-osa-optimalizace-co-blokuje-hlavni-vlakno).

**Souvislosti:** [Co skutečně stojí výkon](projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek) *(tatáž úvaha systematicky)* · [Optimalizace: co blokuje hlavní vlákno](../praxe/optimalizace.md#druha-osa-optimalizace-co-blokuje-hlavni-vlakno) · [Nepřítel, který obchází překážky](animace-a-pohyb.md#nepritel-ktery-obchazi-prekazky-navigace-ve-2d-je-rucni-prace) *(co se tu vlastně přepočítává)* · [Rejstřík: Time slicing](../rejstrik.md#time-slicing) · [Rejstřík: Multithreading](../rejstrik.md#multithreading) · [Rejstřík: Frame time](../rejstrik.md#frame-time)
