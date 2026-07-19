# Ukládání: SaveGame objekty

Save systém v UE je překvapivě málo kódu — SaveGame objekt, slot se jménem a tři uzly. Zajímavá část je architektura okolo: kde má save reference bydlet, aby přežila přechody mezi levely a byla dostupná odkudkoli. Tutoriál Unreal University (autorizovaný UE instruktor) to řeší vzorem Game Instance + function library a dává k dispozici projektové soubory.

---

## SaveGame + Game Instance + function library: save dostupný odkudkoli

**Zdroj:** [How to Easily Save Games with SaveGame Objects in Unreal Engine (Demo and Guide)](https://www.youtube.com/watch?v=-0111fuUPz8) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~14 min, průvodce hotovým systémem

**Shrnutí:** Demo ukládá zdraví, rychlost, klobouk a pozici hráče — save, load i delete na tlačítko [(0:02)](https://www.youtube.com/watch?v=-0111fuUPz8&t=2s). Kostra: **SaveGame blueprint** nese ukládané proměnné, **Game Instance** vlastní jeho referenci (přežívá mezi levely) a **Blueprint Function Library** k ní pouští kterýkoli blueprint jedním pure uzlem.

### Rozpad myšlenky

**SaveGame objekt** [(1:35)](https://www.youtube.com/watch?v=-0111fuUPz8&t=95s): nový Blueprint Class → All Classes → `SaveGame`; uvnitř jen proměnné, které chceš persistovat (health, speed, hat, location, rotation). Ukládá se do pojmenovaného **slotu** — string, který identifikuje soubor na disku.

**Proč Game Instance** [(2:21)](https://www.youtube.com/watch?v=-0111fuUPz8&t=141s): u malé hry lze save řešit v characteru, ale character umírá s levelem. Game Instance žije od spuštění aplikace do jejího konce a přežívá přechody mezi levely [(2:21)](https://www.youtube.com/watch?v=-0111fuUPz8&t=141s) — ideální domov pro save referenci (stejné pravidlo „kde co bydlí" jako v [nářadí z workshopu](principy-architektury.md#naradi-z-workshopu-kde-co-bydli-a-jak-se-to-hybe)). Na `Event Initialize` [(3:08)](https://www.youtube.com/watch?v=-0111fuUPz8&t=188s): `Does Save Game Exist(slot)` → neexistuje-li, `Create Save Game Object`; existuje-li, `Load Game From Slot` + cast → uložit jako proměnnou. Nezapomeň vlastní Game Instance zaregistrovat v `Project Settings → Game Instance Class` [(6:13)](https://www.youtube.com/watch?v=-0111fuUPz8&t=373s), jinak systém tiše nefunguje.

**Přístup odkudkoli** [(4:40)](https://www.youtube.com/watch?v=-0111fuUPz8&t=280s): function library s pure funkcí `GetGameInstance → Cast (pure)` — a každý widget, character i level blueprint se k savu dostane dvěma uzly.

**Toky:** *Save* [(6:59)](https://www.youtube.com/watch?v=-0111fuUPz8&t=419s) = nastav hodnoty na save referenci → `Save Game to Slot`; jde ukládat i selektivně (funkce, co uloží jen rychlost [(9:18)](https://www.youtube.com/watch?v=-0111fuUPz8&t=558s)) — save nemusí být all-or-nothing. *Load* [(10:52)](https://www.youtube.com/watch?v=-0111fuUPz8&t=652s) = přečti hodnoty a *aplikuj*: rychlost do Character Movementu, transform přes Set Actor Location — load není magie, je to ruční obnova stavu z dat. *Delete* = `Delete Game in Slot` [(12:27)](https://www.youtube.com/watch?v=-0111fuUPz8&t=747s). Video vše balí do funkcí v Game Instance („Save Player Stats") — méně míst, kde udělat chybu.

> **Pozn.:** Co tutoriál neřeší a jednou řešit budeš: verze save formátu (přidáš proměnnou → staré savy ji nemají; SaveGame to přežije, ale hodnoty budou default), více slotů (slot name jako parametr) a *co* vlastně ukládat u větších her — u naší adventury spíš „stav světa" (otevřené dveře, sebrané klíče — viz [aktivity tagy](telemetrie.md)) než transform hráče. Základní vzor ale zůstává tenhle.

**Souvislosti:** [Principy architektury: kde co bydlí](principy-architektury.md#naradi-z-workshopu-kde-co-bydli-a-jak-se-to-hybe) · [Save systém, který přežije druhý projekt](#save-system-ktery-prezije-druhy-projekt-struktury-interface-a-async) *(tytéž mezery dořešené)* · [Telemetrie](telemetrie.md) · [Rejstřík: SaveGame objekt](../rejstrik.md#savegame-objekt) · [Rejstřík: Game Instance](../rejstrik.md#game-instance)

---

## Save systém, který přežije druhý projekt: struktury, interface a async

**Zdroj:** [The ultimate guide | How to Save & Load your unreal engine 5 game](https://www.youtube.com/watch?v=H6rqJbwjRIk) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~50 min, tutoriál

**Shrnutí:** Předchozí myšlenka končí seznamem toho, co neřeší. Tenhle padesátiminutový průchod řeší přesně to — a jeho vlastní ambice je jinde než u běžného návodu [(0:02)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=2s): *„možná jsi ukládání dělal už dřív, ale mým cílem je naučit tě strukturovat kód tak, abys systém snadno přenesl do dalších projektů, udržoval ho a rozšiřoval."* Tři nosné myšlenky: **struktury místo rozsypaných proměnných**, **interface na Game Instance**, a **rozdělení funkcí na generické a herně specifické**.

### Rozpad myšlenky

**Co ukládat je otázka, ne odpověď** [(2:23)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=143s): *„tahle data hodně závisí na typu hry, kterou stavíš. V téhle fázi musíš přemýšlet: jaké informace potřebuju uložit, aby šlo stav levelu dokonale zrekonstruovat?"* To je správné pořadí — návrh save formátu je návrh odpovědi na otázku „co je vlastně stav mojí hry".

**Struktury místo seznamu proměnných** [(3:55)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=235s): místo `Health`, `Location`, `Rotation`, `Weapon`… vedle sebe vznikne struktura `S_PlayerSave` s transformem, **class referencí zbraně** (*„ne object reference — potřebujeme vědět, jestli je to meč nebo sekera"*), zdravím a **control rotation** [(5:28)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=328s), protože *„transform mi řekne směr meshe, ale ne kamery"*. SaveGame objekt pak drží jednu proměnnou místo osmi — a přidání dalšího ukládaného údaje je změna na jednom místě.

**Sync vs. async** [(7:51)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=471s): UE má obě varianty; async běží na pozadí a hlásí se `Completed` pinem. Autorovo doporučení je asymetrické a dává smysl [(9:25)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=565s): **načítej synchronně** — *„protože často potřebuješ načíst věci dřív, než hra začne"* — a **ukládej asynchronně**, aby hra běžela dál. U asynchronního načtení pak nutně přibude dispatcher `OnGameLoaded` [(18:00)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=1080s): *„kdo čeká na data, musí dostat zprávu — místo aby se každých pár sekund ptal, jestli je načteno."* Tedy [observer](komunikace-blueprintu.md#observer-pattern-nejcastejsi-chyba-zacatecniku-a-jeji-oprava) na svém typickém místě.

**Interface místo castů** [(12:32)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=752s): `BPI_SaveGame` s `LoadGameData(async)`, `SaveGameData(async)` a `GetGameData → BP_SaveGame`, implementovaný na Game Instance. *„Nechci castovat pokaždé, když chci sáhnout na save data, protože vím, že jsou vždycky v game instanci."* Odkudkoli v projektu pak stačí `GetGameInstance → SaveGameData` bez jediného castu.

**Vrstvení interface je ta přenositelná část** [(23:17)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=1397s): ty tři funkce jsou **společné pro každý projekt**; nad ně se přidávají herně specifické (`SavePlayer(S_PlayerSave, async)`, `SaveCubes(async)`). *„A takhle ten systém rozšiřuješ."* Právě tohle dělá ze save systému knihovnu místo jednorázovky.

**Kdo co ví** [(22:31)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=1351s) autor demonstruje na vlastní zavržené verzi. První nástřel nechal checkpoint sestavit celou strukturu a zavolat uložení — a hned to zamítne: *„to je moc věcí, které checkpoint musí vědět o save datech. Game instance ví o save datech všechno, checkpoint ne. Checkpoint potřebuje vědět jen to, že chce uložit data hráče."* Proto `GetPlayerSave` bydlí v postavě (*„kdo zná informace o hráči? Third person character"*) a checkpoint volá **jednu funkci**.

**Dvě praktické pasti**: funkce a proměnná **nesmí mít stejný název** [(14:54)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=894s); a u asynchronního načtení se **castuje až na `Completed` pinu**, ne na okamžitém výstupu [(17:14)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=1034s). K tomu drobná úleva: `CreateSaveGameObject` s vyplněnou třídou vrací rovnou správný typ, takže cast odpadá [(16:28)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=988s).

> **Pozn.:** Ochrana proti poškozeným datům je v návodu decentní, ale důležitá [(28:05)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=1685s): před použitím se kontroluje, jestli uložený transform není nulový — *„to obvykle znamená, že save soubor existuje, ale data hráče v něm nejsou"*. Je to primitivní verze toho, co u větší hry potřebuješ jako **verzování formátu**: až přidáš do struktury pole, staré savy ho budou mít v defaultu a musíš vědět, co s tím. Soubor mimochodem leží v `<projekt>/Saved/SaveGames/<slot>.sav` [(32:48)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=1968s) — a při testování ho budeš mazat často, protože jinak ti „play from here" vždycky načte uložený stav.

**Souvislosti:** [SaveGame + Game Instance + function library](#savegame-game-instance-function-library-save-dostupny-odkudkoli) *(minimální verze téhož)* · [Ukládání stavu světa](#ukladani-stavu-sveta-spawn-update-zniceni-a-indikator) · [Interface, nebo dispatcher](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) · [Principy architektury: kde co bydlí](principy-architektury.md#naradi-z-workshopu-kde-co-bydli-a-jak-se-to-hybe) · [Rejstřík: SaveGame objekt](../rejstrik.md#savegame-objekt) · [Rejstřík: struct](../rejstrik.md#struct)

---

## Ukládání stavu světa: spawn, update, zničení a indikátor

**Zdroj:** [The ultimate guide | How to Save & Load your unreal engine 5 game](https://www.youtube.com/watch?v=H6rqJbwjRIk) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · druhá polovina tutoriálu

**Shrnutí:** Uložit hráče je snadné. **Uložit svět** — objekty, které hráč vytvořil, posunul nebo zničil — je ten skutečný problém, a je to přesně to, co potřebuje adventura s otevřenými dveřmi a sebranými klíči. Video to řeší polem transformů, „ulož, až se to zastaví" trikem a poctivou výhradou k tomu, kdy tenhle naivní přístup přestane stačit.

### Rozpad myšlenky

**Datová struktura** [(6:16)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=376s): pole transformů, kde každý prvek odpovídá jednomu objektu. Ukládací funkce [(35:01)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=2101s) pak dělá vždycky totéž: `Clear` pole → `GetAllActorsOfClass` → for each → `AddUnique(GetActorTransform)` → `SaveGameData(async)`. Volá se na **třech místech**: po spawnu, po zničení a po pohybu.

**Kde se naivita láme — a autor to řekne sám** [(35:47)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=2147s): *„když máš v levelu desetitisíce aktérů, neaktualizuj zbytečně všechny, když se změní jeden — dej jim unikátní identifikátor a přepiš jen ten. Pro moje použití to dopad nemá, testoval jsem to se dvěma tisíci kostkami a byl zanedbatelný."* Tahle věta je cennější než celý zbytek: **dává ti měřítko, kdy jednoduché řešení stačí, a jmenuje náhradu, až stačit přestane.**

**Načtení s výchozím stavem** [(38:07)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=2287s): level blueprint se podívá na délku uloženého pole → je-li větší než nula, spawnuje z uložených transformů; jinak spustí původní výchozí rozestavění. *„Je dobré si ten default nechat."* Bez něj by prázdný save znamenal prázdný svět — což je přesně ta chyba, která se najde až u hráče.

**Ulož, až se to zastaví** [(41:16)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=2476s) je nejchytřejší trik ve videu. Ukládat pozici strkaného objektu každý frame je nesmysl, ukládat ji při nárazu je předčasné — tak: `OnComponentHit` nastartuje **timer po 0,1 s**, ten kontroluje `VectorLength(Velocity)` (*„velocity je rychlost krát směr, takže délka vektoru je rychlost"*), a klesne-li pod tři, timer se zruší a teprve pak se ukládá. Autor přiznává i mez: zastavíš-li hru, dokud se objekt ještě hýbe, pozice se neuloží.

**Indikátor ukládání** [(44:33)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=2673s): widget vpravo dole, v Game Instance dvojice eventů show/hide s **Convert to Validated Get** (neplatný → vytvoř a přidej do viewportu). Volá se **jen na asynchronní větvi** — u synchronního uložení by problikl na jeden snímek. A poctivé zarámování na konec [(48:46)](https://www.youtube.com/watch?v=H6rqJbwjRIk&t=2926s): *„u her, které ukládají i do cloudu, ta doba zahrnuje request na server, uložení a potvrzení — proto tam ten indikátor vidíš mnohem dýl."* Ta ikona „nevypínej konzoli" tedy není dekorace; je to **měřítko skutečné operace**.

> **Pozn.:** U adventury nebo jakékoli hry se sbíráním předmětů je poučení jasnější než u kostek: **ukládat transformy je řešení pro věci, které se hýbou; pro věci, které mají stav, potřebuješ stav** — dveře nejsou pozice, ale „odemčeno/otevřeno", klíč není transform, ale „v inventáři". Vhodná datová struktura je tedy spíš mapa **identifikátor → stav** (a identifikátorem se nabízí [gameplay tag](gameplay-tags.md) nebo stabilní jméno aktéra) než pole transformů. Autorova rada „dej jim unikátní identifikátor" míří přesně sem — jen o dvě velikosti projektu dřív, než ji vyslovil.

**Souvislosti:** [Save systém, který přežije druhý projekt](#save-system-ktery-prezije-druhy-projekt-struktury-interface-a-async) · [Gameplay Tags](gameplay-tags.md) *(kandidát na identifikátor stavu)* · [Telemetrie: activity tracker](telemetrie.md#activity-tracker-gameplay-tagy-jako-zaznam-cinnosti) · [Level streaming](levely-a-streaming.md) · [Rejstřík: SaveGame objekt](../rejstrik.md#savegame-objekt)
