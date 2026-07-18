# GDD: dokument jako způsob myšlení

Game design document má pověst byrokratické přítěže — a zaslouží si ji jen tehdy, když se píše jako stostránková bible, kterou nikdo neotevře. Dvě videa Indie Game Clinic ukazují opačný přístup z obou konců: minimalistická metoda „skica všech oblastí hry na pár stránek" a exkurze po skutečných dokumentech klasik (Diablo, GTA, Sam & Max, Star Fox 2, Monaco), ze kterých je vidět, co profesionální dokumenty spojuje — a jak moc se finální hry od svých dokumentů liší. Společná teze: **dokument není smlouva o hře, je to nástroj přemýšlení o ní.**

---

## GDD minimalisticky: skica všech oblastí, ne bible jedné

**Zdroj:** [Game Design Documents — a Minimalist Approach](https://www.youtube.com/watch?v=uBxYGFRi-S4) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~37 min, metoda s živou ukázkou

**Shrnutí:** Jednotný správný formát GDD neexistuje. Minimalistický princip: **hrubě popsat každou oblast hry, kterou dokážeš vyjmenovat — a zkontrolovat, že dávají smysl dohromady.** Málo slov, hodně diagramů a obrázků, žádné detaily obsahu. Účel dokumentu není hru vyprojektovat, ale co nejrychleji tě dovést k prototypu, který umíš popsat a otestovat.

### Rozpad myšlenky

Proti čemu metoda stojí [(0:00)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=0s): každý má oblíbenou oblast. Story člověk u sekce „příběh" upadne do transu, napíše Pána prstenů — a probudí se s milionem slov narativní bible, nulou myšlenek o level designu, monetizaci a art stylu. Velké dokumenty mají i druhou vadu: nikdo je nečte — programátoři a artisti chtějí „dělat barvičky a programovat exploze", ne louskat elaborát [(0:50)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=50s). Respekt ke čtenáři (nebo k budoucímu sobě) znamená dokument ne větší, než musí být.

Čemu dokument slouží [(1:40)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=100s): říct „tohle chceme vyrobit — **je to dobrý nápad?**" Do designu nevstupuj s předpokladem, že odpověď zní ano: design je iterace a spolutvorba s publikem [(2:31)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=151s). Proto žádné hluboké detaily předem: 90 % předčasného psaní se stane irelevantním, až se hra změní nebo zařízne. Konkrétní stopka: **nevyráběj víc než level, víc než půlhodinu obsahu, dokud jádro netestovalo 10–20 lidí** [(14:27)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=867s) — místo stohů popisů nech v dokumentu viditelnou díru („tento seznam = MVP, další typy později") a vrať se k ní, až testy řeknou, že má smysl ji plnit [(13:16)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=796s).

