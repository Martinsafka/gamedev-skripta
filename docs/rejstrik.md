# Rejstřík

Odborné termíny napříč skripty — **termín anglicky, výklad česky**, protože přesně tak se s nimi potkáš v editoru, dokumentaci i komunitě. Rejstřík má dvě vrstvy: každý výskyt termínu kdekoli na webu má automatický tooltip s krátkou definicí a tahle stránka přidává hloubku a odkazy do kapitol, kde termín žije v kontextu.

Rejstřík roste s obsahem — každé zpracované video sem přidává svoje pojmy.

---

### Affordance

**Vlastnost objektu či prostoru, která signalizuje, jak s ním jde interagovat — dřív, než to hráč zkusí.**

Pojem z designové psychologie (Gibson, Norman): klika říká „stiskni", římsa říká „vylez". V level designu se affordances vyrábějí světlem, kompozicí a kontrastem — tajná odbočka musí *vypadat* zajímavě a interaktivně, jinak ji hráč mine. Zrádné jsou falešné affordances: co vypadá průchozí a není, rozbíjí důvěru (viz invisible wall).

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Vedení hráče](teorie/vedeni-hrace.md)

### Asset pack

**Balík hotových assetů — modely, zvuky, UI, shadery — připravený k okamžitému použití.**

Pro sólo vývojáře nástroj přežití: 50 hodin vlastního lokalizačního toolkitu vs. hotový asset za pár desítek dolarů je reálná volba z praxe. Kupuje se to, co dělat neumíš nebo nechceš; vlastní ruce si šetři na to, čím se hra liší. Při prototypování asset packy dodají vizuál a vibe za nulový čas — a u „design by constraint" umí být rovnou zdrojem nápadu („šla by kolem tohohle jediného assetu postavit hra?").

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Nápad](teorie/napad.md) · [Scope](teorie/scope.md)

### B-roll

**Doplňkové záběry, které běží na obrazovce, zatímco mluvíš o něčem obecnějším — ve videích o hrách typicky záběry gameplaye.**

Pravidlo devlogů: na obrazovce má být hra, pořád — ideálně přesně to, o čem zrovna mluvíš, jinak aspoň obecný B-roll. Chytrý zdroj záběrů starších verzí hry: version control — checkout starého commitu a natoč, co potřebuješ.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md)

### Blockout

**Hrubá stavba levelu z primitivních tvarů — testuje prostor, metriky a flow dřív, než přijdou finální assety.**

Blockout disciplína: grid/metrické materiály (okamžitě vidíš, že vchod je úzký nebo skok dlouhý), konzistentní barevný jazyk (cover jedna barva, traversal jiná) a „level design gym" — referenční mapa metrik sdílená napříč levely. Startovní bod hráče a hlavní landmark se rozhodují ještě před blockoutem.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md) · [Prototypování](teorie/prototypovani.md)

### Blueprint Interface

**Sada deklarovaných funkcí bez implementace — kontrakt, který si každý Blueprint naplní po svém.**

Volající posílá zprávu (message call) na libovolný actor; pokud actor interface implementuje, zareaguje vlastní logikou, pokud ne, nestane se nic — žádný pád, žádná závislost. Je to enginová podoba principu „programuj proti rozhraní": character nemusí znát třídu dveří, truhly ani panelu, stačí mu smlouva „umíš interagovat?". Přidání nového typu interaktivního objektu pak neznamená žádnou změnu ve volajícím.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Boolean

**Geometrická operace kombinující dvě tělesa: sjednocení (union), rozdíl (subtract), průnik (intersect).**

Pojmenováno po booleovské logice — tělesa se skládají jako množiny bodů. V Mesh Terrainu boolean modifier skutečně vroubuje cizí mesh do terénu: union přiroste, subtract vyřízne díru a geometrie se na okrajích sešije. Klasický nástroj CSG modelování (Constructive Solid Geometry), který znáš z Blenderu i CADů.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Call to action

**Závěrečná výzva trailer u nebo videa: co má divák udělat teď — „Wishlist on Steam", „Demo out now".**

Formát pro herní trailer: 5–8 vteřin na konci, key art + název + jedna výzva. Právě jedna — dvě CTA najednou („demo + wishlist") si konkurují a oslabují se. V širším marketingu platí totéž pro každý kanál: post, devlog i stránka mají mít jeden jasný další krok.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Capsule

**Náhledový obrázek hry na Steamu — miniatura, kterou zákazník vidí ve všech seznamech dřív než cokoli jiného.**

Nejdůležitější kus grafiky celé stránky. Zásady: žádné AI generované umění, custom nebo semi-custom logo (volný font + gradient + tematický detail), silný kontrast textu vůči pozadí, žádný text kromě názvu hry, nekolidovat se Steam badgi (Demo) — a rámeček, který capsule vysekne ze seznamu. Rozbory dobrých a špatných: steamcapsule.com.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md) · [Co prodává](teorie/co-prodava.md)

### Cast

**Přetypování obecné reference na konkrétní třídu, aby šlo volat její specifické funkce.**

