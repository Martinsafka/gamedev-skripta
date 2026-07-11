# Interaktivní voda: vlnky pod nohama

Voda, která na tebe *odpovídá* — vlnky za postavou, kruhy po hozené bedně — je jeden z nejlevnějších imerzních efektů vůbec. Dvě cesty: od 5.6 **zaškrtávátko** (Water Advanced plugin + shallow water subsystem) a pro starší verze či plnou kontrolu ruční **Niagara Fluids** simulace. Obě jsou 2D grid simulace hladiny — liší se jen tím, kdo ji zapojuje.

---

## 5.6+: Water Advanced a shallow water subsystem

**Zdroj:** [How To Enable Water Interaction - Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=EUbSj2hEMCE) · [Pitchfork Academy](https://www.youtube.com/channel/UCXp4W8jzNe280dGy_IvKX4Q) · ~11 min ·
[How To Make Interactive Water Simulation (Just Like The Witcher 4)](https://www.youtube.com/watch?v=kkwXxeys8JE) · [MakeCodeSimple_Unreal](https://www.youtube.com/channel/UCshQIu-qsu9rDqTqK6X2GHQ) · ~7 min

**Shrnutí:** Od 5.6 je interakce s vodou vestavěná: zapnout plugin **Water Advanced** (k běžnému Water) [(1:34)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=94s) a v Project Settings **Use Default Shallow Water Subsystem** [(2:23)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=143s) — pod kapotou Niagara 2D grid simulace. Postava pak dělá vlnky **ve všech water bodies** bez jediného uzlu navíc.

### Rozpad myšlenky

Dva restarty editoru (po pluginech a po project setting) a funguje to napříč oceánem, jezerem i řekou [(8:35)](https://www.youtube.com/watch?v=EUbSj2hEMCE&t=515s). Jediný zádrhel z praxe: při prvním spuštění se simulace může pár vteřin kompilovat a vypadá to, že nefunguje — počkat, nefixovat [(3:08)](https://www.youtube.com/watch?v=kkwXxeys8JE&t=188s).

> **Pozn.:** MakeCodeSimple to prodává titulkem „jako Witcher 4" — a není to klik-bait nadsázka: tech demo CDPR běželo na stejném engine základě a interaktivní hladina je přesně ten detail, který v demu prodával les. Water Advanced je experimental (5.6) — pro shipping s tím počítej; pro vývoj a prototyp bez debat nejrychlejší cesta. Kdo je na 5.5 a starších, jde na ruční setup z další myšlenky — výsledek je stejná simulace.

**Souvislosti:** [Voda a buoyancy: water bodies](voda-a-buoyancy.md#vodni-telesa-spliny-napojeni-na-teren-a-reka-s-proudem) · [Game feel a imerze](../teorie/game-feel.md#imerze-svet-ktery-na-tebe-odpovida) · [Rejstřík: water body](../rejstrik.md#water-body)

---

## Niagara Fluids ručně: Grid 2D šablona a collider tagy

**Zdroj:** [Unreal 5 - Realistic Interactive Water in 5 Minutes](https://www.youtube.com/watch?v=i9Bfg5H_fKM) · [renderBucket](https://www.youtube.com/channel/UCK6qQleNA8zZ2BNTESe2cag) · ~7 min ·
[Making Interactive Water in Unreal Engine](https://www.youtube.com/watch?v=QdwKSsVjYo8) · [sappydev](https://www.youtube.com/channel/UCpbGb4X4C1B_GKpdSb6ImgA) · ~6 min ·
[Create Realistic & Interactive Water in 5 minutes in Unreal 5.5](https://www.youtube.com/watch?v=FqkS6Ke0ouE) · [LearningTheWires](https://www.youtube.com/channel/UCjX1pD1w4UGH_6PFF3Z34hA) · ~5 min

**Shrnutí:** Tři tutoriály, jeden postup: plugin **Niagara Fluids** → nový Niagara systém ze šablony **Grid 2D SW Particle Collisions** → smazat demo emittery → kolize přes **tagy „collider"** na systému i objektech → doladit tři parametry (dissipation, delta time, collision multiplier), ať postava nedělá tsunami.

### Rozpad myšlenky

**Setup:** šablona obsahuje demo kouli — smazat emitter „shallow water collision particles" i vypnutý „secondary" [(0:50)](https://www.youtube.com/watch?v=i9Bfg5H_fKM&t=50s). Ve scéně systému nastavit user parametr **World Grid Size** podle plochy (např. 3000×3500) [(1:37)](https://www.youtube.com/watch?v=i9Bfg5H_fKM&t=97s).

**Kolize přes tagy:** systém má v user parametrech **Actor Tags** a **Component Tags** — default „collider". Cokoli má stejný tag (actor tag + component tag na meshi), dělá vlny: postava, krabice, sud [(2:25)](https://www.youtube.com/watch?v=i9Bfg5H_fKM&t=145s), [(5:33)](https://www.youtube.com/watch?v=i9Bfg5H_fKM&t=333s). Pozor na **lowercase** — tag je case-sensitive [(1:52)](https://www.youtube.com/watch?v=QdwKSsVjYo8&t=112s).

**Ladicí trio** (default postava dělá vlny jako náklaďák):

- **Velocity Dissipation** (emitter summary → simulation) — jak rychle vlny odezní; 0,005–0,1 [(3:57)](https://www.youtube.com/watch?v=i9Bfg5H_fKM&t=237s), [(3:09)](https://www.youtube.com/watch?v=FqkS6Ke0ouE&t=189s).
- **Delta Time Multiplier** (emitter update → Update Sim Attributes) — tempo simulace; 0,4–0,5 [(4:46)](https://www.youtube.com/watch?v=i9Bfg5H_fKM&t=286s).
- **Collision Velocity Multiplier** (collisions tab) — kolik rychlosti kolize předá vodě; 0,1–0,2 [(4:46)](https://www.youtube.com/watch?v=i9Bfg5H_fKM&t=286s), [(3:55)](https://www.youtube.com/watch?v=FqkS6Ke0ouE&t=235s).

**Kvalita a okraje:** Resolution Max Axis ~512 pro jemnější vlny, Bottom Depth ~−20 zklidní hladinu [(2:41)](https://www.youtube.com/watch?v=QdwKSsVjYo8&t=161s); čára na okraji gridu zmizí volbou **„dissipate waves near edge"** v emitteru [(3:27)](https://www.youtube.com/watch?v=QdwKSsVjYo8&t=207s). K ladění poslouží Niagara **debug overview** [(5:02)](https://www.youtube.com/watch?v=QdwKSsVjYo8&t=302s).

> **Pozn.:** Tohle je tatáž technologie, kterou 5.6 zapíná checkboxem — ruční verze má smysl na starších verzích a tam, kde chceš vodní plochu *mimo* water body (bazén, kaluž, žlab). Hodnoty ladicího tria se mezi autory liší (0,005 vs. 0,1 dissipation) — nejsou „správné", jsou per projekt; důležité je vědět, které tři knoflíky existují. A spojení s [krokovým systémem](footsteps.md) se nabízí: stejné tagy, stejná filozofie „svět odpovídá".

**Souvislosti:** [Kroky a povrchy](footsteps.md) · [Rejstřík: Niagara Fluids](../rejstrik.md#niagara-fluids) · [Rejstřík: Niagara Data Channel](../rejstrik.md#niagara-data-channel)