Největší benefit je psychologický [(31:58)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1918s): systematický průchod všemi oblastmi **tě donutí myslet na sekce, před kterými utíkáš** — a některá z nich je přesně pro tebe. Teprve s vyplněnou skicou jde udělat krok zpět a ptát se, jestli části ladí („potenciálně urážlivá hra… mířená na pětileté — hm") [(32:44)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1964s). Je to **skica, ne obraz**: části volně rozvrhnout, hýbat s nimi, teprve pak malovat.

A hranice metody [(34:21)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=2061s): pod ní existuje ještě **one-pager** (stránka, jeden obrázek, co chci vyrobit a jak vypadá úspěch); nad ní rostou specializované dokumenty — narativní bible, balancovací spreadsheet, art bible — až se z „GDD" stane složka dokumentů [(37:04)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=2224s). Vždycky je to ale **pracovní dokument otevřený změnám**, ne odevzdaný úkol.

> **Pozn.:** V závěru videa autor propaguje vlastní placenou službu review GDD na Fiverru [(35:11)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=2111s) — obsahu to neubírá, jen vězte, že závěrečná vstřícnost má i obchodní motiv. — Metoda je rozvinutí „nástěnky místo eseje" ze [startu projektu](jak-zacit.md#design-dokument-ktery-skutecne-otevres-nastenka-misto-eseje): stejný instinkt (dokument, který skutečně otevřeš), tady dotažený do úplné šablony.

**Souvislosti:** [Start projektu: design dokument](jak-zacit.md#design-dokument-ktery-skutecne-otevres-nastenka-misto-eseje) · [Prototypování: tři brány](prototypovani.md#tri-brany-gameplay-prototyp-vertical-slice-produkce) · [Zápisky: GDD review](../zapisky/gdd-review.md) *(vlastní GDD proti téhle laťce)* · [Rejstřík: GDD](../rejstrik.md#game-design-document) · [Rejstřík: one-pager](../rejstrik.md#one-pager)

---

## Od širokého ke konkrétnímu: pilíře, publikum, jádro

**Zdroj:** [Game Design Documents — a Minimalist Approach](https://www.youtube.com/watch?v=uBxYGFRi-S4) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · struktura ukázkového dokumentu

**Shrnutí:** Univerzální pravidlo vší dokumentace: **začni nejobecnějším a postupuj ke konkrétnímu** — nikdy neotvírej dokument popisem jedné postavy nebo levelu. Ukázkový dokument fiktivní hry Prophecy (top-down multiplayer: každý hráč je prorok s rostoucím hejnem followerů, god game × battle royale) to předvádí sekci po sekci: popis, pilíře, publikum, core gameplay, balanc, art, svět, byznys.

### Rozpad myšlenky

**Nejširší popis** [(3:21)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=201s): pár vět bez superlativů — žádné „bude to nejúžasnější…", jen co hra je a čím je jiná. Reference na existující hry se nebát („god game jako Populous × zjednodušené Agar.io") a přidat jejich obrázky — „X plus Y" pitch je cheesy, ale funguje [(4:08)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=248s).

**Design pillars s vysvětlením v dokumentu** [(5:48)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=348s): pilíře nejsou žánr ani art style — míří na zážitek publika. Trik navíc: přímo do dokumentu napsat, *proč* tam pilíře jsou, aby je programátor neodmávl jako designérskou mystiku [(6:38)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=398s). Proti vágnímu „fun" pomůže framework **14 forms of fun**: vyber tři (Prophecy: power, competition, problem solving) a tabulkou ukaž, jak se navzájem sytí — výběr upgradů (problem solving) živí rostoucí hejno (power) a to pohání soupeření (competition) [(7:28)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=448s). Cvičení nutí promyslet souhru systémů dřív, než existují.

**Publikum a trh brzy** [(9:59)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=599s): marketing není reklama — je to všechno chování na trhu: co prodáváš, komu, kde. Malé hry často umírají na nesoulad hry a platformy (casual mobilní hra na Steamu) [(10:45)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=645s). A **nikdy nedesignuj pro všechny** [(11:34)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=694s): nevíš-li, pro koho hra je, urči aspoň, **pro koho není** — Prophecy si od začátku přiznává, že neuctivý humor o náboženství a groteskní násilí část lidí vyloučí, a z toho plyne tón celé hry [(12:30)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=750s).

**Core gameplay = největší sekce** [(12:30)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=750s): co hráč fyzicky dělá (pohyb prorokem, rozkazy hejnu), typy followerů s chováním — a u featur **zdůvodnění místo pouhého popisu** [(15:15)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=915s): tech tree „jako divine inspiration tree v Cult of the Lamb" je v dokumentu obhájený gameplayem (strategické volby, jiný průběh každé hry) *i* tématem (větve stromu = vývoj náboženské doktríny). Když se mechanika jmenuje po světě hry, vysvětluje se sama [(16:06)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=966s).

**Limitování projektu přímo v dokumentu** [(24:09)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1449s): finální hra má mít procedurální svět — ale prototyp a slice pojedou na **jednom fixním světě s layoutem skutečné Země** („mapu už máme"), jen s domalovaným pevninským mostem, aby šla přejít [(24:55)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1495s). U procedurálních her je to zásadní past: měsíce ladění generátorů dřív, než víš, jestli je uvnitř hra. Stejně střídmě: balanc jako přístup (catch-up mechaniky proti snowballu), ne Excel [(18:31)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1111s); art jen tam, kde ovlivňuje gameplay (followeri malí a mravenčí — konvence god game; týmové barvy, které musí popnout — proto tmavý neutrální svět) [(21:46)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1306s); narativ „not doing one, mate" [(27:13)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1633s); a byznys model aspoň načrtnutý (demo zdarma → Kickstarter → premium pod 10 $), protože financování zpětně tvaruje design — odměny pro backery musí jít do hry snadno přidat [(28:51)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1731s).

> **Pozn.:** Pilíře + 14 forms of fun je stejná dvojice nástrojů jako v [taxonomii zábavy](zabava.md#zabava-neni-jedna-vec-taxonomie-a-pilire) a v [obraně proti scope creepu](scope.md#scope-creep-napad-zaparkuj-nezabijej) — GDD je místo, kde se pilíře poprvé zapisují, backlog místo, kde se podle nich rozhoduje. A „mapa Země místo generátoru" je čistokrevný [design by constraint](scope.md#design-by-constraint-krabice-napred-napad-dovnitr).

**Souvislosti:** [Zábava: taxonomie a pilíře](zabava.md#zabava-neni-jedna-vec-taxonomie-a-pilire) · [Ludotematický soulad](ludonarativni-soulad.md) *(mechanika pojmenovaná světem hry)* · [Co prodává](co-prodava.md) · [Rejstřík: design pillars](../rejstrik.md#design-pillars) · [Rejstřík: MVP](../rejstrik.md#mvp)

---

## Will, should, could: jazyk závazku a dokument, který chce někdo číst

**Zdroj:** [Game Design Documents — a Minimalist Approach](https://www.youtube.com/watch?v=uBxYGFRi-S4) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · řemeslo psaní ·
[What Do "Professional" Game Design Documents Look Like?](https://www.youtube.com/watch?v=fk-rQlrNYZ8) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · důkazy z klasik

**Shrnutí:** GDD je technický dokument a technické psaní má řemeslné minimum: slova **will / should / could** nesou tři různé úrovně slibu, bullet points chtějí uvozující větu, a dokument, který má někdo číst, musí střídat média — text, tabulku, diagram, obrázek. Nejlepší dokumenty jdou dál: nesou grafický jazyk, nebo dokonce hlas budoucí hry.

### Rozpad myšlenky

**Hierarchie závazku** [(19:21)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1161s): „there **should** be elements which prevent players getting too far ahead" je slabší slib než *will* — a „one example **could** be culling areas of the map" je ještě slabší: jedno možné řešení, ne rozhodnutí [(20:13)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1213s). Zní to banálně, ale přesně tahle slova oddělují jádro od stretch goals — dokument Sam & Max u mini-her píše „interfaces will surface from time to time… simple point and click variety": jazyk, který říká „nedrž mě za slovo" [(20:12)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1212s). Kdo úrovně slibu nerozlišuje, tomu za půl roku někdo vyčte „slíbils" [(21:01)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1261s). K tomu kázeň bulletů [(13:16)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=796s): seznam jen s uvozující větou, proč existuje, a položky jedné kategorie.

**Střídání médií** [(16:54)](https://www.youtube.com/watch?v=uBxYGFRi-S4&t=1014s): GDD je učební materiál — čtou ho lidi s různými hlavami (textoví, vizuální, tabulkoví). Zeď textu je pro půlku týmu totéž co japonský dokument pro neznalé japonštiny [(26:45)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1605s) — a dokument Star Foxu 2 dokazuje opak: flow diagramy gameplaye a meta-progrese jsou srozumitelné, i když neumíš přečíst ani znak [(21:16)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1276s). Lekce ze skic: **neumíš-li nápad z hlavy převést do pár čar, nejspíš není domyšlený** [(22:50)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1370s). A důležitý kontraintuitivní detail: i Nintendo kreslí *schválně* skicovitě — vyleštěná prezentace rozdělané věci působí jako finál k odkývnutí, skica zve ke změnám [(24:23)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1463s).

**Grafický jazyk hry v dokumentu**: pitch Diabla (1994) je prošpikovaný royalty-free středověkými rytinami a nadpisy v náhrobkovém (ale čitelném) fontu — dokument začíná budovat vizuální branding hry [(4:17)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=257s). Sam & Max jdou nejdál: titulka „an adventure game based on the collected works of Drew Barrymore" a postavy lámou čtvrtou zeď přímo v textu [(15:29)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=929s) — dokument popisuje komediální hru *jejím vlastním tónem*. Normálně to nedělej; tady je to chytré, protože **komedie je pilíř hry a dokument ji dokazuje na sobě** [(16:18)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=978s). Trik s postavami vysvětlujícími svět v dokumentu je použitelný i u vážných her [(17:06)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1026s).

A poslední řemeslná poznámka: dokument nemusí mít jednoho autora [(27:31)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1651s) — sdílené psaní (Google Docs) znamená, že artista přispěje skicami a každý vlastní svou oblast; dokument je pak **„míč na tenis"**: pomalá asynchronní konverzace týmu přes časová pásma [(40:43)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=2443s).

> **Pozn.:** Uprostřed druhého videa je krátký merch blok (hrnek „playtester tears") [(19:26)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1166s) — kanálový žert, ne sponzoring.

**Souvislosti:** [Devlogy: scénář psaný nahlas](devlogy.md) *(stejné řemeslo, jiné médium)* · [Steam stránka](steam-stranka.md) *(capsule a branding — kam grafický jazyk dorůstá)* · [Rejstřík: GDD](../rejstrik.md#game-design-document) · [Rejstřík: art bible](../rejstrik.md#art-bible)

---

## Race'n'Chase a spol.: dokument není smlouva

**Zdroj:** [What Do "Professional" Game Design Documents Look Like?](https://www.youtube.com/watch?v=fk-rQlrNYZ8) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~41 min, pět historických dokumentů

**Shrnutí:** Nejcennější na dokumentech klasik je, kolik toho ve finálních hrách *není*. Diablo bylo v pitchi tahové a mělo rasy postav. GTA se jmenovalo Race'n'Chase a hrál jsi policajta. Monaco v dokumentu mělo character creation. Dokument je záznam myšlení v čase — a myšlení se vyvíjí; hodnota dokumentu není v tom, že platí, ale v tom, že ukazuje, *o čem* se přemýšlelo.

### Rozpad myšlenky

**Diablo (1994)** [(1:10)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=70s): popsaná hra sedí s Diablem dodnes — až na to, že „the entire game operates on a turn-based system" [(1:57)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=117s), a na D&D rasy a classy, ze kterých zbyly tři archetypy [(5:04)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=304s). Za pozornost stojí, jak dokument deklaruje přístup obecnými větami, které zní samozřejmě („hlubší patra = těžší nepřátelé"), ale nahoře v dokumentu plní roli kursu [(4:17)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=257s) — a „user story" pasáž krok za krokem popisující, co hráč vidí a dělá po vstupu do chrámu [(7:27)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=447s).

**GTA = Race'n'Chase** [(8:47)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=527s): v původním dokumentu **řídíš policejní auto** a honíš prchající vůz [(9:16)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=556s). Hrát policii nebyla zábava — tak ji vyškrtli a nechali jen zločin [(10:04)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=604s). Z toho plyne nejlepší definice scope v celé kapitole: **scope není velikost, scope je dalekohled** [(10:50)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=650s) — zazoomování věci odřízne (to vidí každý) a zároveň *zaostří to, co zbylo* (to se přehlíží). Druhá zvláštnost: půlka dokumentu jsou technické specifikace ukládání sprajtů — protože hra vyrostla z tech dema „jak vůbec uložit a streamovat velké město" [(11:36)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=696s). Všechen „GTA flavor" — svět, hlášky, mise — přišel o roky později [(12:24)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=744s). Lekce pro každého, kdo na něčem sedí dlouho: **unique selling point hry nemusí existovat od začátku; klidně se do projektu nastěhuje po letech** [(13:10)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=790s).

**Sam & Max a pořadí sekcí** [(17:53)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1073s): narativní hra frontloaduje příběh, postavy a lokace; puzzly až dál. Univerzální pravidlo broad→specific se ohýbá podle žánru — co je pro hru primární, jde nahoru.

**Monaco (2003 → 2013)** [(28:18)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1698s): dokument deset let před vydáním, a přesto pozoruhodně podobný finálu — včetně vizuálu barevných bloků v černém rámu. V dokumentu je i menu flow diagram (splash → title → profil → černý trh…): „není to zábava, ale máš-li menu, udělej ho" [(35:18)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=2118s). A z projektové historie: Andy Schatz design vymyslel jako zaměstnanec studia na odsouzeném projektu — a **smluvně si zajistil vlastnictví konceptů**, kdyby je firma nechtěla [(29:05)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1745s). Video z toho vyvozuje nepohodlnou tezi: úspěšní „bedroom" indie vývojáři jsou vzácnost — většina slavných indie her vzešla od lidí, kteří **napřed dělali hry jako zaměstnání** a teprve pak šli na volnou nohu; jako v každém řemesle: napřed učedník [(30:37)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1837s).

Syntéza obou videí [(36:04)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=2164s): **psaní je myšlení** — jako u diplomky: píšeš, zjistíš, že si myslíš něco jiného, přepíšeš. Dokument je rozhovor se sebou (vrátíš se za týden: „je tohle pravda?") a se spoluhráči. A memento na závěr: **odpracovaný čas nezvyšuje hodnotu hry** [(38:22)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=2302s) — nikdo hru nekoupí proto, žes na ní strávil dekádu; dokument je místo, kde zdůvodňuješ, proč věci budou fungovat *pro hráče*.

> **Pozn.:** GTA dalekohled je třetí formulace téže pravdy jako [„malá hra = jedna mechanika"](scope.md#mala-hra-jedna-mechanika-ne-zmenseny-skyrim) a [rozpočet pozornosti](scope.md#proc-male-rozpocet-pozornosti-ne-jen-dokoncitelnost) — škrt není ztráta, škrt je ohnisko. A teze „napřed zaměstnanec, pak indie" je vzácný protihlas k YouTube folklóru; vrátí se u kariérních videí druhé vlny.

**Souvislosti:** [Scope: malá hra = jedna mechanika](scope.md#mala-hra-jedna-mechanika-ne-zmenseny-skyrim) · [Postmortem ShantyTown](postmortem-shantytown.md) *(tříletý dokument-vs-realita z první ruky)* · [Rejstřík: user story](../rejstrik.md#user-story) · [Rejstřík: USP](../rejstrik.md#usp)

---

## Monaco: pitch jako zdůvodnění — Pac-Man ožeň s Hitmanem

**Zdroj:** [What Do "Professional" Game Design Documents Look Like?](https://www.youtube.com/watch?v=fk-rQlrNYZ8) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · rozbor dokumentu Monaco

**Shrnutí:** „Monaco kombinuje low-level mechaniky Pac-Mana se stealth prvky Hitmana" — učebnicový elevator pitch. Ne proto, že zní chytře, ale proto, že celý dokument pak **dokazuje, že to není fráze**: bod po bodu mapuje, jak přesně heist hra kopíruje Pac-Mana — a každý překlad zdůvodňuje. Pitch není ozdoba dokumentu; je to teze, kterou dokument obhajuje.

### Rozpad myšlenky

Řemeslo kombinace [(32:10)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1930s): „X meets Y" selhává dvěma způsoby — **redundancí** („The Walking Dead meets Day of the Dead": totéž dvakrát, proč to spojovat) a **nespojitelností** („The Walking Dead meets Sylvanian Families": hlava to neposkládá). Hledá se kombinace, u které člověk řekne „hm — zajímavé": dost blízko, aby držela pohromadě, dost daleko, aby byla nová [(32:59)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=1979s).

Mapování Pac-Mana na heist [(33:45)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=2025s) — tři přesné shody: **active stealth** (musíš se hýbat, abys unikal — Pac-Man, ne schovávaná za bednou); **vyluxuj prostředí od lootu** (tečky); **stráže omračuješ a za chvíli se vrací** (duchové v domečku — a zároveň kodex hrdinů heist filmů: nezabíjet). K tomu převleky jako power pellets (chvíli se pohybuješ volně) a časované minihry (lockpicking, hackování) jako kontrapunkt neustálého pohybu — které mimochodem dělají z abstraktního bludiště skutečné místo [(34:31)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=2071s).

Proč to je vzor a ne kuriozita [(33:45)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=2025s): **stavěj na ověřeném, ale rekontextualizovaném**. Čistá kopie vyvolává otázku „proč nehrát originál"; kopie v novém kontextu nabízí novost — a přitom máš rozumnou jistotu, že mechanismy fungují, protože už jednou fungovaly. V dokumentu je to vidět jako práce designéra-obhájce: každá půjčka má vedle sebe důvod, proč v novém rámu dává smysl [(37:36)](https://www.youtube.com/watch?v=fk-rQlrNYZ8&t=2256s).

> **Pozn.:** Tohle je [yoink & twist](napad.md#yoink-twist-lepsi-nebo-dost-jina) dotažený do dokumentační praxe — a zároveň dvojice [hook + anchor](napad.md#ctyri-zdroje-napadu-a-evaluace-hook-anchor-appeal) v akci: Pac-Man je anchor (každý ví, jak se hraje), heist s vlastními parťáky hook. Srovnej i s [„kopíruj poznámkami"](pripadovky-designu.md#150-her-na-operacnim-stole-vzorce-ktere-se-vraceji): kopíruje se mechanismus a důvod, ne povrch.

**Souvislosti:** [Nápad: yoink & twist](napad.md#yoink-twist-lepsi-nebo-dost-jina) · [Případovky designu](pripadovky-designu.md#150-her-na-operacnim-stole-vzorce-ktere-se-vraceji) · [Rejstřík: elevator pitch](../rejstrik.md#elevator-pitch) · [Rejstřík: hook](../rejstrik.md#hook)
