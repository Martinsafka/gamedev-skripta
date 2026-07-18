# Komunikace Blueprintů: cast, interface, dispatcher

Jak spolu mají Blueprinty mluvit je nejčastější architektonická otázka v UE — a odpověď má tři (a půl) podoby. Tahle kapitola dává vedle sebe mechaniku všech metod z tutoriálu Unreal University a doplňuje ji rozhodovacím pravidlem, kdy kterou sáhnout; čtvrtou cestu (broadcast kanály) přidává krátký klip Taken Grace.

---

## Tři kanály a kdy který: cast, interface, event dispatcher

**Zdroj:** [All 3 Blueprint Communication Methods in Unreal Engine Explained in Under 18 Minutes](https://www.youtube.com/watch?v=ZSRSktpezII) · [Unreal University](https://www.youtube.com/channel/UCQv4mwerZLQVe3wPbsMc-qw) · ~18 min, tutoriál (pes, papoušek, kostka)

**Shrnutí:** **Casting** ověří, že neznámý objekt je konkrétní třída, a zpřístupní všechno, co v ní je [(1:08)](https://www.youtube.com/watch?v=ZSRSktpezII&t=68s). **Interface** je sada funkcí bez implementace — každý blueprint si je naplní po svém [(6:04)](https://www.youtube.com/watch?v=ZSRSktpezII&t=364s). **Event dispatcher** je rádio: jeden vysílá, kdokoli přihlášený slyší [(11:44)](https://www.youtube.com/watch?v=ZSRSktpezII&t=704s). Mechanicky je zvládneš za odpoledne; architektonicky rozhodují o tom, kdo na kom závisí.

### Rozpad myšlenky

**Cast** [(1:27)](https://www.youtube.com/watch?v=ZSRSktpezII&t=87s): `Cast To BP_Dog` na actor z overlapu/hitu — uspěje-li, máš k dispozici funkce i proměnné psa (zavolej `Bark`, přečti jméno). Neuspěje-li (trefil jsi papouška), jede větev Failed [(3:16)](https://www.youtube.com/watch?v=ZSRSktpezII&t=196s). Legitimní použití: když cílovou třídu *z podstaty znáš* — `Get Player Character → Cast To BP_PlayerCharacter` [(4:41)](https://www.youtube.com/watch?v=ZSRSktpezII&t=281s) je v pořádku, hráčova třída je jistota. Past: cast vytváří tvrdou závislost a řetěz „zkus psa, zkus papouška, zkus dveře…" neškáluje — viz [Reference Viewer diagnóza](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data).

**Interface** [(6:04)](https://www.youtube.com/watch?v=ZSRSktpezII&t=364s): vytvoř `BPI_Interact` s funkcí `Interact`, implementuj v `Class Settings → Interfaces` u psa i papouška [(7:05)](https://www.youtube.com/watch?v=ZSRSktpezII&t=425s) — každý reaguje po svém (pes si sedne, papoušek mluví). Volající se ptá `Does Object Implement Interface` [(9:55)](https://www.youtube.com/watch?v=ZSRSktpezII&t=595s) a volá message — bez znalosti třídy, bez závislosti; kdo neimplementuje, prostě nereaguje. Interface funkce umí vstupy i výstupy [(11:00)](https://www.youtube.com/watch?v=ZSRSktpezII&t=660s). Typické použití: interakční systémy — jeden volající, mnoho různých příjemců.

**Event dispatcher** [(11:44)](https://www.youtube.com/watch?v=ZSRSktpezII&t=704s): vlastník (hráč) deklaruje dispatcher a v pravou chvíli ho `Call`ne [(12:12)](https://www.youtube.com/watch?v=ZSRSktpezII&t=732s); posluchači se na BeginPlay `Bind`nou [(13:14)](https://www.youtube.com/watch?v=ZSRSktpezII&t=794s) a dodají vlastní custom event. Posluchačů může být libovolně mnoho [(14:55)](https://www.youtube.com/watch?v=ZSRSktpezII&t=895s) (kostka mění barvu, level blueprint loguje — každý nezávisle), jde se odhlásit (`Unbind` [(15:51)](https://www.youtube.com/watch?v=ZSRSktpezII&t=951s)) a dispatcher umí nést parametry [(16:57)](https://www.youtube.com/watch?v=ZSRSktpezII&t=1017s). Typické použití: „stalo se X, koho to zajímá" — jeden vysílá, N poslouchá, vysílač o posluchačích neví.

> **Pozn.:** Rozhodovací zkratka, kterou video neříká explicitně, ale plyne z [loose couplingu](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data): **cast**, když třídu garantuješ (vlastní player, GameMode); **interface**, když se ptáš cizího „umíš tohle?"; **dispatcher**, když oznamuješ „stalo se tohle" a nechceš vědět komu. Směr závislosti: cast váže volajícího na třídu, interface na smlouvu, dispatcher nikoho na nic — posluchač závisí na vysílači, ne obráceně.

**Souvislosti:** [Principy architektury](principy-architektury.md) · [Interakce bez Event Ticku](interakce-bez-event-ticku.md) · [Design patterns: strategy a observer](../teorie/design-patterns.md#strategy-a-observer-dva-vzory-ktere-v-ue-pouzivas-denne) *(dispatcher je observer pattern jménem)* · [Rejstřík: Cast](../rejstrik.md#cast) · [Rejstřík: Blueprint Interface](../rejstrik.md#blueprint-interface) · [Rejstřík: event dispatcher](../rejstrik.md#event-dispatcher)

---

## Čtvrtý kanál: broadcast přes subsystem s payloady

**Zdroj:** [Unreal Engine: Boost Game Perf with Smart Broadcasts! #shorts](https://www.youtube.com/watch?v=dIXGXiB9Okc) · [Taken Grace](https://www.youtube.com/channel/UCLagdpQoUG-jtyH8bF0IGZg) · ~1,5 min, výřez z delšího videa

**Shrnutí:** Nad třemi klasikami existuje ještě messagingový vzor: **broadcast kanály** přes game instance subsystem — vysílač pošle zprávu na pojmenovaný kanál s payloadem (struct) a subsystem ji doručí všem posluchačům kanálu [(0:01)](https://www.youtube.com/watch?v=dIXGXiB9Okc&t=1s). Na nanosekundy je to *pomalejší* než dispatcher — a přesto to v součtu šetří výkon.

### Rozpad myšlenky

Mechanika: posluchač se „naladí" na kanál (např. `GoldCollector`) a deklaruje očekávaný **payload typ** — struct, který se musí shodovat přesně, jinak zpráva nedorazí [(0:48)](https://www.youtube.com/watch?v=dIXGXiB9Okc&t=48s); on message received pak spustí vlastní logiku. Vysílač jen broadcastne kanál + payload a nikoho nezná.

Proč je to výhra, když je samotné volání pomalejší: **žádné hard reference** [(0:01)](https://www.youtube.com/watch?v=dIXGXiB9Okc&t=1s). Dispatcher vyžaduje, aby posluchač měl referenci na vysílač (bind na konkrétní objekt) — a reference znamená, že se s levelem nahrává i všechno navázané. Kanálový messaging přes subsystem (žije po celou dobu běhu aplikace) obě strany úplně odpojí: level se načte bez tahání závislostí. Klasický trade-off mikrovýkon vs. architektura — a druhý vyhrává.

> **Pozn.:** Tohle je Blueprint podoba vzoru, který [ability systém](principy-architektury.md#tri-principy-skalovatelnosti-separace-volne-vazby-data) řešil event manager subsystémem a který v Lyře žije jako Gameplay Message Subsystem. Klip je výřez (~1,5 min) — kompletní stavbu systému má autor na kanále; pro nás je podstatný princip. Kombinuje se skvěle s [gameplay tagy](gameplay-tags.md) jako názvy kanálů/eventů.

**Souvislosti:** [Principy architektury](principy-architektury.md) · [Gameplay Tags](gameplay-tags.md) · [Rejstřík: subsystem](../rejstrik.md#subsystem) · [Rejstřík: hard reference](../rejstrik.md#hard-reference)