`Cast To DestroyDoor` řekne enginu „zkus s tímhle actorem zacházet jako s třídou DestroyDoor". Cena: volající Blueprint získává tvrdou závislost na cílové třídě (a tahá si její referenci do paměti), takže s každým novým typem objektu roste řetěz castů. Tam, kde jde jen o „pošli zprávu, kdo umí, zareaguje", je lepší Blueprint Interface.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Channel

**V Mesh Terrainu pojmenovaná materiálová vrstva terénu — nástupce landscape layers.**

Channels se definují v data assetu partition definice 1:1 podle vrstev materiálu a rovnou se z nich stávají malovatelné vrstvy, bez ceremonie layer info assetů starého Landscape. Navíc je umí přiřazovat i modifiery (weight channel) — boolean skála si tak vyřízne tvar a zároveň obarví materiál. Pozor na kolizi názvosloví: UE má i kolizní channels (WorldStatic, Pawn…), to je jiný mechanismus.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Cipher

**Typ hráčské postavy: prázdná nádoba bez vlastní osobnosti, hlasu a motivací — oživuje ji hráčova imaginace.**

Jeden ze čtyř typů protagonisty (cipher · fixní · customizovatelný · customizovatelný s fixním základem). „Bez osobnosti" není vada: mlčící postava v puzzle hrách (Half-Life, Tunic) nechává znít hlas v hráčově hlavě. Cena: veškerá tíha charakterizace jde do vizuální komunikace — jak postava vypadá a co reprezentuje. Praktické pravidlo: umíš psát → fixní postava; umíš vyrábět cool věci, ale ne psát → cipher.

Kde se s tím potkáš: [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Cold open

**Otvírák traileru: prvních 10–15 vteřin nabitých highlighty v rychlých střizích, teprve pak volnější tempo.**

Pojem z filmového střihu (a trailerového řemesla Dereka Lieu). Důvod jsou retention grafy: velká část diváků odpadne během první půlminuty — kdo šetří nejlepší záběry na konec, ukáže je prázdnému sálu. Pravidla k tomu: celková délka 30–50 s, žádný záběr přes ~6 vteřin, na konci call to action.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Collision preset

**Předpis, jak objekt reaguje na jednotlivé kolizní kanály: Block, Overlap, nebo Ignore.**

Preset je první a nejlevnější filtr kolizního systému — rozhoduje se ještě před jakoukoli herní logikou. Trigger nastavený „Ignore all, Overlap jen WorldStatic/WorldDynamic/Pawn/PhysicsBody" negeneruje eventy o věcech, které tě nezajímají. Vlastní (Custom) preset se vyplatí kdykoli, kdy výchozí profily neodpovídají roli objektu.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Context steering

**Technika pohybu AI: entita průběžně hodnotí všechny směry vahami a vybírá nejlepší proveditelný.**

Vylepšení klasických steering behaviors (boids), jejichž protichůdné vektory se umí vyrušit — AI pak zamrzne u zdi, místo aby ji obešla. Context steering drží ohodnocení celé růžice směrů (typicky přes dot product vůči kýženému směru); zablokovaný nejlepší směr prostě nahradí druhý nejlepší. Tvarováním vah vznikají chování jako kroužení kolem cíle nebo nájezdy a odskoky — základ soubojů, které jsou zábavné pohybem, ne čísly.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md)

### Core loop

**Základní smyčka činností, kterou hráč ve hře opakuje nejčastěji — jádro, na kterém všechno ostatní stojí.**

„Plíž se → pozoruj → proklouzni" nebo „těž → vyrob → prodej". Užitečný pojem při analýze (co hráč *reálně* dělá většinu času?) i při ořezávání scope — co nesytí core loop, je kandidát na vyhození. Zároveň platí výhrada z kapitoly o smyčkách: popisuje strukturu, nevysvětluje kvalitu.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md) · [Nápad](teorie/napad.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### Data asset

**Asset nesoucí čistá strukturovaná data — konfiguraci bez logiky.**

V UE typicky potomek `UDataAsset`: designér edituje hodnoty v editoru, kód/Blueprinty je čtou. Odděluje „co" od „jak" — stejná logika, jiná data, jiné chování. Mesh Terrain v data assetu (Mesh Partition Definition) drží materiál, texel size a definice channels.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md) · [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md)

### Design by constraint

**Metoda hledání nápadů: nejdřív si zvol omezení, která řežou scope, a nápad nech vzniknout uvnitř nich.**

„Žádný příběh", „celá hra na jedné obrazovce", „žádné viditelné postavy", „jeden level" — omezení zmenší prostor možností tak, že se v něm dá tvořit. Postup: zvol omezení → posbírej hry se stejným omezením jako katalog interakcí → nech omezení třít o téma, dokud nevypadne nápad (piráti × jedna obrazovka = ostrov). Mini Metro tak vzniklo doslova. Druhá půlka metody: každé vývojářské omezení potřebuje player-facing alibi — téma, které ho vysvětlí a prodá.

