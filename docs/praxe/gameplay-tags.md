# Gameplay Tags: stav bez booleanové špagety

Gameplay tagy nahrazují změť booleanů a enumů, kterou většina her sleduje svůj stav [(0:02)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2s). Ali Elzoheiry ale nejde jen po „co to je" — řeší, kde mají tagy bydlet, jak se na ně ptát bez skrytých bugů a jak je pojmenovat, aby škálovaly. Tahle kapitola je základ, na kterém později stojí i GAS: tagy jsou jeho lepidlo [(49:09)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2949s).

---

## Hierarchie místo booleanů: proč `Status.MovementBlocked.*` vyhrává

**Zdroj:** [Everything You Need to Know About Gameplay Tags | UE5 Tutorial](https://www.youtube.com/watch?v=UNDbcAMMJwk) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · ~50 min, systematický tutoriál

**Shrnutí:** Motivační bug je klasika: stun nastaví `MovementBlocked = true`, root taky — a když root skončí dřív, nastaví false a hráč se hýbe *uprostřed stunu* [(2:27)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=147s). Root se choval, jako by byl jediný, kdo pohyb blokuje. Oprava booleany (`IsStunned || IsRooted || …`) znamená s každou novou schopností přepisovat každou podmínku [(4:02)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=242s). Tagy to řeší **hierarchií**: dotaz na rodiče pokryje všechny současné i budoucí děti.

### Rozpad myšlenky

Mechanika: actor nese **Gameplay Tag Container** [(5:02)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=302s) (tagy se spravují v `Tools → Gameplay Tag Manager` [(5:20)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=320s)). Tag v containeru = true, tag mimo = false — potud jsou to booleany. Rozdíl dělá tečková hierarchie [(5:47)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=347s): místo plochých `IsStunned`/`IsRooted` vytvoříš `Status.MovementBlocked.Stunned` a `.Rooted` (zkratka: šipka u rodiče → Add Sub Tag [(6:56)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=416s)). Stun/root si při startu svůj tag přidají (`Add Gameplay Tag`) a při konci odeberou — a pohybová logika se ptá jedinou otázkou: **má container `Status.MovementBlocked`?** [(9:12)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=552s) Dotaz na rodiče automaticky matchuje všechny potomky. Přidání freeze = přidat sub-tag; žádná podmínka v projektu se nemění.

Jakmile začneš myslet v tazích, vidíš je všude [(11:03)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=663s): typy poškození a rezistence (`Damage.Type.Fire` × `Resistance.Fire`), kategorie inventáře (slot přijímá jen děti `Item.Consumable` [(11:11)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=671s)), stealth (`Status.Hidden` — dokud ho máš, AI tě nevidí [(11:23)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=683s)).

K pojmenování dává video dvě pravidla. **Hloubka** [(39:47)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2387s): ani ploché top-level tagy (ztratíš rodičovské dotazy), ani `Status.Movement.Blocked.Ability.Rooted` — nest jen tak hluboko, aby existovaly **smysluplné rodičovské dotazy** [(40:54)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2454s); test: „bude se někdy někdo ptát na tenhle mezi-uzel?" **Funkční kbelíky** [(41:15)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2475s) pro top-level: `Status` (dočasný stav), `Item` (kategorizace), `Damage`/`Resistance`, `Event` (oznámení typu `Event.EnemyKilled` [(43:19)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2599s)). A neplánuj dopředu všechno — struktura tagů vyroste z use cases.

> **Pozn.:** Tagy jsou definované v `Config/DefaultGameplayTags.ini` — v týmu je to magnet na merge konflikty [(44:57)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2697s); `Project Settings → Gameplay Tags → New Tag Source` [(45:29)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2729s) rozdělí tagy do souborů podle domén (combat, UI…) bez vlivu na dotazování. V C++ jdou tagy deklarovat nativně jako symboly [(46:45)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2805s) — konec překlepů ve stringách.

**Souvislosti:** [Principy architektury](principy-architektury.md) · [Komunikace Blueprintů](komunikace-blueprintu.md) · [Rejstřík: gameplay tag](../rejstrik.md#gameplay-tag)

---

## Kde tagy bydlí a jak se na ně ptát bez skrytých bugů

**Zdroj:** [Everything You Need to Know About Gameplay Tags | UE5 Tutorial](https://www.youtube.com/watch?v=UNDbcAMMJwk) · [Ali Elzoheiry](https://www.youtube.com/channel/UCrrZx9bh7RMYhXvaN8BrbNg) · stejné video, systémová část

**Shrnutí:** Container přilepený na player characteru se rozbije v momentě, kdy se na tagy chce ptát někdo, kdo o tvé třídě neví. Řešení do Blueprintů: **komponenta jako nosič containeru** + **function library na bezpečný přístup**. K tomu dvě pasti, které video považuje za nejčastější chyby: struct z funkce je kopie, a mazání sdílených tagů (ref counting).

### Rozpad myšlenky

**Kde bydlí:** nepřítel volí projektil podle rezistencí cíle — ale cíl je „nějaký actor"; cast na konkrétní třídu neškáluje [(14:04)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=844s). C++ nabízí `IGameplayTagAssetInterface`, Blueprint řešení je **actor komponenta `AC_TagManager`** [(15:38)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=938s), jejíž jedinou zodpovědností je nést container. Kdokoli se pak ptá `Get Component By Class → AC_TagManager` [(17:35)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1055s) — na libovolném actoru. Validitu komponenty ale musíš kontrolovat pokaždé, a tak patří do **Blueprint Function Library** [(20:46)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1246s): `GetActorGameplayTagContainer(Actor)` vrací container, nebo *prázdný container* při chybějící komponentě — dotazy pak bezpečně selžou místo errorů. (Plus párové helpery `AddGameplayTagToActor`/`RemoveGameplayTagFromActor`.)

**Past č. 1 — struct je kopie** [(23:27)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1407s): funkce v Blueprintech vrací structy *hodnotou*. `Add/Remove Gameplay Tag` chtějí referenci (diamantový pin [(23:51)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1431s)) — zavoláš-li Add na návratové hodnotě funkce, modifikuješ kopii a neuděláš nic. Přidávat/odebírat jde jen přes **skutečnou proměnnou** (container z komponenty). Video to opakuje třikrát a právem: je to neviditelný bug. S tím souvisí zodpovědnost [(25:59)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1559s): cizí tagy zpravidla jen *čteš*; „stunni nepřítele" znamená zavolat *jeho* funkci Stun, a tag si přidá on sám.

**Past č. 2 — ref counting** [(29:45)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1785s): dva překrývající se ohně přidají hráči tentýž `Status.Damage.Fire` — container je množina, tag tam je jednou; odchod z *jednoho* ohně tag smaže, i když v druhém pořád stojíš [(29:58)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1798s). Řešení podle Lyry: mapa tag→počet [(31:33)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1893s) (add inkrementuje, remove dekrementuje); řešení podle GAS: tagy nese samostatný gameplay effect objekt, kterých může existovat víc [(32:46)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=1966s). Nejlevnější řešení: nedopustit, aby stejný tag modifikovali dva různí actoři.

**Dotazová abeceda:** `Has Tag` matchuje i potomky; **Exact Match** [(33:36)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2016s) vypne dědičnost (dotaz na `MovementBlocked` s exact match *nenajde* `.Stunned`!). `Has Any` = OR přes container [(35:12)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2112s), `Has All` = AND, `Filter` = průnik dvou containerů [(34:56)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2096s), a **Tag Query** s vnořenými expressions [(37:13)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2233s) pro složené podmínky („má rooted a stunned, ale ne freeze" [(37:40)](https://www.youtube.com/watch?v=UNDbcAMMJwk&t=2260s)).

**Souvislosti:** [Principy architektury: tři principy](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) · [Komunikace: broadcast kanály](komunikace-blueprintu.md#ctvrty-kanal-broadcast-pres-subsystem-s-payloady) · [Programátorské myšlení: hodnota vs. reference](../teorie/programatorske-mysleni.md#hodnota-vs-reference-kopie-nebo-listecek-s-sipkou) *(obecný princip za struct-copy pastí)* · [Rejstřík: gameplay tag](../rejstrik.md#gameplay-tag) · [Rejstřík: Blueprint Function Library](../rejstrik.md#blueprint-function-library)
