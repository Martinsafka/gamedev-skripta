# Kabely, lana a Physics Control

Tři malé fyzikální systémy, které oživují svět: **Cable Component** (visící lano za minutu), dynamický kabel s **meshi rozsypanými po délce** (řetězy, girlandy, hadice) a **Physics Control** komponenta na příkladu voru, který se houpe pod nohama. Všechno bez pluginů třetích stran — jen věci zabudované v enginu.

---

## Cable Component: lano za minutu a jeho limity

**Zdroj:** [How to Simulate Ropes And Cables In Unreal Engine 5](https://www.youtube.com/watch?v=uVYaJNUjL2Y) · [Unreal ART With Alireza](https://www.youtube.com/channel/UCnzgRZYpm2C-AqUPdEFOi4Q) · ~5 min, tutoriál

**Shrnutí:** Cable actor stačí přetáhnout do scény — fyziku má z krabice a end location se dá chytit a přemístit [(0:49)](https://www.youtube.com/watch?v=uVYaJNUjL2Y&t=49s). Zbytek je ladění: délka + počet segmentů (hladkost), tuhost (default se chová jako guma na bungee), šířka a **počet stran** (default 4 vypadá hranatě) a tile material pro opakování textury po délce [(1:42)](https://www.youtube.com/watch?v=uVYaJNUjL2Y&t=102s).

### Rozpad myšlenky

**Ukotvení:** oba konce jde připnout na objekty ve scéně (actor picker na end location) — pozor, váže se k **pivotu** objektu, takže typicky doladit Z offset na vršek sloupu [(2:20)](https://www.youtube.com/watch?v=uVYaJNUjL2Y&t=140s). `Enable Collision` checkbox rozhoduje, jestli lano interaguje se světem, nebo jím prochází [(3:15)](https://www.youtube.com/watch?v=uVYaJNUjL2Y&t=195s).

**Mini projekt — houpající se koule:** koule zavěšená na kabelu + **Physics Constraint actor** mezi držákem (kostka) a koulí [(4:10)](https://www.youtube.com/watch?v=uVYaJNUjL2Y&t=250s) — postava do ní vrazí a koule se fyzikálně rozhoupe [(4:43)](https://www.youtube.com/watch?v=uVYaJNUjL2Y&t=283s). Důležitý detail: **kabel tu nic nedrží** — nosnou práci dělá constraint, kabel je jen vizuál. Přesně tak se to dělá i ve velkých hrách: fyzika a její vykreslení jsou dvě různé věci.

> **Pozn.:** Autor limity přiznává na rovinu: cable component je skvělý na dekorace, ale nedává plnou kontrolu (žádné přesné uchopení, omezené kolize) [(4:43)](https://www.youtube.com/watch?v=uVYaJNUjL2Y&t=283s). Pro gameplay lana (šplhání, přetahování) je potřeba constraint řetěz nebo plugin — pro visící dráty, cedule a lucerny bohatě stačí tohle.

**Souvislosti:** [Rejstřík: cable component](../rejstrik.md#cable-component) · [Rejstřík: physics constraint](../rejstrik.md#physics-constraint)

---

## Dynamický kabel s meshi po délce

**Zdroj:** [Create Dynamic Cable Systems in UE5.7, Attach Any Mesh Procedurally](https://www.youtube.com/watch?v=hGz_TWoez0M) · [PolyBoost](https://www.youtube.com/channel/UCHzLwhfU8b07C8WOAcrXiYA) · ~11 min, tutoriál

**Shrnutí:** Girlanda žárovek, řetěz, ostnatý drát — cokoli, co má viset *na* kabelu a houpat se s ním. Recept: blueprint s **cable komponentou + Instanced Static Mesh**, v construction scriptu se nastaví konce a průvěs, a na ticku se instance **každý frame přestaví** na aktuální pozice částic kabelu přes `Get Cable Particle Locations`.

### Rozpad myšlenky

**Parametry pro level designéra:** start/end location, `cable slack` (průvěs) a update rate — všechno instance editable [(1:02)](https://www.youtube.com/watch?v=hGz_TWoez0M&t=62s). Construction script: actor na start, `Set End Location` = end − start (relativní!), a délka kabelu = `Distance(start, end)` × multiplikátor průvěsu [(2:21)](https://www.youtube.com/watch?v=hGz_TWoez0M&t=141s), [(3:41)](https://www.youtube.com/watch?v=hGz_TWoez0M&t=221s).

**Meshe po částicích** [(4:24)](https://www.youtube.com/watch?v=hGz_TWoez0M&t=264s): tick → `Clear Instances` → **`Get Cable Particle Locations`** (pole bodů simulace) → for-loop od 1 do length−1 → `Make Transform` z bodu → `Add Instance`. Instance jsou levné — jeden draw call pro všechny žárovky. Když meshe „ujíždějí", zapni na ISM **world space** instance [(6:40)](https://www.youtube.com/watch?v=hGz_TWoez0M&t=400s).

**Manuální režim:** blueprint s natvrdo zadanými world souřadnicemi nejde chytit a posunout — oprava jsou dvě **arrow komponenty** jako úchyty konců a construction script čtoucí jejich *relativní* pozice [(7:39)](https://www.youtube.com/watch?v=hGz_TWoez0M&t=459s) — pak kabel táhneš po levelu jako každý jiný actor [(10:10)](https://www.youtube.com/watch?v=hGz_TWoez0M&t=610s).

> **Pozn.:** Clear + rebuild všech instancí každý tick je hrubá síla — pro pár kabelů v záběru v pohodě, pro desítky zvaž update rate (proměnná na to v tutoriálu je, jen se nepoužije) nebo `Update Instance Transform` místo přestavby. A rotace instancí se tu neřeší — žárovky visí svisle; kdo chce články řetězu *orientované po kabelu*, spočítá rotaci z vektoru mezi sousedními částicemi (stejný princip jako tangenty u [spline mesh trajektorie](interakce-predmety.md#hazeni-predmetu-s-predikci-trajektorie)).

**Souvislosti:** [Interakce s předměty: spline mesh vizualizace](interakce-predmety.md#hazeni-predmetu-s-predikci-trajektorie) · [Rejstřík: cable component](../rejstrik.md#cable-component) · [Rejstřík: instance](../rejstrik.md#instance)

---

## Physics Control: vor, který se houpe pod nohama

**Zdroj:** [UE5.2 - Physics Control Component - Character interactive raft](https://www.youtube.com/watch?v=A_NMmn-Do38) · [Yepkoo](https://www.youtube.com/channel/UCUHGwLeq0u6-1hnZ6N3lAng) · ~8 min, tutoriál (ruční titulky)

**Shrnutí:** **Physics Control** komponenta (plugin, 5.1+) drží simulované těleso u zadaného cíle pružinou — jako neviditelná ruka, jejíž sílu a tlumení ladíš. Ukázka: vor na vodě, který se pod postavou rozhoupe, nechá se odtlačit a **sám se vrací** na místo. Stejný nástroj, kterým GASP éra řeší „fyzikální, ale ovladatelné" objekty.

### Rozpad myšlenky

**Setup** [(1:59)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=119s): mesh voru musí simulovat fyziku; Physics Control komponenta → **`Create Control`** (child mesh = vor) s make-nody nastavení + **`Create Body Modifier`** — bez něj se control neaplikuje [(2:26)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=146s). Gravitace na 0 (drží ho control), cílová pozice/rotace z transformu actora [(2:47)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=167s). Ladění charakteru: nižší **Linear Strength** = vor se snáz hne, nižší **Linear Damping Ratio** = houpe se déle [(3:04)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=184s).

**Posouvání voru:** box collision kousek pod horní hranou → overlap postavy → `IsMove` bool [(4:40)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=280s); na ticku pak **`Set Control Target Position and Orientation`** posouvá cíl pružiny za mesh [(5:39)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=339s). Dvě jemnosti: cílová pozice se čte z **transformu static meshe, ne actora** — actor stojí, pluje jen simulovaný mesh [(6:35)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=395s); a Z výška + Y rotace se drží z počátečních hodnot, ať se vor nenaklání ani nepotápí [(6:48)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=408s).

**Gotcha se jménem:** `Set Control Target…` chce **Name** controlu — a `Create Control` ho generuje automaticky („test_0"); vytiskni si ho print stringem, jinak uzel tiše nedělá nic [(6:25)](https://www.youtube.com/watch?v=A_NMmn-Do38&t=385s).

> **Pozn.:** Physics Control je mladší sourozenec Physical Animation komponenty z [ragdoll kapitoly](ragdoll.md#active-ragdoll-motory-rizene-rychlosti) — obecnější (funguje na libovolných tělesech, ne jen skeletech) a Epic ho používá i pro fyzikální interakce v ukázkách. Vzor „pružina k cíli místo kinematického pohybu" je přesně to, co dělá svět hmatatelným: vor pod nohama *odpovídá*, místo aby byl výtahem. Pro naši vesnici u vody prakticky povinnost.

**Souvislosti:** [Ragdoll: active ragdoll](ragdoll.md#active-ragdoll-motory-rizene-rychlosti) · [Game feel a imerze](../teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida) · [Rejstřík: physics control](../rejstrik.md#physics-control)