Kde se s tím potkáš: [Scope: malé hry a design by constraint](teorie/scope.md) · [Prototypování](teorie/prototypovani.md)

### Devlog

**Video (či zápis) o vývoji vlastní hry — marketingový kanál a žánr s vlastním řemeslem.**

Dvě funkční podoby: showcase (rozbor jedné feature: proč → proces → výsledek → limity) a story (příběh vývoje, včetně slepých uliček); nejlepší devlogy obojí mísí. Klíč ke kvalitě je scénář — psaný nahlas, ne jako sloh — a hra na obrazovce po celou dobu. Devlog není povinnost: dělá se, když tě baví videa, ne pro automatické wishlisty.

Kde se s tím potkáš: [Devlogy](teorie/devlogy.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### Difficulty curve

**Průběh obtížnosti hry v čase — a hlavní nástroj, jak držet hráče ve flow.**

Skládá se ze dvou složek: novelty (učení nového) a mastery (zvládání naučeného). Šachy mají novelty nafrontovanou na začátek; hry často volí pilový tvar — s každou novou mechanikou schválně klesnou nároky na mastery, aby zbyla kapacita na učení. Doplňkové nástroje: matchmaking, automatické přizpůsobení, skill gates (těžší vstup filtruje nepřipravené) a rubber banding.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Event Tick

**Blueprint event volaný každý vykreslený snímek.**

Kód v Ticku běží 60× i vícekrát za vteřinu, ať se děje cokoli — je to polling: neustálé kladení otázky, jejíž odpověď se většinou nemění. Občas je nutný (plynulý pohyb, interpolace), ale většina herní logiky patří do eventů, timerů a delegátů, které se spouštějí při změnách. „Dostaň to z Ticku" je jedna z nejčastějších optimalizačních rad v UE — a hlavně rada architektonická.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md) · [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md)

### Flow

**Stav plného zaujetí činností, kdy výzva přesně odpovídá dovednosti (Mihály Csíkszentmihályi, 1990).**

Podmínky: častá a rychlá zpětná vazba, hluboké soustředění, výzva ~ skill. Tyrollerovo vysvětlení, proč flow kanál funguje: je to pásmo nejlepšího poměru signálu k šumu — ve frustraci vrací svět pořád „špatně" a v nudě pořád „dobře", učit se dá jen tam, kde některé akce fungují a jiné ne. Prakticky: flow = nejefektivnější učení = zábava; frustrace emočně přebije flow, flow přebije nudu.

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Game Design Document

**Dokument s návrhem hry (GDD) — funguje jen tehdy, když se do něj tým skutečně vrací.**

Klasická podoba (slohová práce v akademickém formátu) u sólo vývojářů umírá nedopsaná a nečtená. Funkční alternativa je vizuální nástěnka: reference s důvody, levely jako sekvence, mechaniky jako GIFy, centrální to-do. Jediná metrika kvality GDD je, jestli je *živý* — forma je vedlejší.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md)

### Game feel

**Hmatový dojem z ovládání hry: odezva, váha, šťavnatost interakcí — souhrn tisíce drobností, které dělají z klikání požitek.**

Screen shake, částice, zvuky zásahů, animační mikropohyby. „Game feel je cheat code": 20 % úsilí udělá 80 % dojmu a částice zamaskují nedodělky líp než cokoli jiného — proto patří i do prototypů. Zároveň platí pravidlo hraček: interakce mají být příjemné samy o sobě, dřív než na nich postavíš výzvy a cíle.

Kde se s tím potkáš: [Game feel a imerze](teorie/game-feel.md) · [Základy: engagement a appeal](teorie/zaklady.md) · [Nápad](teorie/napad.md)

### Game jam

**Časově omezená akce — typicky 48 hodin až týden — během níž vzniká celá malá hra, obvykle na zadané téma.**

