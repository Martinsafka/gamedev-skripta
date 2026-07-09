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

**Souvislosti:** [Principy architektury: kde co bydlí](principy-architektury.md#naradi-z-workshopu-kde-co-bydli-a-jak-se-to-hybe) · [Telemetrie](telemetrie.md) · [Rejstřík: SaveGame objekt](../rejstrik.md#savegame-objekt) · [Rejstřík: Game Instance](../rejstrik.md#game-instance)
