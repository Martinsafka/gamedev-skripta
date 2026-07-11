# Nápad: od záblesku k validované hře

Dvě videa od BiteMe Games — krátká diagnóza pěti nemocí herních nápadů a 67minutový „kurz" celého procesu od záblesku po validovaný prototyp. Společné jádro: **vymyslet nápad je snadné, validovat ho je práce.** Kapitola jde po téhle práci krok za krokem: proč nápady umírají, jak je testovat za hodinu, jak jim vybrat emoci, jak se poměřit s konkurencí a kdy prototyp zabít.

---

## Venn diagram nápadu: chci × umím × koupí

**Zdroj:** [The Only Game Idea Guide You'll Ever Need](https://www.youtube.com/watch?v=d_e9Apys9Dg) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · ~67 min, celý proces ·
[Your game idea (probably) sucks](https://www.youtube.com/watch?v=RqmHvVabdL0) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · ~18 min, katalog selhání

**Shrnutí:** Dobrý nápad leží v průniku tří kruhů: hra, kterou *chceš* dělat, hra, kterou *umíš* udělat, a hra, kterou *lidi chtějí hrát*. Většina mrtvých nápadů (autorův odhad: 80–90 % nikdy nevznikne) vypadla z některého kruhu — a selhání mají opakující se podoby, které jdou diagnostikovat předem.

### Rozpad myšlenky

Katalog selhání, poskládaný z obou videí podle toho, který kruh porušují:

- **Příliš velký** (kruh „umím") [(1:16)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=76s): open-world MMO od sólo vývojáře s pěti hodinami týdně. I „malá hra" znamená 4–8 měsíců vývoje, které stejně nabobtnají přes rok [(1:50)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=110s). Test upřímnosti: co jsi v životě dělal sedm let v kuse, když jsi nemusel? A velký scope má druhou daň: první hratelné jádro máš za dva roky místo dvou týdnů, takže celou dobu letíš bez zpětné vazby [(2:48)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=168s). Patří sem i „umím" v užším smyslu: tým BiteMe zabil svoje středověké CoD zombies, protože neměl skill na animace a multiplayer [(4:46)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=286s) — nápad může být dobrý a přesto ne *pro tebe teď*.
- **Příliš vágní** (kruh „chci" bez obsahu) [(4:52)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=292s): „RTS s teleportací, tak nějak citybuilder". Když hru neumíš vysvětlit, nevíš, co děláš — a projekt se každé tři měsíce potichu promění v jinou hru ve stejném Unity projektu. Diagnóza i lék je test 300 znaků (další myšlenka).
- **Příliš úzký** (kruh „koupí") [(5:30)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=330s): niche niche niche — koňské dostihy ve vesmíru. Průnik dvou publik je průnik, ne součet; viz [míchání žánrů](produktivita.md#scope-creep-a-michani-zanru-dvojsecna-past). Příbuzný druh: hra **příliš osobní** [(11:17)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=677s) — projekt pro čtyři lidi včetně tebe. Smí existovat! Jen si odpověz na otázku z videa: patří tahle hra na Steam [(13:54)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=834s), nebo ji dělám pro sebe a pro radost — a pak nemá smysl platit Steam fee a trápit se marketingem.
- **Příliš pozdě** (kruh „koupí", časová osa) [(14:15)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=855s): další 2D platformer proti Hollow Knight a Silksongu; desktop idlery rok po vlně [(16:11)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=971s) — žánr, kde hráč fyzicky uživí jen jeden kus. A pozor na kombinaci s „příliš velký": sedmiletý vývoj znamená, že vlna, na kterou míříš, přijde a odejde bez tebe [(17:00)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=1020s).

> **Pozn.:** Venn diagram cituje i [idea iceberg](rady-z-praxe.md) — je to zjevně sdílená mentální výbava téhle generace indie vývojářů. Iceberg přidává hloubkový rozměr (jak moc vidíš pod hladinu), Venn šířkový (které podmínky musí platit najednou).

**Souvislosti:** [Idea iceberg](rady-z-praxe.md) · [Co znamená „dělej malé hry"](scope.md) · [Žrouti času](produktivita.md) · [Zápisky: derivační řetěz IZBY](../zapisky/derivace-izby.md) *(odvození nápadu v plné délce z praxe)*

---

## Test 300 znaků: napiš Steam popis hry, která neexistuje

**Zdroj:** [Your game idea (probably) sucks](https://www.youtube.com/watch?v=RqmHvVabdL0) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · ~18 min ·
[The Only Game Idea Guide You'll Ever Need](https://www.youtube.com/watch?v=d_e9Apys9Dg) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · rozšíření na mock page

**Shrnutí:** Nejlevnější validační nástroj celé kapitoly: zkus v den nula napsat 300znakový Steam short description svého nápadu. Když to nejde, nemáš vágní popis — máš vágní hru. A psaní má druhý, nečekaný efekt: nápad zapsaný na papír přestane strašit v hlavě.

### Rozpad myšlenky

Formát testu [(6:56)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=416s): dvě věty, které řeknou žánr, perspektivu, hlavní činnosti hráče, cíl a prostředí. Hodně **sloves** [(7:38)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=458s) — slovesa jsou to, co hráč bude *dělat*, a právě jimi se abstraktní koncept stává srozumitelným. Kdo místo dvou vět spustí pětiminutový brain dump („je to tak trochu jako…, ale spíš…"), má odpověď: nápad ještě není hra.

Guide test rozšiřuje na **mock Steam page** [(24:08)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1448s): dlouhý popis se dvěma třemi hlavními features (formát nadpis + GIF, i když GIF zatím neexistuje), seznam vedlejších features, a klidně i zkusmá capsule — název hry vysázený žánrovým fontem přes náladový podklad. Ne kvůli kráse: skládáš všechny signály (název, vizuál, popis, emoce) vedle sebe a koukáš, jestli ladí. Teprve s tímhle balíkem má smysl jít za lidmi pro názor [(28:44)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1724s) — dřív jim nedáváš dost informací, aby mohli odpovědět užitečně.

Vedlejší mechanismus, který guide vysvětluje přes analogii mozku jako RAM [(26:07)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1567s): nezapsaný nápad krouží hlavou a vytváří iluzi kvality („myslím na to tři týdny, *musí* to být dobré"). Zápis ho vyplaví [(27:28)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1648s) — a druhý den se na něj podíváš cizíma očima. Proto: každý nový nápad během vývoje jiné hry **okamžitě zapiš a zavři do šuplíku** [(60:59)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=3659s); přestaneš na něj myslet a tvoje rozdělaná hra přežije.

> **Pozn.:** Tenhle test je psací obdoba pitch decku z [idea icebergu](rady-z-praxe.md#pracuj-zpatky-jak-brzy-jde-poznat-ze-by-hru-nekdo-koupil) — oba simulují první kontakt zákazníka s hrou dřív, než hra existuje. 300 znaků je sólo verze na pět minut; pitch deck týmová na hodinu.

**Souvislosti:** [Idea iceberg: pracuj zpátky](rady-z-praxe.md#pracuj-zpatky-jak-brzy-jde-poznat-ze-by-hru-nekdo-koupil) · [Start projektu: design dokument](jak-zacit.md#design-dokument-ktery-skutecne-otevres-nastenka-misto-eseje) · [Rejstřík: short description](../rejstrik.md#short-description)

---

## Core DNA a čtyři emoce

**Zdroj:** [The Only Game Idea Guide You'll Ever Need](https://www.youtube.com/watch?v=d_e9Apys9Dg) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · moduly o jádru hry

**Shrnutí:** Dvě otázky, které z mlhavého nápadu udělají designovatelný objekt: **co je core DNA hry** — nejmenší mechanické jádro, když odloupneš všechen obsah — a **kterou z čtyř emocí hra prodává**: power, cozy, tension, nebo wonder. Jedno DNA může nést různé hry podle toho, jakou emoci a žánrový tag k němu přimícháš; emoce se ale nemíchají.

### Rozpad myšlenky

**Core DNA** [(8:11)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=491s) se nejlíp chápe zpětným inženýrstvím hitů — ale pozor, jejich *release* verzí, ne dnešních rozšířených [(10:56)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=656s): Vampire Survivors je pohyb + auto-útok; Phasmophobia je first-person controller + pár nástrojů na lov duchů [(13:00)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=780s). Z jednoho DNA vedou různé cesty: ke stejnému jádru jde přimíchat roguelite, puzzle nebo co-op tag jako v té staré alchymistické hříčce — každá kombinace je jiná hra s jiným trhem. Cvičení: rozlož svůj nápad na DNA a projdi si, jak by vypadaly alternativní reality s jinými tagy.

**Čtyři emoce** [(16:11)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=971s): power (kosit hordy, stavět impérium), cozy (únik a bezpečí), tension (napětí, strach — včetně „nechci ztratit progress", proto je tension i Celeste), wonder (objevování, odkrývání mapy). Hráč nekupuje Stardew Valley kvůli rybaření, kupuje pocit [(16:00)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=960s). Míchání emocí je táž chyba jako míchání žánrů — steak se zmrzlinou v mixéru [(17:21)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1041s) (přirovnání autor připisuje Chrisi Zukowskému).

Zvolená emoce se pak stává **filtrem na features** [(22:48)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1368s): Papers, Please chce tension z morálních dilemat, a tak přidává přesně ty mechaniky, které dilema přiživují — možnost orazítkovat pas „špatně", peníze proti svědomí. Každá zvažovaná feature dostává otázku: podporuje hlavní emoci? Praktické cvičení na kalibraci [(20:25)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1225s): popiš prvních pět minut hry *pocitově* — hudba, obraz, první interakce. Elden Ring to řeší nevyhratelným úvodním bossem [(21:36)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1296s): emoční nastavení celé hry v prvních deseti minutách.

> **Pozn.:** Čtveřice power/cozy/tension/wonder je zjednodušení (akademické modely emocí ve hrách jsou bohatší — MDA framework mluví o osmi „aesthetics"), ale pro sólo vývojáře je právě proto použitelná: čtyři šuplíky, vyber jeden, drž ho.

**Souvislosti:** [Smyčky a řetězce](smycky-a-retezce.md) · [Jak udělat cokoli zábavným](zabava.md) · [Rejstřík: core loop](../rejstrik.md#core-loop)

---

## Yoink & twist: lepší, nebo dost jiná

**Zdroj:** [The Only Game Idea Guide You'll Ever Need](https://www.youtube.com/watch?v=d_e9Apys9Dg) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · modul o trhu a konkurenci

**Shrnutí:** „Stoprocentně originální" není přednost, ale riziko: znamená to, že poptávku nikdy nikdo nevalidoval — a hráč nemá referenční bod, přes který by hru pochopil. Spolehlivější vzorec je yoink & twist: vezmi žánr s prokázaným publikem a přidej vlastní vylepšení nebo obrat. Mladé žánry poráží se *lepší* provedení; staré žánry jen *jiné*.

### Rozpad myšlenky

Argument proti originalitě za každou cenu [(6:42)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=402s): unikátnost = nulová validace trhu + nesrozumitelnost (viz slovesa a referenční body v testu 300 znaků). Naopak klon bez přidané hodnoty taky neprodává [(8:16)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=496s) — a u streamerů má reskin ještě jeden problém: novelty decay [(10:11)](https://www.youtube.com/watch?v=RqmHvVabdL0&t=611s) — tvůrce obsahu už tenhle pitch jednou pokryl a čísla mu řekla, jestli se to vyplatí opakovat.

Postup, jak twist najít, je konkurenční rešerše: vyber **dva tři nejbližší konkurenty** [(42:23)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2543s) (jeden = slepé skvrny, pět = rozstřel), hodina hraní stačí [(42:42)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2562s), a hlavně **přečti negativní recenze** [(36:06)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2166s). BiteMe si pro svou anomaly hru udělali master dokument všech stížností žánru [(36:25)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2185s) — málo konců, nulová replayabilita, frustrující slepý reset — a designovali proti seznamu. Učebnicový případ z videa: Fields of Mistria [(34:31)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2071s) si dovolilo konkurovat Stardew Valley tím, že spravilo dvě jeho nejčastější bolesti (otravné rybaření, průměrné dialogy) — a prodává miliony, přestože vypadá jako klon.

Rozhodovací pravidlo lepší/jiná [(41:05)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2465s): v žánru s 25 lety historie (RTS) na „lepší než Age of Empires" nemáš rozpočet — musíš být jiný. Vlastní příklad studia: generické fantasy RTS s teleportací base přeznačili na nekromanta, který z podsvětí otevírá portály do overworldu [(39:12)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2352s) — **v kódu se nezměnilo nic** [(39:52)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2392s), a ze hry bez tváře byla hra s pitchem. U žánru starého dva roky (Balatro-likes) je to naopak: stačí být lepší — oprav jeden dva problémy a jeď.

K tomu tvrdá data: tagy přes [steamtaghelper.com](https://steamtaghelper.com) (autorův nástroj — průnik tagů podobných her), výdělky žánru přes Gamalytic/VG Insights; okno **poslední 3 roky** [(31:52)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1912s) (starší data lžou o dnešním trhu) a **medián nebo spodních 25–30 %** [(33:15)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=1995s), nikdy průměr — průměr táhnou nahoru výjimky. Když tě konzervativní číslo neuživí, věz to *před* začátkem vývoje.

**Souvislosti:** [Idea iceberg: market research](rady-z-praxe.md#napad-rozhoduje-vic-nez-je-videt-na-hladine) · [Rejstřík: yoink & twist](../rejstrik.md#yoink-twist) · [Rejstřík: market research](../rejstrik.md#market-research)

---

## Prototyp do týdne a momentum bar

**Zdroj:** [The Only Game Idea Guide You'll Ever Need](https://www.youtube.com/watch?v=d_e9Apys9Dg) · [BiteMe Games](https://www.youtube.com/channel/UCHUgO0pyXWkGnQUYp5JgoUg) · moduly o prototypu a validaci

**Shrnutí:** Poslední soud nápadu je prototyp — a má trvat jeden až pět dní, ne týdny [(43:45)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2625s). Kontroverzní rada videa: žádný graybox — prototypuj rovnou s asset packy, hudbou a art directionem, protože testuješ emoci, ne mechaniku v izolaci. A pak nech nápad týden odležet: přežije-li, máš hru.

### Rozpad myšlenky

Proč tak rychle: rychlost není jen efektivita, je to **ochrana proti připoutání** [(53:33)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=3213s) — do prototypu za čtyři týdny se zamiluješ a mrtvý nápad budeš oživovat („I can fix her"); prototyp za dva dny jde do koše bez smutku. Nápadů budeš potřebovat projít hodně, ne jeden.

Proti grayboxu [(44:17)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2657s) stojí argument z předchozí myšlenky: hra prodává emoci a šedé kostky žádnou nemají. Takže od prvních řádků kódu jednoduchý music controller [(44:49)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2689s), asset packy místo vlastního artu [(50:09)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=3009s) (Synty, Kenney, itch.io) a vizuál aspoň směrem k zamýšlenému stylu — i playtester pak hodnotí hru, ne technické demo. Zbytek triků je bezostyšné falšování [(50:46)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=3046s): dialogy natvrdo, žádná lokalizace, žádné modulární systémy (přesně inverze [enginů v enginu](produktivita.md#investice-bez-validace-lesteni-systemy-a-optimalizace-predem) — tady je hardcoding ctnost, protože kód je na vyhození). **Game feel co nejdřív** [(51:13)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=3073s): „game feel je cheat code" — částice a impakt zamaskují nedodělky líp než cokoli jiného. Zákazy: multiplayer v prototypu ne (single-player verze musí fungovat sama [(46:46)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2806s); multiplayer-only hra je podle autora mrtvá ve vodě [(46:58)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=2818s)), custom enginy ne. A když se na něčem zasekneš, přeskoč to jako těžkou otázku v testu — vrátíš se s čerstvou hlavou.

Validace hotového prototypu [(54:17)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=3257s): na itch.io (stránku máš — přepiš mock Steam page), 30s trailer, klidně scuffed TikTok formát „dělám svou první hru, co myslíte?" [(56:24)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=3384s) — vypadá amatérsky schválně, konvertuje tak dobře, že ho záměrně používají i publisheři. Sbíráš datové body, ne sliby.

A nakonec **momentum bar** [(58:14)](https://www.youtube.com/watch?v=d_e9Apys9Dg&t=3494s), nejlepší mentální model videa: každý nápad startuje s jinou zásobou nadšení, která každý den nečinnosti klesá. Nech prototyp týden ležet. Slabý nápad se vybije sám — za tři dny je ti ukradený a máš odpověď zadarmo. Silný přežije a pozitivní ohlasy mu bar dobíjejí. Teprve pak se stavěj most z prototypu do produkce.

> **Pozn.:** Graybox vs. asset packy není dogma, ale spor o to, *co testuješ*: mechanickou hloubku (graybox ji izoluje — tak pracuje [prototypování podle Indie Game Clinic](prototypovani.md)), nebo prodejnost a vibe (tam graybox lže). Odpověz si, kterou otázku zrovna klade tvůj prototyp, a vyber podle toho.

**Souvislosti:** [Prototypování a vertical slice](prototypovani.md) · [Idea iceberg: the Gap](rady-z-praxe.md#the-gap-rozdil-mezi-to-je-hezky-a-tohle-musim-hrat) · [Rejstřík: game feel](../rejstrik.md#game-feel) · [Rejstřík: asset pack](../rejstrik.md#asset-pack)