Institucionalizovaný „malý rozsah": deadline ořeže scope za tebe a vynutí dokončení, což je přesně dovednost, kterou začátečník potřebuje trénovat nejvíc. Bonusy: publikum (ostatní účastníci hru zahrají), zpětná vazba a nulová penalizace za nedokonalost. Jamy fungují i jako „design by constraint jako služba" — omezení dostaneš zadáním; jen pozor, mechanika zábavná 10 minut nemusí unést hodinovou hru.

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Scope](teorie/scope.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Gameplay loop

**Smyčka činností, kterou hráč opakuje — nejcitovanější popisný nástroj game designu.**

Základní podoba je reward-investment: akce → odměna → investice odměny → silnější akce. Smyčky pomáhají číst strukturu her a komunikovat záměr, ale samy o sobě vysvětlují málo — model, pod který spadá skoro každá hra, nediskriminuje. Doplňkovým tvarem je řetězec (chain), který na rozdíl od smyčky nese směřování a rostoucí emoční investici.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Garbage collection

**Automatická správa paměti: engine periodicky uklízí objekty, na které už nikdo neukazuje.**

V UE je objekt po zničení (`Destroy Actor`) nejdřív označen jako **pending kill** — existuje v paměti, ale je „mrtvý" — a fyzicky zmizí až při dalším úklidu. Reference na takový objekt projde, ale použití spadne na runtime error. Obrana v Blueprintech: Validated Get / `Is Valid` před každým použitím reference na objekt, který mohl zaniknout.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Graybox

**Prototyp či blockout ze šedých primitivních tvarů — bez artu, bez nálady, jen prostor a mechanika.**

Správné použití: testování mechanik a metrik (gameplay prototyp, level blockout), kde by krása jen zkreslovala zpětnou vazbu. Špatné použití: testování prodejnosti a emoce — šedé kostky žádnou nemají, tam patří asset packy a hudba od prvního dne. Rozhodni, kterou otázku prototyp klade, a podle toho zvol formu.

Kde se s tím potkáš: [Prototypování](teorie/prototypovani.md) · [Nápad: prototyp do týdne](teorie/napad.md) · [Prostor a hranice](teorie/prostor-a-hranice.md)

### Hard coding

**Hodnoty napsané natvrdo přímo v kódu místo v proměnné či konfiguraci.**

Funguje přesně do chvíle, kdy je potřeba hodnotu změnit — pak ji lovíš po celém projektu a jednu zapomeneš. Pravidlo: každé surové číslo, které budeš někdy ladit, patří do proměnné; stejný princip platí pro vstupy (pojmenované akce místo kláves). Výjimka potvrzující pravidlo: v prototypu na vyhození je hard coding ctnost — rychlost tam poráží čistotu.

Kde se s tím potkáš: [Kolik kódu potřebuješ na start](teorie/co-se-ucit.md) · [Nápad: prototyp do týdne](teorie/napad.md)

### Height mapa

**Černobílá textura kódující výšku terénu jasem pixelu: černá dole, bílá nahoře.**

Formát, na kterém stojí klasický Landscape — a zdroj jeho hlavního limitu: jedna hodnota na pixel znamená jediný stupeň volnosti (nahoru/dolů), takže jeskyně a převisy nejdou. Zůstává ale skvělým výměnným formátem: sculpt z Gaey či World Machine se přenáší právě height mapou a Mesh Terrain ji umí importovat jako startovní tvar i promítat jako texture modifier.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Hook

**Prvek, který hru prodá na první pohled: mechanika, premisa nebo obraz, u kterého se scrollující palec zastaví.**

Portálové portály, vlak-monstrum z Choo Choo Charles, „staráš se o svoje auto v psychedelické Zóně". Hook je vstupní bod trychtýře appealu — bez něj hra nemá jak oslovit lidi, kteří o ní nikdy neslyšeli. Test: dokážeš hook vtěsnat do titulku na Redditu nebo do 300 znaků short description? Hra bez jediné inovace hook nemá — a bez hooku není důvod, aby vznikla.

Kde se s tím potkáš: [Základy: engagement a appeal](teorie/zaklady.md) · [Prototypování](teorie/prototypovani.md) · [Nápad](teorie/napad.md)

### Instance

**Konkrétní umístěný výskyt assetu v levelu.**

Jeden asset (mesh lampy) → stovky instancí (lampy po celé mapě). Rozlišení asset vs. instance je základ práce v editoru: úprava assetu se propíše všem instancím, úprava instance jen jí. Editor umí s instancemi pracovat hromadně — viz Shift+E pro výběr všech výskytů daného assetu.

Kde se s tím potkáš: [Tipy do editoru](praxe/editor-tipy.md)

### Invisible wall

**Neviditelná kolize tam, kde vizuálně nic nebrání v cestě — nejhorší způsob, jak ohraničit mapu.**

Zabíjí imerzi přesně mechanismem „vidím, že to jde, ale hra mi to nedovolí". Alternativy: tvrdé hranice z přirozených bariér světa (útes, řeka, oceán) a pět druhů měkkých hranic — narativní, countdown, nepřátelská, ekonomická, percepční. Pravidlo: hráč se má rozhodnout sám, že dál nepůjde.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Landmark

**Výrazný orientační bod levelu — věž, světlo, brána — ke kterému se vztahuje hráčova navigace i kompozice prostoru.**

V postupu „landmark napřed": startovní bod hráče a hlavní point of interest jsou první dvě rozhodnutí návrhu levelu, ještě před blockoutem — dávají měřítko, směr a osu pro pacing a vertikalitu. Cestou k landmarku pak vedou funneling (zúžení prostoru), leading lines a světlo.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Line Trace

**Raycast — neviditelný paprsek vyslaný z bodu daným směrem, který vrátí první (nebo všechny) kolize na dráze.**

Základní dotazovací nástroj: „na co koukám?", „stojím na zemi?", „vidí mě stráž?". Samotný trace je levný; problém je vzorec „trace každý frame v Event Ticku" — polling tam, kde stačí reagovat na změny. Alternativou pro detekci „něco vstoupilo do zóny" jsou overlap eventy kolizních komponent.

Kde se s tím potkáš: [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Low-fi prototyp

**Prototyp schválně nízké kvality — náčrt na papíře, čmáranice, hrubá animace konceptu — vytvořený za minuty.**

Jeho supersíla je psychologická: do vypiplaného dema se kritikům tluče těžko, ale náčrt za pět minut nikoho nesvazuje — dostaneš syrový názor na *myšlenku*, dokud se dá směr měnit zadarmo. Protějšek high-fi prototypu (funkční hratelné kostry), který je dražší a láká k připoutání. Srovnej s grayboxem: i tam jde o levné testování, ale mechaniky, ne nápadu.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md) · [Prototypování](teorie/prototypovani.md)

### Market research

**Průzkum trhu před rozhodnutím o hře: výdělky žánrů, tagy, recenze konkurence, benchmarky.**

První krok k objektivitě proti zamilovanosti do vlastního nápadu. Prakticky: Steamové roční žebříčky, SteamDB, Gamalytic/VG Insights, benchmarky Chrise Zukowského; okno posledních ~3 let (starší data lžou) a medián či spodních 25–30 % výdělků, nikdy průměr. Nejcennější levný zdroj: negativní recenze konkurence — seznam bolestí, proti kterým můžeš designovat.

Kde se s tím potkáš: [Idea iceberg](teorie/rady-z-praxe.md) · [Nápad: yoink & twist](teorie/napad.md)

### Modifier stack

**Vrstvené nedestruktivní úpravy: každá operace zůstává živým objektem, který lze dodatečně měnit, přesouvat, přeskládat nebo smazat.**

Filozofie „scéna je recept, ne výsledek" — známá z Houdini, Geometry Nodes či modifierů v Blenderu. Mesh Terrain na ní staví celé tvarování: brush, noise, spline, texture, mesh, boolean a remesh modifiery se skládají podle priorit a blend módů. Cena: recept se musí přepočítávat (build cost, FPS propady při editaci). Výhoda: žádné rozhodnutí není konečné.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Nanite

**Virtualizovaná geometrie UE5: engine dynamicky přizpůsobuje detail meshů vzdálenosti a velikosti na obrazovce.**

Prakticky ruší ruční LOD řetězce — mesh se subdivuje a redukuje průběžně, po clusterech, podle toho, co kamera reálně vidí. Mesh Terrain je na Nanite postavený; právě adaptivní subdivize je jeden z důvodů, proč zvládá větší plochy než starý Landscape. Po editaci terénu se Nanite reprezentace přestavuje — proto FPS propad během úprav a krátký build po odkliknutí.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Narrative design

**Návrh vyprávění integrovaný s herním designem — protiklad modelu „designér nechá díry na cutscény a spisovatel je dopíše".**

Pojem posledních ~20 let; zahrnuje volbu typu protagonisty, směr dialogů, rejstříky řeči i vyprávěcí prostředky, které mají jen hry (flavor texty, prostředí, mechaniky). Pro malé týmy začíná třemi branami: kolik implementace vyprávění přinese, jaká je tvá spisovatelská praxe a jaké příběhy ti nabízejí tvoje nástroje.

Kde se s tím potkáš: [Příběh a postavy](teorie/pribeh-a-postavy.md)

### Pacing

**Rytmus zážitku: střídání napětí a klidu, akce a ticha, učení a mistrovství v čase.**

Nástroj režie levelů i celých her: scripted events doručují momenty „ve správnou chvíli", struktura levelu střídá zúžení a otevření, obtížnostní křivka střídá novelty a mastery. Špatný pacing má dva póly — monotónní nuda a únavný nonstop tlak; dobrý pacing je dramaturgie.

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md) · [Zábava a flow](teorie/zabava.md)

