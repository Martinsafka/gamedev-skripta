# Interakce bez Event Ticku

Interakční systém „koukni a zmáčkni E" je jedna z prvních věcí, kterou každá 3D hra potřebuje — a zároveň klasické místo, kde vzniká per-frame kód. Tahle kapitola rozebírá event-driven alternativu: místo Line Trace v Event Ticku trvalý overlap trigger, komunikace přes Blueprint Interface a pár obranných vzorů kolem.

---

## Overlap trigger místo trasování v Ticku

**Zdroj:** [How to Line Trace Without Event Tick — UE5 Tutorial](https://www.youtube.com/watch?v=rCd36pNqCeo) · [Doppelganger Studios](https://www.youtube.com/channel/UCtZgm8cpoDqBzIP1tQa0KYg) · ~16 min, krok-za-krokem Blueprint tutoriál

**Shrnutí:** Standardní přístup k interakci — každý frame vystřelit Line Trace z kamery a ptát se „na co koukám?" — je polling: 60× za vteřinu klade otázku, jejíž odpověď se mění jednou za pár vteřin. Video staví opak: dlouhá kapsle přichycená ke kameře, která **overlap eventy sama hlásí**, kdy interaktivní objekt vstoupil do zorného pole a kdy ho opustil. Logika se pak spouští jen v okamžicích změny.

### Rozpad myšlenky

**Setup kapsle** [(0:47)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=47s): do character Blueprintu přidat Capsule Collision komponentu, attachnout ji **na kameru** (drag-and-drop v hierarchii komponent) — tím kapsle kopíruje směr pohledu, což je přesně role, kterou dřív hrál trace paprsek [(1:34)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=94s). Tvar: úzká a dlouhá (video volí poloměr 15, délku ~500 jednotek — délka = dosah interakce), posunutá mírně před character capsule, aby se obě kolize nepřekrývaly.

Dva nenápadné, ale důležité detaily z videa:

- **Tvar měň přes shape parametry, ne přes Scale tool** [(2:08)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=128s). Non-uniform scale kolizních primitiv je v UE obecně zdroj problémů (deformuje kolizní výpočty); Capsule Half Height a Radius jsou k tomu určené.
- **Collision preset nastavit Custom: Ignore all, Overlap jen vybrané kanály** (WorldStatic, WorldDynamic, Pawn, PhysicsBody) [(3:56)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=236s). Trigger, který overlapuje všechno, generuje eventy o každém stéblu trávy — filtrování na úrovni kolizních kanálů je první a nejlevnější síto.

**Filtrování cílů přes Actor Tags** [(5:57)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=357s): `On Component Begin Overlap` → z Other Actor zavolat `Actor Has Tag` → Branch. Interaktivní objekty dostanou dohodnutý tag (např. `actor_interact`); všechno ostatní projde triggerem bez odezvy. Tag musí být znakově identický na obou stranách — video doporučuje copy-paste místo přepisování [(10:54)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=654s), což zní banálně, ale přesně tyhle překlepy se debugují nejhůř, protože nic nespadne, jen „to nefunguje".

**Vstup jen když má smysl** [(12:26)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=746s): begin overlap → `Enable Input`, end overlap → `Disable Input`. Klávesa E tak vůbec nemůže vystřelit mimo kontext — místo runtime podmínky „jsem u něčeho?" se přepíná samotná schopnost reagovat. Elegantní vedlejší efekt: žádný stavový boolean, který by mohl zestárnout.

> **Pozn.:** K výkonnostnímu tvrzení videa („významně zlepší performance") je fér dodat nuanci: jeden Line Trace za frame je velmi levná operace a trvalý overlap má vlastní, nenulovou cenu. Skutečný přínos je **architektonický** — event-driven kód se spouští při změnách, škáluje lépe (deset triggerů nestojí 10× tick) a hlavně drží logiku mimo Event Tick, což je v Blueprintech dobrá hygiena bez ohledu na mikrobenchmarky. Kdo potřebuje přesnost paprsku (např. míření na malé cíle), pro toho zůstává trace správný nástroj — jen ať ho spouští event nebo timer, ne Tick.

**Souvislosti:** [Blueprint Interface](#blueprint-interface-volani-bez-castu) níže · [Principy architektury](principy-architektury.md) · [Rejstřík: Event Tick](../rejstrik.md#event-tick) · [Rejstřík: Line Trace](../rejstrik.md#line-trace) · [Rejstřík: collision preset](../rejstrik.md#collision-preset)

---

## Blueprint Interface: volání bez castů

**Zdroj:** [How to Line Trace Without Event Tick — UE5 Tutorial](https://www.youtube.com/watch?v=rCd36pNqCeo) · [Doppelganger Studios](https://www.youtube.com/channel/UCtZgm8cpoDqBzIP1tQa0KYg) · stejné video, komunikační vrstva

**Shrnutí:** Druhá polovina tutoriálu řeší, jak triggeru říct „řekni tomu objektu, ať interaguje", aniž by character musel znát konkrétní třídu objektu. Odpověď je Blueprint Interface — sada funkcí bez implementace, kterou si každý interaktivní objekt implementuje po svém. Character posílá zprávu; dveře se zničí, truhla se otevře, panel zabliká — volající o tom nic vědět nemusí.

### Rozpad myšlenky

**Interface** [(4:43)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=283s) se založí jako samostatný asset se dvěma funkcemi — ve videu `ActorInteract` a `ActorStopInteract`. Interaktivní actor si interface přidá v `Class Settings → Interfaces` a implementuje eventy [(10:54)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=654s); character z overlap eventu volá **interface message** na Other Actor [(6:57)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=417s). Podstata: message call na objekt, který interface nemá, prostě tiše neudělá nic — žádný pád, žádný cast.

Proč je to lepší než `Cast To DestroyDoor`: cast vytváří **tvrdou závislost** volajícího na konkrétní třídě. S každým novým typem interaktivního objektu by v characteru přibývala větev cast-řetězce a Blueprint by si tahal reference na všechny třídy světa. Interface tu závislost obrací — character zná jen smlouvu („umíš interagovat?"), objekty ji plní. Nový typ objektu = nula změn v characteru. To je mimochodem tentýž princip, který zná každý programátor jako programování proti rozhraní; Blueprint Interface je jeho enginová podoba.

**Validated Get jako obrana proti pending kill** [(14:57)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=897s): video schválně vyrobí chybu — po zničení dveří stiskne E znovu a reference na komponentu ukazuje na objekt označený ke garbage collection („pending kill"). Fix: pravý klik na Get node → **Convert to Validated Get** — node dostane exec větve Is Valid / Is Not Valid a destruktivní logika běží jen s živou referencí [(15:43)](https://www.youtube.com/watch?v=rCd36pNqCeo&t=943s). Obecné pravidlo, které z toho plyne: **každá uložená reference na objekt, který může zaniknout, se před použitím validuje.** V Blueprintech je to jeden pravý klik; návyk, který ušetří celou třídu runtime chyb.

> **Pozn.:** Ve videu jde o dveře, které interakcí zaniknou. U objektů, které přežívají (páky, terminály), dává interface dvojice Interact/StopInteract navíc prostor pro UI — begin overlap zobrazí prompt „[E] Použít", end overlap ho schová. Stejná kostra, žádný kód navíc.

**Souvislosti:** [Overlap trigger](#overlap-trigger-misto-trasovani-v-ticku) výše · [Komunikace Blueprintů](komunikace-blueprintu.md) · [Komunikace Blueprintů: kolik stojí cast](komunikace-blueprintu.md#interface-nebo-dispatcher-a-kolik-doopravdy-stoji-cast) *(změřená cena tvrdé reference)* · [Rejstřík: Blueprint Interface](../rejstrik.md#blueprint-interface) · [Rejstřík: cast](../rejstrik.md#cast) · [Rejstřík: garbage collection](../rejstrik.md#garbage-collection)
