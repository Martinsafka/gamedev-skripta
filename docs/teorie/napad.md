# Nápad: od záblesku k validované hře

Čtyři videa od tří tvůrců — BiteMe Games (diagnóza nemocí nápadů + 67minutový „kurz" celého procesu), Game Maker's Toolkit (kde se nápady berou a jak je hodnotit) a Indie Game Clinic (osm technik ideace včetně SCAMPER). Společné jádro: **vymyslet nápad je snadné, validovat ho je práce.** Kapitola jde po téhle práci krok za krokem: kde nápady vznikají, proč umírají, jak je testovat za hodinu, jak jim vybrat emoci a kdy prototyp zabít.

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

---

## Čtyři zdroje nápadů — a evaluace: hook, anchor, appeal

**Zdroj:** [How to find amazing game ideas](https://www.youtube.com/watch?v=0m60QbT85Tc) · [Game Maker's Toolkit](https://www.youtube.com/channel/UCqJ-Xo29CKyLTjn6z2XwYAw) · ~27 min, 1. díl série Game Dev 101

**Shrnutí:** Mark Brown po vydání Mind Over Magnet přiznává, že jeho největší chybou byla neznalost produkční pipeline — a začíná sérii o ní od úplného začátku: kde se berou nápady. Odpověď má čtyři šuplíky (existující hra, žánr, nová mechanika, zážitek) a druhou půlku, na kterou se zapomíná častěji: jak poznat, jestli nápad stojí za roky práce. Tam nastupují tři slova — hook, anchor, appeal.

### Rozpad myšlenky

**Čtyři zdroje nápadů:**

1. **Existující hra jako odraziště** [(2:24)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=144s): posuň perspektivu (Factorio z první osoby = Satisfactory), téma (Minecraft pod vodou = Subnautica), médium (společenská hra Werewolf → Among Us), nebo vzkřis mrtvou sérii (Stardew Valley vznikl, protože Harvest Moon podle Barona „postupně upadal"). Nápad navíc projde filtrem tvého vkusu: z her japonského tvůrce Ikiki vzešel nevydaný klon, z klonu po přidání vibu Dennise Wedina Hotline Miami [(3:14)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=194s) — a ta zase inspirovala celou generaci. Terry Cavanagh to říká bez okolků: **everything is a remix** — tvorba nevzniká ve vakuu [(4:50)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=290s).
2. **Žánr jako recept** [(5:37)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=337s): oprav, co tě na žánru štve (RNG nefér roguelike → rytmický Crypt of the NecroDancer; city builder s bobtnající složitostí → Islanders), zkombinuj dva žánry (Spelunky), odeber core mechaniku (Captain Toad neumí skákat [(6:27)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=387s)), nebo vyměň metaforu: FPS je v jádru zaměřování — místo zbraně foťák = Pokémon Snap, wapka = PowerWash Simulator [(7:15)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=435s). Žánr ber co nejvolněji: vyvař ho na DNA a stav od ní.
3. **Mechanika z reálného světa** [(8:06)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=486s): pasová kontrola → Papers, Please; zahradničení → Pikmin; ovládání jako zdroj (swipe = seknutí mečem → Fruit Ninja; analogové triggery GameCubu připomněly Koizumimu vodní pistolky → Mario Sunshine [(9:44)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=584s)); nebo izoluj mechaniku cizí hry a vypěstuj z ní celou svou (rewind z Prince of Persia → Braid; downthrust ze Zeldy 2 → Shovel Knight [(10:32)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=632s)). Tomuhle směru se říká **bottom-up**: mechaniky napřed, téma potom — Splatoon začal jako bloky tofu schovávající se v inkoustu [(11:21)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=681s).
4. **Zážitek napřed = top-down** [(12:09)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=729s): FTL nevznikl ze systémů, ale z fantazie „jsi kapitán Picard a řveš na inženýry, ať nahodí štíty"; Thronefall z power fantasy vládce miniaturního království; Spiritfarer z touhy mluvit o smrti útulně [(12:55)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=775s). Mechaniky se hledají až k obrazu.

**Příběh není herní nápad — a jedna mechanika taky ne** [(13:43)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=823s). Test hratelnosti: co je win state, co překážka, co fail state a co hráč *dělá* — Crazy Taxi na tyhle čtyři otázky odpoví jednou větou [(14:32)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=872s).

**Evaluace** — protože udělat první nápad, co tě napadne, je podle Jonase Tyrollera ruská ruleta [(19:17)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1157s):

- **Zvládneš to ty?** Jonasovo pravidlo palce: gameplay prototyp za 1–2 dny → hra za 1–2 roky; prototyp za dva týdny → projekt na velmi dlouho [(20:04)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1204s). Scope jde ohnout: Firewatch neměl rozpočet na 3D postavy, tak celý příběh přesunul do vysílačky [(20:52)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1252s).
- **Vynikne?** **Hook** = informace, která nutí hru zkusit nebo o ní mluvit (Ryan Clark) [(21:40)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1300s). Headline test: „Darkest Dungeon je lovecraftovský dungeon crawler o psychické dani dobrodružství" — kliknul bys? Ale pozor na přestřelení: příliš originální hra budí nedůvěru — mezoamerické RPG Arco s „bullet-hell-ish real-time turn-based combatem" kritika chválila a prodeje nepřišly [(23:14)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1394s). Proto **anchor**: povědomý prvek, který hráče ukotví (známé mechaniky, žánr, značka). Vzorec Zacharyho Richmana: **simple, with something unexpected** — tower defense, kde tě zraní vlastní kulky; jednoduché otevře dveře, nečekané zahákne [(24:03)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1443s).
- **Přitahuje?** Jonasův **appeal** = síla, která táhne ke hře před hraním: fantasy appeal („chci tohle být"), exploration appeal („chci to prozkoumat"), toy appeal („chci na to sahat") [(24:49)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1489s). Test: Lucas Pope u každého nápadu zkouší v hlavě sestříhat trailer — když nejde, nápad zahodí [(25:37)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1537s); Tom Francis doporučuje vymyslet název a capsule art dřív, než padne první řádek kódu.
- **Baví to?** Nezjistíš přemýšlením: **mozek je mizerný simulátor videoher** — v hlavě zní skvěle skoro všechno [(26:25)](https://www.youtube.com/watch?v=0m60QbT85Tc&t=1585s). Jediná odpověď je prototyp.

> **Pozn.:** Anchor je totéž, co v [scope kapitole](scope.md#omezeni-potrebuje-herni-alibi) dělá „herní alibi" pro omezení — povědomost jako most k novince. A Jonasovo pravidlo 1–2 dnů ladí s BiteMe [prototypem do týdne](#prototyp-do-tydne-a-momentum-bar): oba měří totéž — kolik hry se dá ověřit, než jí uvěříš.

**Souvislosti:** [Co prodává: appeal](co-prodava.md#ctyri-pilire-a-sedm-cest-k-appealu) · [Yoink & twist](#yoink-twist-lepsi-nebo-dost-jina) · [Test 300 znaků](#test-300-znaku-napis-steam-popis-hry-ktera-neexistuje) · [Rejstřík: hook](../rejstrik.md#hook) · [Rejstřík: anchor](../rejstrik.md#anchor-marketing)

---

## Ideace jako řemeslo: skills audit, věta s cílem a SCAMPER

**Zdroj:** [The Secret to GOOD Game Ideas — Practical Ideation Methods](https://www.youtube.com/watch?v=LMOCQNcMleg) · [Indie Game Clinic](https://www.youtube.com/channel/UC9v7V5PKy-FeB9iVY2T5mMA) · ~24 min, osm technik

**Shrnutí:** Kreativní člověk má nápadů víc, než unese — problém je systematicky je třídit a mít i takové, které jde *provést*. Osm technik Joea Baxtera-Webba se dělí na generování (život, ne-hry, omezení) a hodnocení (věta s cílem, momenty) — a končí formálním generátorem SCAMPER, který umí obojí.

### Rozpad myšlenky

**Ze života, ne ze Skyrimu** [(0:48)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=48s): roznášel jsi noviny, hlídal děti, dělal ve skladu? O všem existují úspěšné hry — zatímco trh přetéká zombíky, fantasy a vesmírem [(1:34)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=94s). Všední téma má skrytý bonus: **nutí tě skutečně designovat** — combat a crafting si poskládáš z tisíců hotových vzorů, hru o hlídání dětí musíš vymyslet sám [(2:21)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=141s). A jsi jeden ze sta autorů her o pekárně místo jednoho z deseti milionů o zombících.

**Interakce z ne-her** [(3:07)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=187s): Reigns je vláda královstvím přes swipe rozhraní Tinderu; Mini Metro je vláčková hračka; prak v Angry Birds je objekt z reálného světa — i úplně sváteční hráč okamžitě ví, co se stane [(3:53)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=233s). Designér má být zvědavý na „design všedních věcí": hračky, fidget cube, appky — všechno jsou katalogy interakcí [(4:41)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=281s).

**Skills audit** [(5:27)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=327s): nováčci přestřelují scope, protože nevědí, co nevědí. Sedni si a sepiš: co umím, co neumím, co napůl — je to inventura zdrojů projektu. Máš ilustrátora, ale ne animátora? Hra s mluvícími portréty místo chodících postav. Zní to jako prohra, dokud si nevzpomeneš, že Dredge nemá walk cycle a Mini Metro nemá ani postavy [(6:13)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=373s). Omezení vyřadí 90 % nápadů — a zbydou ty proveditelné; když navíc u zbylých máš osobní zkušenost (lodě a plachtění), získáváš nefér výhodu [(7:01)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=421s).

**Find the fun & retheme** [(7:48)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=468s): nebuď ženatý s tématem. Gabe Cuzzillo dělal top-down ninja stealth, ale bavilo ho chytání a strkání nepřátel — tak z ninji udělal gorilu, z nepřátel křehké střelce a vznikl Ape Out, „nejlepší ultranásilná jazzová gorilí hra roku 2019" [(8:34)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=514s).

**Oprav vnímaný problém** [(8:34)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=514s): Plants vs. Zombies řešil zadání „tower defense pro lidi, co tower defense nikdy nehráli" [(9:21)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=561s). Cvičení: vezmi žánr, který *nemáš rád*, a zjisti, co by se muselo změnit, abys ho rád měl — problem statement navíc míří na trh, který nikdo neobsluhuje [(10:07)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=607s).

**Pitch jednou větou: cíl + akce** [(10:30)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=630s): „hra o teenagerských superhrdinech" není nápad na hru, jen na setting. Věta musí říct, o co hráč usiluje a co pro to dělá: Into the Breach — zachraňuješ města tím, že ničíš kaiju a vylepšuješ mechy [(11:16)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=676s); Stardew — buduješ farmu chovem, pěstováním a přátelstvím s městečkem [(12:04)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=724s). Nejde-li věta napsat, máš nápad na příběh, ne na hru [(12:50)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=770s) — projeď tímhle sítem celý seznam nápadů; a mimochodem přesně takhle se píše marketing copy.

**Design pro momenty** [(13:37)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=817s): deskovkový designér Eric Lang si představí hráče v krámě, jak líčí, co se jim v partii stalo — a pak navrhne hru, která ty vzpomínky vyrábí [(14:24)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=864s). Player-centered myšlení: obsahu můžeš mít tuny, ale hra bez zapamatovatelných momentů se zapomene. Když vybíráš z deseti nápadů, ber ten, u kterého vidíš radost hráčů [(15:11)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=911s).

**SCAMPER** [(15:58)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=958s) — formální technika, která rozhýbe zaseknutý nápad i vygeneruje nový z oblíbené hry: **S**ubstitute (vyměň téma nebo mechaniku), **C**ombine (kombinuj — pozor na složitost; elegantní verze: XP a zlato jako jedna měna = Dark Souls [(17:33)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=1053s)), **A**dapt (jiný kontext: Resident Evil pro děti, se stejným přístupem k lekání), **M**agnify (zazoomuj na nejzábavnější prvek — celá hra o upírově slabosti na slunce místo „všeho o upírech" [(18:21)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=1101s)), **P**urpose (co kdyby hra byla výuková, terapeutická, historický záznam? [(19:07)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=1147s)), **E**liminate (generátor „hra bez X": Skyrim bez magie, Fortnite bez stavění; GTA minimalizuje vězení, protože neslouží fantazii [(19:53)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=1193s)), **R**earrange (hráč padouchem v žánru hrdinů, příběh od starého hrdiny [(21:28)](https://www.youtube.com/watch?v=LMOCQNcMleg&t=1288s)).

> **Pozn.:** Skills audit je měkčí sourozenec řemeslnických otázek z [rozpočtu pozornosti](scope.md#proc-male-rozpocet-pozornosti-ne-jen-dokoncitelnost) („co neumím tak, že to do projektu nesmí?") — a Ape Out příklad si autor o rok později naordinoval sám: viz [pivot Golem Gourmet](scope.md#pivot-kdyz-hra-nasla-jadro-jinde-nez-jsi-planoval). Magnify z SCAMPER je totéž co „malá hra = jedna mechanika" řečené generátorem.

**Souvislosti:** [Scope: design by constraint](scope.md#design-by-constraint-krabice-napred-napad-dovnitr) · [Test 300 znaků](#test-300-znaku-napis-steam-popis-hry-ktera-neexistuje) · [Systémy a mechaniky](systemy-a-mechaniky.md) · [Rejstřík: SCAMPER](../rejstrik.md#scamper) · [Rejstřík: skills audit](../rejstrik.md#skills-audit)