### PCG

**Procedural Content Generation — UE framework pro procedurální osazování a generování obsahu světa.**

Grafem definuješ pravidla (sampluj povrch, filtruj podle sklonu, rozmísti stromy s hustotou X) a engine je aplikuje na libovolnou plochu. S Mesh Terrainem spolupracuje přes interop plugin (Mesh Partition PCG Interop) — v beta fázi s beta mírou spolehlivosti.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Pitch deck

**Krátká prezentace hry, která ještě neexistuje — simulace prvního kontaktu zákazníka s nápadem.**

Logika: první krok nákupu hry stejně neobsahuje hraní (trailer, GIF, screenshot) — pitch deck tenhle moment vyrobí bez jediného řádku kódu. Proces: brainstorm → hlasování → u top nápadů popsat smyčku (slabé se rozpadnou samy) → decky → nechat lidi vybírat. Opory: lidé skvěle *vybírají* a mizerně radí, jak zlepšovat; a deck za hodinu se zahazuje bez bolesti — málo vloženého času = málo biasu.

Kde se s tím potkáš: [Idea iceberg: pracuj zpátky](teorie/rady-z-praxe.md) · [Nápad: test 300 znaků](teorie/napad.md)

### Placeholder

**Provizorní asset, který drží místo finálnímu — kostka místo postavy, čmáranice místo ilustrace.**

