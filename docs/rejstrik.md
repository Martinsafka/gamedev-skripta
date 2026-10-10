# Rejstřík

Odborné termíny napříč skripty — **termín anglicky, výklad česky**, protože přesně tak se s nimi potkáš v editoru, dokumentaci i komunitě. Rejstřík má dvě vrstvy: každý výskyt termínu kdekoli na webu má automatický tooltip s krátkou definicí a tahle stránka přidává hloubku a odkazy do kapitol, kde termín žije v kontextu.

Rejstřík roste s obsahem — každé zpracované video sem přidává svoje pojmy.

---

### AAA

**Termín z financí, ne z kvality: označuje největší a nejbezpečnější finanční sázky v oboru.**

Analogie s ratingem dluhopisů. Neříká nic o tom, jestli je hra dobrá — říká, že rozpočet a marketing jsou tak velké, že si projekt nemůže dovolit riskovat. Proto může existovat i nezávisle financovaná AAA hra: nezávislost a měřítko jsou dvě různé osy. Doplňkově se používá AA pro střední rozpočty.

Kde se s tím potkáš: [Indie kariéra](teorie/indie-kariera.md#kdy-indie-hra-neni-indie-hra)

### A/B test

**Dvě verze téže hry dvěma skupinám testerů — rozhodne chování hráčů, ne jejich názor.**

Testerům se často neříká, co se testuje, ani že existuje druhá verze. Ukázkový případ: puzzle hra řešila, jestli zrušit skok — verze s nízkým skokem sklidila „na co tu je?", ve verzi bez skoku si většina hráčů absence ani nevšimla. Škrt potvrzen daty, ne debatou.

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md)

### Abstract class

**Třída, kterou nejde umístit do světa ani vybrat v referencích — existuje jen jako rodič pro děti.**

U base class v Blueprintech se zapíná v `Class Settings → Generate Abstract Class`. Smysl: master má nést jen data a logiku, žádné meshe či materiály — cokoli master referencuje, se nahrává do paměti s každou referencí na něj. Abstraktní master nikdo omylem nespawne a size map zůstává štíhlá.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Kdy dědit a kdy jen konfigurovat](praxe/principy-architektury.md#kdy-dedit-a-kdy-jen-konfigurovat) · [BP_BaseItem pro předměty](praxe/interakcni-animace.md#objekt-vi-jak-se-s-nim-zachazi-data-interakce-patri-k-veci-ne-k-postave)

### ABTest

**Konzolový příkaz, který střídá dvě hodnoty jedné konzolové proměnné a vypisuje naměřený výkon obou — A/B srovnání nastavení přímo ve viewportu.**

Hodí se, když se rozhoduješ mezi dvěma hodnotami jednoho nastavení a nechceš je přepínat ručně a porovnávat odhadem. Pořád je to ale měření jednoho místa jedné scény; rozhodnutí pro celý projekt patří do opakovatelného testu. Neplést s [A/B testem](#ab-test) z playtestingu, kde se porovnávají dvě verze hry na hráčích.

Kde se s tím potkáš: [Technické zdraví projektu](praxe/organizace-projektu.md#technicke-zdravi-projektu-kontroly-od-prvniho-dne-po-vydani) · [Profiling: reprodukovatelný test](praxe/profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic)

### ACP

**Otevřený protokol pro připojení coding agentů k nástrojům; podle popisu přednášky JetBrains funguje po vzoru LSP.**

Rider přes něj bere agenty z registru i vlastní agenty a Rider Kit tak pouští agenta s plnou integrací IDE i do Unreal Editoru. Pro uživatele to znamená, že agenta jde vyměnit, aniž by se měnilo napojení na nástroje.

Kde se s tím potkáš: [Agent v IDE](praxe/mcp-v-editoru.md#agent-v-ide-index-a-debugger-misto-hledani-v-textu) · [Rejstřík: Rider](#rider) · [Rejstřík: MCP](#mcp)

### Active frames

**Snímky útoku, ve kterých útok opravdu zraňuje — mezi nápřahem (startup) a zotavením (recovery).**

Termín z bojovek. V UE se dají vyjádřit notify statem přes tyto snímky: jeho Received Notify Tick běží v každém snímku okna a táhne hitbox, třeba kouli mezi dvěma sockety zbraně. Jeden útok může mít víc oken s různými parametry (obě ruce, silnější špička čepele). Opakem je jediný impact frame, kdy zásah padne na jeden snímek.

Kde se s tím potkáš: [Hitbox podle poctivosti animace](praxe/souboj.md#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames) · [Rejstřík: Frame data](#frame-data)

### Actor Component

**Znovupoužitelný díl chování, který se připne k libovolnému aktérovi — schopnost bez identity.**

Nemá vlastní reprezentaci ve světě (na rozdíl od scene komponent); nese logiku a data. Klíčové pravidlo: komponenta nikdy nepředpokládá, kdo ji používá — smrt, zásah nebo dokončení jen oznamuje dispatcherem a nechá vlastníka reagovat po svém. Skládání komponent je v UE náhrada za hlubokou dědičnost.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md#komponenty-misto-dedicnosti-skladej-misto-vetveni) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) · [Dvě komponenty: útočník a terč](praxe/souboj.md#dve-komponenty-misto-bojove-postavy-utocnik-a-terc)

### Additive animation

**Animace, která se k základní póze přičítá, místo aby ji nahradila — rozdíl proti referenční póze přidaný navrch.**

Typické použití je náklon, nádech, zásah nebo pohled: základní animace (třeba chůze) běží dál a přírůstek ji jen pozmění. Pastí je přeaplikování. Když se základní póza sama posune stejným směrem (gesto, kývnutí), sečte se to a výsledná póza se rozbije, a proto se síla přírůstku ladí nebo ztlumí křivkou. Look-at v GASP 5.8 je aditivní solver: rotaci k cíli spočítá a přidá, zahranou animaci nemaže.

Kde se s tím potkáš: [Look-at jako aditivní solver](praxe/gasp.md#look-at-jako-aditivni-solver-pohled-bez-ztraty-animace) · [Rejstřík: Layered Blend Per Bone](#layered-blend-per-bone)

### ADSR

**Čtyři knoby obálky: Attack, Decay, Sustain, Release — jak zvuk naběhne, klesne, drží a dozní.**

Attack = náběh po stisku, decay = pokles k sustainu, sustain = hlasitost při držení, release = doznění po puštění. Platí pro noty i zvukové efekty; malá změna dynamiky výrazně mění pocit.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md) · [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Aerial perspective

**Vzdušná perspektiva: čím dál objekt je, tím víc ho překryje barva atmosféry, nejdřív do modra a ve velké dálce do bíla.**

Je to nejlevnější způsob, jak dát krajině měřítko a hloubku. Ve hrách ji obvykle dělá mlha nebo barevný gradient podle vzdálenosti v shaderu. Barva závisí na tom, kolik vzduchu leží mezi okem a cílem, a proto vzdálené hory blednou stejně jako obloha k horizontu. Přehnaná aerial perspective umí předstírat větší dohled, než jaký scéna skutečně má.

Kde se s tím potkáš: [Dohled na kilometry](praxe/velke-svety.md#dohled-na-kilometry-vetsi-chunky-v-dalce-stromy-se-stinem-a-souradnice-ktere-nepretecou) · [Rejstřík: Volumetric fog](#volumetric-fog)

### Affordance

**Vlastnost objektu či prostoru, která signalizuje, jak s ním jde interagovat — dřív, než to hráč zkusí.**

Pojem z designové psychologie (Gibson, Norman): klika říká „stiskni", římsa říká „vylez". V level designu se affordances vyrábějí světlem, kompozicí a kontrastem — tajná odbočka musí *vypadat* zajímavě a interaktivně, jinak ji hráč mine. Zrádné jsou falešné affordances: co vypadá průchozí a není, rozbíjí důvěru (viz invisible wall).

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Vedení hráče](teorie/vedeni-hrace.md)

### Agent skill

**Text s know-how, které model sám nemá, načítaný podle úkolu; Unreal i Claude Code ho berou podle otevřeného standardu Agent Skills.**

Typicky jde o drobné pravidlo zkušeného člověka, třeba „nastav slunce dřív než oblohu". V Unrealu jde skill napsat v C++, v Pythonu nebo jako blueprint asset, který se verzuje s projektem a sdílí s týmem. Epic radí psát skills nově (jen to, co model neví), kolegiálně, trvanlivě (bez jmen properties, která se můžou změnit) a stručně.

Kde se s tím potkáš: [Vlastní tool set a skill](praxe/mcp-v-editoru.md#vlastni-tool-set-a-skill-api-pro-juniora-a-rada-kolegovi) · [Asistent, ne zázrak](praxe/mcp-v-editoru.md#asistent-ne-zazrak-slovnik-priklady-a-skills-delaji-z-llm-stavitele-sveta) · [Rejstřík: Tool set](#tool-set)

### Aggro

**Míra, jak moc chce nepřítel útočit na konkrétní cíl — skóre, podle kterého si vybírá mezi hráči.**

V Lords of the Fallen ho skládají čtyři složky: blízkost, poškození, které cíl nepříteli vytrvale dává, umělé aggro (aby nepřítel zůstal u jednoho hráče) a skóre přepnutí, které brání přeskakování mezi cíli. Některé složky s časem klesají podle křivek. Kdo nepřítele občas trefí, neodláká ho; kdo útočí soustavně, ano.

Kde se s tím potkáš: [Kdo útočí a kdo čeká](praxe/ai-ve-velkem.md#kdo-utoci-a-kdo-ceka-aggro-skore-a-bojove-role) · [Rejstřík: Utility AI](#utility-ai)

### AI Controller

**Mozek AI postavy: posedne pawna (tělo) a rozhoduje — kam jít, kdy útočit; tělo řeší pohyb a animace.**

Oddělení mozku od těla umožňuje znovupoužít logiku napříč postavami. Controller typicky spouští Behavior Tree nebo State Tree (`Run Behavior Tree` / StateTreeAI komponenta) a nese AI Perception. Postava ho dostane přes `AI Controller Class` + `Auto Possess AI`.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [State Trees](praxe/state-trees.md)

### AI Perception

**Percepční systém UE: smysly (sight, hearing, damage) jako konfigurace jedné komponenty, události při změně vjemu.**

Mocnější nástupce Pawn Sensingu: víc smyslů, stárnutí vjemů, lose sight radius (hystereze ztrácení cíle). Dva zádrhely: cíl musí mít AI Perception Stimuli Source komponentu a každý sense config potřebuje zaškrtnout Detect Enemies/Neutrals/Friendlies. Sluch a damage se hlásí přes Report Noise/Damage Event — signály pro AI, ne herní zvuk či poškození.

Kde se s tím potkáš: [AI vnímání](praxe/ai-vnimani.md) · [State Trees](praxe/state-trees.md) · [Základy AI](praxe/ai-zaklady.md) · [AI, která nereaguje](praxe/debugging.md#ai-ktera-nereaguje-gameplay-debugger-a-dve-tiche-priciny)

### Akord

**Tři a více tónů znějících zároveň; nejzákladnější je triáda (základ + tercie + kvinta).**

Podle rozestupů je durový (světlý), mollový (temný) nebo zmenšený (ostrý). Ze stupnice vypadne sedm akordů s předvídatelnou náladou: 1., 4. a 5. stupeň durové, 2., 3. a 6. mollové, 7. zmenšený.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md) · [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Alikvóta

**Vyšší frekvence znějící nad základním tónem (overtone); určuje barvu zvuku a to, co ladí.**

Reálný tón není jedna sinusovka, ale základní frekvence plus řada alikvót. U struny a píšťaly jsou to celočíselné násobky (harmonická řada). Souzvuk vzniká, když se alikvóty dvou tónů dobře potkávají a málo perou.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### ALS

**Advanced Locomotion System — komunitní locomotion framework pro UE; jeho autor dnes v Epicu designově vede GASP.**

Roky de facto standard pokročilého pohybu z marketplace: overlay stavy (pózy držení předmětů vrstvené přes locomotion), layer curves pro per-kost řízení blendů, stance systém. GASP je jeho duchovní nástupce a komunita ALS animace i vzory dál recykluje — overlay přístup ke zbraním nad GASP je přímo z ALS playbooku.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Ambient occlusion

**Ztmavení míst, kam se hůř dostane rozptýlené světlo — kouty, spáry, styky ploch.**

Zkratka za výpočet, jak moc je bod zastíněný okolní geometrií. Dá se zapéct do textury, spočítat ve scéně (screen-space) nebo přimíchat v shaderu násobením přes základní barvu. Fotografické textury vlastní stínění nemají, takže se jim AO musí vracet uměle — bez něj vypadá model plocho.

Kde se s tím potkáš: [Z fotky herní asset](praxe/foto-do-assetu.md#hloubka-bez-druhe-textury) · [Breakdowny: The Ascent](praxe/env-breakdowny.md#the-ascent-ctyri-artisti-jeden-shader)

### Anchor (marketing)

**Povědomý prvek, který hráče ukotví u příliš nové hry: známý žánr, mechanika nebo značka.**

Protiváha hooku (termín Chrise Zukowského): samotná novost budí nedůvěru — „looks cool but I don’t trust it". Hra chce obojí: hook, který zastaví palec, a anchor, díky kterému si hráč umí představit, jak se to hraje. Vzorec Zacharyho Richmana: simple, with something unexpected.

Kde se s tím potkáš: [Nápad: hook, anchor, appeal](teorie/napad.md) · [Steam stránka](teorie/steam-stranka.md)

### Anchor (UI)

**Kotva Control nodu: číslo mezi 0 a 1 určující, kde v rodičově obdélníku prvek začíná a končí.**

Nezaměňovat s [anchorem z marketingu](#anchor-marketing). Řeší jediný problém — layout, který přežije jiné rozlišení. Kotva 0,5 je střed a zůstane středem, protože počet pixelů přestal hrát roli. Doplňují ji **offsety** v pixelech měřené od kotvy (pravý a dolní musí být záporné, mají-li být uvnitř). Nejčastější nedorozumění: **kotvy jsou relativní k rodičovskému nodu, ne k oknu** — kořen je výjimka jen proto, že rodiče nemá. Dítě kontejneru kotvy nemá vůbec; místo nich má container sizing options.

Kde se s tím potkáš: [Kotvy a offsety](godot/ui-control.md#kotvy-a-offsety-layout-ktery-prezije-jine-rozliseni) · [Menu jako předmět ve scéně](praxe/ui-ve-svete.md#menu-jako-predmet-ve-scene-widget-na-televizi-a-virtualni-mys)

### Animation curve

**Pojmenovaná křivka hodnot uložená v animaci nebo montáži — AnimBP ji každý snímek přečte (`Get Curve Value`) a řídí jí cokoli, co má jet v rytmu animace.**

Typické použití: alfa IK ruky, která se zapne jen ve chvíli úchopu, úhel dveří nebo kliky sladěný s rukou, váha pózy prstů. Hodnoty se vyplatí ukládat normalizované (0–1) a maximem násobit až v kódu — změna maxima pak neznamená přepisovat animace. Po skončení montáže křivka čte nulu, takže trvalý stav světa (otevřené dveře) je potřeba podržet zvlášť. Křivkami se dá i upravit animace samotná přímo v editoru: posunout kost a uložit klíč.

Kde se s tím potkáš: [Animace řídí svět](praxe/interakcni-animace.md#animace-ridi-svet-normalizovane-krivky-v-montazi) · [Ruka na klice: alfa z křivky](praxe/interakcni-animace.md#ruka-na-klice-ik-v-control-rigu-prevod-prostoru-a-alfa-z-krivky) · [Řemeslo první osoby: úprava hotové animace](praxe/animace-nastroje.md#krivky-kamera-a-past-30-snimku-remeslo-prvni-osoby) · [Křivka BlendOff v útoku](praxe/souboj.md#utok-za-behu-horni-pulka-bojuje-dolni-bezi-a-krivka-rekne-kdy-ne) · [Síla ragdollu z křivek](praxe/ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu) · [Přepis limitů look-atu](praxe/gasp.md#look-at-jako-aditivni-solver-pohled-bez-ztraty-animace)

### AnimGen

**Experimentální plugin v UE 5.8 pro vlastní animační controllery na strojovém učení, které se trénují přímo v editoru.**

Ukázka na Fabu generuje z jednoho controlleru chůzi hráče s pistolí i NPC v asi čtyřiceti stylech, od nesení tašky po kulhání. Podle Epicu stačilo na demo zhruba 5–10 minut mocapu v řadě stylů a controller běží za rozumný rozpočet výkonu i paměti. Bližší má k Motion Matchingu než ke generátoru klipů: ze záznamu pohybu dělá ovladatelnou postavu.

Kde se s tím potkáš: [Animace z modelu přímo ve hře](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu) · [Rejstřík: Motion matching](#motion-matching)

### Anim montage

**Animační asset pro jednorázové akce (útok, interakce), přehrávaný přes sloty do vybraných částí skeletu.**

Nad Motion Matchingem je montáž základ combatu: spodní tělo matchuje locomotion, horní hraje montáž ve slotu Upper Body (Layered Blend Per Bone + Blend Poses by Bool). Anim notifies uvnitř montáže řídí comba (AddCombo/ResetCombo okna); sloty pro zbraně patří do vlastní slot skupiny, ať výměna nepřeruší jiné montáže. Pro matchování do montáže slouží Pose Search Branch In.

Montáž se dělí na [sekce](#montage-section), mezi kterými lze za běhu přepínat, a nese [křivky](#animation-curve), které řídí věci jedoucí v jejím rytmu (úhel dveří, alfa IK, póza prstů).

Do výsledné pózy se montáž dostane jen přes uzel `Slot` v AnimBP; sekvence sama přes slot neprojde. Svižný útok chce blend in 0 a blend out kolem 0,2 s. Pozor na `Play Montage`: spuštění nové montáže zastaví ostatní a přerušená montáž nedoběhne do On Completed (přijde On Interrupted).

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md) · [MM základy](praxe/mm-zaklady.md) · [Zápas se smyčkou: sekce](praxe/interakcni-animace.md#zapas-se-smyckou-sekce-montaze-a-rozhodnuti-hrace) · [Animace řídí svět: křivky v montáži](praxe/interakcni-animace.md#animace-ridi-svet-normalizovane-krivky-v-montazi) · [Útok je časová osa](praxe/souboj.md#utok-je-casova-osa-montaz-okna-z-notify-a-stav-ktery-se-musi-vratit) · [Útok za běhu](praxe/souboj.md#utok-za-behu-horni-pulka-bojuje-dolni-bezi-a-krivka-rekne-kdy-ne)

### Animation cancel

**Přerušení probíhající animace jinou akcí; v akčních hrách zdroj většiny pokročilých technik.**

Technický předpoklad je jediný: **efekt, který má dohrát, nesmí být dítětem věci, která se může přerušit.** Rozmazaný pruh za mečem přehrávaný jako samostatná animace dohraje i tehdy, když se útok postavy zruší dopadem — a z opravy vizuální vady se rázem stane prostor pro dovednost: dash z útoku, skok z útoku, combo přes zrušení dopadem. Zvedá to [skill ceiling](#skill-ceiling), protože hráč, který se naučí rušit ve správný okamžik, získává tempo.

Kde se s tím potkáš: [Útočit v pohybu, nebo se zastavit](godot/pripadovka-pohyb.md#utocit-v-pohybu-nebo-se-zastavit)

### Anim Notify

**Značka na časové ose animace, která v daném framu spustí logiku — zvuk, efekt, gameplay event.**

Vestavěné (Play Sound) i vlastní blueprint třídy (override Receive Notify) s instance editable parametry — notify pak nese data (která noha, který moment hodu). Notify state je varianta s trváním (od–do framu): motion warping okna, Pose Search Branch In. Pozor v blend space: Notify Trigger Mode default spouští jen nejváženější animaci.

Vlastní notify state z `AnimNotify_PlayMontageNotifyWindow` udělá z okna comba nebo z active frames značku v timeline, kterou kód poslouchá přes On Notify Begin/End uzlu `Play Montage`. Jména se párují přes `Switch on Name` a musí sedět přesně.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Interakce s předměty](praxe/interakce-predmety.md) · [Systémy nad MM](praxe/mm-systemy.md) · [Jedna animace zvednutí: notify OnGrab](praxe/interakcni-animace.md#jedna-animace-zvednuti-pro-vsechno-grip-pointy-a-pozy-ruky) · [Zápas se smyčkou](praxe/interakcni-animace.md#zapas-se-smyckou-sekce-montaze-a-rozhodnuti-hrace) · [Okna comba z notify state](praxe/souboj.md#utok-je-casova-osa-montaz-okna-z-notify-a-stav-ktery-se-musi-vratit) · [Hitbox: impact frame a active frames](praxe/souboj.md#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames)

### Apofenie

**Lidský pud vidět vzory a příběhy i tam, kde nikdo žádný nenapsal — motor emergentního narativu.**

Dej hráči reprezentace, postavy a situace, a příběh si složí v hlavě sám (model, na kterém stojí RimWorld). Pro designéra to znamená, že narativ nemusí být autorský text: stačí systémy, jejichž srážky stojí za převyprávění.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Apply Damage

**Vestavěný systém poškození v UE: útočník zavolá `Apply Damage` (nebo `Apply Point Damage`), terč dostane `Event Any Damage` (nebo `Event Point Damage`).**

Terč musí mít v Class Defaults zapnuté `Can Be Damaged`; jeho vypnutím se dá dočasně udělat nezranitelným. Point Damage nese i hit result, takže terč ví, kam rána dopadla, a může spočítat směr reakce. Komponenta, která vlastní event nemá, se přihlásí k delegátu vlastníka `OnTakePointDamage`. Kolikrát smí jeden útok zasáhnout tentýž cíl, musí hlídat útok sám.

Kde se s tím potkáš: [Damage jednou za útok](praxe/souboj.md#damage-jednou-za-utok-seznam-zasazenych-patri-utoku-ne-terci) · [Terč: směr rány](praxe/souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave) · [Kostra pasti](praxe/pasti-a-mechaniky.md#kostra-pasti-a-tri-variace-bodaky-rameno-rotor) · [Hádanka ze stavebnice](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit)

### Arrangement

**Rozvinutí hudebního loopu do celé skladby — kdy co přidat, ubrat a jak přejít (aranžmá).**

Nejčastější past je „loop trap": pěkný loop, ale nevíš, jak z něj udělat píseň. Pomáhá pravidlo dvou loopů (nejvýš dvě změny na dvě opakování) a vědomí, že píseň žije v přechodech mezi sekcemi.

Kde se s tím potkáš: [Aranžmá: z loopu skladba](hudba/aranz.md)

### Art bible

**Dokument vizuálního jazyka hry: moodboardy, palety, reference a pravidla stylu.**

Vzniká paralelně s gameplay prototypem jako samostatná linka práce — a ve vertical slice se poprvé potká s mechanikami a příběhem. V minimalistickém GDD ji zastupuje pár referenčních obrázků s vytaženou paletou; vlastní dokument si zaslouží, až se tým rozroste nebo styl ustálí.

Kde se s tím potkáš: [GDD](teorie/gdd.md) · [Prototypování](teorie/prototypovani.md) · [Herní art: concept art](teorie/art-pipeline.md)

### Anim Budget Allocator

**Plugin, který rozděluje pevný rozpočet na animace mezi skeletal meshe podle významnosti.**

Funguje z krabice se spravovanými skeletal mesh komponentami a dá se do něj dopsat vlastní výpočet priority — typicky aby hlavní tvorové či postavy **nikdy** nedostali osekané ticky, zatímco kulisa v dálce ano. Nasadit ho stojí za to **hned na začátku**: zpětné doplnění vyžaduje přerodičování a je nepříjemné. Bývá to nejnižší patro delšího žebříku: budget → zjednodušené behavior tree → pohybující se statický mesh → statický mesh.

Kde se s tím potkáš: [Animace ve velkém](praxe/velke-svety.md#animace-ve-velkem-od-tiku-k-udalostem) · [Rejstřík: Mass Entity](#mass-entity) · [Bojovka pro desetiletý hardware](praxe/gpu-pruchod.md#bojovka-pro-desetilety-hardware-rozpocet-po-castech-a-co-se-v-nem-naslo)

### Aspirační obtížnost

**Jak těžké je uspět DOBŘE: lepší cesta, víc bodů, volitelná hloubka — obtížnost, po které hráč sahá sám.**

Protipól průběžné obtížnosti (jak moc tě hra tlačí k prohře). Jahody v Celeste jsou učebnice: místo hard módu zvoleného předem se hráč rozhoduje v každém okamžiku, jestli si troufne na těžší verzi. Aspirační obtížnost vyrábí pocit dobře odvedené práce.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Assist mode

**Volitelný režim, který dovolí hráči upravit si obtížnost po jednotlivých pákách místo výběru „easy".**

Rozdíl proti posuvníku obtížnosti je v kontrole: hráč nedostane „hraju na lehkou a nevím, co to znamená", ale konkrétní volby — víc života, nižší poškození, pomalejší čas. Vzniklo to jako přístupnostní nástroj (někdo nezvládne mačkat dost rychle, aby porazil bosse v limitu) a používá se i obráceně — jako sada dobrovolných ztížení pro ty, co si o ně řeknou. Elegantní implementace je přes systém, který už ve hře je: [odznaky](godot/pripadovka-systemy.md#odznaky-odmena-ktera-nezlehci-hru) v assist režimu prostě dovolí hodnoty, které by jinak byly příliš silné.

Kde se s tím potkáš: [Odznaky: odměna, která nezlehčí hru](godot/pripadovka-systemy.md#odznaky-odmena-ktera-nezlehci-hru) · [Obtížnost a výzva](teorie/obtiznost.md)

### Async compute

**Druhá fronta GPU, která umí jen compute shadery a běží souběžně s grafickou.**

Fronty sdílejí výpočetní jednotky a synchronizují se přes fences — z čehož vznikají **bubliny**: fronta stojí, protože čeká na signál z druhé. Praktický důsledek pro čtení profileru: vysoký *wait* na compute frontě je normální a sám o sobě není chyba, na grafické frontě by měl být blízko nule. A při měření konkrétního průchodu se async compute vyplatí vypnout (`r.RDG.AsyncCompute 0`), protože překrývající se práce zkresluje časy obou front.

Kde se s tím potkáš: [Busy, wait, idle](praxe/gpu-pamet.md#busy-wait-idle-co-rika-novy-gpu-profiler) · [Rejstřík: RHI](#rhi)

### Asset pack

**Balík hotových assetů — modely, zvuky, UI, shadery — připravený k okamžitému použití.**

Pro sólo vývojáře nástroj přežití: 50 hodin vlastního lokalizačního toolkitu vs. hotový asset za pár desítek dolarů je reálná volba z praxe. Kupuje se to, co dělat neumíš nebo nechceš; vlastní ruce si šetři na to, čím se hra liší. Při prototypování asset packy dodají vizuál a vibe za nulový čas — a u „design by constraint" umí být rovnou zdrojem nápadu („šla by kolem tohohle jediného assetu postavit hra?").

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Nápad](teorie/napad.md) · [Scope](teorie/scope.md)

### Asset User Data

**Data pověšená přímo na asset (typicky na static mesh), která s ním cestují, kdekoli se použije.**

Řeší rozpor velkých světů: gameplay chce bohatá data, výkon chce hloupé objekty — a udělat ze sta tisíc objektů blueprinty nejde. Typický obsah: typ povrchu, data pro skener, gameplay tagy, příznaky pro AI. Hledá se v řetězu priorit **blueprintová komponenta → root komponenta → mesh**, takže se dá kdykoli přebít výš. Cena: data nejsou vidět v blueprintu ani v outlineru, takže k nim patří nástroj, který vypíše, co který mesh nese.

Kde se s tím potkáš: [Gameplay na meshi bez blueprintu](praxe/velke-svety.md#gameplay-na-meshi-bez-blueprintu) · [Rejstřík: Gameplay tag](#gameplay-tag) · [Rejstřík: Data asset](#data-asset)

### Astroturfing

**Marketing, který předstírá, že vznikl zdola z komunity, i když ho platí firma.**

Termín z politiky (astroturf je umělý trávník — falešná „grassroots"). V herním kontextu se tak označuje snaha velkého vydavatele vypadat jako indie: cílit na estetiku, tón a hodnoty nezávislé scény bez odpovídajícího produkčního kontextu. Indie publikum na to reaguje citlivě právě proto, že u něj jde o hodnotový systém, ne jen o vkus.

Kde se s tím potkáš: [Indie kariéra](teorie/indie-kariera.md#kdy-indie-hra-neni-indie-hra)

### Async Physics

**Režim, ve kterém fyzika běží s pevným krokem na vlastním vlákně, zatímco hra tiká proměnlivě.**

Zapíná se v Project Settings (Enable Async Physics) i s délkou kroku. Herní vlákno na výsledek nečeká a interpoluje mezi posledními dvěma kroky fyziky, takže je vždy o kousek pozadu, nanejvýš o dva kroky. Pevný krok je podmínkou skoro deterministické simulace, a tedy síťové fyziky. Logika, která na fyziku sahá, musí běžet na fyzikálním vlákně.

Kde se s tím potkáš: [Chaos Mover](praxe/mover.md#chaos-mover-postava-jako-fyzikalni-teleso-se-stropem-sily) · [Síťová fyzika zevnitř](praxe/mover.md#sitova-fyzika-zevnitr-snimky-misto-casu-resimulace-a-input-decay) · [Buoyancy na fyzikálním vlákně](praxe/destrukce-a-latky.md#budova-kterou-rozbije-kdokoli-graf-spojeni-na-serveru-cluster-union-ve-fyzice)

### Attachment rules

**Pravidla, podle kterých `Attach Actor to Component` naloží s polohou, rotací a měřítkem připínaného objektu — Snap to Target, Keep Relative, nebo Keep World.**

Snap to Target spojuje dvě rozhodnutí: připnout (objekt se dál hýbe s rodičem) a okamžitě přesunout na cíl, typicky [socket](#socket). Keep World připne, ale nechá objekt vizuálně tam, kde byl; zbytek cesty pak může dorovnat krátký lerp. Proto předmět při zvednutí nemusí „skočit" do ruky. Pravidla se nastavují zvlášť pro polohu, rotaci a měřítko.

Kde se s tím potkáš: [Předmět do ruky bez teleportu](praxe/interakcni-animace.md#predmet-do-ruky-bez-teleportu-attach-neni-snap-a-dosah-neni-dohled) · [Jedna animace zvednutí](praxe/interakcni-animace.md#jedna-animace-zvednuti-pro-vsechno-grip-pointy-a-pozy-ruky)

### Attenuation

**Útlum hlasitosti zvuku se vzdáleností od zdroje.**

Ve stealth hrách často vizualizovaný v UI. Trik: dej vysokým frekvencím krátký útlum a nízkým dlouhý — zblízka je výstřel ostrý, z dálky jen temné dunění.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Attenuation radius

**Poloměr, za kterým světlo v Unrealu přestane svítit, ať je jakkoli silné.**

Uvnitř objemu se světlo počítá celé, i tam, kam už viditelně nedosvítí, a proto je zbytečně velký radius čistá ztráta. Nové světlo má 1000 cm. S MegaLights je počet radiů, která se překrývají na jednom místě, hlavní metrikou kvality, protože si pixel dělí vzorky mezi všechna světla, která na něj dosáhnou. Jak daleko světlo vypadá, že svítí, závisí i na expozici, a proto se radius ladí od oka v hotové scéně. Neplést s [Attenuation](#attenuation) u zvuku.

Kde se s tím potkáš: [Attenuation radius jako hlavní páka](praxe/megalights.md#attenuation-radius-jako-hlavni-paka-pocitej-prekryvy-ne-svetla) · [Rozpočet vzorků na pixel](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis) · [Rejstřík: MegaLights](#megalights)

### AutoBake

**Funkce sequenceru (5.8), která jedním přepínačem střídá živý control rig a jeho zapečenou animation sequence.**

Po nastavení (pravým na actor → Add AutoBake) přidá zapečenou verzi a ztlumí ji; ikona pak přepíná a změněnou animaci rychle přepeče. Výběr controlu vrátí postavu do živého rigu, ostatní postavy zůstanou zapečené, takže viewport s víc postavami zůstane rychlý. U fyziky (s warm-up snímky na usazení) dává deterministický výsledek, který jde scrubovat a pustit na něj motion trails.

Kde se s tím potkáš: [Sekundární pohyb v Control Rigu](praxe/animace-nastroje.md#sekundarni-pohyb-v-control-rigu-dynamics-za-behu-fyzika-a-autobake-pri-animovani) · [Rejstřík: Control Rig](#control-rig)

### Auto exposure

**Automatická expozice (eye adaptation): engine podle jasu obrazu posouvá expozici, jako když si oko zvyká na tmu nebo na světlo.**

Nastavuje se v post-process volume rozsahem minima a maxima v EV, rychlostí a kompenzací expozice. Pomůže tam, kde hra přechod opravdu potřebuje, třeba při výstupu z tmavého krytu na slunce. Ve scéně s řízeným světlem bývá lepší expozici zamknout nebo jí hodně zúžit rozsah, aby se světlo dalo kalibrovat. Záře, která po zhasnutí světla chvíli zůstane, bývá temporální akumulace, ne adaptace. Emisiv jde vydělit hodnotou adaptace, aby jeho jas zůstal v rozumném rozsahu.

Kde se s tím potkáš: [Expozice, která drží](praxe/megalights.md#expozice-ktera-drzi-kalibrace-local-exposure-a-dva-modely-svetla) · [Attenuation radius jako hlavní páka](praxe/megalights.md#attenuation-radius-jako-hlavni-paka-pocitej-prekryvy-ne-svetla) · [PBL: svítit podle skutečných hodnot](praxe/osvetleni.md#pbl-svitit-podle-skutecnych-hodnot) · [Rejstřík: Local exposure](#local-exposure)

### Autoload

**Scéna nebo skript zaregistrovaný jako globální — načte se sám a přežije výměnu scén.**

Zdejší podoba singletonu: v nastavení projektu zaregistruješ scénu a Godot ji drží naživu bez ohledu na to, která scéna zrovna běží. Typické použití je hudba (jinak se restartuje při každém načtení levelu), skóre, audio mixer a save data. Platí na něj tytéž výhrady jako na každý globální stav — skvělý sluha, špatný pán: jakmile se z autoloadu stane odkladiště pro všechno, co se nehodí jinam, máš [God class](#god-class).

Kde se s tím potkáš: [První hra: AnimationPlayer jako časovač](godot/prvni-hra.md#animationplayer-jako-casovac-sekvence-bez-jedineho-radku-kodu) · [Godot: co si přinést, než otevřeš editor](godot/zaklady.md#co-si-prinest-nez-otevres-editor)

### Biome Core

**Data-driven nástroj nad PCG pro stavbu biomů; je mocný, ale náročný na znalosti.**

Epic k němu napsal skill, takže agent zná jeho datové struktury a umí biom postavit od nuly. Je to dobrý příklad, kdy model nestaví novou věc, ale pomáhá ovládat systém, který už funguje.

Kde se s tím potkáš: [Asistent, ne zázrak](praxe/mcp-v-editoru.md#asistent-ne-zazrak-slovnik-priklady-a-skills-delaji-z-llm-stavitele-sveta) · [Rejstřík: PCG](#pcg) · [Rejstřík: Agent skill](#agent-skill)

### Biome map

**Barevná mapa přes celý terén, kde každá barva označuje jeden biom a řídí, co se kde rozmístí.**

Nejjednodušší je namalovat ji přes screenshot terénu shora v libovolném grafickém editoru, složitější mapy vznikají v nástrojích na stavbu světa. Musí na terén sedět přesně, jinak scatter roste vedle. Scatter každého biomu pak čte jen svou barvu. V ukázce s nástrojem QuickScatter doporučuje autor textuře mapy zapnout Never Stream, protože jinak se mu po znovuotevření levelu sama nenačítala.

Kde se s tím potkáš: [Les pro otevřený svět](praxe/pcg-vegetace.md#les-pro-otevreny-svet-co-se-nacte-s-levelem-a-co-roste-kolem-hrace)

### Blend Poses by Bool

**Anim uzel, který podle boolu přepíná mezi dvěma pózami — „if" v anim grafu.**

Klasicky rozhoduje, jestli se útok vrství přes locomotion (v pohybu), nebo hraje celé tělo (ve stoje), případně jestli postava právě útočí (`IsAttacking`). Podmínka se dá skládat z víc vstupů: pohyb, vzduch, hodnota křivky z animace.

Kde se s tím potkáš: [Útok za běhu](praxe/souboj.md#utok-za-behu-horni-pulka-bojuje-dolni-bezi-a-krivka-rekne-kdy-ne) · [Combat nad MM](praxe/mm-systemy.md#combat-nad-mm-horni-telo-v-montazi-spodni-v-matchingu)

### Blueprint Debugger

**Ladění blueprintů přímo v editoru za běhu hry: breakpointy, sledované hodnoty a zastavení při chybě.**

Pravý klik na pin → *Watch this value* a v toolbaru vybrat ladicí objekt — hodnota pak běží přímo v grafu. Breakpoint zastaví hru na uzlu a dovolí krokovat; volba v Editor Preferences → Experimental zastaví blueprint automaticky na uzlu, kde nastala výjimka (třeba index mimo pole), místo aby hra běžela dál a chyby se objevily až v logu. Rychlejší než archeologie s print stringem, jakmile víš, kterou hodnotu hledáš.

Kde se s tím potkáš: [Ladění: čtyři otázky, čtyři nástroje](praxe/debugging.md#ctyri-otazky-ctyri-nastroje-od-print-stringu-po-visual-logger) · [Nářadí z workshopu](praxe/principy-architektury.md#naradi-z-workshopu-kde-co-bydli-a-jak-se-to-hybe)

### Blueprint Macro

**Znovupoužitelný kus Blueprint grafu, který se rozbalí na místě volání — na rozdíl od funkce smí obsahovat latentní uzly jako Delay a mít víc exec vstupů i výstupů.**

Hodí se tam, kde má volající počkat, než se něco dokončí: zatmívačka kamery před cutscénou (start fade, Delay stejné délky, teprve pak výstup) se do funkce nevejde, protože funkce Delay obsahovat nemůže. Pro jednorázovou čekací logiku stačí i custom event; makro se vyplatí, když se stejný latentní kus opakuje.

Kde se s tím potkáš: [Cutscéna, která vrátí hru tam, kde skončila](praxe/cutsceny.md#cutscena-ktera-vrati-hru-tam-kde-skoncila)

### B-roll

**Doplňkové záběry, které běží na obrazovce, zatímco mluvíš o něčem obecnějším — ve videích o hrách typicky záběry gameplaye.**

Pravidlo devlogů: na obrazovce má být hra, pořád — ideálně přesně to, o čem zrovna mluvíš, jinak aspoň obecný B-roll. Chytrý zdroj záběrů starších verzí hry: version control — checkout starého commitu a natoč, co potřebuješ.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md)

### Backbeat

**Rytmický důraz na sudé doby taktu — na dvojky a čtyřky.**

Je to místo, kam v drtivé většině populární hudby patří snare a clap. V žebříčku síly dob stojí pod downbeatem a ostatními čtvrťovými, ale nad offbeatem — a právě proto funguje: je dost silný, aby se o něj dalo opřít, a dost odlišný od kopáku, aby se s ním nepral.

Kde se s tím potkáš: [Silné a slabé doby](hudba/rytmus.md#silne-a-slabe-doby-pater-a-ozdoby) · [Rejstrik: Synkopa](#synkopa)

### Backlog

**Zásobník všeho, co projekt čeká: úkoly i nezralé nápady — priority se z něj tahají po dávkách.**

Dvojí užitek: nápady se parkují místo zabíjení (secret sauce poznáš často až za měsíc) a rozhodování o nich se přesouvá z emocí brainstormu na pravidelný rytmus — sprint meeting nebo měsíční blok, kde se seznam projde proti pilířům hry. Na dlouhém projektu je backlog nejdelší sloupec kanban boardu.

Kde se s tím potkáš: [Scope: scope creep](teorie/scope.md) · [Plánovací nástroje](teorie/planovani-nastroje.md)

### Backpressure

**Když producent chrlí rychleji, než konzument stíhá: nebufferuj, nezahazuj — propaguj tlak zpět, ať producent zpomalí.**

Naivní odpovědi na přetíženou frontu jsou buffer (odloží problém) a drop (ztratí data). Backpressure místo toho zpomalí zdroj na kapacitu spotřebiče — systém pak pod zátěží degraduje elegantně místo pádu. Ve hrách: spawn throttling, fronty eventů, streaming assetů.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Barbell strategie

**Rozdělení sázek na dva krajní póly — velmi bezpečné a velmi riskantní — místo průměru uprostřed.**

Pojem Nassima Taleba pro prostředí, kde platí mocninné rozdělení: střední cesta tam kombinuje nejhorší z obou světů. V praxi indie studia to znamená držet stabilní základ (práce, úspory, backlog malých her) a z něj dělat odvážné, potenciálně obrovské sázky — ne dělat jednu opatrně průměrnou hru.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#extremistan-tri-mechanismy-ktere-vedou-ke-stejne-strategii) · [Přežít jako studio](teorie/prezit-jako-studio.md#ctyri-roky-bez-hitu-financovani-riziko-a-runway)

### Barrier to play

**Překážka, se kterou hráč zápasí, ačkoli ji designér testovat nechtěl: překomplikované ovládání, informace jen barvou.**

Derek Yu (Spelunky): hráč chtěl „odstranit síť", protože nepřehodil míč — a přitom dostal „raketu s prasklým výpletem". Dokud má hra bariéry, nelze ladit obtížnost ani měřit, jestli výzva baví: hráč nebojuje s výzvou, ale s rozhraním.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Behavior Tree

**Klasický rozhodovací strom AI v UE: selectory a sequence uzly volí tasky podle podmínek z Blackboardu.**

Strom běží na AI controlleru a čte sdílenou tabuli (Blackboard); decoratory hlídají podmínky a s „observer aborts" přerušují běžící větve při změně dat. Vlastní tasky se píší v blueprintu (Receive Execute AI → Finish Execute). Pro nové projekty Epic tlačí State Trees — koncepty se ale přenášejí.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [AI vnímání](praxe/ai-vnimani.md) · [AI, která nereaguje](praxe/debugging.md#ai-ktera-nereaguje-gameplay-debugger-a-dve-tiche-priciny) · [Strom jen rozhoduje](praxe/ai-ve-velkem.md#strom-jen-rozhoduje-akce-v-gameplay-abilitach-nepritel-v-datech) · [Reakce vedle stromu](praxe/ai-ve-velkem.md#reakce-vedle-stromu-co-se-muze-stat-v-kazdem-stavu-nepatri-do-zadne-vetve)

### Beta

**Pozdní testovací verze hry: obsahově víceméně celá, ladí se balanc, bugy a onboarding.**

Na Steamu jde veřejnou betu spustit přes playtest feature — a vyplatí se z ní udělat marketingový beat: „hratelná beta" je zpráva, kterou novináři a tvůrci obsahu můžou předat dál. Po veřejné vlně se testování často zase zužuje na uzavřené kolo s fokusovanými otázkami.

Kde se s tím potkáš: [Playtesting: škálování](teorie/playtesting.md) · [Steam stránka](teorie/steam-stranka.md)

### Blackboard

**Sdílená tabule AI: pojmenované klíče (vector, object, bool…), přes které si percepce, tasky a strom předávají data.**

Klíč typu Object→Actor umí Move To průběžně sledovat (žádné přepočítávání cíle); Blackboard decorator větví strom podle „Is Set / Is Not Set" a observer aborts okamžitě přepne chování při změně. Zápis z blueprintu: Set Blackboard Value as Bool/Vector/Object — jméno klíče musí sedět do písmene.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [AI vnímání](praxe/ai-vnimani.md) · [AI, která nereaguje](praxe/debugging.md#ai-ktera-nereaguje-gameplay-debugger-a-dve-tiche-priciny)

### Blend Space

**Asset, který míchá animace podle hodnot na osách grafu — 1D (rychlost) nebo 2D (rychlost × směr).**

Klipy se rozmístí na osu (idle 0, walk 300, run 600…) a vstupní hodnota určuje mix. Klipy různých délek synchronizují sync markery — bez nich se kroky rozjedou. Blend spacy jdou vkládat i do Motion Matching databází a GASP animace jsou na to fázovány.

Kde se s tím potkáš: [Základy pohybu](praxe/pohyb-zaklady.md) · [MM základy](praxe/mm-zaklady.md) · [Svahy jako blend space v chooseru](praxe/gasp.md#motion-matching-uvnitr-chooseru-pose-match-sloupec-databaze-na-radek-a-blend-space-ve-stacku) · [Pózy ragdollu](praxe/ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu)

### Blend stack

**Anim uzel, který při každé změně animační proměnné přidá nový blend do zásobníku — bez state machine.**

Základ, na kterém Motion Matching stojí: uvnitř MM uzlu běží graf per vybraná animace (tam žije orientation warping, steering…). Varianty: obyčejný blend stack (animace z proměnné), Chooser Player (animace z chooser tabulky, umí i stitch) a hybridní setup se state machine. Max počet současných blendů je konfigurovatelný.

Blend stack umí přehrát i blend space vybraný chooserem; jeho osy krmí vstup blend parameters. S nastavením Blend Space Update Mode = Update Active Only se aktualizuje jen nejnovější animace ve stacku, aby dva blend spacy s jinými osami nedostaly stejná data.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Blend space ve stacku](praxe/gasp.md#motion-matching-uvnitr-chooseru-pose-match-sloupec-databaze-na-radek-a-blend-space-ve-stacku)

### Blockout

**Hrubá stavba levelu z primitivních tvarů — testuje prostor, metriky a flow dřív, než přijdou finální assety.**

Blockout disciplína: grid/metrické materiály (okamžitě vidíš, že vchod je úzký nebo skok dlouhý), konzistentní barevný jazyk (cover jedna barva, traversal jiná) a „level design gym" — referenční mapa metrik sdílená napříč levely. Startovní bod hráče a hlavní landmark se rozhodují ještě před blockoutem.

Z pohledu environment artu je blockout polovina projektu: rozhoduje o čitelnosti, siluetě a měřítku. Pomáhá test přimhouřených očí a postava ve scéně od prvního dne. Pipeline Naughty Dog ho dotahuje přes průchod hodnot a barvy, ještě než vznikne první materiál.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Prototypování](teorie/prototypovani.md) · [Blockout: zastav, omez, porovnej](praxe/blockout.md#zastav-omez-porovnej-blockout-ktery-se-da-precist) · [Hybridní blockout](praxe/blockout.md#hybridni-blockout-hodnoty-a-barva-driv-nez-materialy) · [Od blockoutu ke kitu](praxe/modularni-kity.md#kit-jako-lego-co-nejmene-kusu-mrizka-v-metrech-a-zoo-na-zkousku)

### Beautiful corner

**Jeden malý kus hry dotažený do cílové kvality, zatímco zbytek zůstává v grayboxu.**

Mikroverze vertical slice: jedna místnost nebo jeden výjev jako art prototyp, podle kterého se pozná, kam hra míří vizuálně — aniž bys zabetonoval celý projekt. Řeší napětí mezi „drž iterační cykly krátké" a „potřebuju vidět, jak to bude vypadat"; sólo vývojáři navíc slouží jako legitimní odměna, která drží chuť do práce.

Kde se s tím potkáš: [Level design pro sólo vývojáře](teorie/level-design-solo.md) · [Prototypování](teorie/prototypovani.md)

### Blue ocean

**Trh bez konkurence: hra vytváří novou poptávku, místo aby se prala o etablované publikum (red ocean).**

Termín z byznys strategie: red ocean = přeplněné žánry, kde rozhodují zdroje (battle royale, souls-like); blue ocean = unikátní zážitek, který si publikum teprve vyrobí (Minecraft, Undertale). Pro indie bez rozpočtu velkých studií je modrý oceán — unikátní twist — obvykle lepší sázka.

Kde se s tím potkáš: [Sólo vývoj](teorie/solo-vyvoj.md) · [Nápad](teorie/napad.md)

### Blueprint Function Library

**Sbírka funkcí volatelných z libovolného blueprintu v projektu.**

Ideální pro helper funkce, které nepatří žádné konkrétní třídě: bezpečný přístup ke gameplay tag containeru libovolného actora, pure getter na Game Instance, zápis aktivit. Pure funkce bez side effectů se v grafu chovají jako čisté dotazy. Pravidlo: co voláš ze tří míst, patří do funkce; co voláš ze tří blueprintů, patří do library.

Kde se s tím potkáš: [Gameplay Tags](praxe/gameplay-tags.md) · [Ukládání](praxe/ukladani.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Blueprint Interface

**Sada deklarovaných funkcí bez implementace — kontrakt, který si každý Blueprint naplní po svém.**

Volající posílá zprávu (message call) na libovolný actor; pokud actor interface implementuje, zareaguje vlastní logikou, pokud ne, nestane se nic — žádný pád, žádná závislost. Je to enginová podoba principu „programuj proti rozhraní": character nemusí znát třídu dveří, truhly ani panelu, stačí mu smlouva „umíš interagovat?". Přidání nového typu interaktivního objektu pak neznamená žádnou změnu ve volajícím.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md) · [Objekt ví, jak se s ním zachází](praxe/interakcni-animace.md#objekt-vi-jak-se-s-nim-zachazi-data-interakce-patri-k-veci-ne-k-postave) · [Hádanka ze stavebnice](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit)

### Boids

**Algoritmus hejna (Reynolds, 1986): tři lokální pravidla — separation, alignment, cohesion — a chování hejna emerguje samo.**

Každý agent se vyhýbá tlačenici, srovnává směr s okolím a drží se těžiště sousedů; výsledné vzory hejna nikdo nenaprogramoval. Učebnicový příklad emergence: komplexní chování se levněji pěstuje z jednoduchých pravidel, než skriptuje. Základ ptáků, ryb i davů ve hrách.

Kde se s tím potkáš: [Algoritmy, které stojí za to znát](teorie/algoritmy-prehled.md)

### Boolean

**Geometrická operace kombinující dvě tělesa: sjednocení (union), rozdíl (subtract), průnik (intersect).**

Pojmenováno po booleovské logice — tělesa se skládají jako množiny bodů. V Mesh Terrainu boolean modifier skutečně vroubuje cizí mesh do terénu: union přiroste, subtract vyřízne díru a geometrie se na okrajích sešije. Klasický nástroj CSG modelování (Constructive Solid Geometry), který znáš z Blenderu i CADů.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Blok napřed, silnice potom](praxe/pcg-mesta.md#blok-napred-silnice-potom-block-processor-a-booleany) · [Ostrov z booleanů](praxe/mesh-terrain.md#modifikatory-v-rukou-epicu-poradi-vrstev-rovina-pod-poi-a-pcg-ktere-rozmistuje-skaly)

### Bounds

**Osově zarovnaný obal (kvádr) kolem objektu či bodu — levná aproximace „kolik místa věc zabírá".**

Ve fyzice a tracingu zrychlují testy, v PCG jsou bounds bodů přímo pracovní data: Difference vyřezává podle nich (přesněji to umí kolizní data), Self Pruning jimi měří překryvy a bounds modifier je nafukuje či zmenšuje jako ladicí páku. Get Actor Bounds vrací obal celého actora — základ zarovnávání na neznámé meshe.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md) · [Parkour postaru](praxe/parkour-vault.md) · [Bounds Scale: culling drobných propů](praxe/gpu-pruchod.md#bojovka-pro-desetilety-hardware-rozpocet-po-castech-a-co-se-v-nem-naslo)

### BPM

**Tempo skladby v dobách za minutu (beats per minute); ukotví žánr dřív než noty.**

Lo-fi kolem 77, house 120–130, drum and bass kolem 170. Pro náladu scény je tempo první páka — energii nastavíš dřív, než vybereš jediný akord.

Kde se s tím potkáš: [Žánry a jejich melodie](hudba/zanry-a-styl.md)

### BRDF

**Model odrazu světla od povrchu — matematický základ toho, jak materiál vypadá.**

Bidirectional Reflectance Distribution Function popisuje, kolik světla se odrazí kterým směrem podle úhlu pohledu a dopadu. V praxi ho artista potkává jako sadu vstupů (base color, roughness, metallic, normal) a jako rozpad, na kterém se dá ladit jednotlivá složka zvlášť. Podle artistů Naughty Dog je nejpodceňovanější z nich roughness.

Kde se s tím potkáš: [Breakdowny: Naughty Dog](praxe/env-breakdowny.md#naughty-dog-shadery-misto-polygonu-a-nastroj-misto-modelovani) · [Rejstřík: PBR](#pbr)

### Building in public

**Stavět veřejně: průběžně ukazovat pokrok, rozhodnutí a zdi, na které narážíš — ne až hotový výsledek.**

Funguje dvakrát: jako disciplína (když je pokrok vidět, skončení přestává být neviditelné — v datech jedné výzvy přežívali skoro výhradně ti, kdo postovali buildy) a jako důkaz (veřejný záznam toho, jak myslíš, se nedá nafejkovat promptem). Nejcennější je sdílet uvažování, ne screenshoty úspěchů.

Kde se s tím potkáš: [Produktivita](teorie/produktivita.md) · [Učení v éře AI](teorie/uceni-v-ere-ai.md)

### Buoyancy

**Vztlak: systém Water pluginu, který nechá simulovaná tělesa plavat na vodních tělesech.**

Dvě cesty: klasicky Buoyancy komponenta s pontoony (body vztlaku — 4 rohy lodi; debug `r.water.debug.buoyancy 1`), od 5.7 stačí Physical Material Override → Default Buoyancy Physics Material + na water body kolize Query and Probe s Block na Physics Body. Objekt musí startovat nad hladinou a simulovat fyziku; ladí se mass, damping, center of mass.

Kde se s tím potkáš: [Voda a buoyancy](praxe/voda-a-buoyancy.md) · [Nástroje: EasyWaterscape](praxe/nastroje-voda.md)

### Burn rate

**Kolik peněz projekt nebo firma spálí za měsíc či rok, bez ohledu na příjmy.**

Základní číslo pro plánování: vynásobené délkou vývoje dá celkovou cenu projektu. U jednoho známého desetiletého indie projektu činí 1,8 až 4,4 milionu dolarů ročně; u tříčlenného studia může jít o zlomek toho. Spolu s [runway](#runway) tvoří dvojici, která rozhoduje o tom, jestli má smysl začínat velkou hru.

Kde se s tím potkáš: [Indie kariéra](teorie/indie-kariera.md#ekonomika-desetileteho-projektu) · [Přežít jako studio](teorie/prezit-jako-studio.md#ctyri-roky-bez-hitu-financovani-riziko-a-runway)

### Cable Component

**Vestavěná komponenta simulovaného lana/kabelu — fyzika z krabice, konce jdou ukotvit na objekty.**

Ladí se délka, počet segmentů (hladkost), tuhost, šířka a počet stran renderu (default 4 vypadá hranatě) + tile material. Váže se k pivotu cílového objektu — typicky doladit Z offset. `Get Cable Particle Locations` vrací body simulace, na které jdou věšet instancované meshe (girlandy, řetězy). Nosnou fyziku ale dělá physics constraint — kabel je vizuál.

Kde se s tím potkáš: [Kabely, lana a Physics Control](praxe/lana-kabely.md)

### Cached pose

**Póza z anim grafu uložená pod jménem (`Save Cached Pose`), kterou jde použít na víc místech (`Use Cached Pose`).**

Výstup uzlu v anim grafu jde zapojit jen do jednoho vstupu. Kdo potřebuje tutéž locomotion jako základ vrstvy i jako samostatnou větev, uloží ji do cache. Typické je to u vrstvení útoku přes Layered Blend Per Bone, kde se locomotion i póza se slotem rozvádějí do několika uzlů.

Kde se s tím potkáš: [Útok za běhu](praxe/souboj.md#utok-za-behu-horni-pulka-bojuje-dolni-bezi-a-krivka-rekne-kdy-ne) · [Rejstřík: Layered Blend Per Bone](#layered-blend-per-bone)

### Cache miss

**Procesor potřebuje data, která nemá v cache, a čeká na hlavní paměť — ve hrách častější brzda než samotné výpočty.**

Paměť se do cache načítá po celých řádcích (cache lines), takže rozhoduje, kolik z načteného řádku opravdu použiješ. Objektový kód skáče po pointerech (actor → seznam komponent → hledání podle typu → virtuální metoda) a každý skok je pravděpodobně miss; přednáška o Mass v takovém kódu napočítá kolem sta dereferencí kvůli jediné hodnotě. Proto větší cache hru zrychlí jen málo — a proto [data-oriented design](#data-oriented-design) skládá data, se kterými se pracuje spolu, za sebe.

Kde se s tím potkáš: [Proč objekty zpomalují](praxe/mass-ecs.md#proc-objekty-zpomaluji-pamet-kterou-nactes-a-zahodis) · [Entita není actor: malé fragmenty](praxe/mass-ecs.md#entita-neni-actor-rozkladej-podle-pristupu-do-pameti-ne-podle-postavy) · [Rejstřík: ECS](#ecs)

### Call to action

**Závěrečná výzva trailer u nebo videa: co má divák udělat teď — „Wishlist on Steam", „Demo out now".**

Formát pro herní trailer: 5–8 vteřin na konci, key art + název + jedna výzva. Právě jedna — dvě CTA najednou („demo + wishlist") si konkurují a oslabují se. V širším marketingu platí totéž pro každý kanál: post, devlog i stránka mají mít jeden jasný další krok.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Call down, signal up

**Pravidlo palce pro komunikaci ve stromu scény: rodič smí volat funkce na dětech, dítě má vysílat signály nahoru.**

Formuluje, kdo koho smí znát. Volání směrem dolů je v pořádku, protože rodič své děti vlastní a zná je. Opačný směr — dítě sahající na rodiče — vytváří závislost, která rozbije znovupoužitelnost dítěte. Místo toho dítě vyšle [signál](#signal) a rodič se rozhodne. Sourozenci se propojují přes společného rodiče, obvykle v `_ready()`. Efekt: závislosti kopírují hierarchii a strom scény zůstane čitelný.

Kde se s tím potkáš: [GDScript: call down, signal up](godot/gdscript.md#call-down-signal-up-kdo-koho-smi-znat) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md#observer-pattern-nejcastejsi-chyba-zacatecniku-a-jeji-oprava)

### Camera shake

**Krátký otřes kamery definovaný jako asset (amplituda, frekvence, šum) — spouští se z kódu, z anim notify nebo jako stopa v sequenceru.**

Starší „legacy" camera shake blueprint nastavuje oscilaci rotace (pitch, yaw, roll) třeba Perlinovým šumem. V sequenceru délku otřesu určuje sekce stopy, ne oscillation duration. Otřes patří jen na okamžik dopadu; přes celou animaci by byl k nevydržení — stejná střídmost jako u ostatního [juice](teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku).

Pro dopad zásahu: Camera Shake Base s patternem Perlin noise, krátké trvání (kolem 0,2 s), blend in 0 a krátký blend out, spuštěný přes Player Camera Manager spolu s hit stopem.

Kde se s tím potkáš: [Finisher bez střihu](praxe/cutsceny.md#finisher-bez-strihu-sekvence-ktera-se-prehraje-kolem-hrace) · [Rejstřík: Player Camera Manager](#player-camera-manager) · [Pět potvrzení rány](praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem)

### Capsule

**Náhledový obrázek hry na Steamu — miniatura, kterou zákazník vidí ve všech seznamech dřív než cokoli jiného.**

Nejdůležitější kus grafiky celé stránky. Zásady: žádné AI generované umění, custom nebo semi-custom logo (volný font + gradient + tematický detail), silný kontrast textu vůči pozadí, žádný text kromě názvu hry, nekolidovat se Steam badgi (Demo) — a rámeček, který capsule vysekne ze seznamu. Rozbory dobrých a špatných: steamcapsule.com.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md) · [Co prodává](teorie/co-prodava.md)

### Camera director

**Objekt, který vlastní pravidla kamery pro danou oblast: hranice, čeho si všímat, jak plynule předat řízení dalšímu.**

Každá místnost má výchozího režiséra (hranice nastavené tak, aby tajemství zůstala skrytá) a trigger zóny s vlastními režiséry pro výjimky — tajné chodby, cinematic framing vysokých stropů. Předání se tweenuje; detail, na kterém stojí game feel celé kamery.

Kde se s tím potkáš: [Kamera](teorie/kamera.md)

### Cast

**Přetypování obecné reference na konkrétní třídu, aby šlo volat její specifické funkce.**

`Cast To DestroyDoor` řekne enginu „zkus s tímhle actorem zacházet jako s třídou DestroyDoor". Cena: volající Blueprint získává tvrdou závislost na cílové třídě (a tahá si její referenci do paměti), takže s každým novým typem objektu roste řetěz castů. Tam, kde jde jen o „pošli zprávu, kdo umí, zareaguje", je lepší Blueprint Interface.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Channel

**V Mesh Terrainu pojmenovaná materiálová vrstva terénu — nástupce landscape layers.**

Channels se definují v data assetu partition definice 1:1 podle vrstev materiálu a rovnou se z nich stávají malovatelné vrstvy, bez ceremonie layer info assetů starého Landscape. Navíc je umí přiřazovat i modifiery (weight channel) — boolean skála si tak vyřízne tvar a zároveň obarví materiál. Pozor na kolizi názvosloví: UE má i kolizní channels (WorldStatic, Pawn…), to je jiný mechanismus.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Kanály z vertex colorů a pro PCG](praxe/mesh-terrain.md#modifikatory-v-rukou-epicu-poradi-vrstev-rovina-pod-poi-a-pcg-ktere-rozmistuje-skaly)

### CDO

**Class Default Object — výchozí instance, kterou Unreal vytvoří pro každou třídu sám; dá se z ní číst, aniž bys cokoli konstruoval.**

Umožňuje vzor **„třída jako data"**: definici položky (název, ikona, popis) napíšeš jako `UObject` s `EditDefaultsOnly` vlastnostmi, konkrétní věci jsou blueprintoví potomci bez event grafu — a čte se z nich uzlem `Get Class Defaults`, respektive `GetDefaultObject()` v C++. Proti data assetu má jednu praktickou výhodu: **předáváš třídu, ne objektovou referenci**, takže nevzniká tvrdá reference na asset. Zásadní výhrada: **CDO je globální a sdílené** — cokoli, co se má lišit mezi jednotlivými kusy (opotřebení, náboje, vlastník), do něj nepatří.

Kde se s tím potkáš: [Třída jako data](praxe/principy-architektury.md#trida-jako-data-cdo-misto-instanci) · [Rejstřík: Data asset](#data-asset) · [Rejstřík: Hard reference](#hard-reference) · [Inventář: definice a instance](praxe/inventar.md#definice-popisuje-druh-instance-nese-kus)

### Channel packing

**Uložení několika šedotónových map do kanálů jedné textury, třeba roughness, AO a výšky do R, G a B.**

Šedotónová mapa potřebuje jen jeden kanál, takže tři mapy se vejdou do jedné RGB textury a čtvrtá do alfy. Ušetří se paměť i počet vzorkování v materiálu. Cenou je, že kanály sdílejí rozlišení a kompresi a že materiál musí vědět, co je v kterém kanálu, a proto se rozložení drží jako konvence projektu (třeba ORM: occlusion, roughness, metallic). V UE se pro takovou texturu volí komprese Masks, která vypne sRGB; jinak se hodnoty zkreslí. Workshop o kitech balí roughness, AO a výšku sdíleného tileru do jedné textury a Mortal Shell 2 má podle rozboru herních souborů zabalenou většinu sad textur z Megascans.

Kde se s tím potkáš: [Textury pro kit: dvě textury na kámen](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen) · [Mortal Shell 2](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek) · [Rejstřík: PBR](#pbr)

### Chaos Cloth

**Realtime fyzika látek přes Cloth Asset graf: import meshe → skin weights z těla → weight mapa → config → collider.**

Weight mapa (uzel MaxDistance) maluje, co simulovat a co nechat animaci; kolider dodává kopie physics assetu postavy. Ladicí trojúhelník: mapa × collider koule × config (stiffness, iteration/subdivision count = kvalita vs. CPU). Do postavy se zapojuje Chaos Cloth komponentou; aerodynamics config přidá vítr.

Od pipeline z dema Talisman (5.4) je cloth asset samostatný a nebydlí ve skeletal meshi. Mapa Backstop přidá levný test, aby látka nezapadla za skinovaný povrch, uzel Remesh vygeneruje méně detailní simulační LODy a import z Marvelous Designeru přes USD přenese i parametry simulace.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md) · [Látka jako samostatný asset](praxe/destrukce-a-latky.md#latka-jako-samostatny-asset-chaos-cloth-pres-dataflow)

### Chaos Mover

**Plugin, který z postavy v Moveru dělá dynamické těleso ve fyzikálním světě (experimentální, od 5.7).**

Pohybový mód spočítá cíl jako obvykle, ale k cíli postavu táhne constraint v solveru Chaosu, a to jen do nastaveného limitu síly a momentu. Zvláštní constraint drží postavu nad zemí podle dotazu na zem. Zapíná se backend třídou Chaos Mover na Mover komponentě a potřebuje Async Physics. Výsledkem jsou obousměrné interakce (tlačení, pružiny, hybnost) a síťová fyzika, za cenu mírné latence vstupu.

Kde se s tím potkáš: [Chaos Mover](praxe/mover.md#chaos-mover-postava-jako-fyzikalni-teleso-se-stropem-sily) · [Rejstřík: Mover](#mover)

### Chaos Visual Debugger

**Nástroj, který nahrává fyzikální scénu tak, jak ji vidí Chaos, a dovoluje ji přehrávat snímek po snímku i po fázích solveru.**

Otevírá se přes Tools → Debug → Chaos Visual Debugger. Nahrává v buildech mimo shipping, živě i do souboru, a stojí na Trace jako Insights. Ukáže kontakty s manifoldem a impulzy, dotazy do scény včetně všeho, co navštívily, klouby i geometrii. Klientský a serverový solver umí mít vedle sebe.

Kde se s tím potkáš: [CVD zevnitř](praxe/debugging.md#chaos-visual-debugger-zevnitr-faze-solveru-kontakty-a-klient-vedle-serveru) · [CVD v reálné hře](praxe/gpu-pruchod.md#chaos-visual-debugger-rentgen-fyziky)

### Chooser

**Datová tabulka „když platí tyhle podmínky, vyber tenhle asset" — v MM přepíná databáze, obecně vybírá cokoli.**

Řádky = kandidáti (PSD, montáže, nested choosery), sloupce = podmínky (bool, enum, float range) bindnuté na proměnné AnimBP. V MM: databáze jako Dynamic value, On Update → Evaluate Chooser (All Results) → Set Databases To Search + Interrupt on database change. Umí i output sloupce (damage per útok). Plně integrovaný s rewind debuggerem.

Od 5.8 může být posledním sloupcem [pose match](#pose-match-column), tedy motion matching přímo v tabulce, a chooser drží libovolný počet vnitřních pose search databází. Vrácení víc výstupních structů najednou je volba na uzlu Evaluate Chooser.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md) · [Motion matching uvnitř chooseru](praxe/gasp.md#motion-matching-uvnitr-chooseru-pose-match-sloupec-databaze-na-radek-a-blend-space-ve-stacku) · [Výběr vstávání](praxe/ragdoll.md#vstavani-pres-motion-matching-snapshot-pose-history-z-fyziky-a-chooser)

### CI/CD

**Automatizovaný kontrolní seznam, který po každém pushi ověří změnu a udrží projekt ve stavu, kdy se dá vydat.**

*Continuous integration* = kód se po každém pushi automaticky otestuje proti zbytku; *continuous delivery* = po projití testů je vždycky připravený k vydání. Pod tím je jediná změna návyku: **místo „otestuju, až budu hotový" → každá změna je malá, otestovaná a připravená jít ven.** U GitHubu se nic neinstaluje — stačí složka `.github/workflows` a soubor `.yml`. Pro herní projekt je největší přínos **čistý stroj u každého běhu**: chytí celou třídu chyb typu „u mě to funguje" (chybějící asset, nezakomitovaná změna). Realistický první krok u UE není automatické nasazení, ale **automatické ověření, že projekt jde zabalit**.

Kde se s tím potkáš: [CI/CD je automatizovaný kontrolní seznam](teorie/programatorske-navyky.md#cicd-je-automatizovany-kontrolni-seznam-ne-devops-ritual) · [Rejstřík: Version control](#version-control)

### Chord extension

**Tón přidaný k triádě nad kvintu — septima, nona, undecima… (rozšíření akordu).**

Okamžitě bohatší, „dospělejší" zvuk. Páteř lo-fi, R&B, house a neo soulu. Základní triáda je root + tercie + kvinta; extension staví dál po stejném vzorci obden.

Kde se s tím potkáš: [Žánry a jejich melodie](hudba/zanry-a-styl.md) · [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Chord generator

**Web nebo nástroj, který vygeneruje smysluplnou akordovou progresi za tebe.**

Pravidla stavby akordů někdo naprogramoval (chordchord.com a další). Vygeneruješ čtyřakordovou progresi, přepíšeš do piano rollu — obchází potřebu teorie pro rychlý start. Dlouhodobě je lepší stavět akordy sám.

Kde se s tím potkáš: [Zdarma a rychle: nástroje a game jam](hudba/nastroje-zdarma-a-game-jam.md)

### Chord progression

**Sled akordů hraných za sebou, který tvoří harmonickou kostru skladby.**

Vyklikáš ji po zvýrazněných tónech tóniny; emoci nese hlavně pohyb mezi akordy (vzestup pozitivní, sestup smutný), ne jednotlivé akordy. Generátory (chordchord.com) rozjezd usnadní, ale stavět ji ručně je z dlouhodobého hlediska lepší.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md) · [Jak psát melodie](hudba/melodie.md)

### Cipher

**Typ hráčské postavy: prázdná nádoba bez vlastní osobnosti, hlasu a motivací — oživuje ji hráčova imaginace.**

Jeden ze čtyř typů protagonisty (cipher · fixní · customizovatelný · customizovatelný s fixním základem). „Bez osobnosti" není vada: mlčící postava v puzzle hrách (Half-Life, Tunic) nechává znít hlas v hráčově hlavě. Cena: veškerá tíha charakterizace jde do vizuální komunikace — jak postava vypadá a co reprezentuje. Praktické pravidlo: umíš psát → fixní postava; umíš vyrábět cool věci, ale ne psát → cipher.

Kde se s tím potkáš: [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Closing doors

**Iterační metoda od širokého k úzkému: každé kolo zavře, co nefunguje, a rozvine, co zaujalo.**

Riotí postup pro concept art, ale funguje na jakoukoli tvůrčí volbu. Stojí a padá s jedním sebeovládáním: zavřené dveře se znovu neotevírají. Bez toho pravidla se tým točí v kruhu a projekt se každé tři měsíce potichu promění v jinou hru. Doplňuje se otázkami na cíl (která z nich působí nejděsivěji?) místo otázek na dojem.

Kde se s tím potkáš: [Herní art: pipeline](teorie/art-pipeline.md) · [Nápad](teorie/napad.md)

### Cluster culling

**Nanite zahazuje neviditelnou geometrii po clusterech (~128 trojúhelníků) — buď celý cluster, nebo nic.**

Z toho plyne, že o výkon rozhoduje **topologie**: stěna z dlouhých tenkých trojúhelníků je pár velkých clusterů, takže stačí kousek její hrany a musí se rasterizovat celá — i s tím, co je za ní. Rovnoměrně přesíťovaný mesh má clustery rozeseté po ploše a částečně se cullne, dokonce sám sebe. Druhá past: clustery se cullují **podle bounds**, takže do sebe namačkané meshe culling znemožní. Prakticky to znamená, že cluster culling patří do stylového průvodce k modelování, ne do optimalizačního sprintu na konci.

Kde se s tím potkáš: [Overdraw se autoruje](praxe/nanite-do-hloubky.md#overdraw-se-autoruje-ne-opravuje) · [Rejstřík: Nanite](#nanite) · [Rejstřík: Overdraw](#overdraw) · [Meshlety v Alan Wake 2](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les)

### Cluster Union

**Komponenta Chaosu, která z víc geometry collections udělá jedno fyzikální těleso — a umí prasknout jen v jednom místě.**

Rozhoduje, které vnitřní částice patří do kterého unionu, a podporuje částečnou destrukci: poškození uvolní jen zasaženou část a zbytek zůstane připojený. V LEGO Fortnite ji krmí herní graf spojení na serveru. Kvůli výkonu se postupně zjednodušuje do konvexních obalů, které slouží jen simulaci. Nahrazuje starší cluster groups.

Kde se s tím potkáš: [Budova, kterou rozbije kdokoli](praxe/destrukce-a-latky.md#budova-kterou-rozbije-kdokoli-graf-spojeni-na-serveru-cluster-union-ve-fyzice) · [Destrukce, kterou procesor unese](praxe/destrukce-a-latky.md#destrukce-kterou-procesor-unese-konvexy-debris-sdilene-instance-a-strop-zlomu)

### Color temperature

**Barva světla zadaná teplotou v kelvinech: nízká je teplá a oranžová, vysoká studená a modrá.**

Odpovídá barvě, kterou vyzařuje zahřáté černé těleso, a proto působí přirozeněji než ručně vybraná barva. Svíčka má kolem 1900 K, klasická žárovka kolem 2700 K, denní světlo zhruba 5500 až 6500 K. V Unrealu se na světle zapíná přes Use Temperature, pro emisivní materiál dá stejnou barvu uzel BlackBody. Ruční barva má smysl tam, kam teplota nedosáhne, třeba u neonu nebo červeného zadního světla.

Kde se s tím potkáš: [Svítidlo z víc světel](praxe/megalights.md#svitidlo-z-vic-svetel-odraz-mlha-a-stin-se-ladi-zvlast) · [Malovat světlem](praxe/osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel)

### Computer use

**Režim, ve kterém AI ovládá program jako člověk: dívá se na obrazovku a kliká myší.**

Funguje s čímkoli, ale je pomalý a drahý na tokeny. V testu v Blenderu trvalo jen uložení souboru deset minut. Kde je k dispozici API přes MCP, je programové volání podle Epicu úspornější i rychlejší.

Kde se s tím potkáš: [MCP místo klikání](praxe/claude-code-ue.md#mcp-misto-klikani-agent-v-blenderu-od-blockingu-po-rig) · [Vlastní tool set a skill](praxe/mcp-v-editoru.md#vlastni-tool-set-a-skill-api-pro-juniora-a-rada-kolegovi) · [Rejstřík: MCP](#mcp)

### Construction Script

**Graf actor blueprintu, který běží v editoru při umístění nebo změně actoru a při spawnu — ještě před BeginPlay.**

Hodí se na přípravu dat, která závisí na komponentách konkrétní instance: třeba mapa stran dveří s odkazy na scene komponenty, které do výchozích hodnot proměnné zadat nejde, nebo reference, které mají fungovat i v sequenceru bez spuštěné hry. Nepatří do něj nic drahého — spouští se často, při každém posunu actoru v editoru.

Kde se s tím potkáš: [Objekt ví, jak se s ním zachází](praxe/interakcni-animace.md#objekt-vi-jak-se-s-nim-zachazi-data-interakce-patri-k-veci-ne-k-postave) · [Look-at systém](praxe/metahuman.md#look-at-system-pohled-vrstveny-pres-jakoukoli-animaci) · [Run Construction Script on Drag](praxe/pcg-mesta.md#nastroj-pro-artisty-bake-tlacitkem-a-drobnosti-ktere-setri-hodiny)

### Contact shadows

**Krátké stíny dopočítané v obrazovém prostoru z hloubky scény, které doplní drobné kontakty, kam běžné stíny nedosáhnou.**

V Unrealu se zapínají na světle hodnotou Contact Shadow Length (výchozí je 0). Paprsek se trasuje jen kousek po hloubkovém bufferu, takže jsou levné, ale umí jen krátké stíny. S pixel depth offsetem z výškové mapy dají stíny i reliéfu, který existuje jen v materiálu, třeba pod POM na terénu. Hodí se i na vzdálenou vegetaci.

Kde se s tím potkáš: [Hloubka bez geometrie](praxe/landscape-tipy.md#hloubka-bez-geometrie-pom-contact-shadows-a-plugin-ihp) · [Rejstřík: Pixel Depth Offset](#pixel-depth-offset) · [Rejstřík: Parallax occlusion mapping](#parallax-occlusion-mapping) · [Stíny pokryvu země](praxe/pcg-vegetace.md#les-pro-otevreny-svet-co-se-nacte-s-levelem-a-co-roste-kolem-hrace)

### Context switch

**Přepnutí jádra z jednoho vlákna na druhé; stojí čas na uložení a obnovu stavu.**

V Insights se sleduje vlastním kanálem a čte se ze dvou stran: **jedno jádro obsazené jediným vláknem** může blokovat ostatní, a **příliš časté přepínání** je čistá režie navíc (typicky když je hodně krátce žijících vláken). Otázka, kterou to zodpovídá, je jednoduchá: **je zatížení jader vyvážené?**

Kde se s tím potkáš: [Insights jako disciplína](praxe/mereni-automaticky.md#insights-jako-disciplina-od-symptomu-ke-pricine) · [Rejstřík: Multithreading](#multithreading)

### Cognitive load

**Kolik mozkové kapacity aktivita právě žere; učení nové dovednosti je vědomé a drahé, automatizace ji zlevňuje.**

Příliš nízká zátěž nudí, příliš vysoká zahltí — onboarding je řízení komplexity vůči fázi učení hráče. Pestřejší nepřátelé, víc informací na obrazovce a nové mechaniky zátěž zvedají; proto se nové věci dávkují a učí v izolaci, než se smíchají.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md) · [Zábava a flow](teorie/zabava.md)

### Cold open

**Otvírák traileru: prvních 10–15 vteřin nabitých highlighty v rychlých střizích, teprve pak volnější tempo.**

Pojem z filmového střihu (a trailerového řemesla Dereka Lieu). Důvod jsou retention grafy: velká část diváků odpadne během první půlminuty — kdo šetří nejlepší záběry na konec, ukáže je prázdnému sálu. Pravidla k tomu: celková délka 30–50 s, žádný záběr přes ~6 vteřin, na konci call to action.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Collision mask

**Nastavení „co mě zajímá" — proti vrstvě, která říká „co jsem".**

Dvojice vrstva/maska je filtr kolizí zapsaný v konfiguraci místo v podmínkách kódu. Objekt patří do jedné či více *vrstev* a jeho *maska* určuje, které vrstvy vůbec zaznamená. Prakticky: dej hráče na vlastní vrstvu a nastav minci masku jen na ni — mince pak přestane reagovat na pohyblivé plošiny, aniž bys napsal jediný `if`. Filtr v konfiguraci se drží na jednom místě; filtr v podmínkách se rozleze do každého skriptu.

Kde se s tím potkáš: [První hra: znovupoužitelná scéna](godot/prvni-hra.md#znovupouzitelna-scena-jedna-kill-zone-pro-propast-i-pro-slimaka) · [Mapa 2D nodů](godot/zaklady.md#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti)

### Collision preset

**Předpis, jak objekt reaguje na jednotlivé kolizní kanály: Block, Overlap, nebo Ignore.**

Preset je první a nejlevnější filtr kolizního systému — rozhoduje se ještě před jakoukoli herní logikou. Trigger nastavený „Ignore all, Overlap jen WorldStatic/WorldDynamic/Pawn/PhysicsBody" negeneruje eventy o věcech, které tě nezajímají. Vlastní (Custom) preset se vyplatí kdykoli, kdy výchozí profily neodpovídají roli objektu.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Constraints

**Nepsané dohody, se kterými musí souhlasit každý nový řádek kódu, aby program zůstal správný.**

Příklad: gameplay pozice se drží v desetinných číslech, ale zaokrouhluje na celá, zatímco vizuální pozice se plynule interpoluje — a kolize se počítají výhradně z gameplay pozice. Takové rozhodnutí padne brzy a všechno další s ním musí korektně spolupracovat. Čím větší program, tím hustší pavučina omezení — a právě proto jsou hluboké stavové chyby těžší než mělké. Blízký příbuzný pojmu [invariant](#invariant).

Kde se s tím potkáš: [Indie kariéra](teorie/indie-kariera.md#proc-ai-neumi-velky-kod-argument-o-omezenich) · [Principy architektury](praxe/principy-architektury.md)

### Content

**Vše, co jde ve hře opakovat s variacemi: levely, nepřátelé, příběh, odemykatelné věci.**

Protipól gameplaye (mechanik a systémů). Rozlišení má praktický důsledek: levely testují hráčovo porozumění mechanikám, takže je nelze rozumně navrhovat dřív, než víš, o čem hra je. Nejčastější chyba je vyrábět hory contentu do hry, která na to ještě není připravená — u malé hry se proto škrtá content, ne mechaniky.

Kde se s tím potkáš: [Level design: game design vs. level design](teorie/level-design-solo.md) · [Scope](teorie/scope.md)

### Contextual Animation

**Plugin pro synchronizované animace víc účastníků (postava a objekt, dvě postavy): role, montáže stejné délky a warp pointy v jednom scene assetu.**

Rules asset popisuje role (rozměry kapsle, offset meshe), scene asset přiřazuje rolím animace a určuje, kdo se ke komu warpuje. Za běhu se z binding contextů obou účastníků vytvoří bindings a scéna se spustí na komponentě postavy. Řeší zarovnání a synchronizaci, ne dotyk — IK ruky na kliku musíš dodat sám. V seznamu pluginů je označený jako experimentální.

Kde se s tím potkáš: [Contextual Animation](praxe/interakcni-animace.md#contextual-animation-scena-s-rolemi-misto-rucni-choreografie) · [Zápas se smyčkou](praxe/interakcni-animace.md#zapas-se-smyckou-sekce-montaze-a-rozhodnuti-hrace) · [Finisher bez střihu](praxe/cutsceny.md#finisher-bez-strihu-sekvence-ktera-se-prehraje-kolem-hrace) · [Rejstřík: Motion Warping](#motion-warping)

### Context window

**Kolik textu model najednou udrží: prompt, historii, popisy nástrojů i výsledky.**

S MCP od Epicu je to praktický limit, protože popis jediného tool setu bývá obrovský, u Niagary podle webináře skoro čtvrt milionu jednotek, nejspíš tokenů. Harness s malým oknem popis ořízne a model pak zkouší naslepo, pomalu a draze. Proto taky Epic radí psát skills stručně.

Kde se s tím potkáš: [Jak s agentem v editoru mluvit](praxe/mcp-v-editoru.md#jak-s-agentem-v-editoru-mluvit-presna-jmena-jeden-ukol-a-kontext-ktery-se-vejde) · [Rejstřík: Harness](#harness)

### Control Rig Dynamics

**Částicový systém sekundárního pohybu v Control Rigu (5.8) — pružné řetězy pro culíky, pouzdra a podobné doplňky, laditelné jedním uzlem a běžící i ve hře.**

Podle Epicu zhruba pětkrát rychlejší než Control Rig Physics a stavěný pro postavy: tuhost, tlumení a křivky po délce řetězu, kolize s tělem. Za běhu jede přes Control Rig uzel v AnimBP; debug okno ukazuje tělesa i kolize, i v PIE. S fyzikou se dá kombinovat — dynamics na drobnosti, fyzika na tělo.

Kde se s tím potkáš: [Sekundární pohyb v Control Rigu](praxe/animace-nastroje.md#sekundarni-pohyb-v-control-rigu-dynamics-za-behu-fyzika-a-autobake-pri-animovani) · [Rejstřík: Control Rig](#control-rig)

### Control Rotation

**Rotace, kterou drží player controller — úhel pohledu, který hráč ovládá myší nebo pravou páčkou.**

Kamera s `Use Pawn Control Rotation` a postava s `Use Controller Desired Rotation` se podle ní natáčejí. Po cutscéně má pohled hodnotu z doby před zakázáním vstupu; `Set Control Rotation` ho nastaví na zvolený vstupní úhel. Hodnotu se vyplatí odečíst přímo ve hře (stiskem klávesy uložit aktuální control rotation), ne odhadovat.

Kde se s tím potkáš: [Cutscéna, která vrátí hru tam, kde skončila](praxe/cutsceny.md#cutscena-ktera-vrati-hru-tam-kde-skoncila)

### Cook

**Převod editorových assetů do formátu pro cílovou platformu; probíhá při balení hry.**

Čtyři nastavení, která umí zmenšit balíček o desítky procent: **create compressed cooked packages**, **cook only maps** se výslovným seznamem map, **exclude editor content when cooking** a seznam adresářů, které se nemají cookovat nikdy. Netýká se výkonu, jen velikosti instalace — ale je to jedno z mála míst, kde se dvouciferné procento dá dostat bez kompromisu.

Kde se s tím potkáš: [Drobky: šest zásahů](praxe/pamet-a-instance.md#drobky-sest-zasahu-na-jedno-odpoledne)

### Contact curve

**Animační křivka 0/1 říkající, kdy je chodidlo na zemi — řídí foot pinning; v GASP nahradila foot velocity curves.**

Hodnota 0 = noha ve vzduchu, 1 = došlap. Proti rychlostním křivkám je konzistentní napříč gaity (walk i sprint sdílí stejnou škálu) a snadno se ručně edituje, když noha „lepí" špatně. Epic je generuje interním batch nástrojem; starý foot placement anim uzel pořád chce velocity curve, remapuje se přes Curve Expressions plugin.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Content scheduling

**Kdy a jak často se ve hře věci dějí — rytmus obsahu, ne jeho množství.**

Nejčastější oprava hry, která „má všechno a nudí": nepřidat obsah, ale přeskládat ho v čase. Série dobrých částí bez rytmu je standup, kde každý vtip funguje a routine nedrží pohromadě.

Kde se s tím potkáš: [Případovky designu](teorie/pripadovky-designu.md)

### Context steering

**Technika pohybu AI: entita průběžně hodnotí všechny směry vahami a vybírá nejlepší proveditelný.**

Vylepšení klasických steering behaviors (boids), jejichž protichůdné vektory se umí vyrušit — AI pak zamrzne u zdi, místo aby ji obešla. Context steering drží ohodnocení celé růžice směrů (typicky přes dot product vůči kýženému směru); zablokovaný nejlepší směr prostě nahradí druhý nejlepší. Tvarováním vah vznikají chování jako kroužení kolem cíle nebo nájezdy a odskoky — základ soubojů, které jsou zábavné pohybem, ne čísly.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md)

### Continuing pose

**„Co by hrálo dál, kdybych nic neměnil" — kandidát, kterého musí každá nová animace v Motion Matchingu porazit cenou.**

Klíč k ladění MM: v pose search debuggeru vidíš cenu continuing pose vedle vítěze a channels breakdown řekne, který kanál rozhodl. Continuing pose cost bias (záporný) drží systém déle v jedné animaci; notify tag Override Continuing Pose Bias protlačí hezkou animaci, i když matematicky nevyhrává.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Control Rig

**Grafový rigging a procedurální animace přímo v enginu — běží i za runtime, bez rekompilace.**

V GASP pohání foot placement Mover postavy (slope warping, pinning, root damping) a Locomotor (procedurální chůze bez jediné animace). Zároveň směr, kterým Epic míří s budoucím animačním frameworkem: animační systémy jako vizuální grafy, které si tech animátor otevře a ohne sám. Řemeslný vzor null + control zachovává hratelnost grafu ve viewportu.

Pro gameplay je Control Rig uzel v AnimGraph místo, kde [IK](#ik) dotáhne ruku na kliku nebo předmět — za slotem, který hraje montáže. Ve verzi 5.8 přibyly [Control Rig Dynamics](#control-rig-dynamics) pro sekundární pohyb, fyzika přímo v rig modulech a [Direct Mesh Controls](#direct-mesh-controls).

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [Ruka na klice](praxe/interakcni-animace.md#ruka-na-klice-ik-v-control-rigu-prevod-prostoru-a-alfa-z-krivky) · [Sekundární pohyb v Control Rigu](praxe/animace-nastroje.md#sekundarni-pohyb-v-control-rigu-dynamics-za-behu-fyzika-a-autobake-pri-animovani) · [Rig, který se přenese](praxe/animace-nastroje.md#rig-ktery-se-prenese-controly-na-kuzi-moduly-a-tvary-bez-navratu-k-riggerovi) · [Aditivní look-at](praxe/gasp.md#look-at-jako-aditivni-solver-pohled-bez-ztraty-animace) · [Vazby končetin přes FBIK](praxe/gasp.md#parove-akce-pres-motion-matching-role-rozdeleny-warp-a-vazby-koncetin) · [Rig, o který nikdo neřekl](praxe/claude-code-ue.md#mcp-misto-klikani-agent-v-blenderu-od-blockingu-po-rig)

### Coyote time

**Krátká lhůta po opuštění hrany, během které skok pořád projde.**

Jméno je z kresleného Coyota, který po výběhu z útesu chvíli běží ve vzduchu — a podle autorů Celeste ho vymysleli hráči, ne vývojáři. Typická hodnota je kolem desetiny sekundy (asi šest snímků při 60 FPS). Patří do rodiny „tichých úlev", které pracují se **záměrem hráče místo přesné simulace stisků**: sourozencem je [input buffering](#input-buffering) (stisk těsně *před* dopadem se provede při dopadu) a korekce rohu. Nezvyšuje to jen pohodlí — profesionální hráči ty snímky navíc vyžívají na skoky, které by jinak nevyšly.

Kde se s tím potkáš: [Celeste: křivky v snímcích](teorie/game-feel.md#celeste-krivky-v-snimcich-a-hrst-tichych-ulev) · [Godot: skok, který rozumí hráči](godot/animace-a-pohyb.md#skok-ktery-rozumi-tomu-co-hrac-chtel)

### Core loop

**Základní smyčka činností, kterou hráč ve hře opakuje nejčastěji — jádro, na kterém všechno ostatní stojí.**

„Plíž se → pozoruj → proklouzni" nebo „těž → vyrob → prodej". Užitečný pojem při analýze (co hráč *reálně* dělá většinu času?) i při ořezávání scope — co nesytí core loop, je kandidát na vyhození. Zároveň platí výhrada z kapitoly o smyčkách: popisuje strukturu, nevysvětluje kvalitu.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md) · [Nápad](teorie/napad.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### CPU-bound / GPU-bound

**Které ze dvou zařízení na tvou hru čeká — a tím pádem které z nich má smysl odlehčovat.**

Rozhoduje se podle toho, které číslo v `stat unit` se blíží k `frame`: **game** nebo **draw** → CPU-bound, **GPU** → GPU-bound. Význam je praktický, ne akademický: **stejný symptom má dvě různé léčby.** Padá snímkování a vysoko je `draw`? Neřeš shadery, řeš počet objektů, ze kterých se rozhodnutí dělá. Vysoko je `GPU`? Pak teprve shadery a rozlišení. Zaměnit ta dvě patra znamená optimalizovat celý den bez efektu.

Kde se s tím potkáš: [Rozhodovací strom](praxe/profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Co je v herním vlákně a co v renderovacím](praxe/profiling.md#co-je-v-hernim-vlakne-a-co-v-renderovacim) · [Rejstřík: Herní vlákno](#herni-vlakno)

### Cubemap

**Textura ze šesti čtvercových stěn krychle, která zachytí okolí ze všech směrů.**

Používá se na odrazy, oblohu a HDRI a také na falešné interiéry za okny, kde ji uzel Interior Cubemap promítne tak, že plochá plocha vypadá jako místnost. V Unrealu je cube textura samostatný typ assetu. Vlastní jde vyrobit ze scény přes [Scene Capture](#scene-capture) Cube a Create Static Texture.

Kde se s tím potkáš: [Falešné okno](praxe/materialy.md#falesne-okno-interior-cubemap-a-mistnost-nafocena-v-enginu) · [Rejstřík: Interior mapping](#interior-mapping) · [Rejstřík: Render target](#render-target)

### Custom Depth

**Zvláštní průchod hloubky, do kterého kreslí jen vybrané meshe (`Render CustomDepth Pass`), volitelně se stencil číslem pro rozlišení skupin.**

Zapíná se v Project Settings (Custom Depth-Stencil Pass, varianta Enabled with Stencil) a na meshi; materiál ho čte přes `SceneTexture` (CustomDepth, CustomStencil). Slouží na obrysy, zvýraznění i triky typu „efekt nad zasaženým, ale pod útočníkem": stencil řekne, kde postava je, a porovnání se scene depth, jestli je opravdu vidět. Zadarmo není — průchod stojí výkon, i když ho už nic nepotřebuje.

Kde se s tím potkáš: [Záblesk a kapow](praxe/souboj.md#zablesk-a-kapow-efekt-musi-sedet-na-tele-i-mezi-tely) · [Profilovat cizí hru](praxe/gpu-pruchod.md#profilovat-cizi-hru-priprava-ktera-rozhoduje)

### Custom Primitive Data

**Hodnoty uložené na celé primitive komponentě, které materiál čte jako parametry, takže varianty nepotřebují nové material instances.**

Nastavují se z blueprintu nebo v detailech komponenty a parametr v materiálu musí mít zapnuté Use Custom Primitive Data. Platí pro celou komponentu. Pro jednotlivé instance v ISM slouží sourozenec [Per-instance custom data](#per-instance-custom-data). Obojí šetří material instances, a tím i shading biny a draw cally. Přednáška Lucid Games tímhle pojmem označuje barvy budov předávané z PCG.

Kde se s tím potkáš: [Variabilita z dat](praxe/pcg-mesta.md#variabilita-z-dat-sockety-barvy-instanci-a-presety-pod-tagy) · [Rejstřík: Per-instance custom data](#per-instance-custom-data)

### Custom resource

**Vlastní datový typ uložený jako soubor: `extends Resource` + `class_name`, hodnoty přes `@export`, instance jako `.tres`.**

Godotí obdoba Unity ScriptableObjectu a příbuzný unrealího [Data assetu](#data-asset). Řeší jediný problém: **balancovat hru bez otevírání skriptů**. Struktura se napíše jednou, každá varianta je pak nový soubor s jinými čísly a skript se už nemusí měnit. Pravidlo, které se vyplatí držet: **resource popisuje, co ta věc je; skript řídí, co ta věc dělá** — logika do resourcu nepatří. Pozor na to, že resources jsou **ve výchozím stavu sdílené**: zápis do jednoho se projeví všude, kde je použitý (řeší `duplicate()`).

Kde se s tím potkáš: [Resource: data mimo kód](godot/resources.md) · [Strategy jako vyměnitelný resource](godot/stavy-a-vzory.md#strategy-chovani-jako-vymenitelny-resource)

### Custom Time Dilation

**Násobitel času jednoho aktéra (`Set Custom Time Dilation`) — 0 ho zmrazí, 1 vrátí normální rychlost, zbytek hry běží dál.**

Na rozdíl od [Global Time Dilation](#global-time-dilation) zpomaluje jen toho, komu se nastaví. Při hit stopu tak jde zasaženého úplně zastavit a útočníka jen zpomalit. S aktérem se zpomalí jeho tick i animace; časovače světa (Set Timer by Event) běží normálně, takže jimi jde délku zmrazení odměřit.

Kde se s tím potkáš: [Hit stop: zastav oba, ale každého jinak](praxe/souboj.md#hit-stop-zastav-oba-ale-kazdeho-jinak) · [Rejstřík: Hit stop](#hit-stop)

### Cyklus napětí

**Pět kroků hororové dramaturgie: setup → očekávání → semínko pochyb → diverze → akce; pak se napětí sbírá znovu.**

Setup a očekávání ustaví normál; anomálie ho nahlodají; diverze („čekáš úder — nic") napětí zdvojnásobí; akce ho vybije. Diverze užívej střídmě, jinak hráč prokoukne rytmus. Obecnější verze téhož: oscilace intenzity rozhodování.

Kde se s tím potkáš: [Horor design](teorie/horor-design.md)

### Dataflow

**Grafový systém Unrealu pro zpracování dat assetů — například přenos rigu, vah a tvarů z jednoho meshe na druhý.**

V přednášce o riggingu v 5.8 přenáší uzel Transfer Attributes celý rig z hrubšího meshe, na kterém se pohodlně riguje, na mesh s vyšším rozlišením — a stejně tak z jedné postavy na druhou (zebra → monstrum), takže vysochané tvary jdou použít znovu. Graf se přidává ke skeletal meshi.

Dataflow slouží i destrukci (nedestruktivní lámání assetů v LEGO Fortnite, experimentální v 5.4) a látkám: cloth asset vzniká v grafu z importu, přenosu skin weights, map a konfigurace solveru.

Kde se s tím potkáš: [Rig, který se přenese](praxe/animace-nastroje.md#rig-ktery-se-prenese-controly-na-kuzi-moduly-a-tvary-bez-navratu-k-riggerovi) · [Rejstřík: Morph target](#morph-target) · [Lámání v Dataflow](praxe/destrukce-a-latky.md#budova-kterou-rozbije-kdokoli-graf-spojeni-na-serveru-cluster-union-ve-fyzice) · [Látka přes Dataflow](praxe/destrukce-a-latky.md#latka-jako-samostatny-asset-chaos-cloth-pres-dataflow)

### Data-oriented design

**Návrh kódu podle toho, jak leží data v paměti a jak se k nim přistupuje — ne podle pojmů ze hry.**

Měřítkem je paměťová efektivita: kolik z paměti, kterou procesor načte, opravdu použiješ. Typické důsledky: data zpracovávaná spolu leží za sebou; místo reakcí na jednotlivé události se často každý snímek projdou všechna data najednou; a návrh se kreslí jako tok dat, protože kód pojmům ze hry neodpovídá jedna k jedné. [ECS](#ecs) je jedno z jeho paradigmat. **Neplést s [data-driven design](#data-driven-design)** — ten říká, že hodnoty patří do dat místo do kódu; data-oriented říká, jak data uspořádat pro procesor.

Kde se s tím potkáš: [Proč objekty zpomalují](praxe/mass-ecs.md#proc-objekty-zpomaluji-pamet-kterou-nactes-a-zahodis) · [Jak s Mass pracovat](praxe/mass-ecs.md#jak-s-mass-pracovat-diagram-debugger-a-jedna-implementace-misto-dvou) · [Rejstřík: Cache miss](#cache-miss) · [Částice Chaosu jako struct of arrays](praxe/destrukce-a-latky.md#destrukce-kterou-procesor-unese-konvexy-debris-sdilene-instance-a-strop-zlomu)

### Data table

**Tabulka řádků postavená na jednom structu — každý řádek má jméno a hodnoty se čtou podle něj.**

Typické použití: jedna konfigurovatelná třída (pickup) drží jen jméno řádku a zbytek si dohledá v construction scriptu — žádné dítě pro každou položku. Hranice: tabulka je statická, nedá se k ní přidat funkčnost ani z ní dědit; to umí data asset a „třída jako data".

Kde se s tím potkáš: [Kdy dědit a kdy jen konfigurovat](praxe/principy-architektury.md#kdy-dedit-a-kdy-jen-konfigurovat) · [Třída jako data](praxe/principy-architektury.md#trida-jako-data-cdo-misto-instanci) · [Rejstřík: Data asset](#data-asset)

### Deferred rendering

**Způsob vykreslování, který nejdřív uloží vlastnosti povrchů do bufferů (G-buffer) a světlo počítá až potom, pro každý pixel.**

Cena světla tak nezávisí na počtu objektů, ale na počtu světel a pixelů, které zasáhnou. V Unrealu je to výchozí cesta pro desktop a konzole. Opakem je [forward rendering](#forward-rendering), který světlo počítá rovnou při kreslení objektu. MegaLights podle dokumentace nahrazují deferred shading s vyhodnocením světla vlastním průchodem a s forward shadingem nefungují.

Kde se s tím potkáš: [Rozpočet vzorků na pixel](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis) · [Rejstřík: Forward rendering](#forward-rendering) · [Rejstřík: MegaLights](#megalights)

### Degenerate strategy

**Strategie, která hru rozkládá: dominantní postup, po jehož objevení přestává být hra zajímavá.**

V kompetitivním prostředí ničí zážitek ostatním (combo winter v Magicu), v singleplayeru hráč „prokletý znalostí" zkazí hru sám sobě. Balanc existuje hlavně proto, aby žádná cesta nebyla čtvercovou dírou na všechno.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Zábava: balanc](teorie/zabava.md)

### Data asset

**Asset nesoucí čistá strukturovaná data — konfiguraci bez logiky.**

V UE typicky potomek `UDataAsset`: designér edituje hodnoty v editoru, kód/Blueprinty je čtou. Odděluje „co" od „jak" — stejná logika, jiná data, jiné chování. Mesh Terrain v data assetu (Mesh Partition Definition) drží materiál, texel size a definice channels.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md) · [Rejstřík: Data table](#data-table) · [Nepřítel v datech](praxe/ai-ve-velkem.md#strom-jen-rozhoduje-akce-v-gameplay-abilitach-nepritel-v-datech) · [Nastavení look-at solveru](praxe/gasp.md#look-at-jako-aditivni-solver-pohled-bez-ztraty-animace) · [Budova jako věta](praxe/pcg-mesta.md#budova-jako-veta-panelovy-kit-gramatika-a-patra) · [Les pro otevřený svět](praxe/pcg-vegetace.md#les-pro-otevreny-svet-co-se-nacte-s-levelem-a-co-roste-kolem-hrace)

### Data layer

**Kontejner aktorů ve world-partition světě se třemi stavy: Unloaded / Loaded (v paměti, neviditelné) / Activated.**

Aktory se přiřazují výběrem + right-clickem ve data layer outlineru, vrstvy se dají parentovat (celé patro jedním přepnutím) a aktor smí do víc vrstev. Za běhu je řídí Get Data Layer Manager → Set Data Layer Runtime State — typicky z trigger boxu s počítadlem hráčů. Pro interiéry uvnitř world-partition buňky a stavy „načti až po odemčení"; velké venkovní světy nech streamovat World Partition samotný.

Kde se s tím potkáš: [Optimalizace scény](praxe/optimalizace.md) · [Levely a streaming](praxe/levely-a-streaming.md)

### Data Registry

**Centrální registr konfiguračních dat: pojmenovaný prostor, do kterého se agregují data tables a curve tables.**

Systémy se ptají registru jménem („dej mi settings pro tuhle třídu") místo tvrdých odkazů na konkrétní tabulky. Instanced Actors přes něj čtou per-třída nastavení — řádek tabulky se jmenuje přesně jako třída s příponou `_C`. Registry musí ležet ve složce uvedené v Project Settings → Data Registry → Directories to Scan, jinak pro engine neexistuje.

Kde se s tím potkáš: [Instanced Actors](praxe/instanced-actors.md)

### Data-driven design

**Princip: hodnoty a konfigurace žijí v datech (data assety, tabulky), logika je jen čte.**

Damage, animace, zvuky ani cooldowny nepatří natvrdo do grafu — patří do data assetu, který ability/systém čte. Fragmenty (malé datové objekty pro volitelné části: animace, VFX, damage) řeší, že ne každá entita potřebuje všechno. Odměna: designér vytvoří novou ability výměnou dat, bez zásahu do logiky. UE Gameplay Ability System je tenhle princip dotažený do konce.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Rejstřík: data asset](#data-asset) · [Neplést s data-oriented design](praxe/mass-ecs.md#proc-objekty-zpomaluji-pamet-kterou-nactes-a-zahodis) · [Nepřítel v datech](praxe/ai-ve-velkem.md#strom-jen-rozhoduje-akce-v-gameplay-abilitach-nepritel-v-datech)

### Data validation

**Automatická kontrola assetů proti pravidlům projektu — při vstupu do editoru, při odevzdání a v noci na build stroji.**

Plugin v UE kontroluje typicky jednoduchou i složitou kolizi, počet materiálů a materiálových vrstev, hustotu meshe a strop polygonů. Smysl je posunout záchyt problému co nejdřív: **levnější než hledat drahé assety profilerem je nepustit je dovnitř**. Vynucená kontrola při odevzdání zapisuje výsledek do popisu changelistu, noční běh posílá výpis do týmového kanálu. Vedle toho Asset Audit a Statistics dají tabulku assetů a počty instancí za běhu, obojí exportovatelné do CSV.

Kde se s tím potkáš: [Nález není hotová práce](praxe/profiling.md#nalez-neni-hotova-prace-predani) · [Výkon jako věc celého týmu](praxe/mereni-automaticky.md#vykon-jako-vec-celeho-tymu-dashboard-validace-a-kontrola-pameti) · [Technické zdraví projektu](praxe/organizace-projektu.md#technicke-zdravi-projektu-kontroly-od-prvniho-dne-po-vydani)

### DAW

**Program na tvorbu hudby — nahrávání, MIDI, piano roll, mix, export (digital audio workstation).**

FL Studio, Ableton, Reaper, GarageBand nebo bezplatné LMMS. Srdce celého procesu; stačí ti stock nástroje, co s ním přijdou. Reaper má neomezenou zkušební verzi.

Kde se s tím potkáš: [Zdarma a rychle: nástroje a game jam](hudba/nastroje-zdarma-a-game-jam.md)

### Decal

**Materiál promítnutý na povrch světa — otisky, cákance, graffiti; spawnuje se za běhu bez úpravy podkladu.**

`Spawn Decal at Location` s velikostí a rotací; materiál v režimu deferred decal (translucent). Umístění: bod dopadu + normála × malý offset proti z-fightingu; rotace z normály povrchu, ať decal „leží". S dynamic material instancí jde per decal řídit texturu, barvu i fade-out v čase.

Decal nemusí být jen promítnutý materiál. Mesh decal je plovoucí geometrie s texturou z atlasu, která přikryje spoj nebo přidá poškození.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Decaly jako spoj kusů](praxe/modularni-kity.md#organicky-kit-a-spoje-zaborit-nechat-rust-od-zdroje-zakryt-sev) · [Alan Wake 2: stopy, které si pamatují](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les) · [AC Black Flag: mesh decaly](praxe/env-technika.md#ac-black-flag-resynced-prodat-iluzi-ne-postavit-skutecnost)

### Delegate

**Seznam odběratelů, kterým objekt pošle zprávu, když se něco stane — v Blueprintu se mu říká event dispatcher.**

Engine má vlastní delegáty, ke kterým se dá přihlásit zvenčí: `Landed` u Characteru (dopad na zem), `OnTakePointDamage` u aktéra. Komponenta se k nim přihlásí přes `Bind`/`Assign` a nemusí čekat, až jí vlastník zavolá. Dokud nikdo neodebírá, rozeslání skoro nic nestojí, takže přihlášením a odhlášením jde zapínat i logiku v ticku.

Kde se s tím potkáš: [Dvě komponenty: útočník a terč](praxe/souboj.md#dve-komponenty-misto-bojove-postavy-utocnik-a-terc) · [Útok je časová osa](praxe/souboj.md#utok-je-casova-osa-montaz-okna-z-notify-a-stav-ktery-se-musi-vratit) · [Sto health barů](praxe/ui-ve-svete.md#sto-health-baru-logika-na-ticku-a-prekresleni-jsou-dve-ruzne-ceny) · [Rejstřík: Event dispatcher](#event-dispatcher)

### Delta time

**Čas uplynulý od minulého snímku; násobí se jím každý pohyb, aby nezávisel na výkonu počítače.**

Bez delty znamená `position.x += 1` „jeden pixel za snímek", tedy rychlost svázanou s framerate — na silnějším stroji poletí objekt rychleji. S deltou (`position.x += speed * delta`) je jednotka *za sekundu* a chování je všude stejné. Pravidlo palce: máš-li rychlost, kterou si nastavuješ, nejspíš ji máš násobit deltou. Mez: při velkých výpadcích framerate může být posun za snímek větší než tloušťka kolizního tvaru a objekt „proskočí" — proto se fyzika počítá v pevném rytmu.

Kde se s tím potkáš: [První hra: delta a physics process](godot/prvni-hra.md#delta-a-physics-process-proc-se-rychlost-nasobi-casem)

### Denoiser

**Filtr, který z obrazu spočítaného z málo vzorků odstraní šum, obvykle s pomocí předchozích snímků.**

Ray tracing, Lumen i MegaLights počítají s omezeným počtem paprsků na pixel a výsledek by bez denoiseru zrnil. Čím méně vzorků připadne na jedno světlo, tím víc práce denoiser má a tím spíš obraz v čase bliká nebo se za pohybem táhne. Kvalita se proto ladí hlavně tím, kolik toho na jeden pixel připadne, ne silou filtru.

Kde se s tím potkáš: [Rozpočet vzorků na pixel](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis) · [Attenuation radius jako hlavní páka](praxe/megalights.md#attenuation-radius-jako-hlavni-paka-pocitej-prekryvy-ne-svetla) · [Rejstřík: TSR](#tsr)

### Design by constraint

**Metoda hledání nápadů: nejdřív si zvol omezení, která řežou scope, a nápad nech vzniknout uvnitř nich.**

„Žádný příběh", „celá hra na jedné obrazovce", „žádné viditelné postavy", „jeden level" — omezení zmenší prostor možností tak, že se v něm dá tvořit. Postup: zvol omezení → posbírej hry se stejným omezením jako katalog interakcí → nech omezení třít o téma, dokud nevypadne nápad (piráti × jedna obrazovka = ostrov). Mini Metro tak vzniklo doslova. Druhá půlka metody: každé vývojářské omezení potřebuje player-facing alibi — téma, které ho vysvětlí a prodá.

Kde se s tím potkáš: [Scope: malé hry a design by constraint](teorie/scope.md) · [Prototypování](teorie/prototypovani.md)

### Demo

**Veřejná verze hry, jejímž úkolem je hru prodat — ne ji otestovat.**

Rozdíl proti playtestovacímu buildu je zásadní: demo předpokládá, že už víš, že hra baví. Většina hráčů od něj čeká vertical slice; nejčastější chyba je „diagonální řez", kdy demo naznačí systémy, které pak neukáže. Test dobrého dema: odpovídá na pochybnosti, které bude mít fanoušek žánru.

Kde se s tím potkáš: [Vydání hry: demo prodává, prototyp validuje](teorie/vydani-hry.md) · [Playtesting](teorie/playtesting.md)

### Design pattern

**Pojmenované řešení opakujícího se programátorského problému — slovník, ne dogma.**

Katalog 23 vzorů sepsala v roce 1994 „Gang of Four" do tří rodin: creational (vznik objektů), structural (vztahy), behavioral (komunikace). Vzory nejsou vynálezy, ale jména pro řešení, která dobří programátoři nacházejí opakovaně — a kdo je zná, umí pojmenovat, co staví.

Kde se s tím potkáš: [Design patterns](teorie/design-patterns.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md)

### Design pillars

**2–3 pojmy popisující, co má hráč cítit — a váha, proti které se měří každé rozhodnutí vývoje.**

Pilíře nejsou žánr ani art style („third person shooter" je popis kamery, ne pilíř) — popisují emoce a zkušenost koncového hráče. God of War 2018: exploration, combat, pouto otce a syna; SOMA: everything is story, trust the player. Šetří rozhodování: co pilíře nesytí, letí.

Kde se s tím potkáš: [Zábava: taxonomie a pilíře](teorie/zabava.md) · [Ludotematický soulad](teorie/ludonarativni-soulad.md) · [GDD: pilíře, publikum, jádro](teorie/gdd.md)

### Dependency stack

**Diagram závislostí systémů hry: dole core mechaniky, nahoře obohacení, které jde kdykoli škrtnout.**

Rodiny potřebují postavy, místnosti potřebují stavební mechaniku — pořadí práce padá ze stromu samo a škrty se dělají shora. Sdílený spodek stacku je důvod, proč studia vyrábějí variace téže hry (Fallout/Elder Scrolls).

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Zápisek: Derivační řetěz IZBY](zapisky/derivace-izby.md)

### Device profile

**Hierarchická sada nastavení a konzolových proměnných pro konkrétní platformu — povinná výbava projektu, který míří na 60 FPS.**

Profily se dědí, takže se dá postavit celý strom (projekt → platforma → výkonový režim) a přenastavit v něm každou console variable i texture LOD group naráz. Typický obsah 60FPS profilu: scalability skupiny, rozlišovací žebřík (`r.DynamicRes`, `r.ScreenPercentage`, `r.SecondaryScreenPercentage.GameViewport`) a rozpočet snímku pro dynamické rozlišení. Past: **engine si profil sám nevybere** — potřebuješ device profile selector, který ho podle platformy zvolí. Zakládá se v prvním changelistu; dodělávat to v produkci je mnohem dražší.

Kde se s tím potkáš: [Prvních 16,66 ms se rozdává v CL1](praxe/rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Rejstřík: Scalability groups](#scalability-groups) · [Škálování MegaLights na slabší hardware](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis)

### Devlog

**Video (či zápis) o vývoji vlastní hry — marketingový kanál a žánr s vlastním řemeslem.**

Dvě funkční podoby: showcase (rozbor jedné feature: proč → proces → výsledek → limity) a story (příběh vývoje, včetně slepých uliček); nejlepší devlogy obojí mísí. Klíč ke kvalitě je scénář — psaný nahlas, ne jako sloh — a hra na obrazovce po celou dobu. Devlog není povinnost: dělá se, když tě baví videa, ne pro automatické wishlisty.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Zápisky: devlog jako mapa](zapisky/devlog-jako-mapa.md) *(devlog jako interní nástroj, ne marketing)*

### Diegetic UI

**Rozhraní, které je součástí herního světa a existuje i pro postavy v něm — obrazovka televize, displej na zbrani, mapa v ruce.**

Opakem je klasické UI přes obrazovku. Diegetické menu prodlouží imerzi až do menu a hororu dá atmosféru od první minuty. Cenou je ovládání: paprsek z virtuální myši, kolize, které mu stojí v cestě, a navigace gamepadem, kterou je potřeba vyřešit zvlášť. V UE stojí na [Widget Component](#widget-component) a [Widget Interaction Component](#widget-interaction-component).

Kde se s tím potkáš: [Menu jako předmět ve scéně](praxe/ui-ve-svete.md#menu-jako-predmet-ve-scene-widget-na-televizi-a-virtualni-mys) · [Imerze](teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida)

### Direct Mesh Controls

**Controly rigu, které animátor ovládá tahem přímo za povrch postavy místo kroužků a tvarů kolem ní (5.8, experimentální).**

Rigger přiřadí controlům skupiny polygonů (polygroups uložené ve skeletal meshi, start odvozený ze skin weights) a animátor si je může přemalovat. Vrstvy polygroups sledují stav rigu: ve FK patří plochy paže k jednotlivým kostem, v IK k pole vectoru a IK controlu. Do existujícího rigu se přidávají pluginem a modulem, bez přestavby.

Kde se s tím potkáš: [Rig, který se přenese](praxe/animace-nastroje.md#rig-ktery-se-prenese-controly-na-kuzi-moduly-a-tvary-bez-navratu-k-riggerovi) · [Rejstřík: Control Rig](#control-rig)

### Distance field AO

**Ambient occlusion počítaný z mesh distance fields; v UE se tiše zapíná spolu s movable skylightem.**

Je to jedna ze tří různých metod AO, které v UE5 mohou běžet naráz (dál Lumen AO a post-process AO), a je to nejméně známá skrytá cena: nastavíš-li skylight na *movable*, platíš ji, i když o ní nevíš. Přepnutí na *stationary* ji vypne. Rozdíl je nejlépe vidět ve scénách s vegetací.

Kde se s tím potkáš: [Rozpad ceny výchozí scény](praxe/lehky-render.md#rozpad-ceny-vychozi-sceny-a-cim-ji-nahradit) · [Rejstřík: Ambient occlusion](#ambient-occlusion) · [Rejstřík: Mesh distance field](#mesh-distance-field)

### Difficulty curve

**Průběh obtížnosti hry v čase — a hlavní nástroj, jak držet hráče ve flow.**

Skládá se ze dvou složek: novelty (učení nového) a mastery (zvládání naučeného). Šachy mají novelty nafrontovanou na začátek; hry často volí pilový tvar — s každou novou mechanikou schválně klesnou nároky na mastery, aby zbyla kapacita na učení. Doplňkové nástroje: matchmaking, automatické přizpůsobení, skill gates (těžší vstup filtruje nepřipravené) a rubber banding.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Disonance

**Dojem napětí či drsnosti při současném znění tónů; opak konsonance.**

Fyzikálně vzniká ze záznějů blízkých frekvencí a nedokonalého rozlišení ucha. Není to vypínač, ale spojité pásmo — použitelné jako řízená páka napětí (horor, boss vs. klid, domov).

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### DLSS

**NVIDIA upscaler: hra se renderuje v nižším rozlišení a AI ji dopočítá do nativního — víc FPS, u 4.5 i stabilnější obraz.**

Do projektu přes plugin z NVIDIA developer webu (složky do engine Plugins). Blueprint vzor: Query Support → Set Mode (quality = 66 % rozlišení, ultra performance = 33 %); k tomu Frame Generation (násobení snímků) a Reflex (nižší latence). Nezapomeň kompenzovat mip/LOD bias — engine při nižším interním rozlišení potichu sníží kvalitu textur i Nanite. Multiplatformní alternativa v enginu je TSR.

Kde se s tím potkáš: [Textury a DLSS](praxe/textury-a-dlss.md)

### DNA soubor

**Popis vyřešené MetaHuman hlavy — topologie a proporce namapované na tvůj mesh.**

Vzniká krokem Save Pose v MetaHuman Creatoru po úspěšném solve a je vstupem pro všechno další: z něj se generuje skeletal mesh pro přenos textury a podle jeho referenční pózy se zarovnávají doplňky, které solver ignoroval (rohy, velké uši). Bez uloženého DNA se pozdější kroky nedají zopakovat.

Kde se s tím potkáš: [MetaHuman: z cizího meshe](praxe/metahuman.md#z-ciziho-meshe-metahuman-solve-prenos-textury-a-prichyceni-rohu) · [DevKit: DNA jako open source](praxe/metahuman.md#metahuman-jako-standard-auto-rigging-cizich-postav-davy-a-otevreny-rig)

### Dogfooding

**Používání vlastního produktu jako jeho první a nejpřísnější zákazník.**

Nejlevnější test, že nástroj, komponenta nebo engine unese reálnou práci: postav na něm vlastní věc dřív, než ho dáš ostatním. Náklady vložené do dogfoodingu (hra na vlastním frameworku, demo na vlastním enginu) se konvertují do hodnoty produktu — nálezy přicházejí dřív než support tickety a roadmapa nástroje dostává tvar podle skutečného konzumenta, ne podle domněnek.

Kde se s tím potkáš: [Zápisky: pravidlo 70/30](zapisky/pravidlo-70-30.md) · [Zápisky: devlog jako mapa](zapisky/devlog-jako-mapa.md)

### Do Once

**Blueprint uzel, který propustí exekuci jen poprvé — další průchody blokuje, dokud ho něco nezresetuje.**

Nejjednodušší pojistka proti opakovanému spuštění, typicky u trigger boxu: cutscéna se nespustí znovu, když postava během sekvence projde triggerem podruhé. Reset z jiného místa (druhý trigger, časovač) z něj udělá jednoduchou stavovou logiku — elegantní pro jeden případ, nepřehlednou pro víc.

Kde se s tím potkáš: [Cutscéna, která vrátí hru tam, kde skončila](praxe/cutsceny.md#cutscena-ktera-vrati-hru-tam-kde-skoncila) · [Chase a ztráta zájmu](praxe/ai-zaklady.md#chase-a-ztrata-zajmu-do-once-a-retriggerable-delay) · [Rejstřík: Trigger volume](#trigger-volume)

### Dot product

**Skalární součin dvou jednotkových vektorů = kosinus úhlu mezi nimi: 1 stejný směr, 0 kolmost, −1 protisměr.**

Nejlevnější odpověď na otázku „jak moc se dva směry shodují": pár násobení a součtů, žádná goniometrie za běhu. Stojí na něm osvětlení (L·N), zorná pole AI (porovnej dot s cos poloviny FOV) i rozhodnutí „je cíl přede mnou, nebo za mnou" (znaménko).

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md) · [AI vnímání](praxe/ai-vnimani.md) · [Výběr grip pointu](praxe/interakcni-animace.md#jedna-animace-zvednuti-pro-vsechno-grip-pointy-a-pozy-ruky) · [Terč: směr rány](praxe/souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave)

### Draw call

**Příkaz CPU pro GPU „vykresli tohle" — každý unikátní objekt s unikátním materiálem znamená jeden navíc.**

Tisíce draw calls zahltí CPU dřív, než GPU vůbec začne kreslit. Léky: instancing (stejný mesh + materiál = jeden call pro všechny výskyty), trim sheety a atlasy (víc objektů sdílí materiál) a auto-instancing enginu — v UE4 vázaný i na stejnou lightmapu (trik The Ascent: větší lightmapy = −10 % calls). Pro artistu metrika číslo jedna: šetří se návrhem assetů, ne až profilerem.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md) · [Kit a slučování na konci](praxe/modularni-kity.md#kit-jako-lego-co-nejmene-kusu-mrizka-v-metrech-a-zoo-na-zkousku) · [Kitbashing se sdíleným shaderem](praxe/modularni-kity.md#organicky-kit-a-spoje-zaborit-nechat-rust-od-zdroje-zakryt-sev)

### Dynamic Material Instance

**Kopie materiálu vytvořená za běhu (`Create Dynamic Material Instance`), jejíž parametry jdou měnit z kódu.**

Scalar/vector/texture parametry pojmenované v materiálu se nastavují uzly Set Parameter Value — jména musí sedět do písmene. Základ všeho, co se vizuálně mění za hry: slábnoucí stopy, zabarvení zásahu, progres přebíjení. MID žije per objekt — změna jedné instance neovlivní ostatní.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Health bar z materiálu](praxe/ui-ve-svete.md#health-bar-nad-hlavou-screen-space-ukazatel-z-materialu-a-dojezd-poskozeni) · [Záblesk a kapow](praxe/souboj.md#zablesk-a-kapow-efekt-musi-sedet-na-tele-i-mezi-tely) · [Štětec a povrch přes MID](praxe/footsteps.md#stopy-do-hloubky-render-target-jako-platno-pod-postavou)

### Dynamic Mesh

**Mesh, který jde v editoru i za běhu měnit kódem; s touhle editovatelnou geometrií pracuje Geometry Script.**

Dynamic mesh actor nebo komponenta drží geometrii, kterou nástroje tvarují, ořezávají booleanem nebo přemeshují. Do hry se výsledek obvykle zapeče do static meshe, který má Nanite, LODy a levnější render. Generated Dynamic Mesh Actor se přepočítá při každém pohybu podobně jako construction script, takže těžké operace v něm zdržují editor.

Kde se s tím potkáš: [Blok napřed, silnice potom](praxe/pcg-mesta.md#blok-napred-silnice-potom-block-processor-a-booleany) · [Nástroj pro artisty](praxe/pcg-mesta.md#nastroj-pro-artisty-bake-tlacitkem-a-drobnosti-ktere-setri-hodiny) · [Rejstřík: Geometry Script](#geometry-script)

### Dynamic resolution

**Rozlišení, které engine za běhu snižuje a zvyšuje, aby udržel cílový frame time.**

Nastavuje se rozpočtem (`r.DynamicRes.FrameTimeBudget`, typicky 16,66 ms na 60 FPS) a mezemi screen percentage — v praxi třeba 55–75 %, tedy primární rozlišení mezi ~800 a 1080. Renderuje se na něm všechno, co závisí na rozlišení; dorovnává to temporální upscaler. **Hráči to čtou jako přiznání porážky** („upscalováno z 360p"), technicky je to naopak nástroj, jak udržet plynulost v nejnáročnějších místech místo padání snímků všude.

Kde se s tím potkáš: [Jak to vidí hráč](praxe/frame-pacing.md#jak-to-vidi-hrac-360p-upscaling-a-stutter) · [Rejstřík: TSR](#tsr) · [Rejstřík: Device profile](#device-profile)

### Early access

**Placený předběžný přístup k nedokončené hře, obvykle s příslibem dalšího vývoje.**

Pro hráče je to riziko, a proto jsou u dem ostražití: kdo byl jednou popálený nedokončenou hrou, čte odmávnuté featury jako varování. Historický příklad dobré praxe je hra, která šla do early accessu jen se sandboxovým režimem, bez kampaně — tedy jako poctivý horizontal slice.

Kde se s tím potkáš: [Vydání hry](teorie/vydani-hry.md)

### ECS

**Entity Component System — entita je jen identita se skládankou dat, logiku nesou systémy, které hromadně zpracují všechny entity s určitým složením.**

Složení entity (které fragmenty a tagy má) rozhoduje, které systémy se jí věnují; změna stavu bývá jen přidání nebo odebrání tagu místo události. Data stejného složení leží v paměti za sebou, takže se procházejí levně, a protože každý systém předem deklaruje, co čte a co zapisuje, dají se systémy bez zámků plánovat paralelně. V Unrealu je to [Mass Entity](#mass-entity) — systémům se tam říká procesory a datům fragmenty. Pozor: „komponenta" v ECS je čistá data, ne actor component.

Kde se s tím potkáš: [Proč objekty zpomalují](praxe/mass-ecs.md#proc-objekty-zpomaluji-pamet-kterou-nactes-a-zahodis) · [Entita není actor](praxe/mass-ecs.md#entita-neni-actor-rozkladej-podle-pristupu-do-pameti-ne-podle-postavy) · [Rejstřík: Data-oriented design](#data-oriented-design) · [Rejstřík: Fragment](#fragment) · [Northlight v Alan Wake 2](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les)

### Edit layer

**Vrstva úprav Landscape terénu — sculpt i paint žijí v pojmenovaných vrstvách, které jdou zapínat a mazat.**

Nástroje pracují s aktuálně vybranou vrstvou: copy/paste gizmo kopíruje jen z ní (jinak prázdno), water bodies si vytvářejí vlastní vrstvu. Zhruba totéž, co v Mesh Terrainu dělají modifiery — jen bez 3D volnosti a přeskládávání priorit.

Kde se s tím potkáš: [Landscape tipy](praxe/landscape-tipy.md) · [Voda a buoyancy](praxe/voda-a-buoyancy.md)

### Editor script

**Skript, který běží v editoru místo ve hře — `extends EditorScript`, anotace `@tool`, přepsaná metoda `_run()`.**

Spouští se z palety příkazů, nespouští hru ani scénu. Používá se na generování boilerplate (vytvoř resource i skript podle zadaného jména), na hromadné úpravy assetů a — často nejužitečněji — na **kontrolu konzistence dat**: vypiš, kterým položkám chybí povinné pole. Umí si otevřít vlastní okno s UI. Unrealí protějšek je [Editor Utility Widget](#editor-utility-widget). Zlaté pravidlo: nástroj pro sebe má nejlepší poměr práce k užitku, protože se úspora násobí každým použitím.

Kde se s tím potkáš: [Nástroje pro sebe](godot/projekt-a-vykon.md#nastroje-pro-sebe-editor-script-ktery-ti-usetri-boilerplate)

### Editor Utility Widget

**Blueprint UI, které běží v editoru a automatizuje práci — vlastní nástroj bez psaní pluginu.**

Spouští se pravým klikem → Run Editor Utility Widget a dá se ukotvit vedle ostatních panelů. Typické použití: dávkové přejmenování, kontrola konvencí, přepínání zobrazení scény. Protože je to obyčejný blueprint, jde cizí nástroj otevřít, přečíst a upravit — což je zásadní rozdíl proti zkompilovanému pluginu.

Kde se s tím potkáš: [Animační nástroje: SAM](praxe/animace-nastroje.md#sam-izolace-jednoho-aktera-jako-animatorsky-rezim) · [Editor tipy](praxe/editor-tipy.md) · [Bake tlačítkem](praxe/pcg-mesta.md#nastroj-pro-artisty-bake-tlacitkem-a-drobnosti-ktere-setri-hodiny)

### Effect type

**Asset, který dává Niagara systémům pravidla cullingu a škálování — bez něj se částice simulují i mimo obraz.**

Niagara ve výchozím stavu neculluje nic, takže padesát ambientních systémů roztroušených po levelu běží pořád. Effect type to řeší třemi nastaveními: **max time without render** (nerenderuje-li se to chvíli, zastav), **allow pre-cull by view frustum** (rozhodni už při spawnu, jestli by to vůbec bylo vidět — ideální pro krátké efekty typu záblesku výstřelu) a **cull update frequency**. Zakládá se po kategoriích, ne po systémech: jeden pro ambientní efekty, jeden pro zásahy, jeden pro projektily.

Kde se s tím potkáš: [Hodina v cizí scéně](praxe/gpu-pruchod.md#hodina-v-cizi-scene-co-se-najde-kdyz-se-hleda) · [Rejstřík: Particle system](#particle-system)

### Eigenvektor

**Směr, který lineární transformace nevychýlí — vektor zůstává na své přímce, jen se natáhne či zkrátí o eigenvalue.**

Pro každou matici jiné; párové číslo eigenvalue říká, kolikrát se eigenvektor při transformaci škáluje. U symetrických matic jsou eigenvektory navzájem kolmé, což umožňuje spektrální rozklad: rotace na osy → škálování → rotace zpět.

Kde se s tím potkáš: [Lineární algebra vizuálně](teorie/linearni-algebra-vizualne.md)

### Elemental tetrad

**Čtyři části každé hry podle Jesseho Schella: estetika, mechaniky, technologie a příběh.**

Z knihy The Art of Game Design. Užitečný ne jako škatulky, ale jako kontrolní seznam iterace: každé kolo vývoje má projít všemi čtyřmi — kdo jede jen ve své silné čtvrtině, hru nezlepšuje, jen leští jednu její stěnu.

Kde se s tím potkáš: [Prototypování: iterační spirála](teorie/prototypovani.md) · [Základy designu](teorie/zaklady.md)

### Elevator pitch

**Popis hry na délku jízdy výtahem — nejčastěji ve formátu „X meets Y".**

Kombinace selhává dvěma způsoby: redundancí („The Walking Dead meets Day of the Dead" — totéž dvakrát) a nespojitelností (prvky, které hlava neposkládá). Dobrý pitch je teze, kterou zbytek dokumentu obhajuje — Monaco: „mechaniky Pac-Mana oženěné se stealth prvky Hitmana", a pak bod po bodu proč. Srovnej s pitch deckem — pitch je věta, deck je prezentace.

Kde se s tím potkáš: [GDD: Monaco](teorie/gdd.md) · [Nápad](teorie/napad.md)

### Enum

**Datový typ s pevným seznamem pojmenovaných hodnot — směr zásahu, druh klíče, končetina.**

V Blueprintu se zakládá jako samostatný asset (Enumeration) a používá se v `Switch on`, v `Select` nebo jako klíč mapy. Proti stringu má výhodu, že se nedá napsat špatně a editor nabídne rozbalovací seznam; proti boolu, že unese víc než dva stavy. Hodnota „none" se vyplatí tam, kde systém někdy odpověď nemá.

Kde se s tím potkáš: [Terč: směr rány](praxe/souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave) · [Zdraví po končetinách](praxe/souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav) · [Hádanka ze stavebnice](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit) · [Směrové hit reakce](praxe/mm-systemy.md#smerove-hit-reakce-dot-product-rozhodne-odkud-chooser-vybere-co)

### Environmental storytelling

**Vyprávění prostorem: rozmístění objektů říká, co se tu stalo, dřív než padne jediné slovo.**

Převrácená židle, otevřený šuplík a stopy používání (edge wear, škrábance u dveří, prach v koutech) skládají historii místa. Funguje i kompozičně — stopa předmětů vede hráče ke dveřím — a v hororu buduje napětí dřív, než se cokoli stane. Opak: sterilně čisté a symetrické prostory, které křičí „kulisa".

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md) · [Vedení hráče](teorie/vedeni-hrace.md)

### EQ

**Zesílení nebo potlačení konkrétních frekvencí ve zvuku (equalizace).**

Čištění šumu, zvýraznění či ztlumení tónů, prosazení zvuku v mixu. Spolu s attenuation a reverbem základní nástroj tvarování herního zvuku.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Equipment Instance

**Objekt, který vznikne při nasazení kusu vybavení a pamatuje si, co spawnul a co změnil — aby šlo všechno vrátit.**

Jeden ze čtyř dílů systému vybavení: *definition* (jaký aktér, jaký socket), *instance* (účetní kniha jednoho nasazeného kusu), *manager* komponenta (vytváří instance, hlídá sloty) a samotný *actor* ve světě. Instance drží odkaz na zdrojovou [item instance](#item-instance) — položka v batohu a nasazený kus jsou dvě různé věci. Při sundání zničí aktéra, vynuluje referenci a vrátí aplikované staty. Stejné rozdělení používá Lyra.

Kde se s tím potkáš: [Vybavení je samostatný systém](praxe/inventar.md#vybaveni-je-samostatny-system-definice-instance-manazer-a-akter) · [Staty: modifikátory při vybavení](praxe/inventar.md#staty-nahoda-pri-vzniku-modifikatory-pri-vybaveni)

### Equity

**Podíl na firmě — na rozdíl od půjčky se nesplácí, ale už nikdy se nevrátí.**

Typická cena inkubátoru: 25 000 až 50 000 € za deset procent firmy. Rozdíl proti smlouvě s vydavatelem je zásadní: u vydavatele podepisuješ jednu hru, u investora celou firmu včetně všeho, co kdy uděláš. Souvisí s tím i vnitřní rozdělení podílů mezi společníky podle toho, kdo nese jaké riziko.

Kde se s tím potkáš: [Financování](teorie/financovani.md#granty-inkubatory-a-investori-co-za-penize-odevzdas)

### Eulerovy úhly

**Rotace jako trojice yaw/pitch/roll aplikovaná v pevném pořadí — intuitivní, kompaktní, ale trpí gimbal lockem.**

Standard pro UI (v UE je to Rotator): tři čísla, kterým rozumíš. Cena: mizerná interpolace a gimbal lock — po otočení prostřední osy o 90° se vnější a vnitřní osa zarovnají a ztratíš stupeň volnosti. Uvnitř enginu proto rotace drží kvaterniony.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Euklidovský rytmus

**Zápis `(n,k)`: rozprostři `n` hitů co nejrovnoměrněji do `k` kroků.**

Vznikl ve fyzice — šlo o to, jak v daném časovém okně poslat částice co nejvíc rozestoupené — a ukázalo se, že výsledné vzorce **odpovídají rytmům z mnoha různých kultur**. V praxi je to nástroj na objevování: nevíš, jak má groove znít, změníš jedno číslo a dostaneš jiný. Protiklad k tomu je zápis, kde přesně řekneš, na kterých krocích se hraje. Výhrada: prostor možností je úzký, takže po chvíli **zní euklidovské rytmy poznatelně** — dobré na základ, ne na všechno.

Kde se s tím potkáš: [Euklidovské rytmy a řízená náhoda](hudba/live-coding.md#euklidovske-rytmy-a-rizena-nahoda) · [Rejstřík: Synkopa](#synkopa)

### EV100

**Jednotka expozice: kolik světla pustí kamera do obrazu — EV100 = 1 odpovídá modré hodině, interiér ~5–7, slunečný den ~13.**

Zamčení min = max EV100 v post-process volume vypne auto-exposure a jas scény řídíš ty. Pozor na kopírovaný recept „nastav 1/1": jednička sedí jen velmi tmavým scénám — hodnota se volí podle scénáře a podle toho, pro co exponuješ (slunce, nebo stíny). Vyšší číslo = tmavší obraz.

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Stavba prostředí](praxe/env-tvorba.md)

### EVDB

**Komprimovaný volumetrický asset pluginu Expanse — static mesh, který místo trojúhelníků nese objem.**

Expanse Volume Database drží mrak, kouř nebo oheň ve formě, která zůstává komprimovaná po celou pipeline, takže se dá v levelu duplikovat po stovkách. Rozdíl proti Volume aktéru je tentýž jako mezi static meshem a jeho aktérem: EVDB jsou data, Volume je to, co je zobrazuje. Vzniká konverzí z OpenVDB.

Kde se s tím potkáš: [Osvětlení: objemy přes EVDB](praxe/osvetleni.md#objemy-pres-evdb-mraky-a-mlha-jako-asset)

### Event bus

**Globální kanál událostí: jedno místo, kde jsou deklarované signály, které zajímají víc nepříbuzných systémů.**

V Godotu se dělá jako [autoload](#autoload) obsahující jen signály (žádnou logiku). Řeší problém, na který nestačí přímé propojení: **dynamicky vznikající objekty**, které v době startu scény ještě neexistují, a systémy, které spolu ve stromu nemají žádný rozumný společný bod. Cena je dohledatelnost — u přímého spojení vidíš, kdo koho poslouchá, u autobusu to musíš hledat fulltextem. Proto do něj patří jen události s víc posluchači; cokoli s jedním posluchačem tam nepatří. Unrealí příbuzní: broadcast přes subsystem a event manager.

Kde se s tím potkáš: [Event bus](godot/signaly.md#event-bus-kdyz-se-systemy-nemaji-cim-potkat) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md#ctvrty-kanal-broadcast-pres-subsystem-s-payloady)

### Event dispatcher

**Rádio mezi Blueprinty: vlastník dispatcher zavolá, všichni přihlášení posluchači dostanou event.**

Deklaruje se na vysílači; posluchači se bindují (typicky na BeginPlay) a dodávají vlastní custom event. Umí parametry, unbind i více posluchačů najednou — a obrací závislost: vysílač o posluchačích neví. Použití: „stalo se X, koho to zajímá" (dveře otevřeny, cooldown skončil, aktivita zaznamenána). Pozor na race conditions při bindování v BeginPlay — pořadí inicializace actorů není zaručené.

Dispatcher, který nikdo neodebírá, se rozešle skoro zadarmo. Logiku v ticku proto jde zapínat a vypínat přihlášením a odhlášením (dojezd health baru jen po dobu pohybu).

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Principy architektury](praxe/principy-architektury.md) · [Telemetrie](praxe/telemetrie.md) · [Sto health barů: odběr jen po dobu pohybu](praxe/ui-ve-svete.md#sto-health-baru-logika-na-ticku-a-prekresleni-jsou-dve-ruzne-ceny)

### Event Tick

**Blueprint event volaný každý vykreslený snímek.**

Kód v Ticku běží 60× i vícekrát za vteřinu, ať se děje cokoli — je to polling: neustálé kladení otázky, jejíž odpověď se většinou nemění. Občas je nutný (plynulý pohyb, interpolace), ale většina herní logiky patří do eventů, timerů a delegátů, které se spouštějí při změnách. „Dostaň to z Ticku" je jedna z nejčastějších optimalizačních rad v UE — a hlavně rada architektonická.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md) · [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md) · [Sto health barů](praxe/ui-ve-svete.md#sto-health-baru-logika-na-ticku-a-prekresleni-jsou-dve-ruzne-ceny) · [Barel, který teče](praxe/pasti-a-mechaniky.md#barel-ktery-tece-diry-jako-data-hladina-jako-jedno-cislo) · [Build, který Event Tick odmítne](praxe/mcp-v-editoru.md#jak-s-agentem-v-editoru-mluvit-presna-jmena-jeden-ukol-a-kontext-ktery-se-vejde)

### Export template

**Předkompilované běhové prostředí Godotu pro cílovou platformu; stahuje se zvlášť, není součástí instalace.**

Důvod, proč se Godot vejde do několika desítek megabajtů: engine si s sebou nenese buildy pro Windows, Linux, macOS, web a mobil. Před prvním exportem je proto potřeba je stáhnout (`Editor → Manage Export Templates`). Šablony jsou vázané na verzi enginu — po upgradu se stahují znovu.

Kde se s tím potkáš: [První hra: nastavení projektu](godot/prvni-hra.md#nastaveni-projektu-je-soucast-hry-ne-administrativa)

### Expresivní mechanika

**Mechanika, která nepomáhá vyhrát, ale mění, jak hra chutná: pohladit kočku, emoty, rozbíjení beden bez lootu.**

Rádio a klimatizace auta vedle pedálů. Do prototypu nepatří (jádro první), ale bývá rozdílem mezi docela dobrou a výbornou hrou: vyrábí hravost (paidia), nechává hráče zanechat stopu a projevit vkus — a publikum ji čte jako attention to detail.

Kde se s tím potkáš: [Systémy a mechaniky](teorie/systemy-a-mechaniky.md)

### Extremistan

**Prostředí, kde jeden vzorek může převážit celý zbytek souboru — opak průměrovatelného světa.**

Talebův pojem: v Mediocristanu (tělesná výška) žádný jednotlivec statistiku nezmění, v Extremistanu (příjmy, prodeje her) ano. Prodeje na Steamu do Extremistanu patří — medián a průměr se liší o řády, takže „průměrná hra vydělá X" je neinformativní číslo. Praktický důsledek: strategie musí počítat s tím, že drtivá většina pokusů skončí u nuly a hodnota přijde ze vzácné události.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#extremistan-tri-mechanismy-ktere-vedou-ke-stejne-strategii)

### Fallback mesh

**Klasická, ne-Nanite verze Nanite meshe — engine ji použije tam, kde Nanite nejde nebo kde plná geometrie není potřeba.**

Slouží mimo jiné odrazům, ray tracing scéně, Lumenu a platformám bez podpory Nanitu; protože se v nich drobný rozdíl nepozná, snese výrazně méně trojúhelníků. V editoru meshe se mezi Nanitem a fallbackem přepíná zobrazení (`Ctrl+N`), takže fallback poslouží i jako náhled: dočasně mu nastavíš procento trojúhelníků a z běžné vzdálenosti zjistíš, kolik detailu je vidět — to číslo pak patří do [Keep Triangle Percent](#keep-triangle-percent).

Kde se s tím potkáš: [Nanite a velikost balíčku](praxe/nanite-do-hloubky.md#nanite-a-velikost-balicku-data-ktera-se-nikdy-nevykresli) · [Rejstřík: Nanite](#nanite)

### File locking

**Zamčení souboru tím, kdo na něm pracuje — ostatní ho nemůžou upravit; odpověď na binární assety, které se nedají sloučit.**

Git počítá s tím, že se změny dvou lidí sloučí; u souborů z Photoshopu, Blenderu nebo u scény to nejde. Proto mají herní verzovací nástroje zámky (exclusive checkout) a nad Gitem se doplňují zvlášť. Pro sólo projekt zbytečné — potřeba začnou být s druhým člověkem na projektu.

Kde se s tím potkáš: [Git v Unrealu: kde přestane stačit](praxe/organizace-projektu.md#git-v-unrealu-verzovani-z-editoru-a-cesta-zpet-v-case) · [Rejstřík: Version control](#version-control)

### Fill

**Zahuštění rytmu na konci fráze, které připraví posluchače na příchod další sekce.**

Typicky se přidá synkopa, snare na slabé doby, pár kopáků navíc na osminy nebo tomy. Platí přímá úměra: čím větší změna přijde v další sekci, tím větší fill si zaslouží. Opakem je **prázdno (empty)** — místo přidání se většina rytmických prvků naopak ubere, čímž vznikne vakuum, na jehož zaplnění posluchač čeká. U herní hudby je prázdno cennější, protože **zamaskuje šev smyčky**.

Kde se s tím potkáš: [Za jeden takt: fráze, fill a prázdno](hudba/rytmus.md#za-jeden-takt-fraze-fill-a-prazdno) · [Rejstřík: seamless loop](#seamless-loop)

### Find the fun

**Fáze prototypování: experimentuj s jádrem hry, dokud nezačne bavit samo o sobě.**

Indikátor nalezení: přistihneš se, že si s barebones mechanikou hraješ mimo pracovní dobu — „chtěl jsem vylézt na všechno, co šlo". Druhá podoba téhož: když tě při vývoji baví něco jiného, než co sis naplánoval, následuj to — Ape Out vznikl z ninja stealth hry, protože strkání nepřátel bavilo víc než plížení.

Kde se s tím potkáš: [Scope: malé hry v praxi](teorie/scope.md) · [Nápad: ideace](teorie/napad.md)

### Fixed point

**Čísla s pevnou desetinnou čárkou: celé číslo, které znamená zlomky jednotky, třeba 256 dílků na metr.**

Na rozdíl od floatu mají stejnou přesnost v jakékoli vzdálenosti od počátku, za cenu pevného rozsahu. Při 256 hodnotách na metr dá 32bitové celé číslo přesnost na pár milimetrů a rozsah zhruba ±8 000 km. Pasti jsou jiné než u floatu, hlavně přetečení, třeba při sčítání dvou velkých souřadnic.

Kde se s tím potkáš: [Dohled na kilometry](praxe/velke-svety.md#dohled-na-kilometry-vetsi-chunky-v-dalce-stromy-se-stinem-a-souradnice-ktere-nepretecou) · [Rejstřík: Origin shifting](#origin-shifting)

### Flipbook

**Mřížka snímků v jedné textuře, kterou materiál přehrává jako animaci.**

Standardní způsob, jak do hry dostat výbuch, kouř nebo jiskry bez simulace: 4×4 nebo 8×8 políček v jednom obrázku a uzel, který mezi nimi posouvá UV. Levné na paměť i na výkon, ale rozlišení každého snímku je zlomkem textury — proto se hodí na efekty, které hráč vidí krátce a v pohybu.

Kde se s tím potkáš: [Materiály: VFX textury](praxe/materialy.md#vfx-textury-nedelat-je-a-kdyz-uz-tak-v-krite) · [Tech art a VFX](teorie/art-specializace.md#vfx-primarni-sekundarni-terciarni-a-rozpocet-na-okazalost)

### Flow

**Stav plného zaujetí činností, kdy výzva přesně odpovídá dovednosti (Mihály Csíkszentmihályi, 1990).**

Podmínky: častá a rychlá zpětná vazba, hluboké soustředění, výzva ~ skill. Tyrollerovo vysvětlení, proč flow kanál funguje: je to pásmo nejlepšího poměru signálu k šumu — ve frustraci vrací svět pořád „špatně" a v nudě pořád „dobře", učit se dá jen tam, kde některé akce fungují a jiné ne. Prakticky: flow = nejefektivnější učení = zábava; frustrace emočně přebije flow, flow přebije nudu.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Foley

**Ruční výroba zvukových efektů z reálných předmětů.**

Když knihovna nestačí, zvuk se nahraje z fyzických rekvizit. Riot pro postavu Iverna sroubil „The Creaker" ze dvou prken, pantů a provazu, aby vrzání dodalo napětí před prasknutím štítu.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Foot placement

**Procedurální usazení chodidel na terén: IK na svazích, špendlení došlapů, tlumení roota na hrbolech.**

Řeší tři viditelné neduhy: vznášení nohou na svahu (chodidla na terén + pokles pánve, ať noha dosáhne bez hyperextenze), klouzání chodidel při blendech a rotacích (foot pinning na world-space pozici došlapu) a poskakování těla na nerovnostech (root damping pružinou podél normály terénu). V GASP existuje jako anim uzel (CMC postava) i Control Rig graf (Mover postava); došlapy řídí contact curves.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [MM základy](praxe/mm-zaklady.md)

### Forward rendering

**Způsob vykreslování, kdy se objekt nasvítí rovnou při kreslení — bez mezikroku G-bufferu, na kterém stojí výchozí (deferred) renderer UE.**

V Unrealu je to volba Forward Shading v nastavení projektu, typická pro VR a hry pro slabý hardware (běží na něm třeba bojovka 2XKO). V GPU profileru se u něj čtou poměry mezi passy: dlouhý depth pass ukazuje na moc polygonů, dlouhý base pass u jednoho draw callu na drahý shader, dlouhá translucency na [overdraw](#overdraw).

Kde se s tím potkáš: [Bojovka pro desetiletý hardware](praxe/gpu-pruchod.md#bojovka-pro-desetilety-hardware-rozpocet-po-castech-a-co-se-v-nem-naslo) · [Rejstřík: Overdraw](#overdraw) · [MegaLights s forward shadingem nefungují](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis)

### Four-on-the-floor

**Bicí groove s kopákem na každé ze čtyř dob taktu.**

Základ house a další taneční hudby. Protože je pravidelný, staví se proti němu synkopovaná melodie a bas, aby vznikl tah a groove.

Kde se s tím potkáš: [Žánry a jejich melodie](hudba/zanry-a-styl.md) · [Aranžmá: z loopu skladba](hudba/aranz.md)

### Frame data

**Popis útoku po snímcích: kolik snímků trvá nápřah, které snímky jsou aktivní, jak dlouho je zotavení.**

Slovník bojovek, použitelný v každé akční hře. Ke každému aktivnímu snímku se dají navěsit vlastnosti — poškození, síla odhozu, [hit stop](#hit-stop), otřes obrazovky, stavové efekty — a protože jeden snímek animace může mít víc [hitboxů](#hitbox), dá se útok rozřezat na části s různým chováním (odhoz jen na chodidlech, jed jen na špičce biče). Kritická podmínka při stavbě: **časování musí mít jediný zdroj pravdy**, typicky animaci samotnou — data ve dvou místech se při první úpravě animace rozejdou.

Kde se s tím potkáš: [Frame data: definuj systém dřív, než ho postavíš](godot/pripadovka-nepratele.md#frame-data-definuj-system-driv-nez-ho-postavis) · [Active frames v UE](praxe/souboj.md#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames)

### FM syntéza

**Syntéza, kde jeden signál rozkmitává frekvenci druhého — místo aby se z bohatého zvuku ubíralo filtrem.**

Nejdůležitější parametr není hloubka modulace, ale **harmonicita** — poměr frekvence modulátoru k nosné. Nízké poměry zní jako vibráto, vysoké a neceločíselné dávají kovové alikvóty, celočíselné drží zvuk laděný. Výpočetně levné a zvukově drahé, proto na tom stála éra konzolového a automatového zvuku. Úzký použitelný recept: **sinus + FM + krátká obálka = zvonek nebo perkuse**. Výhrada: ladí se hůř než subtraktivní řetězec — nejdřív hledej poměr, pak tvaruj obálkou.

Kde se s tím potkáš: [FM: když jeden zvuk ohýbá druhý](hudba/synteza-zvuku.md#fm-kdyz-jeden-zvuk-ohyba-druhy) · [Rejstřík: subtraktivní syntéza](#subtraktivni-synteza) · [Rejstřík: oscilátor](#oscilator)

### Fragment

**Objekt, který k definici položky připojí kus dat a kus funkčnosti — kompozice místo jedné obří třídy.**

Řeší, že ne všechny položky mají totéž: co má reprezentaci ve světě, dostane fragment světové reprezentace; co se dá vybavit, fragment vybavení. Definice položky pak drží jen společné vlastnosti a **pole fragmentů**. Vzor stojí na třech C++ specifikátorech, které v blueprintu nejsou: **`DefaultToInstanced`** (instance se při vytvoření duplikují), **`EditInlineNew`** (fragment se přidá tlačítkem přímo v okně vlastností) a **`Instanced`** na tom poli (každá položka dostane vlastní kopii). Praktické měřítko: **vlastnost patří do fragmentu, jakmile ji nemá aspoň polovina položek.** Používá to inventář v Lyře.

V [Mass](#mass-entity) znamená fragment něco jiného: čistá data bez chování, která hromadně zpracovávají procesory — blíž členské proměnné než komponentě. Společná je jen myšlenka skládání; liší se tím, kde žije logika.

Kde se s tím potkáš: [Fragmenty: skládání položky z kusů](praxe/principy-architektury.md#fragmenty-skladani-polozky-z-kusu-misto-jedne-obri-tridy) · [Rejstřík: CDO](#cdo) · [Rejstřík: Data-driven design](#data-driven-design) · [Inventář: definice a instance](praxe/inventar.md#definice-popisuje-druh-instance-nese-kus) · [Inventář: akce](praxe/inventar.md#pouziti-jako-seznam-akci-chovani-slozene-z-malych-kroku) · [Entita není actor: fragment v Mass](praxe/mass-ecs.md#entita-neni-actor-rozkladej-podle-pristupu-do-pameti-ne-podle-postavy)

### Frame time

**Čas na vykreslení jednoho snímku v milisekundách — použitelnější metrika než FPS, protože se z ní počítá rozpočet.**

60 FPS znamená **16,6 ms na všechno dohromady**; 30 FPS je 33,3 ms. Výhoda oproti FPS je v tom, že se frame time **sčítá lineárně**: ušetříš-li 2 ms, víš přesně, kolik ti zbylo. FPS se chová nelineárně (z 200 na 100 FPS je 5 ms, ze 40 na 30 je 8 ms). Měření vyžaduje **vypnutý VSync a nenastavený strop FPS** — jinak engine čeká na monitor a měříš čekání místo práce.

Kde se s tím potkáš: [Kolik nodů je moc](godot/kompozice.md#kolik-nodu-je-moc-zmereno) · [Co skutečně stojí výkon](godot/projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek)

### Fresnel

**Materiálový uzel, jehož hodnota roste k obrysu objektu z pohledu kamery — 0 tam, kde plocha míří ke kameře, k 1 na okraji.**

Používá se na obrysové světlo (rim light), na záblesk zásahu jen po kraji postavy nebo na hrany skla. Exponent (power) a násobič ladí, jak úzký a jasný obrys bude.

Kde se s tím potkáš: [Záblesk a kapow](praxe/souboj.md#zablesk-a-kapow-efekt-musi-sedet-na-tele-i-mezi-tely)

### FX budget

**Rozpočet na částice, podle kterého engine za běhu stahuje cullovací vzdálenosti a stropy instancí.**

Zapíná se `fx.Budget.Enabled` (a `fx.BudgetInEditor.Enabled`), rozpočty na herní a render vlákno se zadávají v `ini` souborech — což je podle praktiků důvod, proč se to používá málo. Reakce jednotlivých systémů se pak řídí přes [effect type](#effect-type). Nejagresivnější varianta je „nad 50 % rozpočtu nás kroky nezajímají vůbec". **Typické selhání je oscilace**: culluješ → jsi pod rozpočtem → smí se spawnovat víc → jsi nad rozpočtem → culluješ. Léčí se zpomalením **zotavení** rozpočtu (`fx.Budget.AdjustedUsageDecayRate`), ne zpřísněním prahu — je to regulační smyčka a potřebuje hysterezi.

Kde se s tím potkáš: [Škálování a pooling](praxe/niagara-vykon.md#skalovani-a-pooling-co-vypnout-a-co-recyklovat) · [Rejstřík: Effect type](#effect-type)

### Game Design Document

**Dokument s návrhem hry (GDD) — funguje jen tehdy, když se do něj tým skutečně vrací.**

Klasická podoba (slohová práce v akademickém formátu) u sólo vývojářů umírá nedopsaná a nečtená. Funkční alternativa je vizuální nástěnka: reference s důvody, levely jako sekvence, mechaniky jako GIFy, centrální to-do. Jediná metrika kvality GDD je, jestli je *živý* — forma je vedlejší.

Kde se s tím potkáš: [GDD: dokument jako způsob myšlení](teorie/gdd.md) · [Start projektu](teorie/jak-zacit.md) · [Zápisky: GDD review](zapisky/gdd-review.md)

### Gameplay Debugger

**Ladicí vrstva přímo ve hře (klávesa apostrof): navmesh, cesta AI, behavior tree, EQS a percepce.**

Kategorie se přepínají numerickou klávesnicí (0 navmesh, 1 AI, 2 behavior tree, 4 EQS, dál percepce a smart objects). Ukáže kužel zraku, hranici ztráty cíle i to, který decorator ve stromu selhal a proč („value equals none"). U AI je to nejrychlejší cesta, protože její chyby nehlásí chybu — postava jen stojí.

Kde se s tím potkáš: [AI, která nereaguje](praxe/debugging.md#ai-ktera-nereaguje-gameplay-debugger-a-dve-tiche-priciny) · [Rejstřík: Behavior Tree](#behavior-tree) · [Rejstřík: AI Perception](#ai-perception) · [Mass Debugger](praxe/mass-ecs.md#jak-s-mass-pracovat-diagram-debugger-a-jedna-implementace-misto-dvou)

### GAS

**Gameplay Ability System — Epicův framework pro schopnosti, atributy a efekty, který hodnoty počítá ze základu a modifikátorů.**

Atribut (rychlost, zdraví) se nemění přepsáním čísla, ale **gameplay efektem** s modifikátory, které jdou zase odebrat — dočasné vlivy se tak nemohou „slít" do základu (příklad, kdy prosté sčítání skončí na 400 místo 500, je v kapitole o statech). Efekt navíc mapuje hodnotu na atribut v datech, ne v kódu. Stojí na něm Lyra; principy, ze kterých vychází (separace, data, komponenty), jsou tytéž jako v Principech architektury.

I AI může jednat přes abilitu: úloha behavior tree jen rozhodne a předá abilitě data (chůze nebo běh, animace přes tag); abilita akci provede a stromu ohlásí konec.

Kde se s tím potkáš: [Staty: modifikátory při vybavení](praxe/inventar.md#staty-nahoda-pri-vzniku-modifikatory-pri-vybaveni) · [Použití jako seznam akcí](praxe/inventar.md#pouziti-jako-seznam-akci-chovani-slozene-z-malych-kroku) · [Tři principy škálovatelnosti](praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [AI: akce v gameplay abilitách](praxe/ai-ve-velkem.md#strom-jen-rozhoduje-akce-v-gameplay-abilitach-nepritel-v-datech)

### Gauntlet

**Automatizační framework Unrealu, který spouští hru na cílových zařízeních (i víc instancí naráz) a řídí na nich testy.**

Typicky ho spouští build systém: build se rozešle na min spec PC nebo konzoli, proběhne smoke test (připojit se, projít level) nebo výkonový průchod a výsledky jdou do reportu či dashboardu. Smysl dostává ve chvíli, kdy ruční testování po každé změně přestane stačit — u her v raném přístupu s častými aktualizacemi, u výkonových dashboardů a u smoke testů na víc platformách.

Kde se s tím potkáš: [Výkon jako věc celého týmu](praxe/mereni-automaticky.md#vykon-jako-vec-celeho-tymu-dashboard-validace-a-kontrola-pameti) · [Technické zdraví projektu](praxe/organizace-projektu.md#technicke-zdravi-projektu-kontroly-od-prvniho-dne-po-vydani) · [Sto tisíc aktérů: automatizované testy](praxe/velke-svety.md#sto-tisic-akteru-co-unese-editor)

### Geometry Collection

**Asset rozbitného objektu v Chaosu: sada fyzikálních těles, která se aktualizují a kreslí společně, s úrovněmi clusteringu.**

Kusy vznikají frakturou, nedestruktivně i v Dataflow grafu, a úrovně clusteringu je seskupují do větších hmot pro simulaci. Za běhu má neměnnou rest collection z assetu a dynamickou kopii, kterou mění simulace. Opakované kusy jde kreslit jako sdílené instance a odlomené drobky jako debris bez vlivu na hru.

Kde se s tím potkáš: [Budova, kterou rozbije kdokoli](praxe/destrukce-a-latky.md#budova-kterou-rozbije-kdokoli-graf-spojeni-na-serveru-cluster-union-ve-fyzice) · [Destrukce, kterou procesor unese](praxe/destrukce-a-latky.md#destrukce-kterou-procesor-unese-konvexy-debris-sdilene-instance-a-strop-zlomu) · [Rejstřík: Cluster Union](#cluster-union)

### Geometry Script

**Knihovna funkcí v Unrealu pro modelování kódem: booleany, remesh, triangulace a další operace nad dynamic meshem.**

Běží v blueprintech i v C++ a v editoru pohání procedurální nástroje, které geometrii vyrábějí, místo aby jen rozmisťovaly hotové meshe. Interop s PCG pošle data z grafu rovnou do dynamic mesh blueprintu. Typický postup je spočítat tvar a výsledek zapéct do static meshe.

Kde se s tím potkáš: [Budova jako věta](praxe/pcg-mesta.md#budova-jako-veta-panelovy-kit-gramatika-a-patra) · [Blok napřed, silnice potom](praxe/pcg-mesta.md#blok-napred-silnice-potom-block-processor-a-booleany) · [Liány po povrchu](praxe/pcg-liany.md#liany-po-povrchu-mesh-sampler-pathfinding) · [Rejstřík: Dynamic Mesh](#dynamic-mesh)

### Gestalt

**Psychologická škola, podle níž člověk vnímá celý obraz a z uspořádání si odvozuje vztahy mezi částmi.**

Do grafického designu se dostala dávno před videohrami a odtud se přelily konvence rozhraní. Pro vývojáře z ní plyne obrácený postup: nezačínej jednotlivým assetem (na který jsi vždy zazoomovaný), ale kompozicí celku, protože hráč uvidí obrazovku najednou. Prakticky: prvky v jedné řadě čteme jako příbuzné, oddělené skupiny jako různé kategorie.

Kde se s tím potkáš: [Vizuální komunikace](teorie/vizualni-komunikace.md) · [Art specializace: UI](teorie/art-specializace.md)

### Game feel

**Hmatový dojem z ovládání hry: odezva, váha, šťavnatost interakcí — souhrn tisíce drobností, které dělají z klikání požitek.**

Screen shake, částice, zvuky zásahů, animační mikropohyby. „Game feel je cheat code": 20 % úsilí udělá 80 % dojmu a částice zamaskují nedodělky líp než cokoli jiného — proto patří i do prototypů. Zároveň platí pravidlo hraček: interakce mají být příjemné samy o sobě, dřív než na nich postavíš výzvy a cíle.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md) · [Základy: engagement a appeal](teorie/zaklady.md) · [Nápad](teorie/napad.md)

### Game Instance

**Objekt žijící od spuštění aplikace po její konec — přežívá přechody mezi levely.**

Domov pro session-wide stav: reference na SaveGame, generátory unikátních ID, nastavení. Existuje vždy (C++ default); vlastní Blueprint verze se registruje v `Project Settings → Maps & Modes → Game Instance Class`. Co do ní nepatří: per-hráč data (Player State) a per-level logika (Game Mode).

Kde se s tím potkáš: [Ukládání](praxe/ukladani.md) · [Principy architektury](praxe/principy-architektury.md)

### Game jam

**Časově omezená akce — typicky 48 hodin až týden — během níž vzniká celá malá hra, obvykle na zadané téma.**

Institucionalizovaný „malý rozsah": deadline ořeže scope za tebe a vynutí dokončení, což je přesně dovednost, kterou začátečník potřebuje trénovat nejvíc. Bonusy: publikum (ostatní účastníci hru zahrají), zpětná vazba a nulová penalizace za nedokonalost. Jamy fungují i jako „design by constraint jako služba" — omezení dostaneš zadáním; jen pozor, mechanika zábavná 10 minut nemusí unést hodinovou hru.

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Scope](teorie/scope.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Game State

**Objekt se stavem probíhající hry, dostupný všem a replikovaný na server i klienty.**

Zatímco Game Instance přežívá levely a Player State patří jednomu hráči, Game State drží to, co platí pro celou aktuální partii — skóre, fázi kola, počet zbývajících nepřátel. Právě proto je to přirozený domov pro event manager: dispatchery na Game State může kdokoli odebírat, aniž by měl referenci na vysílajícího aktéra.

Kde se s tím potkáš: [Komunikace Blueprintů: mediator](praxe/komunikace-blueprintu.md#mediator-koordinator-uprostred-a-event-manager-v-game-state) · [Principy architektury](praxe/principy-architektury.md#naradi-z-workshopu-kde-co-bydli-a-jak-se-to-hybe)

### Gameplay loop

**Smyčka činností, kterou hráč opakuje — nejcitovanější popisný nástroj game designu.**

Základní podoba je reward-investment: akce → odměna → investice odměny → silnější akce. Smyčky pomáhají číst strukturu her a komunikovat záměr, ale samy o sobě vysvětlují málo — model, pod který spadá skoro každá hra, nediskriminuje. Doplňkovým tvarem je řetězec (chain), který na rozdíl od smyčky nese směřování a rostoucí emoční investici.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Gameplay tag

**Hierarchický identifikátor stavu (`Status.MovementBlocked.Stunned`) — náhrada boolean/enum špagety.**

Tag v containeru = true; síla je v hierarchii: dotaz na rodiče (`Status.MovementBlocked`) matchuje všechny potomky, takže nová schopnost blokující pohyb = nový sub-tag, nula změn v podmínkách. Spravují se v Gameplay Tag Manageru (soubory .ini, v týmu dělit podle domén). Pasti: struct z funkce je kopie (Add/Remove jen na skutečné proměnné) a ref counting (dva ohně, jeden tag). V GAS jsou tagy lepidlem celého systému.

Kde se s tím potkáš: [Gameplay Tags](praxe/gameplay-tags.md) · [Telemetrie](praxe/telemetrie.md) · [Nepřítel v datech: tag → animace](praxe/ai-ve-velkem.md#strom-jen-rozhoduje-akce-v-gameplay-abilitach-nepritel-v-datech) · [Tick podmínky reakcí](praxe/ai-ve-velkem.md#reakce-vedle-stromu-co-se-muze-stat-v-kazdem-stavu-nepatri-do-zadne-vetve) · [Presety budov pod tagy](praxe/pcg-mesta.md#variabilita-z-dat-sockety-barvy-instanci-a-presety-pod-tagy) · [Filtr tagů v nástroji](praxe/pcg-mesta.md#nastroj-pro-artisty-bake-tlacitkem-a-drobnosti-ktere-setri-hodiny)

### Garbage collection

**Automatická správa paměti: engine periodicky uklízí objekty, na které už nikdo neukazuje.**

V UE je objekt po zničení (`Destroy Actor`) nejdřív označen jako **pending kill** — existuje v paměti, ale je „mrtvý" — a fyzicky zmizí až při dalším úklidu. Reference na takový objekt projde, ale použití spadne na runtime error. Obrana v Blueprintech: Validated Get / `Is Valid` před každým použitím reference na objekt, který mohl zaniknout.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md) · [Když stav opouští inventář](praxe/inventar.md#kdyz-stav-opousti-inventar-cestuje-jako-data-ne-jako-objekt) · [Technické zdraví projektu: příčiny hitchů](praxe/organizace-projektu.md#technicke-zdravi-projektu-kontroly-od-prvniho-dne-po-vydani)

### GASP

**Game Animation Sample Project — Epicův „živý" ukázkový projekt gameplay animace: 500+ animací, hotový Motion Matching, traversal a od 5.7 Mover.**

Zdarma, blueprint-only. Smysl projektu: zvednout minimální laťku kvality herní animace a dát šablonu, jak MM stavět — databáze per stav, choosery, procedurální doladění. Není to plugin: do vlastního projektu se migruje content (+ console variables a pluginy) a každá verze enginu přináší výrazné změny.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md) · [Update 5.8: poslední pro UE5](praxe/gasp.md#posledni-update-pro-ue5-sample-ne-framework) · [AnimGen ve streamu o GASP](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu)

### GDScript

**Skriptovací jazyk Godotu — syntaxí blízký Pythonu, gradually typed, navržený přímo pro strom scény.**

Odsazením strukturovaný, bez středníků, case-sensitive. Klíčové vlastnosti, které ho odlišují od „Pythonu pro hry": [gradual typing](#gradual-typing) (typy jsou volitelné a přidávají se po jedné proměnné), [signály](#signal) jako jazykový prvek, `@export` pro vystavení proměnné do inspektoru a `@onready` pro reference na nody, které v okamžiku načtení skriptu ještě neexistují. Godot umí i C# a C++, ale GDScript je jazyk, kterým je psaná dokumentace i většina komunitního materiálu.

Kde se s tím potkáš: [GDScript](godot/gdscript.md) · [Nody, scény a strom](godot/zaklady.md#nody-a-sceny-strom-ktery-je-zaroven-architekturou)

### Genre descoping

**Vzít jeden příjemný prvek velkého žánru a nafouknout ho na celou hru — vzorec vzniku nových subžánrů.**

Tower defense je RTS bez jednotek a útočení; backpack hry jsou Diablo svařené na inventář. Škrt musí něco přidat (fokus, přístupnost): dobrý nápad řeší dva problémy — méně práce pro vývojáře a ostřejší zážitek pro hráče.

Kde se s tím potkáš: [Žánry očima designéra](teorie/zanry.md) · [Scope a malé hry](teorie/scope.md)

### Ghost note

**Tišší verze téhož bicího zvuku, položená na slabou dělenou dobu.**

Nejčastěji na snare a nejčastěji na šestnáctinách. Přidá beatu hustotu, aniž by přidala důraz — proto na nich stojí většina slavných breakbeatů. Princip je obecnější než bicí: *tentýž prvek tišeji na slabší pozici* je způsob, jak něco zahustit, aniž bys posunul těžiště.

Kde se s tím potkáš: [Silné a slabé doby](hudba/rytmus.md#silne-a-slabe-doby-pater-a-ozdoby) · [Rejstřík: Synkopa](#synkopa)

### Gimbal lock

**Ztráta stupně volnosti u Eulerových úhlů: prostřední osa na 90° zarovná zbylé dvě a rotace se „slepí".**

Důsledek aplikace rotací v pevném pořadí. Vizuálně: tři gimbaly (kroužky), prostřední se otočí o 90° a vnější s vnitřním najednou točí kolem téže osy. Řešení: kvaterniony — proto se v enginech interpoluje přes slerp, ne přes yaw/pitch/roll.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Git LFS

**Rozšíření gitu pro velké binární soubory: v repozitáři je jen odkaz, obsah leží zvlášť.**

Bez něj git u každé změny ukládá celý binární soubor znovu, takže repozitář s animacemi a texturami rychle nabobtná. Háček je cena: na GitHubu je zdarma jen první gigabajt úložiště a pak se platí. Rozhodnutí zapnout či nezapnout LFS se dělá na začátku projektu — pozdější migrace je bolestivá.

Kde se s tím potkáš: [Organizace projektu: Git v Unrealu](praxe/organizace-projektu.md#git-v-unrealu-verzovani-z-editoru-a-cesta-zpet-v-case)

### Global Distance Field

**Hrubé, sloučené pole vzdáleností k povrchům celé scény v okolí kamery — odpověď na „jak daleko je odsud nejbližší povrch" pro celý svět najednou.**

Skládá se z [mesh distance fieldů](#mesh-distance-field) jednotlivých objektů. Hodnota v bodě je zároveň poloměr největší koule, která se tam vejde — na tom stojí [sphere tracing](#sphere-tracing). Používají ho mimo jiné Lumen v softwarovém režimu, distance field AO a GPU částice Niagary pro kolize; na mobilu nemusí být k dispozici.

Kde se s tím potkáš: [Živý svět z částic](praxe/niagara-vykon.md#zivy-svet-z-castic-tvorove-kteri-poslouchaji-ale-nehlasuji) · [Rejstřík: Mesh distance field](#mesh-distance-field)

### Global Time Dilation

**Násobitel rychlosti času celé hry — hodnota 0,1 zpomalí všechno včetně animací na desetinu.**

Kromě efektů typu slow motion je to ladicí nástroj: zpomalená interakce ukáže, kdy se ruka chytí, kdy se předmět připne a kde výběr úchopu přeskočí. Nastavuje se uzlem `Set Global Time Dilation`, v editoru i konzolovým příkazem `slomo`.

Kde se s tím potkáš: [Jedna animace zvednutí](praxe/interakcni-animace.md#jedna-animace-zvednuti-pro-vsechno-grip-pointy-a-pozy-ruky) · [Předmět do ruky bez teleportu](praxe/interakcni-animace.md#predmet-do-ruky-bez-teleportu-attach-neni-snap-a-dosah-neni-dohled) · [Hit stop per aktér](praxe/souboj.md#hit-stop-zastav-oba-ale-kazdeho-jinak) · [Zpomalení na ladění VFX](praxe/footsteps.md#castice-podle-povrchu-trace-z-chodidla-pooling-a-sila-podle-rychlosti)

### GOAP

**Goal-Oriented Action Planning: AI si sama poskládá posloupnost akcí vedoucí k cíli.**

Každá akce má předpoklady a účinky; plánovač hledá řetěz, který ze současného stavu světa dojde k cíli. Proti behavior tree, kde posloupnost napíšeš ty, tady vzniká za běhu — cenou je horší předvídatelnost a ladění. S Utility AI se nevylučuje: utility vrstva vybere cíl, GOAP naplánuje cestu k němu.

Kde se s tím potkáš: [Základy AI: Utility AI](praxe/ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) · [State Trees](praxe/state-trees.md)

### God class

**Antipattern: třída, do které se postupně nastěhuje logika všech ostatních — a pak s každou změnou padá půl projektu.**

V dědičnosti vzniká z pohodlnosti („dám to do masteru, ať to mají všichni") — jenže kódový zámek jednoho typu dveří nepatří všem dveřím. Pravidlo: rodič nese jen to, co potřebují všechny děti; specifika bydlí v dětech. Příbuzný jev mimo dědičnost: player character s inventářem, questy a UI v jednom grafu — lék jsou komponenty.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Gradual typing

**Typový systém, kde jsou typy volitelné a dají se přidávat postupně, proměnnou po proměnné.**

Kompromis mezi dynamickým a statickým typováním: `var x = 5` je dynamické (typ se dá přepsat, chyby vyplavou za běhu), `var x: int = 5` i `var x := 5` jsou statické (chyba se ohlásí v editoru před spuštěním, běh je rychlejší). Praktický důsledek té „postupnosti": nemusíš přepisovat projekt naráz — vyplatí se typovat nejdřív hranice, tedy parametry a návratové typy funkcí a vystavené proměnné, protože právě tam se chyby předávají mezi částmi kódu.

Kde se s tím potkáš: [GDScript: gradual typing](godot/gdscript.md#gradual-typing-kolik-bezpecnosti-si-koupis) · [Godot: co si přinést, než otevřeš editor](godot/zaklady.md#co-si-prinest-nez-otevres-editor)

### Granulární syntéza

**Rozsekání zvuku na krátká zrna a jejich přeskládání — z jednoho vzorku vznikne cokoli.**

Zrno je několik desítek milisekund; podle toho, jak se přehrávají, jak se překrývají a v jakém pořadí jdou, vznikne z téhož zdroje mrak, textura nebo úplně nový nástroj. Offline nástroje umí i věci nemožné v reálném čase — třeba přerovnat všechna zrna souboru podle hlasitosti.

Kde se s tím potkáš: [Nástroje zdarma: CDP a SoundThread](hudba/nastroje-zdarma-a-game-jam.md#cdp-a-soundthread-laborator-na-zvuk-zdarma) · [Syntéza zvuku](hudba/synteza-zvuku.md)

### Graybox

**Prototyp či blockout ze šedých primitivních tvarů — bez artu, bez nálady, jen prostor a mechanika.**

Správné použití: testování mechanik a metrik (gameplay prototyp, level blockout), kde by krása jen zkreslovala zpětnou vazbu. Špatné použití: testování prodejnosti a emoce — šedé kostky žádnou nemají, tam patří asset packy a hudba od prvního dne. Rozhodni, kterou otázku prototyp klade, a podle toho zvol formu.

Kde se s tím potkáš: [Prototypování](teorie/prototypovani.md) · [Nápad: prototyp do týdne](teorie/napad.md) · [Prostor a hranice](teorie/prostor-a-hranice.md) · [Hádanka ze stavebnice](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit) · [Blockout z pohledu env artu](praxe/blockout.md#zastav-omez-porovnej-blockout-ktery-se-da-precist)

### Groom

**Systém vlasů a srsti z jednotlivých pramenů (strands) — MetaHuman vlasy, obočí i řasy.**

Groom komponenty mají vlastní LODy — při skládání postavy z komponent je drží pohromadě LOD Sync komponenta (bez ní se vlasy rozbijí; hlavní postavě typicky Force LOD 0). Dražší než mesh vlasy; v dálce se groomy přepínají na karty.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Halting problem

**Turingův důkaz (1936): neexistuje obecný algoritmus, který o libovolném programu rozhodne, zda skončí.**

Zní akademicky, funguje jako kompas hranic řešitelnosti: každé „najdeme automaticky všechny bugy" a „AI garantuje správný kód" naráží na tenhle strop. Kdo o něm ví, je imunní vůči celé kategorii technického hadího oleje.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Harness

**Program, ve kterém agent s modelem běží: posílá prompty, spravuje kontext a volá nástroje (Claude Code, Codex, Cursor a další).**

Stejný model se v různých harnessech chová různě, protože každý jinak hospodaří s kontextem. Když jednoduchý úkol trvá nečekaně dlouho, bývá podle webináře Epic Education problém mezi MCP a harnessem, ne v promptu.

Kde se s tím potkáš: [Jak s agentem v editoru mluvit](praxe/mcp-v-editoru.md#jak-s-agentem-v-editoru-mluvit-presna-jmena-jeden-ukol-a-kontext-ktery-se-vejde) · [Rejstřík: Context window](#context-window)

### Herní vlákno

**Vlákno, na kterém běží všechno, co bys označil za „tvoji hru" — herní logika, AI, fyzika, blueprinty.**

V `stat unit` je to hodnota **game**. Přeroste-li renderovací vlákno, jsi CPU-bound a příčina je skoro jistě v kódu, který jsi napsal. Pozor na záměnu s **renderovacím vláknem** (viz vlastní heslo), které je taky CPU — ale dělá něco úplně jiného a šetří se na něm jinými zásahy.

Kde se s tím potkáš: [Co je v herním vlákně a co v renderovacím](praxe/profiling.md#co-je-v-hernim-vlakne-a-co-v-renderovacim) · [Rejstřík: Renderovací vlákno](#renderovaci-vlakno) · [Rejstřík: Frame time](#frame-time)

### Hitch

**Jednotlivý snímek, který trvá výrazně déle než ostatní — škubnutí, které hráč vidí, i když průměrné FPS vypadá dobře.**

Průměr ho schová, a proto se hitche hledají na časové ose snímků. Obvyklé příčiny podle týmu technical developer relations Epicu: streaming levelů, fyzika, spawn aktérů, synchronní načítání, kompilace [PSO](#pso), [garbage collection](#garbage-collection), blueprinty a samotné množství obsahu. Nejsou jen estetická vada — v souboji nebo v multiplayeru mění výsledek. Neplést s [jitterem](#jitter) (nerovnoměrné tempo bez jediného dlouhého snímku) ani s [hitch resiliency](#hitch-resiliency) (rezerva potrubí, která krátký výpadek pohltí).

Kde se s tím potkáš: [Technické zdraví projektu](praxe/organizace-projektu.md#technicke-zdravi-projektu-kontroly-od-prvniho-dne-po-vydani) · [Rejstřík: PSO](#pso) · [Rejstřík: Hitch resiliency](#hitch-resiliency)

### Hit flash

**Krátké rozsvícení nebo zbarvení zasaženého — vizuální potvrzení, že rána dopadla.**

Jedna z nejlevnějších vrstev [juice](#juice). V UE vede ke dvěma cestám: výměna materiálu za jiný (třeba červený) a zpátky, nebo [overlay material](#overlay-material), který se jen položí přes stávající materiál a po zásahu se odebere. Overlay funguje přes jakýkoli materiál, ale nevidí jeho WPO deformaci. Blikání jde udělat přímo v materiálu (čas → sinus → round); rychlé blikání je i otázka přístupnosti.

Kde se s tím potkáš: [Záblesk a kapow](praxe/souboj.md#zablesk-a-kapow-efekt-musi-sedet-na-tele-i-mezi-tely) · [Pět potvrzení rány](praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem) · [Katalog juice](teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku)

### HLOD

**Hierarchical LOD — sloučená náhrada za skupinu objektů v dálce; jeden mesh místo stovky.**

Ve world-partition světech se staví po streamovacích buňkách a vyplatí se u něj zaškrtnout *use render LOD meshes*, aby se do sloučení použily fallback meshe místo plných Nanite dat (jinak dojde paměť při buildu). Méně zřejmé použití: **skrytá HLOD proxy, která pořád vrhá stín** — scéna pak má stovky stín vrhajících primitiv místo desetitisíců, což je zásadní tam, kde se nedá spolehnout na Nanite a virtuální stíny.

Kde se s tím potkáš: [Odložit místo zlevnit](praxe/velke-svety.md#odlozit-misto-zlevnit-skorapka-prvni-interier-na-vyzadani) · [Rejstřík: World Partition](#world-partition) · [Rejstřík: Nanite](#nanite) · [Proxy v Beauclair](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [Větší chunky v dálce](praxe/velke-svety.md#dohled-na-kilometry-vetsi-chunky-v-dalce-stromy-se-stinem-a-souradnice-ktere-nepretecou)

### Hitch resiliency

**Schopnost potrubí snímků pohltit krátký výpadek, aniž hráč přijde o jediný snímek — placená vstupní latencí.**

Plná pipeline v Unrealu drží šest snímků v enginu a dva v hardwaru; hotová práce v back bufferech je rezerva, ze které se dá dohnat i zásek přes tři snímky rozpočtu. Cena je latence (šest snímků × frame time: ~200 ms na 30 FPS, ~100 na 60, ~50 na 120). Zkrátíš-li potrubí kvůli latenci, rezervu zahodíš — a to je v pořádku **jen když rozpočet skutečně držíš**, jinak snímky začnou padat. Tichá vedlejší cena i při úspěšném pohlcení: [jitter](#jitter).

Kde se s tím potkáš: [Latence proti odolnosti](praxe/frame-pacing.md#latence-proti-odolnosti-co-za-co-menis) · [Rejstřík: Input latency](#input-latency) · [Rejstřík: Jitter](#jitter) · [Rejstřík: Hitch](#hitch)

### HLSL

**High-Level Shading Language: jazyk shaderů se syntaxí podobnou C, ve kterém píšeš vlastní výpočty pro GPU.**

V Unrealu se objevuje v Custom uzlu materiálu a v Niagaře jako custom HLSL výraz nebo modul. Hodí se na krátký výpočet, který by v uzlech zabral moc místa, třeba přepočet počtu částic podle parametru. Výraz musí vracet správný typ, počet částic například celé číslo.

Kde se s tím potkáš: [Částice podle povrchu](praxe/footsteps.md#castice-podle-povrchu-trace-z-chodidla-pooling-a-sila-podle-rychlosti) · [Rejstřík: User Parameter](#user-parameter) · [Agent a materiál v HLSL](praxe/mcp-v-editoru.md#jak-s-agentem-v-editoru-mluvit-presna-jmena-jeden-ukol-a-kontext-ktery-se-vejde)

### Hot reload

**Načtení změněného kódu nebo assetu do běžící hry bez restartu.**

Změna se projeví hned, bez nového buildu a bez ztráty stavu hry, takže iterace trvá vteřiny místo minut. U assetů, jako jsou textury, meshe nebo data, je to běžné. U kódu je to těžší, protože se musí vyměnit funkce v běžícím procesu. Unreal pro C++ používá Live Coding, který přeloží změněné soubory a záplatuje běžící editor; starší mechanismus se jmenoval přímo Hot Reload a měl pověst nespolehlivého. Engine 007 First Light tvoří editor, runtime a resource server, takže hot reload funguje i napříč několika běžícími hrami. Neplést s [Live coding](#live-coding) v hudbě.

Kde se s tím potkáš: [007 First Light: editor zvlášť od hry](praxe/env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka) · [Rejstřík: Trunk-based development](#trunk-based-development)

### Houdini

**Procedurální 3D software od SideFX, který staví geometrii a efekty uzlovými sítěmi; do Unrealu ho přenáší plugin Houdini Engine.**

Studia v něm dlouho stavěla procedurální nástroje pro svět, třeba budovy, silnice nebo terén. S PCG a Geometry Scriptem část z nich přesouvají přímo do Unrealu, aby artist nemusel opouštět editor. Houdini má podle Lucid Games dál své využití, záleží na tom, čeho chceš dosáhnout.

Kde se s tím potkáš: [Nástroj pro artisty](praxe/pcg-mesta.md#nastroj-pro-artisty-bake-tlacitkem-a-drobnosti-ktere-setri-hodiny) · [Blok napřed, silnice potom](praxe/pcg-mesta.md#blok-napred-silnice-potom-block-processor-a-booleany) · [Modifier stack v Mesh Terrainu](praxe/mesh-terrain.md#modifier-stack-nedestruktivni-tvarovani)

### HUD

**Heads-up display: vrstva informací zobrazená přes gameplay — zdraví, munice, minimapa, cíle.**

Jen jedna část UI: patří k němu i mapy, výběr postav, inventář, skill tree a questovní okna. Kolik HUDu hra unese, určuje žánr — karetní hra je z velké části rozhraní, narativní hra si vystačí s minimem. Rozvržení HUDu není dekorace: mozek dělá asociace podle blízkosti, takže pruh vedle jména nepřítele čteme jako jeho zdraví.

Kde se s tím potkáš: [Art specializace: UI a UX](teorie/art-specializace.md) · [První dojem](teorie/prvni-dojem.md) · [Hádanka ze stavebnice](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit) · [UI ve světě](praxe/ui-ve-svete.md)

### Hit stop

**Krátké zamrznutí hry v okamžiku zásahu; dodá útoku váhu a dá hráči čas si zásah uvědomit.**

Technika převzatá z bojovek, jeden z nejlevnějších juice triků vůbec — pár řádků kódu, žádný asset. Použitelné rozmezí pro běžný sek je zhruba **1/20 až 1/10 sekundy**; silné údery snesou víc. Škáluje se podle síly útoku: má-li silný hit stop každý zásah, přestane znamenat cokoli. Jedna past, na kterou se zapomíná: **hit stop zdržuje vstup**, takže se během něj vyplatí vstupy [bufferovat](#input-buffering), ne zahazovat.

V UE se dá postavit per aktér přes [Custom Time Dilation](#custom-time-dilation): zasažený stojí, útočník jen zpomalí (třeba na 5 %). Patří k němu i otřes meshe (ne aktéra, ať se netřese kapsle), silnější u zasaženého a slábnoucí ke konci.

Kde se s tím potkáš: [Combo a hit stop](godot/pripadovka-nepratele.md#combo-a-hit-stop-dva-casovace-a-ctvrt-sekundy) · [Katalog juice](teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) · [Hit stop: zastav oba, ale každého jinak](praxe/souboj.md#hit-stop-zastav-oba-ale-kazdeho-jinak)

### Hitbox

**Oblast, která při zásahu působí — proti hurtboxu, což je oblast, která zásah přijímá.**

Rozdělení na dvě oblasti je základ čitelného soubojového systému: útok má hitbox, tělo má hurtbox, a teprve jejich překryv znamená zásah. Umožňuje to věci, které by jinak nešly — hitbox větší než zbraň (velkorysost), hurtbox menší než postava (odpuštění), nebo dočasné vypnutí hurtboxu (nezranitelnost po zásahu). Ve [frame datech](#frame-data) je hitbox jednotka, ke které se váže poškození, odhoz a efekty.

V UE se hitbox útoku typicky dělá tracem během animace: box před postavou na jednom snímku (impact frame), nebo koule tažená mezi sockety zbraně po celé [active frames](#active-frames). Kolikrát smí jeden útok zasáhnout tentýž cíl, hlídá seznam zasažených, který se s každým útokem vyprázdní.

Kde se s tím potkáš: [Frame data](godot/pripadovka-nepratele.md#frame-data-definuj-system-driv-nez-ho-postavis) · [Komponenta má být sobecká](godot/kompozice.md#komponenta-ma-byt-sobecka-test-kamene) · [Hitbox podle poctivosti animace](praxe/souboj.md#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames) · [Damage jednou za útok](praxe/souboj.md#damage-jednou-za-utok-seznam-zasazenych-patri-utoku-ne-terci)

### Hard coding

**Hodnoty napsané natvrdo přímo v kódu místo v proměnné či konfiguraci.**

Funguje přesně do chvíle, kdy je potřeba hodnotu změnit — pak ji lovíš po celém projektu a jednu zapomeneš. Pravidlo: každé surové číslo, které budeš někdy ladit, patří do proměnné; stejný princip platí pro vstupy (pojmenované akce místo kláves). Výjimka potvrzující pravidlo: v prototypu na vyhození je hard coding ctnost — rychlost tam poráží čistotu.

Kde se s tím potkáš: [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md) · [Nápad: prototyp do týdne](teorie/napad.md)

### Hard reference

**Přímý odkaz na asset/třídu, který s sebou tahá vše, co cíl referencuje — do paměti i do buildů.**

Vzniká castem, class referencí, přiřazeným meshem. Diagnóza: pravý klik na asset → Reference Viewer (kdo na kom závisí) a Size Map (kolik paměti reference stáhne). Následky: dlouhé loady, provázané levely, křehké systémy. Léky: abstraktní datový master, interfacy, event dispatchery, broadcast kanály — a u assetů soft reference, které se načítají až na vyžádání.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Organizace projektu](praxe/organizace-projektu.md) · [Soft reference: načti, až když to hra potřebuje](praxe/pamet-a-instance.md#soft-reference-nacti-az-kdyz-to-hra-potrebuje) · [Cast na lehkého rodiče](praxe/komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast)

### Harmonická řada

**Řada alikvót struny nebo píšťaly: celočíselné násobky základní frekvence (1×, 2×, 3×…).**

Právě z ní vypadnou intervaly západní hudby — oktáva (2:1), kvinta (3:2), kvarta (4:3). Jiné nástroje (zvony, kovové tyče) mají neharmonické alikvóty, a proto vedou k jiným stupnicím.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### HDRI

**Panoramatická fotografie s vysokým dynamickým rozsahem — obloha a světlo skutečného místa v jednom assetu.**

HDRI Backdrop plugin ji promítne na kupoli a skylight z téže mapy vezme indirect — konzistentní intenzita oblohy i odrazů. Alternativa bez pluginu: obří sphere s Unlit materiálem a isSky checkboxem. Zdroje: Poly Haven, locationtextures.com (s časem a místem pořízení — hodí se pro fyzikální kalibraci světla).

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Stavba prostředí](praxe/env-tvorba.md)

### Height mapa

**Černobílá textura kódující výšku terénu jasem pixelu: černá dole, bílá nahoře.**

Formát, na kterém stojí klasický Landscape — a zdroj jeho hlavního limitu: jedna hodnota na pixel znamená jediný stupeň volnosti (nahoru/dolů), takže jeskyně a převisy nejdou. Zůstává ale skvělým výměnným formátem: sculpt z Gaey či World Machine se přenáší právě height mapou a Mesh Terrain ji umí importovat jako startovní tvar i promítat jako texture modifier.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [POM a contact shadows z výškové mapy](praxe/landscape-tipy.md#hloubka-bez-geometrie-pom-contact-shadows-a-plugin-ihp) · [Tři pouta height mapy](praxe/mesh-terrain.md#proc-trojuhelniky-a-ne-voxely-mesh-partition-od-zdroje-po-runtime)

### Hurtbox

**Oblast, která zásah přijímá — protějšek [hitboxu](#hitbox), který zásah působí.**

Hurtbox menší než postava odpouští těsné úhyby, dočasně vypnutý hurtbox je nezranitelnost. V UE ho v jednoduchých systémech dělá kapsle (typ objektu Pawn), na kterou útok trasuje. Jemnější systémy trasují na fyzikální těla physics assetu a podle jejich physical materialu poznají, kterou končetinu rána zasáhla.

Kde se s tím potkáš: [Hitboxy: velkorysost, ne přesnost](praxe/pasti-a-mechaniky.md#hitboxy-velkorysost-ne-presnost) · [Hitbox podle poctivosti animace](praxe/souboj.md#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames) · [Zdraví po končetinách](praxe/souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav)

### Hydratace

**Přepnutí objektu z levné reprezentace na plnohodnotnou, když se k němu hráč přiblíží — a zpátky, když odejde.**

V dálce instance v ISM komponentě, u hráče aktér se vší logikou. Naměřený přínos u instance actorů: streamování levelu s tisícem objektů bylo **asi pětkrát rychlejší** než s tisícem aktérů, protože každá instance je jen transform, ne objekt a ne komponenta. Klíčový recept navrch: objekt může být z instancí **natrvalo vyhozen** (*eject*) ve chvíli, kdy se z kulisy stane součást hráčova příběhu. Zásadní důsledek pro návrh: **volba reprezentace určuje, jak se ta věc ukládá** — aktér, instance actor a mass entita každý jinak.

Kde se s tím potkáš: [Hydratace: instance actory a mass](praxe/persistence-a-hydratace.md#hydratace-instance-actory-a-mass) · [Rejstřík: Instanced Actors](#instanced-actors) · [Rejstřík: ISM](#ism)

### Hook

**Prvek, který hru prodá na první pohled: mechanika, premisa nebo obraz, u kterého se scrollující palec zastaví.**

Portálové portály, vlak-monstrum z Choo Choo Charles, „staráš se o svoje auto v psychedelické Zóně". Hook je vstupní bod trychtýře appealu — bez něj hra nemá jak oslovit lidi, kteří o ní nikdy neslyšeli. Test: dokážeš hook vtěsnat do titulku na Redditu nebo do 300 znaků short description? Hra bez jediné inovace hook nemá — a bez hooku není důvod, aby vznikla.

Kde se s tím potkáš: [Základy: engagement a appeal](teorie/zaklady.md) · [Prototypování](teorie/prototypovani.md) · [Nápad](teorie/napad.md) · [GDD: Monaco](teorie/gdd.md)

### IES profile

**Soubor s naměřeným rozložením světla skutečného svítidla, který dá světlu realistický tvar kuželu a kresbu.**

Formát pochází z osvětlovací techniky (Illuminating Engineering Society) a výrobci svítidel ho dodávají ke svým výrobkům. Unreal ho použije jako masku jasu podle směru, takže reflektor nebo lampa vrhá typické kruhy a přechody. S MegaLights je podporovaný od 5.8 a pár profilů je přímo v enginu. Vnitřní kužel spotu má mít zhruba stejný úhel jako paprsek v profilu, aby se ukázala celá kresba.

Kde se s tím potkáš: [Svítidlo z víc světel](praxe/megalights.md#svitidlo-z-vic-svetel-odraz-mlha-a-stin-se-ladi-zvlast) · [Rejstřík: Rect light](#rect-light)

### IK

**Inverzní kinematika — výpočet, který natočí řetěz kostí tak, aby koncová kost (effector) dosáhla zadaného cíle.**

Opak FK, kde se natáčí kost po kosti od kořene. Ve hrách typicky opravuje animaci na posledním metru podle světa: nohy na nerovném terénu, ruka na klice nebo na předmětu. V Control Rigu ji řeší uzly Basic IK (tři kosti), Full Body IK a další; podstatné je nastavit osy řetězu a [pole vector](#pole-vector) a převést cíl do správného prostoru (u postav do prostoru meshe). Váha uzlu slouží jako alfa, kterou může řídit [křivka v animaci](#animation-curve).

Kde se s tím potkáš: [Ruka na klice](praxe/interakcni-animace.md#ruka-na-klice-ik-v-control-rigu-prevod-prostoru-a-alfa-z-krivky) · [Hratelný MetaHuman: foot IK](praxe/metahuman.md#hratelny-metahuman-retarget-jednim-klikem-a-virtual-bones) · [GASP: foot placement](praxe/gasp.md#proceduralni-vrstva-v-control-rigu-foot-placement-springy-a-locomotor) · [Vazby končetin u párových akcí](praxe/gasp.md#parove-akce-pres-motion-matching-role-rozdeleny-warp-a-vazby-koncetin) · [Control rig s IK od agenta](praxe/claude-code-ue.md#mcp-misto-klikani-agent-v-blenderu-od-blockingu-po-rig)

### Iluze plynulosti

**Pocit „rozumím tomu", který vzniká z plynulého čtení — a zhroutí se při prvním pokusu věc vysvětlit krok za krokem.**

Klasický experiment: lidé si věří, že chápou kolo nebo zip, dokud nemají popsat, jak přesně fungují. Proti iluzi pomáhá vybavování (retrieval practice), učení druhých a psaní vlastními slovy — všechno formy nárazu na realitu.

Kde se s tím potkáš: [Učení v éře AI](teorie/uceni-v-ere-ai.md) · [Zápisek: Kvízový protokol](zapisky/kvizovy-protokol.md)

### Importance sampling

**Vzorkování podle důležitosti: víc vzorků dostane to, co k výsledku víc přispívá.**

Je to obecná technika výpočtů metodou Monte Carlo a stojí na ní path tracing i ray tracing, protože rozhazovat paprsky rovnoměrně se nevyplatí. MegaLights tak dělí omezený počet vzorků na pixel mezi světla podle jejich příspěvku. Má to stinnou stránku: velmi jasné světlo, které svítí na všechno, si vezme skoro celou důležitost a menším světlům ji bere. Proto se slunce do MegaLights nedává.

Kde se s tím potkáš: [Slunce bez MegaLights](praxe/megalights.md#slunce-bez-megalights-silne-svetlo-spolkne-rozpocet) · [Rozpočet vzorků na pixel](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis) · [Rejstřík: Denoiser](#denoiser)

### Impostor

**Nejagresivnější stupeň LOD: 3D asset nahrazený obrázkem, který se otáčí s kamerou.**

Z dostatečné vzdálenosti rozdíl nepoznáš — a stojí to zlomek původní ceny. Vyplácí se dotáhnout: renderovat k diffuse i normálovou mapu a vypéct víc pohledů, mezi kterými se blenduje. Ve scénách s desetitisíci stromů jsou impostory důvod, proč se to vůbec dá vykreslit. Proč to funguje tak nepoměrně dobře, vysvětluje [quad utilization](#quad-utilization) — nejde o počet vrcholů, ale o to, že mikrotrojúhelníky jsou pro GPU nejdražší možný vstup.

Octahedral impostor jde dál. Strom se předrenderuje z mnoha úhlů a shader mezi pohledy skládá obraz, který se chová skoro jako geometrie a umí vrhat i přijímat stín. Bez stínů se vzdálený les slije do ploché barevné masy.

Kde se s tím potkáš: [Proč malé trojúhelníky ničí GPU](praxe/rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu) · [Rejstřík: Nanite](#nanite) · [Octahedral impostory](praxe/velke-svety.md#dohled-na-kilometry-vetsi-chunky-v-dalce-stromy-se-stinem-a-souradnice-ktere-nepretecou)

### Inertialization

**Způsob blendování animací, který nemíchá dvě pózy, ale z rychlosti původního pohybu dopočítá plynulý doběh do nové animace.**

Na rozdíl od crossfadu se nemusí vyhodnocovat obě animace současně a přechod působí přirozeně i u prudkých změn. V montážích se volí jako blend mode in/out; aby fungoval, musí být v AnimBP uzel Inertialization.

Kde se s tím potkáš: [Contextual Animation](praxe/interakcni-animace.md#contextual-animation-scena-s-rolemi-misto-rucni-choreografie)

### Inheritance

**Dědičnost: děti přebírají proměnné, funkce a komponenty rodiče — základ, na kterém stojí celý UE (Actor → Pawn → Character).**

Lakmusový test každého vztahu: „is it a?" — pes *je* mazlíček, dům není. Rodič je smlouva (co deklaruje, mají garantovaně všechny děti) a na smlouvě stojí polymorfismus: volající volá `Interact`, každé dítě odpoví po svém. Blueprint specifika: component eventy nejde overridnout (obal je do custom eventů), overridnutý event nespouští rodiče automaticky (Add Call to Parent Function).

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Kdy dědit a kdy jen konfigurovat](praxe/principy-architektury.md#kdy-dedit-a-kdy-jen-konfigurovat) · [Pasti z jednoho rodiče](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit)

### Idea reservoir

**Zásobník nápadů, které NEJSOU schválené: kanban sloupec před to-do, ze kterého se tahá podle vývoje hry.**

Rozdíl proti klasickému backlogu: nic v rezervoáru není slib. Když se ukáže, co ve hře funguje, taháš nápady, které to sytí — pivot bez přepisování plánu. Protilék na „therapeutic planning": dlouhé dokumenty psané pro dobrý pocit z nejistoty.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Tvůrčí zásek: Grail metoda](teorie/tvurci-zasek.md)

### Horizontal slice

**Ukázka celé hry skrz zlomek jejích systémů — opak vertical slice.**

Vertikální řez předpokládá, že se všechny podstatné části hry vejdou do jednoho úseku. U pomalých her o postupném odemykání (management, budovatelské strategie, 4X) to neplatí: hráč potřebuje odehrát celou seanci. Řešením je dát mu celou hru, ale jen třicet až čtyřicet procent systémů — a zbytek naznačit jako slib do plné verze.

Kde se s tím potkáš: [Vydání hry: vertikální a horizontální řez](teorie/vydani-hry.md) · [Prototypování](teorie/prototypovani.md)

### Input buffering

**Vstup stisknutý těsně před tím, než je platný, se zapamatuje a provede v první možný moment.**

Skok zmáčknutý dva framy před dopadem se provede při dopadu — spolu s coyote time nejcitovanější výjimka, kterou input systém obsluhuje hráčovo očekávání místo doslovného čtení vstupů. „Input manager nemá slepě překládat stisky."

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Game feel a imerze](teorie/game-feel.md)

### Input decay

**Tlumení predikovaného vstupu při resimulaci — čím hlouběji v predikci, tím slabší.**

Predikce předpokládá, že hráč drží vstup dál. Když zastaví, kopie jeho postavy u ostatních popojede moc daleko a po korekci couvá. Útlum podle křivky v Network Physics Settings to zmírní; v kódu jde o vynásobení pohybového vstupu hodnotou křivky.

Kde se s tím potkáš: [Síťová fyzika zevnitř](praxe/mover.md#sitova-fyzika-zevnitr-snimky-misto-casu-resimulace-a-input-decay) · [Rejstřík: Resimulation](#resimulation)

### Input latency

**Prodleva mezi hráčovým vstupem a okamžikem, kdy je následek vidět na monitoru.**

Pozor na to, co pod tím jménem měří Unreal: statistika `input` v `stat unit` je **od navzorkování vstupu na začátku herního snímku po flip back bufferu** — ne hardware, ne operační systém, ne kompozitor, ne kabel, ne odezva monitoru. Hlavní páky: vyšší framerate (počet snímků v potrubí je konstantní, mění se jejich délka), přiškrcení herního vlákna (`r.GTSyncType 2` na konzolích, Nvidia Reflex / AMD Anti-Lag 2 / Intel XeLL na PC) a kratší potrubí. Vždycky se za to platí [odolností proti záseku](#hitch-resiliency).

Kde se s tím potkáš: [Latence proti odolnosti](praxe/frame-pacing.md#latence-proti-odolnosti-co-za-co-menis) · [Snímek není fronta](praxe/frame-pacing.md#snimek-neni-fronta-je-to-potrubi)

### Integer scaling

**Zvětšování obrazu celými násobky (2x, 3x) místo desetinných — jediný způsob, jak udržet pixel art ostrý.**

Neceločíselné zvětšení rozdělí jeden zdrojový pixel mezi dva cílové a hrana se rozmaže. Jde ruku v ruce s filtrováním textur na nearest a se zachováním poměru stran; společně to jsou tři nastavení, na kterých stojí, jestli hra vypadá ostře, nebo jako kaše.

Kde se s tím potkáš: [2D vizuál: pixel art](teorie/2d-vizual.md)

### Instance

**Konkrétní umístěný výskyt assetu v levelu.**

Jeden asset (mesh lampy) → stovky instancí (lampy po celé mapě). Rozlišení asset vs. instance je základ práce v editoru: úprava assetu se propíše všem instancím, úprava instance jen jí. Editor umí s instancemi pracovat hromadně — viz Shift+E pro výběr všech výskytů daného assetu.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md) · [Rejstřík: Item Instance](#item-instance) *(jiný význam)*

### Interior mapping

**Shaderová iluze místnosti za oknem: interiér se promítne z textury podle úhlu pohledu a za sklem žádná geometrie není.**

Okno je jedna plocha. Klasická varianta spočítá v pixel shaderu, kde paprsek pohledu protne virtuální krabici místnosti, a vzorkuje její stěny, podlahu a strop z textury. Jednodušší varianty jen posunou plochou texturu interiéru parallaxem. Hloubka vznikne bez jediného polygonu navíc, a proto se tak plní okna celých měst. Variaci mezi okny dodá náhodný výběr místnosti, jasu nebo rozsvícení podle denní doby. V UE na to existuje material function InteriorCubemap.

Kde se s tím potkáš: [AC Black Flag Resynced: falešný interiér](praxe/env-technika.md#ac-black-flag-resynced-prodat-iluzi-ne-postavit-skutecnost) · [Beauclair: okleštěné interiéry](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [RE Requiem: interiéry jako textury](praxe/levely-a-streaming.md#jak-to-dela-resident-evil-requiem) · [Rejstřík: Parallax occlusion mapping](#parallax-occlusion-mapping) · [Falešné okno v UE](praxe/materialy.md#falesne-okno-interior-cubemap-a-mistnost-nafocena-v-enginu) · [Interiér, kam hráč nesmí](praxe/pcg-mesta.md#interier-z-bodu-mistnosti-jako-subgrafy-a-devet-uzlu-na-bar)

### ISM

**Instanced Static Mesh — shodná geometrie vykreslená jedním draw callem místo jednoho na kopii.**

Podmínka je tvrdší, než se čeká: **naprosto identická geometrie i materiál**. Barel a bedna se nesloučí ani se stejným materiálem; na to je *Merge Actors*, který vyrobí nový sloučený mesh (hrubší metoda, funguje u objektů blízko sebe — ale slučuje i LOD logiku). **HISM** je varianta s podporou LODů, vhodná pro objekty rozeseté po velké ploše. Past: instance se cullují jako **jeden celek**, takže sloučíš-li i stromy za budovami, budou se kreslit pořád. Máš-li zapnutý [Nanite](#nanite), ISM nepotřebuješ — Nanite culluje sám.

Kde se s tím potkáš: [ISM, HISM a merge](praxe/pamet-a-instance.md#ism-hism-a-merge-draw-cally-podle-geometrie) · [Rejstřík: Draw call](#draw-call) · [Rejstřík: Packed Level Actor](#packed-level-actor) · [Sdílené instance kusů destrukce](praxe/destrukce-a-latky.md#destrukce-kterou-procesor-unese-konvexy-debris-sdilene-instance-a-strop-zlomu)

### Indexical storytelling

**Vyprávění stopami a náznaky: hráč čte důsledky událostí a příběh si složí sám.**

Termín Clary Fernández-Vary; „index" je ze semiotiky znak, který zastupuje něco jiného, ale poznáš to jen proto, že ses to naučil — kouř znamená oheň, stopy znamenají, že tudy někdo šel. Prakticky to znamená rozmístit vodítka detektivního typu (vlečné stopy, podezřele čistá část místnosti) místo dopisů, které všechno vysvětlí.

Kde se s tím potkáš: [Prostor vypráví](teorie/prostor-vypravi.md) · [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Instanced Actors

**Experimentální systém (5.5+): svět stojí z levných instanced static meshů a objekty u hráče se vymění za plnohodnotné Blueprint actory.**

Swap na blueprint řídí Max Actor Distance, culling samotných instancí Max Instance Distances. Zásadní pravidlo: probuzený actor vzniká pokaždé od nuly — stav (sebraný pickup) musí držet externí manager. Posunutou fyziku vrací na místo, pokud nezapneš Eject on Actor Moved. S PCG spojuje uzel Spawn Instanced Actors (interop od 5.6) a jednorázový setup přes Data Registry.

Kde se s tím potkáš: [Instanced Actors](praxe/instanced-actors.md) · [Případovka Hex-A-Gone](praxe/pcg-hexagone.md)

### Integer overflow

**Přetečení celého čísla: součet přeroste, co jde uložit, a hodnota se překlopí do záporných.**

32bitové celé číslo má jeden bit na znaménko a 31 na hodnotu, takže strop je zhruba **2,1 miliardy**. Překročíš-li ho, procesor „vesele" překlopí znaménkový bit a z obřího kladného čísla je obří záporné — hráč nasbírá miliardy mincí a najednou je v mínusu. Řešení jsou dvě: **omez maximum**, aby se ke stropu nepřiblížilo, nebo **použij víc bitů**. Příbuzná past u desetinných čísel je nepřesnost floatů, kde s velikostí čísla roste velikost kroku, takže se fyzika daleko od počátku souřadnic rozpadá.

Kde se s tím potkáš: [Čísla mají meze](godot/pripadovka-systemy.md#cisla-maji-meze-overflow-a-nepresnost-floatu)

### Interval

**Vzdálenost mezi dvěma tóny, měřená v půltónech; nese vlastní emoční zabarvení.**

Kvinta (1→5) zní hrdinsky jako Star Wars, malá sexta tajemně, půltón napjatě. V melodii nesou emoci hlavně intervaly s největším důrazem — na začátku nebo ve vrcholu.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md) · [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Invariant

**Podmínka, která v daném bodě programu platí vždy — bez ohledu na to, kudy se tam běh dostal.**

Rámec precondition → postcondition → invariant pochází z formální verifikace: místo „spusť a koukej, co spadne" se ptáš, co musí platit před, po a během. Herně: „HP nikdy pod 0", „inventář nepřeteče kapacitu" — a assert tam, kudy tečou data.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Invisible wall

**Neviditelná kolize tam, kde vizuálně nic nebrání v cestě — nejhorší způsob, jak ohraničit mapu.**

Zabíjí imerzi přesně mechanismem „vidím, že to jde, ale hra mi to nedovolí". Alternativy: tvrdé hranice z přirozených bariér světa (útes, řeka, oceán) a pět druhů měkkých hranic — narativní, countdown, nepřátelská, ekonomická, percepční. Pravidlo: hráč se má rozhodnout sám, že dál nepůjde.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Item Instance

**Konkrétní kus položky v inventáři — nese stav, který definice mít nemůže (zbývající použití, vylosované staty).**

Vzniká z definice při zvednutí; fragmenty si v ní při vzniku založí svůj stav. Stohovatelné položky mají jednu instanci na stack, takže se „při vzniku instance" nic neděje, když do stacku jen přibude kus. Mezi systémy (zahození do světa, uložení) necestuje instance jako objekt, ale její stav jako data. Neplést s [Instance](#instance) — tam jde o umístěný výskyt assetu v levelu.

Kde se s tím potkáš: [Definice popisuje druh, instance nese kus](praxe/inventar.md#definice-popisuje-druh-instance-nese-kus) · [Když stav opouští inventář](praxe/inventar.md#kdyz-stav-opousti-inventar-cestuje-jako-data-ne-jako-objekt) · [Rejstřík: CDO](#cdo) · [Rejstřík: Fragment](#fragment)

### Iterace

**Jedno kolo smyčky uprav → otestuj → vyhodnoť; hry nevznikají jedním tahem, ale koly.**

Metafora spirály: ve středu je nedosažitelná dokonalá verze hry a každé kolo — přes všechny čtyři čtvrtiny elemental tetradu — tě k ní přiblíží. Playtest je motor iterace: neříká jen, jestli minulé kolo fungovalo, ale co má být v příštím.

Kde se s tím potkáš: [Prototypování: iterační spirála](teorie/prototypovani.md) · [Playtesting](teorie/playtesting.md)

### Izometrie

**Perspektiva bez úběžníku: vzdálené objekty se nezmenšují, takže scéna je čitelná v celé hloubce.**

Proto ji volí budovatelské a simulační hry — dává přehled o prostoru a snese hodně detailu, aniž by si prvky překážely. Dvě daně: perspektivu je nutné držet ve všech assetech (jinak se objekty odmítají slučovat s prostředím) a se statickou kamerou musíš řešit, co komu zakrývá výhled — mřížkou, zdí na horním okraji mapy nebo stupňovitým layoutem.

Kde se s tím potkáš: [2D vizuál: izometrie](teorie/2d-vizual.md)

### Jitter

**Mikro-škubání animací a kamery, které vzniká, i když nespadne ani jeden snímek.**

Delta time pro simulaci je frame time **předchozího** snímku, ale zobrazované snímky jdou v pevném rytmu VSyncu. Pohltí-li potrubí zásek, hráč o žádný snímek nepřijde — jenže následuje dohánění s velkým delta timem a pak doplnění potrubí s krátkými delta timy, takže se simulace rozjede a zpomalí. Diagnostika, která z nejednoznačného dojmu udělá jednoznačné čtení: **kolo rozdělené na 60 dílů s jednou otáčkou za sekundu** — čáry mají být při 60 FPS pořád zarovnané. Nedá se to spravit fixním delta timem (variabilní obnovovací frekvence; méně než třetina monitorů má celočíselnou nativní frekvenci).

Kde se s tím potkáš: [Jitter](praxe/frame-pacing.md#jitter-nespadne-ani-jeden-snimek-a-presto-to-skube) · [Rejstřík: Delta time](#delta-time) · [Rejstřík: Hitch resiliency](#hitch-resiliency)

### JSON Schema

**Popis typů v JSONu: jak se jmenují argumenty funkce a jakého jsou typu.**

MCP potřebuje dvojici schema (typy) a data (hodnoty). V Unrealu 5.8 obojí vyrábí reflexe ze signatur UFunctions, včetně enumů, structů a vnořených kontejnerů, takže autor nástroje JSON nepíše ručně.

Kde se s tím potkáš: [Vlastní tool set a skill](praxe/mcp-v-editoru.md#vlastni-tool-set-a-skill-api-pro-juniora-a-rada-kolegovi) · [Rejstřík: Reflection system](#reflection-system)

### Juice

**Vrstva audiovizuálního feedbacku, která prodává akce: screen shake, particles, squash & stretch, flash při zásahu.**

Stejné mechaniky s juice a bez něj jsou dvě různé hry — dash stejné rychlosti působí rychleji, kulka s odletujícími kusy zdi má najednou váhu. Teoreticky čistý signal-to-noise: každý detail hlásí, co se stalo a že to svět zaznamenal. Leští se na jádru, které už baví.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md) · [Pět potvrzení rány](praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem) · [Záblesk a kapow](praxe/souboj.md#zablesk-a-kapow-efekt-musi-sedet-na-tele-i-mezi-tely)

### Kanban

**Řízení práce kartami ve sloupcích To Do → Doing → Done: tok, jasné vlastnictví, limit rozdělanosti.**

Trello je značka, kanban je systém (jede i v Jira nebo Notionu). Tři nosná pravidla: karty dost malé, aby šly dokončit; jeden vlastník na kartu — když jsou zodpovědní dva, není zodpovědný nikdo; a nejméně karet je uprostřed, protože Doing je deklarace dnešního fokusu, ne evidence ambicí.

Kde se s tím potkáš: [Plánovací nástroje](teorie/planovani-nastroje.md)

### Keep Triangle Percent

**Nastavení Nanite meshe: kolik procent zdrojových trojúhelníků se uloží — zbytek se zahodí a zmizí z balíčku.**

Má smysl u meshů, jejichž nejjemnější detail se z běžné vzdálenosti nikdy neukáže; s počtem trojúhelníků klesá i velikost na disku (kořeny z 11 milionů na 150 tisíc). Kolik nechat, se dá zjistit přes [fallback mesh](#fallback-mesh) jako náhled. Na listí se nehodí — ubírání po procentech rozpojí větve a listy; tam patří [Trim Relative Error](#trim-relative-error).

Kde se s tím potkáš: [Nanite a velikost balíčku](praxe/nanite-do-hloubky.md#nanite-a-velikost-balicku-data-ktera-se-nikdy-nevykresli) · [Rejstřík: Nanite](#nanite)

### Keyboard ghosting

**Hardwarové omezení klávesnice: při některých kombinacích současně držených kláves jeden vstup nedorazí do hry.**

Klávesnice nemá vodič ke každé klávese — má matici řádků a sloupců. Při více současných stiscích může signál projít matricí neočekávanou cestou a vypadat jako stisk klávesy, kterou nikdo nezmáčkl (odtud „duch"). Moderní klávesnice tomu předcházejí tím, že místo vymyšlené klávesy jednu skutečnou **zahodí** (*key jamming*). Které kombinace selžou, se liší podle značky a modelu. **Kódem se to opravit nedá** — brání se tomu design ovládání: přemapovatelné klávesy, víc výchozích rozložení, podpora gamepadu, žádné kritické akce na třech současně držených klávesách. Viz [N-key rollover](#n-key-rollover).

Kde se s tím potkáš: [GDScript: když bug není v kódu](godot/gdscript.md#kdyz-bug-neni-v-kodu-keyboard-ghosting)

### Kimodo

**Model NVIDIA, který generuje animaci z textu a dalších omezení, jako jsou dráha, pózy a waypointy.**

Je trénovaný na 700 hodinách optického mocapu. C++ port běží i bez GPU, animace na tři vteřiny ale na CPU trvá až pět minut. Pro komerční použití vol kostry SOMA nebo G1, ne SMPL-X, a počítej s tím, že prsty se zatím nehýbou.

Kde se s tím potkáš: [Animace a 2D: Kimodo a PixelLab](praxe/ai-assety.md#animace-a-2d-kimodo-a-pixellab) · [Animace z modelu přímo ve hře](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu) · [Agent v Blenderu a ComfyUI](praxe/claude-code-ue.md#agent-v-blenderu-a-comfyui-lokalni-pipeline)

### Kitbashing

**Skládání nových objektů z dílů existujících kitů, třeba architektury a trubek, místo modelování od nuly.**

Termín pochází z modelářství, kde se z dílů různých stavebnic lepily nové modely. Ve hrách z kombinace dvou kitů vzniknou nové kusy a sdílené materiály pomůžou, aby k sobě pasovaly. Je to levné na výrobu i na paměť, protože nepřibývají nové textury. Rizikem je opakování a díly, které na sebe nesedí, a proto se švy kryjí stejnými spoji jako u kitů.

Kde se s tím potkáš: [Organický kit a spoje: kitbashing](praxe/modularni-kity.md#organicky-kit-a-spoje-zaborit-nechat-rust-od-zdroje-zakryt-sev) · [Rejstřík: Modular kit](#modular-kit)

### Knockback

**Odhození zasaženého směrem od útoku — potvrzení, že rána měla sílu.**

Vedle záblesku nejčitelnější reakce na zásah. Když se škáluje podle zbraně, zároveň rozlišuje mechaniky (dýka málo, kopí hodně). V UE ho typicky dělá `Launch Character` nebo impulz na fyzikální tělo.

Kde se s tím potkáš: [Pět potvrzení rány](praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem) · [Katalog juice](teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku) · [Kostra pasti](praxe/pasti-a-mechaniky.md#kostra-pasti-a-tri-variace-bodaky-rameno-rotor)

### Large World Coordinates

**Souřadnice v double precision, které UE5 používá pro pozice, aby velké světy nenarážely na přesnost floatu.**

32bitový float má pevný počet platných číslic, takže daleko od počátku se pozice začnou třást a výpočty selhávat. LWC tenhle strop posouvá o řády. Ne všechno v enginu ale počítá v doublech, GPU například pracuje s pozicemi vztaženými ke kameře. Mimo UE se stejný problém řeší origin shiftingem nebo fixed point čísly.

Kde se s tím potkáš: [Dohled na kilometry](praxe/velke-svety.md#dohled-na-kilometry-vetsi-chunky-v-dalce-stromy-se-stinem-a-souradnice-ktere-nepretecou) · [Proč Mesh Terrain existuje](praxe/mesh-terrain.md#proc-mesh-terrain-existuje-limity-landscape) · [Rejstřík: Origin shifting](#origin-shifting)

### Legibilita

**Čitelnost textu: jak snadno oko rozliší písmena a slova — ne totéž co velikost písma.**

Čtyři nejčastější prohřešky ve hrách: celé věty verzálkami (stejná výška písmen ruší tvar slova, nejvíc to dopadá na dyslektiky), zbytečně dekorativní řezy, velké skoky ve velikosti (oko musí přeostřovat) a slabý kontrast, ve hrách vyhrocený tím, že text leží přes pohyblivé pozadí. Není to kosmetika: hůř čitelná instrukce prokazatelně zhoršuje výkon v úkolu, který popisuje.

Kde se s tím potkáš: [Typografie](teorie/typografie.md) · [První dojem](teorie/prvni-dojem.md)

### Klonování hlasu

**Model vytrénovaný na nahrávkách konkrétního hlasu, který pak umí přezpívat nebo přemluvit cizí výkon jeho barvou.**

V praxi se kombinuje se dvěma dalšími kroky: generátor přezpívá tvůj text a melodii pořádně (ale cizím hlasem), stem separace z výsledku vytáhne samotný zpěv a klon ho převede zpátky na tvou barvu. Výstup je **suchý** — bez dozvuku a efektů — a to je jeho hlavní přednost, protože se dá posadit do mixu jako běžná nahrávka. Vážit je potřeba tři věci: běží to v cloudu (nahráváš otisk vlastního hlasu na cizí server), licenčně to má dvě vrstvy a nástroje se často propagují placenou spoluprací.

Kde se s tím potkáš: [AI na vokál](hudba/nastroje-zdarma-a-game-jam.md#ai-na-vokal-prezpivat-ale-zustat-sam-sebou) · [Rejstřík: Stem separace](#stem-separace)

### Konsonance

**Dojem klidu a souznění při současném znění tónů; opak disonance.**

Vzniká, když se alikvóty tónů dobře zarovnají a málo perou — proto oktáva a kvinta znějí stabilně. Konsonance je „domov", ke kterému se napětí disonance vrací.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### Kontrapunkt

**Skládání nezávislých melodií, které fungují zároveň (counterpoint).**

Horizontální dovednost (proti vertikální harmonii). Podle Inside the Score nejčastěji chybějící dovednost, která odděluje profíky od amatérů — i mírné zvládnutí povýší melodickou a texturní vyspělost hudby.

Kde se s tím potkáš: [Cesta skladatele: sedm pilířů](hudba/cesta-skladatele.md)

### Kumulativní výhoda

**Kdo je vidět, je víc vidět — úspěch se sám zesiluje bez ohledu na kvalitu.**

Známé i jako Matoušův efekt nebo „bohatí bohatnou". Na Steamu funguje mechanicky: algoritmus doporučuje to, co se prodává, a co se doporučuje, se prodává. Je to jeden ze tří mechanismů, které vedou k mocninnému rozdělení výsledků, a zároveň důvod, proč je start hry disproporčně důležitý oproti její dlouhodobé kvalitě.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#extremistan-tri-mechanismy-ktere-vedou-ke-stejne-strategii) · [Co prodává](teorie/co-prodava.md)

### Kvintový kruh

**Schéma dvanácti tónů seřazených po kvintách, které se po dvanácti krocích vrací na začátek — jenže nevrací.**

Kvinta je definovaná jako frekvenční poměr 3:2, ale ta, kterou skutečně hrajeme, je o třetinu procenta jinde. Po dvanácti krocích tedy skončíš zhruba **24 centů** vedle — je to **pythagorejské koma** — takže kvintový kruh je ve skutečnosti spirála. Rovnoměrné temperování ten rozdíl rozprostře po všech dvanácti tónech: žádný interval není úplně čistý, ale všechny tóniny znějí stejně a dá se mezi nimi modulovat. Je to obchod, ne pravda.

Kde se s tím potkáš: [Kvintový kruh je ve skutečnosti spirála](hudba/fyzika-souzvuku.md#kvintovy-kruh-je-ve-skutecnosti-spirala) · [Rejstřík: rovnoměrně temperované ladění](#rovnomerne-temperovane-ladeni) · [Rejstřík: Tritón](#triton)

### Kvaternion

**Reprezentace 3D rotace čtyřmi čísly: imunní vůči gimbal locku a hladce interpolovatelná (slerp) — výměnou za nulovou intuici.**

Rozšíření komplexních čísel o tři imaginární složky; násobení skládá rotace. V UE je to typ Quat — engine v něm rotace drží interně, zatímco Rotator (Eulerovy úhly) slouží UI. Chápat přesné vnitřnosti netřeba; vědět, kdy sáhnout po slerpu, ano.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Jump scare

**Úleková špička hororu: náhlý audiovizuální úder, který vybije nasbírané napětí.**

Rozpočet žánru: hlasité 2–3 na hodinu, tiché (leknutí bez plného vybití tenze) podle potřeby. Nejlepší scary jsou mini-dramaturgie — oči ve tmě, dohrávající písnička, natažené ticho, teprve pak úder — a monstrum smí jen implikovat.

Kde se s tím potkáš: [Horor design](teorie/horor-design.md)

### Landmark

**Výrazný orientační bod levelu — věž, světlo, brána — ke kterému se vztahuje hráčova navigace i kompozice prostoru.**

V postupu „landmark napřed": startovní bod hráče a hlavní point of interest jsou první dvě rozhodnutí návrhu levelu, ještě před blockoutem — dávají měřítko, směr a osu pro pacing a vertikalitu. Cestou k landmarku pak vedou funneling (zúžení prostoru), leading lines a světlo.

Ve Witcher 3: Blood and Wine má landmark i technický úkol. Ulice ústí na výhled k němu a stavba, která vede hráče, zároveň zkracuje průhledy a šetří streamování.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Beauclair: orientační body](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt)

### Landscape

**Klasický terénní systém UE: „papírově tenká" plocha deformovaná height mapou — jen nahoru a dolů, žádné převisy.**

Pořád produkční volba, dokud Mesh Terrain nedozraje. Klíčové nástroje: sculpt/paint módy s edit layers, copy/paste gizmo (patche a import height map do zón), paint vrstvy jako data pro PCG, Nanite displacement pro reliéf z materiálu. Limity řeší nástupce Mesh Terrain (skutečná mesh geometrie).

Kde se s tím potkáš: [Landscape tipy](praxe/landscape-tipy.md) · [Mesh Terrain](praxe/mesh-terrain.md) · [Limity Landscape podle Epicu](praxe/mesh-terrain.md#proc-trojuhelniky-a-ne-voxely-mesh-partition-od-zdroje-po-runtime) · [Město na svahu](praxe/pcg-mesta.md#blok-napred-silnice-potom-block-processor-a-booleany)

### Layered Blend Per Bone

**Anim uzel míchající dvě pózy od zadané kosti nahoru — základ vrstvení horního těla přes locomotion.**

V layer setupu se uvádí jméno kosti (přesný spelling!), od které blend působí — typicky clavicle nebo spine; blend depth a weight ladí měkkost přechodu. Nad Motion Matchingem dvě klasická použití: montáž útoku do horního těla (s Blend Poses by Bool) a overlay póza držené zbraně (single frame animace).

Blend depth rozkládá přechod po kostech (hodnota 4 od pánve dá 25/50/75/100 %), blend depth −1 větev vyřadí (stehna, aby útok nešel do nohou) a Mesh Space Rotation Blend bere rotaci vrstvy v prostoru meshe místo podle rodičovských kostí.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [Systémy nad MM](praxe/mm-systemy.md) · [Pózy prstů od hand_r](praxe/interakcni-animace.md#jedna-animace-zvednuti-pro-vsechno-grip-pointy-a-pozy-ruky) · [Pistole s baterkou](praxe/animace-nastroje.md#krivky-kamera-a-past-30-snimku-remeslo-prvni-osoby) · [Útok za běhu](praxe/souboj.md#utok-za-behu-horni-pulka-bojuje-dolni-bezi-a-krivka-rekne-kdy-ne)

### Layered move

**Dočasný zdroj pohybu v Moveru — nástupce root motion sources: dash, naváděný útok, skok.**

Na rozdíl od movement módů jich může běžet víc naráz; každý generuje rychlost, mixují se nebo přepisují podle priority a výsledek vykoná aktivní mód. Animation root motion přichází jako obyčejný layered move — a proto jde konečně míchat s řízeným pohybem (v CMC platilo buď–anebo).

Kde se s tím potkáš: [Mover](praxe/mover.md)

### Layering

**Vrstvení více zvuků hrajících tutéž linku, aby zněla velce a plně.**

Tatáž melodie na jednom tenkém synthu je „skoro ono"; teprve několik vrstev (piano + bright lead + bas) dá plný zvuk. Melodie a akordy jsou kostra, dojem dělá aranž a vrstvení.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md)

### Leitmotiv

**Melodie svázaná s postavou, místem nebo věcí, která se vrací a mění podle scény.**

Motiv s přiřazeným významem: téma postavy se proměňuje podle nálady, ale zůstává rozpoznatelné. Propojuje soundtrack v jeden svět — Jaies zapracuje téma postavy i do hudby oblasti, kterou postava obývá. Přímá aplikace práce s motivem.

Kde se s tím potkáš: [Tvorba herního soundtracku](hudba/tvorba-soundtracku.md) · [Jak psát melodie](hudba/melodie.md)

### Lerp

**Lineární interpolace A + (B − A)·t — nejlevnější kouzlo enginu: plynulý přechod čehokoli, co jde vyjádřit čísly.**

A a B může být pozice, scale, barva i délka health baru. Strohost lineárního průběhu opravují shaping functions (smoothstep a spol.) aplikované na parametr t; barevné přechody vylepší interpolace v jiném prostoru (HSV, Lab) místo RGB.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md) · [Předmět do ruky bez teleportu](praxe/interakcni-animace.md#predmet-do-ruky-bez-teleportu-attach-neni-snap-a-dosah-neni-dohled)

### Level instance

**Znovupoužitelný sub-level: skupina aktorů (klidně s blueprinty) zabalená do jednoho celku, který se dá rozmístit vícekrát.**

Vytváří se výběrem aktorů → right-click → Level → Create Level Instance; sourozenec Packed Level Actor dělá totéž jen pro static meshe a převádí je na instance (jeden draw call, ideální pro modulární budovy). Editace se propíše všem kopiím — varianta se dělá z duplikátu. Vzor „dům z Warzone": jednou postavit, šestkrát položit.

Kde se s tím potkáš: [Optimalizace scény](praxe/optimalizace.md)

### Level Sequence

**Asset [sequenceru](#sequencer): časová osa se stopami actorů, kamer a událostí, kterou lze přehrát v editoru i za běhu hry.**

Za běhu ji přehrává Level Sequence Player (`Create Level Sequence Player` → `Play`). Pro návrat do hry rozhoduje `When Finished: Keep State` na stopách (postava zůstane tam, kam ji sekvence dovedla) a `Can Blend` na camera cuts. `Transform Origin Actor` přehraje sekvenci relativně k zadanému actoru, takže jeden záběr funguje kdekoli v levelu. Slouží i jako měřidlo — pro benchmark nebo pro ladění synchronizace animace s objektem.

Kde se s tím potkáš: [Cutscéna, která vrátí hru tam, kde skončila](praxe/cutsceny.md#cutscena-ktera-vrati-hru-tam-kde-skoncila) · [Finisher bez střihu](praxe/cutsceny.md#finisher-bez-strihu-sekvence-ktera-se-prehraje-kolem-hrace) · [Benchmark z level sequence](praxe/mereni-automaticky.md#benchmark-z-level-sequence-mereni-jako-soucast-prace) · [Animace řídí svět](praxe/interakcni-animace.md#animace-ridi-svet-normalizovane-krivky-v-montazi)

### Level streaming

**Načítání a uvolňování částí světa za běhu — místo výměny celého levelu přes Open Level.**

Persistent level je rám; sub-levely (`Window → Levels`) se nahrávají přes Level Streaming Volumes nebo uzly Load/Unload Streaming Level, asynchronně — hra mezitím žije. Detaily: *loaded* ≠ *visible* (neviditelný level drží paměť); streaming volume musí ležet v persistent levelu; persistent nejde unloadnout (trik: veškerý obsah do sub-levelu „Base"). Pro open worldy je nástupcem World Partition.

Kde se s tím potkáš: [Levely a streaming](praxe/levely-a-streaming.md) · [Beauclair: clony pro streamování](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [Mortal Shell 2: úzké průchody](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek)

### LFO

**Pomalý oscilátor (low-frequency oscillator), který za tebe donekonečna otáčí zvoleným knobem.**

Zatímco obálka otočí knobem jednou (při notě), LFO ho otáčí pořád dokola — vibrato, wobble, pohyb filtru. Modulace (obálka i LFO) otevírá nekonečno zvuků z jednoho patche.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Lighting channels

**Kanály, kterými se v Unrealu určuje, na které objekty světlo svítí.**

Světlo i objekt mají zapnuté některé z kanálů 0 až 2 a světlo zasáhne jen objekty se společným kanálem. Jsou jen tři, takže jde o jednoduchou náhradu light linkingu z filmových programů. Stačí ale třeba na to, aby pomocné světlo nepřepálilo samotné svítidlo. S MegaLights fungují od 5.8. Které světlo je v jakém kanálu, ukáže Light Mixer.

Kde se s tím potkáš: [Svítidlo z víc světel](praxe/megalights.md#svitidlo-z-vic-svetel-odraz-mlha-a-stin-se-ladi-zvlast) · [Slunce bez MegaLights](praxe/megalights.md#slunce-bez-megalights-silne-svetlo-spolkne-rozpocet)

### Liminální prostor

**Veřejný prostor zbavený lidí a účelu — mall, škola, letiště v prázdnu; děsí tím, že je skoro normální.**

Repetitivní vzory, dlouhé prázdné chodby, známá infrastruktura bez života: mozek hlásí „tohle znám" i „tady něco nesedí" zároveň, příbuzné uncanny valley. Hororová scéna z něj udělala celý subžánr.

Kde se s tím potkáš: [Horor design](teorie/horor-design.md)

### Line Trace

**Raycast — neviditelný paprsek vyslaný z bodu daným směrem, který vrátí první (nebo všechny) kolize na dráze.**

Základní dotazovací nástroj: „na co koukám?", „stojím na zemi?", „vidí mě stráž?". Samotný trace je levný; problém je vzorec „trace každý frame v Event Ticku" — polling tam, kde stačí reagovat na změny. Alternativou pro detekci „něco vstoupilo do zóny" jsou overlap eventy kolizních komponent.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md) · [Barel, který teče](praxe/pasti-a-mechaniky.md#barel-ktery-tece-diry-jako-data-hladina-jako-jedno-cislo) · [Zdraví po končetinách](praxe/souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav) · [Trace z chodidla](praxe/footsteps.md#castice-podle-povrchu-trace-z-chodidla-pooling-a-sila-podle-rychlosti) · [Přichycení města na terén](praxe/pcg-mesta.md#blok-napred-silnice-potom-block-processor-a-booleany)

### Linear grammar

**Gramatika PCG nástrojů: string symbolů, který určuje rytmus modulů podél splinu.**

Modulům (meshům) přiřadíš symboly a zapíšeš vzor: `[A,B]` je sekvence, číslo přesný počet (`A3`, `[A,B]2`), `*` opakuje vzor do vyplnění délky splinu a `+` navíc moduly roztáhne, aby délka vyšla přesně. Plot s brankami nebo zeď se sloupky je pak jeden řádek textu místo ručního skládání dílců.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md) · [Budova jako věta](praxe/pcg-mesta.md#budova-jako-veta-panelovy-kit-gramatika-a-patra)

### Linked anim graph

**Samostatný animační graf připojený do AnimBP jako modul — s tagem, přes který na něj komponenty sáhnou zvenčí.**

Vzor z traversal/cover systémů nad GASP: parkour či overlay logika žije ve vlastním grafu, hlavní AnimBP ji jen linkuje; tag („parkour", „overlay") umožňuje actor komponentám najít anim instanci a řídit ji. Drží AnimBP čitelný a systémy přenositelné mezi projekty.

Modul jde vytvořit jako template AnimBP bez skeletu, se vstupem přes `Input Pose`. Sloty uvnitř linked grafu se ale ve výchozím stavu nevyhodnocují, takže modul potřebuje v Class Defaults `Use Main Instance Montage Evaluation Data`. Branch filtry Layered Blend Per Bone se z modulu vystavit nedají.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md) · [Útok za běhu: modul pro další postavy](praxe/souboj.md#utok-za-behu-horni-pulka-bojuje-dolni-bezi-a-krivka-rekne-kdy-ne)

### Lightweight emitter

**Niagara emitter s pevně danou funkčností — řádově levnější a řádově omezenější.**

Naměřeno na krocích deseti postav: herní vlákno **1,3 → 0,2 ms**, paměť **2,7 → 0,27 MB**, GPU cena na nule (nedispatchuje se). Cena je zásadní: bez scratch padu, s minimálním napojením dat a **bez dynamických vstupů** — takže se hodí na jednoduché opakující se efekty, ne na cokoli, co potřebuje dostávat data z gameplaye. Rozšířit se dá v C++. Nejde kombinovat s [Niagara Data Channelem](#niagara-data-channel), protože neumí vlastní uzly.

Kde se s tím potkáš: [Dvě cesty, jak přestat spawnovat systémy](praxe/niagara-vykon.md#dve-cesty-jak-prestat-spawnovat-systemy) · [Rejstřík: Effect type](#effect-type)

### Line of action

**Pomyslná linie procházející pózou postavy; udává, kam pohyb směřuje.**

Chceš ji rovnou a čitelnou, s částmi těla, které ji následují — zlomená nebo komplikovaná linie ničí účel pózy a pohyb se hůř čte. Spolu s těžištěm (musí padat nad chodidla, pokud zrovna nechceš ukázat ztrátu rovnováhy) je to základ, který stojí před vším ostatním: animace je série póz, takže špatná póza se nedá zachránit časováním.

Kde se s tím potkáš: [Art specializace: animace](teorie/art-specializace.md)

### Live coding

**Tvorba hudby psaním kódu, který zní okamžitě a mění se za běhu — takže skládání a vystoupení splývají.**

Nejdostupnějším nástrojem je **Strudel** (viz vlastní heslo). Podstatný rozdíl proti DAW: nepokládáš události na časovou osu, ale **popisuješ dělení cyklu**, takže se rytmus mění změnou jednoho čísla. Vedlejší důsledek, který stojí za zmínku: protože se nástroj mění během hraní, **vlastní knihovna funkcí je zároveň nástroj i styl** — určuje, co je při vystoupení snadné, a tedy co zahraješ.

Kde se s tím potkáš: [Live coding: hudba jako kód](hudba/live-coding.md) · [Rejstřík: Strudel](#strudel)

### Live Link

**Systém pro streamování dat do enginu (mocap, kamery, DCC nástroje) — a od 5.8 s Live Link Hubem i offline zpracování videa.**

Pro markerless mocap: Live Link Hub → Capture Manager → Mono Video Ingest převede MP4 na capture data, které umí číst MetaHuman Performance. Živá cesta (telefon jako facial kamera, mocap obleky) používá tentýž systém — proto to jméno.

Kde se s tím potkáš: [Animační nástroje](praxe/animace-nastroje.md) · [Markerless mocap: Live Link Hub a Capture Manager](praxe/animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku)

### Local exposure

**Expozice, která se liší po částech obrazu: tmavé oblasti zesvětlí a světlé ztlumí, aniž by se změnila celková expozice.**

V post-process volume se ladí kontrastem světel a stínů, prahy a detail strength. Funguje podobně, jako když se do HDR skládají dvě expozice. Šablony Unrealu mají kontrast 0,8, nově přidaný post-process volume 1,0, a to je častý zdroj nesouladu. Prahy dovolí nejtmavší pixely ze zvedání vynechat, aby obraz nepřišel o čistou černou.

Kde se s tím potkáš: [Expozice, která drží](praxe/megalights.md#expozice-ktera-drzi-kalibrace-local-exposure-a-dva-modely-svetla) · [Rejstřík: Auto exposure](#auto-exposure)

### Locomotor

**Control Rig uzel pro procedurální chůzi: počítá došlapy dynamicky podle pohybu, žádné animační klipy.**

Foot sets definují končetiny (fázové offsety = charakter chůze — pavouk 0/0,25/0,5/0,75), pelvis settings usazení těla, stepping výšku a tempo kroků; do kostí to propíše Full Body IK s effectory na špičkách. Ladí se collision radius per noha a max collision height. Experimental plugin; Epic jím demí mecha v GASP.

Kde se s tím potkáš: [Animační nástroje](praxe/animace-nastroje.md) · [GASP](praxe/gasp.md)

### Locus of control

**Kde člověk hledá řídicí sílu svého jednání: uvnitř (sám se rozhoduju), nebo venku (čekám, až mě někdo dotlačí).**

Pojem z psychologie: výchova, kde motivaci vždy dodával někdo zvenčí, pěstuje externí locus — a v dospělosti se čeká na dalšího „dozorce". Tvůrčí dospělost znamená převzít roli disciplinující figury sám nad sebou; vnější závazky (ukázka k datu) jsou legitimní berlička.

Kde se s tím potkáš: [Produktivita](teorie/produktivita.md)

### LOD

**Level of Detail: jednodušší verze meshe, které engine střídá podle vzdálenosti nebo velikosti na obrazovce.**

LOD0 je plná verze, LOD1, LOD2 a další mají méně trojúhelníků a často i levnější materiál. Přepínání šetří geometrii i paměť, ale bez dobrého přechodu je vidět doskakování (popping); clony a zakřivené ulice ho dokážou schovat. Vzdálená náhrada celé skupiny objektů je [HLOD](#hlod), Witcher 3 jí říká proxy. Nanite v UE5 nahrazuje ruční LODy průběžnou volbou detailu. Kde Nanite použít nejde, a v jiných enginech, se LODy dělají dál.

Kde se s tím potkáš: [Beauclair: streamování LODů](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [007 First Light: mech podle vzdálenosti](praxe/env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka) · [Rejstřík: HLOD](#hlod) · [Rejstřík: Nanite](#nanite)

### Look ahead

**Předsazení kamery směrem, kam se hráč dívá nebo poletí — kamera sleduje pozornost, ne sprite.**

Horizontálně podle směru pohybu (v obousměrných hrách se přepíná), vertikálně podle fáze skoku: na zemi nad hlavu (plánuješ skok), v apexu na tělo, při pádu pod nohy. Vedlejší efekty (bump při dopadu) bývají zadarmo a stojí za ponechání.

Kde se s tím potkáš: [Kamera](teorie/kamera.md)

### Loose coupling

**Princip: třídy na sobě závisejí co nejméně — komunikují přes smlouvy (interfacy) a eventy, ne přes tvrdé reference.**

Diagnóza vazeb: Reference Viewer („proč ability závisí na třídě nepřítele?"). Léky: interface místo castu (damageable — „poskytneš-li Take Damage, zavolám ji"), mediátor mezi systémy (event subsystem mezi gameplayem a UI), broadcast kanály. Odměna: systémy jdou měnit a nahrazovat nezávisle — definice škálovatelnosti.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md)

### Low-fi prototyp

**Prototyp schválně nízké kvality — náčrt na papíře, čmáranice, hrubá animace konceptu — vytvořený za minuty.**

Jeho supersíla je psychologická: do vypiplaného dema se kritikům tluče těžko, ale náčrt za pět minut nikoho nesvazuje — dostaneš syrový názor na *myšlenku*, dokud se dá směr měnit zadarmo. Protějšek high-fi prototypu (funkční hratelné kostry), který je dražší a láká k připoutání. Srovnej s grayboxem: i tam jde o levné testování, ale mechaniky, ne nápadu.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md) · [Prototypování](teorie/prototypovani.md)

### Low-pass filtr

**Filtr propouštějící nízké frekvence a ubírající vysoké (low-pass filter).**

Základní nástroj subtraktivní syntézy: z bohaté vlny „ořízne" výšky. Libovolná vlna v nízké oktávě protažená úzkým low-pass filtrem dá bas.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Lumen

**Realtime globální osvětlení a odrazy v UE5 — nepřímé světlo bez pečení, za cenu stálého rozpočtu.**

Orientační rozpočet od Epicu: **~4 ms na 60 FPS, ~8 ms na 30**. Ověřuje se operativně — vypni ho (`r.DynamicGlobalIlluminationMethod 0`, `r.ReflectionMethod 0`) a změř, o kolik se snímek zrychlí; to je jeho skutečná cena, protože v profileru je rozprostřený do víc položek (scene lighting, diffuse indirect a AO, reflections). Ladí se ve dvou větvích: **screen traces** (hodnoty z pixelů na obrazovce) proti **world traces** (z Lumen scény) — vypnutí screen traces je nejrychlejší způsob, jak zjistit, kterou půlku prohledávat.

Kde se s tím potkáš: [Lumen: rozpočet a binární hledání](praxe/gpu-pruchod.md#lumen-rozpocet-a-binarni-hledani) · [Rejstřík: Surface cache](#surface-cache) · [Rejstřík: Nanite](#nanite) · [Mortal Shell 2: osekaný rozpočet](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek) · [Lumen a MegaLights spolupracují](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis) · [Lumen po změně světla dohání](praxe/megalights.md#expozice-ktera-drzi-kalibrace-local-exposure-a-dva-modely-svetla)

### Ludonarativní disonance

**Nesoulad mezi tím, co hra říká příběhem, a tím, co odměňuje gameplayem (Hocking o BioShocku, 2007).**

Sympatický hrdina cutscén vyvraždí v gameplayi stovky lidí. Není inherentně špatná: humor (sbírky zelí ve vážném Skyrimu) i identita hry (Cult of the Lamb: roztomilé + temné) na disonanci stojí. Vadí, když podrývá pointu, kterou hra vážně míní — a cítí ji každý jinak.

Kde se s tím potkáš: [Ludotematický soulad](teorie/ludonarativni-soulad.md)

### Ludus a paidia

**Cailloisovo spektrum hry: ludus = hra podle přísných pravidel, paidia = volné blbnutí bez cíle.**

Videohry dnes potřebují obojí — když hra působí holá, má často moc ludus a málo paidia. Expresivní mechaniky (emoty, hlouposti bez užitku) jsou paidia vrstva nad pravidly. Od téhož autora pochází i čtveřice agon/alea/mimicry/ilinx.

Kde se s tím potkáš: [Systémy a mechaniky](teorie/systemy-a-mechaniky.md) · [Zábava: taxonomie a pilíře](teorie/zabava.md)

### LUT

**Look-up table: tabulka, která přemapuje barvy obrazu na jiné, ve hrách typicky pro barevné ladění (color grading) v postprocesu.**

Ve hrách je to obvykle malá textura, třeba 16 × 16 × 16 barev rozložených do pruhu, ve které každá vstupní barva najde svou výstupní. Grading se tak připraví v grafickém programu na screenshotu a engine ho levně aplikuje na celý snímek. UE ji bere v Post Process Volume jako Color Grading LUT. V rozboru pipeline Naughty Dog ji autor zmiňuje u posledního kroku, postprocesu, a Mortal Shell 2 má podle rozboru přes 25 LUTů.

Kde se s tím potkáš: [Hybridní blockout: postprocess](praxe/blockout.md#hybridni-blockout-hodnoty-a-barva-driv-nez-materialy) · [Mortal Shell 2](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek)

### Markerless mocap

**Motion capture z obyčejného videa bez markerů a obleku — pohyb se odhadne z obrazu jedné kamery.**

Klasické cesty, optický systém s markery nebo inerciální oblek, potřebují hardware, čas na nasazení i na čištění dat. Markerless snižuje vstupní bariéru na kameru a světlo — kvalita výsledku ale přímo závisí na záznamu (celé tělo v záběru, pevná kamera, rovnoměrné světlo, kontrastní a nevolné oblečení). V Unrealu ho od 5.8 experimentálně umí [MetaHuman Animator](#metahuman-animator); výstup je výchozí bod pro dočištění.

Kde se s tím potkáš: [Markerless mocap v 5.8](praxe/animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku) · [MetaHuman jako standard](praxe/metahuman.md#metahuman-jako-standard-auto-rigging-cizich-postav-davy-a-otevreny-rig) · [Ruce, které Kimodo nemá](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu)

### Material Instance

**Potomek materiálu, který přebírá jeho graf a mění jen vystavené parametry — barvu, texturu, číslo.**

Rodičovský materiál definuje logiku a parametry, instance je jen sada hodnot: tři barvy klíčů jsou tři instance, ne tři materiály. Změna rodiče se propíše do všech instancí. Instance se nastavuje v editoru; za běhu se parametry mění přes [Dynamic Material Instance](#dynamic-material-instance).

Kde se s tím potkáš: [Hádanka ze stavebnice](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit) · [Master material](praxe/materialy.md#master-material-pet-textur-nema-mit-kazdy-mesh) · [Pět potvrzení rány](praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem)

### Material Parameter Collection

**Asset se sadou globálních parametrů, které čte libovolný počet materiálů najednou.**

Změna jedné hodnoty, třeba z Blueprintu nebo editor utility, se hned projeví ve všech materiálech, které kolekci používají. Hodí se na denní dobu, počasí nebo globální efekty. Na rozdíl od parametru v material instanci nepatří jednomu materiálu, ale celé scéně.

Kde se s tím potkáš: [Expozice, která drží: neony podle času](praxe/megalights.md#expozice-ktera-drzi-kalibrace-local-exposure-a-dva-modely-svetla) · [Falešné okno](praxe/materialy.md#falesne-okno-interior-cubemap-a-mistnost-nafocena-v-enginu) · [Rejstřík: Material Instance](#material-instance)

### MAYA

**Most Advanced Yet Acceptable: nejpokročilejší varianta, kterou publikum ještě přijme.**

Princip z průmyslového designu, který se dobře hodí na volbu míry inovace ve hře — obvyklé doporučení zní, že hra má být zhruba z třetiny nová a ze zbytku srozumitelně žánrová. Chrání před dvěma extrémy: klonem, který nemá důvod existovat, a hrou tak originální, že jí nikdo nerozumí (viz hook a anchor).

Kde se s tím potkáš: [Co prodává: hraj hry jako profesní povinnost](teorie/co-prodava.md) · [Nápad](teorie/napad.md)

### Map (dictionary)

**Datová struktura klíč → hodnota: místo „co je na indexu 3" se ptáš „kolik stojí Big Mac".**

Klíč je čitelný a smysluplný; přidání a úprava mají stejnou syntax (nový klíč přidá, existující přepíše), klíč musí sedět přesně (překlep = nový klíč = tichý bug) a nesmí být měnitelný. V Blueprintech je to node Map; příbuzné jsou Data Table s Row Name jako klíčem.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md) · [Ukládání](praxe/ukladani.md) · [Strana dveří → data](praxe/interakcni-animace.md#objekt-vi-jak-se-s-nim-zachazi-data-interakce-patri-k-veci-ne-k-postave) · [Výška → montáž zvednutí](praxe/interakcni-animace.md#predmet-do-ruky-bez-teleportu-attach-neni-snap-a-dosah-neni-dohled) · [Terč: mapa směr → montáž](praxe/souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave)

### Marching cubes

**Algoritmus (1987), který z 3D skalárního pole vyrobí mesh: 8 sousedů = krychle = 256 případů s předpočítanými polygony.**

Původně pro vizualizaci CT/MRI; dnes základ voxelových terénů, deformovatelných jeskyní a metaballů. Hodnoty nad/pod prahem čte jako bity 8bitového čísla a „pochoduje" polem, dokud nevyskládá celý povrch.

Kde se s tím potkáš: [Algoritmy, které stojí za to znát](teorie/algoritmy-prehled.md) · [Mesh Terrain (UE 5.8)](praxe/mesh-terrain.md)

### Market research

**Průzkum trhu před rozhodnutím o hře: výdělky žánrů, tagy, recenze konkurence, benchmarky.**

První krok k objektivitě proti zamilovanosti do vlastního nápadu. Prakticky: Steamové roční žebříčky, SteamDB, Gamalytic/VG Insights, benchmarky Chrise Zukowského; okno posledních ~3 let (starší data lžou) a medián či spodních 25–30 % výdělků, nikdy průměr. Nejcennější levný zdroj: negativní recenze konkurence — seznam bolestí, proti kterým můžeš designovat.

Kde se s tím potkáš: [Idea iceberg](teorie/rady-z-praxe.md) · [Nápad: yoink & twist](teorie/napad.md)

### Markovův řetěz

**Stavy + pravděpodobnosti přechodů + memoryless vlastnost: pro predikci dalšího kroku stačí současný stav, historie je fuk.**

Markov jím dokázal, že i závislé události poslouchají zákon velkých čísel. Sedí uvnitř PageRanku, Monte Carlo simulací i prediktivního textu — a ve hrách v každém stavovém stroji s pravděpodobnostními přechody, generátoru počasí či pity systému dropů.

Kde se s tím potkáš: [Markovovy řetězce a Monte Carlo](teorie/markovovy-retezce.md)

### Mass Entity

**ECS framework UE pro simulaci tisíců entit — davy, doprava; pohání City Sample i MetaHuman Crowd.**

Entity nejsou actory: data žijí ve fragmentech zpracovávaných hromadně, proto škálování na tisíce NPC s navigací a vyhýbáním. Pro viditelnost se kombinuje s instancovanými meshi a streamováním plných actorů u kamery.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md) · [Mass a ECS: proč objekty zpomalují](praxe/mass-ecs.md#proc-objekty-zpomaluji-pamet-kterou-nactes-a-zahodis) · [Entita není actor](praxe/mass-ecs.md#entita-neni-actor-rozkladej-podle-pristupu-do-pameti-ne-podle-postavy) · [Jak s Mass pracovat](praxe/mass-ecs.md#jak-s-mass-pracovat-diagram-debugger-a-jedna-implementace-misto-dvou) · [Davy MetaHumanů v 5.8](praxe/metahuman.md#metahuman-jako-standard-auto-rigging-cizich-postav-davy-a-otevreny-rig)

### Material function

**Znovupoužitelný blok materiálové logiky — funkce, kterou vložíš do libovolného materiálu v projektu.**

Se vstupem a výstupem typu material attributes funguje jako vrstva: materiál postavy → funkce (decay, sníh, mokro) → výstup. Uvnitř Get/Set Material Attributes upraví jen vybrané atributy, zbytek proteče beze změny. Jedna funkce pro celý projekt znamená i opravy na jednom místě.

Kde se s tím potkáš: [Materiály](praxe/materialy.md) · [Kámen ze čtyř vrstev](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen) · [Mortal Shell 2](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek) · [Contact shadows jako material function](praxe/landscape-tipy.md#hloubka-bez-geometrie-pom-contact-shadows-a-plugin-ihp)

### Matice

**Blok čísel čtený jako lineární transformace: sloupce říkají, kam se přesunou osy prostoru.**

Identity nedělá nic, diagonála škáluje osy, záporná čísla zrcadlí, rotační matice je bod na jednotkové kružnici. Násobení matic = skládání transformací do jedné. Homogenní souřadnice (4×4 v enginech) propašují do matice i translaci — proto je transform jedna matice.

Kde se s tím potkáš: [Lineární algebra vizuálně](teorie/linearni-algebra-vizualne.md) · [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### McNamarův klam

**Chyba rozhodování, kdy se to, co jde snadno změřit, prohlásí za to jediné důležité.**

Pojmenováno po ministru obrany, který během války ve Vietnamu řídil postup podle počtu zabitých nepřátel — metriky rostly, válka se prohrávala. V gamedevu se projevuje sledováním wishlistů, zhlédnutí nebo počtu recenzí namísto obtížně měřitelných věcí, jako je to, jestli hra někoho baví a jestli ji doporučí dál.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#mcnamaruv-klam-co-se-snadno-meri-neni-totez-co-dulezite) · [Playtesting](teorie/playtesting.md)

### MCP

**Model Context Protocol — standard, kterým AI agent (Claude Code, Codex, Gemini…) mluví s nástroji; od 5.8 nativně v Unrealu.**

Trojice pluginů Unreal MCP + Terminal + Editor Toolset dá agentovi kontext projektu a kontrolu nad editorem: blueprinty, materiály, PCG, level design. Config per agent generuje konzolový příkaz (.mcp.json). Stejný protokol propojuje agenty s Blenderem i ComfyUI. Zlaté pravidlo: obecný prompt = obecný výsledek — rozepsaná logika a detailní zadání dělají rozdíl.

Webinář Epic Education uvádí jako potřebnou trojici Unreal MCP, All Tool Sets a Editor Tool Set; Terminal je podle všeho potřeba jen pro terminál přímo v editoru. Plugin MCP sám nástroje nemá, dodávají je tool sety, a protože jejich popisy zabírají hodně kontextu, záleží i na harnessu a modelu.

Kde se s tím potkáš: [AI agenti: Claude Code a MCP](praxe/claude-code-ue.md) · [MCP v editoru](praxe/mcp-v-editoru.md) · [MCP místo klikání](praxe/claude-code-ue.md#mcp-misto-klikani-agent-v-blenderu-od-blockingu-po-rig)

### MCP Inspector

**Oficiální ladicí klient pro MCP: vypíše všechny nabízené nástroje a dovolí je volat přímo, bez agenta.**

Hodí se, když agent hlásí, že nástroje nevidí, a nepomohl ani Output Log s podrobnějším výpisem. Lektor Epic Education ho ale za měsíce práce nepotřeboval.

Kde se s tím potkáš: [Rozjet MCP](praxe/mcp-v-editoru.md#rozjet-mcp-tri-pluginy-agent-ze-spravne-slozky-a-co-delat-kdyz-nic-nevidi) · [Rejstřík: MCP](#mcp)

### MDA framework

**Mechanics → Dynamics → Aesthetics: mechaniky se dějí v kódu, dynamika v akcích hráče, estetika v jeho pocitech.**

Akademický rámec (2004) pro analýzu mechanik: designér sahá jen na mechaniky a změny kaskádují — málo munice → opatrné chování → strach. Půjčuješ-li mechaniku z jiné hry, MDA odpovídá na otázku, PROČ tam funguje a jestli u tebe vyrobí tytéž pocity.

Kde se s tím potkáš: [Základy designu: MDA](teorie/zaklady.md) · [Systémy a mechaniky](teorie/systemy-a-mechaniky.md)

### Mechanika

**Jednotka gameplaye složená z pravidel: sloveso hráče (skoč, seber, unikni) — nástroj, kterým se působí na herní svět.**

Pravidla jsou logika („když tohle, pak tohle"), mechaniky z nich skládají interakce a systémy jsou větší celky, se kterými hráč skrze mechaniky jedná. Stejné sloveso s jinými pravidly je jiný pocit — a pocit jádrové mechaniky je charakter hry.

Kde se s tím potkáš: [Systémy a mechaniky](teorie/systemy-a-mechaniky.md) · [Rejstřík: Core loop](rejstrik.md#core-loop)

### Mediator pattern

**Prostředník, přes kterého aktéři komunikují místo napřímo — každý pak závisí jen na něm.**

Analogie je řízení letového provozu: letadla se nedomlouvají mezi sebou, mluví s věží. V UE typicky aktér v levelu (combat manager koordinující, kdo smí útočit) nebo objekt na Game State (event manager rozesílající události). Kombinuje se s rozhraními: mediátor definuje, co od aktérů potřebuje, a implementaci nechá na nich.

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md#mediator-koordinator-uprostred-a-event-manager-v-game-state) · [Design patterns](teorie/design-patterns.md#tri-rodiny-vzoru-tvorba-struktura-chovani)

### MegaLights

**Systém UE od 5.5, který zlevňuje scény s velkým počtem stínících světel.**

Místo aby každé světlo platilo plnou cenu za stíny a výpočet, MegaLights je vzorkuje sdíleně, takže se desítky až stovky dynamických světel stanou realistickou volbou. Pro workflow, kde se scéna maluje z mnoha malých zdrojů místo jednoho směrového světla, je to zásadní rozdíl.

Od 5.8 jsou připravené pro produkci. Každý pixel má pevný počet vzorků, takže cenu určuje hlavně rozlišení a kvalita klesá tam, kde se překrývá moc světel. Na silné slunce se nepoužívají, to patří virtuálním stínovým mapám. S forward shadingem nefungují a hardwarový ray tracing nepotřebují.

Kde se s tím potkáš: [Osvětlení: malovat světlem](praxe/osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel) · [Jiná cesta v 007 First Light](praxe/env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka) · [Rozpočet vzorků na pixel](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis) · [Attenuation radius jako hlavní páka](praxe/megalights.md#attenuation-radius-jako-hlavni-paka-pocitej-prekryvy-ne-svetla) · [Svítidlo z víc světel](praxe/megalights.md#svitidlo-z-vic-svetel-odraz-mlha-a-stin-se-ladi-zvlast) · [Slunce bez MegaLights](praxe/megalights.md#slunce-bez-megalights-silne-svetlo-spolkne-rozpocet)

### Megascans

**Knihovna fotogrammetrických skenů povrchů, skal a vegetace od Quixelu (Epic), dnes dostupná přes Fab.**

Skeny jsou kalibrované pro PBR, takže z nich i malý tým dostane realistický povrch bez vlastního skenování. Protože je používá spousta her i studentských prací, hrozí, že všechno vypadá stejně. Mortal Shell 2 ukazuje, že rozdíl dělá přizpůsobení: vlastní shadery, masky, LUTy a malá knihovna tilerů. Workshop o kitech je bere jako referenci tvarů pro kupky.

Kde se s tím potkáš: [Mortal Shell 2](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek) · [Organický kit: kupky](praxe/modularni-kity.md#organicky-kit-a-spoje-zaborit-nechat-rust-od-zdroje-zakryt-sev) · [Rejstřík: Asset pack](#asset-pack) · [Rejstřík: PBR](#pbr) · [Dark Ruins a volumetric sampling](praxe/pcg-liany.md#podlaha-steny-a-strop-jednim-grafem-volumetric-sampling-misto-mesh-sampleru)

### Mesh distance field

**Předpočítané pole vzdáleností k nejbližšímu povrchu meshe — shader se může kdykoli zeptat „jak daleko je geometrie?".**

Zapíná se v project settings, kontroluje vizualizačním viewmodem. Uzel Distance to Nearest Surface na něm staví efekty obtékající objekty: mlha plazící se po zdech, sníh u stěn, ohořelé okraje. Stejná data pohání distance field stíny a AO.

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Rejstřík: Global Distance Field](#global-distance-field) · [007 First Light: GI proti distance fields](praxe/env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka)

### Meshlet

**Malý shluk trojúhelníků (třeba 64 trojúhelníků a 64 vrcholů), na které se rozdělí mesh, aby se dal ořezávat a kreslit po kouscích.**

Každý meshlet nese obal, typicky kouli a kužel normál, takže GPU může zahodit kousky mimo záběr, zakryté nebo odvrácené dřív, než je vykreslí. Je to stavební kámen mesh shaderů a virtualizované geometrie: Nanite stojí na stejném principu se svými clustery a navrch má hierarchii detailu. Alan Wake 2 má v ukázkové scéně kolem 4 milionů meshletů a u skinované vegetace jejich obaly přepočítává compute shaderem.

Kde se s tím potkáš: [Alan Wake 2: meshlety](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les) · [Rejstřík: Cluster culling](#cluster-culling) · [Rejstřík: Nanite](#nanite)

### Mesh Partition

**Generická vrstva Unrealu pro autoring a streamování obřích meshů po sekcích; Mesh Terrain je terénní nástavba nad ní.**

Mesh se dělí na libovolné sekce, klidně po trojúhelnících, a ty jde načítat, upravovat a zamykat zvlášť. Zdroj tvoří base sections a modifikátory. Mezivrstva dává náhled v editoru a runtime data se staví pro každou platformu zvlášť přes transformers a build variants. Za běhu z toho vznikají běžné Nanite meshe, static meshe a kolize.

Kde se s tím potkáš: [Proč trojúhelníky a ne voxely](praxe/mesh-terrain.md#proc-trojuhelniky-a-ne-voxely-mesh-partition-od-zdroje-po-runtime) · [Modifikátory v rukou Epicu](praxe/mesh-terrain.md#modifikatory-v-rukou-epicu-poradi-vrstev-rovina-pod-poi-a-pcg-ktere-rozmistuje-skaly) · [Založení terénu](praxe/mesh-terrain.md#zalozeni-terenu-partitions-a-rozliseni) · [Rejstřík: Mesh Terrain](#mesh-terrain)

### Mesh Terrain

**Terénní systém z UE 5.8, ve kterém je terén skutečný trojúhelníkový mesh rozdělený na sekce, ne height mapa.**

Umí převisy, tunely i létající ostrovy a tvaruje se nedestruktivním stackem modifikátorů. Stojí na generické vrstvě [Mesh Partition](#mesh-partition) a za běhu dává Nanite meshe, static meshe s LODy a Chaos kolize. V 5.8 je experimentální a Epic cílí produkční připravenost na konec roku 2027.

Kde se s tím potkáš: [Mesh Terrain (UE 5.8)](praxe/mesh-terrain.md) · [Proč trojúhelníky a ne voxely](praxe/mesh-terrain.md#proc-trojuhelniky-a-ne-voxely-mesh-partition-od-zdroje-po-runtime) · [Rejstřík: Landscape](#landscape)

### Mesh to MetaHuman

**Převod cizího meshe (skenu, sculptu, modelu) na plnohodnotného MetaHumana s rigem podle standardu Epicu.**

Solver obalí mesh topologií MetaHumana a postaví skeleton a rig, takže výsledek je kompatibilní s úpravami v Creatoru, groomy, oblečením, retargetem i GASP. Dlouho šlo jen o hlavu; od 5.8 pracuje s celou postavou a Epic mu interně říká auto rigging. Co přesahuje lidský tvar (rohy, velké uši), solver ignoruje — to se přišívá ručně.

Kde se s tím potkáš: [Z cizího meshe MetaHuman](praxe/metahuman.md#z-ciziho-meshe-metahuman-solve-prenos-textury-a-prichyceni-rohu) · [MetaHuman jako standard](praxe/metahuman.md#metahuman-jako-standard-auto-rigging-cizich-postav-davy-a-otevreny-rig) · [Rejstřík: MetaHuman](#metahuman)

### MetaHuman

**Epicův systém fotorealistických postav: creator, rig obličeje i těla a nástroje (Animator, Performance) kolem.**

Od 5.8 žije tvorba přímo v enginu (MetaHuman Creator plugin; Core Data při instalaci enginu). MetaHuman Performance asset zpracuje capture data na animaci — s Body Trackingem tělo i obličej (blend shapes). První rig vyžaduje potvrzení licence na webu. Výstup jde retargetovat na libovolný skeleton — MetaHuman může sloužit jen jako mocap prostředník.

Od 5.8 ho Epic prezentuje jako standard digitálních postav: [Mesh to MetaHuman](#mesh-to-metahuman) riguje cizí postavy celé, [MetaHuman Collection](#metahuman-collection) skládá davy a DNA s [RigLogic](#riglogic) jsou open source.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md) · [Animační nástroje](praxe/animace-nastroje.md) · [GASP](praxe/gasp.md) · [MetaHuman jako standard](praxe/metahuman.md#metahuman-jako-standard-auto-rigging-cizich-postav-davy-a-otevreny-rig) · [Markerless mocap](praxe/animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku)

### MetaHuman Animator

**Nástroj, který z natočeného výkonu (video, hloubková data, zvuk) spočítá animaci MetaHumana — od roku 2023 obličej, od 5.8 experimentálně i celé tělo.**

Výkon se zpracuje v MetaHuman Performance assetu z capture dat (Live Link Hub → Capture Manager); výstupem je animation sequence pro skeleton MetaHumana, kterou jde retargetovat. Obličej umí z iPhonu, ze stereo kamer i jen ze zvuku, tělo přes markerless plugin z Fabu. Zpracování běží lokálně, ne v cloudu.

Kde se s tím potkáš: [Markerless mocap v 5.8](praxe/animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku) · [MetaHuman jako standard](praxe/metahuman.md#metahuman-jako-standard-auto-rigging-cizich-postav-davy-a-otevreny-rig) · [Rejstřík: Live Link](#live-link)

### MetaHuman Collection

**Asset (5.8, experimentální), ze kterého se z malé sady dílů skládají velké a pestré davy MetaHumanů.**

Postavy v davu se v dálce kreslí jako instancované skinned meshe (podle Epicu s asi desetinou paměti) a u kamery plynule přejdou na plnohodnotné MetaHuman actory; simulace jede přes [Mass](#mass-entity). Epic ukazuje tisíc oblečených postav na základním PS5 a 500 na mobilu. Najdeš ho v menu MetaHuman → MetaHuman Collections.

Kde se s tím potkáš: [MetaHuman jako standard](praxe/metahuman.md#metahuman-jako-standard-auto-rigging-cizich-postav-davy-a-otevreny-rig) · [Crowd plugin](praxe/metahuman.md#crowd-plugin-tisic-metahumanu-pres-mass)

### MetaSounds

**Grafový audio systém UE5 — nástupce Sound Cues: procedurální zvuk s parametry měnitelnými za běhu.**

Graf jako AnimBP: wave playery, randomizace, matematika nad audiem. Vstupní parametry (float, trigger…) se nastavují přes audio komponentu — `Spawn Sound at Location` ji vrací (Play Sound ne!), pak `Set Float Parameter`. Typické použití: jeden asset kroků, kde rychlost postavy řídí hlasitost i pitch.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md)

### Mip mapa

**Řetěz zmenšených kopií textury (4K → 2K → 1K → …), ze kterého GPU vybírá podle vzdálenosti a velikosti na obrazovce.**

Mip bias výběr posouvá: +1 = poloviční hrana (čtvrtina paměti), −1 = detailnější. Ladí se per textura (LOD Bias v editoru), per materiál (Mip Value Mode = MipBias) nebo hromadně přes property matrix. Prakticky: base color snese bias klidně +5 — dojem detailu nese normal mapa; a při DLSS/upscalingu je potřeba bias kompenzovat záporně.

Kde se s tím potkáš: [Textury a DLSS](praxe/textury-a-dlss.md) · [Nastavení výškové textury pro IHP](praxe/landscape-tipy.md#hloubka-bez-geometrie-pom-contact-shadows-a-plugin-ihp)

### Mixamo

**Webová služba Adobe s automatickým rigem a knihovnou animací, oblíbená jako mezikrok retargetingu.**

Postava z AI pipeline často dostane rig právě tady. AI animace z Kimoda jde retargetovat na kostru Mixama a odtud dál na jakoukoli jinou.

Kde se s tím potkáš: [Animace z modelu přímo ve hře](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu) · [Rejstřík: Retargeting](#retargeting)

### Mobility

**Nastavení, které určuje, jestli se aktér nebo světlo smí za běhu měnit: Static, Stationary, nebo Movable.**

Static světlo se jen zapeče. Stationary se nehýbe, ale vedle zapečeného světla vrhá dynamický stín na pohyblivé objekty. Movable je plně dynamické. Stationary světla se kvůli stínovým kanálům smějí překrývat jen omezeně, a když se jich potká moc, editor ukáže varování. V plně dynamickém projektu s MegaLights se světla dávají na movable a v Project Settings se vypíná Allow Static Lighting, aby ubylo shaderových permutací.

Kde se s tím potkáš: [Rozpočet vzorků na pixel](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis)

### Mód hry

**Struktura hraní přes sezení: roguelike, metroidvania, souls-like — neříká nic o tom, co držíš v rukou.**

Prostřední patro pyramidy žánr → mód → nálada: žánr je moment-to-moment činnost (platformer), mód je důvod pokračovat (permadeath, mapa, corpse run), nálada jsou vibes (cozy, horor). Spelunky je platformer v roguelike módu — při jednom hraní mód ani nepoznáš.

Kde se s tím potkáš: [Žánry očima designéra](teorie/zanry.md)

### Mixels

**Míchání různě velkých pixelů v jedné scéně; v pixel artu skoro vždycky vypadá špatně.**

Vzniká zvětšením jednoho spritu v enginu — jeho pixel je pak větší než pixel okolí a oko to okamžitě pozná, i když nepojmenuje. Souvisí s tím pravidlo o **velikosti plátna**: protože pixel art nejde škálovat, plátno určuje velikost objektu ve hře, takže se volí relativně k hlavní postavě, ne podle toho, kolik detailu chceš. Výjimka: zvětšení **celočíselným násobkem** mřížku zachová, a mixely tedy nedělá.

Kde se s tím potkáš: [Pixel art má měřítko](godot/pripadovka-vizual-a-zvuk.md#pixel-art-ma-meritko-mixely-a-velikost-platna)

### Moderovaný playtest

**Test, u kterého sedíš: díváš se, jak člověk hraje, mlčíš — a ptáš se přesně v místě tření.**

Setup: „máš 30 minut? chci se dívat, jak to hraješ" — osobně nebo videohovor se sdílenou obrazovkou. Pravidla: think-aloud (komentuj myšlenky nahlas), nezasahovat ani u trápení s tutoriálem, standardní otázky na konec. Protiváha: sledovaný hráč hraje jinak, proto se doplňuje širokým testem bez tebe.

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md)

### Modifier stack

**Vrstvené nedestruktivní úpravy: každá operace zůstává živým objektem, který lze dodatečně měnit, přesouvat, přeskládat nebo smazat.**

Filozofie „scéna je recept, ne výsledek" — známá z Houdini, Geometry Nodes či modifierů v Blenderu. Mesh Terrain na ní staví celé tvarování: brush, noise, spline, texture, mesh, boolean a remesh modifiery se skládají podle priorit a blend módů. Cena: recept se musí přepočítávat (build cost, FPS propady při editaci). Výhoda: žádné rozhodnutí není konečné.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Modifikátory v rukou Epicu](praxe/mesh-terrain.md#modifikatory-v-rukou-epicu-poradi-vrstev-rovina-pod-poi-a-pcg-ktere-rozmistuje-skaly)

### Modular kit

**Sada dílů na společné mřížce (stěny, podlahy, sloupy, okna), ze kterých se skládají scény jako z lega.**

Kusy sdílejí rozměry, pivoty a materiály, takže zacvaknou k sobě a texturují se sdílenými tilery a trimy. Kit začíná co nejmenším počtem kusů a roste hlavně v konkrétních situacích: opakování, detail, nový prvek, destrukce. Velikost kusu se řídí velikostí prostředí, u města je kusem klidně celé patro. Nevýhodou je hodně objektů a draw callů, proto se kusy na konci produkce někdy slučují. Pevný kit řeší švy, organický snese kusy zabořené do sebe.

Kde se s tím potkáš: [Kit jako lego](praxe/modularni-kity.md#kit-jako-lego-co-nejmene-kusu-mrizka-v-metrech-a-zoo-na-zkousku) · [Organický kit a spoje](praxe/modularni-kity.md#organicky-kit-a-spoje-zaborit-nechat-rust-od-zdroje-zakryt-sev) · [Beauclair: kit radnice](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [Rejstřík: Trim sheet](#trim-sheet) · [Rejstřík: Kitbashing](#kitbashing)

### Montage section

**Pojmenovaný úsek anim montáže; sekce na sebe navazují podle nastavených linků a kód může za běhu přesměrovat, kam se pokračuje.**

Typický tvar je start → smyčka → konec, kde smyčka navazuje sama na sebe, dokud `Montage Set Next Section` neřekne jinak — tak vznikne zápas, který čeká na reakci hráče. U párové animace se sekce přepínají na obou postavách současně, každá ve své montáži. Sekce se hledají podle jména, takže jméno v kódu musí přesně odpovídat jménu v montáži.

Kde se s tím potkáš: [Zápas se smyčkou](praxe/interakcni-animace.md#zapas-se-smyckou-sekce-montaze-a-rozhodnuti-hrace) · [Rejstřík: Anim montage](#anim-montage)

### Monte Carlo metoda

**Neumíš to spočítat? Nasimuluj tisíce náhodných běhů a přečti odpověď z histogramu.**

Zrozena z Ulamova Solitaire a neutronů Manhattan Projectu (s von Neumannem a Markovovými řetězy uvnitř), pojmenovaná po kasinu. Aproximuje řešení, která analyticky neexistují — za cenu výpočetního času a statistické jistoty. Pro designéra: balanc ekonomiky a dropů simulací místo tabulky průměrů.

Kde se s tím potkáš: [Markovovy řetězce a Monte Carlo](teorie/markovovy-retezce.md) · [Prototypování](teorie/prototypovani.md)

### Moodboard

**Sbírka referencí, která ukazuje tón a směr dřív, než vznikne první vlastní kresba.**

Dělá se před kreslením ze dvou důvodů: dá týmu možnost zkorigovat směr s minimem odvedené práce, a nutí autora směr pojmenovat. Smí obsahovat krátké deskriptory (pillars). Příliš obecný nebo roztříštěný moodboard je varovný signál — vede ke zmatku a pivotům později, protože ve skutečnosti žádný směr nedeklaroval.

Kde se s tím potkáš: [Herní art: concept art](teorie/art-pipeline.md) · [GDD](teorie/gdd.md)

### Morph target

**Uložená deformace vrcholů meshe (blend shape), kterou lze plynule zapínat váhou — základ obličejových výrazů a korektivních tvarů.**

V riggingu je alternativou ke kostem: obličej zebry v ukázce 5.8 stojí na morph targetech řízených Control Rigem. Korektivní tvar opravuje konkrétní pózu; „shot corrective" dokonce jen pózu v jednom záběru, bez zásahu do rigu (v 5.8 přes Morph Target Driver z Animator Kitu). Optimalizace obličeje MetaHumana může naopak kosti nahradit tvary.

Kde se s tím potkáš: [Rig, který se přenese](praxe/animace-nastroje.md#rig-ktery-se-prenese-controly-na-kuzi-moduly-a-tvary-bez-navratu-k-riggerovi) · [Optimalizace obličeje](praxe/metahuman.md#optimalizace-obliceje-co-dela-metapipe-nitrous)

### MotionBricks

**Model NVIDIA, který místo klasického animačního systému předpovídá pohyb postavy za běhu podle ovládání.**

Negeneruje klipy z promptu a ovládá se hlavně stylem pózy. Slibované „smart primitives" pro interakci s předměty zatím nevyšly. C++ port běží i na CPU, autor testu to ale bere spíš jako výzkumné použití.

Kde se s tím potkáš: [Animace z modelu přímo ve hře](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu) · [Kam se posunulo ARDY](praxe/ai-assety.md#animace-generovana-v-realnem-case-kam-se-posunulo-ardy)

### Motion matching

**Dotazový systém výběru animací: každý frame hledá v databázi pózu, která nejlépe naváže na trajektorii a aktuální pózu.**

Nahrazuje state machines — žádné stavy a přechody, jen databáze (PSD), schema (co a s jakou vahou měřit) a cena kandidátů; vítězí nejnižší. Stavební kameny: trajektorie (predikce pohybu), pose history (odkud jdu), chooser (která databáze), continuing pose (koho porazit). Od 5.4 v UE, showcase je Game Animation Sample; Fortnite s ním shipuje na všech platformách. Nepotřebuje stovky animací — viz sparse set.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Systémy nad MM](praxe/mm-systemy.md) · [AnimGen jako příbuzný](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu)

### Motion Warping

**Ohnutí root motion animace tak, aby trefila cílový transform — notify state v montáži + warp target za běhu.**

Základ traversalu a interakcí: Motion Matching vybere nejbližší vhodnou animaci a warp uvnitř svého okna dožene zbytkovou chybu pozice i rotace. Precomputed warp (5.7, z Witcher dema) přidává oddělené křivky pro translaci a rotaci (posun na začátku, dotočení na konci) a steering, který dráhu k cíli ohne do přirozeného oblouku.

U interakcí bez Motion Matchingu (dveře, zvednutí předmětu, párový útok) musí zbytkovou chybu unést samotná animace — proto se do ní záměrně přidává přístupový krok. U dvou postav lze warp rozdělit: obě se k sobě přiblíží napůl (váha 0,5 u obou rolí).

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [Systémy nad MM](praxe/mm-systemy.md) · [Dojít na místo: krok v animaci](praxe/interakcni-animace.md#dojit-na-misto-motion-warping-potrebuje-krok-ktery-je-v-animaci-schvalne) · [Contextual Animation](praxe/interakcni-animace.md#contextual-animation-scena-s-rolemi-misto-rucni-choreografie) · [Rozdělený warp u párových akcí](praxe/gasp.md#parove-akce-pres-motion-matching-role-rozdeleny-warp-a-vazby-koncetin)

### Motiv

**Krátká, zapamatovatelná dvou- až pětitónová buňka uvnitř melodie.**

Skvělý odrazový můstek: motiv se dá opakovat, posunout výš/níž, obrátit, zrychlit. Když melodické dovednosti nestačí, „kraď sám od sebe" — z jediného motivu vytěžíš půl skladby a výsledek zůstane soudržný. Leitmotiv je motiv přiřazený postavě či místu.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md)

### Movement Mode

**Modulární objekt Moveru definující jeden režim pohybu (walking, falling, slide…) — vyměnitelný a rozšiřitelný i v Blueprintu.**

Proti CMC, kde režimy byly zadrátované v komponentě, si módy skládáš: child mód přepíše generate-move funkci, zavolá parenta a upraví parametry (sprint = přepiš max speed podle custom input structu). Společná data módů řeší shared settings; blueprint proměnné módu se objeví v details panelu komponenty a replikují se samy.

Kde se s tím potkáš: [Mover](praxe/mover.md) · [GASP](praxe/gasp.md)

### Mover

**Nová pohybová komponenta UE — nástupce Character Movement Componentu postavený na replikaci vstupů a modulárních movement módech.**

Klíčové rozdíly proti CMC: replikují se inputy (i vlastní blueprint structy) místo výsledků pohybu, rotace je zcela volná (spin transitions, twin-stick intent) a predikce trajektorie pro Motion Matching spouští skutečný simulační kód včetně custom módů. V GASP od 5.7 výchozí; CMC postava zůstává jako legacy. Pozor na frame zpoždění vstupu (network prediction tiká před pawnem) — kameru a AnimBP krmit post-sim hodnotami.

Fyzikální variantu přináší [Chaos Mover](#chaos-mover). V GASP 5.8 má Mover i ragdoll mód, ve kterém kapsle jen sleduje pánev fyzikálního těla.

Kde se s tím potkáš: [Mover](praxe/mover.md) · [GASP](praxe/gasp.md) · [Chaos Mover](praxe/mover.md#chaos-mover-postava-jako-fyzikalni-teleso-se-stropem-sily) · [Ragdoll jako pohybový mód](praxe/ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu)

### Multithreading

**Rozdělení práce na víc vláken, aby dlouhý výpočet neblokoval běh hry.**

Kód hry běží standardně na jediném hlavním vlákně — pohyb, stavové automaty i kolize. Jedna drahá operace tam zastaví všechno ostatní. Vlákna navíc se hodí na úkoly typu „pošli data, vrať se s výsledkem": hledání cesty, načítání assetů, procedurální generování. Cena je omezení: mimo hlavní vlákno se na aktéry ve scéně obvykle sahat nesmí.

Kde se s tím potkáš: [Optimalizace: co blokuje hlavní vlákno](praxe/optimalizace.md#druha-osa-optimalizace-co-blokuje-hlavni-vlakno) · [Rejstřík: race condition](#race-condition) · [Offset cesty na pozadí](praxe/ai-ve-velkem.md#velky-nepritel-na-malem-agentovi-offset-cesty-ktery-nevyjede-z-navigace) · [Async Physics](praxe/mover.md#chaos-mover-postava-jako-fyzikalni-teleso-se-stropem-sily)

### MVP

**Minimum Viable Product: nejmenší verze produktu, která doručí jádro hodnoty — jen core loop, žádný dezert.**

Ve hrách: přihlas se → udělej věc → viz výsledek; leaderboardy, dark mode a marketplace počkají. Smysl MVP není ošidit kvalitu, ale co nejdřív ověřit, že jádro funguje a někoho zajímá — příbuzný gameplay prototypu a vertical slice.

Kde se s tím potkáš: [Jak se učit kódovat](teorie/jak-se-ucit-kodovat.md) · [Prototypování](teorie/prototypovani.md) · [GDD](teorie/gdd.md)

### Nav Agent

**Profil, pro který Unreal generuje nav data — hlavně poloměr a výška agenta.**

Poloměr agenta je odstup okraje navigace od překážek: AI se stejně velkou kapslí se pak o nic neodře a navigace nevznikne tam, kam se nevejde. Každý další agent znamená další sadu nav dat (paměť, generování). Hře s mnoha velikostmi nepřátel se proto může vyplatit jeden agent pro nejmenší velikost a šířka chodeb zapsaná do nav dat jako flag.

Kde se s tím potkáš: [Jeden nav mesh pro všechny velikosti](praxe/ai-ve-velkem.md#jeden-nav-mesh-pro-vsechny-velikosti-sirka-chodby-jako-flag-v-nav-datech) · [Velký nepřítel na malém agentovi](praxe/ai-ve-velkem.md#velky-nepritel-na-malem-agentovi-offset-cesty-ktery-nevyjede-z-navigace) · [Rejstřík: Nav Mesh](#nav-mesh)

### Navigation Query Filter

**Pravidla, která při výpočtu cesty zvýhodní, zdraží nebo vyřadí určité oblasti a flagy navigace.**

Filtr se předá s požadavkem na pohyb a běží během pathfindingu. Nav data nemění, mění jen to, jak je konkrétní dotaz čte. Typické použití: nepřítel, který neprojde ohněm, vyřadí flag ohně, a velký nepřítel vyřadí flagy úzkých chodeb. Vlastní filtry mohou dědit z výchozího.

Kde se s tím potkáš: [Jeden nav mesh pro všechny velikosti](praxe/ai-ve-velkem.md#jeden-nav-mesh-pro-vsechny-velikosti-sirka-chodby-jako-flag-v-nav-datech) · [Rejstřík: Nav Agent](#nav-agent)

### N-gon

**Polygon s víc než čtyřmi hranami — na ploché ploše neškodný, jinde zdroj chyb.**

Enginy si při importu vše stejně převedou na trojúhelníky, takže n-gon sám o sobě nevadí. Problém nastává na zakřivených plochách (nepředvídatelná triangulace, ošklivé stínování) a při dalších operacích jako subdivision nebo loop cut, které počítají s quady. Pravidlo palce: quady všude, kde se bude ještě modelovat; n-gon jen tam, kde je hotovo a rovno.

Kde se s tím potkáš: [Z fotky herní asset](praxe/foto-do-assetu.md#narovnat-obtahnout-promitnout) · [PS1 estetika](praxe/ps1-estetika.md#model-a-uv-po-stenach-krychle-quady-a-fotky-narovnane-do-obdelniku)

### N-key rollover

**Schopnost klávesnice správně nahlásit N současně stisknutých kláves; obrana proti [keyboard ghostingu](#keyboard-ghosting).**

Marketingový termín z klávesnic („anti-ghosting", „6-key rollover", „full N-key rollover"), pod kterým je konkrétní hardware — izolační diody v matici, které zabrání falešným cestám signálu. Pro vývojáře je to hlavně připomínka, že **vlastní dobrá klávesnice je nereprezentativní testovací prostředí**: co ti funguje, může u hráče s levnou membránovou klávesnicí selhat.

Kde se s tím potkáš: [GDScript: když bug není v kódu](godot/gdscript.md#kdyz-bug-neni-v-kodu-keyboard-ghosting)

### Nanite

**Virtualizovaná geometrie UE5: engine dynamicky přizpůsobuje detail meshů vzdálenosti a velikosti na obrazovce.**

Prakticky ruší ruční LOD řetězce — mesh se subdivuje a redukuje průběžně, po clusterech, podle toho, co kamera reálně vidí. Mesh Terrain je na Nanite postavený; právě adaptivní subdivize je jeden z důvodů, proč zvládá větší plochy než starý Landscape. Po editaci terénu se Nanite reprezentace přestavuje — proto FPS propad během úprav a krátký build po odkliknutí.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Nanite a velikost balíčku](praxe/nanite-do-hloubky.md#nanite-a-velikost-balicku-data-ktera-se-nikdy-nevykresli) · [Ze 100 na 200 FPS: základní cena Nanitu](praxe/lehky-render.md#ze-100-na-200-fps-co-stalo-za-vypnuti-ve-skutecne-hre) · [Mortal Shell 2: Nanite a kity](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek) · [Meshlety v Alan Wake 2](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les) · [Sklo mimo Nanite](praxe/pcg-mesta.md#budova-jako-veta-panelovy-kit-gramatika-a-patra) · [Runtime bez nových systémů](praxe/mesh-terrain.md#proc-trojuhelniky-a-ne-voxely-mesh-partition-od-zdroje-po-runtime)

### Narrative design

**Návrh vyprávění integrovaný s herním designem — protiklad modelu „designér nechá díry na cutscény a spisovatel je dopíše".**

Pojem posledních ~20 let; zahrnuje volbu typu protagonisty, směr dialogů, rejstříky řeči i vyprávěcí prostředky, které mají jen hry (flavor texty, prostředí, mechaniky). Pro malé týmy začíná třemi branami: kolik implementace vyprávění přinese, jaká je tvá spisovatelská praxe a jaké příběhy ti nabízejí tvoje nástroje.

Kde se s tím potkáš: [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Nav Mesh

**Navigační síť: oblast, ve které AI umí počítat cesty — bez ní se žádné AI MoveTo nepohne.**

Do levelu se přidává jako Nav Mesh Bounds Volume; klávesa P zobrazí zeleně pochozí plochy. Vygenerovaný RecastNavMesh má v Generation nastavení jako Agent Radius (odstup cest od stěn — lék na zasekávání o rohy) nebo výšku kroku. Body pro pohyb dodávají uzly typu Get Random Location in Navigable Radius.

Hra s mnoha velikostmi nepřátel nemusí mít nav mesh pro každou. Stačí jeden pro nejmenšího [agenta](#nav-agent), šířka chodeb zapsaná do flagů polygonů při cookování a [navigační filtr](#navigation-query-filter), který velkým nepřátelům úzká místa vyřadí (Lords of the Fallen).

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md) · [State Trees](praxe/state-trees.md) · [Jeden nav mesh pro všechny velikosti](praxe/ai-ve-velkem.md#jeden-nav-mesh-pro-vsechny-velikosti-sirka-chodby-jako-flag-v-nav-datech)

### Nearest-neighbor filtering

**Vzorkování textury bez vyhlazování — pixel zůstane pixelem.**

Výchozí *linear* filtrování mezi texely interpoluje, což je žádoucí u fotorealistických textur a katastrofa u pixel artu: přiblížený sprite se rozmaže. Přepnutí na *nearest* (jinde „point sampling") vezme nejbližší texel bez míchání a hrany zůstanou ostré. V Godotu je to `Rendering → Textures → Default Texture Filter`. Patří k témuž rodu rozhodnutí jako [integer scaling](#integer-scaling) a [pixel-perfect](#pixel-perfect) zobrazení.

Kde se s tím potkáš: [První hra: nastavení projektu](godot/prvni-hra.md#nastaveni-projektu-je-soucast-hry-ne-administrativa) · [2D vizuál](teorie/2d-vizual.md#pixel-art-je-rozhodnuti-ne-nouzove-reseni) · [PS1 estetika](praxe/ps1-estetika.md) · [Pixely z UV jako jiná cesta](praxe/ps1-estetika.md#ps1-v-enginu-mlha-jako-post-process-material-a-pixely-z-uv)

### Network Prediction

**Generalizovaný rollback framework UE — jedna ze dvou síťových větví Moveru (druhá je Chaos networked physics).**

Klienti posílají jen vstupy s časem simulace; server je bufferuje, konzumuje podle svých hodin a vysílá stav — chyby detekuje a řeší klient. Rollback je „unified": vrací se a přehrává celé okolí naráz, takže korekce bývá jedna. Prakticky: režim interpolated + Sync Inputs for Sim Proxy řeší klepání simulated proxies; pozor na frame zpoždění vstupu (tiká před pawnem).

Protože Mover tiká na začátku snímku, nový pohybový mód zařazený z herní logiky začne platit až v dalším snímku. GASP proto po vstupu do ragdollu snímek nato kontroluje, jestli se mód opravdu změnil.

Kde se s tím potkáš: [Mover](praxe/mover.md) · [GASP](praxe/gasp.md) · [Síťová fyzika zevnitř](praxe/mover.md#sitova-fyzika-zevnitr-snimky-misto-casu-resimulace-a-input-decay)

### Niagara Data Channel

**Kanál, do kterého gameplay jen zapisuje data (pozice, normála…) a jediný běžící Niagara systém z nich spawnuje částice.**

Řeší nešvar „nový particle systém per událost": sto kroků = sto zápisů do kanálu, ne sto systémů. Emitter čte přes Spawn from Data Channel; typ gameplay boost (5.7) umí při zápisu přepnout, který systém se spawne. NDC referenci ukládej jako system value.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Živý svět z částic](praxe/niagara-vykon.md#zivy-svet-z-castic-tvorove-kteri-poslouchaji-ale-nehlasuji)

### Niagara Fluids

**Plugin s šablonami fyzikálních simulací — pro interaktivní hladinu šablona Grid 2D SW Particle Collisions.**

2D grid simulace mělké vody: postava a objekty s tagy „collider" (actor i component tag, case-sensitive) dělají vlny. Ladicí trio: Velocity Dissipation (dozvuk vln), Delta Time Multiplier (tempo), Collision Velocity Multiplier (síla vstupu). Od 5.6 totéž zapíná Water Advanced plugin checkboxem (shallow water subsystem).

Kde se s tím potkáš: [Interaktivní voda](praxe/interaktivni-voda.md)

### Normal mapa

**Textura kódující, jak má povrch odrážet světlo — dodá reliéf bez přidání polygonů.**

Vzniká nejčastěji bakem z high-poly modelu na low-poly mesh: detail vysochaný v sochacím programu se promítne do textury. Spolu s height mapou (jak moc části vystupují) a barvou tvoří základní trojici map, ze které se skládá materiál.

Kde se s tím potkáš: [Herní art: character art](teorie/art-pipeline.md) · [Materiály v UE](praxe/materialy.md) · [Unikátní normála s maskami](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen)

### Normalizace vektoru

**Zmenšení vektoru na délku 1 se zachováním směru: složky vydělíš délkou (Pythagoras — a tedy odmocnina).**

Jednotkové vektory vyžaduje skoro všechno: dot product jako kosinus, osvětlení, raycasty, klouzání po zdi. Právě cena té odmocniny zrodila slavný Quake 3 hack rychlé inverzní odmocniny — dnes ji řeší hardwarová instrukce.

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Normal To Density

**PCG uzel, který převede natočení bodu na hustotu podle toho, jak moc jeho normála míří zvoleným směrem.**

S následným Density Filter z něj vznikne filtr sklonu. Osa Z s hodnotou 1 nechá podlahy, −1 stropy a čtyři uzly pro ±X a ±Y stěny, protože uzel bere jen jeden směr najednou. Dolní mez filtru určuje toleranci, 0,5 odpovídá zhruba 45°.

Kde se s tím potkáš: [Podlaha, stěny a strop jedním grafem](praxe/pcg-liany.md#podlaha-steny-a-strop-jednim-grafem-volumetric-sampling-misto-mesh-sampleru)

### Object pooling

**Předem vytvořená zásoba objektů, které se recyklují místo neustálého vytváření a rušení.**

Klasický lék na sekání u střel, částic nebo nepřátel: objekt se po „zničení" jen skryje a vrátí do zásoby, odkud si ho další výstřel vyzvedne. Šetří alokace i práci [garbage collectoru](#garbage-collection). Není to univerzální řešení — u problému s instanciací stovky složitých scén v jednom snímku pooling pomůže jen částečně a začne působit jako obcházení příčiny místo její opravy.

Kde se s tím potkáš: [Když nody opravdu bolí](godot/kompozice.md#kdyz-nody-opravdu-boli-115-ms-na-jednu-obrazovku) · [Pooling efektů kroků](praxe/footsteps.md#castice-podle-povrchu-trace-z-chodidla-pooling-a-sila-podle-rychlosti)

### Obrat akordu

**Tentýž akord s jiným pořadím tónů — jednu notu posuneš o oktávu.**

Akord zůstane týž, ale zní jinak a přechody mezi akordy sedí líp. Praktický zvyk: nejdřív si odděl basové tóny (o oktávu dolů), pak obracej zbytek, ať neztratíš přehled, co je bas.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Observer pattern

**Objekty se přihlásí k odběru událostí jiného objektu; zdroj při události obvolá odběratele — nikdo nepolluje smyčkou.**

YouTube zvoneček jako architektura: subscribe/unsubscribe u zdroje, notify při události. V UE je to doslova Event Dispatcher (bind/unbind/call). Pozor na event callback hell — událost spouštějící událost spouštějící událost.

Kde se s tím potkáš: [Design patterns](teorie/design-patterns.md) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md)

### Occlusion culling

**Vyřazení objektů, které jsou v záběru, ale schované za jinými, dřív, než je GPU začne kreslit.**

Frustum culling zahodí, co je mimo pohled, occlusion culling to, co zakrývá něco bližšího, třeba dům za zdí. Dělá se předpočítaně (Witcher 3 na to měl middleware Umbra), nebo za běhu z hloubky a hrubých obalů. V Unrealu je dynamická okluze zapnutá standardně a Nanite ořezává po clusterech. Funguje jen tehdy, když level má co zakrývat, a proto jsou clony a zakřivené ulice i výkonové rozhodnutí.

Kde se s tím potkáš: [Beauclair: Umbra a clony](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [Alan Wake 2: culling po stupních](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les) · [Rejstřík: Cluster culling](#cluster-culling) · [Rejstřík: Visual blocker](#visual-blocker)

### Oktáva

**Vzdálenost mezi tónem a jeho příštím výskytem; frekvenční poměr 2:1.**

Dvanáct tónů se dokola opakuje po oktávách; C o oktávu výš je „totéž C, jen výš" a spolu splývají. Nejkonsonantnější interval — přímý důsledek zarovnání první alikvóty.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Octree

**Rekurzivní dělení prostoru na osminy; základ prostorových indexů a streamovacích dlaždic.**

Proti pravidelné mřížce má jednu zásadní výhodu: dá se udělat **adaptivní** — každá dlaždice se testuje proti prahu (třeba 20 000 trojúhelníků) a dělí se dál jen tam, kde je detail. Dělení pak sleduje složitost obsahu místo aby ho ignorovalo, což u naskenovaných dat znamená řádově méně dlaždic při stejné kvalitě. Táž logika jako u Nanite clusterů: **struktura má kopírovat obsah, ne souřadnice.**

Kde se s tím potkáš: [Odložit místo zlevnit](praxe/velke-svety.md#odlozit-misto-zlevnit-skorapka-prvni-interier-na-vyzadani) · [Rejstřík: Cluster culling](#cluster-culling)

### Onboarding

**Prvních pár minut, kdy se hráč učí hru — a rozhoduje se, jestli zůstane.**

Nejhůř testovatelná část hry vlastníma očima: svoje hře rozumíš, takže tření nevidíš. Playtesty mívají největší dopad právě tady; a pozor na překlad feedbacku — „hra je moc těžká" v raných minutách často znamená „hráč je zmatený", ne „sniž obtížnost".

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md) · [První dojem](teorie/prvni-dojem.md)

### One-pager

**Pitch na jednu stránku: jeden obrázek, co chci vyrobit a jak vypadá úspěch.**

Nejmenší dokument v rodině GDD — předchází i minimalistickému návrhu; slouží k prvnímu testu, jestli myšlenka unese větu a obrázek. Když one-pager nejde napsat, je pozdě na dokumenty a brzy na engine: nápad ještě není hra.

Kde se s tím potkáš: [GDD](teorie/gdd.md) · [Nápad: test 300 znaků](teorie/napad.md)

### One File Per Actor

**Režim, ve kterém má každý aktér vlastní soubor místo jednoho velkého souboru levelu.**

Bez něj nemůže na téže mapě pracovat víc lidí naráz, protože level je jeden binární soubor a konflikty se neslučují. S ním je merge triviální a mapa se sto tisíci aktéry se dá vůbec otevřít. Spolu s [World Partition](#world-partition) je to rozhodnutí **z nultého dne**: dodělat se dá, ale přepisuje historii verzování. Vývojáři Subnautiky 2 to shrnuli takto: *„upřímně si neumím představit, jak bychom tu hru bez nich udělali."*

Kde se s tím potkáš: [Sto tisíc aktérů](praxe/velke-svety.md#sto-tisic-akteru-co-unese-editor) · [Rejstřík: World Partition](#world-partition) · [Rejstřík: Version control](#version-control)

### One-way door

**Rozhodnutí drahé nebo nemožné na reverz — dělá se pomalu, vědomě a s jasným vlastníkem; opak je two-way door.**

Metafora dělí rozhodnutí na dva druhy: jednosměrné dveře (žánr hry, veřejné API, volba enginu) chtějí rozmysl, vyslovené premisy a datovaný zápis; obousměrné dveře (mechanika uvnitř žánru, interní refactor) jsou levné experimenty, kde rychlost přebíjí jistotu. Premisy jednosměrného rozhodnutí se znovu otevírají jen v sankcionovaném okně (preprodukce, gate s vertical slicem) — ne pokaždé, když má projekt špatný den. Po gate platí disagree & commit.

Kde se s tím potkáš: [Zápisky: derivační řetěz IZBY](zapisky/derivace-izby.md) · [Zápisky: cut line](zapisky/cut-line.md)

### OpenStreetMap

**Otevřená mapová databáze světa se silnicemi, půdorysy budov a jejich atributy, volně ke stažení.**

Pro procedurální města je to hotový vstup. Půdorysy a uliční síť skutečného místa jde načíst třeba z JSONu a nechat nástroj, ať na ně postaví budovy. Data sama nejsou herní level, styl a úpravy jim dodá až nástroj a artist.

Kde se s tím potkáš: [Variabilita z dat](praxe/pcg-mesta.md#variabilita-z-dat-sockety-barvy-instanci-a-presety-pod-tagy)

### Orchestrace

**Rozdělení hudby mezi nástroje a jejich smíchání do barvy (orchestration).**

Často to, co odděluje začátečnicky znějící kus od profesionálního — ale má přijít až po zvládnutí melodie, harmonie a kontrapunktu, jinak „orchestruješ prázdno". V herní hudbě obdoba výběru a vrstvení zvuků a sound fontů.

Kde se s tím potkáš: [Cesta skladatele: sedm pilířů](hudba/cesta-skladatele.md)

### Order-independent transparency

**Kreslení průhledných ploch tak, aby výsledek nezávisel na pořadí, ve kterém je GPU dostane (zkratka OIT).**

Běžná průhlednost se musí řadit odzadu dopředu a u protínajících se ploch, částic v mlze nebo víc vrstev skla to selhává: vrstvy problikávají nebo se kreslí ve špatném pořadí. OIT místo řazení ukládá nebo aproximuje příspěvky všech vrstev v pixelu a skládá je dohromady. Varianta založená na momentech (MBOIT) drží v Alan Wake 2 pohromadě mlhu, průhlednou geometrii a efekty. Systém Smolder v 007 First Light díky OIT prolíná objemy s průhlednými objekty. Cenou je paměť a výpočet navíc.

Kde se s tím potkáš: [Alan Wake 2: mlha a průhlednost](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les) · [007 First Light: Smolder](praxe/env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka) · [Rejstřík: Overdraw](#overdraw)

### Origin shifting

**Varianta floating origin: když se hráč vzdálí od počátku scény, posune se zpátky i s celým světem.**

Souřadnice pro logiku a generování světa zůstávají velké a přesné, zatímco scéna v enginu pracuje s malými čísly blízko nuly. Řeší rozbité stíny, UV a třesoucí se objekty daleko od počátku. UE5 místo toho sází hlavně na [Large World Coordinates](#large-world-coordinates).

Kde se s tím potkáš: [Dohled na kilometry](praxe/velke-svety.md#dohled-na-kilometry-vetsi-chunky-v-dalce-stromy-se-stinem-a-souradnice-ktere-nepretecou) · [Rejstřík: Fixed point](#fixed-point)

### Oscilátor

**Zdroj surového zvuku v synthu (oscillator); tvar vlny určuje barvu, a tím alikvóty.**

Sinus (bez alikvót, teplý), obdélník a pila (bohaté na alikvóty), trojúhelník. Unison navrství víc kopií vlny na notu a rozšíří zvuk do sterea.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Outer

**Objekt, ke kterému je `UObject` přivázaný — s ním žije a s ním ho uklidí garbage collector.**

Určuje se při konstrukci objektu (`Construct Object from Class`, parametr *Outer*) a záleží na něm i v multiplayeru. Změnit ho dodatečně jde (v C++ `Rename`), ale je to drahé, protože to sahá na haldu a spustí garbage collector — proto se stav mezi pickupem ve světě a inventářem posílá jako data, ne jako objekt.

Kde se s tím potkáš: [Když stav opouští inventář](praxe/inventar.md#kdyz-stav-opousti-inventar-cestuje-jako-data-ne-jako-objekt) · [Vybavení je samostatný systém](praxe/inventar.md#vybaveni-je-samostatny-system-definice-instance-manazer-a-akter) · [Rejstřík: Garbage collection](#garbage-collection)

### Overdraw

**Tentýž pixel vykreslený vícekrát, protože se geometrie překrývá — tichý zabiják výkonu hustých scén.**

Typicky listí, masky a průhlednost; vizualizuje ho Nanite overdraw view (jasné/bílé plochy = zle). Léčba: redukovat překryvy — voxelizace vzdálené vegetace, plná geometrie místo masek, menší footprint assetů, mazat zakopanou geometrii. Nikdy nebude nula; loví se největší viníci vypínáním spawnerů jednoho po druhém.

Kde se s tím potkáš: [Optimalizace scény](praxe/optimalizace.md) · [PCG vegetace](praxe/pcg-vegetace.md) · [Bojovka pro desetiletý hardware](praxe/gpu-pruchod.md#bojovka-pro-desetilety-hardware-rozpocet-po-castech-a-co-se-v-nem-naslo)

### Overlay material

**Druhý materiál, který se vykreslí přes základní materiál meshe (slot Overlay Material) — bez zásahu do něj.**

Hodí se na záblesk zásahu, zvýraznění výběru nebo stav postavy, a jeden overlay funguje na všech postavách. Kreslí se ale na tvar meshe bez deformace, kterou dělá WPO základního materiálu. U postav s WPO ho je potřeba nafouknout podél normál ve vlastním WPO.

Kde se s tím potkáš: [Záblesk a kapow](praxe/souboj.md#zablesk-a-kapow-efekt-musi-sedet-na-tele-i-mezi-tely) · [Rejstřík: Hit flash](#hit-flash)

### Overlay state

**Enum-řízená vrstva pózy horního těla přes locomotion — drž pistoli, luk nebo pochodeň bez vlastních pohybových animací.**

Vzor z ALS: animation layer s Blend Poses by Enum a per ozbrojený stav Layered Blend Per Bone se single-frame pózou od clavicle nahoru; spodní tělo dál plně řídí Motion Matching. Levná cesta k „postava drží předmět" — skutečný pohyb se zbraní už chce vlastní databáze per stance.

Kde se s tím potkáš: [GASP](praxe/gasp.md)

### Pacing

**Rytmus zážitku: střídání napětí a klidu, akce a ticha, učení a mistrovství v čase.**

Nástroj režie levelů i celých her: scripted events doručují momenty „ve správnou chvíli", struktura levelu střídá zúžení a otevření, obtížnostní křivka střídá novelty a mastery. Špatný pacing má dva póly — monotónní nuda a únavný nonstop tlak; dobrý pacing je dramaturgie.

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md) · [Zábava a flow](teorie/zabava.md)

### Palette swap

**Barevná varianta spritu vyrobená přemapováním palety, ne překreslením.**

Shader dostane vstupní paletu (původní barvy) a výstupní paletu, projde pixely a barvy vymění. Ušetří to druhou sadu souborů pro tutéž postavu — a hlavně **z varianty udělá data**, takže se dá generovat, náhodně vybírat nebo vázat na region či obtížnost. Podmínka funkčnosti: paleta musí být oddělená; sdílí-li kůže a oblek tentýž odstín, přebarvíš i to, co jsi nechtěl. Historicky technika ze šetření pamětí, dnes se dělá ze stejného důvodu — odlišit variantu bez placení za druhý asset.

Kde se s tím potkáš: [Barvy: hue shifting a palette swap](godot/pripadovka-vizual-a-zvuk.md#barvy-hue-shifting-a-palette-swap-pres-shader)

### Parallax

**Vrstvy pozadí, které se pohybují pomaleji než kamera; vzniká tím iluze hloubky.**

Napodobuje to, jak vzdálené objekty ve skutečnosti zdánlivě putují pomaleji. Rychlost vrstvy přitom neurčuje jen hloubku, ale i **vnímanou velikost**: pomalejší pozadí působí větší a vzdálenější, rychlejší menší a bližší. Nepříjemnost při vývoji: v editoru se parallax počítá proti pozici editorového pohledu, takže se vrstvy „samy" posunou i při změně velikosti okna — pomůže vložit do scény referenční postavu s obrysem herní kamery.

Kde se s tím potkáš: [Level editor, který nakonec nebyl level editor](godot/pripadovka-level-a-mapa.md#level-editor-ktery-nakonec-nebyl-level-editor) · [Mapa 2D nodů](godot/zaklady.md#mapa-2d-nodu-vyber-tela-je-prvni-designove-rozhodnuti) · [Parallax vrstvy z AI](teorie/2d-vizual.md#layering-a-verticalita-staticka-kamera-jako-scenografie)

### Parallax occlusion mapping

**Pixel-shader iluze hloubky: UV se posouvají podle úhlu kamery a height mapy — reliéf bez jediného vertexu navíc.**

Levnější než displacement (žádná tessellace), ale na hraně meshe „uřízne" — siluetu neumí; varianty silhouette POM a screen space displacement to řeší až přepisem hloubky v Z-bufferu. Základ kamenných zdí Crimson Desert i kované brány v TLOU (geometrii má jen rám, ornament je textura). Cena: flickering a wobble při ostrých úhlech kamery.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md) · [AC Black Flag: falešný interiér](praxe/env-technika.md#ac-black-flag-resynced-prodat-iluzi-ne-postavit-skutecnost) · [Hloubka bez geometrie](praxe/landscape-tipy.md#hloubka-bez-geometrie-pom-contact-shadows-a-plugin-ihp)

### Pareto distribuce

**Mocninné rozdělení, kde malá menšina případů drží většinu celkové hodnoty.**

Lidově pravidlo 80/20, ale u her je poměr mnohem drastičtější — top procento titulů bere většinu tržeb celé platformy. Zásadní vlastnost: takové rozdělení nemá smysluplný průměr, takže mediánová čísla o prodejích jsou informativnější než průměrná. Viz [Extremistan](#extremistan).

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#extremistan-tri-mechanismy-ktere-vedou-ke-stejne-strategii)

### Particle system

**Systém, který z emitteru vystřeluje sprity nebo modely a řídí jejich chování v čase.**

Emitter je neviditelný bod v prostoru; nastavením se z něj stane proud vody reagující na gravitaci i jediný nehybný obrázek. Základní stavební kámen herních VFX, které na rozdíl od filmových musí běžet v reálném čase, a proto se počítají každý snímek.

Kde se s tím potkáš: [Art specializace: VFX](teorie/art-specializace.md)

### Packed Level Actor

**Skupina aktérů zabalená do jednoho assetu, který je vykreslí jako instance.**

Vzniká výběrem aktérů → pravý klik → Level → Create Packed Level Actor; alternativou je *Harvest Instances* v modeling mode nebo pole transformů v construction scriptu. Pozor na velikost: **hranice packed level actoru rozhodují, do které streamovací buňky spadne** — pokrývá-li dva bloky města a buňka je poloviční, bude načtený pořád.

Kde se s tím potkáš: [ISM, HISM a merge](praxe/pamet-a-instance.md#ism-hism-a-merge-draw-cally-podle-geometrie) · [Rejstřík: ISM](#ism) · [Rejstřík: World Partition](#world-partition)

### Pass by reference

**Předání odkazu na data místo kopie: levné a rychlé, ale změny vidí všichni, kdo sdílejí tentýž originál.**

Jazyky typicky předávají lehké typy (čísla, stringy) hodnotou — kopií — a těžké (pole, mapy, objekty) referencí („sticky note s šipkou na heap"). Mentální test proti bugům: kopíruju, nebo sdílím? V UE běží tahle hranice mezi structy (kopie) a objekty/aktory (reference).

V Blueprintu se u vstupu funkce zaškrtává Pass-by-Reference. Bez něj funkce dostane kopii structu a změny se po jejím skončení zahodí — u funkce, která má struct upravit (zdraví končetiny), je to tichý bug.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md) · [Gameplay Tags](praxe/gameplay-tags.md) · [Zdraví po končetinách](praxe/souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav)

### Passing chord

**Průchozí akord vložený mezi dva hlavní, který přemostí jejich přechod.**

Rozbije příliš jednolitý tok — do sestupné, „moc smutné" progrese vloží malé vzepětí nahoru. Krátký, obslužný akord, ne nositel harmonie.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Pawn Sensing

**Jednoduchá smyslová komponenta: kužel zraku + rádius sluchu, viditelné jako gizmo přímo ve viewportu.**

Event On See Pawn pálí každý sensing interval (default 0,5 s), dokud cíl vidí — logiku přechodu proto obal Do Once a ztrátu zájmu řeš Retriggerable Delay delším než interval. Přes zdi s kolizí nevidí. Pro víc smyslů a jemnější kontrolu je nástupce AI Perception.

Kde se s tím potkáš: [AI vnímání](praxe/ai-vnimani.md) · [Základy AI](praxe/ai-zaklady.md)

### PBR

**Physically Based Rendering: materiály popsané fyzikálními vlastnostmi (albedo, roughness, metallic, normal) místo „namalovaného" vzhledu.**

Standard herních materiálů — povrch reaguje na libovolné světlo správně, protože mapy nesou vlastnosti, ne výsledek. Proto dobrá textura nemá zapečené světlo ani stíny z reference (světlo dodá engine) a proto se AI generátorům PBR dogenerování vyplatí. Mapy nemusí sdílet rozlišení: roughness snese polovinu albeda.

Kde se s tím potkáš: [AI assety](praxe/ai-assety.md) · [Textury a DLSS](praxe/textury-a-dlss.md) · [Barva v mezích PBR už v blockoutu](praxe/blockout.md#hybridni-blockout-hodnoty-a-barva-driv-nez-materialy)

### PCG

**Procedural Content Generation — UE framework pro procedurální osazování a generování obsahu světa.**

Grafem definuješ pravidla (sampluj povrch, filtruj podle sklonu či namalované vrstvy, rozmísti stromy s hustotou X) a engine je aplikuje na libovolnou plochu. Typický řetěz: Get Landscape Data / Mesh Partition Query → Surface Sampler → Filter → Transform Points → Spawner. S Mesh Terrainem spolupracuje přes interop plugin — v beta fázi s beta mírou spolehlivosti (spolehlivější je World Ray Hit Query). V 5.7 plugin opustil betu (verze 1.0) a přibyl PCG Mode — kreslení grafů přímo v editoru.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md) · [PCG vegetace](praxe/pcg-vegetace.md) · [Instanced Actors](praxe/instanced-actors.md) · [Landscape tipy](praxe/landscape-tipy.md) · [Mesh Terrain](praxe/mesh-terrain.md) · [PCG města](praxe/pcg-mesta.md) · [Volumetric sampling](praxe/pcg-liany.md#podlaha-steny-a-strop-jednim-grafem-volumetric-sampling-misto-mesh-sampleru) · [Les pro otevřený svět](praxe/pcg-vegetace.md#les-pro-otevreny-svet-co-se-nacte-s-levelem-a-co-roste-kolem-hrace) · [Agent staví přes PCG](praxe/mcp-v-editoru.md#asistent-ne-zazrak-slovnik-priklady-a-skills-delaji-z-llm-stavitele-sveta)

### PCGEx

**PCG Extended Toolkit: plugin třetí strany, který rozšiřuje výchozí sadu PCG o širokou škálu uzlů.**

Lucid Games ho v přednášce o městech používá na zaoblená nároží (bevel), čtení socketů z meshů a generování vodorovného značení. Podle přednášky je jeho čtení socketů výrazně rychlejší než stejná práce v blueprintu. Není součástí enginu, takže verze pluginu musí sedět s verzí UE projektu.

Kde se s tím potkáš: [Budova jako věta](praxe/pcg-mesta.md#budova-jako-veta-panelovy-kit-gramatika-a-patra) · [Variabilita z dat](praxe/pcg-mesta.md#variabilita-z-dat-sockety-barvy-instanci-a-presety-pod-tagy) · [Blok napřed, silnice potom](praxe/pcg-mesta.md#blok-napred-silnice-potom-block-processor-a-booleany)

### PCG Mode

**Editorový režim (5.7): PCG grafy se kreslí přímo do světa — splinou, štětcem nebo volumem.**

Aktor s grafem vzniká sám a panel nástroje zrcadlí exposed parametry grafu; vlastní graf zaregistruješ přes Tool Data sekci (compatible tool tags — konvence „zahoď draw, zbytek bez mezer + tool"). Pasti verze 1.0: paint klade body podle vzdálenosti od posledního bodu (ne plochou štětce), guma maže na původních pozicích před transformy a Ctrl+Z ruší celý rozdělaný nástroj.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md)

### PCG Primitives

**Knihovna přes 80 drobných prostorových operací z PCG subgrafů, kterou Epic vydal jako slovník pro agenty.**

Jsou to plně parametrizované a zdokumentované subgrafy pro tvary, skládání, transformace, sampling, filtering a spawning. Jazykový model je řetězí jako slova a nemusí uvažovat o každém kroku. Fungují ale i bez něj a výsledek je deterministický, protože je to obyčejné PCG.

Kde se s tím potkáš: [Asistent, ne zázrak](praxe/mcp-v-editoru.md#asistent-ne-zazrak-slovnik-priklady-a-skills-delaji-z-llm-stavitele-sveta) · [Rejstřík: PCG](#pcg)

### Per-instance custom data

**Pole hodnot nastavitelné pro každou instanci zvlášť — variace bez unikátních materiálů.**

Řeší přímý rozpor: instancování vyžaduje shodný materiál, ale scéna má být rozmanitá. Místo dvaceti materiálových instancí (dvacet [shading binů](#shading-bin)) se hodnoty posílají per instanci — je potřeba nastavit *Num Custom Data Floats*. Levnější sourozenec téhož triku: náhodná variace odvozená z **pozice instance** (například posun odstínu), která nepotřebuje ani ta data.

Kde se s tím potkáš: [ISM, HISM a merge](praxe/pamet-a-instance.md#ism-hism-a-merge-draw-cally-podle-geometrie) · [Rejstřík: ISM](#ism) · [Rejstřík: Shading bin](#shading-bin) · [Barvy budov z dat](praxe/pcg-mesta.md#variabilita-z-dat-sockety-barvy-instanci-a-presety-pod-tagy)

### Pedal tone

**Tón, který zní pod celou progresí a nikdy se nemění (česky prodleva).**

Sjednotí přechody — všechny akordy teď sdílejí aspoň jeden tón — a přidá dojemnost. Když je pak zvuku moc, postav akordy kolem prodlevy: sundej kvinty a nech ji uprostřed.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Persistence key

**Záznam o změně světa uložený mimo objekt, kterého se týká — aby přežil odložení z paměti.**

Řeší problém plynulých světů s neviditelnými načítacími zónami: porazíš nepřítele, oblast se uvolní, vrátíš se a nepřítel je zase naživu. Klíč se uloží někam, co se neodkládá (typicky k hráči), a objekt se při načtení sám zeptá, jestli jeho klíč existuje. Hry s viditelně oddělenými místnostmi tenhle problém nemají, protože obnova nepřátel při vstupu do nové místnosti působí přirozeně — **rozdíl není technický, ale v očekávání hráče**. Pozor na růst: patří tam poražení bossové a otevřené zkratky, ne každý zabitý slimák.

Kde se s tím potkáš: [Persistence key: svět, který si pamatuje](godot/pripadovka-level-a-mapa.md#persistence-key-svet-ktery-si-pamatuje) · [Ukládání stavu světa](praxe/ukladani.md#ukladani-stavu-sveta-spawn-update-zniceni-a-indikator)

### Persistent level

**Hlavní (rodičovský) level, pod kterým žijí streamované sub-levely — rám, který nikdy neopouštíš.**

Hráč, GameMode i stav přežívají, protože se nikdy nemění celý level — jen sub-levely uvnitř. Nejde unloadnout; chceš-li „vyměnit svět", drž persistent prázdný a veškerý obsah měj v sub-levelech. Objekty, které mají spouštět streaming (volumes, trigger boxy), musí ležet v persistentu — jinak jsou schované spolu s levelem, který mají nahrát.

Kde se s tím potkáš: [Levely a streaming](praxe/levely-a-streaming.md)

### Physical Animation Component

**Komponenta, která motory kloubů táhne simulované kosti k animované póze — základ active ragdollu.**

`Set Skeletal Mesh Component` na BeginPlay, pak `Apply Physical Animation Settings Below` od zvolené kosti (typicky pelvis) s daty orientation/position strength. Síly jdou měnit za běhu — mapování na rychlost těla (letí = tuhý, leží = hadr) je klíčový trik věrohodných ragdollů. Gang Beasts/Human Fall Flat pocit.

Kde se s tím potkáš: [Ragdoll](praxe/ragdoll.md) · [Physics Control jako obecnější nástroj](praxe/ragdoll.md#physics-control-profily-hra-rekne-ragdoll-cisla-bydli-v-assetu)

### Physical Material

**Asset nesoucí fyzikální vlastnosti povrchu — včetně Surface Type, přes který systémy poznají, po čem stojíš.**

Surface typy se definují v Project Settings (Physical Surface, až 62 + Default). Přiřazení: v materiálu/instanci (všechny meshe s ním automaticky) nebo per-mesh override v levelu. Čtení: hit result → Get Surface Type → Switch on EPhysicalSurface, nebo mapa physical material → data v data assetu. Krom povrchových systémů nese i friction/restituci (gumový míč).

Physical materials na tělech physics assetu fungují i jako adresa zásahu: jméno materiálu z hit resultu řekne, kterou končetinu rána zasáhla.

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Interakce s předměty](praxe/interakce-predmety.md) · [Zdraví po končetinách](praxe/souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav) · [Alan Wake 2: spouštěče podle povrchu](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les) · [Povrch z trace chodidla](praxe/footsteps.md#castice-podle-povrchu-trace-z-chodidla-pooling-a-sila-podle-rychlosti)

### Physics Asset

**Fyzikální kostra skeletal meshe: kolizní těla (primitiva per kost) + constrainty (kloubové limity) — bez něj není ragdoll.**

Defaultní assety manekýnů jsou pro ragdoll nedoladěné — limity swing/twist je potřeba ladit (Simulate Selected). Klíčové triky: kinematic body na root kosti (jinak se mesh při simulaci odpojí a nejde číst rychlost), angular drive motory Twist and Swing s výjimkou pelvis, kolize tělo×tělo per dvojice tvarů.

Kde se s tím potkáš: [Ragdoll](praxe/ragdoll.md) · [Terč: smrt jako ragdoll](praxe/souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave) · [Zdraví po končetinách](praxe/souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav) · [Asset pod Physics Control](praxe/ragdoll.md#physics-control-profily-hra-rekne-ragdoll-cisla-bydli-v-assetu)

### Physics Constraint

**Kloub mezi dvěma fyzikálními těly: limity pohybu (linear/angular) + volitelné motory, které táhnou k cílové póze.**

Existuje v physics assetu (klouby ragdollu) i jako samostatný actor/komponenta ve scéně (závěs houpačky, pant). Angular limity: swing 1/2 a twist, každý Locked/Limited/Free; drive mode Twist and Swing vrací kloub do přirozené pózy. Motorům se ladí spring (tuhost) a damping.

Kde se s tím potkáš: [Ragdoll](praxe/ragdoll.md) · [Kabely, lana a Physics Control](praxe/lana-kabely.md)

### Physics Control

**Komponenta (plugin, 5.1+), která drží simulovaná tělesa u cíle laditelnou pružinou — „fyzikální, ale ovladatelné".**

`Create Control` + `Create Body Modifier` (bez něj se nastavení neaplikuje); cíl se posouvá přes `Set Control Target Position and Orientation` — pozor, uzel chce auto-generované jméno controlu. Linear Strength = poddajnost, Damping Ratio = dohoupání. Obecnější sourozenec Physical Animation komponenty — funguje na libovolných tělesech.

V GASP 5.8 se ovládá přes **profily** v Physics Control assetu. Nad physics assetem jsou definované končetiny, pro každé těleso body modifier, world-space a parent-space control a z nich sady a profily (kinematic, physical animation, ragdoll). Hra pak volá jen `Invoke Control Profile` se jménem, volitelně s maskou končetin. Profil se uplatní až při další aktualizaci komponenty, takže impulz hned po přepnutí chce simulaci zapnutou napřed.

Kde se s tím potkáš: [Kabely, lana a Physics Control](praxe/lana-kabely.md) · [Fyzika v Control Rigu při animování](praxe/animace-nastroje.md#sekundarni-pohyb-v-control-rigu-dynamics-za-behu-fyzika-a-autobake-pri-animovani) · [Physics Control profily](praxe/ragdoll.md#physics-control-profily-hra-rekne-ragdoll-cisla-bydli-v-assetu) · [Ragdoll, který se chrání](praxe/ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu)

### Pitch deck

**Krátká prezentace hry, která ještě neexistuje — simulace prvního kontaktu zákazníka s nápadem.**

Logika: první krok nákupu hry stejně neobsahuje hraní (trailer, GIF, screenshot) — pitch deck tenhle moment vyrobí bez jediného řádku kódu. Proces: brainstorm → hlasování → u top nápadů popsat smyčku (slabé se rozpadnou samy) → decky → nechat lidi vybírat. Opory: lidé skvěle *vybírají* a mizerně radí, jak zlepšovat; a deck za hodinu se zahazuje bez bolesti — málo vloženého času = málo biasu.

Kde se s tím potkáš: [Idea iceberg: pracuj zpátky](teorie/rady-z-praxe.md) · [Nápad: test 300 znaků](teorie/napad.md)

### Pixel Depth Offset

**Výstup materiálu, který posune hloubku pixelu dál od kamery, aniž by se pohnula geometrie.**

Posunutá hloubka mění, jak se povrch protíná s jinými objekty a jak na něj dopadají stíny. Hodí se na měkčí přechod mezi skálou a terénem nebo na to, aby reliéf z POM vrhal contact shadows. Hloubka se jen přičítá, takže povrch jde opticky „zatlačit" dovnitř, ale ne vytáhnout k divákovi.

Kde se s tím potkáš: [Hloubka bez geometrie](praxe/landscape-tipy.md#hloubka-bez-geometrie-pom-contact-shadows-a-plugin-ihp) · [Rejstřík: Contact shadows](#contact-shadows) · [Rejstřík: Parallax occlusion mapping](#parallax-occlusion-mapping) · [Materiál pro Virtual Heightfield Mesh](praxe/footsteps.md#stopy-do-hloubky-render-target-jako-platno-pod-postavou)

### Pixel Inspector

**Nástroj editoru, který pro pixel pod kurzorem vypíše hodnoty z renderovací pipeline.**

Ukáže pre-exposure, barvu scény před tone mappingem a po něm, finální barvu i data z G-bufferu. Hodí se na kontrolu expozice: střední šedá má být kolem 0,18 v každém kanálu.

Kde se s tím potkáš: [Expozice, která drží](praxe/megalights.md#expozice-ktera-drzi-kalibrace-local-exposure-a-dva-modely-svetla) · [Rejstřík: Auto exposure](#auto-exposure)

### Playblast

**Rychlý náhledový render animace přímo z viewportu, bez finálního renderu.**

Slouží ke kontrole timingu a kamery. V AI pipeline z něj může vycházet videomodel, který z jednoduchých primitiv udělá hotový záběr, a režírovaný pohyb pro playblasty je podle kapitoly o AI animaci její nejbližší praktické využití.

Kde se s tím potkáš: [MCP místo klikání](praxe/claude-code-ue.md#mcp-misto-klikani-agent-v-blenderu-od-blockingu-po-rig) · [Kam se posunulo ARDY](praxe/ai-assety.md#animace-generovana-v-realnem-case-kam-se-posunulo-ardy)

### Player Camera Manager

**Objekt player controlleru, který spravuje výsledný pohled hráče — mimo jiné zatmívačky (camera fade) a otřesy kamery.**

`Start Camera Fade` zatmí obraz do barvy během zadané doby, `Set Manual Camera Fade` nastaví míru zatmění ručně. Po zatmívačce před cutscénou je potřeba vrátit ji na nulu, jinak hra zůstane potemnělá. Přes něj se spouštějí i [camera shaky](#camera-shake).

Kde se s tím potkáš: [Cutscéna, která vrátí hru tam, kde skončila](praxe/cutsceny.md#cutscena-ktera-vrati-hru-tam-kde-skoncila) · [Hit stop: třes z pohledu kamery](praxe/souboj.md#hit-stop-zastav-oba-ale-kazdeho-jinak) · [Pět potvrzení rány](praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem)

### Point cloud

**Mračno bodů z laserového skenu — surová prostorová data bez ploch a bez topologie.**

Do enginu se dostává přes prostorové dělení do dlaždic a streamování; barva sedí na bodu jako vertex color, takže odpadá starost s texturami. Na rozdíl od meshových dlaždic se **vrství**: detail se přidává na sebe místo aby nahrazoval, což je vlastnost octree indexu. V herní praxi se s tím potkáš hlavně u digitálních dvojčat a reality capture pipeline — a jako referenci, podle které se modeluje.

Kde se s tím potkáš: [Odložit místo zlevnit](praxe/velke-svety.md#odlozit-misto-zlevnit-skorapka-prvni-interier-na-vyzadani) · [Rejstřík: Octree](#octree)

### Pixel-perfect

**Celočíselné škálování pixel artu, kde každý herní pixel je stejně velká mřížka pixelů monitoru.**

360p se škáluje 3× na 1080p a 4× na 1440p beze zbytku; necelé faktory míchají velikosti pixelů. Dogma s trhlinou: ve slepém testu necelé faktory skoro nikdo nepozná — teoretická vada není automaticky vnímaná vada. Zoom se řeší škálováním finálního renderu, ne kamerou.

Kde se s tím potkáš: [Kamera](teorie/kamera.md)

### Pivot

**Vztažný bod objektu: kolem něj se rotuje a škáluje, k němu se přichytává — na jeho umístění záleží víc, než je vidět.**

Nekonzistentní pivoty mezi asset packy rozbíjejí sockety (každá zbraň sedí v ruce jinak) i navazování dílců. Oprava bez DCC: modeling mode → Transform → Edit Pivot, přijmout a instance v levelu vyměnit. U kyvadel a pák je pivot přímo herní mechanika — bod závěsu určuje dráhu.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md) · [Pasti a mechaniky](praxe/pasti-a-mechaniky.md) · [Pivoty kitu](praxe/modularni-kity.md#kit-jako-lego-co-nejmene-kusu-mrizka-v-metrech-a-zoo-na-zkousku)

### Pivot (design)

**Změna směru projektu: hra našla těžiště jinde, než byl plán — a plán se přizpůsobí hře.**

Nezaměňovat s pivotem objektu (viz předchozí heslo). Signál bývá „monstrum v rohu": oblast, které se měsíce vyhýbáš, i když technicky zvládnutelná je. Recept: pivotuj k subsystému, který už prokazatelně funguje — a ověř rychlým prototypem („je to jiná hra, ale lepší"). Historická opora: GTA vzniklo pivotem z policejní honičky Race’n’Chase.

Kde se s tím potkáš: [Scope: pivot](teorie/scope.md) · [GDD: dokument není smlouva](teorie/gdd.md)

### Placeholder

**Provizorní asset, který drží místo finálnímu — kostka místo postavy, čmáranice místo ilustrace.**

Nástroj řazení priorit: dokud není jisté, že mechanika žije, každá hodina v grafice je sázka naslepo. Rada z praxe: dělej vlastní placeholdery *záměrně špatně* — hezký provizorní asset svádí k ladění, ošklivý ne. Pozor na licence: placeholdery z cizích her nesmí do ničeho vydaného, včetně dema.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md) · [Prototypování](teorie/prototypovani.md)

### Player State

**Objekt nesoucí data jednoho hráče — inventář, skóre, klíče — nezávisle na jeho pawnovi.**

Pawn může zemřít a respawnout, Player State žije dál (a v multiplayeru se replikuje všem). Vlastní Blueprint verze se registruje v Game Mode. Pravidlo „kde co bydlí": per-hráč data → Player State; session-wide → Game Instance; per-level pravidla → Game Mode.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Playtest

**Testování hry skutečnými hráči s cílem získat zpětnou vazbu — o srozumitelnosti, obtížnosti, zábavnosti.**

Nejmenší funkční forma je „ukaž rozdělanou věc kamarádovi": i to je zpětnovazební smyčka, bez které se cvičné hodiny nepočítají. Klíčová dovednost je kalibrace publika podle fáze — shovívavé publikum pro motivaci na začátku, kritické pro růst později. A čti chování, ne slova: playtesteři, kteří si o nový build říkají sami, jsou jiný signál než zdvořilé „je to hezký" (the gap).

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md) · [Vydání hry: demo prodává](teorie/vydani-hry.md) · [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Idea iceberg: the Gap](teorie/rady-z-praxe.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### Pole vector

**Cíl, který IK řešiči určuje, kterým směrem se má ohnout prostřední kloub řetězu (loket, koleno).**

Bez něj má řetěz ze tří kostí nekonečně mnoho řešení a loket se může stočit libovolně. V Control Rigu ho jde dopočítat automaticky (Compute Pole Vector), nebo zadat ručním controlem. Automatika vychází z aktuální polohy kostí, takže v krajních pózách (skoro natažená paže) může řetěz překroutit — tam je ruční control spolehlivější.

Kde se s tím potkáš: [Ruka na klice](praxe/interakcni-animace.md#ruka-na-klice-ik-v-control-rigu-prevod-prostoru-a-alfa-z-krivky) · [Rejstřík: IK](#ik)

### POM

**Zkratka pro parallax occlusion mapping — viz [Parallax occlusion mapping](#parallax-occlusion-mapping).**

Pixel-shader trik hloubky bez geometrie; v breakdownech a diskusích se běžně používá jen zkratka.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md)

### Polymetr

**Dvě či víc rytmických řad, které běží současně a mají různou délku — takže se jejich zarovnání posouvá.**

Není to totéž co polyrytmus: u polymetru mají řady stejnou dobu, ale různý počet dob v cyklu (třeba 4 proti 3), takže se vzorec zopakuje až po nejmenším společném násobku. Prakticky to dává **dlouho se neopakující groove z krátkého zápisu**, což je přesně to, co se hodí u generativní herní hudby. Ve Strudelu se píše složenými závorkami.

Kde se s tím potkáš: [Cyklus jako pizza](hudba/live-coding.md#cyklus-jako-pizza-mini-notace) · [Rejstřík: Synkopa](#synkopa)

### Polyrytmus

**Dva rytmické vzorce ve stejném metru: první doby sedí, ale dělení nesedí.**

Klasika je 3:2 — tři noty ve stejném čase jako dvě. Nezaměňovat s [polymetrem](#polymetr), kde je to naopak (mřížka sedí, těžké doby ne). Doporučení pro začátečníky je opatrnost, aby skladba nezněla zmateně — přesnější formulace ale je, že polyrytmus je nečitelný jen tehdy, když posluchač nemá čeho se držet; nad pevnou páteří naopak funguje.

Kde se s tím potkáš: [Za jeden takt: fráze, fill a prázdno](hudba/rytmus.md#za-jeden-takt-fraze-fill-a-prazdno) · [Rejstřík: Polymetr](#polymetr)

### Pose Asset

**Asset s pojmenovanými pózami, které AnimBP vybírá a míchá podle jména — typicky pózy prstů pro různé úchopy.**

Vzniká z animace, kde každý snímek je jedna póza. V AnimGraph se póza vytáhne uzlem `Pose by Name` a přes [Layered Blend Per Bone](#layered-blend-per-bone) přepíše jen část skeletu (od ruky dolů); váhu může řídit křivka v montáži. Jedna animace zvednutí tak pokryje nůž, láhev i krabici.

Kde se s tím potkáš: [Jedna animace zvednutí](praxe/interakcni-animace.md#jedna-animace-zvednuti-pro-vsechno-grip-pointy-a-pozy-ruky)

### Pose History

**Uzel v AnimBP, který si pamatuje nedávné pózy a trajektorii — z něj čte každé hledání motion matchingu.**

Plní se během aktualizace AnimBP, tedy před fyzikou, a o výsledku fyziky neví. GASP 5.8 má funkci, která do něj po ragdollu zapíše fyzikální pózu, aby motion matching vybral vstávání podle skutečné polohy těla. Latenci to nepřidá, protože matching porovnává pózu z předchozího snímku.

Kde se s tím potkáš: [Vstávání přes motion matching](praxe/ragdoll.md#vstavani-pres-motion-matching-snapshot-pose-history-z-fyziky-a-chooser) · [Rejstřík: Pose Match column](#pose-match-column)

### Pose Match column

**Sloupec chooseru, který mezi kandidáty vybranými ostatními sloupci provede motion matching — vybere animaci i snímek.**

Ostatní sloupce filtrují podle herní logiky, pose match rozhodne podle pózy a trajektorie. Od 5.8 chooser drží libovolný počet vnitřních pose search databází a každý řádek si zvolí svou. Sloupec filtruje i zapisuje do výstupního structu, proto patří na konec tabulky. Které snímky smí hledání vidět, omezují notify staty Exclude From Database a Sampling Range.

Kde se s tím potkáš: [Motion matching uvnitř chooseru](praxe/gasp.md#motion-matching-uvnitr-chooseru-pose-match-sloupec-databaze-na-radek-a-blend-space-ve-stacku) · [Vstávání přes motion matching](praxe/ragdoll.md#vstavani-pres-motion-matching-snapshot-pose-history-z-fyziky-a-chooser) · [Rejstřík: Chooser](#chooser)

### Pose Search Database

**PSD — kolekce animací pro jeden typ pohybu, ve které Motion Matching hledá pózy.**

Databáze se dělí podle stavů (idle, run starts, stops, crouch…) — jednak kvůli přehlednosti, jednak kvůli responzivitě: chooser vynutí prohledání správné databáze v ten samý frame (vzor z Fortnite). Ceny mezi oddělenými databázemi zporovnatelní normalization set. Do PSD patří sekvence, blend spacy i montáže; klipy musí mít root motion + force root lock.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Databáze na řádek chooseru](praxe/gasp.md#motion-matching-uvnitr-chooseru-pose-match-sloupec-databaze-na-radek-a-blend-space-ve-stacku) · [Databáze s rolemi](praxe/gasp.md#parove-akce-pres-motion-matching-role-rozdeleny-warp-a-vazby-koncetin)

### Pose Search Interaction Asset

**Asset pro párové animace přes motion matching: montáže přiřazené k rolím (útočník, oběť) a pravidla, jak rozdělit chybu warpu.**

Databáze s ním má schéma s kostrou pro každou roli a kanály měří kořeny postav vůči sobě. Funkce motion match multi podle ceny přidělí role a vybere dvojici animací pro skutečné postavení obou postav. Zbylou chybu dorovná motion warping, kontakty IK. Experimentální od 5.7.

Kde se s tím potkáš: [Párové akce přes motion matching](praxe/gasp.md#parove-akce-pres-motion-matching-role-rozdeleny-warp-a-vazby-koncetin) · [Rejstřík: Motion Warping](#motion-warping)

### Pose Search Schema

**Definice, co Motion Matching měří: kanály (trajektorie, pozice a rychlosti kostí) s vahami.**

Váhy říkají, na čem při výběru záleží — pozice chodidel typicky 1, rychlosti 0,3, trajektorie 1 (default 7 je moc). Vzorky trajektorie sahají do minulosti (−0,05 s) i budoucnosti (+0,35/0,7/1,0 s). Ladění je „umělecký proces": experimentuj a čti channels breakdown v debuggeru. Různé databáze můžou mít různá schémata (při skoku na chodidlech záleží míň). Kvadrupedi: přední a zadní nohy měřit zvlášť.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Pose Snapshot

**Zmrazení aktuální pózy skeletu (`Save Pose Snapshot`) jako blendovací zdroj v AnimBP — most z fyziky zpět do animace.**

Klíč k plynulému vstávání z ragdollu: tělo leží v póze, kterou žádná animace nezná — snapshot ji zachytí a Pose Snapshot uzel (stejné jméno!) z ní nechá blendovat do vstávací montáže. Alternativa: timeline nad Physics Blend Weight (postupné předání fyziky animaci).

Kde se s tím potkáš: [Ragdoll](praxe/ragdoll.md) · [Vstávání přes motion matching](praxe/ragdoll.md#vstavani-pres-motion-matching-snapshot-pose-history-z-fyziky-a-chooser)

### Post-process AnimBP

**Animation blueprint přiřazený meshi (ne postavě), který se vyhodnocuje po hlavní animaci — vždy poslední.**

Ideální pro vrstvení: look-at hlavy a očí, korekce, cloth logika — cokoli, co se má aplikovat „přes" libovolnou animaci. Vázaný na skeleton (nový skeleton = duplikát + Assign Skeleton) a sdílený všemi instancemi meshe — logika pro víc postav se větví přes Get Owning Actor.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Postmortem

**Ohlédnutí za dokončeným (nebo pohřbeným) projektem: co fungovalo, co ne a proč.**

Nejhutnější studijní žánr gamedevu — na rozdíl od tutoriálů obsahuje i cenu rozhodnutí a slepé uličky. Dobrý postmortem přiznává čísla (wishlisty, prodeje, časové odhady vs. realita) i emoce (launch blues). Psát vlastní postmortemy je nejrychlejší způsob, jak z odehraných projektů vytěžit zkušenost — viz Zápisky.

Kde se s tím potkáš: [Postmortem: tři roky na ShantyTown](teorie/postmortem-shantytown.md)

### Post-process material

**Materiál s doménou Post Process, který pracuje s hotovým obrazem scény místo s povrchem objektu.**

Z uzlu SceneTexture čte obraz (PostProcessInput0), hloubku nebo G-buffer a výsledek posílá zpátky na obrazovku. Přidává se do pole Post Process Materials v post-process volume. Blendable location určuje, ve kterém místě pipeline se uplatní, třeba před tone mappingem nebo po hloubce ostrosti. Je levný, ale o světle a stínech ví jen to, co je vidět v obraze. Typické použití je stylizace, obrysy, retro mlha nebo filtry.

Kde se s tím potkáš: [PS1 v enginu: mlha jako post-process materiál](praxe/ps1-estetika.md#ps1-v-enginu-mlha-jako-post-process-material-a-pixely-z-uv)

### Predictive interpolation

**Režim replikace fyziky, ve kterém klient míří na stav mírně za serverem a dorovnává se rychlostí, ne skokem polohy.**

Cíl je zhruba o polovinu doby odezvy za serverem, takže serverové události, třeba zlomy, přicházejí skoro načas, a mezi zprávami se cíl extrapoluje. Je levnější než resimulace a obejde se bez rewindu, hodí se tedy na objekty, se kterými hráč přímo neinteraguje (LEGO Fortnite). Zapíná se v nastavení physics replication aktéra.

Kde se s tím potkáš: [Rozbití v multiplayeru](praxe/destrukce-a-latky.md#rozbiti-v-multiplayeru-predictive-interpolation-misto-predikce) · [Rejstřík: Resimulation](#resimulation)

### Prefab

**Uložená skupina objektů i s nastavením, kterou jde opakovaně vkládat do scény jako jeden celek.**

Termín je z Unity a dalších enginů. Prefab může nést i logiku a změna ve vzoru se propíše do všech kopií. V Unrealu tu roli plní Blueprint aktor, [Level instance](#level-instance) nebo [Packed Level Actor](#packed-level-actor). Witcher 3 tak zařizoval interiéry a tržní stánky z hotových balíčků deco týmu, v 007 First Light je obdobou template, sbírka entit včetně logiky.

Kde se s tím potkáš: [Beauclair: dekorace jako balíčky](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [007 First Light: entita, template, brick](praxe/env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka) · [Rejstřík: Level instance](#level-instance) · [Rejstřík: Packed Level Actor](#packed-level-actor)

### Premature optimization

**Optimalizace před důkazem, že je potřeba — přepis na ECS ve hře, která běží na 200 FPS.**

Klasická past programátorů: výkonový strop se řeší dřív než hratelnost, workflow se deformuje kolem optimalizací a vývoj zpomalí. Pragmatická rada z praxe: 80/20 — většina velkých problémů se dá vyřešit měsíc před vydáním za zlomek času. Výjimka: tvrdý platformní cíl (slabý handheld) je požadavek, ne optimalizace. Pojem zpopularizoval Donald Knuth („premature optimization is the root of all evil").

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md)

### Press kit

**Balíček pro novináře: popis hry, kontakty, loga, screenshoty a trailer v plné kvalitě na jednom místě.**

Novinář, který o hře chce napsat, potřebuje assety hned — press kit mu šetří mailování a tobě zvyšuje šanci na pokrytí. Nástroj presskit() ho vygeneruje zdarma za odpoledne; odkaz na něj plní roli webu, dokud web není. Patří k němu press release při velkých beatech (zveřejnění stránky, datum vydání) — rozesílá se např. přes GamesPress.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Procedural Vegetation

**Editor procedurálních stromů v enginu (5.7+): strom je graf uzlů — od presetu či od nuly po export static/skeletal meshe s Nanite foliage.**

Preset Loader nebo Grower dá strukturu, žluté modifiery (carve, gravity, slope) tvarují point cloud před Mesh Builderem, foliage palette + distributor olistí (ethylene threshold = plnost) a bone reduction ladí cenu větru. Vítr běží jen na instancích (wind transform provider + BP Global Foliage Actor). Presety Mega Plants dává Quixel zdarma na Fabu zhruba měsíčně; 5.8 přidává extract to mesh (procedurální strom z existující geometrie) a object interaction.

Kde se s tím potkáš: [PCG vegetace](praxe/pcg-vegetace.md)

### Process mode

**Vlastnost nodu, která určuje, jestli běží, když je strom scény pozastavený.**

Výchozí hodnota se **dědí od rodiče**, takže pauza ve výchozím stavu zastaví skoro všechno — včetně věcí, které mají běžet dál. Typický důsledek: pauzovací menu, které se po zapauzování nedá ovládat, nebo přechod mezi scénami, který uprostřed zamrzne. Praktické rozdělení: kořen aplikace a přechodová vrstva běží vždy, svět je pauzovatelný, vrstva pauzy musí běžet **během** pauzy.

Kde se s tím potkáš: [Vlastnictví napřed, složky potom](godot/projekt-a-vykon.md#vlastnictvi-napred-slozky-potom-main-game-jako-koordinator)

### Producent

**V herním týmu project manager: zná timeline, drží seznam úkolů a ví, kdo co dělá a kdo je volný.**

Titul „producent" znamená v každém médiu něco jiného — ve hrách je to tahle role (občas s přesahem do kreativních rozhodnutí). Kdo vede kanban board na jamech s kamarády, dělá produkci doopravdy: je to reálná praxe pro industry roli.

Kde se s tím potkáš: [Plánovací nástroje](teorie/planovani-nastroje.md)

### Profiling

**Měření toho, kde se ve snímku ztrácí čas — na rozdíl od hádání, které v enginu skoro nikdy nevyjde.**

První krok je vždy stejný: zjistit, **který rozpočet je vyčerpaný** (`stat unit` ukáže frame, game, draw, GPU — to, které se blíží k frame, je brzda), a teprve podle toho volit nástroj. Vizuální debug režimy k bottlenecku nevedou; dají se optimalizovat celý den bez dopadu na snímkování. Druhá polovina disciplíny je porovnatelnost: reprodukovatelný měřicí bod, umlčené proměnné a jediná změna mezi dvěma záznamy.

Kde se s tím potkáš: [Profiling: měření místo odhadů](praxe/profiling.md) · [Rejstřík: Unreal Insights](#unreal-insights) · [Rejstřík: Frame time](#frame-time)

### Prokletí znalosti

**Expert na vlastní hru si neumí dát zážitek nováčka — ví příliš mnoho, než aby viděl tření.**

Dvě podoby: u tutorialu se svou hru nedokážeš odnaučit (proto onboarding testují cizí oči), u launche zase hraješ „správně", takže nevidíš exploity, které hardcore hráči najdou za večer. Playtest je jediný pohled na hru bez tohohle prokletí.

Kde se s tím potkáš: [Playtesting](teorie/playtesting.md) · [První dojem](teorie/prvni-dojem.md)

### Průběžná obtížnost

**Jak moc tě hra aktivně tlačí k prohře — kolik odporu klade cestou k cíli.**

Protipól aspirační obtížnosti. Bullet hell má průběžnou obtížnost vysokou, cozy sim skoro žádnou (grind není totéž co odpor); upgrade zdraví v roguelite ji snižuje. Vyrábí stres a úlevu — a spolu s estetikou říká hráči dopředu, jaké pocity čekat.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Předznamenání

**Dvojice čísel na začátku skladby, která říká, kolik dob je v taktu a jaká nota je jedna doba.**

Horní číslo je počet, spodní hodnota noty. 4/4 jsou čtyři čtvrťové (proto se počítá „1 2 3 4"), 3/4 tři (valčík), a 6/8 počítá osminy — šest jich v taktu dá **triolový pocit** místo čtyřdobého. Anglicky *time signature*. Pro herní hudbu drobná výhrada: triolová předznamenání znějí svěže ve smyčce na deset vteřin, ale při hodině hraní unavují rychleji než čtyřdobý takt.

Kde se s tím potkáš: [Mřížka: takt, dělení a swing](hudba/rytmus.md#mrizka-takt-deleni-a-swing) · [Rejstřík: BPM](#bpm) · [Rejstřík: Swing](#swing)

### Půltón

**Nejmenší vzdálenost mezi dvěma sousedními tóny (E–F, C–C#).**

Se svým dvojčetem (celý tón) je stavební jednotkou stupnic i akordů. Sám o sobě není „čistý" interval; zblízka ve stejné oktávě pere výrazně víc než rozhozený po oktávách.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### PSO

**Pipeline state object — předpřipravený stav grafického potrubí; když chybí, kompiluje se shader za běhu a hra sekne.**

Zásky z kompilace shaderů obstarává **procesor**, ne grafika, takže je rychlá grafická karta nespraví. Konzole je nemají tak zlé, protože hardware je ve všech kusech stejný a dá se zkompilovat jednou a rozdat předpřipravené; na PC to nelze. Řešení jsou dvě a nevylučují se: **bundlovat** PSO a **předcache**. Při testování je potřeba **mazat cache**, jinak lokálně neuvidíš, že s tím je problém.

Kde se s tím potkáš: [Jak to vidí hráč](praxe/frame-pacing.md#jak-to-vidi-hrac-360p-upscaling-a-stutter) · [Prvních 16,66 ms se rozdává v CL1](praxe/rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Technické zdraví projektu: příčiny hitchů](praxe/organizace-projektu.md#technicke-zdravi-projektu-kontroly-od-prvniho-dne-po-vydani) · [Mortal Shell 2: předkompilace](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek)

### Pure function

**Funkce bez exec pinů, která jen vrací hodnotu a nemění stav — v grafu se spočítá, kdykoli je její výstup potřeba.**

Hodí se na převody a výpočty: místo zásahu → směr, jméno physical materialu → končetina. Protože se vyhodnocuje při každém čtení výstupu, nemá dělat nic drahého ani nic měnit; náročný výsledek je lepší uložit do proměnné.

Kde se s tím potkáš: [Terč: směr rány](praxe/souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave) · [Zdraví po končetinách](praxe/souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav)

### Quad

**Čtyřúhelníková buňka mřížky meshe — u terénu základní jednotka rozlišení.**

Rozlišení Mesh Terrainu se zadává počtem quadů v osách XY; víc quadů = jemnější síť = víc detailu i dat. Interně se quady stejně dělí na trojúhelníky (GPU nic jiného nekreslí), ale pro autorskou práci je čtyřúhelníková mřížka přehlednější — proto s ní pracují terény, subdivision modeling i retopologie.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Quad utilization

**Podíl skutečně použité práce v základní jednotce GPU — čtverci 2×2 pixely.**

Pixel shader se neplánuje po jednotlivých pixelech, ale po čtvercích 2×2 (tolik informace stačí na gradienty textur pro mip mapping a je to jednoduché na hardwaru). Trojúhelník menší než ten čtverec se **spočítá celý a 75 % výsledku se zahodí**; totéž v menší míře platí pro každý quad na hranici trojúhelníku, a s tím se nedá nic dělat. Co ovlivnit lze, je jaké trojúhelníky GPU dostane — proto fungují LODy a [impostory](#impostor), proto má stejný mesh při jiné triangulaci jiný výkon (dlouhé tenké trojúhelníky jsou nejhorší) a proto si Epic napsal pro mikrotrojúhelníky vlastní softwarový rasterizér v Nanitu. Druhý strop vedle toho: **primitive assembly zvládne jeden primitiv za takt**.

Kde se s tím potkáš: [Proč malé trojúhelníky ničí GPU](praxe/rozpocet-snimku.md#proc-male-trojuhelniky-nici-gpu) · [Rejstřík: Quad](#quad) · [Rejstřík: Overdraw](#overdraw)

### Race condition

**Chyba závislá na pořadí: dva kusy kódu se inicializují souběžně a jeden čte data, která druhý ještě nenastavil.**

V UE klasicky mezi BeginPlay různých actorů — klíč se ptá dveří na ID dřív, než si ho dveře vygenerovaly. Pořadí inicializace není zaručené; nespoléhej na něj. Lék: event dispatcher („KeyAssigned") — místo čtení hned se posluchač binduje a data si nechá oznámit, až existují.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md)

### Ragdoll

**Postava, jejíž kostra přestane hrát animaci a začne simulovat jako soustava fyzikálních těles spojených klouby.**

Tvar a limity dává physics asset; bez dalšího ovládání padá jako hadrová panenka. Active ragdoll přidá motory kloubů, které tělo táhnou k póze (Physical Animation Component, Physics Control). V GASP 5.8 ragdollu podsouvá pózy AnimBP (rozhazování, natažené ruce, schoulení) a sílu kloubů řídí křivky. Návrat zpět chce pose snapshot a výběr vstávací animace.

Kde se s tím potkáš: [Ragdoll za minutu](praxe/ragdoll.md#ragdoll-za-minutu-preset-simulace-kamera) · [Active ragdoll](praxe/ragdoll.md#active-ragdoll-motory-rizene-rychlosti) · [Ragdoll, který se chrání](praxe/ragdoll.md#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu) · [Terč: smrt jako ragdoll](praxe/souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave)

### Random pitch variation

**Náhodný posun výšky zvuku při každém přehrání; zabíjí mechanickou repetici.**

Zvuk sebrání předmětu ve Stardew Valley je mlasknutí pusou — s náhodným pitchem přestane znít digitálně a otravně. Často je způsob implementace důležitější než samotný zvuk.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md) · [Pět potvrzení rány: Modulator](praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem)

### Raster bin

**Nanitová dávka geometrie se shodným stavem rasterizace; cílem je mít ve scéně co nejméně různých binů.**

Sourozenec [shading binu](#shading-bin) a stejná logika: cenu určuje **rozmanitost, ne množství**. Dvě stě kamenů z jednoho materiálu je levnějších než dvacet kamenů z dvaceti materiálů. Vizualizace *Nanite → raster bin* obarví assety podle binu — chceš vidět většinu scény v jedné barvě. Nejčastější příčina roztříštěnosti: scéna složená z několika stažených sad, kde má každá vlastní materiály. Náprava: společný materiál, textury do UDIMů a variace přes per-instance data.

Kde se s tím potkáš: [View modes](praxe/rozpocet-snimku.md#view-modes-kde-se-ztraci-nez-otevres-profiler) · [Rejstřík: Shading bin](#shading-bin) · [Rejstřík: Draw call](#draw-call)

### Ray tracing

**Výpočet světla sledováním paprsků scénou, místo aby se odhadovalo jen z rastrovaného obrazu.**

V Unrealu existuje ve dvou podobách. Hardwarový ray tracing běží na RT jádrech grafické karty proti skutečné geometrii. Softwarový trasuje proti zjednodušené reprezentaci, třeba distance fields, a běží i bez RT hardwaru. Lumen umí obojí. MegaLights na ray tracingu stojí, ale hardwarový nevyžadují. Výsledky z malého počtu paprsků čistí [denoiser](#denoiser).

Kde se s tím potkáš: [Rozpočet vzorků na pixel](praxe/megalights.md#rozpocet-vzorku-na-pixel-co-megalights-meni-a-co-za-to-platis) · [Slunce bez MegaLights](praxe/megalights.md#slunce-bez-megalights-silne-svetlo-spolkne-rozpocet) · [007 First Light: GI bez hardwarového RT](praxe/env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka) · [Rejstřík: Lumen](#lumen)

### Recall priming

**Level design technika: rozmístit do prostředí nenápadné nápovědy, které hráči zpřístupní správnou vzpomínku těsně před tím, než ji bude potřebovat.**

Hráči se u puzzlů nezasekávají hloupostí, ale nedostupností správného nástroje v paměti. Priming ji zvedá prostředím: tmavá chodba donutí vytáhnout pochodeň, hořlavé liány cestou připomenou, že oheň pálí vegetaci — a u puzzle s liánami řešení „samo" naskočí. Hráč se necítí veden, cítí se chytrý; UI nápověda by mu ten pocit ukradla.

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md)

### Recoup

**Splacení vydavatelovy investice z tržeb, než se vývojáři začne vyplácet jeho podíl.**

Do okamžiku recoupu obvykle plyne vydavateli 80 až 90 procent tržeb; teprve pak se poměr překlopí ve prospěch studia. Proto se na vydavatelskou smlouvu vyplatí dívat jako na půjčku splácenou z budoucích prodejů, ne jako na grant — a proto je klíčové, co všechno se do splácené částky započítá (marketing, lokalizace, portace).

Kde se s tím potkáš: [Financování](teorie/financovani.md#vydavatel-je-banka-ne-darce)

### Rect light

**Obdélníkové plošné světlo, které svítí z plochy jedním směrem, jako panel, okno nebo softbox.**

Intenzita se rozkládá do plochy, takže užší světlo se stejnou hodnotou svítí jasněji. Klapky (barn doors) zužují úhel, výchozí je 88°, a dají přirozený přechod světla, které padá dovnitř oknem. Bez MegaLights je to nejdražší typ světla. S MegaLights stojí skoro stejně jako bodové světlo se source radiem.

Kde se s tím potkáš: [Svítidlo z víc světel](praxe/megalights.md#svitidlo-z-vic-svetel-odraz-mlha-a-stin-se-ladi-zvlast) · [Rejstřík: Source radius](#source-radius)

### Reflection system

**Systém Unrealu, díky kterému engine za běhu zná typy, properties a funkce označené makry UCLASS, USTRUCT, UPROPERTY a UFUNCTION.**

Stojí na něm editor, blueprinty, serializace i Python. Ve verzi 5.8 z něj MCP automaticky vyrábí JSON pro agenty, takže nový nástroj pro agenta je obyčejná UFunction s tooltipem.

Kde se s tím potkáš: [Vlastní tool set a skill](praxe/mcp-v-editoru.md#vlastni-tool-set-a-skill-api-pro-juniora-a-rada-kolegovi) · [Rejstřík: JSON Schema](#json-schema)

### Refundace

**Vrácení peněz za koupenou hru — na Steamu automatické do dvou hodin hraní a dvou týdnů od nákupu.**

Z pohledu vývojáře je to první srážka z hrubé tržby, po níž následuje podíl obchodu, bankovní poplatky a daně. Praktický důsledek: číslo na dashboardu není příjem — v rozpadu jednoho indie studia zbyla z hrubé tržby po všech srážkách zhruba polovina, a to ještě před zdaněním.

Kde se s tím potkáš: [Vydání hry: co ti reálně zbyde](teorie/vydani-hry.md)

### Redirector

**Ghost soubor, který po přesunu assetu zůstává na starém místě a přesměrovává reference na nové.**

Důvod, proč „prázdné" složky nejdou smazat — a proč force delete rozbije projekt (reference vedou do prázdna). Správně: pravý klik → Update Redirector References (odkazy se přepíšou natrvalo), pak Delete Unreferenced Redirectors, pak teprve mazat složku. Stěhuj po jedné složce — hromadné přesuny editor shazují.

Kde se s tím potkáš: [Organizace projektu](praxe/organizace-projektu.md)

### Referenční transparentnost

**Funkci lze nahradit její návratovou hodnotou, aniž se program změní — žádné skryté závislosti, žádný sdílený stav.**

Odměna: triviální testování, paralelizace i cachování. Užitečnější jako čočka na design než jako akademický pojem: když se něco blbě testuje, neptej se po mock knihovně — ptej se, proč ta funkce není referenčně transparentní. V UE: pure funkce bez side-effectů.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Rekurze

**Funkce, která volá sama sebe — s base case proti nekonečnu a zmenšováním problému směrem k němu.**

Tři principy: volá sebe; má base case (nejmenší problém s přímou odpovědí); každé volání problém zmenšuje. Zbytek je „recursive leap of faith" — důvěra, že menší práci funkce odvede. Přirozená pro stromy: složky, dialogy, scene graph, behavior tree.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)

### Relativní dur

**Durová tónina sdílející tytéž tóny s danou mollovou (a naopak).**

C dur a A moll mají stejné tóny, liší se domovským tónem. Trik na radost v moll: třetí akord mollové stupnice je tónika relativní durové — kdykoli po něm sáhneš, vlije se do skladby světlo.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md) · [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Remesh

**Přestavba sítě trojúhelníků na novou, rovnoměrnější topologii podle cílové délky hrany.**

Opravuje topologii po booleanech, zahušťuje řídký mesh před deformací a umí i vyhlazovat. V procedurálních nástrojích se často používá dvakrát: nejdřív hrubě, aby následný výpočet běžel rychle, pak jemně, aby se vrátil detail. V Mesh Terrainu je remesh samostatný modifikátor, který jde omezit kanálem.

Kde se s tím potkáš: [Blok napřed, silnice potom](praxe/pcg-mesta.md#blok-napred-silnice-potom-block-processor-a-booleany) · [Modifikátory v rukou Epicu](praxe/mesh-terrain.md#modifikatory-v-rukou-epicu-poradi-vrstev-rovina-pod-poi-a-pcg-ktere-rozmistuje-skaly) · [Modifier stack](praxe/mesh-terrain.md#modifier-stack-nedestruktivni-tvarovani)

### Render target

**Textura, do které engine vykresluje za běhu — použitelná jako vstup i jako výstup.**

Slouží k obrazovkám kamer, zrcadlům nebo malování do textury za běhu. Šikovné vedlejší použití: materiál složený z noise uzlů se dá do render targetu vypéct a uložit jako obyčejnou texturu — takže na generování šumu nepotřebuješ žádný externí program.

Kde se s tím potkáš: [Materiály: VFX textury](praxe/materialy.md#vfx-textury-nedelat-je-a-kdyz-uz-tak-v-krite) · [Cube render target pro falešné okno](praxe/materialy.md#falesne-okno-interior-cubemap-a-mistnost-nafocena-v-enginu) · [Stopy do hloubky](praxe/footsteps.md#stopy-do-hloubky-render-target-jako-platno-pod-postavou)

### Renderovací vlákno

**Čas, který procesor stráví přípravou práce pro GPU — ne čas GPU.**

V `stat unit` je to hodnota **draw** a je to nejčastěji špatně čtené číslo v celém panelu. Odehrává se tam **culling** (příkazy pro deset tisíc objektů se musí připravit, i když jich uvidíš zlomek), **výběr LODů** podle vzdálenosti a **sestavení a odeslání draw callů**. Praktický důsledek: LODy a culling nešetří jen GPU, ale i procesor — takže „mám málo trojúhelníků, LODy nepotřebuju" přestává platit, jakmile je objektů hodně.

Kde se s tím potkáš: [Co je v herním vlákně a co v renderovacím](praxe/profiling.md#co-je-v-hernim-vlakne-a-co-v-renderovacim) · [Rejstřík: Herní vlákno](#herni-vlakno) · [Rejstřík: Draw call](#draw-call) · [Rejstřík: RHI](#rhi)

### Resimulation

**Síťová korekce fyziky: návrat do minulého snímku, oprava podle serveru a přehrání simulace až do současnosti.**

Stojí na pevném kroku a číslech snímků (posun mezi klientem a serverem). Drží vlastní postavu a to, s čím hráč interaguje, ve stejné časové ose se serverem; vstupy ostatních se během přehrání predikují a tlumí (viz [input decay](#input-decay)). Logika, která ovlivňuje fyziku, musí běžet na fyzikálním vlákně, aby se při resimulaci přehrála taky.

Kde se s tím potkáš: [Síťová fyzika zevnitř](praxe/mover.md#sitova-fyzika-zevnitr-snimky-misto-casu-resimulace-a-input-decay) · [Rozbití v multiplayeru](praxe/destrukce-a-latky.md#rozbiti-v-multiplayeru-predictive-interpolation-misto-predikce)

### Retargeting

**Přenos animace z jedné kostry na jinou, která má odlišné proporce.**

Bez něj by každá postava potřebovala vlastní sadu animací. V UE se řeší IK Rigem a IK Retargeterem: řekneš, které kosti si odpovídají, a engine dopočítá zbytek. Právě proto je u AI generovaných animací důležité, na jaké standardní kostře model exportuje — mapování na běžný skeleton je rozdíl mezi „použitelné" a „k ničemu".

Kde se s tím potkáš: [AI assety: animace v reálném čase](praxe/ai-assety.md#animace-generovana-v-realnem-case-kam-se-posunulo-ardy) · [MetaHuman v praxi](praxe/metahuman.md#hratelny-metahuman-retarget-jednim-klikem-a-virtual-bones) · [Export markerless animace](praxe/animace-nastroje.md#markerless-mocap-v-58-z-videa-na-animaci-bez-obleku) · [Kimodo na Mixamo a dál](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu)

### Retopologie

**Přestavba geometrie na čistší síť: z milionů neuspořádaných trojúhelníků (sculpt, sken, AI generát) použitelný mesh pro rig a animaci.**

AI pipeline ji řeší třemi cestami: decimace + normal bake (rychlá, „topologie pro start"), smart low poly režimy generátorů (pečou normal mapu z HD verze), nebo nástroje jako Quad Remesher. Na čem záleží: deformující se části (klouby, obličej) chtějí pořádnou topologii, rekvizity snesou decimát.

Kde se s tím potkáš: [AI assety](praxe/ai-assety.md) · [AI agenti](praxe/claude-code-ue.md)

### Retrieval practice

**Učení vybavováním: odvrať zrak a zkus si vzpomenout — poráží opakované čtení, i když se hůř „cítí".**

Opakované čtení buduje známost, ne vlastnictví; vybavování nutí mozek znalost rekonstruovat, a tím ji ukládá. Prakticky: po kapitole ji převyprávěj vlastními slovy, uč druhé (klidně zeď), dej si kvíz. Věda za kvízovým protokolem.

Kde se s tím potkáš: [Učení v éře AI](teorie/uceni-v-ere-ai.md) · [Zápisek: Kvízový protokol](zapisky/kvizovy-protokol.md)

### Retriggerable Delay

**Delay, který se každým dalším spuštěním restartuje od nuly — doběhne až po klidu na vstupu.**

Ideální „ztráta zájmu" AI: dokud percepce cíl hlásí (a event se opakuje), odpočet se resetuje; jakmile hlásit přestane, delay doběhne a vrátí AI k patrole. Délka musí být větší než interval, kterým se vstup opakuje (u Pawn Sensingu > 0,5 s), jinak doběhne i mezi dvěma hlášeními.

Kde se s tím potkáš: [AI vnímání](praxe/ai-vnimani.md) · [Základy AI](praxe/ai-zaklady.md)

### Reverb

**Odraz zvuku od prostředí; dozvuk.**

Slouží dvěma věcem: slepit zvuky dohromady, nebo vyjádřit prostor (chodba, koupelna, kaňon). Přidává realističnost a hloubku — bez něj zní zvuk synteticky.

Kde se s tím potkáš: [Sound design ve hře](hudba/sound-design-ve-hre.md)

### Rewind Debugger

**Nahraje běh hry a nechá tě scrollovat časem: co hrálo, proč to Motion Matching vybral, jak rozhodoval State Tree.**

`Debug → Rewind Debugger`, zapni auto-record (+ auto-eject). Dvojklik na track otevře asset na správném framu; šipkami jdeš frame po framu; eject kamery přehraje pohyb ve světě. Pose search debugger uvnitř ukazuje kandidáty, ceny a channels breakdown; od 5.7 má vlastní track i State Tree — vidíš přesný frame, kdy padlo rozhodnutí.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [GASP](praxe/gasp.md) · [Look-at v GASP 5.8](praxe/gasp.md#look-at-jako-aditivni-solver-pohled-bez-ztraty-animace)

### Rider

**IDE od JetBrains pro herní vývoj s hlubokou podporou Unrealu: indexy blueprintů a assetů a debugger.**

V éře agentů půjčuje svoje indexy, debugger a kontroly kódu i agentům. Přednáška JetBrains ukazuje, že hledání potomků třídy s indexem trvá zlomek času a najde víc než hledání podle jmen souborů.

Kde se s tím potkáš: [Agent v IDE](praxe/mcp-v-editoru.md#agent-v-ide-index-a-debugger-misto-hledani-v-textu) · [Rejstřík: ACP](#acp)

### RigLogic

**Knihovna, která za běhu vyhodnocuje rig MetaHumana podle jeho [DNA](#dna-soubor) — od roku 2026 open source pod licencí MIT.**

Spolu s DNA tvoří MetaHuman DevKit, který Epic uvolnil, aby šli MetaHumani načíst a animovat stejnou logikou rigu i mimo Unreal — součást snahy udělat z MetaHumana standard digitálních postav.

Kde se s tím potkáš: [MetaHuman jako standard](praxe/metahuman.md#metahuman-jako-standard-auto-rigging-cizich-postav-davy-a-otevreny-rig)

### RITE

**Rapid Iterative Testing and Evaluation: jeden tester → oprav vážné problémy → další tester.**

Metoda z UX designu pro vývojáře bez velkého poolu testerů: sleduj jednoho hráče, zapisuj vše pozoruhodné, komunikuj minimálně; po sezení oprav každý vážný problém a opakuj s novým člověkem, který by na staré problémy už neměl narazit. Cíl není hra snadná na hraní, ale snadná na chtění hrát.

Kde se s tím potkáš: [Playtesting: kadence a RITE](teorie/playtesting.md)

### RHI

**Render Hardware Interface — vrstva enginu mezi rendererem a grafickým API dané platformy.**

Implementuje se jedna na platformu (D3D12, Vulkan, Metal…) a překládá zaznamenané příkazy do skutečných GPU command listů. Pro ladění výkonu jsou zajímavé dvě věci: **paralelní překlad** se ladí přes `r.RHICommand.ParallelTranslate.MaxCommandsPerTranslate` (na víc jádrech jít do šířky, na omezeném stroji naopak), a **použití immediate command listu vynutí jednovláknový překlad**, tedy bublinu v potrubí — v RDG průchodech proto ber základní typ, ne immediate.

Kde se s tím potkáš: [Busy, wait, idle](praxe/gpu-pamet.md#busy-wait-idle-co-rika-novy-gpu-profiler) · [Potrubí snímku](praxe/frame-pacing.md#snimek-neni-fronta-je-to-potrubi)

### Rigging

**Vložení kostry do modelu a nastavení, jak kosti ovládají mesh — bez toho zůstane model socha.**

Následuje weight painting (malování vlivu jednotlivých kostí, aby deformace vypadala přirozeně) a stavba ovladačů, které animátorovi umožní hýbat kostrou jednoduše — jako provázky loutky. Na téhle vrstvě se řeší i to, aby chodidlo drželo na zemi, když se hýbe zbytek těla. Typická práce technického artisty.

Kde se s tím potkáš: [Art specializace: tech art](teorie/art-specializace.md) · [Animace v UE](praxe/animace-nastroje.md) · [Rig, který se přenese](praxe/animace-nastroje.md#rig-ktery-se-prenese-controly-na-kuzi-moduly-a-tvary-bez-navratu-k-riggerovi)

### Roguelike

**Žánr postavený na opakovaných bězích: smrt je součást smyčky, svět se generuje procedurálně, znalost hráče je hlavní trvalý pokrok.**

Pro design je podstatný důsledek mnoha běhů: hráč potkává stejné systémy znovu a znovu, což násobí šanci na náhodné objevení skrytých pravidel — proto žánru tak sedí tajné řetězce (Spelunky). Odnož s trvalým meta-postupem mezi běhy se označuje roguelite.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Roughness

**Drsnost povrchu v PBR: 0 = zrcadlo, 1 = zcela matný — a v UE5 zároveň prahová hodnota pro cenu odrazů.**

Výkonový háček, který se snadno přehlédne: Lumen trasuje **dedikované odrazové paprsky** pro pixely pod prahem `r.Lumen.Reflections.MaxRoughnessToTrace` (výchozí 0,4). Hodně projektů má většinu materiálů kolem 0,35, takže valná část obrazovky trasuje odrazy, aniž by to někdo chtěl. Zvlášť zákeřné je to u listí (vlastní proměnná `…ForFoliage`, klidně 0) a u shaderů počasí, které za deště srazí roughness všemu.

Kde se s tím potkáš: [Lumen: rozpočet a binární hledání](praxe/gpu-pruchod.md#lumen-rozpocet-a-binarni-hledani) · [Rejstřík: PBR](#pbr) · [Rejstřík: Lumen](#lumen)

### Root motion

**Pohyb uložený v animaci samotné (v root kosti) — postava se hýbe tak, jak animátor animoval, kapsle následuje.**

Protiklad capsule driven přístupu (vstup hýbe kapslí, animace se lepí). Motion Matching root motion data vyžaduje — z nich čte trajektorie klipů; hromadně se zapíná přes Property Matrix (Enable Root Motion + Force Root Lock, u smyček Looping). GASP je capsule driven, ale animace root motion mají — budoucnost je blending obou přístupů po částech animace.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md) · [Dojít na místo](praxe/interakcni-animace.md#dojit-na-misto-motion-warping-potrebuje-krok-ktery-je-v-animaci-schvalne) · [Contextual Animation: movement mode Flying](praxe/interakcni-animace.md#contextual-animation-scena-s-rolemi-misto-rucni-choreografie)

### Rovnoměrně temperované ladění

**Ladění, které dělí oktávu na dvanáct stejně velkých kroků (equal temperament).**

Nejčistší intervaly (z alikvót) jen přibližuje, ne přesně trefuje — velká tercie tak reálně sedí lehce na vrcholu disonance. Kompromis, který umožňuje hrát ve všech tóninách bez přelaďování.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### Rubber banding

**Umělá podpora hráče, který je pozadu, a brzda hráče napřed — v multiplayeru se říká catch-up mechanika.**

Nejde o podvod na hráče, ale o opravu učebního prostředí: kdo je beznadějně pozadu, dostává od hry konstantní „špatně" a nemá se z čeho učit; kdo je nedostižně napřed, dostává konstantní „dobře". Rubber banding oba vrací do pásma, kde akce zase mají čitelné následky. Příbuzné nástroje: hinty, skipy, měkké stavy úspěchu (skóre místo výhra/prohra).

V AI nepřátel (Lords of the Fallen) se stejným slovem říká i vodítku: nepřítel se nenechá odlákat daleko od svého území a pomalu se vrací, ať hráč přijde za ním.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md) · [Reakce vedle stromu](praxe/ai-ve-velkem.md#reakce-vedle-stromu-co-se-muze-stat-v-kazdem-stavu-nepatri-do-zadne-vetve)

### Rubber duck debugging

**Vysvětli problém nahlas — klidně gumové kachně — a řešení se často objeví v půlce vysvětlování.**

Formulace nutí seřadit fakta a předpoklady, a přesně v tom seřazení bývá chyba vidět. Funguje s kachnou, kamarádem i AI; s člověkem má bonus druhé perspektivy („z ptačí vidím díru v úvaze").

Kde se s tím potkáš: [Programátorské návyky](teorie/programatorske-navyky.md) · [Ladění](praxe/debugging.md#ctyri-otazky-ctyri-nastroje-od-print-stringu-po-visual-logger)

### Runtime generation

**PCG generování za běhu: obsah vzniká jen v buňkách kolem hráče a s jeho pohybem se načítá a uvolňuje.**

Vyžaduje Generate at Runtime a zároveň Is Partitioned, jinak se generuje celý objem najednou. Velikost buněk (grid size) a vzdálenost generování jsou kompromis. Méně velkých buněk je levnějších, menší buňky dají kulatější oblast kolem hráče, ale když jich je moc, výpočet zpomalí. Hodí se na hustý pokryv země, který by přes celý svět nešel.

Kde se s tím potkáš: [Les pro otevřený svět](praxe/pcg-vegetace.md#les-pro-otevreny-svet-co-se-nacte-s-levelem-a-co-roste-kolem-hrace) · [Foliage optimalizace II](praxe/optimalizace.md#foliage-optimalizace-ii-gpu-scatter-a-runtime-kvalita) · [Rejstřík: PCG](#pcg)

### Runtime Virtual Texture

**Virtuální textura, kterou engine za běhu vykresluje ze scény, typicky shora z terénu, a jiné materiály z ní čtou.**

Obvykle nese barvu nebo výšku terénu. Objekty se pak do terénu prolnou a Virtual Heightfield Mesh podle ní ví, kde terén leží. Podle Epicu přesouvá cenu mnoha textur z renderu do načítání. Na terénu z height mapy stačí ortografická projekce shora, Mesh Terrain potřebuje obecnou 3D projekci, která do 5.8 nedorazila.

Kde se s tím potkáš: [Proč trojúhelníky a ne voxely](praxe/mesh-terrain.md#proc-trojuhelniky-a-ne-voxely-mesh-partition-od-zdroje-po-runtime) · [Stopy do hloubky](praxe/footsteps.md#stopy-do-hloubky-render-target-jako-platno-pod-postavou) · [Rejstřík: Virtual texture](#virtual-texture)

### Runway

**Kolik měsíců dokážeš pracovat, než dojdou peníze — ne kolik peněz máš.**

Runway se dá prodloužit z obou stran: naspořením hotovosti i snížením výdajů. Typický vzorec u přeživších indie studií je období cíleného šetření před skokem na plný úvazek. Jedno tříčlenné studio si takto koupilo rok a půl jistoty a skromným životem ji natáhlo na dva roky. Protějšek [burn rate](#burn-rate).

Kde se s tím potkáš: [Přežít jako studio](teorie/prezit-jako-studio.md#ctyri-roky-bez-hitu-financovani-riziko-a-runway) · [Financování](teorie/financovani.md#co-si-udrzi-kontrolu-uspory-prijmy-z-backlogu-a-komunita)

### Sampling

**Použití kusu existující nahrávky jako stavebního materiálu nové skladby.**

Základ hip hopu (vintage soul samply) i moderního hood trapu (remix nečekané písně). Nahrávku izoluješ, nasekáš, přeskládáš, zrychlíš nebo přeladíš. Pozor na práva k původní nahrávce.

Kde se s tím potkáš: [Žánry a jejich melodie](hudba/zanry-a-styl.md)

### SaveGame objekt

**Blueprint třída typu SaveGame: nese proměnné k uložení a přes pojmenovaný slot se zapisuje na disk.**

Tři uzly stačí: Create Save Game Object / Load Game From Slot / Save Game to Slot (+ Delete Game in Slot). Architektura okolo: referenci drží Game Instance (přežije přechody levelů), přístup odkudkoli dává function library. Load není magie — hodnoty se musí ručně aplikovat zpět (rychlost do movementu, transform na actora). Myslet dopředu: verze formátu a více slotů.

Kde se s tím potkáš: [Ukládání](praxe/ukladani.md)

### Scalability groups

**Skupiny nastavení kvality renderování (Low → Epic); pozor na to, že *Epic* je režim pro 30 snímků, ne „nejlepší".**

Míříš-li na 60 FPS, je tvůj referenční režim **High** — a dokud ho nenastavíš, díváš se v editoru na jinou hru, než jakou chceš dodat. Za celý tým se to dá udělat jen jednou: v `DefaultEditorSettings.ini` sekcí se skupinami na `2`, dokud projekt nikdo neotevřel. Uživatelské změny se ukládají zvlášť (`Engine/Saved/Config`), takže se dá kdykoli resetovat. Do hry samotné to nasazují [device profily](#device-profile).

Kde se s tím potkáš: [Prvních 16,66 ms se rozdává v CL1](praxe/rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Co říká GPU profiler](praxe/profiling.md#co-rika-gpu-profiler-a-co-v-nem-nenajdes)

### SCAMPER

**Sedm pák na nápad: Substitute, Combine, Adapt, Magnify, Purpose, Eliminate, Rearrange.**

Formální ideační technika — funguje na vylepšení rozdělané hry i generování nové z oblíbené. Nejužitečnější páky pro gamedev: Magnify (zazoomuj na nejzábavnější prvek a udělej z něj celou hru) a Eliminate (generátor „hra bez X": Skyrim bez magie, Fortnite bez stavění).

Kde se s tím potkáš: [Nápad: ideace jako řemeslo](teorie/napad.md)

### Scene Capture

**Aktér, který snímá scénu kamerou do render targetu.**

Scene Capture 2D dělá obyčejný obraz, třeba pro monitor ve hře, zrcadlo nebo minimapu. Scene Capture Cube snímá na všechny strany do cube render targetu, který jde jednorázově uložit jako statickou cube texturu (Create Static Texture), například pro falešný interiér za oknem. Živé snímání stojí výkon jako další vykreslení scény.

Kde se s tím potkáš: [Falešné okno](praxe/materialy.md#falesne-okno-interior-cubemap-a-mistnost-nafocena-v-enginu) · [Rejstřík: Render target](#render-target) · [Rejstřík: Cubemap](#cubemap)

### Scene Component

**Komponenta, která má jen transformaci (polohu, rotaci, měřítko) a může nést děti — bez geometrie a bez logiky.**

Slouží jako pivot (pant dveří), jako značka místa (kam se postava postaví, kam sáhne ruka, warp target) nebo jako základ vlastní třídy: grip point odvozený od Scene Component najde `Get Components by Class` a odliší ho od ostatních bodů. Reference na scene komponenty nejde zadat do výchozích hodnot proměnných; plní se v [construction scriptu](#construction-script).

Kde se s tím potkáš: [Jedna animace zvednutí](praxe/interakcni-animace.md#jedna-animace-zvednuti-pro-vsechno-grip-pointy-a-pozy-ruky) · [Objekt ví, jak se s ním zachází](praxe/interakcni-animace.md#objekt-vi-jak-se-s-nim-zachazi-data-interakce-patri-k-veci-ne-k-postave) · [Úkryt ve skříni](praxe/interakce-predmety.md#ukryt-ve-skrini-markery-lerpy-a-synchronizace-s-animaci)

### Screen percentage

**V jakém rozlišení se scéna doopravdy renderuje, než ji upscaler dotáhne na výstupní.**

Zákeřné je výchozí nastavení: UE5 má screen percentage **„based on display resolution"**, takže na vyšších rozlišeních tiše renderuje **pod 100 %**. Kdo o tom neví, srovnává dvě měření v různém rozlišení a netuší, že měří něco jiného. Přepíná se na **manual** na dvou místech nastavení projektu (hra a editor). Souvisí s tím **temporal upscaling**: se zapnutým vypadá 80 % skoro jako 100, s vypnutým je i 80 % rozmazané.

Kde se s tím potkáš: [Rozpad ceny výchozí scény](praxe/lehky-render.md#rozpad-ceny-vychozi-sceny-a-cim-ji-nahradit) · [Rejstřík: Dynamic resolution](#dynamic-resolution) · [Rejstřík: TSR](#tsr)

### Scene inheritance

**Nová scéna odvozená z existující: převezme celý strom nodů a dovolí přepsat jen to, co se liší.**

Odpověď na duplikování scén. Máš-li základního nepřítele a chceš rychlou, silnou a bossovskou variantu, duplikát znamená, že každou opravu budeš dělat čtyřikrát. Dědičná scéna sdílí základ a přepisuje jen odchylky (rychlost 200 → 400), takže vylepšení základu se propíše do všech potomků. **Nemá to nic společného s dědičností tříd** — dědí se strom nodů, ne skript.

Kde se s tím potkáš: [Editor se prohledává, ne prochází](godot/zaklady.md#editor-se-prohledava-ne-prochazi)

### Scene tree

**Strom nodů a vnořených scén, ze kterého se skládá běžící hra; jeho kořen se jmenuje root.**

Není to jen organizační pomůcka — nese tři věci naráz: **transformace** se dědí po hierarchii (kamera jako dítě hráče ho následuje bez kódu), **pořadí vykreslení** uzlů se stejným [Z indexem](#z-index) odpovídá pořadí ve stromu, a **komunikace** se řídí podle hierarchie (viz [call down, signal up](#call-down-signal-up)). Proto platí rada „nestav hluboké hierarchie": strom scény je architektura, ne složka na soubory.

Kde se s tím potkáš: [Nody, scény a strom](godot/zaklady.md#nody-a-sceny-strom-ktery-je-zaroven-architekturou) · [Praxe v Godotu](godot/index.md)

### Scope

**Rozsah projektu: kolik obsahu, systémů a ambicí hra obsáhne.**

Hlavní páka proveditelnosti — a nejčastější příčina nedokončených her. Pro začátečníka platí, že malý scope není kompromis, ale strategie: krátká smyčka dokončení → zpětná vazba → další projekt o úroveň výš. Malá hra přitom není zmenšená velká hra, ale jedna vyjmutá mechanika, které všechno slouží. „Scope creep" je plíživé bobtnání rozsahu během vývoje; game jam je institucionalizovaná obrana.

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Scope: malé hry a design by constraint](teorie/scope.md) · [Start projektu](teorie/jak-zacit.md)

### Scope creep

**Plíživé bobtnání rozsahu během vývoje: „co kdybychom přidali rybaření?"**

Dvojsečná past: někdy je to přesně ten twist, který hře chyběl, častěji fraktální bobtnání (rybaření → pruty → rybářské lodě) nebo míchání žánrů, které vyrobí hru pro nikoho — publikum dvou žánrů je průnik, ne součet. Rozhodovací filtr: sytí nápad účel hry, nebo ho ředí? Obrana: sticky note test na začátku, momentum bar a psaní nápadů do šuplíku během vývoje.

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Scope: nápad zaparkuj, nezabíjej](teorie/scope.md) · [Nápad](teorie/napad.md) · [Start projektu](teorie/jak-zacit.md)

### Scrum

**Agilní metodika: práce ve sprintech, priority se na sprint meetingu tahají z backlogu.**

Oproti kanbanu (plynulý tok karet) přidává rytmus: pevné bloky času s jasným cílem a review na konci. Indie hybrid: kanban board + měsíční „sprint" zakončený týdnem playtestů. Kříženec obou metodik se jmenuje scrumban.

Kde se s tím potkáš: [Plánovací nástroje](teorie/planovani-nastroje.md) · [Playtesting: kadence](teorie/playtesting.md)

### Semantic search

**Vyhledávání podle významu místo přesných slov; agent jím najde asset podle popisu.**

V ukázce Epicu agent zařizuje obývák a gauč nebo konferenční stolek najde podle popisu. Ukázková implementace je součástí MCP z 5.8. Funguje tím líp, čím lépe jsou assety pojmenované a popsané.

Kde se s tím potkáš: [Asistent, ne zázrak](praxe/mcp-v-editoru.md#asistent-ne-zazrak-slovnik-priklady-a-skills-delaji-z-llm-stavitele-sveta)

### Semiotika

**Nauka o tom, co symboly znamenají a proč — u písma a tvarů dřív, než přečteš obsah.**

Typografie nese význam třemi cestami: materiálem a nástrojem vzniku (dláto do kamene, brk, tiskový lis), historickou epochou a odkazy na jiná média (filmové plakáty, umělecká hnutí). Proto font sdělí žánr a dobu dřív, než hráč přečte první slovo — a proto hra zasazená do konkrétní éry znamená spoustu práce na cedulích a plakátech ve světě.

Kde se s tím potkáš: [Typografie](teorie/typografie.md) · [Ludotematický soulad](teorie/ludonarativni-soulad.md)

### Seamless loop

**Hudební smyčka, jejíž konec plynule navazuje na začátek — bez slyšitelného „švu".**

Herní hudba se přehrává donekonečna, takže poslední takt musí přejít do prvního. Jinak uslyšíš šev při každém opakování. Je to aranžérský přechod zapojený do kruhu.

Kde se s tím potkáš: [Tvorba herního soundtracku](hudba/tvorba-soundtracku.md)

### Self Pruning

**PCG uzel, který z překrývajících se bodů nechá jen některé — procedurální „ať se to nedotýká".**

Překryvy měří podle bounds, volitelně podle skutečných kolizí (use collision attribute) — pozor, bere menší z obou, takže pro kolizní režim bounds záměrně nafoukni bounds modifierem. S bounds nastavenými na požadovaný rozestup funguje jako foliage garance minimální vzdálenosti, jen checkboxem v grafu.

Kde se s tím potkáš: [PCG základy](praxe/pcg-zaklady.md) · [Shluky svíček](praxe/pcg-liany.md#podlaha-steny-a-strop-jednim-grafem-volumetric-sampling-misto-mesh-sampleru)

### Separation of concerns

**Princip: systém se dělí na malé části s jedinou zodpovědností — jako motor z vyměnitelných dílů.**

Návrhová otázka „co mají všechny X společné?" oddělí obecné (base classa, komponenta) od specifického (děti). Ability se vytáhne z komponenty do vlastního objektu; komponenta pak řeší jen aktivaci a cooldowny. Odměna: 20 abilit = 20 nezávislých blueprintů se stejnou strukturou, každý laditelný zvlášť.

Kde se s tím potkáš: [Principy architektury](praxe/principy-architektury.md) · [Organizace projektu](praxe/organizace-projektu.md)

### Septakord

**Akord se čtvrtým tónem přidaným nad triádu — septimou.**

Je to koření žánru: bez septakordů nezní funk funkově a jazz jazzově. Zároveň platí varování, které stojí za zapamatování, protože je proti intuici — **neudělej septakord z každého akordu v progresi**, protože tím emoci „vymyješ". Septakordy fungují jako kontrast, ne jako výchozí stav.

Kde se s tím potkáš: [Katalog progresí podle nálady](hudba/akordy-a-harmonie.md#katalog-progresi-podle-nalady) · [Rejstřík: Akord](#akord) · [Rejstřík: chord progression](#chord-progression)

### Sequencer

**Editor časových os v Unrealu — cutscény, kamerové záběry, animace postav a jejich úpravy, render filmových záběrů.**

Pracuje s [level sequences](#level-sequence): stopy actorů (transform, animace, control rig), camera cuts (s `Can Blend` pro plynulý přechod z herní kamery a zpět), fade, camera shake, události. V 5.8 se rozrostl o animátorské nástroje — výběr synchronizovaný s curve editorem, Simple View, fyziku vrstvenou nad animací a [AutoBake](#autobake). Hodí se i mimo cutscény, třeba jako měřidlo synchronizace animace s objektem.

Kde se s tím potkáš: [Cutscény](praxe/cutsceny.md) · [Sekundární pohyb v Control Rigu](praxe/animace-nastroje.md#sekundarni-pohyb-v-control-rigu-dynamics-za-behu-fyzika-a-autobake-pri-animovani) · [Animace řídí svět](praxe/interakcni-animace.md#animace-ridi-svet-normalizovane-krivky-v-montazi) · [Look-at systém](praxe/metahuman.md#look-at-system-pohled-vrstveny-pres-jakoukoli-animaci)

### Set dressing

**Zaplnění hotového prostoru drobnými propy a detaily, které mu dají příběh a život: nábytek, nádobí, nepořádek.**

Přichází po stavbě z kitu a v něm vzniká velká část vyprávění prostředím: kdo tu bydlel a co se tu stalo. Kvůli rychlosti se často staví z předpřipravených balíčků ([prefabů](#prefab)). V rozboru Alan Wake 2 patří spolu s kity a vyprávěním prostředím k základům, které technologie artistovi nebere.

Kde se s tím potkáš: [Alan Wake 2: lekce](praxe/env-technika.md#alan-wake-2-neviditelne-systemy-ktere-za-artisty-ozivi-les) · [Beauclair: dekorace jako balíčky](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [Rejstřík: Prefab](#prefab)

### Set Timer by Event

**Uzel, který po zadané době (jednou, nebo opakovaně) zavolá event — časovač místo Delay nebo Event Ticku.**

Vrací timer handle, přes který jde časovač zastavit (`Clear and Invalidate Timer by Handle`) nebo zjistit, kolik z něj uběhlo (`Get Timer Elapsed Time by Handle`) — tak se dá číst průběh hit stopu normalizovaně od 0 do 1. Opakovaný časovač po pár sekundách je levná náhrada ticku pro kontroly, které nemusí běžet každý snímek.

Kde se s tím potkáš: [Hit stop](praxe/souboj.md#hit-stop-zastav-oba-ale-kazdeho-jinak) · [Barel, který teče](praxe/pasti-a-mechaniky.md#barel-ktery-tece-diry-jako-data-hladina-jako-jedno-cislo) · [Terč: odstranění těla](praxe/souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave)

### Short description

**Krátký popis hry na Steamu — ~300 znaků pod capsule obrázkem, první text, který potenciální hráč čte.**

Zároveň nejlevnější validační nástroj nápadu: „test 300 znaků" = zkus popis napsat v den nula. Dvě věty se žánrem, perspektivou, hlavními činnostmi (hodně sloves!), cílem a prostředím. Když to nejde, nemáš vágní popis — máš vágní hru. Rozšířená verze testu je mock Steam page: dlouhý popis, features, zkusmá capsule.

Kde se s tím potkáš: [Nápad: test 300 znaků](teorie/napad.md) · [Scope](teorie/scope.md)

### Serif

**Patka: drobné zakončení na koncích tahů písmene. Nese historickou asociaci a mírně zpomaluje čtení.**

Vznikla v době fyzického tisku, kde bránila rozpíjení inkoustu a opotřebení stroje — proto s patkovým písmem podvědomě spojujeme starší dobu. Praktický důsledek pro hry: dekorativní patkový font se hodí na názvy a nápisy ve světě, ale funkční text (popisy schopností, tutoriály) patří do bezpatkového, protože se čte rychleji.

Kde se s tím potkáš: [Typografie](teorie/typografie.md)

### Sidechain

**Automatické stažení jednoho zvuku pokaždé, když udeří jiný — nejčastěji padu nebo basu při kopáku.**

Slyšitelný výsledek je „pumpování do beatu", které v taneční hudbě dělá místo pro kopák a zároveň drží energii. Ve Strudelu se jmenuje **`duck`**: vzor se dá na orbitu (skupinu sdílející efekty) a kopák na tu orbitu zavolá duck; `duckattack` řídí, jak dlouho zůstane stažené (0 = okamžitý návrat, 1 = drží dole). Existuje i varianta bez zdroje — ghost ducking, kde se ducká, jako by tam kopák byl.

Kde se s tím potkáš: [Zvuk, efekty a modulace](hudba/live-coding.md#zvuk-efekty-a-modulace) · [Rejstřík: LFO](#lfo)

### Signal

**Zpráva, kterou node vyšle, aniž by věděl, kdo ji poslouchá — vestavěný [observer pattern](#observer-pattern).**

Deklaruje se řádkem `signal neco_se_stalo`, vysílá `neco_se_stalo.emit()` a připojit se dá myší v editoru i kódem (`connect` / `disconnect`). Umí nést parametry, takže s událostí cestuje i kontext. Význam je v tom, co odesílatel **neví**: tlačítko netuší, které funkce jsou na jeho signál napojené, takže se dá použít kdekoli. V Unrealu je nejbližší příbuzný [event dispatcher](#event-dispatcher).

Kde se s tím potkáš: [GDScript: call down, signal up](godot/gdscript.md#call-down-signal-up-kdo-koho-smi-znat) · [Komunikace Blueprintů](praxe/komunikace-blueprintu.md#tri-kanaly-a-kdy-ktery-cast-interface-event-dispatcher)

### Signal-to-noise ratio

**Poměr užitečné informace (signál) k balastu (šum) — klíčová veličina učení, soustředění i designu obtížnosti.**

Učení je budování prediktivního modelu světa a potřebuje data, ze kterých se dá učit. Frustrace = konstantní „špatně" (nulový signál), nuda = konstantní „dobře" (nulový signál); flow kanál je pásmo, kde některé akce fungují a jiné ne — nejlepší signál. Jasné cíle jsou filtr šumu; soustředění je totéž z druhé strany (rozptýlení a vizuální balast = šum).

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Shading bin

**Nanitová obdoba draw callu: každý materiál ve scéně si vyžádá vlastní bin, s minimem ~3 µs na GPU.**

Vlastní bin potřebuje **každá materiálová instance** — konstantní i dynamická — takže počet binů roste s rozmanitostí materiálů, ne s počtem meshů. Řádová orientace z profilování reálné hry: naměřeno ~2 100 raster a ~4 000 shading binů, cíl ~50 raster a ~1 000 shading. Cesta dolů je architektonická: pevná topologie materiálu a znovupoužité instance, kterým se hodnoty předávají přes custom primitive data, material parameter collections nebo per-instance custom data — místo skládání materiálových vrstev jako v Photoshopu.

Kde se s tím potkáš: [Čísla, se kterými se dá srovnávat](praxe/profiling.md#cisla-se-kterymi-se-da-srovnavat) · [Rejstřík: Nanite](#nanite) · [Rejstřík: Draw call](#draw-call)

### Shape language

**Standardizace tvarů pro významy napříč celou hrou: plus je zdraví, kruh štít, špičaté tvary poškození.**

Nutnost všude, kde je efektů nebo ikon hodně — konzistentní tvarosloví umožní pochopit funkci prvku bez čtení. Klíčová vlastnost: když jsou barvy podobné, tvar je jediné, co prvky rozliší. Používá se stejně ve VFX i v rozhraní, a spolu s barvou a pozicí tvoří pravidla, kterým se říká vizuální jazyk hry.

Kde se s tím potkáš: [Art specializace: VFX](teorie/art-specializace.md) · [Game feel](teorie/game-feel.md)

### Significance handler

**Pravidlo, které u Niagary rozhodne, které instance přežijí strop počtu.**

Vestavěné jsou dvě — **podle vzdálenosti** a **podle věku**; vlastní se dá dopsat v C++. Bez něj strop instancí funguje, ale vybírá libovolně. Pozor na cenu při velkých počtech: u tisíců systémů na jednom effect typu musí significance manager při každé změně projít celé pole (naměřený případ: **~7 000 systémů na padající listí → 30ms spike**). Praktické pravidlo: **strop instancí je levnější než významnost** — nejdřív omez počet, pak laď, kdo přežije.

Kde se s tím potkáš: [Effect type](praxe/niagara-vykon.md#effect-type-jeden-asset-ktery-rozhoduje-o-vsem) · [Rejstřík: Effect type](#effect-type) · [Significance Manager v AI](praxe/ai-ve-velkem.md#velky-nepritel-na-malem-agentovi-offset-cesty-ktery-nevyjede-z-navigace)

### Significance Manager

**Plugin UE, který objektům průběžně počítá význam (třeba podle vzdálenosti od hráče) — hra podle něj rozhoduje, kdo běží naplno, kdo zpomalí a kdo spí.**

V Lords of the Fallen drží nanejvýš 20 aktivních nepřátel a s LOD a agregací ticku vypíná, co není potřeba. U Niagary jde o příbuzný mechanismus, [Significance handler](#significance-handler), který vybírá, které instance efektu přežijí strop počtu.

Kde se s tím potkáš: [Velký nepřítel na malém agentovi](praxe/ai-ve-velkem.md#velky-nepritel-na-malem-agentovi-offset-cesty-ktery-nevyjede-z-navigace)

### Silueta

**Obrys tvaru — nejrychlejší nosič identity a čitelnosti; poznáš z ní postavu i prostředí bez jediného detailu.**

V prostředí siluety vyrábí kontrast světla a stínu (chiaroscuro): žádný kontrast = žádné tvary = „proč to vypadá špatně, když mám Nanite?". Test: screenshot → odbarvit → levels stáhnout na černobílou; když nezbydou čitelné plochy světla a tmy, žádný setting scénu nezachrání. U assetů rozhoduje silueta o rozpoznatelnosti víc než textury.

Kde se s tím potkáš: [Stavba prostředí](praxe/env-tvorba.md) · [Breakdowny](praxe/env-breakdowny.md) · [Blockout se soudí podle siluety](praxe/blockout.md#zastav-omez-porovnej-blockout-ktery-se-da-precist)

### Simulated annealing

**Optimalizace po vzoru žíhání kovů: začni ochotou přijímat i horší kroky (explorace) a postupně chladni k vylepšování.**

Prostý hill-climb uvízne na prvním lokálním vrcholu; klesající „teplota" dává šanci přeskočit údolí k lepším řešením. Tentýž explore/exploit trade-off, na kterém stojí teorie zábavy — tady jako nástroj na rozvrhy, rozmístění a tuning parametrů.

Kde se s tím potkáš: [Algoritmy, které stojí za to znát](teorie/algoritmy-prehled.md) · [Zábava a flow](teorie/zabava.md)

### Single Layer Water

**Shading model pro vodu: translucence a kaustika za cenu jednoho průchodu — de facto standard v UE.**

Zásadní limit: stíny přijímá jen z primárního directional lightu — scéna svícená spotlighty se na hladině rozpadne. Řešení per záběr: přepnout materiál na Default Lit (+ metallic 1 pro tmavou hlubokou vodu) tam, kde translucenci nepotřebuješ. Žádný z modelů není univerzálně lepší.

Kde se s tím potkáš: [Nástroje: EasyWaterscape](praxe/nastroje-voda.md)

### Single responsibility principle

**Jeden modul, jedna zodpovědnost — a tedy jen jeden důvod, proč ho měnit.**

Prakticky: jeden skript, jedna práce. Health komponenta řeší život a smrt, input komponenta jen tlačítka. Porušení se pozná podle toho, že soubor roste a přibývají do něj věci, které spolu nesouvisejí — `player.gd` s pohybem, dvojskokem, dashem, útokem, úhybem a blokem je učebnicový příklad. Kritérium pro rozdělení není délka, ale **počet nezávislých důvodů ke změně**: mění-li se dvě části souboru z různých podnětů, patří jinam.

Kde se s tím potkáš: [Has-a místo is-a](godot/kompozice.md#has-a-misto-is-a-hrdinuv-batoh) · [Principy architektury](praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data)

### Single source of truth

**Jedna informace existuje na jednom místě; kdo ji potřebuje, ptá se toho místa místo aby si držel vlastní kopii.**

Zkracuje se SSOT. Problém, který řeší, je **rozejití duplicitních stavů**: dvoje hodiny v domě ukazují různý čas a ty nevíš, kterým věřit. V kódu to vypadá tak, že hra funguje, dokud někdo neaktualizuje jednu kopii a na druhou zapomene — pak se chová nepředvídatelně a bez chybové hlášky. Řešení není nutně mazat proměnné; je to **rozhodnout, kde stav bydlí** (vlastnost nodu, existence spojení, jedna proměnná) a všechny ostatní přinutit se ptát.

Kde se s tím potkáš: [Jediný zdroj pravdy](godot/signaly.md#jediny-zdroj-pravdy-dva-budiky-ukazuji-ruzny-cas) · [Gameplay Tags](praxe/gameplay-tags.md#hierarchie-misto-booleanu-proc-statusmovementblocked-vyhrava)

### Singleton

**Vzor garantující jedinou instanci s globálním přístupem — a zároveň „glorifikovaná globální proměnná".**

Legitimní pro centrální logger či connection pool; nebezpečný jako výmluva pro globální stav (mizerné testování, multithreading chce ošetření). V UE singleton žije jako Game Instance a Subsystems — jedinost garantuje engine; co tam nacpeš, to se rozleze.

Kde se s tím potkáš: [Design patterns](teorie/design-patterns.md) · [Principy architektury](praxe/principy-architektury.md)

### Size Map

**Nástroj editoru, který ukáže, kolik paměti asset zabere i se vším, co s sebou táhne.**

Pravý klik na asset → Size Map → Memory Size. Nejlepší způsob, jak zviditelnit cenu tvrdých referencí: přidání jediného cast uzlu do blueprintu může jeho paměťovou stopu zdvojnásobit, protože cílová třída se od té chvíle nahrává s ním. Diagnostický protějšek Reference Vieweru, který ukazuje vazby, ne velikost.

Kde se s tím potkáš: [Komunikace Blueprintů: kolik stojí cast](praxe/komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) · [Principy architektury](praxe/principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Soft reference](praxe/pamet-a-instance.md#soft-reference-nacti-az-kdyz-to-hra-potrebuje)

### Skill ceiling

**Maximální dosažitelná úroveň dovednosti ve hře — strop toho, jak dobře se dá hrát.**

Vysoký ceiling znamená prostor pro růst a mastery (fighting hry, závodní simy); nízký znamená, že hru brzy „vytěžíš". „Easy to learn, hard to master" = nízký floor + vysoký ceiling — drahý ideál, který vyžaduje hloubku systémů, ne jen tvrdší čísla.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Skill floor

**Minimální dovednost nutná k tomu, hru vůbec hrát — bariéra vstupu.**

Kdo na floor nedosáhne, nehraje (dítě s ovladačem hru „hraje" jen zdánlivě). Komplexita ovládání je floor sama o sobě — proto casual hry sázely na Wii remote a touchscreeny. Hardcore hry mají floor záměrně výš: předpokládají znalost konvencí žánru.

Kde se s tím potkáš: [Obtížnost a výzva](teorie/obtiznost.md)

### Skills audit

**Inventura vlastních dovedností před volbou projektu: co umím, co neumím, co napůl.**

Zdroje projektu nejsou jen čas a peníze — hlavně schopnosti. Audit vyřadí 90 % nápadů a zbydou proveditelné: máš ilustrátora bez animátora → hra s mluvícími portréty (Dredge nemá walk cycle, Mini Metro nemá postavy — dohromady přes 6 milionů kopií). Tvrdší varianta otázky: co neumím tak, že to do projektu nesmí?

Kde se s tím potkáš: [Nápad: ideace jako řemeslo](teorie/napad.md) · [Scope: rozpočet pozornosti](teorie/scope.md)

### Skirt

**Pruh geometrie kolem spodku kusu, který přechází do země a skrývá ostrý šev mezi objektem a terénem.**

Sukně nese materiál, který se prolne s podkladem, třeba hlínu nebo mech, takže kus nevypadá postavený na zem, ale zasazený do ní. Ve workshopu o kitech je to jeden ze čtyř texturových spojů vedle vertex blendingu, decalů a světové projekce.

V terénech rozdělených na chunky má slovo ještě druhý význam: svislý pruh geometrie na okraji chunku, který zakryje praskliny mezi sousedními chunky s různým LOD.

Kde se s tím potkáš: [Organický kit a spoje](praxe/modularni-kity.md#organicky-kit-a-spoje-zaborit-nechat-rust-od-zdroje-zakryt-sev) · [Textury pro kit: sendvič](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen) · [Terrain skirts mezi chunky](praxe/velke-svety.md#dohled-na-kilometry-vetsi-chunky-v-dalce-stromy-se-stinem-a-souradnice-ktere-nepretecou)

### Smart Object

**Objekt světa, který inzeruje interakce: sloty k zabrání a chování (State Tree), které se po claimu spustí na postavě.**

Lavička nese smart object komponentu a definition data asset; NPC si najde volný slot, claimne ho (druhé NPC už ho nedostane) a spustí injektovaný strom — jiný objekt dodá jinou logiku, beze změny AI postavy. V GASP navázané na Motion Matching: vstupní montáž se vybírá pose match sloupcem podle pózy a vzdálenosti od vstupního bodu.

Kde se s tím potkáš: [GASP](praxe/gasp.md) · [Hráč na lavičce v 5.8](praxe/gasp.md#posledni-update-pro-ue5-sample-ne-framework)

### SMPL-X

**Parametrický model lidského těla a kostry z výzkumu, který nejde použít komerčně.**

Kimodo.cpp ho zpočátku podporoval jako jedinou kostru. Do hry vol licenčně čisté kostry, u Kimoda SOMA nebo G1, a animaci retargetuj.

Kde se s tím potkáš: [Animace z modelu přímo ve hře](praxe/ai-assety.md#animace-z-modelu-primo-ve-hre-animgen-se-trenuje-v-editoru-porty-modelu-nvidia-bezi-i-na-cpu) · [Rejstřík: Retargeting](#retargeting)

### Socket

**Pojmenovaný bod na kosti skeletal meshe (nebo na static meshi), ke kterému se připínají jiné objekty — zbraň do ruky, předmět při zvednutí.**

Socket má vlastní offset a rotaci vůči kosti, takže se dá doladit, jak předmět v ruce sedí; v editoru skeletu pomůže preview asset. Když má každý předmět jiný úchop, má i vlastní socket a jeho jméno vrací předmět sám, třeba přes interface. Jak se předmět na socket dostane, určují [attachment rules](#attachment-rules).

Kde se s tím potkáš: [Jedna animace zvednutí](praxe/interakcni-animace.md#jedna-animace-zvednuti-pro-vsechno-grip-pointy-a-pozy-ruky) · [Předmět do ruky bez teleportu](praxe/interakcni-animace.md#predmet-do-ruky-bez-teleportu-attach-neni-snap-a-dosah-neni-dohled) · [Řemeslo první osoby: pistole a baterka](praxe/animace-nastroje.md#krivky-kamera-a-past-30-snimku-remeslo-prvni-osoby) · [Hitbox mezi sockety zbraně](praxe/souboj.md#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames) · [Sklo a doplňky přes sockety](praxe/pcg-mesta.md#budova-jako-veta-panelovy-kit-gramatika-a-patra) · [Sockety jako rozdělovník](praxe/pcg-mesta.md#variabilita-z-dat-sockety-barvy-instanci-a-presety-pod-tagy)

### Soft boundary

**Hranice mapy, kterou lze fyzicky překročit — ale svět dá jasně najevo, že je to špatný nápad.**

Pět vzorů: narativní (most se zřítí, postava odmítne jít dál), countdown (mráz, plyn, dezerce — tlak času místo kolize), nepřátelská (za hranicí loví něco silnějšího; nemusí zabíjet — stačí probrat se potlučený zpátky), ekonomická (kyslík/palivo nevystačí na návrat) a percepční (ztráta orientace a viditelnosti). Nejlépe fungují kombinované a vždy s fikčním alibi.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Softlock

**Stav, kdy hra běží, ale nedá se dohrát — hráč uvízl bez cesty dál a bez způsobu, jak se vrátit.**

Typické příčiny: ztracený předmět, který hádanka potřebuje, spínač, který nejde znovu stisknout, nebo obejitá podmínka postupu. Obrana je v designu: cíl podmíněný tím, co hráč musí mít (všechny klíče), ne místem, kam se dostal, a předměty hádanky, které se doplní, když se ztratí.

Kde se s tím potkáš: [Hádanka ze stavebnice](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit)

### Soft reference

**Odkaz, který drží jen cestu k assetu — nic nenačte, dokud si o to hra neřekne.**

Typ proměnné *Soft Object Reference* (pro třídy *Soft Class Reference*). Použití: `Is Valid?` → je-li asset načtený, použij ho; jinak `Async Load Asset` a pokračuj z pinu *Completed*. Šetří paměť (blueprint s jedním efektem 24,5 MB → 99 KB) i škubnutí při spawnu, protože se načítá na pozadí. Past: v editoru to často funguje i bez načtení, protože asset už je v paměti odjinud; po restartu se nenačte nic. Kdy: u assetů potřebných jen při konkrétní akci.

Kde se s tím potkáš: [Soft reference: načti, až když to hra potřebuje](praxe/pamet-a-instance.md#soft-reference-nacti-az-kdyz-to-hra-potrebuje) · [Rejstřík: Hard reference](#hard-reference)

### Soft skills

**Dovednosti bez přímo viditelného výstupu — úsudek, komunikace, analýza, empatie; modifikují kvalitu všeho, co vzniká.**

Protiklad hard skills (kód, obrázek — měřitelný výstup). Zásadní rozdíl pro učení: hard skills se dají učit didakticky (návodem), soft skills jen objevováním — hraním, rozborem, workshopem. Game design je svazek soft skills; proto na něj neexistují recepty.

Kde se s tím potkáš: [Rady z praxe](teorie/rady-z-praxe.md) · [Učení v éře AI](teorie/uceni-v-ere-ai.md)

### Sound Cue

**Klasický zvukový asset UE: graf uzlů nad wave soubory — random variace, mixování, attenuace.**

Multi-select wave souborů → Create Sound Cue vloží Random uzel automaticky (variace kroků jedním klikem). Pro pokročilejší práci (parametry za běhu, procedurální audio) je nástupcem MetaSounds; Sound Cue zůstává nejrychlejší cesta k „přehraj náhodnou variaci".

Kde se s tím potkáš: [Kroky](praxe/footsteps.md) · [Pět potvrzení rány](praxe/souboj.md#rana-ktere-hrac-uveri-pet-potvrzeni-kazde-o-necem-jinem)

### Sound font

**Kolekce nasamplovaných zvuků nástroje, přehrávaná sound font playerem (soubory .sf2).**

Charakteristický retro zvuk herní hudby (Undertale) často dělá paleta, ne skladba — Toby Fox použil fonty ze SNES her. Rychlá, autentická alternativa ke stavbě zvuku od nuly v synthu.

Kde se s tím potkáš: [Tvorba herního soundtracku](hudba/tvorba-soundtracku.md)

### Source radius

**Velikost zdroje světla, která určuje, jak měkký stín světlo vrhá a jak velký dělá odlesk.**

S nulovým radiem svítí světlo z jediného bodu a stíny jsou ostré jako vystřižené. Skutečné zdroje mají plochu, a tak větší radius dá přirozený polostín, třeba u svíčky nebo pochodně. Vedle něj má světlo i soft source radius, který změkčí okraj tvaru zdroje, a bodové světlo navíc délku zdroje (source length), se kterou svítí jako trubice. Zdroj je vidět i v odrazech, a proto se u pomocných světel vypíná specular scale.

Kde se s tím potkáš: [Svítidlo z víc světel](praxe/megalights.md#svitidlo-z-vic-svetel-odraz-mlha-a-stin-se-ladi-zvlast) · [Attenuation radius jako hlavní páka](praxe/megalights.md#attenuation-radius-jako-hlavni-paka-pocitej-prekryvy-ne-svetla) · [Rejstřík: Rect light](#rect-light)

### Sparse set

**Minimální sada animací pro Motion Matching: ~13 klipů bez strafu, ~26 se strafem, ~60–80 se stavy.**

Epicův recept proti mýtu „potřebuju 500 animací jako GASP": idle, run forward, starty a stopy (levá i pravá noha kvůli stutter-stepům), oblouky (run arcs) a refacing starty. Rozsah řídí otázky na hru: co gameplay potřebuje a kolik movement states (každý ≈ 2×). S procedurálními uzly je 26animační set podle Epicu shippable. Klidně hand-keyed a stylizovaný.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Spatial Noise

**PCG uzel, který bodům přiřadí hodnotu podle šumového vzoru ve world space.**

S Density Filter z něj vznikají přirozené shluky místo čistě náhodného rozptylu. Měřítko vzoru určuje velikost shluků a kontrast rozdíl mezi shlukem a prázdným místem. Protože vzor drží ve světě, sousední grafy na sebe navazují. Podle Procedural Minds je uzel jen 2D.

Kde se s tím potkáš: [Podlaha, stěny a strop jedním grafem](praxe/pcg-liany.md#podlaha-steny-a-strop-jednim-grafem-volumetric-sampling-misto-mesh-sampleru) · [Les pro otevřený svět](praxe/pcg-vegetace.md#les-pro-otevreny-svet-co-se-nacte-s-levelem-a-co-roste-kolem-hrace)

### Sphere tracing

**Trasování podél paprsku po skocích dlouhých tolik, kolik říká distance field — bližší povrch tam není, takže se nic nepřeskočí.**

Na rozdíl od klasického paprsku, který je nekonečně tenký a proklouzne škvírou, se dá trasovat s tloušťkou: objekt (třeba ryba v hejnu) projde jen tam, kam se vejde. Na GPU nad [global distance fieldem](#global-distance-field) je to levná náhrada kolizí pro velké množství částic; na platformách bez distance fieldů ale nejde.

Kde se s tím potkáš: [Živý svět z částic](praxe/niagara-vykon.md#zivy-svet-z-castic-tvorove-kteri-poslouchaji-ale-nehlasuji) · [Rejstřík: Global Distance Field](#global-distance-field)

### Spline

**Komponenta s křivkou z tažitelných bodů — trasa, po které se dá vést pohyb, geometrie nebo obsah.**

Body se tahají přímo v levelu (Alt + tažení duplikuje); kód čte Get Location at Spline Point / Get Number of Spline Points — pozor na coordinate space (typicky World). V AI definuje patrol trasy, v traversal systémech značí hrany překážek, u coveru tvar krytí.

Kde se s tím potkáš: [State Trees](praxe/state-trees.md) · [GASP](praxe/gasp.md) · [Systémy nad MM](praxe/mm-systemy.md) · [Interakce s předměty](praxe/interakce-predmety.md)

### Spline mesh

**Mesh procedurálně natažený a ohnutý podél segmentu splinu — křivka se stává viditelnou geometrií.**

Každý segment dostane instanci meshe zdeformovanou mezi počátečním a koncovým bodem (Set Start and End v Blueprintu, spline mesh spawner v PCG). Na orientaci záleží: forward axis musí odpovídat ose meshe, jinak se geometrie kroutí. Liány a lana z obyčejného válce, oblouk předpovězené dráhy hodu z tenkého průsvitného válce.

Kde se s tím potkáš: [PCG liány](praxe/pcg-liany.md) · [Interakce s předměty](praxe/interakce-predmety.md) · [Zaoblené nároží](praxe/pcg-mesta.md#budova-jako-veta-panelovy-kit-gramatika-a-patra) · [Interiér z bodů](praxe/pcg-mesta.md#interier-z-bodu-mistnosti-jako-subgrafy-a-devet-uzlu-na-bar)

### Spline Sampler

**PCG uzel, který ze spline udělá body, buď podél křivky, nebo s volbou On Interior uvnitř uzavřené spline.**

Je základem plotů, cest, mýtin i interiérů z půdorysu. S Fit to Curve rozprostře body rovnoměrně po celé délce. Výsledné body jde filtrovat, posouvat a spojovat do nových spline.

Kde se s tím potkáš: [Interiér z bodů](praxe/pcg-mesta.md#interier-z-bodu-mistnosti-jako-subgrafy-a-devet-uzlu-na-bar) · [Mýtiny a cesty](praxe/pcg-vegetace.md#mytiny-a-cesty)

### Sprite sheet

**Jeden obrázek, ve kterém je mřížka jednotlivých snímků animace nebo sada dlaždic.**

Alternativou by byl soubor na každý snímek, což se u animované postavy rychle změní v neudržovatelnou hromadu. Engine si z listu vyřízne buňky podle zadané mřížky a poskládá z nich animaci (v Godotu `AnimatedSprite2D` + `SpriteFrames`) nebo [tile set](#texture-atlas). Vedlejší efekt, kvůli kterému se to dělá i tam, kde by jednotlivé soubory nevadily: všechny snímky jsou v jedné textuře, takže se kreslí z jedné paměti.

Kde se s tím potkáš: [První hra](godot/prvni-hra.md) · [Rejstřík: Flipbook](#flipbook)

### Squeeze and release

**Rytmus střídání tlaku a úlevy: výzva hráče stiskne, checkpoint nebo odměna povolí.**

Hry stresují záměrně, protože stres je nosič výzvy — jenže obě krajnosti končí stejně: samý tlak vede k frustraci, samá úleva k nudě, a hráč v obou případech skončí. Nejúčinnější a nejlevnější forma úlevy je **checkpoint**, který nic nedává, jen přestane hrozit. Prakticky z toho plyne, že rozmístění checkpointů není technické rozhodnutí, ale dramaturgické — a v pasáži, kde chceš držet napětí, se vynechává schválně.

Kde se s tím potkáš: [Squeeze and release](godot/pripadovka-proces.md#squeeze-and-release-hra-bez-stresu-neni-hra) · [Horor design](teorie/horor-design.md)

### Square hole

**Chyba balancu: univerzální nástroj či strategie, která řeší každou situaci — a tím zabíjí všechna rozhodnutí.**

Podle memu „it goes in the square hole". Vzniká z balancování jedinou osou síly: jeden nástroj vždycky vyjde o chlup líp a stane se odpovědí na všechno. Lék: vícerozměrné nástroje (každý dobrý na něco jiného) + pestré problémy + zajímavé hraniční případy, kde volba vyžaduje úvahu. Cíl balancu: rozhodnutí netriviální, předvídatelná a nosná i po opakování.

Kde se s tím potkáš: [Zábava: balanc rozhodnutí](teorie/zabava.md)

### Squash & stretch

**Animační princip: deformace objektu při akci — zploštění při dopadu, natažení při výskoku.**

Nejstarší trik animace (Disney) přenesený do her: skok s deformací působí pružně, nepřítel, který se při zásahu „zmáčkne", působí živě. Levný a účinný kus juice — mění pocit, ne mechaniku.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md)

### State alias

**Zástupný uzel ve state machine, který reprezentuje všechny zaškrtnuté stavy — jedno přechodové pravidlo místo N.**

Alias „to crouch" zastupující idle i walk/run znamená jediný přechod do podřepu místo přechodu z každého stavu zvlášť. S rostoucím počtem stavů drží graf čitelný; pravidla se píší jednou a platí pro všechny zastoupené stavy.

Kde se s tím potkáš: [Základy pohybu](praxe/pohyb-zaklady.md)

### State machine

**Stavový automat v AnimBP: stavy = animace, přechody = pravidla — klasická architektura herní animace.**

Užitečné vzory: vícedílné akce (skok start → loop → end) s Automatic Rule Based on Sequence Player (přechod po dohrání klipu), state aliases proti explozi přechodů, AnimBP bez castu (Try Get Pawn Owner + Get Movement Component = funguje na každé postavě se stejným skeletonem). Motion Matching state machines nahrazuje, ale hybridní setupy je kombinují dál.

Kde se s tím potkáš: [Animační nástroje](praxe/animace-nastroje.md) · [MM základy](praxe/mm-zaklady.md) · [Základy pohybu](praxe/pohyb-zaklady.md)

### State Tree

**Hierarchický stavový automat UE pro AI i obecnou logiku — sesterský systém behavior tree.**

Vyhodnocuje se shora dolů, stavy nesou tasky a přechody podle úspěchu/selhání; umí linkované podstromy (patrol) i stromy injektované zvenčí (smart objects). Přechody spouští i eventy s gameplay tagy (Send State Tree Event); Finish Task končí celý stav, context injektuje taskům AI controller. Tasků má z krabice málo — píšou se per projekt.

Kde se s tím potkáš: [State Trees](praxe/state-trees.md) · [GASP](praxe/gasp.md) · [Reakce vedle stromu](praxe/ai-ve-velkem.md#reakce-vedle-stromu-co-se-muze-stat-v-kazdem-stavu-nepatri-do-zadne-vetve)

### Static switch

**Přepínač v materiálu, o kterém se rozhoduje při kompilaci — nepoužitá větev ze shaderu úplně zmizí.**

Proto je levnější než lerp mezi nulou a jedničkou, který počítá obě větve a jen je smíchá. Cena je jinde: každá kombinace přepínačů je další permutace shaderu, tedy víc kompilace a paměti. Typické použití: materiálová instance, která drahou vrstvu nepotřebuje, ji přepínačem vypne místo násobení nulou.

Kde se s tím potkáš: [Bojovka pro desetiletý hardware](praxe/gpu-pruchod.md#bojovka-pro-desetilety-hardware-rozpocet-po-castech-a-co-se-v-nem-naslo) · [Rejstřík: PSO](#pso)

### Steam Next Fest

**Steamový online festival demoverzí nevydaných her, koná se třikrát ročně.**

Funguje jako multiplikátor wishlistů — čím víc jich máš na vstupu, tím víc akce vygeneruje — a každá hra se smí zúčastnit jen jednou, takže načasování je strategické rozhodnutí (jít tam s maximem, klidně couvnout a počkat na další termín). Citované minimum pro smysluplný efekt ~7 000 wishlistů na vstupu (údaj jednoho vydání, ne konstanta).

Kde se s tím potkáš: [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Stem separace

**Rozdělení hotové nahrávky zpět na jednotlivé složky — zpěv, bicí, bas, zbytek.**

Dnes to zvládají modely překvapivě dobře a v praxi se to používá jinak, než se čekalo: ne na remixy, ale jako **mezikrok v řetězu** — vytáhnout z generovaného výstupu jen tu stopu, kterou chceš, a zbytek zahodit. Výsledek nese artefakty, které jsou tím slyšitelnější, čím víc se stopy v originále překrývaly.

Kde se s tím potkáš: [AI na vokál](hudba/nastroje-zdarma-a-game-jam.md#ai-na-vokal-prezpivat-ale-zustat-sam-sebou) · [Rejstřík: Klonování hlasu](#klonovani-hlasu) · [Rejstřík: Sampling](#sampling)

### Streaming pool

**Pevně vyhrazená část VRAM pro streamované textury; při přeplnění spadne rozlišení mipy.**

Výchozích 2 000 MB bylo zvoleno pro cizí projekt — a příliš velký pool je stejná chyba jako příliš malý, jen tišší, protože ta paměť chybí jinde. Postup, jak zjistit skutečnou potřebu: **zmenšuj `r.Streaming.PoolSize`, dokud engine nezačne hlásit „streaming pool over budget"** — to je tvůj vodočet. Virtuální textury mají pooly zvlášť pro každý kompresní formát; od 5.4 si engine vede transient list dosažených maxim, ze kterého se hodnoty opíšou do fixed poolu.

Kde se s tím potkáš: [Pooly a jejich vodočty](praxe/gpu-pamet.md#pooly-a-jejich-vodocty) · [Rejstřík: Virtual texture](#virtual-texture) · [Rejstřík: Mip mapa](#mip-mapa)

### Stitching

**Experimentální MM technika: místo lineárního blendu najde animaci, která tě za daný čas dostane z aktuální pózy do cílové.**

Řeší přechody locomotion → gameplay akce (úder, který má za 0,25 s dopadnout) a gameplay → cinematika (sequencer stitch track v 5.6; Witcher 4 demo). Nosiče: Chooser Player se stitch databází, Sequence Player se „start with matching pose" + Pose Search Branch In notify. Čas přechodu je laditelný designérem, ne zadrátovaný animátorem.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Strategy pattern

**Rodina zaměnitelných algoritmů, každý ve své třídě za společným rozhraním — místo rostoucího if/else stromu.**

„Programování na úrovni rozhraní": cíl jeden, strategií víc, výměna za běhu. Ukázka open-closed principu — nové chování přidáš novou třídou bez sahání do existujícího kódu. V UE: movement modes Moveru, choosery, Blueprint Interface místo kaskády castů.

Kde se s tím potkáš: [Design patterns](teorie/design-patterns.md) · [Mover](praxe/mover.md)

### String pulling

**Zkrácení cesty přes navigační polygony na nejkratší možnou — body se přitáhnou k rohům a přebytečné zmizí (funnel algoritmus).**

S agentem stejně velkým jako postava funguje. Je-li agent menší, vede velkou postavu těsně kolem rohů a odsazení od nich musí přijít zvlášť. Vestavěné Offset From Corners přitom posouvá jen konce úseků a umí cestu vyvést mimo navigaci.

Kde se s tím potkáš: [Velký nepřítel na malém agentovi](praxe/ai-ve-velkem.md#velky-nepritel-na-malem-agentovi-offset-cesty-ktery-nevyjede-z-navigace) · [Rejstřík: Nav Agent](#nav-agent)

### Strudel

**Prohlížečové prostředí pro live coding hudby — JavaScriptová verze jazyka TidalCycles.**

Nic se neinstaluje, běží na `strudel.cc`, vestavěné zvuky nesou jména z klasických bicích automatů (`bd`, `hh`, `cp`). Základ je **mini notace**: `*4` dělí cyklus na čtvrtiny, `[a b]` dělí dál, `~` je pomlka, `<a b>` střídá po cyklech, `{}` je polymetr. Dvě věci, které začátečníka nutně potkají: **vzory zleva doprava určují, jak často se vzorkuje ten vpravo** (léčí `setDefaultJoin('mix')`) a **dlouhé vzorky se bez `clip(1)` vrství samy na sebe**.

Kde se s tím potkáš: [Cyklus jako pizza](hudba/live-coding.md#cyklus-jako-pizza-mini-notace) · [Rejstřík: Live coding](#live-coding) · [Rejstřík: Euklidovský rytmus](#euklidovsky-rytmus)

### Struct

**Pojmenovaná skupina proměnných, se kterou se zachází jako s jednou hodnotou.**

Místo osmi vstupů do funkce jeden; místo osmi proměnných v SaveGame objektu jedna. Kromě čitelnosti přináší hlavně jedno místo změny: přidáš-li do struktury pole, všechna místa, která ji předávají, fungují dál. V save systémech je to rozdíl mezi rozšiřitelným formátem a rozsypaným seznamem.

Kde se s tím potkáš: [Ukládání: struktury a interface](praxe/ukladani.md#save-system-ktery-prezije-druhy-projekt-struktury-interface-a-async) · [Data stran dveří](praxe/interakcni-animace.md#objekt-vi-jak-se-s-nim-zachazi-data-interakce-patri-k-veci-ne-k-postave) · [Hitbox: profil útoku](praxe/souboj.md#hitbox-podle-toho-jak-poctiva-je-animace-impact-frame-nebo-active-frames) · [Zdraví po končetinách](praxe/souboj.md#zdravi-po-koncetinach-physical-material-jako-adresa-struct-jako-stav)

### Stupnice

**Sada tónů, které spolu znějí dobře, daná vzorcem půltónů a celých tónů.**

Durová = celý–celý–půl–celý–celý–celý–půl, mollová = celý–půl–celý–celý–půl–celý–celý; vzorec přiložíš na libovolný tón. Nemusíš znát tóny každé tóniny — stačí vzorec a počítat půltóny.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Subsystem

**Automaticky vytvářený singleton s definovaným životním cyklem (engine / game instance / world / local player).**

Nemusíš ho spawnovat ani registrovat — engine ho vytvoří a drží podle typu. Game instance subsystem žije po celou dobu aplikace, ideální pro mediátory (event manager, broadcast kanály) a služby bez vlastního místa ve světě. Blueprintově se konzumuje snadno; definice vyžaduje C++.

Kde se s tím potkáš: [Komunikace Blueprintů](praxe/komunikace-blueprintu.md) · [Principy architektury](praxe/principy-architektury.md)

### Subtraktivní syntéza

**Nejběžnější typ syntézy (subtractive synthesis): oscilátor generuje bohatý zvuk, filtr z něj ubírá.**

Řetězec oscilátor → filtr → obálka/LFO. Slavný pad je jen pila protažená filtrem. Pochopíš-li tenhle jeden signálový řetězec, přečteš skoro každý synth.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Surface cache

**Zjednodušená reprezentace povrchů scény, ze které Lumen čte při world traces.**

Diagnostický view mode má vlastní legendu: **žlutá** = Lumen to z Lumen scény vyřadil a neřeší · **fialová** = do Lumen scény se to nakreslilo, ale pixely se nevykreslily — typicky protože surface cards nejsou správně nastavené nebo je mesh příliš členitý. Odtud pochází většina záhad typu „proč se ta lávka v nepřímém osvětlení vůbec neobjevuje".

Kde se s tím potkáš: [Lumen: rozpočet a binární hledání](praxe/gpu-pruchod.md#lumen-rozpocet-a-binarni-hledani) · [Rejstřík: Lumen](#lumen)

### Survivorship bias

**Zkreslení z toho, že vidíš jen ty, kdo přežili — neúspěšné pokusy zmizí z dohledu.**

V gamedevu je obzvlášť silné: postmortemy píšou hlavně ti, komu to vyšlo, a zrušené projekty nemají Steam stránku. Poctivé odhady mluví o tom, že úspěchu ve smyslu udržitelné obživy dosáhne méně než patnáct procent těch, kdo to zkusí. Praktický důsledek: rady od úspěšných vývojářů popisují nutné, ne postačující podmínky.

Kde se s tím potkáš: [Data o úspěchu](teorie/data-o-uspechu.md#krivka-preziti-proc-se-sance-zlepsuji-s-patou-hrou) · [Přežít jako studio](teorie/prezit-jako-studio.md#stesti-dovednost-a-veci-ktere-cisla-neukazou)

### SVD

**Singular Value Decomposition: každá matice — bez ohledu na tvar a symetrii — je rotace → škálování se změnou dimenze → rotace.**

„Velké finále" lineární algebry: A = UΣVᵀ, kde U a V jsou rotace (singulární vektory) a Σ nese singulární hodnoty. Geometricky posílá koule na elipsoidy; prakticky stojí za kompresí obrázků (low-rank aproximace) i PCA.

Kde se s tím potkáš: [Lineární algebra vizuálně](teorie/linearni-algebra-vizualne.md)

### Swing

**Prodloužení první a třetí šestnáctiny na úkor druhé a čtvrté — čímž vznikne „push-pull" groove.**

Není to efekt ani „posuň to trochu", je to konkrétní záměna délek dob, a proto se dá zopakovat. Šestnáctinový swing je klíčem k tomu, aby house zněl jako house; doma je taky v jazzu a big bandu. Swingované osminy při větších hodnotách začnou znít jako trioly. Pro generativní herní hudbu je to nejlevnější páka na charakter: **změní žánr, aniž bys sáhl na jedinou notu**.

Kde se s tím potkáš: [Mřížka: takt, dělení a swing](hudba/rytmus.md#mrizka-takt-deleni-a-swing) · [Rejstřík: Předznamenání](#predznamenani) · [Rejstřík: Synkopa](#synkopa)

### Sync marker

**Značka v animaci (typicky došlap L/R), podle které se synchronizují klipy různých délek při blendování.**

Bez markerů se walk/run/sprint v blend space fázově rozjedou a mix „plave". Markery musí mít **stejná jména** napříč klipy (L, R) — stažené animace je často nemají a je potřeba je doplnit ručně podle došlapů.

Kde se s tím potkáš: [Základy pohybu](praxe/pohyb-zaklady.md)

### Tagy

**Štítky hry na obchodní platformě; primárně vstup pro doporučovací algoritmus, ne popis pro zákazníka.**

Vybírají se obráceně, než by člověk čekal: najdi hru se stejným publikem a opiš si její tagy, protože cílem je dostat se v databázi vedle správných her. Nejčastější chyba je použít nejgeneričtější tagy (promarníš místo) — a poznávacím znamením špatných tagů jsou nesourodé hry v sekci doporučení.

Kde se s tím potkáš: [Steam stránka: screenshoty a tagy](teorie/steam-stranka.md)

### TAA

**Temporal anti-aliasing — starší a mnohem levnější sourozenec [TSR](#tsr).**

Naměřený rozdíl ve výchozí scéně UE5: **TSR ~1,7 ms proti TAA 0,15 ms.** Cena je rozmazání v pohybu, takže volba je žánrová: pohodovým hrám a adventurám TAA sedne, rychlé stříleččce nebo závodům ne. Ještě levnější mezistupeň pro stylizované a mobilní projekty je **FXAA**, který ale hrany jen prostorově rozmazává.

Kde se s tím potkáš: [Rozpad ceny výchozí scény](praxe/lehky-render.md#rozpad-ceny-vychozi-sceny-a-cim-ji-nahradit) · [Rejstřík: TSR](#tsr) · [Rejstřík: Screen percentage](#screen-percentage) · [Ze 100 na 200 FPS](praxe/lehky-render.md#ze-100-na-200-fps-co-stalo-za-vypnuti-ve-skutecne-hre)

### Synkopa

**Akcent na nepřízvučnou dobu; hlavní koření rytmické proměny.**

Přesun not z přízvučných dob na „mezidoby" oživí mrtvou melodii. Dobrý rytmus balancuje opakování a proměnu — a synkopa je nejlevnější způsob, jak dodat proměnu.

Kde se s tím potkáš: [Jak psát melodie](hudba/melodie.md)

### Take Recorder

**Nástroj, který nahraje běžící hraní jako sekvenci — a pro měření gameplaye je to past.**

Nahrává **transformy**, takže přehrání sekvence sice pohybuje postavou přesně jako tehdy, ale **nespustí tvůj gameplay kód**. Na vizuální testy a na cinematiky je to správný nástroj; na benchmark funkce, kterou jsi napsal, je to měření něčeho jiného, co vypadá stejně. Řešení: level sequence s **event trackem**, jehož událost tu funkci opravdu zavolá.

Kde se s tím potkáš: [Benchmark z level sequence](praxe/mereni-automaticky.md#benchmark-z-level-sequence-mereni-jako-soucast-prace) · [Rejstřík: Unreal Insights](#unreal-insights)

### Tell

**Signál, kterým se dopředu prozradí, co přijde — nápřah, blik, zvuk, změna pózy.**

Bez tellu není útok výzva, ale loterie: hráč nemá podle čeho se rozhodnout, takže uhýbá naslepo. Tři varianty téhož útoku se stejným nápřahem jsou proto fakticky neuhnutelné. Praktický postup, který se vyplatí: **prototypuj signál dřív než jeho podobu** — barevný obdélník vedle hlavy nepřítele odpoví na otázku „stihne to hráč přečíst?" za pět minut, zatímco nakreslit animaci a teprve pak zjistit, že tell nefunguje, stojí dny.

Kde se s tím potkáš: [Boss se staví z otázek](godot/pripadovka-nepratele.md#boss-se-stavi-z-otazek-ne-z-atributu) · [Obtížnost a výzva](teorie/obtiznost.md)

### Telemetrie

**Sběr dat o tom, co hráči ve hře skutečně dělají — lokálně (čítače, achievementy) i vzdáleně (analytický backend).**

Lokální patro: activity tracker — gameplay tagy hlášené centrální funkci, dispatcher pro odběratele, mapa tag→počet. Vzdálené patro: plugin (TrackEdge) + backend (PostHog): person properties, eventy s vlastnostmi, sessions s trváním, dashboardy. K vydání patří privacy rozvaha (poloha, GDPR). Telemetrie je chování, ne slova — sesterská měna „the gap".

Kde se s tím potkáš: [Telemetrie](praxe/telemetrie.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Tessellation

**Dělení geometrie na jemnější trojúhelníky, aby povrch unesl víc detailu.**

V Mesh Terrainu ve dvou podobách: adaptivní teselace texture modifieru (zjemní síť tam, kde height mapa nese detail, řízeno error tolerancí) a Tessellate režim remesh modifieru. Protiklad k uniformnímu remeshi: adaptivní přístup šetří trojúhelníky, ale hůř se predikuje výsledný tvar. Obecná rada z praxe: hrubé tvarování s teselací vypnutou, detail zapínat cíleně na konci.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Texture modifier s teselací](praxe/mesh-terrain.md#modifikatory-v-rukou-epicu-poradi-vrstev-rovina-pod-poi-a-pcg-ktere-rozmistuje-skaly)

### Texel density

**Kolik pixelů textury připadá na jednotku plochy ve scéně, typicky v pixelech na metr.**

Když mají sousední objekty rozdílnou hustotu, jeden vypadá ostře, druhý rozmazaně a je hned vidět, že k sobě nepatří. Studia proto volí jednu cílovou hodnotu; workshop o kitech pracuje s 512 px na metr, takže kus dlouhý 4 m odpovídá 2K textuře. Hustotu rozbije libovolné škálování kusů. Nízkou hustotu unikátní textury lze dorovnat opakováním tileru v materiálu. Witcher 3 ji v DLC Blood and Wine zdvojnásobil, a proto musel šetřit jinde.

Kde se s tím potkáš: [Kit jako lego: mřížka v metrech](praxe/modularni-kity.md#kit-jako-lego-co-nejmene-kusu-mrizka-v-metrech-a-zoo-na-zkousku) · [Textury pro kit](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen) · [Trim sheet jako systém](praxe/modularni-kity.md#trim-sheet-jako-system-jedna-textura-mnoho-assetu-a-kdy-ne) · [Beauclair: jeden shader na čtvrť](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [Rejstřík: UV mapping](#uv-mapping)

### Texture array

**Sada textur stejné velikosti a formátu uložená jako jeden objekt, ze kterého shader vybírá vrstvu indexem.**

Na rozdíl od atlasu se vrstvy nepřelévají přes okraje a mipmapy fungují pro každou zvlášť. Shader tak drží mnoho sad textur v jednom vzorkovači a vybírá z nich třeba hodnotou z vertex color. Witcher 3 tak oblékal bohatou čtvrť Beauclair: barvu, normálu, roughness i masku sad textur měl v texture arrays. V UE existuje jako asset Texture 2D Array.

Kde se s tím potkáš: [Beauclair: jeden shader na čtvrť](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [Rejstřík: Texture atlas](#texture-atlas) · [Rejstřík: Vertex painting](#vertex-painting)

### Texture atlas

**Jedna textura, ve které leží vedle sebe povrchy pro mnoho objektů nebo částí modelu.**

Snižuje počet materiálů a tím i draw callů: místo dvaceti textur po 128 pixelech jedna 512, ve které si každá stěna vezme svůj výřez. Příbuzný trim sheetu, ale bez jeho pásové logiky — atlas je prostě mozaika. Cenou je ruční práce s UV a nutnost hlídat okraje, aby se sousední výřezy nepromíchaly filtrováním.

Kde se s tím potkáš: [PS1 estetika](praxe/ps1-estetika.md#textura-dela-styl-rozliseni-kontrast-a-nearest) · [Rejstřík: trim sheet](#trim-sheet) · [AC Black Flag: atlas mesh decalů](praxe/env-technika.md#ac-black-flag-resynced-prodat-iluzi-ne-postavit-skutecnost)

### Tileable texture

**Textura, která na sebe navazuje ve všech směrech, takže se dá opakovat přes libovolně velkou plochu (tiler).**

Jedna textura pokryje stěny, podlahy i skály celého prostředí, a proto je základem texturování kitů: nejdřív tilery, pak trimy a unikátní textury jen tam, kde nic jiného nestačí. Slabinou je viditelné opakování, které se rozbíjí vertex paintingem, decaly a sendvičem s trimy. Na kusech postavených na metrové mřížce tiler mezi kusy většinou naváže bez starostí. Neplést s [Tile set](#tile-set) z 2D her.

Kde se s tím potkáš: [Textury pro kit](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen) · [Mortal Shell 2: málo tilerů](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek) · [Rejstřík: Trim sheet](#trim-sheet) · [Rejstřík: Texel density](#texel-density)

### Tile set

**Sada dlaždic, ze kterých se maluje 2D svět; k ní patří pravidla, jak na sebe navazují.**

Počet dlaždic je kompromis. Chtít vlastní obrázek pro každou kombinaci osmi sousedů znamená **256 dlaždic**, takže se v praxi používají menší sady: 15dílná (levná, ale hrany vede středem dlaždice, takže nesedí na mřížku), 47dílná (sedí, ale je jich 47) nebo 16dílná podmnožina. **Dual-grid** ten kompromis obchází dvěma mřížkami posunutými o půl dlaždice — každá dlaždice pak má jen čtyři sousedy, tedy **16 kombinací**. K tile setu se v enginu váží i fyzikální, navigační a occluder vrstvy.

Kde se s tím potkáš: [Dual-grid: 16 dlaždic místo 256](godot/2d-svet.md#dual-grid-16-dlazdic-misto-256) · [Pixel art do Godotu](godot/2d-svet.md#pixel-art-do-godotu-paleta-silueta-a-jedno-nastaveni)

### Time slicing

**Rozložení drahého výpočtu do času: místo každý snímek se počítá každý n-tý.**

Nejlevnější optimalizace, jaká existuje, protože nemění algoritmus — mění jen frekvenci. Hledání cesty počítané stokrát za sekundu srazí hru na 10 FPS; totéž desetkrát za sekundu ji vrátí nad 100, a hráč rozdíl nepozná, protože se cíl za tři setiny sekundy nikam nepřesune. Rozhodovací otázka zní **„jak často se to musí opravdu přepočítat?"** a platí na dohled nepřátel, vzdálenosti, UI i kontrolu podmínek. Nezaměňovat s asynchronním kódem — ten neblokuje, ale nezlevňuje.

Kde se s tím potkáš: [Dvě věci o výkonu, které se pletou](godot/pripadovka-proces.md#dve-veci-o-vykonu-ktere-se-pletou) · [Co skutečně stojí výkon](godot/projekt-a-vykon.md#co-skutecne-stoji-vykon-ne-nody-ale-co-v-nich-bezi-kazdy-snimek)

### Timeline

**Blueprint uzel s křivkami v čase: Play/Reverse/Finished — animace hodnot bez animačního assetu.**

Float track 0→1 + Lerp = pohyb A→B (linear klíče = konstantní rychlost, Auto = ease); looping track 0→360 = rotace. Ping-pong vzor: na Finished přečti Direction enum a zavolej Reverse/Play. Set Timeline Length za běhu mění tempo — délka nad poslední klíč vyrábí pauzu v krajní poloze. Latentní uzel — jen v event graphu, ne ve funkcích.

Kde se s tím potkáš: [Pasti a arénové mechaniky](praxe/pasti-a-mechaniky.md) · [Lerp předmětu do ruky](praxe/interakcni-animace.md#predmet-do-ruky-bez-teleportu-attach-neni-snap-a-dosah-neni-dohled) · [Plošina s pákou](praxe/interakcni-animace.md#contextual-animation-scena-s-rolemi-misto-rucni-choreografie) · [Agent a delaye místo Timeline](praxe/mcp-v-editoru.md#jak-s-agentem-v-editoru-mluvit-presna-jmena-jeden-ukol-a-kontext-ktery-se-vejde)

### Tool set

**Sada nástrojů v Unreal MCP: API, přes které agent sahá na jeden systém editoru, třeba PCG, materiály nebo blueprinty.**

Plugin MCP sám nástroje nemá, dodávají je tool sety v pluginech All Tool Sets a Editor Tool Set. Ve verzi 5.8 je tool set třída, jejíž nástroje jsou statické UFunctions. Reflexe z nich sama vyrobí JSON, takže jdou psát v C++ i v Pythonu. Dobrý tool set je čistý, úplný (getter, setter i výpis), skladebný a vrací chyby, které radí, co dál.

Kde se s tím potkáš: [Vlastní tool set a skill](praxe/mcp-v-editoru.md#vlastni-tool-set-a-skill-api-pro-juniora-a-rada-kolegovi) · [Rozjet MCP](praxe/mcp-v-editoru.md#rozjet-mcp-tri-pluginy-agent-ze-spravne-slozky-a-co-delat-kdyz-nic-nevidi) · [Asistent, ne zázrak](praxe/mcp-v-editoru.md#asistent-ne-zazrak-slovnik-priklady-a-skills-delaji-z-llm-stavitele-sveta) · [Rejstřík: MCP](#mcp)

### Trim Relative Error

**Nastavení Nanite meshe: zahodí všechny detaily pod danou relativní chybou — místo procenta trojúhelníků povolená odchylka tvaru.**

Protože jde o chybu, ne o procento, přizpůsobí se sama různě hustým meshům a hodí se i tam, kde [Keep Triangle Percent](#keep-triangle-percent) škodí — hlavně na listí, kde ubírání po procentech rozpojí větve. V příkladu z kapitoly o Nanitu stačila hodnota 0,1 bez viditelné ztráty a 0,5 už byla moc; na vlastních meshích je ale potřeba hodnoty ověřit.

Kde se s tím potkáš: [Nanite a velikost balíčku](praxe/nanite-do-hloubky.md#nanite-a-velikost-balicku-data-ktera-se-nikdy-nevykresli) · [Rejstřík: Nanite](#nanite)

### Triplanar projection

**Promítnutí textury ze tří os světa místo UV, s prolnutím podle normály, takže textura sedí na jakkoli natočený tvar.**

Shader vzorkuje texturu shora, zepředu a z boku a míchá výsledky podle toho, kam plocha míří. Hodí se na skály, terén a světovou projekci sněhu nebo mechu přes všechno, protože nepotřebuje UV a nedělá švy. Cenou jsou tři vzorkování místo jednoho a rozmazané přechody na šikmých plochách. V UE je na to material function WorldAlignedTexture.

Kde se s tím potkáš: [Organický kit a spoje: světová projekce](praxe/modularni-kity.md#organicky-kit-a-spoje-zaborit-nechat-rust-od-zdroje-zakryt-sev) · [Mortal Shell 2: material functions](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek) · [Rejstřík: Material function](#material-function)

### Tritón

**Interval přesně uprostřed oktávy — dokonalé rozpůlení kruhu dvanácti tónů.**

Notoricky nestabilní dvojice, která „se chce ohnout a rozvést". Zajímavé je, že jeho pověst nejdisonantnějšího intervalu je z velké části kulturní: v grafu disonance na tom není o moc hůř než malá sexta. A obecnější poučení, které z něj plyne: **na kruhu tónů znamená symetrie nestabilitu**, ne stabilitu — dokonale pravidelný tvar (tritón, zvětšený akord, zmenšený akord) nemá kam gravitovat.

Kde se s tím potkáš: [Kvintový kruh je ve skutečnosti spirála](hudba/fyzika-souzvuku.md#kvintovy-kruh-je-ve-skutecnosti-spirala) · [Jiné alikvóty, jiné stupnice](hudba/fyzika-souzvuku.md#jine-alikvoty-jine-stupnice) · [Rejstřík: Konsonance](#konsonance)

### Tónina

**Domovská stupnice skladby — tón a stupnice, ke kterým vše tíhne.**

V piano rollu ji nastavíš přes scale highlighting; „špatné" tóny pak zmizí z dohledu a skládáš skoro naslepo po zvýrazněných. C dur a A moll mají stejné tóny, liší se právě cítěným domovem.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Tone mapper

**Převod HDR hodnot renderu na to, co zobrazí monitor — a hlavní příčina toho, čemu se říká „unreal engine look".**

UE5 posílá ve výchozím stavu **ACES**, filmový tone mapper navržený pro záběry, které se pak barevně korigují v postprodukci. Ve hrách ta postprodukce nikdy nepřijde, a ACES má návyk, který v reálném čase vadí: **sytě jasné barvy netlačí plynule do bílé, ale posouvá je** — odtud vymyté šedivé střední tóny a plochý přechod. Alternativa, kterou přejala Blenderová komunita, je **AGX**: jas přechází do bílé přirozeněji a detail v normálových mapách a albedu je čitelnější. Nasazuje se **zásahem do shaderu enginu** (`PostProcessTonemap.usf`), takže se to týká všech projektů na dané verzi enginu — a mění to pracovní postup, protože světla s AGX rychleji zesvětlují.

Kde se s tím potkáš: [Tone mapper: odkud je „unreal engine look"](praxe/osvetleni.md#tone-mapper-odkud-je-unreal-engine-look) · [Rejstřík: EV100](#ev100)

### Toon shading

**Stylizované stínování v ostrých pásech (cel shading) — od 5.8 vestavěný shading model přes Substrate Toon BSDF.**

Toon Profile asset řídí diffuse/specular rampu (počet, pozice a tvrdost pásů) a offset textury (halftone, malířský rozpad). Není to post-process — nasazuje se per materiál; největší výhoda proti ručním cel shaderům: správně reaguje na barevná světla, více světel i Lumen.

Kde se s tím potkáš: [Materiály](praxe/materialy.md)

### Trace channel

**Přepínač, kterým se v Unrealu volí, co se do trasovacího záznamu vůbec zapisuje.**

Kanály jsou po kategoriích (výkon, paměť, kontext, systémy) a nad nimi jsou **předvolby** podle scénáře, které se dají definovat v `ini` a sdílet v týmu. Je to hlavní páka na **šířku pásma**, a ta je důležitější, než se čeká: nestíhá-li worker vlákno data odesílat, roste spotřeba paměti a po dosažení limitu se **aplikace zastaví** — žádné plynulé zhoršení. Tři pravidla: rozhodni se pro scénář předem a nemíchej je (podrobné sledování paměti zkreslí měření výkonu), nezapínej kanály, o kterých nevíš, co dělají, a používej předvolby.

Kde se s tím potkáš: [Tracing bez utopení](praxe/mereni-automaticky.md#tracing-bez-utopeni-kanaly-sirka-pasma-a-scenare) · [Rejstřík: Unreal Insights](#unreal-insights)

### Trajektorie

**V Motion Matchingu spočítaná historie a predikce pohybu postavy — modrá budoucnost, červená minulost.**

Každý frame se z rychlosti a vstupu predikuje, kde postava bude (+0,35/0,7/1 s) — a proti tomu se matchují animace. Nezaměňovat s traversal (detekce překážek) ani s intentem (co hráč chce = vstup; trajektorie = co se asi stane). Generuje ji Character Trajectory komponenta nebo Pose Search Generate Trajectory; debug: `a.CharacterTrajectory.Debug 1`. Expozice trajektorie gameplayi umí předpovědět zastavení či budoucí rychlost.

Kde se s tím potkáš: [MM základy](praxe/mm-zaklady.md)

### Traversal

**Překonávání překážek (vault, mantle, hurdle) — v GASP detekce hran + výběr animace podle stavu a překážky.**

Vzor z GASP: spline/trace detekce překážky → chooser (hurdle/vault/mantle podle typu a výšky) → montáž s Pose Search Branch In oknem + motion warping na hranu (get-to-bone, interaction transform přes blueprint channel ve schématu). Funguje jen na Traversable blocích; komunitní komponenty (AC_TraceTraversal) ho naučí šplhat i na běžnou geometrii — zákaz per objekt tagem.

Kde se s tím potkáš: [Systémy nad MM](praxe/mm-systemy.md) · [GASP](praxe/gasp.md) · [Parkour postaru](praxe/parkour-vault.md) · [MM základy](praxe/mm-zaklady.md)

### Triáda

**Nejzákladnější akord ze tří tónů: základ, tercie a kvinta.**

Rozestupy určí barvu: 4+3 půltóny = durová, 3+4 = mollová, 3+3 = zmenšená. Postavíš-li triádu na každém stupni stupnice, dostaneš pevný vzorec durových, mollových a zmenšených akordů.

Kde se s tím potkáš: [Základy hudební teorie](hudba/hudebni-teorie-zaklady.md)

### Trigger volume

**Neviditelná zóna v levelu, která při vstupu hráče (či jiné entity) spustí událost.**

Základní nástroj skriptovaných momentů: rozhovor NPC na tržišti, změna hudby, otevření cesty, cinematika na správném místě. Designové pravidlo: nejdřív otázky „jaký zážitek, jaká emoce, jaká informace, jaká další akce?" — trigger je jen doručovací mechanismus. V UE odpovídá trigger box/volume s overlap eventy (viz praxe: interakce bez Event Ticku).

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md) · [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md) · [Cutscéna: spouštěč, který nezlobí](praxe/cutsceny.md#cutscena-ktera-vrati-hru-tam-kde-skoncila)

### Trim sheet

**Sdílená textura z pásů detailů (římsy, sokly, hrany), po kterých se mapují UV mnoha různých assetů.**

Jedna textura obslouží stovky modelů — draw calls i VRAM klesají řádově. Varianta baked bevel (TLOU): modely hard-edge v 90° úhlech a všechno zaoblení dodá normal mapa trimu. Bonusové triky: UV přeložené přes roh trimu = falešný bevel bez geometrie, bílý trim + color parametr = přebarvitelnost. Základ produkce od The Ascent po San Francisco 1:1.

Trim se navrhuje s kitem, ne po něm. Workshop o kitech ho staví přímo z geometrie kitu, a aby zkosení na sebe navazovala, musí se potkat hrany stejného druhu. Pro unikátní hero asset a nepravidelné organické tvary obvykle dává větší smysl vlastní textura.

Kde se s tím potkáš: [Breakdowny](praxe/env-breakdowny.md) · [Trim z vlastní geometrie](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen) · [Trim sheet jako systém](praxe/modularni-kity.md#trim-sheet-jako-system-jedna-textura-mnoho-assetu-a-kdy-ne) · [AC Black Flag: lodě](praxe/env-technika.md#ac-black-flag-resynced-prodat-iluzi-ne-postavit-skutecnost)

### Trunk-based development

**Vývoj, ve kterém všichni odevzdávají do jedné hlavní větve často a po malých krocích, místo dlouhých oddělených větví.**

Konflikty se řeší průběžně a hlavní větev je pořád blízko hratelnému stavu. Potřebuje to ale automatické buildy a testy, které rozbití chytí hned. IO Interactive tak u 007 First Light skládá nový build editoru zhruba po každých 10 až 15 odevzdáních, tedy každých 15 až 30 minut.

Kde se s tím potkáš: [007 First Light: iterace jako zásada](praxe/env-technika.md#007-first-light-editor-ve-kterem-se-vsechno-sklada-z-entit-a-nikdo-neceka) · [Rejstřík: Hot reload](#hot-reload)

### TSR

**Temporal Super Resolution — upscaler UE5; nejčastější viník „rozmazané" vody a jemných pohyblivých detailů.**

Viewport typicky běží na 80–90 % screen percentage a TSR dopočítává — pohyblivá hladina pak ghostuje a smearuje. Diagnóza: screen percentage 100 % (či 125–200 %) a porovnat. Léčba: jiná AA metoda přes console variable, tonemapper sharpen 0,5–1, a hlavně vyhnout se upscalingu, kde to jde.

Kde se s tím potkáš: [Nástroje: EasyWaterscape](praxe/nastroje-voda.md) · [Ze 100 na 200 FPS](praxe/lehky-render.md#ze-100-na-200-fps-co-stalo-za-vypnuti-ve-skutecne-hre) · [Stopy v TSR a Output Depth and Velocity](praxe/megalights.md#attenuation-radius-jako-hlavni-paka-pocitej-prekryvy-ne-svetla)

### Tři C

**Character, camera, controls — trojice, kterou žánr definuje: koho ovládáš, odkud se díváš, čím to řídíš.**

Průmyslový termín; ve velkých studiích existují vyhraněné 3C designérské role. „Platformer" nebo „RTS" v hlavě okamžitě vykreslí všechny tři C — proto jsou to žánry; „roguelike" nevykreslí žádné — proto je to mód.

Kde se s tím potkáš: [Žánry očima designéra](teorie/zanry.md)

### Tutorial hell

**Smyčka „sleduju tutoriály, umím je zopakovat, ale sám nepostavím nic" — nejčastější past učení enginu.**

Sledování není učení. Útěk je vždycky stejný: po každém tutoriálu zavřít video a postavit něco malého vlastního s tím, co ses právě naučil. Mezera mezi následováním kroků a vlastním myšlením se zavírá jen malými dokončenými projekty — dveře, mince, postava s damage.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md) · [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Jak se učit z GASP](praxe/gasp.md#posledni-update-pro-ue5-sample-ne-framework)

### Typografie

**Řemeslo práce s písmem: volba řezů, jejich role v hierarchii textu a pravidla, kdy se který používá.**

Praktické minimum pro hru: dva fonty s jasnou rolí (nadpisy, tělo), a každý další styl — tučné, kurzíva, jiný řez — jen s důvodem, který platí v celé hře. Kurzíva vyhrazená pro flavor text hráči napoví, že tohle nemusí číst kvůli hraní; tučné klíčové slovo naopak říká, že tohle je mechanika.

Kde se s tím potkáš: [Typografie](teorie/typografie.md) · [Art specializace: UI](teorie/art-specializace.md)

### Two-loop rule

**Aranžérské pravidlo: každé dva loopy hlavního nástroje uděláš nejvýš dvě změny.**

Změna = přidat nástroj, ubrat nástroj, přidat výraz, ubrat výraz. Mechanické lešení, které rozhýbe loop v píseň, aniž bys musel „vymyslet aranž".

Kde se s tím potkáš: [Aranžmá: z loopu skladba](hudba/aranz.md)

### Type 2 fun

**Zábava, která bolí teď a těší až ve vzpomínce: námaha a peril, na které jsi hrdý.**

Z třístupňové Fun Scale (Newberry): Type 1 baví hned, Type 2 až zpětně (výstup na horu, soulsovka), Type 3 je „zábava, co se pokazila" — a rage hry ji vyrábějí schválně. Co je pro jednoho Type 2, je pro jiného Type 3; volba publika, ne kvality.

Kde se s tím potkáš: [Zábava: taxonomie a pilíře](teorie/zabava.md) · [Obtížnost a výzva](teorie/obtiznost.md)

### UMG

**Unreal Motion Graphics — systém uživatelského rozhraní v UE: widget blueprinty skládané v designeru z panelů, tlačítek, textů a obrázků.**

Widget se zobrazí buď přes obrazovku (`Add to Viewport`), nebo ve světě přes [Widget Component](#widget-component). Kód widgetu žije v jeho event graphu, kde Event Construct hraje roli BeginPlay. Property bindings se vyhodnocují každý snímek a Epic radí je v projektu zakázat.

Kde se s tím potkáš: [UI ve světě](praxe/ui-ve-svete.md) · [Prvních 16,66 ms se rozdává v CL1](praxe/rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Hádanka ze stavebnice: HUD](praxe/pasti-a-mechaniky.md#hadanka-ze-stavebnice-spinac-nic-nezna-a-level-se-nesmi-dat-rozbit)

### Unison

**Navrstvení více kopií téže vlny na jednu notu; rozšíří zvuk do sterea.**

Tři noty × 10 hlasů unisonu = 30 pil přes sebe. Nejvíc těží pila. Slavný supersaw je pila s vysokým unisonem protažená filtrem.

Kde se s tím potkáš: [Syntéza zvuku od nuly](hudba/synteza-zvuku.md)

### Unreal Insights

**Profiler pro CPU stranu snímku: co dělá herní a render vlákno, po funkcích a v čase.**

Chodí se sem, když `stat unit` ukáže vysoký **game** nebo **draw** — obojí je CPU. Praktická pravidla: spustit Insights **dřív než hru** (pozdní připojení může data poškodit), profilovat **development build** (v testu je většina informací vystřižená) a držet `trace.stop`, dokud hledáš to správné místo, jinak vyrobíš gigabajty nepoužitelných dat. Značky `trace bookmark` a `trace screenshot` pomůžou najít konkrétní snímek; kanál `counters` přidá čísla, která se jinak shánějí těžko — paměť, počet draw callů po cullingu, počet `UObject`ů, aktivní fyzikální tělesa.

Kde se s tím potkáš: [Rozhodovací strom](praxe/profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Reprodukovatelný test](praxe/profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic) · [CVD na stejném Trace](praxe/debugging.md#chaos-visual-debugger-zevnitr-faze-solveru-kontakty-a-klient-vedle-serveru)

### User Parameter

**Parametr Niagara systému, který jde nastavit zvenčí, z blueprintu nebo kódu, a moduly v emitterech ho čtou.**

Nastavuje se typicky přes Set Niagara Variable na komponentě, kterou vrátí spawn. Jeden systém tak může reagovat na hru, třeba škálovat počet částic podle rychlosti postavy. Jméno parametru musí v blueprintu přesně sedět.

Kde se s tím potkáš: [Částice podle povrchu](praxe/footsteps.md#castice-podle-povrchu-trace-z-chodidla-pooling-a-sila-podle-rychlosti) · [Rejstřík: HLSL](#hlsl)

### User story

**Popis funkce jako kroky uživatele: co vidí a co dělá — ne jak je to naprogramované.**

Termín ze softwarového vývoje, který se hodí i do GDD: pitch Diabla obsahuje pasáž „hráč vede postavu po cestě do opuštěného chrámu, počítač vygeneruje první patro…" — krok za krokem zážitek hráče. Dobrý test srozumitelnosti návrhu: jde odvyprávět jako user story?

Kde se s tím potkáš: [GDD: dokument není smlouva](teorie/gdd.md)

### USP

**Unique selling point: co má jen tvoje hra — důvod koupit ji, a ne konkurenci.**

Uklidňující lekce z historie: USP nemusí existovat od začátku. GTA vyrostlo z tech dema o streamování velkého města a všechen „GTA flavor" se nastěhoval po letech; unikátnost se do projektu dá dovézt i pivotem nebo škrtem.

Kde se s tím potkáš: [GDD: dokument není smlouva](teorie/gdd.md) · [Co prodává](teorie/co-prodava.md)

### Utility AI

**Rozhodovací rámec, kde si každý úkol spočítá skóre a spustí se ten s nejvyšším.**

Není to plugin ani kód, ale způsob návrhu — a nenahrazuje behavior trees ani state trees, používá je jako výkonnou vrstvu. Skóre není konstanta, ale součet důvodů (počet nepřátel, zdraví, vzdálenost, povaha), takže z týchž úkolů vznikne se zbabělcem jiné chování než s veteránem. Škáluje tam, kde by strom podmínek přestal být čitelný.

Kde se s tím potkáš: [Základy AI](praxe/ai-zaklady.md#utility-ai-rozhodovani-podle-skore-misto-vetveni) · [State Trees](praxe/state-trees.md) · [Rejstřík: GOAP](#goap) · [Paměť utility v Lords of the Fallen](praxe/ai-ve-velkem.md#reakce-vedle-stromu-co-se-muze-stat-v-kazdem-stavu-nepatri-do-zadne-vetve) · [Aggro](praxe/ai-ve-velkem.md#kdo-utoci-a-kdo-ceka-aggro-skore-a-bojove-role)

### UV mapping

**Předpis, která část 2D textury se natáhne na kterou plochu modelu.**

U a V jsou souřadnice v textuře (obdoba X a Y), takže UV mapa je model rozstřižený a rozložený do roviny. Automatické rozbalení je rychlé, ale u stylizovaných assetů se UV umisťují ručně — a pak je to samo o sobě tvůrčí rozhodnutí: tatáž geometrie s jinými UV je jiný objekt.

Kde se s tím potkáš: [Z fotky herní asset](praxe/foto-do-assetu.md#narovnat-obtahnout-promitnout) · [PS1 estetika](praxe/ps1-estetika.md#model-a-uv-po-stenach-krychle-quady-a-fotky-narovnane-do-obdelniku) · [Rejstřík: trim sheet](#trim-sheet) · [Rozbalení na mřížce a na trim](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen) · [Hrany, které navazují](praxe/modularni-kity.md#trim-sheet-jako-system-jedna-textura-mnoho-assetu-a-kdy-ne)

### UX

**User experience: informační architektura hry — kde informace bydlí a kolika kroky se k nim hráč dostane.**

Předchází UI: nejdřív se mapuje cesta hráče a minimalizuje počet nutných akcí, teprve pak se staví vizuál. U malých týmů je to jedna role, a právě proto se vyplatí držet obě zadání oddělená — jinak se optimalizuje vzhled obrazovky, která neměla vzniknout.

Kde se s tím potkáš: [Art specializace: UI a UX](teorie/art-specializace.md) · [První dojem](teorie/prvni-dojem.md)

### Value pass

**Krok blockoutu, ve kterém dostanou plochy různé odstíny šedi, aby se oddělily tvary a scéna získala hloubku.**

Na rozdíl od jednotné 50% šedé nutí rozhodnout, co má být světlejší a co tmavší. Autor rozboru pipeline Naughty Dog k tomu radí oddělit vodorovné plochy od svislých. Naughty Dog použil kolem deseti odstínů, pro začátek stačí tři nebo čtyři. Hodnota, tedy šerosvit, je nejsilnější typ kontrastu, a proto ji blockout drží i bez barvy. Po value passu přichází průchod barvy.

Kde se s tím potkáš: [Hybridní blockout](praxe/blockout.md#hybridni-blockout-hodnoty-a-barva-driv-nez-materialy) · [Zastav, omez, porovnej: šedá jako hodnota](praxe/blockout.md#zastav-omez-porovnej-blockout-ktery-se-da-precist) · [Rejstřík: Blockout](#blockout)

### Vertex painting

**Malování hodnot do vrcholů meshe (vertex color), podle kterých materiál prolíná vrstvy, třeba kámen, mech a špínu.**

Každý vrchol nese až čtyři kanály (RGBA) a materiál je čte jako masky, takže stejný mesh bez nových textur vypadá na každém místě jinak. Přechod je ale jen tak jemný, jak hustá je geometrie, a proto mají modely určené k malování plochy rozdělené i tam, kde by tvar vrcholy nepotřeboval. Aby přechod nebyl jen rozmazaný, míchá se často podle výškové mapy (HeightLerp), takže štěrk vyleze z bláta nejdřív na hrbolech. V UE se maluje v Mesh Paint módu nebo v Modeling Tools.

Kde se s tím potkáš: [Nanite displacement](praxe/materialy.md#nanite-displacement-relief-malovany-vertex-colorem) · [Textury pro kit](praxe/modularni-kity.md#textury-pro-kit-tilery-trimy-a-masky-dve-textury-na-kamen) · [Trim sheet jako systém](praxe/modularni-kity.md#trim-sheet-jako-system-jedna-textura-mnoho-assetu-a-kdy-ne) · [Organický kit a spoje](praxe/modularni-kity.md#organicky-kit-a-spoje-zaborit-nechat-rust-od-zdroje-zakryt-sev) · [Beauclair: jeden shader na čtvrť](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [AC Black Flag: páry materiálů](praxe/env-technika.md#ac-black-flag-resynced-prodat-iluzi-ne-postavit-skutecnost) · [Naughty Dog: hustota geometrie](praxe/env-breakdowny.md#naughty-dog-shadery-misto-polygonu-a-nastroj-misto-modelovani)

### Virtual Heightfield Mesh

**Plugin a komponenta, která podle výšky z runtime virtual texture vyrobí hustou geometrii terénu.**

Potřebuje RVT volume se stejnou polohou a velikostí a MinMax texturu, která se postaví v jejích detailech. Materiál ji může dál posouvat world position offsetem, a proto se hodí na deformace typu stopy ve sněhu. Je to samostatný mesh nad terénem, ne úprava samotného landscape.

Kde se s tím potkáš: [Stopy do hloubky](praxe/footsteps.md#stopy-do-hloubky-render-target-jako-platno-pod-postavou) · [Rejstřík: Runtime Virtual Texture](#runtime-virtual-texture)

### Visual blocker

**Prvek levelu, který záměrně zkrátí průhled, třeba budova, zeď nebo zatáčka, aby řídil, co hráč vidí, a tím i co se musí načíst.**

Dlouhé průhledy jsou drahé, protože engine musí vykreslit a mít v paměti všechno, co je vidět. Clona je přeruší a dá streamování čas nahrát další část. Částečná clona nechá něco prosvítat, takže hráč ví, že tam něco je, a navíc schová doskakování LODů. Dobře postavená clona je zároveň level design: rámuje výhled a vede k orientačnímu bodu. Úzké průchody v Mortal Shell 2 mají stejný úkol.

Kde se s tím potkáš: [Beauclair: clony](praxe/modularni-kity.md#beauclair-500-mb-textur-na-cele-mesto-orientacni-body-clony-a-jeden-shader-na-ctvrt) · [Mortal Shell 2: výkon začíná u designu](praxe/modularni-kity.md#mortal-shell-2-spickovy-vzhled-od-triceti-lidi-malo-materialu-a-hodne-masek) · [Rejstřík: Landmark](#landmark) · [Rejstřík: Occlusion culling](#occlusion-culling) · [Rejstřík: Level streaming](#level-streaming)

### Visual Logger

**Nahrávač hodnot a ladicích tvarů v čase (Tools → Debug → Visual Logger); po hře se dá procházet po časové ose.**

Zápisy se třídí do kategorií a dají se filtrovat; mimo text umí i tvary a segmenty, ze kterých jde poskládat graf hodnoty přímo v levelu. Odpovídá na otázku „jak se to vyvíjelo", na kterou print string neumí. Nejbližší příbuzný je Chaos Visual Debugger pro fyziku.

Kde se s tím potkáš: [Ladění: čtyři otázky, čtyři nástroje](praxe/debugging.md#ctyri-otazky-ctyri-nastroje-od-print-stringu-po-visual-logger) · [Chaos Visual Debugger](praxe/gpu-pruchod.md#chaos-visual-debugger-rentgen-fyziky)

### Volume Sampler

**PCG uzel, který vyplní objem body v mřížce voxelů.**

Sám dá plnou kostku bodů. S World Volumetric Query jako vstupem nechá jen body, které se překrývají se světem v daném collision channelu, a raycast je pak přichytí na povrch. V jiných grafech slouží jako výřez, třeba pro mýtinu z blocking volume.

Kde se s tím potkáš: [Podlaha, stěny a strop jedním grafem](praxe/pcg-liany.md#podlaha-steny-a-strop-jednim-grafem-volumetric-sampling-misto-mesh-sampleru) · [Mýtiny a cesty](praxe/pcg-vegetace.md#mytiny-a-cesty)

### Voxel

**Objemový pixel: buňka pravidelné 3D mřížky, která nese hodnotu, třeba jestli je v ní hmota.**

Voxelové terény umí jeskyně a převisy. Podle Epicu jsou ale v podstatě 3D height mapa se stejnými limity rozlišení a mřížky a k renderu se stejně převádějí na trojúhelníky. Proto Mesh Terrain sází rovnou na trojúhelníkové meshe. V PCG se se slovem potkáš u voxel size Volume Sampleru.

Kde se s tím potkáš: [Proč trojúhelníky a ne voxely](praxe/mesh-terrain.md#proc-trojuhelniky-a-ne-voxely-mesh-partition-od-zdroje-po-runtime) · [Rejstřík: Volume Sampler](#volume-sampler) · [Algoritmy, které staví herní světy](teorie/algoritmy-prehled.md#algoritmy-ktere-stavi-herni-svety)

### VSync

**Synchronizace výměny obrazových bufferů s obnovovacím cyklem monitoru — buď žádné trhání, nebo nejnižší latence.**

Bez VSyncu se buffery vymění uprostřed vykreslování a snímek se rozdělí (**tearing**); s VSyncem se čeká na konec cyklu. Vypnutý VSync dává nižší [vstupní latenci](#input-latency), ale kromě trhání ubere i schopnost potrubí pohltit zásek. Většina konzolových her ho má zapnutý. Praktické doporučení z Epicu: **zapnout ve výchozím stavu a nechat hráči možnost vypnout.** Bonus: proměnná obnovovací frekvence (VRR/G-Sync/FreeSync) se v Unrealu zapíná právě tím, že necháš VSync zapnutý — o ostatní se stará hardware hráče.

Kde se s tím potkáš: [Snímek není fronta](praxe/frame-pacing.md#snimek-neni-fronta-je-to-potrubi) · [Rejstřík: Frame time](#frame-time)

### Value chain

**Hodnotový řetězec (Dan Cook): smysl a zábavnost sběrné činnosti nedává činnost sama, ale její zamýšlené použití dál v řetězci.**

Sbírání klacíků nudí, dokud z nich hráč nestaví něco, co sytí fantazii hry — pak se každé rozhodnutí „co sebrat" stává plánováním. Prakticky: nudnou mechaniku neoživuj pozlátkem, dej jí destinaci. Cíl řetězce zpětně obarvuje všechny jeho články.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Vektor

**Dvojice/trojice čísel se dvěma čteními: bod v prostoru (pozice), nebo směr s velikostí (velocity, síla).**

Rozlišení užití chrání před nesmysly: pozice + vektor = nová pozice, pozice − pozice = vektor „odsud tam", pozice + pozice = nesmysl. Z pár operací padá celý pohyb (Eulerova integrace: pozice += velocity·dt) i dotazy na svět (dot product).

Kde se s tím potkáš: [Matematika pro gamedev](teorie/matematika-pro-gamedev.md)

### Value curve

**Profil hry přes dimenze appealu: na čem stojí, na čem ne — a s kým se tím pádem vlastně měří.**

Rozepiš, co hru prodává (téma, mechanický hook, atmosféra…), oskóruj důležitost a polož vedle konkurence: klon trefující stejné kolonky nemá důvod existovat. Lepší 1–2 výjimečnosti (jedna neobvyklá) než všechno na sedm z deseti.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md) · [Rady z praxe: idea iceberg](teorie/rady-z-praxe.md)

### Version control

**Verzování projektu (typicky Git): každá změna se ukládá jako commit, ke kterému se lze kdykoli vrátit.**

Dvě služby: záchranné lano z každé katastrofy a viditelná historie pokroku (protilék na „nic nestíhám"). Zásada zrnitosti: commituj malé celky s popisnou zprávou — velký commit se špatně popisuje, vrací i slučuje. UE specifika: Blueprinty jsou binární (diff neuvidíš, zpráva je vše), na velké assety Git LFS, v editoru vestavěná integrace Revision Control.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md) · [Rejstřík: File locking](#file-locking)

### Vizuální hierarchie

**Uspořádání scény tak, aby nejdůležitější informace byla nejsnáze vidět.**

Vzniká kontrastem — v tvaru, velikosti, barvě, saturaci i míře detailu. Kontraintuitivní jádro: fokus se nedělá zvýrazněním jednoho místa, ale potlačením všech ostatních (na šachovnici, kde má stejný kontrast všechno, oko nemá kde přistát). Postup je dvoukrokový: nejdřív informační hierarchie (co je jak důležité), pak její překlad do vizuálních prostředků.

Kde se s tím potkáš: [Herní art: pipeline](teorie/art-pipeline.md) · [Vizuální komunikace](teorie/vizualni-komunikace.md) · [Prostor a hranice](teorie/prostor-a-hranice.md)

### Vertical slice

**Reprezentativní výsek hry ve finální kvalitě — brána mezi prototypem a plnou produkcí.**

Ne nutně začátek hry: libovolných 5–60 minut zážitku, na kterém se poprvé potkají mechaniky z prototypu, art style a tón. Otázka, na kterou odpovídá: nadchne lidi reprezentativní ukázka natolik, aby se vyplatilo vyrábět zbytek obsahu? U komplexních her se skládá z ~60 % žánrových standardů a ~40 % inovací — testovat jde jen to nové.

Kde se s tím potkáš: [Prototypování a vertical slice](teorie/prototypovani.md) · [Základy designu](teorie/zaklady.md) · [Zápisky: cut line](zapisky/cut-line.md)

### Virtual texture stack

**Počet unikátních UV kombinací v materiálu — cena zpětné vazby virtuálních textur se počítá na stack, ne na texturu.**

Tři různá dláždění znamenají tři stacky, protože pro každý se musí zvlášť vyhodnotit, které mipy a dlaždice nahrát. Vzorkovat víc textur toutéž UV kombinací stack **nepřidá**; dát normálce vlastní dláždění ano. Praktické pravidlo při stavbě master materiálu: sdílej UV kombinace, kde to jde, a nové zaváděj vědomě.

Kde se s tím potkáš: [Virtualizace](praxe/gpu-pamet.md#virtualizace-kniha-ze-ktere-ctes-jen-otevrenou-stranku) · [Rejstřík: Virtual texture](#virtual-texture)

### Virtual bone

**Kost existující jen v enginu — přidá se na skeleton (Add Virtual Bone) bez re-exportu z DCC nástroje.**

Sleduje transform zdrojové kosti vůči jiné; typické použití: IK cíle (foot IK pro skeleton, který IK kosti nemá — MetaHuman) a odvozené sockety. Rychlá cesta, jak cizímu skeletonu doplnit, co rig očekává.

Kde se s tím potkáš: [MetaHuman v praxi](praxe/metahuman.md)

### Virtual Shadow Maps

**Stínový systém UE5 navržený pro Nanite a Lumen — vysoké rozlišení bez ručního ladění kaskád.**

Nahrazuje klasické cascaded shadow maps: stíny se počítají po dlaždicích a v rozlišení, které odpovídá tomu, co je vidět. Prakticky to znamená ostré stíny zblízka i v dálce bez typického přeskakování kaskád. Je to doporučené nastavení všude, kde běží Nanite — s nímž si naopak ray traced shadows nerozumí.

Vedle MegaLights zůstávají správnou volbou pro slunce. Ray-traced slunce by na velké scéně potřebovalo velmi dlouhý dosah paprsků a jasné směrové světlo by MegaLights přetížilo.

Kde se s tím potkáš: [Osvětlení: malovat světlem](praxe/osvetleni.md#malovat-svetlem-scena-slozena-z-falesnych-svetel) · [Rejstřík: Nanite](#nanite) · [Slunce bez MegaLights](praxe/megalights.md#slunce-bez-megalights-silne-svetlo-spolkne-rozpocet)

### Virtual texture

**Textura rozsekaná na stránky, které se streamují jen tam, kam se kamera dívá — „Nanite pro textury".**

Pevný pool stránek ve VRAM: při přeplnění nejhůř rozmazání, nikdy out-of-memory. Ulevuje CPU (méně unikátních materiálů) i paměti, daní je page table indirekce — extra GPU čas na každý přístup, takže ne na všechno. Ideální pro obří plochy s kritickým detailem; runtime virtual textures navíc pohánějí blending terénu.

Kde se s tím potkáš: [Textury a DLSS](praxe/textury-a-dlss.md) · [Breakdowny](praxe/env-breakdowny.md) · [RVT na Mesh Terrainu](praxe/mesh-terrain.md#proc-trojuhelniky-a-ne-voxely-mesh-partition-od-zdroje-po-runtime) · [RVT pro Virtual Heightfield Mesh](praxe/footsteps.md#stopy-do-hloubky-render-target-jako-platno-pod-postavou)

### Voice leading

**Vedení tónů tak, aby přechody mezi akordy byly co nejjemnější (vedení hlasů).**

Vyhledej tón, který „trčí" a ruší tok, a schovej ho tak, aby sousední akordy sdílely co nejvíc společných tónů. Když akordy plynou hladce, emoce je „z jiného světa".

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Voicing

**Způsob, jak rozmístíš tóny akordu — v jakém pořadí a oktávách znějí.**

Základní tvar (root–tercie–kvinta natěsno) zní basicky; zvedneš-li jednu notu o oktávu, dostaneš otevřený voicing s prostornějším zvukem. Stejné noty, jiný dojem — páka, kterou začátečníci přeskakují.

Kde se s tím potkáš: [Akordy a harmonie](hudba/akordy-a-harmonie.md)

### Volumetric fog

**Objemová mlha: světlo se rozptyluje v „hustotě vzduchu" — paprsky, god rays a atmosféra s hloubkou.**

Zapíná se na Exponential Height Fog; tvar řídí scattering distribution, start distance a height falloff. Materiály s domain Volume do ní kreslí vlastní objemy (mlha Silent Hill 2). Kvalita: r.VolumetricFog.GridPixelSize (default 8, nižší = jemnější) a GridSizeZ (128 → 256/512, ten dražší).

Kde se s tím potkáš: [Osvětlení](praxe/osvetleni.md) · [Stavba prostředí](praxe/env-tvorba.md) · [Podíl světla v mlze](praxe/megalights.md#svitidlo-z-vic-svetel-odraz-mlha-a-stin-se-ladi-zvlast) · [Mlha, která rozmaže záři](praxe/megalights.md#expozice-ktera-drzi-kalibrace-local-exposure-a-dva-modely-svetla)

### Oblique

**Perspektiva, ve které je scéna nakloněná tak, že vidíš horní i boční stranu objektů.**

Perspektiva her jako Harvest Moon nebo Stardew Valley — není to čistý pohled shora, ale ani izometrie. Rozdíl proti izometrii je v tom, jak se osy sbíhají; prakticky se volí tam, kde je potřeba čitelný půdorys a zároveň rozpoznatelné postavy zpředu.

Kde se s tím potkáš: [2D vizuál: izometrie](teorie/2d-vizual.md)

### Widget Blueprint

**Asset UMG, který spojuje vzhled widgetu (designer) s jeho logikou (graph).**

Prvek, na který chceš z kódu sáhnout, musí mít zaškrtnuté Is Variable. Kotvy a alignment drží rozložení při změně rozlišení. Hotový widget se přidá do viewportu, nebo se dá do Widget Component ve světě.

Kde se s tím potkáš: [Menu jako předmět ve scéně](praxe/ui-ve-svete.md#menu-jako-predmet-ve-scene-widget-na-televizi-a-virtualni-mys) · [Health bar nad hlavou](praxe/ui-ve-svete.md#health-bar-nad-hlavou-screen-space-ukazatel-z-materialu-a-dojezd-poskozeni) · [Rejstřík: Anchor (UI)](#anchor-ui)

### Widget Component

**Komponenta, která zobrazí UMG widget ve světě — na ploše ve scéně (World), nebo nad aktérem čelem ke kameře (Screen).**

World space dělá z widgetu předmět ve scéně (menu na televizi), screen space ukazatel v pevné velikosti, který se vždy dívá do kamery (health bar). `Draw at Desired Size` srovná velikost s obsahem. `Redraw Time` dává strop, jak často se widget překreslí: 0 znamená každý snímek, 0,1 nanejvýš desetkrát za sekundu.

Kde se s tím potkáš: [Menu jako předmět ve scéně](praxe/ui-ve-svete.md#menu-jako-predmet-ve-scene-widget-na-televizi-a-virtualni-mys) · [Health bar nad hlavou](praxe/ui-ve-svete.md#health-bar-nad-hlavou-screen-space-ukazatel-z-materialu-a-dojezd-poskozeni) · [Sto health barů](praxe/ui-ve-svete.md#sto-health-baru-logika-na-ticku-a-prekresleni-jsou-dve-ruzne-ceny)

### Widget Interaction Component

**Virtuální myš pro widgety ve světě: paprsek, který widgetu na Widget Componentě posílá najetí a kliknutí.**

Zdrojem paprsku může být kurzor myši (Interaction Source = Mouse) nebo směr samotné komponenty. Paprsek se zastaví o první kolizi, takže meshe před widgetem nesmějí blokovat. Kliknutí se do komponenty předává ručně (`Press Pointer Key` / `Release Pointer Key`).

Kde se s tím potkáš: [Menu jako předmět ve scéně](praxe/ui-ve-svete.md#menu-jako-predmet-ve-scene-widget-na-televizi-a-virtualni-mys)

### World Composition

**Starší systém UE 4 pro velké světy: svět složený ze sublevelů v mřížce, které se streamují podle vzdálenosti.**

Předchůdce [World Partition](#world-partition). Projekty začaté před jeho příchodem na něm stavěly i v UE 5; Lords of the Fallen po sublevelech streamují i nav data.

Kde se s tím potkáš: [Jeden nav mesh pro všechny velikosti](praxe/ai-ve-velkem.md#jeden-nav-mesh-pro-vsechny-velikosti-sirka-chodby-jako-flag-v-nav-datech) · [Rejstřík: World Partition](#world-partition)

### WPO

**World Position Offset — posun vrcholů v materiálu; nejčastější tichá příčina drahých stínů.**

Slouží k větru v listí, vlnám a podobným deformacím a je to **programovatelná rasterizace**, tedy v Nanite světě výrazně dražší cesta. Dvě pole, která k němu vždycky patří: **WPO disabled distance** (za ní se přepne na rychlou fixed-function cestu) a u listí **shadow cache invalidation behavior**, protože pohybující se vrcholy jinak invalidují stínovou cache každý snímek. Diagnostika: Nanite visualization → *Evaluate WPO*; zelená znamená, že se vyhodnocuje.

Kde se s tím potkáš: [Kdo invaliduje stínovou cache](praxe/nanite-do-hloubky.md#kdo-invaliduje-stinovou-cache) · [Rejstřík: Virtual Shadow Maps](#virtual-shadow-maps) · [Rejstřík: Nanite](#nanite) · [Overlay a WPO](praxe/souboj.md#zablesk-a-kapow-efekt-musi-sedet-na-tele-i-mezi-tely) · [AC Black Flag: okna s náhodnou místností](praxe/env-technika.md#ac-black-flag-resynced-prodat-iluzi-ne-postavit-skutecnost) · [Prohlubně z render targetu](praxe/footsteps.md#stopy-do-hloubky-render-target-jako-platno-pod-postavou)

### Water Body

**Actor Water pluginu: ocean, lake, river, island — vodní tělesa tvarovaná splinami, vzájemně propojitelná.**

Klávesa G ukáže spline pointy; řeka má rychlost proudu per point (alt+tažení přidává body). Vztah k terénu řeší Edge Offset / Channel Edge Offset a falloff mode (Angle→Width proti hřebeni u břehu); landscape drž ~1 cm nad nulou. Vestavěné: waterline efekt kamery a podvodní post-process.

Kde se s tím potkáš: [Voda a buoyancy](praxe/voda-a-buoyancy.md) · [Interaktivní voda](praxe/interaktivni-voda.md)

### Wave Function Collapse

**Procedurální generátor: každé políčko je superpozicí všech dlaždic a „pozorování" ho zkolabuje podle pravidel sousedství.**

Metafora z kvantové mechaniky, mechanika ze sudoku: vyber políčko, zkolabuj na dlaždici konzistentní se sousedy (silnice navazují), opakuj. Výsledek náhodný, a přitom soudržný — nekonečné mapy bez ruční práce a bez generativní AI.

Kde se s tím potkáš: [Algoritmy, které stojí za to znát](teorie/algoritmy-prehled.md) · [PCG: základy a nástroje](praxe/pcg-zaklady.md)

### WIP limit

**Strop rozdělané práce v kanbanu: jedna, maximálně dvě karty v Doing na osobu.**

„Kdo tvrdí, že právě dělá tři věci, v podstatě lže — jednu dělá a ostatní ignoruje, nebo mezi nimi těká." Limit dělá z prostředního sloupce pravdivý komunikační kanál: tým vidí, na čem kdo dnes opravdu je, a pozná, kdo je volný.

Kde se s tím potkáš: [Plánovací nástroje](teorie/planovani-nastroje.md) · [Žrouti času](teorie/produktivita.md)

### Wishlist

**Přání na Steamu — před vydáním hlavní měřítko zájmu o hru a palivo algoritmu viditelnosti.**

Wishlisty pohánějí doporučování a rozhodují o síle launche; Steam Next Fest funguje jako jejich multiplikátor. Zároveň pozor na „the gap": wishlist je zdvořilý zájem, nákup je závazek — konverze není samozřejmá. V žebříčku důkazů síly nápadu stojí wishlisty vysoko, ale pozdě; validovat jde mnohem dřív a levněji.

Kde se s tím potkáš: [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### World Partition

**Streamovací systém UE5: svět rozdělený na buňky, které se nahrávají a uvolňují podle vzdálenosti či logiky.**

Nahrazuje starší ruční level streaming; open world level je level s aktivním World Partition. Mesh Terrain na něm závisí — terén existuje jako partition chunky viditelné ve World Partition okně, kde jde s regiony pracovat (load/unload) i během editace, což šetří paměť při práci na velkých plochách.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Zákon opaků

**Marketingová technika: najdi slabinu, na kterou si stěžují fanoušci žánru, odstraň ji a postav na tom svůj slib.**

Případovka: survival hra si všimla, že hráči mají dost mechaniky hladovění, vyřadila ji a udělala z toho hlavní sdělení — hra zůstala z devadesáti procent žánrová a prodávala se tou jednou změnou. Působí to jako honba za trendem, ale je to opak: vidíš, čeho mají lidé dost, a jdeš před ně.

Kde se s tím potkáš: [Co prodává: zákon opaků](teorie/co-prodava.md) · [Žánry očima designéra](teorie/zanry.md)

### Yomi

**Čtení soupeřovy mysli jako herní dovednost: vím, že on ví, že já vím — a přesně o tom je vrcholné hraní.**

Termín z fighting her: mind game nad mechanikami. Šachy proti dítěti nebaví, protože Yomi předpokládá sdílené porozumění; skryté karty (Scythe) jsou konfrontačnější než kostky, protože hraješ proti mysli, ne proti hodu.

Kde se s tím potkáš: [Engineering experiences](teorie/engineering-experiences.md)

### Yoink & twist

**Vzorec tvorby nápadu: vezmi žánr s prokázaným publikem (yoink) a přidej vlastní vylepšení nebo obrat (twist).**

Protiklad honby za stoprocentní originalitou, která znamená nulovou validaci trhu a chybějící referenční body. Rozhodovací pravidlo: v mladém žánru stačí být *lepší* (oprav pár bolestí z negativních recenzí — Fields of Mistria vs. Stardew Valley), ve starém žánru musíš být *jiný* (Age of Empires neporazíš kvalitou). Twist často stojí jen reskin a fikci — v kódu se nemusí změnit nic.

Kde se s tím potkáš: [Nápad: yoink & twist](teorie/napad.md) · [Prototypování: standardy vs. inovace](teorie/prototypovani.md)

### Zákop (trench)

**Nejmenší nosný kus skladby — hlavní hlas a akordy pod ním — do kterého se investuje nepoměrně víc času než do zbytku.**

Metoda má tři kroky: vykopat zákop (melodie první, akordy druhé), rozšířit ho o bicí, melodii a bas — **s kontrolou celku mezi každými dvěma přidanými nástroji** — a teprve pak aranžovat. Jádro není v pořadí, ale v té kontrole: dokud spolu fundamenty nesedí, žádná další vrstva už tomu nepomůže. Je to totéž jako integrace po malých krocích proti big-bang integraci, jen se to v hudbě projeví tiše — mix nespadne, jen postupně přestane fungovat.

Kde se s tím potkáš: [Metoda zákopu](hudba/aranz.md#metoda-zakopu-nic-nepridavej-dokud-stavajici-nesedne) · [Rejstřík: Arrangement](#arrangement)

### Zázněj

**Pomalé kolísání hlasitosti, když spolu znějí dvě skoro stejné frekvence (beating).**

Vzniká střídavým sčítáním a odečítáním vln („wa-wa-wa"). Čím dál od sebe frekvence, tím rychlejší kolísání, až se z něj stane obecná drsnost — jedna ze dvou příčin pásma nepohody mezi tóny.

Kde se s tím potkáš: [Fyzika souzvuku](hudba/fyzika-souzvuku.md)

### Z index

**Číslo, které určuje pořadí vykreslení 2D objektů nezávisle na jejich pozici ve stromu.**

Ve výchozím stavu mají všechny viditelné nody Z index 0, a proto se kreslí v pořadí, v jakém jsou ve [stromu scény](#scene-tree) — což znamená, že přeuspořádání stromu tiše změní, co je vidět. Nastavit hráči vyšší Z index je explicitní pravidlo („hráč je vždycky vepředu") místo skryté závislosti na pořadí. Obecně platí: kde na překrývání záleží, zapiš to číslem, ne pořadím.

Kde se s tím potkáš: [Nody, scény a strom](godot/zaklady.md#nody-a-sceny-strom-ktery-je-zaroven-architekturou)

### Zero indexing

**První prvek má index 0: lidské „první" je strojová nula — a na záměně padly nespočetné hodiny ladění.**

Konvence většiny jazyků (i UE polí): n-tý prvek sedí na indexu n − 1. Klasický důsledek je off-by-one chyba — smyčka o jedno projede či nedojede. Kdykoli sáhneš po indexu, řekni si nahlas, jestli počítáš od nuly.

Kde se s tím potkáš: [Programátorské myšlení](teorie/programatorske-mysleni.md)
