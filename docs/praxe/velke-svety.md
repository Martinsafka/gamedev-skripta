# Velké světy: sto tisíc aktérů a terabajty dat

Dvě přednášky a jeden devlog o tom, co se stane, když měřítko přeroste hlavu. První je **postmortem z rozdělané hry** — Subnautica 2, ručně stavěná mapa 3 × 1,5 km se sto tisíci aktéry a výhledem na půl milionu — a je vzácná tím, že mluví hlavně o věcech, které nevyšly. Druhá je z úplně jiného oboru (digitální dvojčata historických budov), ale technika, kterou popisuje, je přenositelná bez zbytku: **jak nacpat terabajty naskenovaných dat do enginu tak, aby se to dalo streamovat.** Třetí zdroj je devlog z procedurální hry v Unity a ukazuje, [co stojí dohled na kilometry](#dohled-na-kilometry-vetsi-chunky-v-dalce-stromy-se-stinem-a-souradnice-ktere-nepretecou) a co se stane s čísly 8 000 km od počátku.

Předchozí kapitoly bloku řeší, jak zlevnit to, co ve scéně je. Tahle o patro výš: **co do ní pustit a kdy**.

---

## Postavit, nebo si vzít: asymetrie rizika

**Zdroj:** [Lessons Learned from Building a Very Large Open World Game in UE5](https://www.youtube.com/watch?v=AalP65lrtpo) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~38 min, Unreal Fest Chicago 2026 (programátor, Unknown Worlds)

**Shrnutí:** Přednášející vypráví dva příběhy vedle sebe a **ani jeden z nich není úspěch v obvyklém smyslu**. V prvním postaví tým vlastní nástroj na rozmisťování surovin, dvakrát ho přepíše a nakonec vyhodí. Ve druhém sáhne po cizích pluginech — jeden se osvědčil dokonale, druhý po čase taky zahodí. Rozdíl mezi těmi dvěma konci je celá myšlenka. Háček: **nejde o to, co bylo lepší, ale o to, kolik stálo být na omylu.**

### Rozpad myšlenky

**Zadání, které znělo rozumně** [(4:47)](https://www.youtube.com/watch?v=AalP65lrtpo&t=287s): suroviny se mají rozmisťovat procedurálně, aby při každém hraní ležely jinde, aby se dala kdykoli doladit rovnováha, aby platila složitá pravidla „kde to dává smysl" a aby to fungovalo i pod převisy a v jeskyních — tedy ne shora dolů promítnuté na terén. PCG tehdy ještě nebylo připravené (mimo jiné proto, že jeho tehdejší nástroje předpokládaly volnou cestu z nebe na terén, což pod vodou v jeskyni neplatí).

**Verze první** vyplavila celou mapu raycasty: začni ve známém hratelném bodě a **flood fillem** projdi svět, označ povrchy, kam se dá spawnovat. Vypadalo to skvěle. Selhalo to pěti způsoby naráz:

| problém | proč bolí |
|---|---|
| pomalé a **nelineární v objemu** | čím větší kus mapy, tím hůř — a mapa rostla |
| vlastní nástroj | každá změna pravidel = změna nástroje = práce navíc |
| **manuální spouštění** | po každé úpravě terénu; u velkých oblastí až pár hodin, a nedá se čekat, že to bude umět každý, kdo dělá obsah |
| **černá skříňka** | výsledek jsi viděl až ve hře — takže do pečlivě naaranžované scény napadaly suroviny a vypadalo to hrozně |
| **hráč z toho nic neměl** | *„když si to zahraješ dvakrát a titan je o metr vlevo, nevšimneš si a je ti to jedno"* |

**Verze druhá** opravila skoro všechno: zahodila požadavek na runtime (takže se dalo péct do levelu a prohlížet v editoru), dostala vlastní nástroj v editoru místo pravidel zahrabaných v data assetech, **voxelizovala mapu** v metrovém rozlišení a pravidla pouštěla jen na voxelech, které je splňovaly, a běhala v noci na build stroji. Z hodin se stalo 15–20 vteřin.

**A pak stejně skončila v koši** [(10:16)](https://www.youtube.com/watch?v=AalP65lrtpo&t=616s): mapa rostla, z 20 vteřin bylo 20 a pak 30 minut. Noční běhy **zaváděly chyby** — *„nejhorší, co se může stát, je přijít ráno do práce a zjistit, že přes noc vznikly bugy, i když nikdo nepracoval."* A příprava stála hodiny ručního označování hratelného prostoru, takže **lidé nakonec suroviny stejně rozmisťovali ručně**. Autorovo shrnutí je bez sebelítosti: *„vezmeš měsíce práce a hodíš to do koše. Ale to je v pořádku."*

Čtyři lekce, které z toho vyvodí: **počítej s údržbou** · **mohli jsme zpomalit** a zeptat se, jestli ten požadavek vůbec platí · **preferuj enginové nástroje** (*„Epic má na nástroje obrovský tým; vy a my máme menší"*) · **zahozená práce je v pořádku**.

**Druhý příběh: pluginy** [(13:23)](https://www.youtube.com/watch?v=AalP65lrtpo&t=803s). Švy mezi meshi jsou u jejich barevně kontrastního stylu extrémně vidět; jeden z výtvarníků to shrnul slovy *„bitvu se švy nevyhraješ."* Vyzkoušeli RVT, decaly a sukně, zakrývání propy a listím, mesh distance fields — všechno buď nedostatečné, nebo s ruční prací navíc. Nakonec se **výtvarník zeptal na fóru**, někoho ten problém zaujal a napsal jim post-process shader; z toho vznikl plugin **Mesh Blend**. Byl levný (je to post-process) a hlavně: *„prostě jsme ho hodili do hry a všechno fungovalo. Nemuseli jsme měnit žádné assety."*

Druhý plugin dopadl jinak. Chtěli prefaby jako v předchozím enginu, našli **Prefabricator** pro UE4 (MIT licence), portovali ho na UE5, opravili pády, vylepšili a zveřejnili na GitHubu. A teď zvažují návrat k level instancím, protože *„noví lidé se ptají, proč to používáme, a po čase jsme to nedokázali obhájit."*

**A ta pointa** [(18:03)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1083s): *„u pluginů není žádná ztracená práce."* Kdyby zahodili Mesh Blend nebo Prefabricator, přišli by o pár dní. Vlastní nástroj je stál měsíce. A dodává, že **pluginy nejsou jen pro malé týmy**: *„někdo už udělal spoustu práce na jednom velmi konkrétním problému — a to je problém, do kterého ty nemusíš dát šest měsíců."*

> **Pozn.:** Nejcennější je tady **asymetrie**, ne doporučení. Obě cesty se mohou ukázat jako slepé; liší se cenou omylu — u pluginu dny, u vlastního systému měsíce plus doživotní údržba. Z toho plyne rozhodovací pravidlo, které přednáška neříká takhle přímo: **zkoušej nejdřív to, co se dá levně opustit.** Za pozornost stojí i to, jak to zapadá k [rozhodnutí zahodit vlastní level editor](../godot/pripadovka-level-a-mapa.md#level-editor-ktery-nakonec-nebyl-level-editor) z godotí případovky — tam po deseti hodinách, tady po měsících, a v obou případech byla chyba **v zadání, ne v provedení**. A jedna vlastní výhrada k „preferuj enginové nástroje": platí to tehdy, když ten nástroj existuje. Tenhle tým začínal v době, kdy PCG připravené nebylo — takže reálná volba nebyla „vlastní nástroj proti PCG", ale „vlastní nástroj proti počkat". A to je rozhodnutí, které se dělá s kalendářem v ruce, ne s principem.

**Souvislosti:** [Sto tisíc aktérů](#sto-tisic-akteru-co-unese-editor) · [Godot: level editor, který nakonec nebyl level editor](../godot/pripadovka-level-a-mapa.md#level-editor-ktery-nakonec-nebyl-level-editor) *(týž omyl v menším měřítku)* · [PCG: základy a nástroje](pcg-zaklady.md) · [Scope creep](../teorie/scope.md#scope-creep-napad-zaparkuj-nezabijej) · [Rejstřík: PCG](../rejstrik.md#pcg) · [PCG města: nástroj pro artisty](pcg-mesta.md#nastroj-pro-artisty-bake-tlacitkem-a-drobnosti-ktere-setri-hodiny) *(protipól: vlastní nástroj, který se vyplatil)*

---

## Sto tisíc aktérů: co unese editor

**Zdroj:** [Lessons Learned from Building a Very Large Open World Game in UE5](https://www.youtube.com/watch?v=AalP65lrtpo) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~38 min, Unreal Fest Chicago 2026

**Shrnutí:** U velkého světa se výkon za běhu řeší jako všude jinde — ale přibude druhá otázka, na kterou nikdo nemyslí: **jak se s tím pracuje v editoru.** Jak se otevře mapa se sto tisíci aktéry, co udělá outliner, jak najdeš věc a co když je potřeba změnit všechny naráz. Háček, který je celé myšlence jádrem: **ty problémy se ukázaly být malé — protože se na začátku sáhlo po dvou správných věcech.**

### Rozpad myšlenky

**Dvě rozhodnutí z nultého dne** [(19:36)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1176s): **World Partition** a **one file per actor**. Formulace je nezvykle silná: *„upřímně si neumím představit, jak bychom tu hru bez nich udělali."*

**Výkon editoru se ladí stejně jako výkon hry** [(19:36)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1176s) — a to je poznatek, který se snadno přehlédne: **Insights funguje v editoru stejně jako za běhu.** Konkrétní nález: kolem 50–100 tisíc aktérů začalo být pomalé **mazání**; trace ukázal kontroly referencí, ty se optimalizovaly a problém zmizel.

**Skript místo tažení myší** [(20:23)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1223s). Tým se rozhodl **posunout celou mapu o 6 metrů**, aby byla mělčí. Přednášející to komentuje bez příkras (*„docela hloupý nápad, ale udělali jsme to"*) a podstatné je jak: **editor widgety a skripty**, protože *„rozhodně bych nikomu neradil vybrat to celé v outlineru a tahat myší."* K tomu **world partition builder commandlety** na operace nad celou mapou, které nepotřebují celou mapu naráz: načti kus, udělej práci, ulož, uvolni, další.

**Automatizované testy, protože na ruční už není kapacita** [(21:56)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1316s). V raném přístupu vydávají pravidelné aktualizace a *„nejde po každé malé opravě znovu ručně otestovat celou hru — nebylo by to vůči QA fér."* Skladba: gauntlet smoke testy (připojit se, projít se), unit testy, funkční testy (utopí se postava, když jí dojde kyslík?) a — nejrychlejší na nasazení — **validátory blueprintů a data assetů**. Zdůvodnění validátorů je nejlepší věta celé pasáže: *„jako inženýr si říkáš ‚tohle nikdo neudělá, protože jsem to napsal do dokumentu a poprosil je'. No — validátor zařídí, že se to opravdu nestane."*

**Photo tools** [(24:16)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1456s), tedy jejich domácí automatizace: skript objede celou mapu, **dělá snímky** (aby bylo vidět, jestli se za pár dní vizuálně nezměnilo něco nečekaného) a **sbírá výkonové trace**. Hodnota je v rozlišení v čase: špička se dá zúžit na **jeden den**, dohledat v changelistech a srazit hned — *„místo aby ti v projektu ležela rok a pak ji hledáš."*

**A jedna přiznaná mezera**: data layers používají hlavně na velké přestavby oblastí a sami vědí, že by se daly využít mnohem víc, zvlášť za běhu.

> **Pozn.:** Tahle myšlenka je nejlepší doklad toho, že **volba infrastruktury na začátku rozhoduje o tom, jaké problémy vůbec budeš mít.** World Partition a OFPA nejsou optimalizace; jsou to rozhodnutí o tom, jestli půjde na mapě pracovat ve víc lidech a jestli půjde otevřít. Pak už se řeší jen drobnosti — což je přesně to, co se v přednášce stalo. Souvisí to s [nastaveními, která se dají udělat jen v CL1](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1). Nejpřenositelnější drobnost je ale ta věta o validátorech, protože pojmenovává obecný jev: **pravidlo, které existuje jen v dokumentu, není pravidlo — je to přání.** Cokoli, co má tým dodržovat a co se dá strojově zkontrolovat, patří do validátoru, ne do wiki; táž logika stojí za [validací assetů](profiling.md#nalez-neni-hotova-prace-predani) i za tím, proč se scalability nastavuje [za celý tým naráz](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1).

**Souvislosti:** [Postavit, nebo si vzít](#postavit-nebo-si-vzit-asymetrie-rizika) · [Automatizované měření](mereni-automaticky.md#benchmark-z-level-sequence-mereni-jako-soucast-prace) *(tatáž disciplína dotažená do nástroje)* · [Levely a streaming](levely-a-streaming.md#open-level-zamrzne-hru-streaming-ji-drzi-zivou) · [Optimalizace: data layers](optimalizace.md#proc-jsou-levely-pomale-od-instanci-po-data-layers) · [Rejstřík: World Partition](../rejstrik.md#world-partition) · [Rejstřík: One File Per Actor](../rejstrik.md#one-file-per-actor) · [Rejstřík: Data layer](../rejstrik.md#data-layer)

---

## Gameplay na meshi bez blueprintu

**Zdroj:** [Lessons Learned from Building a Very Large Open World Game in UE5](https://www.youtube.com/watch?v=AalP65lrtpo) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~38 min, Unreal Fest Chicago 2026

**Shrnutí:** Ve hře, kde se dá naskenovat skoro cokoli a dostat k tomu kus lore, potřebuje **skoro každý objekt trochu herní logiky**. Při sto tisících objektech to nemůžou být blueprinty a rozhodně nesmí nic tikat. Řešení není architektonicky vzrušující a právě proto stojí za zapamatování: **data se pověsí přímo na mesh.** Háček, který z toho dělá vzor: **ta data pak cestují s meshem všude, kde ho použiješ.**

### Rozpad myšlenky

**Zadání** [(25:50)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1550s): většina objektů jsou statické meshe, hodně z nich instancované, a leckterý korál je ve skutečnosti čtyři pět meshů poskládaných dohromady. Přesto potřebují nést: data pro skener, **typ povrchu** pro rozmisťování surovin (a to jemně — křemen se spawnuje **jen na perleťovém materiálu uvnitř** korálové kopule, ne na oranžovém venku), příznak *„do tohohle můžou velcí tvorové vrazit"* a gameplay tagy.

**Řešení: asset user data** — a k němu tým dopsal jen drobná rozšíření pro dotazování z blueprintů. Řetěz priorit, ve kterém se to hledá [(27:23)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1643s), je celý vzor:

1. **blueprintová komponenta** — je-li tam a má-li data, platí
2. **root komponenta**
3. **mesh v root komponentě**

Ten třetí stupeň je ta hodnota: *„můžeš přidat asset user data na meshe — což znamená, že ať se ten mesh použije kdekoli, ať v blueprintu nebo u nás v prefabu, ta data jdou s ním."*

**A závěr, který si tým odnesl z celého projektu** [(28:57)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1737s), je zároveň jeho hlavní pointa: *„boj proti workflow Unrealu nám málokdy vyšel. Všechny nástroje a systémy v enginu jsou navržené, aby spolu fungovaly, a když proti tomu jdeš, přicházíš o kus práce, kterou Epic dělá zadarmo."* Konkrétně: prefaby by příště vynechali a šli by cestou level instancí. Asset user data naopak *„bychom použili znovu — a příště ještě víc."*

> **Pozn.:** Tenhle vzor je cennější, než vypadá, protože řeší **rozpor, který se v každém velkém projektu objeví**: gameplay chce bohatá data, výkon chce hloupé objekty. Obvyklá odpověď — udělat z toho blueprint — je při vysokém počtu neúnosná; tahle odpověď říká **pověs data na asset, ne na instanci**, a tím se rozpor rozpadne. Godotí příbuzný je [resource jako popis toho, co ta věc je](../godot/resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je), s týmž rozdělením „data zvlášť od chování". Vlastní výhrada, kterou přednáška nezmiňuje: **data na meshi se hůř hledají.** Nikdo je neuvidí v blueprintu ani v outlineru, takže se k tomu musí přidat nástroj, který vypíše, co který mesh nese — jinak vznikne pravidlo, které zná jen ten, kdo ho zavedl. To je táž potřeba jako u [nástrojů pro sebe](../godot/projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate).

**Souvislosti:** [Animace ve velkém](#animace-ve-velkem-od-tiku-k-udalostem) · [Paměť a instancování: ISM](pamet-a-instance.md#ism-hism-a-merge-draw-cally-podle-geometrie) · [Instanced Actors](instanced-actors.md#swap-podle-vzdalenosti-setup-pres-data-registry) · [Godot: resource popisuje, co ta věc je](../godot/resources.md#data-ven-ze-skriptu-skript-ridi-chovani-resource-popisuje-co-ta-vec-je) · [Rejstřík: Asset User Data](../rejstrik.md#asset-user-data) · [Rejstřík: Gameplay Tags](../rejstrik.md#gameplay-tag)

---

## Animace ve velkém: od tiku k událostem

**Zdroj:** [Lessons Learned from Building a Very Large Open World Game in UE5](https://www.youtube.com/watch?v=AalP65lrtpo) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~38 min, Unreal Fest Chicago 2026

**Shrnutí:** Tři sta animovaných tvorů naráz, žádný z nich není humanoid, **žádní dva nesdílejí kostru** a půlka má fyzikálně simulované části. Kapitola je o dvou různých odpovědích: **postupně všechno zlevňovat se vzdáleností** a **přestat sbírat data každý snímek**. Háček, který je na tom nejpoučnější: to druhé bylo 1,8 ms práce, která **nedělala vůbec nic** — jen přenášela hodnoty z místa na místo.

### Rozpad myšlenky

**Žebřík zlevňování** [(30:32)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1832s) má u nich čtyři patra a je hezky konkrétní:

1. **Anim Budget Allocator** se spravovanými skeletal mesh komponentami — funguje z krabice a tým do něj jen dopsal vlastní výpočet priority (aby jejich obří „hero" tvorové **nikdy** nedostali osekané ticky).
2. **Zjednodušené behavior trees** na dálku.
3. Ještě dál: tvor se **promění ve statický mesh, který se pohybuje**.
4. A nejdál: **statický mesh, který stojí**.

K tomu vícevláknové animace, kde to jde, a **Niagara místo tvorů** — tři až čtyři sta drobných rybek jsou částice, ne skeletal meshe. *„Nemyslím, že by to šlo udělat jinak, a jsou tak malé, že na tom nezáleží."*

**Lítost, kterou stojí za to slyšet předem** [(32:07)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1927s): spravované skeletal meshe nezavedli od začátku a **zpětně se to dodělává těžko**. *„Přál bych si, abychom to použili na každém skeletal meshi hned na začátku."*

**A ten hlavní nález** [(32:53)](https://www.youtube.com/watch?v=AalP65lrtpo&t=1973s). Každá ryba měla blueprintovou komponentu, která **každý snímek** posbírala rychlost, rychlost otáčení, maximální rychlost a rozdíl oproti minulému snímku — aby to všechno bylo k dispozici v animačním blueprintu. Při dvou až třech stovkách tvorů to dělalo **1,8 ms na vývojářském stroji**, a jak přednášející podotýká: *„a nic z toho ve skutečnosti nedělá žádnou práci. Jenom to bere proměnné z míst, která ta data už mají."*

Postup oprav a jejich pořadí je poučný: **agregované ticky** (všechny do jednoho tickeru) pomohly, **přepis do C++** pomohl víc — ale pořád se plýtvalo. Skutečné řešení bylo **změnit směr toku**: místo aby si animace data tahala každý snímek, **vysílá je pohybová komponenta jako událost** ve chvíli, kdy se mění, a animační blueprint si odebírá jen to, co pro daný styl tvora potřebuje. Výhody: **nic netiká** a je to **přátelské k vláknům** — data jsou aktuální už v okamžiku, kdy se animace pouští, takže není co synchronizovat.

> **Pozn.:** Ten rozdíl mezi „zrychlit sbírání dat" a „přestat je sbírat" je nejpřenositelnější věc celé kapitoly a platí daleko za animacemi. **Agregace ticků a přepis do C++ jsou obě optimalizace téže špatné otázky**; teprve otočení směru (push místo pull) tu práci zruší. Je to táž změna, jakou v knihovně popisuje [interakce bez Event Ticku](interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku) a [událost místo příkazu](../godot/signaly.md#udalost-ne-prikaz-jmeno-signalu-prozradi-jestli-jsi-ho-pochopil) — jen aplikovaná na data místo na logiku. Praktický test, který se z toho dá odvodit: **najdi kód, který každý snímek jen kopíruje hodnoty, a zeptej se, kdo je vlastník.** Vlastník má vysílat; ostatní mají poslouchat. A vlastní výhrada k tomu žebříku: čtyři patra LODů zní elegantně, ale **každý přechod mezi nimi je místo, kde může být vidět skok** — takže cena té techniky není jen v implementaci, ale v ladění přechodů, o kterém přednáška nemluví.

**Souvislosti:** [Gameplay na meshi bez blueprintu](#gameplay-na-meshi-bez-blueprintu) · [Interakce bez Event Ticku](interakce-bez-event-ticku.md#overlap-trigger-misto-trasovani-v-ticku) · [Niagara: výkon částic](niagara-vykon.md#effect-type-jeden-asset-ktery-rozhoduje-o-vsem) · [Optimalizace: co blokuje hlavní vlákno](optimalizace.md#druha-osa-optimalizace-co-blokuje-hlavni-vlakno) · [Rejstřík: Anim Budget Allocator](../rejstrik.md#anim-budget-allocator) · [Rejstřík: Event Tick](../rejstrik.md#event-tick) · [Mass a ECS: proč objekty zpomalují](mass-ecs.md#proc-objekty-zpomaluji-pamet-kterou-nactes-a-zahodis) *(opačný závěr: v datech je tik levnější než události)* · [Bojovka pro desetiletý hardware](gpu-pruchod.md#bojovka-pro-desetilety-hardware-rozpocet-po-castech-a-co-se-v-nem-naslo) *(Anim Budget Allocator v lobby)*

---

## Odložit místo zlevnit: skořápka první, interiér na vyžádání

**Zdroj:** [From Scan to Stream: Open Pipelines for Large-Scale 3D in Unreal Engine](https://www.youtube.com/watch?v=5ehoHM-uzRQ) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~38 min, Unreal Fest Chicago 2026 (výzkumník, digitální dvojčata a památková dokumentace)

**Shrnutí:** Přednáška je z jiného oboru než zbytek knihovny — jde o naskenované budovy a digitální dvojčata, ne o hry — a bereme z ní **techniku, ne kontext**. Tým řeší, jak dostat do enginu stovky gigabajtů mračen bodů, fotogrammetrie a BIM modelů tak, aby se to streamovalo. Odpovědi jsou tři a všechny se dají použít i jinde. Háček, který je vlastně tou hlavní myšlenkou: **největší úspora nevznikla zlevněním práce, ale jejím odložením.**

### Rozpad myšlenky

**Omezení, které celou práci určilo** [(2:21)](https://www.youtube.com/watch?v=5ehoHM-uzRQ&t=141s), stojí za zmínku, protože je to typ zadání, se kterým se dá potkat i v hrách: **data nesmějí opustit budovu.** Jde o památkové objekty a vládní budovy, takže *„jakmile nástroj řekne ‚nahrajte data na naše servery', ta konverzace rychle končí."* A protože nástroje na terabajtové 3D jsou skoro všechny cloudové, museli si tři konverzní pipeline postavit sami — otevřeně a lokálně.

**První technika: dělení podle složitosti, ne podle mřížky** [(12:25)](https://www.youtube.com/watch?v=5ehoHM-uzRQ&t=745s). Existující nástroje krájejí model **pravidelnou mřížkou**, což ignoruje, co uvnitř je: *„ozdobná římsa v místnosti je výrazně složitější než stěna nebo podlaha vedle ní — nedává smysl zacházet s nimi stejně."* Jejich řešení je **adaptivní octree**: krabice se rekurzivně dělí na osminy a u každé dlaždice se kontroluje **práh 20 000 trojúhelníků**; pod prahem se dělení zastaví. Výsledek: dělení sleduje složitost a dlaždic je minimum.

**Druhá technika: textura na dlaždici, ne na modelu** [(13:57)](https://www.youtube.com/watch?v=5ehoHM-uzRQ&t=837s). Existující nástroje trpí **texturovou redundancí** — vezmou 16K texturu a **zapečou ji do každé dlaždice**, takže z megabajtové dlaždice je padesátimegabajtová, a to 256×. Náprava má tři kroky: každá dlaždice dostane vlastní **1024 × 1024** texturu přes smart UV project · protože se dlaždice fyzicky liší velikostí, **texel density se přizpůsobí sama** · a **LOD žebřík** drží to rozlišení, dokud se nedosáhne texelového rozpočtu celého modelu, pak klesá až na 32 pixelů. Pointa toho posledního: *„nikdy nevymýšlíme detail, který ve zdrojové textuře nebyl."*

**Třetí a nejpřenositelnější: skořápka první** [(24:55)](https://www.youtube.com/watch?v=5ehoHM-uzRQ&t=1495s). U budov rozdělí model na **plášť** a **interiér**. Do scény se nejdřív načte jen plášť — **260 000 trojúhelníků** — takže je to za pár vteřin. Interiér (**10,6 milionu** trojúhelníků) se dotahuje **až když uživatel budovu aktivuje** kliknutím nebo přiblížením. **Odloží se tím skoro 98 % trojúhelníků.**

K tomu dvě věci, které stojí za pozornost i mimo arch-viz:

- **Skryté meshe, které pořád vrhají stín**: sloučené buňky LOD1 se v aktivním stavu schovají, ale stín z nich zůstane — takže scéna má **134 stín vrhajících primitiv místo 26 000**. Zdůvodnění je poctivé: *„za běhu se nemůžeme spolehnout na Nanite a virtuální stíny, takže je většina našich procesů vázaná na CPU a každá milisekunda pomáhá."*
- **Výběr, který promuje jen to, na co klikneš**: uzel *select at screen position* rozbalí na jednotlivé instance jen buňky kolem místa kliknutí; zbytek zůstane sloučený.

Výsledek na jejich sestavě: jedna budova 120–130 FPS, celý kampus (47 modelů) se načte za ~5 minut a drží **60–70 FPS** — a to všechno **za běhu, bez pečení v editoru**.

> **Pozn.:** Za tímhle materiálem stojíme kvůli jedné větě, kterou se dá shrnout celý blok o výkonu: **odložená práce je levnější než zlevněná práce.** Optimalizace se obvykle ptá „jak tohle udělat rychleji"; tady se ptají „musí se to dít teď?" — a odpověď 98 % odložených trojúhelníků žádná optimalizace rasterizace nedožene. Je to tentýž princip jako [pre-cull u částic](niagara-vykon.md#effect-type-jeden-asset-ktery-rozhoduje-o-vsem) a jako [hydratace instance actorů](persistence-a-hydratace.md#hydratace-instance-actory-a-mass) — jen v jiném měřítku. Za pozornost stojí i to **adaptivní dělení**: pravidelná mřížka je pohodlná pro programátora a lhostejná k obsahu, adaptivní octree je opačně — a je to táž volba jako [topologie proti cluster cullingu](nanite-do-hloubky.md#overdraw-se-autoruje-ne-opravuje). Výhrada k přenositelnosti: tenhle tým **nemůže použít Nanite ani virtuální stíny**, protože všechno vzniká za běhu z externích dat, takže část jejich vynalézavosti je náhrada za funkce, které v běžné herní pipeline dostaneš zadarmo. Neber to tedy jako doporučení stavět HLOD ručně — ale jako doklad, kolik se dá získat **strukturou načítání**.

**Souvislosti:** [Sto tisíc aktérů](#sto-tisic-akteru-co-unese-editor) · [Persistence a hydratace](persistence-a-hydratace.md#hydratace-instance-actory-a-mass) · [Nanite do hloubky: cluster culling](nanite-do-hloubky.md#overdraw-se-autoruje-ne-opravuje) · [Levely a streaming](levely-a-streaming.md#open-level-zamrzne-hru-streaming-ji-drzi-zivou) · [Rejstřík: Octree](../rejstrik.md#octree) · [Rejstřík: HLOD](../rejstrik.md#hlod) · [Rejstřík: Point cloud](../rejstrik.md#point-cloud)

---

## Dohled na kilometry: větší chunky v dálce, stromy se stínem a souřadnice, které nepřetečou

**Zdroj:** [Supercharging my procedural mountain forest](https://www.youtube.com/watch?v=ACjlgxRp69c) · [runevision](https://www.youtube.com/channel/UCj4OTbKSiCxjGoQhalUvrdg) · ~18 min, devlog (Unity, vlastní framework)

**Shrnutí:** Devlog z procedurální horské hry v Unity, ne v Unrealu. Autor zvětšuje dohled z necelého kilometru na zhruba pět a postupně platí tři účty, které velký dohled vystaví: čas generování, vykreslení vzdálených stromů a přesnost čísel daleko od počátku. Odpovědi jsou LOD vrstvy generování, kde má každá vrstva dvakrát větší chunky při stejném rozlišení, dále octahedral impostory, které vrhají i přijímají stín, a fixed point souřadnice s origin shiftingem. Háček: svět o rozsahu ±8 000 km autor otestoval, a přesto říká, že na velikosti v praxi moc nezáleží. Procedurální svět je jen tak dobrý jako jeho rozmanitost.

### Rozpad myšlenky

**Rychlost napřed.** Hra má pracovní název The Big Forest a svět se generuje na pozadí v několika vláknech [(0:52)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=52s) [(1:39)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=99s). Vizualizace úloh ukázala, že nejvíc času padá na čtení dat deformace cest zpátky z compute shaderu. Autor tu práci přesunul na CPU a přepsal ji pro Unity Burst compiler: statické funkce, žádné třídy, NativeArray místo polí. NativeArray je jen jednorozměrné, takže si na 2D napsal vlastní obaly. Celé generování se zrychlilo trojnásobně a stíhá i postavu, která se řítí krajinou [(2:26)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=146s).

**Větší chunky v dálce.** Přehnaná aerial perspective, tedy modrý nádech do dálky, dávala dojem měřítka, ale vidět bylo méně než kilometr [(3:02)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=182s). Všechny chunky terénu měly stejnou velikost. Řešením jsou čtyři LOD kopie generační vrstvy. Všechny drží kolem hráče mřížku 5 × 5 chunků, jen každá další s chunky dvojnásobné velikosti. Rozlišení chunku zůstává stejné, takže vzdálený velký chunk stojí při generování i vykreslení tolik co blízký malý. Velký chunk se skryje, jakmile jeho plochu celou pokryjí menší [(3:49)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=229s). V dálce se šetří dvakrát: stromů je tam méně kvůli snímkové frekvenci a cesty se tam nestaví kvůli času generování. Za tyhle drobné ústupky dostal autor trojnásobný dohled, zhruba 2,5 km, se stejným počtem chunků i stejným časem generování. Mezi chunky různých velikostí ale občas prosvítaly drobné praskliny. Unity na to hotové řešení nemá, a tak se chunky trochu překrývají a mají terrain skirts [(4:37)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=277s).

**Vrstvy, které o sobě vědí.** Hra stojí na autorově open source frameworku LayerProcGen [(4:37)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=277s). Framework neříká, jakým algoritmem generovat, jen jak generování rozdělit: do vrstev, kde každá smí číst vrstvy pod sebou. Cesta tak může vzniknout pathfindingem nad daty nižších vrstev a hranice chunků jí nevadí. Framework autor vydal v květnu 2024 a pečlivě zdokumentoval hlavně jeho koncepty, ne jen implementaci [(5:27)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=327s).

**Stromy, které nejsou plochá skvrna.** Hry vzdálené stromy obvykle nahrazují obrázky [(6:59)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=419s). Vestavěné řešení Unity je rychlé, ale vzdálené stromy nevrhají ani nepřijímají stíny. Les se tak v dálce slije do ploché barevné masy a krajina ztratí tvar. Autor přešel na octahedral impostory: strom je předem vyrenderovaný z mnoha úhlů a shader z těch obrázků skládá pohled, který se chová překvapivě jako geometrie. Rychlost dodal GPU instancing [(7:49)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=469s). V autorově případě ale nástroj třetí strany GPU Instancer trpěl chybami vykreslování a zadrháváním. Použitelný byl až v létě 2025, ve verzi Pro a s opravami chyb, které autor nahlásil. Matné nové stromy pak oživily čtyři úpravy shaderu [(8:38)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=518s): pryč s výchozím leskem Unity, wrap-around lighting, které stíny prosvětlí, vítr, při kterém se větve houpou bez natahování, a translucency, díky které listím prosvítá světlo. Ta je podle autora pro vzhled stromů zásadní hlavně v protisvětle. A když někdo napsal, že stromy vypadají jako zastřižené plotostřihem, zdrsnil jim normály.

**Hory a eroze.** Autorův erozní filtr je open source shader a další lidé ho přenesli do Unity, Unrealu, Godotu, Blenderu, Houdini a jinam [(9:36)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=576s). Do hry chtěl dostat obojí, velkolepé hory i menší útesy a kopce, za kterými láká podívat se, co je dál [(10:26)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=626s). Vyšší hory si vyžádaly další LOD úroveň a dohled se zdvojnásobil na zhruba 5 km. S erozí ale výpočet výšek na CPU zpomalil. Pomohl nezdokumentovaný trik s knihovnou Unity Mathematics, díky kterému jde jeden kód psát pro C# i pro shader. Výšku pak umí spočítat obě strany: CPU jen v bodech, které rané vrstvy potřebují pro plánování cest, GPU pro celý výsledný terén. Nad krajinou pak jde letět rychlostí 300 km/h [(11:14)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=674s).

**Čísla daleko od počátku.** Pozice ve hrách bývají 32bitové floaty s omezeným počtem číslic [(12:03)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=723s). Čím větší číslo, tím menší přesnost, takže daleko od počátku se věci začnou rozpadat. Generování proto počítá ve fixed point. 256 hodnot na metr dává přesnost na pár milimetrů v jakékoli vzdálenosti a rozsah zhruba ±8 milionů metrů, tedy rozsah 32bitového celého čísla dělený 256. To byla teorie. V květnu autor postavil hráče 8 000 km od počátku a vylezly chyby [(12:53)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=773s). Byly záludné. Kód například hledal střed mezi dvěma souřadnicemi jako jejich průměr, jenže součet přetekl rozsah dřív než kterákoli ze souřadnic a dělení dvěma přišlo až po přetečení. Oprava je spočítat průměr jinak, bez sčítání. Po sérii oprav se svět v 8 000 km generoval bez chyb. Vykreslovat se ale musí ve floatech, a tam byly stíny i UV mapování rozbité [(13:42)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=822s). Lékem je floating origin ve variantě origin shifting. Souřadnice světa pro generování jsou oddělené od souřadnic scény v enginu. Když se hráč vzdálí od počátku scény, přesune se zpátky i s celým světem. Hra pak funguje v ±8 000 km stejně dobře jako uprostřed, a čtverec o hraně 16 000 km je zhruba polovina povrchu Země [(14:32)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=872s). Autor hned dodává, že na tom v praxi moc nezáleží. Procedurální svět je jen tak dobrý jako jeho rozmanitost, ne jako jeho velikost. Velikost ho jen přestala omezovat.

**Atmosféra.** Modrý nádech v dálce působil po rozšíření dohledu trochu nevýrazně [(14:32)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=872s). Vodítko přinesla dovolená v Japonsku. Hory tam s rostoucí vzdáleností nejdřív modraly a pak bledly do bíla, přesně jako obloha u obzoru. Obojí má stejnou příčinu, tloušťku vzduchu mezi okem a cílem. Mlha ve hře proto teď ve velké dálce bledne [(15:20)](https://www.youtube.com/watch?v=ACjlgxRp69c&t=920s). Fyzikálně přesný atmospheric scattering to není, autorovi ale dvoubarevný gradient zatím stačí a krajině přidal hloubku.

> **Pozn.:** Zdroj je z Unity a vlastního frameworku, takže čti principy, ne nastavení. V UE mají své protějšky. Chunky s rostoucí velikostí odpovídají myšlence [HLOD](../rejstrik.md#hlod) a hierarchického streamování a impostory rozebírá [Proč malé trojúhelníky ničí GPU](rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu). Přesnost řeší UE5 přes [Large World Coordinates](../rejstrik.md#large-world-coordinates), tedy pozice v double precision. Ani v UE ale nepočítá v doublech úplně všechno a limit přesnosti daleko od počátku zmiňuje i [Mesh Terrain](mesh-terrain.md#proc-mesh-terrain-existuje-limity-landscape). Past s přetečením součtu číhá v každém vlastním kódu, který pracuje s celými čísly. Vzdálené chunky bez cest jsou malá verze [odložené práce](#odlozit-misto-zlevnit-skorapka-prvni-interier-na-vyzadani). Toto čtení je naše.

**Souvislosti:** [Sto tisíc aktérů](#sto-tisic-akteru-co-unese-editor) · [PCG vegetace: les pro otevřený svět](pcg-vegetace.md#les-pro-otevreny-svet-co-se-nacte-s-levelem-a-co-roste-kolem-hrace) *(totéž v UE: hustota jen kolem hráče)* · [Rejstřík: Impostor](../rejstrik.md#impostor) · [Rejstřík: Origin shifting](../rejstrik.md#origin-shifting) · [Rejstřík: Fixed point](../rejstrik.md#fixed-point) · [Rejstřík: Aerial perspective](../rejstrik.md#aerial-perspective) · [Rejstřík: Skirt](../rejstrik.md#skirt)