Nástroj řazení priorit: dokud není jisté, že mechanika žije, každá hodina v grafice je sázka naslepo. Rada z praxe: dělej vlastní placeholdery *záměrně špatně* — hezký provizorní asset svádí k ladění, ošklivý ne. Pozor na licence: placeholdery z cizích her nesmí do ničeho vydaného, včetně dema.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md) · [Prototypování](teorie/prototypovani.md)

### Playtest

**Testování hry skutečnými hráči s cílem získat zpětnou vazbu — o srozumitelnosti, obtížnosti, zábavnosti.**

Nejmenší funkční forma je „ukaž rozdělanou věc kamarádovi": i to je zpětnovazební smyčka, bez které se cvičné hodiny nepočítají. Klíčová dovednost je kalibrace publika podle fáze — shovívavé publikum pro motivaci na začátku, kritické pro růst později. A čti chování, ne slova: playtesteři, kteří si o nový build říkají sami, jsou jiný signál než zdvořilé „je to hezký" (the gap).

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Idea iceberg: the Gap](teorie/rady-z-praxe.md) · [Postmortem ShantyTown](teorie/postmortem-shantytown.md)

### Postmortem

**Ohlédnutí za dokončeným (nebo pohřbeným) projektem: co fungovalo, co ne a proč.**

Nejhutnější studijní žánr gamedevu — na rozdíl od tutoriálů obsahuje i cenu rozhodnutí a slepé uličky. Dobrý postmortem přiznává čísla (wishlisty, prodeje, časové odhady vs. realita) i emoce (launch blues). Psát vlastní postmortemy je nejrychlejší způsob, jak z odehraných projektů vytěžit zkušenost — viz Zápisky.

Kde se s tím potkáš: [Postmortem: tři roky na ShantyTown](teorie/postmortem-shantytown.md)

### Premature optimization

**Optimalizace před důkazem, že je potřeba — přepis na ECS ve hře, která běží na 200 FPS.**

Klasická past programátorů: výkonový strop se řeší dřív než hratelnost, workflow se deformuje kolem optimalizací a vývoj zpomalí. Pragmatická rada z praxe: 80/20 — většina velkých problémů se dá vyřešit měsíc před vydáním za zlomek času. Výjimka: tvrdý platformní cíl (slabý handheld) je požadavek, ne optimalizace. Pojem zpopularizoval Donald Knuth („premature optimization is the root of all evil").

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md)

### Press kit

**Balíček pro novináře: popis hry, kontakty, loga, screenshoty a trailer v plné kvalitě na jednom místě.**

Novinář, který o hře chce napsat, potřebuje assety hned — press kit mu šetří mailování a tobě zvyšuje šanci na pokrytí. Nástroj presskit() ho vygeneruje zdarma za odpoledne; odkaz na něj plní roli webu, dokud web není. Patří k němu press release při velkých beatech (zveřejnění stránky, datum vydání) — rozesílá se např. přes GamesPress.

Kde se s tím potkáš: [Steam stránka](teorie/steam-stranka.md)

### Quad

**Čtyřúhelníková buňka mřížky meshe — u terénu základní jednotka rozlišení.**

Rozlišení Mesh Terrainu se zadává počtem quadů v osách XY; víc quadů = jemnější síť = víc detailu i dat. Interně se quady stejně dělí na trojúhelníky (GPU nic jiného nekreslí), ale pro autorskou práci je čtyřúhelníková mřížka přehlednější — proto s ní pracují terény, subdivision modeling i retopologie.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Recall priming

**Level design technika: rozmístit do prostředí nenápadné nápovědy, které hráči zpřístupní správnou vzpomínku těsně před tím, než ji bude potřebovat.**

Hráči se u puzzlů nezasekávají hloupostí, ale nedostupností správného nástroje v paměti. Priming ji zvedá prostředím: tmavá chodba donutí vytáhnout pochodeň, hořlavé liány cestou připomenou, že oheň pálí vegetaci — a u puzzle s liánami řešení „samo" naskočí. Hráč se necítí veden, cítí se chytrý; UI nápověda by mu ten pocit ukradla.

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md)

### Roguelike

**Žánr postavený na opakovaných bězích: smrt je součást smyčky, svět se generuje procedurálně, znalost hráče je hlavní trvalý pokrok.**

Pro design je podstatný důsledek mnoha běhů: hráč potkává stejné systémy znovu a znovu, což násobí šanci na náhodné objevení skrytých pravidel — proto žánru tak sedí tajné řetězce (Spelunky). Odnož s trvalým meta-postupem mezi běhy se označuje roguelite.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Rubber banding

**Umělá podpora hráče, který je pozadu, a brzda hráče napřed — v multiplayeru se říká catch-up mechanika.**

Nejde o podvod na hráče, ale o opravu učebního prostředí: kdo je beznadějně pozadu, dostává od hry konstantní „špatně" a nemá se z čeho učit; kdo je nedostižně napřed, dostává konstantní „dobře". Rubber banding oba vrací do pásma, kde akce zase mají čitelné následky. Příbuzné nástroje: hinty, skipy, měkké stavy úspěchu (skóre místo výhra/prohra).

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Scope

