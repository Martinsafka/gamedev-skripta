# Instanced Actors: instance, které ožijí

**Instanced Actors** (experimentální od 5.5, s PCG interopem od 5.6) řeší staré dilema procedurálních světů: tisíc objektů jako levné instanced static meshe, **nebo** interaktivní blueprinty — vyber si. Tenhle systém dává obojí: svět stojí z instancí a teprve objekt, ke kterému se hráč přiblíží, se **vymění za plnohodnotný Blueprint actor**; po odchodu se zase složí zpět do instance. Kapitola vychází z jednoho podrobného průvodce a pokrývá setup přes Data Registry, vzor pro perzistenci stavu i chování fyziky.

---

## Swap podle vzdálenosti: setup přes Data Registry

**Zdroj:** [The NEW Instanced Actors Interop in 5.6 is Game Changing!](https://www.youtube.com/watch?v=B9s_1qkTRfI) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~22 min, tutoriál

**Shrnutí:** PCG graf spawne stovky stolů jako instance; jakmile k některému dojdeš, stane se z něj blueprint — s kolizemi, overlap eventy, čímkoli — a za zády se zase promění v instanci [(0:03)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=3s). Výkon zůstává instancovaný, protože hráč nikdy nestojí u všeho najednou [(0:51)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=51s). Nejtěžší část celého systému je jednorázová byrokracie: **Data Registry**.

### Rozpad myšlenky

**Pluginy a graf:** zapnout tři pluginy — PCG framework, **Instanced Actors** a experimentální **Instanced Actor Interop** — a restartovat [(0:51)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=51s). Graf je triviální: Create Points Grid (2000×2000, coordinate space *local component*) → Select Points (0,02–0,05) → **Spawn Instanced Actors** uzel, kterému patří blueprint třída [(2:23)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=143s) [(3:09)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=189s). V outlineru se objeví **Instanced Actor Manager**, pod kterým všechny instance žijí [(4:41)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=281s).

**Registry (tady se chybuje):** uzel hned vyhodí warning, že třída „nemá záznam v actor class settings registry" [(3:55)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=235s). Postup opravy:

1. Right-click → Miscellaneous → **Data Registry** [(4:41)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=281s). Registry type a item struct = **InstancedActorsClassSettings** — přesný název si okopíruj z Project Settings → Engine → Instanced Actors (*named settings registry type*), překlep = nefunkční setup [(5:29)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=329s).
2. Do registry přidat data source typu **Data Table**; tabulku nech vytvořit rovnou z dialogu, row structure opět InstancedActorsClassSettings [(6:16)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=376s).
3. Řádek tabulky: **row name = přesné jméno třídy s příponou `_C`** (`BP_TableInteractable_C`) [(6:16)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=376s) [(7:02)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=422s). V řádku se per třída řídí stíny instancí, fyzika, vliv na navigaci, dokonce záměna celého actora [(7:02)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=422s).
4. Project Settings → Game → Data Registry → **Directories to Scan** + složka, kde registry leží [(7:02)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=422s).

Validace prostá: **Force Regen** na PCG komponentě — žádný warning znamená hotovo; autorovými slovy „genuinely, that is the hardest part" [(7:48)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=468s).

**Interakce po swapu:** do blueprintu sphere collision + On Component Begin Overlap s testem **Is Player Controlled** na pawnovi [(8:34)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=514s); kolizi nastav custom — ignore all, overlap jen Pawn — a vypni Hidden in Game, ať sféra neruší [(9:20)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=560s). Vzdálenost, ve které se instance mění na actora, řídí **Max Actor Distance** v řádku data table — s hodnotou 500 se objekt „probouzí" až těsně u hráče [(10:06)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=606s).

> **Pozn.:** Systém je **experimental** — UI i názvy se mohou mezi verzemi hnout a dokumentace je zatím řídká (i proto je celý setup tak neintuitivní). Registry byrokracie je ale per projekt: druhá a další třída už jen přidává řádek do tabulky.

**Souvislosti:** [PCG: základy a nástroje](pcg-zaklady.md) · [Rejstřík: instanced actors](../rejstrik.md#instanced-actors) · [Rejstřík: data registry](../rejstrik.md#data-registry) · [Rejstřík: instance](../rejstrik.md#instance)

---

## Paměť, fyzika a dosahy: život v hive mind

**Zdroj:** [The NEW Instanced Actors Interop in 5.6 is Game Changing!](https://www.youtube.com/watch?v=B9s_1qkTRfI) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~22 min, tutoriál

**Shrnutí:** Klíčové pravidlo systému: instanced actor se při každém probuzení **staví od nuly** — nic si nepamatuje [(11:39)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=699s). Z toho plyne všechno ostatní: stav (sebraný pickup) musí držet externí manager, posunutá fyzika se vrací na místo, a dokud je objekt instancí, žije z něj **jen static mesh** [(15:32)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=932s).

### Rozpad myšlenky

**Jen mesh — a proč je to featura:** v instancované podobě neexistuje hitbox, světlo, decal ani nic dalšího z blueprintu; komponenty ožijí až swapem [(15:32)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=932s). Otočeno v užitek: dej do blueprintu point light a máš **automatický senzor vzdálenosti hráče** — světla se rozsvěcují před ním a zhasínají za ním, strašidelná chodba bez jediného triggeru [(16:20)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=980s) [(17:06)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=1026s). Cokoli „podle vzdálenosti hráče" tenhle systém dává zadarmo. (Komponenta Instanced Actors na blueprintu se ukázala jako zbytečná — bez nastavení a fungovalo to i bez ní [(17:06)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=1026s).)

**Pickup s pamětí — manager pattern:** demo staví předmět na stole: begin play nastaví mesh, overlap ho zničí (destroy component přes validated get) [(10:53)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=653s) — jenže po odchodu a návratu je předmět zpátky, protože actor vznikl znovu [(11:39)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=699s). Řešení je malý **manager actor**: pole `locations` (vector array) a dvě funkce — *Check Location* (Find item, nalezeno = index ≠ −1) a *Add To Locations* (**Add Unique**) [(12:25)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=745s) [(13:13)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=793s). Interaktivní actor si na begin play najde manager (Get Actor of Class → promote to variable), zkontroluje **vlastní get actor location** proti seznamu a pickup spawne jen pokud tam není; při sebrání pozici do seznamu přidá [(13:59)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=839s) [(14:45)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=885s). Pozice bodu je tu přirozený stabilní klíč — PCG je generuje deterministicky.

**Fyzika a „hive mind":** kostka se simulate physics se dá odstrčit, ale po unloadu se **vrátí na původní místo** — manager si pamatuje jen spawn transform [(17:52)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=1072s). Přepínač **Eject on Actor Moved** + distance threshold (default 1, v demu 1000) chování mění: objekt posunutý za práh se **trvale osamostatní** — opustí správu manageru a zůstane obyčejným actorem ve světě [(18:38)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=1118s) [(19:26)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=1166s). Trade-off: zpět do „úlu" se už nevrátí (autorova starší čistě PCG metoda fyzikálních objektů reattach uměla — pro spoustu fyzikálních objektů může být pořád vhodnější) [(19:26)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=1166s).

**Dosahy:** vedle Max Actor Distance (swap na blueprint) existuje **Max Instance Distances** — culling samotných instancí; je to pole čtyř hodnot, z nichž v testech reagovala jen poslední (500 → objekty se objevují až blízko) [(20:14)](https://www.youtube.com/watch?v=B9s_1qkTRfI&t=1214s). Kombinací obou vzdáleností se dá řídit pop-in i cena světa.

> **Pozn.:** Stejná filozofie jako [Mass Entity crowd u MetaHumanů](metahuman.md#crowd-plugin-tisic-metahumanu-pres-mass): plná simulace jen tam, kde se hráč dívá, zbytek světa v levné reprezentaci. Instanced Actors ji přinášejí obecným objektům — a spolu s PCG z toho je vzor pro celé herní mechaniky (pickupy, dveře, lootovací bedny) rozseté po velkém světě.

**Souvislosti:** [Případovka: Hex-A-Gone z PCG](pcg-hexagone.md) · [MetaHuman: Crowd plugin](metahuman.md#crowd-plugin-tisic-metahumanu-pres-mass) · [Výřezy a debug PCG](pcg-zaklady.md#vyrezy-podle-kolizi-a-debug-grafu) · [Rejstřík: instanced actors](../rejstrik.md#instanced-actors) · [Rejstřík: Mass Entity](../rejstrik.md#mass-entity)
