*[Abstract class]: Třída, kterou nejde umístit do světa ani referencovat — existuje jen jako rodič pro děti.
*[Affordance]: Vlastnost objektu/prostoru signalizující, jak s ním jde interagovat — klika říká „stiskni".
*[AI Controller]: Mozek AI postavy: posedne pawna a rozhoduje; spouští Behavior/State Tree, nese percepci.
*[AI Perception]: Percepční systém UE: smysly (sight, hearing, damage) jedné komponenty; cíl musí mít Stimuli Source.
*[ALS]: Advanced Locomotion System — komunitní locomotion framework; jeho autor dnes v Epicu vede design GASP.
*[Anim montage]: Animační asset pro jednorázové akce, hraný přes sloty; nad MM základ combatu (horní tělo).
*[Anim Notify]: Značka na časové ose animace spouštějící logiku v daném framu; notify state = varianta s trváním.
*[Asset pack]: Balík hotových assetů (modely, zvuky, UI) k okamžitému použití — základ rychlého prototypování.
*[B-roll]: Doplňkové záběry pod mluvené slovo; v devlozích typicky záběry gameplaye.
*[Behavior Tree]: Rozhodovací strom AI: selectory a sequence volí tasky podle Blackboardu; decoratory hlídají podmínky.
*[Blackboard]: Sdílená tabule AI: pojmenované klíče, přes které si percepce, tasky a strom předávají data.
*[Blend Space]: Asset míchající animace podle hodnot na osách (rychlost, směr); klipy synchronizují sync markery.
*[Blend stack]: Anim uzel: změna animační proměnné = nový blend do zásobníku — bez state machine.
*[Blockout]: Hrubá stavba levelu z primitiv — testuje prostor, metriky a flow před finálními assety.
*[Blueprint Function Library]: Sbírka funkcí volatelných z libovolného blueprintu v projektu.
*[Blueprint Interface]: Sada funkcí bez implementace — kontrakt mezi Blueprinty, volání zprávou bez znalosti třídy.
*[Boolean]: Geometrická operace kombinující dvě tělesa: sjednocení (union), rozdíl (subtract), průnik.
*[Bounds]: Osově zarovnaný obal objektu či bodu; v PCG pracovní data — výřezy, pruning, bounds modifier.
*[Buoyancy]: Vztlak Water pluginu: pontoony (klasika) nebo od 5.7 Default Buoyancy Physics Material + Query and Probe.
*[Cable Component]: Vestavěné simulované lano/kabel; konce jdou ukotvit, částice čte Get Cable Particle Locations.
*[Call to action]: Závěrečná výzva traileru/videa: co má divák udělat teď („Wishlist on Steam"). Právě jedna.
*[Capsule]: Náhledový obrázek hry na Steamu — nejdůležitější kus grafiky celé stránky.
*[Cast]: Přetypování reference na konkrétní třídu; vytváří tvrdou závislost volajícího na dané třídě.
*[Channel]: V Mesh Terrainu malovatelná materiálová vrstva — nástupce landscape layers.
*[Chaos Cloth]: Realtime fyzika látek: Cloth Asset graf s weight mapou, configem a colliderem z physics assetu.
*[Chooser]: Datová tabulka „za těchto podmínek vyber tenhle asset“; v MM přepíná databáze.
*[Cipher]: Typ hráčské postavy: prázdná nádoba bez osobnosti a hlasu; oživí ji až hráčova imaginace.
*[Cold open]: Otvírák traileru: prvních 10–15 s nabitých highlighty v rychlých střizích, pak teprve klid.
*[Collision preset]: Předpis, jak objekt reaguje na kolizní kanály: Block / Overlap / Ignore.
*[Contact curve]: Animační křivka 0/1 „chodidlo na zemi" — řídí foot pinning; nahradila foot velocity curves.
*[Context steering]: Pohyb AI: entita ohodnotí všechny směry vahami a vybere nejlepší proveditelný — nezamrzá u zdi.
*[Continuing pose]: „Co by hrálo dál“ — kandidát, kterého musí nová animace v MM porazit cenou.
*[Control Rig]: Grafový rigging a procedurální animace v enginu — běží i za runtime, bez rekompilace.
*[Core loop]: Základní opakovaná smyčka činností, na které hra stojí.
*[Data asset]: Asset nesoucí čistá strukturovaná data (konfiguraci) bez logiky.
*[Data Registry]: Registr konfiguračních dat (data tables) — systémy se ptají jménem místo tvrdých odkazů na tabulky.
*[Data-driven design]: Hodnoty a konfigurace žijí v datech (data assety); logika je jen čte.
*[Decal]: Materiál promítnutý na povrch světa (otisky, cákance) — spawnuje se za běhu bez úpravy podkladu.
*[Design by constraint]: Návrh z omezení: nejdřív zvol limity (žádný příběh, jedna obrazovka), nápad hledej uvnitř nich.
*[Devlog]: Video či zápis o vývoji vlastní hry — marketingový kanál a žánr s vlastním řemeslem.
*[Difficulty curve]: Průběh obtížnosti hry v čase; skládá se z novelty (učení nového) a mastery (zvládání známého).
*[Dynamic Material Instance]: Runtime kopie materiálu s parametry měnitelnými z kódu (Set Parameter Value); žije per objekt.
*[Edit layer]: Vrstva úprav Landscapu (sculpt i paint); nástroje pracují s aktuálně vybranou — kopie z jiné = prázdno.
*[Event dispatcher]: Rádio mezi Blueprinty: vlastník zavolá, všichni bindnutí posluchači dostanou event.
*[Event Tick]: Blueprint event volaný každý snímek; polling, kterému se dobrý návrh vyhýbá.
*[Flow]: Stav plného zaujetí, kdy výzva odpovídá dovednosti (Csíkszentmihályi); pásmo nejefektivnějšího učení.
*[Foot placement]: Procedurální usazení chodidel: IK na svazích, špendlení došlapů, tlumení roota na hrbolech.
*[Game Design Document]: Dokument s návrhem hry; funguje, jen když se do něj tým skutečně vrací — forma je vedlejší.
*[Game feel]: Hmatový dojem z ovládání: odezva, váha, šťavnatost interakcí. „Game feel je cheat code."
*[Game Instance]: Objekt žijící od spuštění aplikace po její konec — přežívá přechody mezi levely.
*[Game jam]: Časově omezená akce (hodiny až dny), během níž vzniká celá malá hra.
*[Gameplay loop]: Smyčka činností, kterou hráč opakuje; popisný nástroj game designu.
*[Gameplay tag]: Hierarchický identifikátor stavu (Status.MovementBlocked.Stunned) — náhrada boolean špagety.
*[Garbage collection]: Automatický úklid paměti; zničené objekty jsou dočasně „pending kill".
*[GASP]: Game Animation Sample — Epicův živý ukázkový projekt gameplay animace: 500+ animací, MM, traversal, Mover.
*[GDD]: Game design document — dokument s návrhem hry; funguje, jen když se do něj skutečně vracíš.
*[God class]: Antipattern: třída, do které se postupně nastěhuje logika všech ostatních.
*[Graybox]: Prototyp/blockout ze šedých primitiv — správný pro testování mechanik, špatný pro testování prodejnosti.
*[Groom]: Vlasy/srst z pramenů (strands); vlastní LODy — při skládání postavy je drží LOD Sync komponenta.
*[Hard coding]: Hodnoty zadrátované přímo v kódu; v produkci antipattern, v prototypu ctnost.
*[Hard reference]: Přímý odkaz, který s sebou tahá vše, co cíl referencuje — do paměti i do buildů.
*[Height mapa]: Černobílá textura kódující výšku terénu jasem pixelu.
*[Hook]: Prvek, který hru prodá na první pohled — mechanika, premisa nebo obraz, co zastaví palec při scrollování.
*[Inheritance]: Dědičnost: děti přebírají proměnné, funkce a komponenty rodiče. Lakmusový test: „is it a?"
*[Instance]: Konkrétní umístěný výskyt assetu v levelu.
*[Instanced Actors]: Systém (5.5+): svět z levných instancí; objekty u hráče se swapnou na plné Blueprint actory a zpět.
*[Invisible wall]: Neviditelná kolize tam, kde vizuálně nic nebrání — nejhorší způsob ohraničení mapy.
*[Landmark]: Výrazný orientační bod levelu; v postupu „landmark napřed" první rozhodnutí návrhu prostoru.
*[Landscape]: Klasický terén UE: height mapa, jen nahoru/dolů; produkční volba, dokud Mesh Terrain nedozraje.
*[Layered Blend Per Bone]: Anim uzel míchající dvě pózy od zadané kosti nahoru — vrstvení horního těla přes locomotion.
*[Layered move]: Dočasný zdroj pohybu v Moveru (dash, skok) — nástupce root motion sources; víc jich běží naráz.
*[Level streaming]: Načítání a uvolňování částí světa za běhu; persistent level je rám, sub-levely obsah.
*[Line Trace]: Raycast — neviditelný paprsek hledající kolize na své dráze.
*[Linear grammar]: Gramatika PCG: string symbolů řídí rytmus modulů podél splinu — sekvence, počty, opakování.
*[Linked anim graph]: Samostatný anim graf připojený jako modul; přes tag na něj sáhnou komponenty zvenčí.
*[Live Link]: Streamování dat do enginu (mocap, kamery); Live Link Hub od 5.8 zpracuje i offline video na capture data.
*[Locomotor]: Control Rig uzel procedurální chůze: došlapy počítá dynamicky — foot sets, fázové offsety, žádné klipy.
*[Loose coupling]: Třídy na sobě závisejí co nejméně — komunikace přes smlouvy a eventy, ne tvrdé reference.
*[Low-fi prototyp]: Schválně laciný prototyp (náčrt na papíře, čmáranice) — nízké úsilí zve k upřímné kritice nápadu.
*[Market research]: Průzkum trhu: žánrové výdělky (medián!), tagy, recenze konkurence — objektivita proti zamilovanosti.
*[Mass Entity]: ECS framework pro tisíce entit (davy, doprava) — City Sample i MetaHuman Crowd; entity nejsou actory.
*[MetaHuman]: Epicův systém fotorealistických postav; Performance asset zpracuje video na animaci těla i obličeje.
*[MetaSounds]: Grafový audio systém UE5 — nástupce Sound Cues; parametry za běhu přes audio komponentu.
*[Modifier stack]: Vrstvené nedestruktivní úpravy; každou lze dodatečně měnit, přesouvat či smazat.
*[Motion matching]: Dotazový výběr animací: každý frame hledá v databázi pózu nejlépe navazující na trajektorii.
*[Motion Warping]: Ohnutí root motion animace, aby trefila cílový transform; okno řídí notify state v montáži.
*[Movement Mode]: Modulární objekt Moveru pro jeden režim pohybu; vyměnitelný a rozšiřitelný i v Blueprintu.
*[Mover]: Nástupce Character Movement Componentu: replikuje vstupy, modulární módy, pravdivá trajektorie pro MM.
*[Nanite]: Virtualizovaná geometrie UE5 — detail meshů se dynamicky přizpůsobuje kameře.
*[Narrative design]: Návrh vyprávění integrovaný s herním designem — ne „spisovatel dopíše cutscény".
*[Nav Mesh]: Navigační síť, ve které AI počítá cesty; do levelu jako Nav Mesh Bounds Volume, náhled klávesou P.
*[Network Prediction]: Rollback framework UE — síťová větev Moveru: klient posílá jen vstupy, rollback celého okolí naráz.
*[Niagara Data Channel]: Gameplay zapisuje data do kanálu, jediný Niagara systém z nich spawnuje částice — ne systém per událost.
*[Niagara Fluids]: Plugin simulačních šablon; Grid 2D SW Particle Collisions = interaktivní hladina s collider tagy.
*[Overlay state]: Enum-řízená vrstva pózy horního těla přes locomotion — drž předmět bez vlastních pohybových animací.
*[Pacing]: Rytmus zážitku: střídání napětí a klidu, akce a ticha, učení a mistrovství v čase.
*[Pawn Sensing]: Jednoduchá smyslová komponenta (kužel zraku + sluch) s gizmem ve viewportu; event On See Pawn.
*[PCG]: Procedural Content Generation — UE framework pro procedurální osazování světa.
*[PCG Mode]: Editorový režim (5.7): kreslení PCG grafů přímo do světa splinou, štětcem nebo volumem.
*[Persistent level]: Hlavní level, pod kterým žijí streamované sub-levely; nejde unloadnout.
*[Physical Animation Component]: Motory kloubů táhnou simulované kosti k animované póze — základ active ragdollu.
*[Physical Material]: Asset s vlastnostmi povrchu vč. Surface Type — systémy přes něj poznají, po čem stojíš.
*[Physics Asset]: Fyzikální kostra meshe: kolizní těla per kost + constrainty s limity — bez něj není ragdoll.
*[Physics Constraint]: Kloub mezi fyzikálními těly: linear/angular limity + motory; v assetu i jako actor ve scéně.
*[Physics Control]: Komponenta držící simulovaná tělesa u cíle laditelnou pružinou — fyzikální, ale ovladatelné.
*[Pitch deck]: Prezentace hry, která ještě neexistuje; simuluje první kontakt zákazníka s nápadem.
*[Placeholder]: Provizorní asset držící místo finálnímu; schválně ošklivý, aby nesváděl k ladění.
*[Player State]: Objekt s daty jednoho hráče (inventář, skóre) nezávisle na pawnovi; v multiplayeru se replikuje.
*[Playtest]: Testování hry skutečnými hráči za účelem zpětné vazby.
*[Pose Search Database]: PSD — kolekce animací jednoho typu pohybu, ve které Motion Matching hledá pózy.
*[Pose Search Schema]: Definice, co MM měří: kanály (trajektorie, kosti) s vahami; ladí se experimentem.
*[Pose Snapshot]: Zmrazení pózy skeletu jako blendovací zdroj v AnimBP — most z ragdoll fyziky zpět do animace.
*[Post-process AnimBP]: AnimBP meshe vyhodnocovaný po hlavní animaci — vrstvení look-atu a korekcí; vázaný na skeleton.
*[Postmortem]: Ohlédnutí za dokončeným projektem: co fungovalo, co ne a proč — nejhutnější studijní žánr gamedevu.
*[Premature optimization]: Optimalizace před důkazem, že je potřeba; deformuje workflow a žere čas.
*[Press kit]: Balíček pro novináře: popis, kontakty, loga, screenshoty, trailer v plné kvalitě na jednom místě.
*[Quad]: Čtyřúhelníková buňka mřížky meshe; jednotka rozlišení terénu.
*[Race condition]: Chyba pořadí inicializace: kód čte data, která jiný kód ještě nenastavil (BeginPlay actorů!).
*[Recall priming]: Nenápadné nápovědy v prostředí, které hráči zpřístupní správnou vzpomínku těsně před puzzlem.
*[Redirector]: Ghost soubor po přesunu assetu; před smazáním složky spusť Update Redirector References.
*[Retriggerable Delay]: Delay restartovaný každým dalším spuštěním — doběhne až po klidu; „ztráta zájmu" AI.
*[Rewind Debugger]: Nahraje běh hry a nechá tě scrollovat časem: co hrálo, proč to MM vybralo, jak rozhodl State Tree.
*[Roguelike]: Žánr postavený na opakovaných bězích, smrti jako součásti smyčky a procedurální generaci.
*[Root motion]: Pohyb uložený v root kosti animace; MM ho vyžaduje (Enable Root Motion + Force Root Lock).
*[Rubber banding]: Umělá podpora hráče pozadu / brzda napřed; opravuje signal-to-noise na okrajích obtížnosti.
*[SaveGame objekt]: Blueprint třída nesoucí ukládané proměnné; přes pojmenovaný slot se zapisuje na disk.
*[Scope]: Rozsah projektu — hlavní páka proveditelnosti a nejčastější příčina nedokončení.
*[Scope creep]: Plíživé bobtnání rozsahu během vývoje („co kdybychom přidali rybaření?").
*[Self Pruning]: PCG uzel mazající překrývající se body podle bounds či kolizí — garance rozestupů checkboxem.
*[Separation of concerns]: Systém z malých částí s jedinou zodpovědností — jako motor z vyměnitelných dílů.
*[Short description]: 300znakový popis hry na Steamu; test 300 znaků = zkus ho napsat v den nula nápadu.
*[Signal-to-noise ratio]: Poměr užitečné informace k šumu; flow kanál je pásmo nejlepšího signálu pro učení.
*[Single Layer Water]: Shading model vody (translucence, kaustika); stíny jen z directional lightu — jinak Default Lit.
*[Smart Object]: Objekt světa inzerující interakce: sloty k zabrání + State Tree chování spuštěné na postavě.
*[Soft boundary]: Překročitelná hranice mapy, u které svět dává najevo „špatný nápad": příběh, čas, nepřítel, cena, mlha.
*[Sound Cue]: Zvukový asset s grafem nad wave soubory — random variace, mix, attenuace; nástupce je MetaSounds.
*[Sparse set]: Minimální MM sada: ~13 klipů bez strafu, ~26 se strafem — mýtus 500 animací neplatí.
*[Spline]: Komponenta s křivkou z tažitelných bodů — patrol trasy, hrany překážek, tvary krytí.
*[Square hole]: Chyba balancu: univerzální nástroj, který řeší každou situaci, a tím zabíjí rozhodování.
*[State alias]: Zástupný uzel state machine reprezentující víc stavů — jedno přechodové pravidlo místo N.
*[State machine]: Stavový automat AnimBP: stavy = animace, přechody = pravidla; MM ho nahrazuje, hybridy kombinují.
*[State Tree]: Hierarchický stavový automat UE (sestra behavior tree); stavy s tasky, přechody, injektované stromy.
*[Steam Next Fest]: Steamový festival demoverzí (3× ročně); multiplikátor wishlistů, účast jen jednou za hru.
*[Stitching]: Experimentální MM technika: místo lineárního blendu najde animaci z pózy A do pózy B za daný čas.
*[Subsystem]: Automaticky vytvářený singleton s daným životním cyklem (engine/game instance/world); definice v C++.
*[Sync marker]: Značka v animaci (došlap L/R) synchronizující klipy různých délek při blendování; jména musí sedět.
*[Telemetrie]: Sběr dat o tom, co hráči ve hře skutečně dělají — lokální čítače i vzdálená analytika.
*[Tessellation]: Dělení geometrie na jemnější trojúhelníky pro vyšší detail povrchu.
*[Timeline]: Blueprint uzel s křivkami v čase (Play/Reverse/Finished) — animace hodnot bez animačního assetu.
*[Trajektorie]: Historie + predikce pohybu postavy, proti které MM matchuje animace (modrá budoucnost, červená minulost).
*[Traversal]: Překonávání překážek (vault, mantle, hurdle): detekce hran + chooser + montáž s motion warpingem.
*[Trigger volume]: Neviditelná zóna v levelu, která při vstupu spustí událost — základ skriptovaných momentů.
*[TSR]: Temporal Super Resolution — upscaler UE5; rozmazaná voda a ghosting jemných detailů = typicky jeho vina.
*[Value chain]: Hodnotový řetězec — smysl sběru dává až jeho zamýšlené použití (Dan Cook).
*[Version control]: Verzování projektu (Git): návratové body a historie jako deník pokroku; commituj malé celky.
*[Vertical slice]: Reprezentativní výsek hry ve finální kvalitě; brána mezi prototypem a plnou produkcí.
*[Virtual bone]: Kost existující jen v enginu (Add Virtual Bone) — IK cíle a sockety bez re-exportu z DCC.
*[Water Body]: Actor Water pluginu (ocean/lake/river/island) tvarovaný splinami; řeka má rychlost proudu per point.
*[Wishlist]: Přání na Steamu; před vydáním hlavní měřítko zájmu a palivo algoritmu viditelnosti.
*[World Partition]: Streamovací systém UE5 — svět v buňkách nahrávaných podle potřeby.
*[Yoink & twist]: Vzorec nápadu: vezmi žánr s prokázaným publikem (yoink) a přidej vlastní vylepšení či obrat (twist).