**Rozsah projektu: kolik obsahu, systémů a ambicí hra obsáhne.**

Hlavní páka proveditelnosti — a nejčastější příčina nedokončených her. Pro začátečníka platí, že malý scope není kompromis, ale strategie: krátká smyčka dokončení → zpětná vazba → další projekt o úroveň výš. Malá hra přitom není zmenšená velká hra, ale jedna vyjmutá mechanika, které všechno slouží. „Scope creep" je plíživé bobtnání rozsahu během vývoje; game jam je institucionalizovaná obrana.

Kde se s tím potkáš: [Začátky bez zkušeností](teorie/zacatky-bez-zkusenosti.md) · [Scope: malé hry a design by constraint](teorie/scope.md) · [Start projektu](teorie/jak-zacit.md)

### Scope creep

**Plíživé bobtnání rozsahu během vývoje: „co kdybychom přidali rybaření?"**

Dvojsečná past: někdy je to přesně ten twist, který hře chyběl, častěji fraktální bobtnání (rybaření → pruty → rybářské lodě) nebo míchání žánrů, které vyrobí hru pro nikoho — publikum dvou žánrů je průnik, ne součet. Rozhodovací filtr: sytí nápad účel hry, nebo ho ředí? Obrana: sticky note test na začátku, momentum bar a psaní nápadů do šuplíku během vývoje.

Kde se s tím potkáš: [Žrouti času](teorie/produktivita.md) · [Nápad](teorie/napad.md) · [Start projektu](teorie/jak-zacit.md)

### Short description

**Krátký popis hry na Steamu — ~300 znaků pod capsule obrázkem, první text, který potenciální hráč čte.**

Zároveň nejlevnější validační nástroj nápadu: „test 300 znaků" = zkus popis napsat v den nula. Dvě věty se žánrem, perspektivou, hlavními činnostmi (hodně sloves!), cílem a prostředím. Když to nejde, nemáš vágní popis — máš vágní hru. Rozšířená verze testu je mock Steam page: dlouhý popis, features, zkusmá capsule.

Kde se s tím potkáš: [Nápad: test 300 znaků](teorie/napad.md) · [Scope](teorie/scope.md)

### Signal-to-noise ratio

**Poměr užitečné informace (signál) k balastu (šum) — klíčová veličina učení, soustředění i designu obtížnosti.**

Učení je budování prediktivního modelu světa a potřebuje data, ze kterých se dá učit. Frustrace = konstantní „špatně" (nulový signál), nuda = konstantní „dobře" (nulový signál); flow kanál je pásmo, kde některé akce fungují a jiné ne — nejlepší signál. Jasné cíle jsou filtr šumu; soustředění je totéž z druhé strany (rozptýlení a vizuální balast = šum).

Kde se s tím potkáš: [Zábava: flow](teorie/zabava.md)

### Soft boundary

**Hranice mapy, kterou lze fyzicky překročit — ale svět dá jasně najevo, že je to špatný nápad.**

Pět vzorů: narativní (most se zřítí, postava odmítne jít dál), countdown (mráz, plyn, dezerce — tlak času místo kolize), nepřátelská (za hranicí loví něco silnějšího; nemusí zabíjet — stačí probrat se potlučený zpátky), ekonomická (kyslík/palivo nevystačí na návrat) a percepční (ztráta orientace a viditelnosti). Nejlépe fungují kombinované a vždy s fikčním alibi.

Kde se s tím potkáš: [Prostor a hranice](teorie/prostor-a-hranice.md)

### Square hole

**Chyba balancu: univerzální nástroj či strategie, která řeší každou situaci — a tím zabíjí všechna rozhodnutí.**

Podle memu „it goes in the square hole". Vzniká z balancování jedinou osou síly: jeden nástroj vždycky vyjde o chlup líp a stane se odpovědí na všechno. Lék: vícerozměrné nástroje (každý dobrý na něco jiného) + pestré problémy + zajímavé hraniční případy, kde volba vyžaduje úvahu. Cíl balancu: rozhodnutí netriviální, předvídatelná a nosná i po opakování.

Kde se s tím potkáš: [Zábava: balanc rozhodnutí](teorie/zabava.md)

### Steam Next Fest

**Steamový online festival demoverzí nevydaných her, koná se třikrát ročně.**

Funguje jako multiplikátor wishlistů — čím víc jich máš na vstupu, tím víc akce vygeneruje — a každá hra se smí zúčastnit jen jednou, takže načasování je strategické rozhodnutí (jít tam s maximem, klidně couvnout a počkat na další termín). Citované minimum pro smysluplný efekt ~7 000 wishlistů na vstupu (údaj jednoho vydání, ne konstanta).

