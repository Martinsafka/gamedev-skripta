*[A/B test]: Dvě verze hry dvěma skupinám testerů — rozhodne chování, ne názor; testerům se často neříká nic.
*[AAA]: Termín z financí, ne z kvality: největší a nejbezpečnější finanční sázky v oboru.
*[Abstract class]: Třída, kterou nejde umístit do světa ani referencovat — existuje jen jako rodič pro děti.
*[ABTest]: Konzolový příkaz střídající dvě hodnoty jedné proměnné a vypisující výkon obou.
*[Active frames]: Snímky, ve kterých útok zraňuje — mezi nápřahem a zotavením; v UE typicky notify state.
*[Actor Component]: Znovupoužitelný díl chování připnutý k aktérovi — schopnost bez identity.
*[ADSR]: Attack/Decay/Sustain/Release — jak zvuk naběhne, klesne, drží a dozní (obálka zvuku).
*[Affordance]: Vlastnost objektu/prostoru signalizující, jak s ním jde interagovat — klika říká „stiskni".
*[Aggro]: Skóre, podle kterého si nepřítel vybírá cíl — blízkost, vydržené poškození, umělé aggro, cooldown přepnutí.
*[AI Controller]: Mozek AI postavy: posedne pawna a rozhoduje; spouští Behavior/State Tree, nese percepci.
*[AI Perception]: Percepční systém UE: smysly (sight, hearing, damage) jedné komponenty; cíl musí mít Stimuli Source.
*[Akord]: Tři a více tónů zároveň; nejzákladnější je triáda (základ + tercie + kvinta).
*[Alikvóta]: Vyšší frekvence nad základním tónem; určuje barvu zvuku a to, co ladí (overtone).
*[ALS]: Advanced Locomotion System — komunitní locomotion framework; jeho autor dnes v Epicu vede design GASP.
*[Ambient occlusion]: Ztmavení míst, kam se hůř dostane rozptýlené světlo — kouty, spáry, styky ploch.
*[Anchor (UI)]: Kotva Control nodu — číslo 0–1 určující místo v rodičově obdélníku; přežije změnu rozlišení.
*[Animation curve]: Pojmenovaná křivka v animaci či montáži, kterou AnimBP čte každý snímek (alfa IK, úhel dveří…).
*[Anim montage]: Animační asset pro jednorázové akce, hraný přes sloty; nad MM základ combatu (horní tělo).
*[Anim Notify]: Značka na časové ose animace spouštějící logiku v daném framu; notify state = varianta s trváním.
*[Animation cancel]: Přerušení animace jinou akcí; v akčních hrách zdroj většiny pokročilých technik.
*[Apofenie]: Pud vidět vzory a příběhy všude — motor emergentního narativu (RimWorld model).
*[Apply Damage]: Vestavěné poškození v UE: Apply (Point) Damage u útočníka, Event Any/Point Damage u terče.
*[Arrangement]: Rozvinutí loopu do celé skladby (aranžmá); píseň žije v přechodech mezi sekcemi.
*[Art bible]: Dokument vizuálního jazyka hry: moodboardy, palety, reference, pravidla stylu.
*[Anim Budget Allocator]: Plugin rozdělující pevný rozpočet na animace podle významnosti; nasadit hned, zpětně to bolí.
*[Aspirační obtížnost]: Jak těžké je uspět DOBŘE (víc bodů, volitelná hloubka) — obtížnost, po které hráč sahá sám.
*[Async compute]: Druhá fronta GPU jen pro compute; vysoký „wait" na ní je normální, na grafické ne.
*[Asset pack]: Balík hotových assetů (modely, zvuky, UI) k okamžitému použití — základ rychlého prototypování.
*[Assist mode]: Volitelný režim, kde si hráč upraví obtížnost po jednotlivých pákách místo výběru „easy".
*[Asset User Data]: Data pověšená na asset, která s ním cestují všude; gameplay na meshi bez blueprintu.
*[Astroturfing]: Marketing předstírající, že vznikl zdola z komunity, i když ho platí firma.
*[Attachment rules]: Pravidla připnutí objektu: Snap to Target ho okamžitě přesune, Keep World ho nechá na místě.
*[Attenuation]: Útlum hlasitosti se vzdáleností; per-frekvenčně dělá zblízka ostrý, z dálky dunivý zvuk.
*[AutoBake]: Přepínání živého control rigu a jeho zapečené animation sequence v sequenceru (UE 5.8).
*[Autoload]: Scéna zaregistrovaná jako globální — načte se sama a přežije výměnu scén (zdejší singleton).
*[Blend Poses by Bool]: Anim uzel, který podle boolu přepne mezi dvěma pózami — „if" v anim grafu.
*[Blueprint Debugger]: Ladění blueprintů za běhu: breakpointy, sledované hodnoty a zastavení na uzlu, kde nastala chyba.
*[Blueprint Macro]: Znovupoužitelný kus Blueprint grafu; na rozdíl od funkce smí obsahovat Delay a jiné latentní uzly.
*[B-roll]: Doplňkové záběry pod mluvené slovo; v devlozích typicky záběry gameplaye.
*[Backbeat]: Rytmický důraz na sudé doby taktu; místo pro snare a clap.
*[Backlog]: Zásobník všeho, co projekt čeká (úkoly i nápady); priority se z něj tahají po dávkách.
*[Backpressure]: Producent rychlejší než konzument? Nebufferuj, nezahazuj — propaguj tlak zpět, ať zdroj zpomalí.
*[Barbell strategie]: Sázej na oba krajní póly (bezpečné + riskantní), ne na průměr uprostřed.
*[Barrier to play]: Překážka, kterou designér testovat nechtěl (ovládání, barvy) — dokud existuje, obtížnost neladíš.
*[Beautiful corner]: Jeden malý kus hry v cílové kvalitě, zbytek v grayboxu — mikro vertical slice.
*[Behavior Tree]: Rozhodovací strom AI: selectory a sequence volí tasky podle Blackboardu; decoratory hlídají podmínky.
*[Beta]: Pozdní testovací verze: obsahově víceméně celá hra, ladí se balanc, bugy a onboarding.
*[Blackboard]: Sdílená tabule AI: pojmenované klíče, přes které si percepce, tasky a strom předávají data.
*[Blend Space]: Asset míchající animace podle hodnot na osách (rychlost, směr); klipy synchronizují sync markery.
*[Blend stack]: Anim uzel: změna animační proměnné = nový blend do zásobníku — bez state machine.
*[Blockout]: Hrubá stavba levelu z primitiv — testuje prostor, metriky a flow před finálními assety.
*[Blue ocean]: Trh bez konkurence — hra vytváří novou poptávku; opak red ocean (přeplněné žánry, boj zdroji).
*[Blueprint Function Library]: Sbírka funkcí volatelných z libovolného blueprintu v projektu.
*[Blueprint Interface]: Sada funkcí bez implementace — kontrakt mezi Blueprinty, volání zprávou bez znalosti třídy.
*[Boids]: Algoritmus hejna: tři pravidla (separation, alignment, cohesion) — chování hejna emerguje samo.
*[Boolean]: Geometrická operace kombinující dvě tělesa: sjednocení (union), rozdíl (subtract), průnik.
*[Bounds]: Osově zarovnaný obal objektu či bodu; v PCG pracovní data — výřezy, pruning, bounds modifier.
*[BPM]: Tempo v dobách za minutu; ukotví žánr a energii dřív než noty (lo-fi ~77, DnB ~170).
*[BRDF]: Model odrazu světla od povrchu — matematický základ toho, jak materiál vypadá.
*[Building in public]: Ukazuj pokrok a uvažování průběžně: viditelný pokrok = skončení přestává být neviditelné.
*[Buoyancy]: Vztlak Water pluginu: pontoony (klasika) nebo od 5.7 Default Buoyancy Physics Material + Query and Probe.
*[Burn rate]: Kolik peněz projekt spálí za měsíc či rok; krát délka vývoje = cena projektu.
*[Cable Component]: Vestavěné simulované lano/kabel; konce jdou ukotvit, částice čte Get Cable Particle Locations.
*[Cached pose]: Póza uložená v anim grafu pod jménem, aby šla použít na víc místech (Save/Use Cached Pose).
*[Cache miss]: Data nejsou v cache procesoru a čeká se na hlavní paměť — ve hrách častější brzda než výpočty.
*[Call down, signal up]: Pravidlo Godotu: rodič volá funkce na dětech, dítě posílá signály nahoru.
*[Call to action]: Závěrečná výzva traileru/videa: co má divák udělat teď („Wishlist on Steam"). Právě jedna.
*[Camera director]: Objekt vlastnící pravidla kamery pro oblast: hranice, výjimky, plynulé předání řízení.
*[Camera shake]: Krátký otřes kamery jako asset (amplituda, frekvence, šum); z kódu, notify nebo v sequenceru.
*[Capsule]: Náhledový obrázek hry na Steamu — nejdůležitější kus grafiky celé stránky.
*[Cast]: Přetypování reference na konkrétní třídu; vytváří tvrdou závislost volajícího na dané třídě.
*[Channel]: V Mesh Terrainu malovatelná materiálová vrstva — nástupce landscape layers.
*[CDO]: Class Default Object — výchozí instance každé třídy; umožňuje vzor „třída jako data" bez konstruování.
*[Chaos Cloth]: Realtime fyzika látek: Cloth Asset graf s weight mapou, configem a colliderem z physics assetu.
*[Chooser]: Datová tabulka „za těchto podmínek vyber tenhle asset“; v MM přepíná databáze.
*[CI/CD]: Automatizovaný kontrolní seznam po každém pushi; u her je největší přínos čistý build stroj.
*[Chord extension]: Tón přidaný k triádě nad kvintu (septima, nona…); bohatší zvuk lo-fi, R&B, house.
*[Chord generator]: Web generující smysluplnou akordovou progresi (chordchord.com); rychlý start bez teorie.
*[Chord progression]: Sled akordů tvořící harmonickou kostru; emoci nese pohyb mezi nimi, ne jednotlivé akordy.
*[Cipher]: Typ hráčské postavy: prázdná nádoba bez osobnosti a hlasu; oživí ji až hráčova imaginace.
*[Closing doors]: Iterace od širokého k úzkému; zavřené dveře se znovu neotevírají.
*[Cluster culling]: Nanite zahazuje geometrii po clusterech — buď celý, nebo nic; rozhoduje topologie meshe.
*[Construction Script]: Graf actor blueprintu, který běží v editoru při umístění či změně actoru a při spawnu.
*[Context switch]: Přepnutí jádra mezi vlákny; časté přepínání je čistá režie, nevyvážená jádra blokují ostatní.
*[Cognitive load]: Kolik mozku aktivita žere; nové dovednosti jsou drahé — onboarding = řízení komplexity.
*[Cold open]: Otvírák traileru: prvních 10–15 s nabitých highlighty v rychlých střizích, pak teprve klid.
*[Collision mask]: „Co mě zajímá" — proti vrstvě, která říká „co jsem"; filtr kolizí v konfiguraci místo v kódu.
*[Collision preset]: Předpis, jak objekt reaguje na kolizní kanály: Block / Overlap / Ignore.
*[Constraints]: Nepsané dohody, se kterými musí souhlasit každý nový řádek kódu.
*[Contextual Animation]: Plugin pro synchronizované animace víc účastníků: role, montáže stejné délky, warp pointy.
*[Control Rig Dynamics]: Částicový sekundární pohyb v Control Rigu (5.8): culíky, pouzdra, řetězy; běží i ve hře.
*[Control Rotation]: Rotace player controlleru — úhel pohledu, který hráč ovládá myší nebo páčkou.
*[Cook]: Převod assetů do formátu cílové platformy při balení; čtyři nastavení umí zmenšit balíček o desítky procent.
*[Contact curve]: Animační křivka 0/1 „chodidlo na zemi" — řídí foot pinning; nahradila foot velocity curves.
*[Content]: Vše, co jde opakovat s variacemi: levely, nepřátelé, příběh, odemykatelné věci.
*[Content scheduling]: Kdy a jak často se věci dějí — rytmus obsahu; častá oprava hry, co „má vše a nudí".
*[Context steering]: Pohyb AI: entita ohodnotí všechny směry vahami a vybere nejlepší proveditelný — nezamrzá u zdi.
*[Continuing pose]: „Co by hrálo dál“ — kandidát, kterého musí nová animace v MM porazit cenou.
*[Control Rig]: Grafový rigging a procedurální animace v enginu — běží i za runtime, bez rekompilace.
*[Core loop]: Základní opakovaná smyčka činností, na které hra stojí.
*[Coyote time]: Krátká lhůta po opuštění hrany, během které skok pořád projde (asi 6 snímků).
*[CPU-bound / GPU-bound]: Které zařízení na hru čeká; určuje, kterým směrem vůbec optimalizovat.
*[Custom Depth]: Hloubkový průchod jen pro vybrané meshe, se stencil čísly; materiál ho čte přes SceneTexture.
*[Custom resource]: Vlastní datový typ uložený jako soubor (.tres) — balancování hry bez otevírání skriptů.
*[Custom Time Dilation]: Násobitel času jednoho aktéra: 0 ho zmrazí, zbytek hry běží dál; základ hit stopu.
*[Cyklus napětí]: Horor v pěti krocích: setup → očekávání → pochyby → diverze → akce; a znovu.
*[Data asset]: Asset nesoucí čistá strukturovaná data (konfiguraci) bez logiky.
*[Dataflow]: Grafový systém UE pro zpracování dat assetů, např. přenos rigu a tvarů mezi meshi.
*[Data layer]: Kontejner aktorů (world partition): Unloaded/Loaded/Activated — načítání zón triggerem za běhu.
*[Data-oriented design]: Návrh podle toho, jak leží data v paměti a jak se k nim přistupuje; neplést s data-driven.
*[Data Registry]: Registr konfiguračních dat (data tables) — systémy se ptají jménem místo tvrdých odkazů na tabulky.
*[Data-driven design]: Hodnoty a konfigurace žijí v datech (data assety); logika je jen čte.
*[Data table]: Tabulka řádků podle jednoho structu; konfigurovatelná třída si podle jména řádku dohledá data.
*[Data validation]: Automatická kontrola assetů proti pravidlům projektu — v editoru, při odevzdání i v noci.
*[DAW]: Digital audio workstation — program na tvorbu hudby (FL, Ableton, Reaper, LMMS zdarma).
*[Decal]: Materiál promítnutý na povrch světa (otisky, cákance) — spawnuje se za běhu bez úpravy podkladu.
*[Degenerate strategy]: Dominantní postup, po jehož objevení hra přestává bavit; cíl balancu je ho zabít.
*[Delegate]: Seznam odběratelů zprávy (v BP event dispatcher); engine má vlastní, např. Landed a OnTakePointDamage.
*[Delta time]: Čas od minulého snímku; násobí se jím pohyb, aby nezávisel na výkonu počítače.
*[Demo]: Veřejná verze hry, jejímž úkolem je prodat — ne otestovat (to dělá playtest build).
*[Dependency stack]: Strom závislostí systémů: dole core mechaniky, nahoře škrtnutelné obohacení.
*[Design by constraint]: Návrh z omezení: nejdřív zvol limity (žádný příběh, jedna obrazovka), nápad hledej uvnitř nich.
*[Design pattern]: Pojmenované řešení opakujícího se problému v kódu; katalog Gang of Four (1994), tři rodiny.
*[Design pillars]: 2–3 pojmy o tom, co má hráč cítit; váha pro každé rozhodnutí. Žánr ani art style pilíř není.
*[Device profile]: Hierarchická sada nastavení a CVarů pro platformu; engine si ji sám nevybere — musíš ji zvolit.
*[Devlog]: Video či zápis o vývoji vlastní hry — marketingový kanál a žánr s vlastním řemeslem.
*[Diegetic UI]: UI, které je součástí herního světa (obrazovka televize, displej zbraně) — ne vrstva přes obrazovku.
*[Direct Mesh Controls]: Controly rigu ovládané tahem přímo za povrch postavy, ne za kroužky kolem ní (UE 5.8).
*[Distance field AO]: AO z mesh distance fields; tiše se zapíná spolu s movable skylightem, takže ho platíš bez vědomí.
*[Difficulty curve]: Průběh obtížnosti hry v čase; skládá se z novelty (učení nového) a mastery (zvládání známého).
*[Disonance]: Dojem napětí či drsnosti při znění tónů; opak konsonance, spojitá páka napětí.
*[DLSS]: NVIDIA upscaler: render v nižším rozlišení + AI dopočet; s Frame Generation a Reflex; kompenzuj mip bias.
*[DNA soubor]: Popis vyřešené MetaHuman hlavy; vzniká krokem Save Pose a je vstupem pro texturu i doplňky.
*[Dogfooding]: Používání vlastního produktu jako jeho první zákazník — nejlevnější test, že unese reálnou práci.
*[Do Once]: Blueprint uzel, který propustí exekuci jen poprvé, dokud ho něco nezresetuje.
*[Dot product]: Skalární součin jednotkových vektorů = kosinus úhlu: 1 stejný směr, 0 kolmost, −1 protisměr.
*[Draw call]: Příkaz CPU pro GPU „vykresli tohle"; šetří se instancingem a sdílením materiálů (trim sheety).
*[Dynamic Material Instance]: Runtime kopie materiálu s parametry měnitelnými z kódu (Set Parameter Value); žije per objekt.
*[Dynamic resolution]: Rozlišení snižované za běhu, aby engine udržel cílový frame time (typicky 55–75 %).
*[Early access]: Placený předběžný přístup k nedokončené hře s příslibem dalšího vývoje.
*[ECS]: Entity Component System — entity jako skládanky dat, logika v systémech nad entitami stejného složení.
*[Edit layer]: Vrstva úprav Landscapu (sculpt i paint); nástroje pracují s aktuálně vybranou — kopie z jiné = prázdno.
*[Editor script]: Skript, který běží v editoru místo ve hře; generuje boilerplate nebo hlídá konzistenci dat.
*[Editor Utility Widget]: Blueprint UI běžící v editoru — vlastní nástroj bez psaní pluginu.
*[Effect type]: Asset s pravidly cullingu pro Niagara systémy; bez něj se částice simulují i mimo obraz.
*[Eigenvektor]: Směr, který transformace nevychýlí — jen natáhne či zkrátí o eigenvalue.
*[Elemental tetrad]: Schellovy čtyři části hry: estetika, mechaniky, technologie, příběh — iteruj přes všechny.
*[Elevator pitch]: Popis hry na délku jízdy výtahem, nejčastěji „X meets Y"; nesmí být redundantní ani nespojitelný.
*[Enum]: Typ s pevným seznamem pojmenovaných hodnot (směr, druh klíče); Switch, Select, klíč mapy.
*[Environmental storytelling]: Vyprávění prostorem: rozmístění objektů a stopy používání říkají, co se tu stalo.
*[EQ]: Zesílení či potlačení konkrétních frekvencí; čištění šumu a prosazení zvuku v mixu.
*[Equipment Instance]: Objekt nasazeného kusu vybavení — pamatuje si, co spawnul a změnil, aby šlo vše vrátit.
*[Equity]: Podíl na firmě — nesplácí se jako půjčka, ale už se nikdy nevrátí.
*[Eulerovy úhly]: Rotace jako yaw/pitch/roll v pevném pořadí — intuitivní, ale hrozí gimbal lock.
*[Euklidovský rytmus]: Zápis (n,k) — rozprostři n hitů rovnoměrně do k kroků; algoritmus původem z fyziky.
*[EV100]: Jednotka expozice; min=max v PPV zamkne auto-exposure. 1 = modrá hodina, interiér 5–7, den ~13.
*[EVDB]: Komprimovaný volumetrický asset (Expanse): static mesh, který místo trojúhelníků nese objem.
*[Event bus]: Globální kanál událostí — autoload se signály, které zajímají víc nepříbuzných systémů.
*[Event dispatcher]: Rádio mezi Blueprinty: vlastník zavolá, všichni bindnutí posluchači dostanou event.
*[Event Tick]: Blueprint event volaný každý snímek; polling, kterému se dobrý návrh vyhýbá.
*[Export template]: Předkompilované běhové prostředí Godotu pro cílovou platformu; stahuje se zvlášť.
*[Expresivní mechanika]: Nepomáhá vyhrát, mění chuť hry: pohladit kočku, emoty — rozdíl mezi dobrou a výbornou hrou.
*[Extremistan]: Prostředí, kde jeden vzorek převáží celý zbytek souboru (prodeje her).
*[Fallback mesh]: Klasická verze Nanite meshe pro místa, kde Nanite nejde (odrazy, ray tracing, starší HW).
*[File locking]: Zamčení souboru tím, kdo na něm pracuje; řešení pro binární assety, které se nedají sloučit.
*[Fill]: Zahuštění rytmu na konci fráze před další sekcí; opakem je prázdno.
*[Find the fun]: Fáze prototypování: experimentuj s jádrem, dokud nebaví samo — hraješ si s ním i mimo práci.
*[Flipbook]: Mřížka snímků v jedné textuře, kterou materiál přehrává jako animaci.
*[Flow]: Stav plného zaujetí, kdy výzva odpovídá dovednosti (Csíkszentmihályi); pásmo nejefektivnějšího učení.
*[Foley]: Ruční výroba zvukových efektů z reálných předmětů, když knihovna nestačí.
*[Foot placement]: Procedurální usazení chodidel: IK na svazích, špendlení došlapů, tlumení roota na hrbolech.
*[Forward rendering]: Vykreslování bez G-bufferu: objekt se nasvítí rovnou při kreslení; typické pro VR a slabý hardware.
*[Four-on-the-floor]: Bicí groove s kopákem na každé ze čtyř dob; základ house, proti němu synkopa.
*[Frame data]: Popis útoku po snímcích — nápřah, aktivní snímky, zotavení; ke každému snímku vlastní vlastnosti.
*[FM syntéza]: Syntéza, kde jeden signál moduluje frekvenci druhého; klíčový parametr je harmonicita.
*[Fragment]: Objekt připojující k položce kus dat a funkčnosti — kompozice místo jedné obří třídy.
*[Frame time]: Čas na jeden snímek v ms; 60 FPS = rozpočet 16,6 ms. Sčítá se lineárně, na rozdíl od FPS.
*[Fresnel]: Materiálový uzel, který roste k obrysu objektu z pohledu kamery; rim light, záblesk po kraji.
*[FX budget]: Rozpočet na částice, který za běhu stahuje culling; typické selhání je oscilace, léčí ji decay rate.
*[Game Design Document]: Dokument s návrhem hry; funguje, jen když se do něj tým skutečně vrací — forma je vedlejší.
*[Game feel]: Hmatový dojem z ovládání: odezva, váha, šťavnatost interakcí. „Game feel je cheat code."
*[Game Instance]: Objekt žijící od spuštění aplikace po její konec — přežívá přechody mezi levely.
*[Game jam]: Časově omezená akce (hodiny až dny), během níž vzniká celá malá hra.
*[Gameplay Debugger]: Ladicí vrstva ve hře (apostrof): navmesh, cesta AI, behavior tree, EQS a percepce.
*[Game State]: Stav probíhající partie, dostupný všem a replikovaný; domov pro event manager.
*[Gameplay loop]: Smyčka činností, kterou hráč opakuje; popisný nástroj game designu.
*[Gameplay tag]: Hierarchický identifikátor stavu (Status.MovementBlocked.Stunned) — náhrada boolean špagety.
*[Garbage collection]: Automatický úklid paměti; zničené objekty jsou dočasně „pending kill".
*[GAS]: Gameplay Ability System — schopnosti, atributy a efekty; hodnota ze základu a odebíratelných modifikátorů.
*[GASP]: Game Animation Sample — Epicův živý ukázkový projekt gameplay animace: 500+ animací, MM, traversal, Mover.
*[Gauntlet]: Automatizační framework UE: spouští hru na cílových zařízeních a řídí na nich testy.
*[GDD]: Game design document — dokument s návrhem hry; funguje, jen když se do něj skutečně vracíš.
*[GDScript]: Skriptovací jazyk Godotu — blízký Pythonu, gradually typed, navržený pro strom scény.
*[Genre descoping]: Jeden prvek velkého žánru nafouknutý na celou hru (TD z RTS, backpack z Diabla).
*[Gestalt]: Psychologie celku: člověk čte celý obraz a z uspořádání odvozuje vztahy mezi částmi.
*[Ghost note]: Tišší verze téhož bicího na slabé dělené době; hustota bez důrazu.
*[Gimbal lock]: Ztráta stupně volnosti: prostřední osa na 90° zarovná zbylé dvě a rotace se slepí.
*[Git LFS]: Rozšíření gitu pro velké binárky: v repozitáři odkaz, obsah zvlášť; na GitHubu 1 GB zdarma.
*[Global Distance Field]: Hrubé sloučené pole vzdáleností k povrchům celé scény kolem kamery (Lumen, DFAO, Niagara).
*[Global Time Dilation]: Násobitel rychlosti času celé hry; zpomalí všechno včetně animací, hodí se i na ladění.
*[GOAP]: Goal-Oriented Action Planning — AI si posloupnost akcí k cíli poskládá sama za běhu.
*[God class]: Antipattern: třída, do které se postupně nastěhuje logika všech ostatních.
*[Gradual typing]: Typy jsou volitelné a přidávají se postupně; statický zápis hlásí chyby před spuštěním.
*[Granulární syntéza]: Rozsekání zvuku na krátká zrna a jejich přeskládání — z jednoho vzorku cokoli.
*[Graybox]: Prototyp/blockout ze šedých primitiv — správný pro testování mechanik, špatný pro testování prodejnosti.
*[Groom]: Vlasy/srst z pramenů (strands); vlastní LODy — při skládání postavy je drží LOD Sync komponenta.
*[Halting problem]: Turing 1936: obecně nejde rozhodnout, zda program skončí — kompas hranic řešitelnosti.
*[Hard coding]: Hodnoty zadrátované přímo v kódu; v produkci antipattern, v prototypu ctnost.
*[Hard reference]: Přímý odkaz, který s sebou tahá vše, co cíl referencuje — do paměti i do buildů.
*[Harmonická řada]: Alikvóty struny/píšťaly jako celočíselné násobky základní frekvence; zdroj západních intervalů.
*[HDRI]: Panorama s vysokým dynamickým rozsahem — obloha a světlo místa; backdrop + skylight z téže mapy.
*[Height mapa]: Černobílá textura kódující výšku terénu jasem pixelu.
*[Hitch]: Jednotlivý výrazně dlouhý snímek — škubnutí, které průměrné FPS schová.
*[Hit flash]: Krátké rozsvícení či zbarvení zasaženého jako potvrzení zásahu; výměnou materiálu nebo overlayem.
*[Hit stop]: Krátké zamrznutí hry při zásahu (asi 1/20–1/10 s) — dodá útoku váhu a čitelnost.
*[Hitbox]: Oblast, která při zásahu působí — proti hurtboxu, který zásah přijímá.
*[Herní vlákno]: Vlákno s herní logikou, AI, fyzikou a blueprinty; v stat unit hodnota game.
*[HLOD]: Sloučená náhrada za skupinu objektů v dálce; skrytá HLOD proxy může pořád vrhat stín.
*[Hook]: Prvek, který hru prodá na první pohled — mechanika, premisa nebo obraz, co zastaví palec při scrollování.
*[Horizontal slice]: Celá hra skrz zlomek systémů — pro pomalé hry o odemykání, kde vertical slice selhává.
*[Hurtbox]: Oblast, která zásah přijímá (protějšek hitboxu); menší než postava odpouští, vypnutá = nezranitelnost.
*[Hydratace]: Přepnutí objektu z levné instance na plnohodnotného aktéra podle vzdálenosti — a zpátky.
*[Hitch resiliency]: Schopnost potrubí pohltit zásek bez zahozeného snímku; platí se vstupní latencí.
*[HUD]: Heads-up display — informace zobrazené přes gameplay: zdraví, munice, minimapa, cíle.
*[Idea reservoir]: Zásobník NEschválených nápadů před to-do; taháš, až se ukáže, co ve hře funguje.
*[IK]: Inverzní kinematika: řetěz kostí se natočí tak, aby koncová kost dosáhla cíle.
*[Iluze plynulosti]: Pocit „rozumím" z plynulého čtení; zhroutí se při vysvětlování krok za krokem.
*[Inertialization]: Blend, který z rychlosti původního pohybu dopočítá plynulý přechod místo míchání dvou póz.
*[ISM]: Instanced Static Mesh — shodná geometrie i materiál v jednom draw callu; HISM přidává LODy.
*[Indexical storytelling]: Vyprávění stopami a náznaky; hráč si příběh složí sám (Clara Fernández-Vara).
*[Impostor]: Nejagresivnější LOD: asset nahrazený obrázkem otáčejícím se s kamerou.
*[Inheritance]: Dědičnost: děti přebírají proměnné, funkce a komponenty rodiče. Lakmusový test: „is it a?"
*[Input buffering]: Vstup těsně před platností se zapamatuje a provede hned, jak to jde (skok před dopadem).
*[Instance]: Konkrétní umístěný výskyt assetu v levelu.
*[Instanced Actors]: Systém (5.5+): svět z levných instancí; objekty u hráče se swapnou na plné Blueprint actory a zpět.
*[Integer overflow]: Přetečení celého čísla — hodnota přeroste strop (asi 2,1 mld.) a překlopí se do záporných.
*[Input latency]: Od vstupu k fotonu; v `stat unit` jen od navzorkování vstupu po flip back bufferu.
*[Integer scaling]: Zvětšování celými násobky (2x, 3x); jediný způsob, jak udržet pixel art ostrý.
*[Interval]: Vzdálenost dvou tónů v půltónech; nese emoci (kvinta hrdinská, malá sexta tajemná).
*[Invariant]: Podmínka platná v daném bodě programu vždy, ať se tam běh dostal jakkoli.
*[Invisible wall]: Neviditelná kolize tam, kde vizuálně nic nebrání — nejhorší způsob ohraničení mapy.
*[Item Instance]: Konkrétní kus položky v inventáři — nese stav, který definice mít nemůže (použití, staty).
*[Iterace]: Jedno kolo smyčky uprav → otestuj → vyhodnoť; hry nevznikají tahem, ale koly.
*[Izometrie]: Perspektiva bez úběžníku — vzdálené objekty se nezmenšují, scéna je čitelná v hloubce.
*[Jitter]: Mikro-škubání z rozhoupaného delta timu — nastane, i když nespadne ani jeden snímek.
*[Juice]: Feedback vrstva prodávající akce: shake, particles, squash — signál, že svět akci zaznamenal.
*[Jump scare]: Úleková špička: hlasité 2–3 na hodinu, tiché dle potřeby; stavěj jako mini-dramaturgii.
*[Kanban]: Řízení práce kartami To Do → Doing → Done: jeden vlastník na kartu, limit rozdělanosti.
*[Keep Triangle Percent]: Nanite: kolik procent zdrojových trojúhelníků se uloží; zbytek zmizí z balíčku.
*[Keyboard ghosting]: Hardwarový limit klávesnice: u některých kombinací kláves jeden vstup nedorazí do hry.
*[Klonování hlasu]: Model natrénovaný na tvém hlase, který přezpívá cizí výkon tvou barvou.
*[Knockback]: Odhození zasaženého směrem od útoku; potvrzuje sílu rány (Launch Character, impulz).
*[Konsonance]: Dojem klidu a souznění tónů; opak disonance, „domov" harmonie.
*[Kontrapunkt]: Skládání nezávislých melodií, které fungují zároveň; odděluje profíky od amatérů.
*[Kumulativní výhoda]: Kdo je vidět, je víc vidět — úspěch se sám zesiluje bez ohledu na kvalitu.
*[Kvintový kruh]: Dvanáct tónů po kvintách; ve skutečnosti spirála, ne kruh.
*[Kvaternion]: Rotace čtyřmi čísly: bez gimbal locku, hladký slerp — výměnou za nulovou intuici.
*[Landmark]: Výrazný orientační bod levelu; v postupu „landmark napřed" první rozhodnutí návrhu prostoru.
*[Landscape]: Klasický terén UE: height mapa, jen nahoru/dolů; produkční volba, dokud Mesh Terrain nedozraje.
*[Layered Blend Per Bone]: Anim uzel míchající dvě pózy od zadané kosti nahoru — vrstvení horního těla přes locomotion.
*[Layered move]: Dočasný zdroj pohybu v Moveru (dash, skok) — nástupce root motion sources; víc jich běží naráz.
*[Layering]: Vrstvení více zvuků na tutéž linku, aby zněla velce a plně.
*[Legibilita]: Čitelnost textu: jak snadno oko rozliší písmena a slova. Není to velikost písma.
*[Leitmotiv]: Melodie svázaná s postavou/místem, která se vrací a mění podle scény; pojivo světa.
*[Lerp]: Lineární interpolace A + (B − A)·t: plynulý přechod čehokoli, co jde vyjádřit čísly.
*[Level instance]: Znovupoužitelný sub-level; Packed Level Actor = totéž pro static meshe (převod na instance).
*[Level Sequence]: Asset sequenceru — časová osa se stopami actorů, kamer a událostí, přehrávaná i za běhu.
*[Level streaming]: Načítání a uvolňování částí světa za běhu; persistent level je rám, sub-levely obsah.
*[LFO]: Pomalý oscilátor otáčející donekonečna zvoleným knobem (vibrato, wobble, pohyb filtru).
*[Liminální prostor]: Veřejný prostor bez lidí a účelu — skoro normální, a proto zneklidňující.
*[Lightweight emitter]: Niagara emitter s pevnou funkčností: řádově levnější a řádově omezenější (bez dynamických vstupů).
*[Line of action]: Pomyslná linie procházející pózou; rovná a čitelná = jasný pohyb.
*[Line Trace]: Raycast — neviditelný paprsek hledající kolize na své dráze.
*[Linear grammar]: Gramatika PCG: string symbolů řídí rytmus modulů podél splinu — sekvence, počty, opakování.
*[Linked anim graph]: Samostatný anim graf připojený jako modul; přes tag na něj sáhnou komponenty zvenčí.
*[Live coding]: Tvorba hudby psaním kódu, který zní okamžitě; skládání a vystoupení splývají.
*[Live Link]: Streamování dat do enginu (mocap, kamery); Live Link Hub od 5.8 zpracuje i offline video na capture data.
*[Locomotor]: Control Rig uzel procedurální chůze: došlapy počítá dynamicky — foot sets, fázové offsety, žádné klipy.
*[Locus of control]: Kde hledáš řídicí sílu jednání: uvnitř (rozhoduju sám), či venku (čekám na dotlačení).
*[Look ahead]: Předsazení kamery za pozorností hráče: směr pohybu, fáze skoku (nad hlavu → pod nohy).
*[Loose coupling]: Třídy na sobě závisejí co nejméně — komunikace přes smlouvy a eventy, ne tvrdé reference.
*[Low-fi prototyp]: Schválně laciný prototyp (náčrt na papíře, čmáranice) — nízké úsilí zve k upřímné kritice nápadu.
*[Low-pass filtr]: Filtr propouštějící nízké frekvence a ubírající vysoké; z bohaté vlny udělá bas/pad.
*[Lumen]: Realtime GI a odrazy v UE5; orientační rozpočet ~4 ms na 60 FPS, ~8 ms na 30.
*[Ludonarativní disonance]: Nesoulad příběhu a gameplaye (hodný hrdina, stovky mrtvých). Neutrální nástroj — i humor.
*[Ludus a paidia]: Caillois: hra podle pravidel vs. volné blbnutí. Holá hra = moc ludus, málo paidia.
*[Map (dictionary)]: Struktura klíč → hodnota: čitelný klíč místo indexu; překlep klíče = tichý bug.
*[Marching cubes]: Z 3D skalárního pole mesh: krychle z 8 sousedů, 256 případů, předpočítané polygony.
*[Markerless mocap]: Motion capture z obyčejného videa bez markerů a obleku.
*[Market research]: Průzkum trhu: žánrové výdělky (medián!), tagy, recenze konkurence — objektivita proti zamilovanosti.
*[Markovův řetěz]: Stavy a pravděpodobnosti přechodů; memoryless — pro další krok stačí současný stav.
*[Mass Entity]: ECS framework pro tisíce entit (davy, doprava) — City Sample i MetaHuman Crowd; entity nejsou actory.
*[Material function]: Znovupoužitelný blok materiálové logiky; s material attributes I/O funguje jako vrstva.
*[Material Instance]: Potomek materiálu, který mění jen vystavené parametry (barva, textura); graf zůstává u rodiče.
*[Matice]: Lineární transformace: sloupce říkají, kam se přesunou osy; násobení = skládání transformací.
*[MAYA]: Most Advanced Yet Acceptable — nejpokročilejší varianta, kterou publikum ještě přijme.
*[McNamarův klam]: Co jde snadno změřit, se prohlásí za jediné důležité; metriky rostou, věc se prohrává.
*[MCP]: Model Context Protocol — AI agent s kontextem a kontrolou editoru; od 5.8 nativně v UE (3 pluginy).
*[MDA framework]: Mechanics→Dynamics→Aesthetics: kód → chování hráče → pocity; designér sahá jen na první článek.
*[Mechanika]: Jednotka gameplaye z pravidel: sloveso hráče (skoč, seber) působící na herní svět.
*[Mediator pattern]: Prostředník, přes kterého aktéři komunikují místo napřímo (věž místo letadel).
*[MegaLights]: Systém UE od 5.5, který zlevňuje scény s velkým počtem stínících světel.
*[Mesh distance field]: Pole vzdáleností k povrchu meshe — efekty obtékající geometrii (Distance to Nearest Surface).
*[Mesh to MetaHuman]: Převod cizího meshe na MetaHumana s rigem podle standardu Epicu; od 5.8 i celé tělo.
*[MetaHuman]: Epicův systém fotorealistických postav; Performance asset zpracuje video na animaci těla i obličeje.
*[MetaHuman Animator]: Nástroj, který z natočeného výkonu spočítá animaci MetaHumana; od 5.8 i tělo.
*[MetaHuman Collection]: Asset pro davy MetaHumanů z malé sady dílů; v dálce instance, u kamery plný MetaHuman.
*[MetaSounds]: Grafový audio systém UE5 — nástupce Sound Cues; parametry za běhu přes audio komponentu.
*[Mip mapa]: Zmenšené kopie textury; bias +1 = poloviční hrana. Base color snese víc, detail nese normálka.
*[Mixels]: Míchání různě velkých pixelů v jedné scéně; v pixel artu skoro vždycky vypadá špatně.
*[Moderovaný playtest]: Test, u kterého sedíš: díváš se, mlčíš, čteš chování — a ptáš se v místě tření.
*[Modifier stack]: Vrstvené nedestruktivní úpravy; každou lze dodatečně měnit, přesouvat či smazat.
*[Montage section]: Pojmenovaný úsek anim montáže; navazování sekcí lze za běhu přesměrovat.
*[Monte Carlo metoda]: Simuluj tisíce náhodných běhů a odpověď přečti z histogramu — místo výpočtu, který nejde.
*[Moodboard]: Sbírka referencí ukazující tón a směr dřív, než vznikne první vlastní kresba.
*[Morph target]: Uložená deformace vrcholů meshe (blend shape) zapínaná váhou — výrazy a korektivy.
*[Motion matching]: Dotazový výběr animací: každý frame hledá v databázi pózu nejlépe navazující na trajektorii.
*[Motion Warping]: Ohnutí root motion animace, aby trefila cílový transform; okno řídí notify state v montáži.
*[Motiv]: Krátká zapamatovatelná dvou- až pětitónová buňka melodie; jde ji opakovat, obrátit, posunout.
*[Movement Mode]: Modulární objekt Moveru pro jeden režim pohybu; vyměnitelný a rozšiřitelný i v Blueprintu.
*[Mover]: Nástupce Character Movement Componentu: replikuje vstupy, modulární módy, pravdivá trajektorie pro MM.
*[Multithreading]: Rozdělení práce na víc vláken, aby dlouhý výpočet neblokoval běh hry.
*[MVP]: Minimum Viable Product: nejmenší verze doručující jádro hodnoty — jen core loop, dezert počká.
*[Mód hry]: Struktura hraní přes sezení (roguelike, metroidvania) — neříká, co držíš v rukou.
*[Nav Agent]: Profil (poloměr, výška), pro který se generují nav data; každý další agent = další sada dat.
*[Navigation Query Filter]: Pravidla pro výpočet cesty: zvýhodní, zdraží nebo vyřadí oblasti a flagy navigace pro daný dotaz.
*[N-gon]: Polygon s víc než čtyřmi hranami; na ploché ploše neškodný, na zakřivené zdroj chyb.
*[N-key rollover]: Schopnost klávesnice nahlásit N současně stisknutých kláves; obrana proti ghostingu.
*[Nanite]: Virtualizovaná geometrie UE5 — detail meshů se dynamicky přizpůsobuje kameře.
*[Narrative design]: Návrh vyprávění integrovaný s herním designem — ne „spisovatel dopíše cutscény".
*[Nav Mesh]: Navigační síť, ve které AI počítá cesty; do levelu jako Nav Mesh Bounds Volume, náhled klávesou P.
*[Nearest-neighbor filtering]: Vzorkování textury bez vyhlazování — pixel zůstane pixelem (nutnost u pixel artu).
*[Network Prediction]: Rollback framework UE — síťová větev Moveru: klient posílá jen vstupy, rollback celého okolí naráz.
*[Niagara Data Channel]: Gameplay zapisuje data do kanálu, jediný Niagara systém z nich spawnuje částice — ne systém per událost.
*[Niagara Fluids]: Plugin simulačních šablon; Grid 2D SW Particle Collisions = interaktivní hladina s collider tagy.
*[Normal mapa]: Textura kódující odraz světla — reliéf bez přidání polygonů, obvykle z baku.
*[Normalizace vektoru]: Zmenšení vektoru na délku 1 se zachováním směru: složky děleno délkou (odmocnina!).
*[Object pooling]: Zásoba předem vytvořených objektů, které se recyklují místo neustálého vytváření a rušení.
*[Oblique]: Nakloněná perspektiva: vidíš horní i boční stranu objektů (Stardew Valley).
*[Obrat akordu]: Tentýž akord s jiným pořadím tónů (nota posunutá o oktávu); hladší přechody.
*[Observer pattern]: Objekty se přihlásí k odběru událostí zdroje; v UE doslova Event Dispatcher.
*[Oktáva]: Vzdálenost tónu a jeho příštího výskytu; poměr 2:1, nejkonsonantnější interval.
*[Octree]: Rekurzivní dělení prostoru na osminy; adaptivní varianta sleduje složitost místo souřadnic.
*[Onboarding]: Prvních pár minut, kdy se hráč učí hru a rozhoduje se, jestli zůstane.
*[One-pager]: Pitch na jednu stránku: obrázek, co chci vyrobit a jak vypadá úspěch.
*[One File Per Actor]: Každý aktér ve vlastním souboru; bez toho nemůže na mapě pracovat víc lidí naráz.
*[One-way door]: Rozhodnutí drahé na reverz (žánr, API, engine) — dělá se vědomě, s premisami; opak: two-way door.
*[Orchestrace]: Rozdělení hudby mezi nástroje a smíchání do barvy; až po melodii, harmonii a kontrapunktu.
*[Oscilátor]: Zdroj surového zvuku v synthu; tvar vlny (sinus/pila/obdélník) určuje barvu a alikvóty.
*[Outer]: Objekt, ke kterému je UObject přivázaný — s ním žije a s ním ho uklidí garbage collector.
*[Overdraw]: Tentýž pixel kreslený vícekrát (překryvy listí, masky) — vizualizace v Nanite overdraw view.
*[Overlay material]: Materiál vykreslený přes základní materiál meshe (slot Overlay Material); nevidí WPO pod sebou.
*[Overlay state]: Enum-řízená vrstva pózy horního těla přes locomotion — drž předmět bez vlastních pohybových animací.
*[Pacing]: Rytmus zážitku: střídání napětí a klidu, akce a ticha, učení a mistrovství v čase.
*[Palette swap]: Barevná varianta spritu vyrobená přemapováním palety shaderem, ne překreslením.
*[Parallax]: Vrstvy pozadí pohybující se pomaleji než kamera; iluze hloubky a vnímané velikosti.
*[Parallax occlusion mapping]: Pixel-shader hloubka: posun UV dle kamery a height mapy; bez geometrie, siluety neumí.
*[Pareto distribuce]: Mocninné rozdělení: malá menšina případů drží většinu celkové hodnoty.
*[Particle system]: Emitter vystřelující sprity či modely a řídící jejich chování v čase.
*[Packed Level Actor]: Skupina aktérů zabalená do assetu vykresleného jako instance; hranice rozhodují o streamovací buňce.
*[Pass by reference]: Předání odkazu místo kopie: změny vidí všichni sdílející originál. Kopíruju, nebo sdílím?
*[Passing chord]: Průchozí akord mezi dvěma hlavními, který přemostí a rozbije jejich tok.
*[Pawn Sensing]: Jednoduchá smyslová komponenta (kužel zraku + sluch) s gizmem ve viewportu; event On See Pawn.
*[PBR]: Physically Based Rendering — materiál z vlastností (albedo, roughness, metallic), bez zapečeného světla.
*[PCG]: Procedural Content Generation — UE framework pro procedurální osazování světa.
*[PCG Mode]: Editorový režim (5.7): kreslení PCG grafů přímo do světa splinou, štětcem nebo volumem.
*[Per-instance custom data]: Hodnoty nastavitelné pro každou instanci zvlášť — variace bez unikátních materiálů.
*[Pedal tone]: Tón znějící pod celou progresí, který se nemění (prodleva); sjednotí přechody.
*[Persistence key]: Záznam o změně světa uložený mimo objekt, kterého se týká — přežije odložení z paměti.
*[Persistent level]: Hlavní level, pod kterým žijí streamované sub-levely; nejde unloadnout.
*[Physical Animation Component]: Motory kloubů táhnou simulované kosti k animované póze — základ active ragdollu.
*[Physical Material]: Asset s vlastnostmi povrchu vč. Surface Type — systémy přes něj poznají, po čem stojíš.
*[Physics Asset]: Fyzikální kostra meshe: kolizní těla per kost + constrainty s limity — bez něj není ragdoll.
*[Physics Constraint]: Kloub mezi fyzikálními těly: linear/angular limity + motory; v assetu i jako actor ve scéně.
*[Physics Control]: Komponenta držící simulovaná tělesa u cíle laditelnou pružinou — fyzikální, ale ovladatelné.
*[Pitch deck]: Prezentace hry, která ještě neexistuje; simuluje první kontakt zákazníka s nápadem.
*[Pivot]: Vztažný bod objektu (rotace, scale, přichytávání); v enginu opravitelný přes modeling mode Edit Pivot.
*[Player Camera Manager]: Objekt player controlleru spravující výsledný pohled hráče: zatmívačky, otřesy kamery.
*[Point cloud]: Mračno bodů z laserového skenu; barva sedí na bodu, detail se vrství místo aby nahrazoval.
*[Pixel-perfect]: Celočíselné škálování pixel artu; ve slepém testu necelé faktory skoro nepoznáš.
*[Placeholder]: Provizorní asset držící místo finálnímu; schválně ošklivý, aby nesváděl k ladění.
*[Player State]: Objekt s daty jednoho hráče (inventář, skóre) nezávisle na pawnovi; v multiplayeru se replikuje.
*[Playtest]: Testování hry skutečnými hráči za účelem zpětné vazby.
*[Pole vector]: Cíl, který IK řešiči určuje směr ohybu prostředního kloubu (loket, koleno).
*[POM]: Parallax occlusion mapping — pixel-shader iluze hloubky posunem UV; na hranách řeže, siluety neumí.
*[Polymetr]: Souběžné rytmické řady různé délky; dlouhý groove z krátkého zápisu.
*[Polyrytmus]: Dva vzorce ve stejném metru: první doby sedí, dělení ne.
*[Pose Asset]: Asset s pojmenovanými pózami, které AnimBP vybírá a míchá podle jména (např. úchopy).
*[Pose Search Database]: PSD — kolekce animací jednoho typu pohybu, ve které Motion Matching hledá pózy.
*[Pose Search Schema]: Definice, co MM měří: kanály (trajektorie, kosti) s vahami; ladí se experimentem.
*[Pose Snapshot]: Zmrazení pózy skeletu jako blendovací zdroj v AnimBP — most z ragdoll fyziky zpět do animace.
*[Post-process AnimBP]: AnimBP meshe vyhodnocovaný po hlavní animaci — vrstvení look-atu a korekcí; vázaný na skeleton.
*[Postmortem]: Ohlédnutí za dokončeným projektem: co fungovalo, co ne a proč — nejhutnější studijní žánr gamedevu.
*[Premature optimization]: Optimalizace před důkazem, že je potřeba; deformuje workflow a žere čas.
*[Press kit]: Balíček pro novináře: popis, kontakty, loga, screenshoty, trailer v plné kvalitě na jednom místě.
*[Procedural Vegetation]: Editor stromů v enginu (5.7+): graf uzlů od presetu/growere po export s Nanite foliage a větrem.
*[Process mode]: Vlastnost nodu určující, jestli běží při pozastaveném stromu scény; ve výchozím stavu se dědí.
*[Producent]: Ve hrách project manager: timeline, seznam úkolů, kdo co dělá a kdo je volný.
*[Profiling]: Měření, kde se ve snímku ztrácí čas; napřed zjisti vyčerpaný rozpočet, pak volej nástroj.
*[Prokletí znalosti]: Expert na vlastní hru si neumí dát zážitek nováčka — tření vidí až playtest.
*[Průběžná obtížnost]: Jak moc tě hra tlačí k prohře; vyrábí stres a úlevu. Upgrade zdraví ji snižuje.
*[Předznamenání]: Kolik dob je v taktu a jaká nota je jedna doba (4/4, 3/4, 6/8).
*[Půltón]: Nejmenší vzdálenost dvou sousedních tónů (E–F); stavební jednotka stupnic.
*[PSO]: Pipeline state object; chybí-li, kompiluje se shader za běhu na CPU a hra sekne.
*[Pure function]: Funkce bez exec pinů, která jen vrací hodnotu; počítá se znovu při každém čtení výstupu.
*[Quad]: Čtyřúhelníková buňka mřížky meshe; jednotka rozlišení terénu.
*[Quad utilization]: Podíl využité práce ve čtverci 2×2 pixely — jednotce, po které GPU plánuje pixel shader.
*[Race condition]: Chyba pořadí inicializace: kód čte data, která jiný kód ještě nenastavil (BeginPlay actorů!).
*[Random pitch variation]: Náhodný posun výšky při každém přehrání; ubíjí mechanickou repetici opakovaného zvuku.
*[Raster bin]: Nanitová dávka se shodným stavem rasterizace; cenu určuje rozmanitost materiálů, ne počet meshů.
*[Recall priming]: Nenápadné nápovědy v prostředí, které hráči zpřístupní správnou vzpomínku těsně před puzzlem.
*[Recoup]: Splacení investice vydavatele z tržeb, než se vývojáři začne vyplácet jeho podíl.
*[Redirector]: Ghost soubor po přesunu assetu; před smazáním složky spusť Update Redirector References.
*[Referenční transparentnost]: Volání funkce lze nahradit její hodnotou beze změny programu — žádné skryté závislosti.
*[Refundace]: Vrácení peněz za hru; první srážka z hrubé tržby před podílem obchodu a daněmi.
*[Rekurze]: Funkce volající sama sebe: base case + zmenšování problému + skok důvěry.
*[Relativní dur]: Durová tónina se stejnými tóny jako daná mollová; třetí stupeň moll vlévá radost.
*[Render target]: Textura, do které engine vykresluje za běhu — jde do ní i vypéct materiál.
*[Renderovací vlákno]: Čas CPU na přípravu práce pro GPU (culling, LODy, draw cally) — ne čas GPU.
*[Retargeting]: Přenos animace z jedné kostry na jinou s odlišnými proporcemi (IK Rig + Retargeter).
*[Retopologie]: Přestavba geometrie na čistou síť pro rig/animaci; AI cesty: decimace+bake, smart low poly, remesher.
*[Retrieval practice]: Učení vybavováním: odvrať zrak a vzpomínej — poráží opakované čtení.
*[Retriggerable Delay]: Delay restartovaný každým dalším spuštěním — doběhne až po klidu; „ztráta zájmu" AI.
*[Reverb]: Odraz zvuku od prostředí (dozvuk); slepí zvuky nebo vyjádří prostor (chodba, kaňon).
*[Rewind Debugger]: Nahraje běh hry a nechá tě scrollovat časem: co hrálo, proč to MM vybralo, jak rozhodl State Tree.
*[RHI]: Render Hardware Interface — vrstva mezi rendererem a grafickým API dané platformy.
*[Rigging]: Vložení kostry do modelu a nastavení, jak kosti ovládají mesh.
*[RigLogic]: Knihovna vyhodnocující rig MetaHumana podle DNA; open source (MIT) v MetaHuman DevKitu.
*[RITE]: Rapid Iterative Testing and Evaluation: jeden tester → oprav vážné problémy → další tester.
*[Roguelike]: Žánr postavený na opakovaných bězích, smrti jako součásti smyčky a procedurální generaci.
*[Roughness]: Drsnost povrchu v PBR; zároveň práh, pod kterým Lumen trasuje dedikované odrazové paprsky.
*[Root motion]: Pohyb uložený v root kosti animace; MM ho vyžaduje (Enable Root Motion + Force Root Lock).
*[Rovnoměrně temperované ladění]: Oktáva dělená na 12 stejných kroků; čisté intervaly jen přibližuje (equal temperament).
*[Rubber banding]: Umělá podpora hráče pozadu / brzda napřed; opravuje signal-to-noise na okrajích obtížnosti.
*[Rubber duck debugging]: Vysvětli problém nahlas (třeba kachně) — řešení se často ukáže v půlce vysvětlování.
*[Runway]: Kolik měsíců vydržíš pracovat, než dojdou peníze — ne kolik peněz máš.
*[Sampling]: Použití kusu existující nahrávky jako materiálu nové skladby; pozor na práva.
*[SaveGame objekt]: Blueprint třída nesoucí ukládané proměnné; přes pojmenovaný slot se zapisuje na disk.
*[Scalability groups]: Skupiny kvality renderování; *Epic* je režim pro 30 FPS, pro 60 je referenční *High*.
*[SCAMPER]: Sedm pák na nápad: Substitute, Combine, Adapt, Magnify, Purpose, Eliminate, Rearrange.
*[Scene Component]: Komponenta jen s transformací a dětmi, bez geometrie — pivot, značka místa, warp target.
*[Screen percentage]: V jakém rozlišení se scéna doopravdy renderuje; výchozí „based on display resolution" tiše jde pod 100 %.
*[Scene inheritance]: Scéna odvozená z jiné: převezme celý strom nodů a přepíše jen odchylky.
*[Scene tree]: Strom nodů a vnořených scén, ze kterého se skládá běžící hra; nese i transformace a pořadí kreslení.
*[Scope]: Rozsah projektu — hlavní páka proveditelnosti a nejčastější příčina nedokončení.
*[Scope creep]: Plíživé bobtnání rozsahu během vývoje („co kdybychom přidali rybaření?").
*[Scrum]: Agilní metodika: sprinty s pevným cílem, priority z backlogu na sprint meetinzích.
*[Seamless loop]: Smyčka, jejíž konec plynule navazuje na začátek bez slyšitelného švu; nutnost herní hudby.
*[Self Pruning]: PCG uzel mazající překrývající se body podle bounds či kolizí — garance rozestupů checkboxem.
*[Semiotika]: Nauka o tom, co symboly znamenají a proč — u písma dřív, než přečteš obsah.
*[Separation of concerns]: Systém z malých částí s jedinou zodpovědností — jako motor z vyměnitelných dílů.
*[Sequencer]: Editor časových os v UE: cutscény, kamery, animace postav, render záběrů.
*[Serif]: Patka na konci tahu písmene; nese historickou asociaci a mírně zpomaluje čtení.
*[Set Timer by Event]: Časovač, který po zadané době (jednou či opakovaně) zavolá event; handle ho zastaví nebo změří.
*[Shading bin]: Nanitová obdoba draw callu; vlastní bin chce každá materiálová instance, ~3 µs minimum.
*[Shape language]: Standardizace tvarů pro významy: plus je zdraví, kruh štít, špice poškození.
*[Septakord]: Akord se septimou nad triádou; koření žánru, ne výchozí stav.
*[Short description]: 300znakový popis hry na Steamu; test 300 znaků = zkus ho napsat v den nula nápadu.
*[Sidechain]: Automatické stažení zvuku při úderu jiného; ve Strudelu duck na orbitě.
*[Signal]: Zpráva, kterou node vyšle, aniž ví, kdo ji poslouchá — observer pattern zabudovaný do enginu.
*[Signal-to-noise ratio]: Poměr užitečné informace k šumu; flow kanál je pásmo nejlepšího signálu pro učení.
*[Significance handler]: Pravidlo, které u Niagary rozhodne, které instance přežijí strop počtu (vzdálenost nebo věk).
*[Significance Manager]: Plugin, který objektům počítá význam (vzdálenost aj.); hra podle něj řídí LOD, tick a počet aktivních.
*[Silueta]: Obrys tvaru — nosič identity a čitelnosti; v prostředí ji tvoří kontrast světla a stínu.
*[Simulated annealing]: Optimalizace žíháním: nejdřív ochota k horším krokům, pak chladnutí k vylepšování.
*[Single Layer Water]: Shading model vody (translucence, kaustika); stíny jen z directional lightu — jinak Default Lit.
*[Single responsibility principle]: Jeden modul, jedna zodpovědnost — a tedy jen jeden důvod, proč ho měnit.
*[Single source of truth]: Jedna informace na jednom místě; ostatní se ptají místo aby si drželi vlastní kopii.
*[Singleton]: Garantovaná jediná instance s globálním přístupem — a glorifikovaná globální proměnná.
*[Size Map]: Pravý klik na asset → kolik paměti zabere i se vším, co s sebou táhne.
*[Skill ceiling]: Strop dosažitelné dovednosti — prostor pro mastery.
*[Skill floor]: Minimum dovednosti, abys vůbec hrál; komplexita ovládání je floor sama o sobě.
*[Skills audit]: Inventura dovedností před volbou projektu: co umím, co ne, co napůl.
*[Smart Object]: Objekt světa inzerující interakce: sloty k zabrání + State Tree chování spuštěné na postavě.
*[Socket]: Pojmenovaný bod na kosti nebo meshi, ke kterému se připínají jiné objekty.
*[Soft boundary]: Překročitelná hranice mapy, u které svět dává najevo „špatný nápad": příběh, čas, nepřítel, cena, mlha.
*[Softlock]: Stav, kdy hra běží, ale nejde dohrát — hráč uvízl bez cesty dál (ztracený předmět, obejitá podmínka).
*[Soft reference]: Odkaz jen s cestou k assetu; nic nenačte, dokud si o to hra neřekne (Async Load Asset).
*[Soft skills]: Dovednosti bez viditelného výstupu (úsudek, empatie, komunikace); učí se objevováním, ne návodem.
*[Sound Cue]: Zvukový asset s grafem nad wave soubory — random variace, mix, attenuace; nástupce je MetaSounds.
*[Sound font]: Kolekce nasamplovaných zvuků nástroje (.sf2); rychlá retro paleta (Undertale, SNES).
*[Sparse set]: Minimální MM sada: ~13 klipů bez strafu, ~26 se strafem — mýtus 500 animací neplatí.
*[Sphere tracing]: Trasování po skocích o hodnotu distance fieldu; počítá s tloušťkou, neproklouzne škvírou.
*[Spline]: Komponenta s křivkou z tažitelných bodů — patrol trasy, hrany překážek, tvary krytí.
*[Spline mesh]: Mesh natažený podél segmentu splinu — liány, lana, oblouky drah; pozor na forward axis.
*[Sprite sheet]: Jeden obrázek s mřížkou snímků animace nebo sadou dlaždic.
*[Square hole]: Chyba balancu: univerzální nástroj, který řeší každou situaci, a tím zabíjí rozhodování.
*[Squash & stretch]: Animační princip: zploštit při dopadu, natáhnout při výskoku — levný juice.
*[Squeeze and release]: Rytmus střídání tlaku a úlevy; nejlevnější forma úlevy je checkpoint.
*[State alias]: Zástupný uzel state machine reprezentující víc stavů — jedno přechodové pravidlo místo N.
*[State machine]: Stavový automat AnimBP: stavy = animace, přechody = pravidla; MM ho nahrazuje, hybridy kombinují.
*[State Tree]: Hierarchický stavový automat UE (sestra behavior tree); stavy s tasky, přechody, injektované stromy.
*[Static switch]: Přepínač v materiálu rozhodnutý při kompilaci — nepoužitá větev ze shaderu zmizí.
*[Steam Next Fest]: Steamový festival demoverzí (3× ročně); multiplikátor wishlistů, účast jen jednou za hru.
*[Stem separace]: Rozdělení hotové nahrávky zpět na zpěv, bicí, bas a zbytek.
*[Streaming pool]: Vyhrazená VRAM pro streamované textury; zmenšuj ji, dokud engine nezačne hlásit přetečení.
*[Stitching]: Experimentální MM technika: místo lineárního blendu najde animaci z pózy A do pózy B za daný čas.
*[Strategy pattern]: Rodina zaměnitelných algoritmů za společným rozhraním místo if/else stromu.
*[String pulling]: Zkrácení cesty na nejkratší přes nav polygony (funnel); body se přitáhnou k rohům.
*[Strudel]: Prohlížečové prostředí pro live coding; JavaScriptová verze TidalCycles.
*[Struct]: Pojmenovaná skupina proměnných, se kterou se zachází jako s jednou hodnotou.
*[Stupnice]: Sada tónů daná vzorcem půltónů a celých tónů; durová a mollová pokryjí většinu.
*[Subsystem]: Automaticky vytvářený singleton s daným životním cyklem (engine/game instance/world); definice v C++.
*[Subtraktivní syntéza]: Oscilátor generuje bohatý zvuk, filtr ubírá; řetězec oscilátor → filtr → obálka/LFO.
*[Surface cache]: Zjednodušené povrchy, ze kterých Lumen čte; žlutá = vyřazeno, fialová = nevykresleno.
*[Survivorship bias]: Vidíš jen ty, kdo přežili; neúspěšné pokusy z dohledu zmizely.
*[SVD]: Každá matice = rotace → škálování se změnou dimenze → rotace (A = UΣVᵀ).
*[Swing]: Prodloužení liché šestnáctiny na úkor sudé; klíč k houseovému groovu.
*[Sync marker]: Značka v animaci (došlap L/R) synchronizující klipy různých délek při blendování; jména musí sedět.
*[TAA]: Temporal anti-aliasing — desetinásobně levnější než TSR, cenou je rozmazání v pohybu.
*[Synkopa]: Akcent na nepřízvučnou dobu; hlavní koření rytmické proměny melodie.
*[Tagy]: Štítky hry v obchodě; vstup pro doporučovací algoritmus, ne popis pro zákazníka.
*[Telemetrie]: Sběr dat o tom, co hráči ve hře skutečně dělají — lokální čítače i vzdálená analytika.
*[Take Recorder]: Nahrává hraní jako sekvenci transformů — nespustí gameplay kód, takže benchmark z něj lže.
*[Tell]: Signál prozrazující dopředu, co přijde; bez něj není útok výzva, ale loterie.
*[Tessellation]: Dělení geometrie na jemnější trojúhelníky pro vyšší detail povrchu.
*[Texture atlas]: Jedna textura s povrchy pro mnoho objektů vedle sebe — méně materiálů, méně draw callů.
*[Tile set]: Sada dlaždic pro 2D svět a pravidla, jak na sebe navazují; počet dlaždic je vždycky kompromis.
*[Time slicing]: Drahý výpočet se nepočítá každý snímek, ale každý n-tý; mění frekvenci, ne algoritmus.
*[Timeline]: Blueprint uzel s křivkami v čase (Play/Reverse/Finished) — animace hodnot bez animačního assetu.
*[Tone mapper]: Převod HDR na obraz monitoru; výchozí ACES stojí za „unreal engine lookem", alternativa je AGX.
*[Toon shading]: Stínování v pásech; od 5.8 Substrate Toon BSDF + Toon Profile, funguje s Lumenem i barevnými světly.
*[Trace channel]: Přepínač, co se zapíše do trace; přeteče-li šířka pásma, aplikace se zastaví, nedegraduje.
*[Trajektorie]: Historie + predikce pohybu postavy, proti které MM matchuje animace (modrá budoucnost, červená minulost).
*[Traversal]: Překonávání překážek (vault, mantle, hurdle): detekce hran + chooser + montáž s motion warpingem.
*[Trigger volume]: Neviditelná zóna v levelu, která při vstupu spustí událost — základ skriptovaných momentů.
*[Trim Relative Error]: Nanite: zahodí detail pod danou relativní chybou; na listí vhodnější než procento.
*[Trim sheet]: Sdílená textura z pásů detailů pro mnoho assetů — řádová úspora draw calls a VRAM.
*[Triáda]: Nejzákladnější akord ze tří tónů (základ, tercie, kvinta); rozestupy určí dur/moll/zmenšená.
*[TSR]: Temporal Super Resolution — upscaler UE5; rozmazaná voda a ghosting jemných detailů = typicky jeho vina.
*[Tutorial hell]: Smyčka „umím zopakovat tutoriál, sám nepostavím nic"; útěk: po každém videu malý vlastní projekt.
*[Two-loop rule]: Každé dva loopy nejvýš dvě změny (přidat/ubrat nástroj či výraz); lešení pro aranžmá.
*[Type 2 fun]: Bolí teď, těší ve vzpomínce (hora, soulsovka). Pro jiného hráče Type 3 — volba publika.
*[Typografie]: Práce s písmem: volba řezů, jejich role v hierarchii textu a pravidla použití.
*[Tritón]: Interval uprostřed oktávy; symetrie na kruhu tónů znamená nestabilitu.
*[Tónina]: Domovská stupnice skladby; v piano rollu scale highlighting schová „špatné" tóny.
*[Tři C]: Character, camera, controls — co žánr definuje; v AAA samostatná designérská role.
*[UMG]: Unreal Motion Graphics — systém UI v UE: widget blueprinty z panelů, tlačítek a textů.
*[Unison]: Navrstvení více kopií vlny na jednu notu; rozšíří zvuk do sterea (supersaw).
*[Unreal Insights]: Profiler CPU strany snímku (herní a render vlákno); spouštěj ho dřív než hru.
*[User story]: Popis funkce jako kroky uživatele: co vidí a dělá, ne jak je to naprogramované.
*[USP]: Unique selling point — co má jen tvoje hra; nemusí existovat od začátku (GTA).
*[Utility AI]: Každý úkol si spočítá skóre, spustí se nejvyšší; nenahrazuje stromy, řídí je.
*[UV mapping]: Předpis, která část 2D textury se natáhne na kterou plochu modelu.
*[UX]: User experience — informační architektura: kde informace bydlí a kolika kroky se k nim dostaneš.
*[Visual Logger]: Nahrávač hodnot a tvarů v čase; po hře se prochází po časové ose a kategoriích.
*[VSync]: Synchronizace výměny bufferů s cyklem monitoru: bez trhání, ale za cenu latence.
*[Value chain]: Hodnotový řetězec — smysl sběru dává až jeho zamýšlené použití (Dan Cook).
*[Value curve]: Profil hry přes dimenze appealu: klon trefující stejné kolonky nemá důvod existovat.
*[Vektor]: Bod v prostoru (pozice), nebo směr s velikostí (velocity) — dvě čtení, nemíchat.
*[Version control]: Verzování projektu (Git): návratové body a historie jako deník pokroku; commituj malé celky.
*[Vertical slice]: Reprezentativní výsek hry ve finální kvalitě; brána mezi prototypem a plnou produkcí.
*[Virtual texture stack]: Počet unikátních UV kombinací v materiálu; cena zpětné vazby se počítá na stack.
*[Virtual bone]: Kost existující jen v enginu (Add Virtual Bone) — IK cíle a sockety bez re-exportu z DCC.
*[Virtual Shadow Maps]: Stínový systém UE5 pro Nanite a Lumen — vysoké rozlišení bez ladění kaskád.
*[Virtual texture]: Textura streamovaná po stránkách jen kam se kamera dívá; pevný pool, daň = page table.
*[Vizuální hierarchie]: Uspořádání scény tak, aby nejdůležitější informace byla nejsnáze vidět.
*[Voice leading]: Vedení tónů tak, aby přechody mezi akordy byly co nejjemnější (vedení hlasů).
*[Voicing]: Jak rozmístíš tóny akordu (pořadí, oktávy); otevřený voicing zní prostorněji.
*[Volumetric fog]: Objemová mlha na height fogu — paprsky a atmosféra; kvalita přes GridPixelSize/GridSizeZ.
*[Widget Blueprint]: Asset UMG, který spojuje vzhled widgetu (designer) s jeho logikou (graph).
*[Widget Component]: Komponenta, která zobrazí UMG widget ve světě — na ploše (World), nebo nad aktérem ke kameře (Screen).
*[Widget Interaction Component]: Virtuální myš pro widgety ve světě: paprsek, který Widget Componentě posílá najetí a klik.
*[World Composition]: Starší systém UE 4 pro velké světy: sublevely v mřížce streamované podle vzdálenosti; předchůdce WP.
*[WPO]: World Position Offset — posun vrcholů v materiálu; nejčastější tichá příčina drahých stínů.
*[Water Body]: Actor Water pluginu (ocean/lake/river/island) tvarovaný splinami; řeka má rychlost proudu per point.
*[Wave Function Collapse]: PCG: políčko jako superpozice dlaždic, kolaps dle pravidel sousedství — náhodné, a přitom soudržné.
*[WIP limit]: Kanban strop rozdělanosti: 1–2 karty v Doing na osobu; víc = těkání.
*[Wishlist]: Přání na Steamu; před vydáním hlavní měřítko zájmu a palivo algoritmu viditelnosti.
*[World Partition]: Streamovací systém UE5 — svět v buňkách nahrávaných podle potřeby.
*[Yoink & twist]: Vzorec nápadu: vezmi žánr s prokázaným publikem (yoink) a přidej vlastní vylepšení či obrat (twist).
*[Yomi]: Čtení soupeřovy mysli jako dovednost (fighting hry); hraješ proti mysli, ne proti hodu.
*[Z index]: Číslo určující pořadí vykreslení 2D objektů nezávisle na jejich pozici ve stromu.
*[Zero indexing]: První prvek má index 0; n-tý sedí na n − 1. Záměna = klasická off-by-one chyba.
*[Zákon opaků]: Najdi slabinu žánru, odstraň ji a postav na tom svůj marketingový slib.
*[Zákop (trench)]: Hlavní hlas plus akordy — nejmenší nosný kus skladby.
*[Zázněj]: Pomalé kolísání hlasitosti dvou blízkých frekvencí (beating); příčina pásma nepohody.
