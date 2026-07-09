*[Abstract class]: Třída, kterou nejde umístit do světa ani referencovat — existuje jen jako rodič pro děti.
*[Affordance]: Vlastnost objektu/prostoru signalizující, jak s ním jde interagovat — klika říká „stiskni".
*[Asset pack]: Balík hotových assetů (modely, zvuky, UI) k okamžitému použití — základ rychlého prototypování.
*[B-roll]: Doplňkové záběry pod mluvené slovo; v devlozích typicky záběry gameplaye.
*[Blockout]: Hrubá stavba levelu z primitiv — testuje prostor, metriky a flow před finálními assety.
*[Blueprint Function Library]: Sbírka funkcí volatelných z libovolného blueprintu v projektu.
*[Blueprint Interface]: Sada funkcí bez implementace — kontrakt mezi Blueprinty, volání zprávou bez znalosti třídy.
*[Boolean]: Geometrická operace kombinující dvě tělesa: sjednocení (union), rozdíl (subtract), průnik.
*[Call to action]: Závěrečná výzva traileru/videa: co má divák udělat teď („Wishlist on Steam"). Právě jedna.
*[Capsule]: Náhledový obrázek hry na Steamu — nejdůležitější kus grafiky celé stránky.
*[Cast]: Přetypování reference na konkrétní třídu; vytváří tvrdou závislost volajícího na dané třídě.
*[Channel]: V Mesh Terrainu malovatelná materiálová vrstva — nástupce landscape layers.
*[Cipher]: Typ hráčské postavy: prázdná nádoba bez osobnosti a hlasu; oživí ji až hráčova imaginace.
*[Cold open]: Otvírák traileru: prvních 10–15 s nabitých highlighty v rychlých střizích, pak teprve klid.
*[Collision preset]: Předpis, jak objekt reaguje na kolizní kanály: Block / Overlap / Ignore.
*[Context steering]: Pohyb AI: entita ohodnotí všechny směry vahami a vybere nejlepší proveditelný — nezamrzá u zdi.
*[Core loop]: Základní opakovaná smyčka činností, na které hra stojí.
*[Data asset]: Asset nesoucí čistá strukturovaná data (konfiguraci) bez logiky.
*[Data-driven design]: Hodnoty a konfigurace žijí v datech (data assety); logika je jen čte.
*[Design by constraint]: Návrh z omezení: nejdřív zvol limity (žádný příběh, jedna obrazovka), nápad hledej uvnitř nich.
*[Devlog]: Video či zápis o vývoji vlastní hry — marketingový kanál a žánr s vlastním řemeslem.
*[Difficulty curve]: Průběh obtížnosti hry v čase; skládá se z novelty (učení nového) a mastery (zvládání známého).
*[Event Tick]: Blueprint event volaný každý snímek; polling, kterému se dobrý návrh vyhýbá.
*[Event dispatcher]: Rádio mezi Blueprinty: vlastník zavolá, všichni bindnutí posluchači dostanou event.
*[Flow]: Stav plného zaujetí, kdy výzva odpovídá dovednosti (Csíkszentmihályi); pásmo nejefektivnějšího učení.
*[GDD]: Game design document — dokument s návrhem hry; funguje, jen když se do něj skutečně vracíš.
*[Game Design Document]: Dokument s návrhem hry; funguje, jen když se do něj tým skutečně vrací — forma je vedlejší.
*[Game Instance]: Objekt žijící od spuštění aplikace po její konec — přežívá přechody mezi levely.
*[Game feel]: Hmatový dojem z ovládání: odezva, váha, šťavnatost interakcí. „Game feel je cheat code."
*[Game jam]: Časově omezená akce (hodiny až dny), během níž vzniká celá malá hra.
*[Gameplay loop]: Smyčka činností, kterou hráč opakuje; popisný nástroj game designu.
*[Gameplay tag]: Hierarchický identifikátor stavu (Status.MovementBlocked.Stunned) — náhrada boolean špagety.
*[Garbage collection]: Automatický úklid paměti; zničené objekty jsou dočasně „pending kill".
*[God class]: Antipattern: třída, do které se postupně nastěhuje logika všech ostatních.
*[Graybox]: Prototyp/blockout ze šedých primitiv — správný pro testování mechanik, špatný pro testování prodejnosti.
*[Hard coding]: Hodnoty zadrátované přímo v kódu; v produkci antipattern, v prototypu ctnost.
*[Hard reference]: Přímý odkaz, který s sebou tahá vše, co cíl referencuje — do paměti i do buildů.
*[Height mapa]: Černobílá textura kódující výšku terénu jasem pixelu.
*[Hook]: Prvek, který hru prodá na první pohled — mechanika, premisa nebo obraz, co zastaví palec při scrollování.
*[Inheritance]: Dědičnost: děti přebírají proměnné, funkce a komponenty rodiče. Lakmusový test: „is it a?"
*[Instance]: Konkrétní umístěný výskyt assetu v levelu.
*[Invisible wall]: Neviditelná kolize tam, kde vizuálně nic nebrání — nejhorší způsob ohraničení mapy.
*[Landmark]: Výrazný orientační bod levelu; v postupu „landmark napřed" první rozhodnutí návrhu prostoru.
*[Level streaming]: Načítání a uvolňování částí světa za běhu; persistent level je rám, sub-levely obsah.
*[Line Trace]: Raycast — neviditelný paprsek hledající kolize na své dráze.
*[Loose coupling]: Třídy na sobě závisejí co nejméně — komunikace přes smlouvy a eventy, ne tvrdé reference.
*[Low-fi prototyp]: Schválně laciný prototyp (náčrt na papíře, čmáranice) — nízké úsilí zve k upřímné kritice nápadu.
*[Market research]: Průzkum trhu: žánrové výdělky (medián!), tagy, recenze konkurence — objektivita proti zamilovanosti.
*[Modifier stack]: Vrstvené nedestruktivní úpravy; každou lze dodatečně měnit, přesouvat či smazat.
*[Nanite]: Virtualizovaná geometrie UE5 — detail meshů se dynamicky přizpůsobuje kameře.
*[Narrative design]: Návrh vyprávění integrovaný s herním designem — ne „spisovatel dopíše cutscény".
*[PCG]: Procedural Content Generation — UE framework pro procedurální osazování světa.
*[Pacing]: Rytmus zážitku: střídání napětí a klidu, akce a ticha, učení a mistrovství v čase.
*[Persistent level]: Hlavní level, pod kterým žijí streamované sub-levely; nejde unloadnout.
*[Pitch deck]: Prezentace hry, která ještě neexistuje; simuluje první kontakt zákazníka s nápadem.
*[Placeholder]: Provizorní asset držící místo finálnímu; schválně ošklivý, aby nesváděl k ladění.
*[Player State]: Objekt s daty jednoho hráče (inventář, skóre) nezávisle na pawnovi; v multiplayeru se replikuje.
*[Playtest]: Testování hry skutečnými hráči za účelem zpětné vazby.
*[Postmortem]: Ohlédnutí za dokončeným projektem: co fungovalo, co ne a proč — nejhutnější studijní žánr gamedevu.
*[Premature optimization]: Optimalizace před důkazem, že je potřeba; deformuje workflow a žere čas.
*[Press kit]: Balíček pro novináře: popis, kontakty, loga, screenshoty, trailer v plné kvalitě na jednom místě.
*[Quad]: Čtyřúhelníková buňka mřížky meshe; jednotka rozlišení terénu.
*[Race condition]: Chyba pořadí inicializace: kód čte data, která jiný kód ještě nenastavil (BeginPlay actorů!).
*[Recall priming]: Nenápadné nápovědy v prostředí, které hráči zpřístupní správnou vzpomínku těsně před puzzlem.
*[Redirector]: Ghost soubor po přesunu assetu; před smazáním složky spusť Update Redirector References.
*[Roguelike]: Žánr postavený na opakovaných bězích, smrti jako součásti smyčky a procedurální generaci.
*[Rubber banding]: Umělá podpora hráče pozadu / brzda napřed; opravuje signal-to-noise na okrajích obtížnosti.
*[SaveGame objekt]: Blueprint třída nesoucí ukládané proměnné; přes pojmenovaný slot se zapisuje na disk.
*[Scope]: Rozsah projektu — hlavní páka proveditelnosti a nejčastější příčina nedokončení.
*[Scope creep]: Plíživé bobtnání rozsahu během vývoje („co kdybychom přidali rybaření?").
*[Separation of concerns]: Systém z malých částí s jedinou zodpovědností — jako motor z vyměnitelných dílů.
*[Short description]: 300znakový popis hry na Steamu; test 300 znaků = zkus ho napsat v den nula nápadu.
*[Signal-to-noise ratio]: Poměr užitečné informace k šumu; flow kanál je pásmo nejlepšího signálu pro učení.
*[Soft boundary]: Překročitelná hranice mapy, u které svět dává najevo „špatný nápad": příběh, čas, nepřítel, cena, mlha.
*[Square hole]: Chyba balancu: univerzální nástroj, který řeší každou situaci, a tím zabíjí rozhodování.
*[Steam Next Fest]: Steamový festival demoverzí (3× ročně); multiplikátor wishlistů, účast jen jednou za hru.
*[Subsystem]: Automaticky vytvářený singleton s daným životním cyklem (engine/game instance/world); definice v C++.
*[Telemetrie]: Sběr dat o tom, co hráči ve hře skutečně dělají — lokální čítače i vzdálená analytika.
*[Tessellation]: Dělení geometrie na jemnější trojúhelníky pro vyšší detail povrchu.
*[Trigger volume]: Neviditelná zóna v levelu, která při vstupu spustí událost — základ skriptovaných momentů.
*[Value chain]: Hodnotový řetězec — smysl sběru dává až jeho zamýšlené použití (Dan Cook).
*[Version control]: Verzování projektu (Git): návratové body a historie jako deník pokroku; commituj malé celky.
*[Vertical slice]: Reprezentativní výsek hry ve finální kvalitě; brána mezi prototypem a plnou produkcí.
*[Wishlist]: Přání na Steamu; před vydáním hlavní měřítko zájmu a palivo algoritmu viditelnosti.
*[World Partition]: Streamovací systém UE5 — svět v buňkách nahrávaných podle potřeby.
*[Yoink & twist]: Vzorec nápadu: vezmi žánr s prokázaným publikem (yoink) a přidej vlastní vylepšení či obrat (twist).