Kde se s tím potkáš: [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### Tessellation

**Dělení geometrie na jemnější trojúhelníky, aby povrch unesl víc detailu.**

V Mesh Terrainu ve dvou podobách: adaptivní teselace texture modifieru (zjemní síť tam, kde height mapa nese detail, řízeno error tolerancí) a Tessellate režim remesh modifieru. Protiklad k uniformnímu remeshi: adaptivní přístup šetří trojúhelníky, ale hůř se predikuje výsledný tvar. Obecná rada z praxe: hrubé tvarování s teselací vypnutou, detail zapínat cíleně na konci.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Trigger volume

**Neviditelná zóna v levelu, která při vstupu hráče (či jiné entity) spustí událost.**

Základní nástroj skriptovaných momentů: rozhovor NPC na tržišti, změna hudby, otevření cesty, cinematika na správném místě. Designové pravidlo: nejdřív otázky „jaký zážitek, jaká emoce, jaká informace, jaká další akce?" — trigger je jen doručovací mechanismus. V UE odpovídá trigger box/volume s overlap eventy (viz praxe: interakce bez Event Ticku).

Kde se s tím potkáš: [Vedení hráče](teorie/vedeni-hrace.md) · [Interakce bez Event Ticku](praxe/interakce-bez-event-ticku.md)

### Value chain

**Hodnotový řetězec (Dan Cook): smysl a zábavnost sběrné činnosti nedává činnost sama, ale její zamýšlené použití dál v řetězci.**

Sbírání klacíků nudí, dokud z nich hráč nestaví něco, co sytí fantazii hry — pak se každé rozhodnutí „co sebrat" stává plánováním. Prakticky: nudnou mechaniku neoživuj pozlátkem, dej jí destinaci. Cíl řetězce zpětně obarvuje všechny jeho články.

Kde se s tím potkáš: [Smyčky a řetězce](teorie/smycky-a-retezce.md)

### Version control

**Verzování projektu (typicky Git): každá změna se ukládá jako commit, ke kterému se lze kdykoli vrátit.**

Dvě služby: záchranné lano z každé katastrofy a viditelná historie pokroku (protilék na „nic nestíhám"). Zásada zrnitosti: commituj malé celky s popisnou zprávou — velký commit se špatně popisuje, vrací i slučuje. UE specifika: Blueprinty jsou binární (diff neuvidíš, zpráva je vše), na velké assety Git LFS, v editoru vestavěná integrace Revision Control.

Kde se s tím potkáš: [Start projektu](teorie/jak-zacit.md)

### Vertical slice

**Reprezentativní výsek hry ve finální kvalitě — brána mezi prototypem a plnou produkcí.**

Ne nutně začátek hry: libovolných 5–60 minut zážitku, na kterém se poprvé potkají mechaniky z prototypu, art style a tón. Otázka, na kterou odpovídá: nadchne lidi reprezentativní ukázka natolik, aby se vyplatilo vyrábět zbytek obsahu? U komplexních her se skládá z ~60 % žánrových standardů a ~40 % inovací — testovat jde jen to nové.

Kde se s tím potkáš: [Prototypování a vertical slice](teorie/prototypovani.md) · [Základy designu](teorie/zaklady.md)

### Wishlist

**Přání na Steamu — před vydáním hlavní měřítko zájmu o hru a palivo algoritmu viditelnosti.**

Wishlisty pohánějí doporučování a rozhodují o síle launche; Steam Next Fest funguje jako jejich multiplikátor. Zároveň pozor na „the gap": wishlist je zdvořilý zájem, nákup je závazek — konverze není samozřejmá. V žebříčku důkazů síly nápadu stojí wishlisty vysoko, ale pozdě; validovat jde mnohem dřív a levněji.

Kde se s tím potkáš: [Postmortem ShantyTown](teorie/postmortem-shantytown.md) · [Idea iceberg](teorie/rady-z-praxe.md)

### World Partition

**Streamovací systém UE5: svět rozdělený na buňky, které se nahrávají a uvolňují podle vzdálenosti či logiky.**

Nahrazuje starší ruční level streaming; open world level je level s aktivním World Partition. Mesh Terrain na něm závisí — terén existuje jako partition chunky viditelné ve World Partition okně, kde jde s regiony pracovat (load/unload) i během editace, což šetří paměť při práci na velkých plochách.

Kde se s tím potkáš: [Mesh Terrain](praxe/mesh-terrain.md)

### Yoink & twist

**Vzorec tvorby nápadu: vezmi žánr s prokázaným publikem (yoink) a přidej vlastní vylepšení nebo obrat (twist).**

Protiklad honby za stoprocentní originalitou, která znamená nulovou validaci trhu a chybějící referenční body. Rozhodovací pravidlo: v mladém žánru stačí být *lepší* (oprav pár bolestí z negativních recenzí — Fields of Mistria vs. Stardew Valley), ve starém žánru musíš být *jiný* (Age of Empires neporazíš kvalitou). Twist často stojí jen reskin a fikci — v kódu se nemusí změnit nic.

Kde se s tím potkáš: [Nápad: yoink & twist](teorie/napad.md) · [Prototypování: standardy vs. inovace](teorie/prototypovani.md)
