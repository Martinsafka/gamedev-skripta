# Multiplayer: high-level API

Jediná myšlenka, ale stojí za samostatnou kapitolu, protože odpovídá na otázku, kterou si u multiplayeru položíš první: **kolik z toho za tebe udělá engine?** Godot nabízí dvě úrovně a rozdíl mezi nimi je zásadní — jedna ti dá hratelný prototyp za odpoledne, druhá kontrolu nad každým paketem a s ní všechnu práci.

Playlist pokrývá jen tu první. Nízkoúrovňová cesta (vlastní synchronizace, ruční správa paketů) tady chybí a je to potřeba mít na paměti: **kapitola ukazuje strop, ne celý obor.**

---

## High-level API: spawner, synchronizer a otázka, kdo koho ovládá

**Zdroj:** [Godot Multiplayer Tutorial: The Quick and Easy High-Level API](https://www.youtube.com/watch?v=YnfsyZJRsL8) · [IcyEngine](https://www.youtube.com/channel/UCmKDrObnr6ubDnF7fZxJ22Q) · ~8 min, tutoriál

**Shrnutí:** Vysokoúrovňové API vymění kontrolu za rychlost: **`MultiplayerSpawner`** se postará o to, aby objekt vzniklý na serveru vznikl i u všech klientů, **`MultiplayerSynchronizer`** hlídá vybrané vlastnosti, a ty napíšeš zhruba padesát řádků. Háček, na kterém stojí celý funkční příklad a v tutoriálech se snadno přehlédne: **autorita** — bez jejího předání ovládá všechny postavy server.

### Rozpad myšlenky

**Volba úrovně napřed** [(0:32)](https://www.youtube.com/watch?v=YnfsyZJRsL8&t=32s), protože je to rozhodnutí, ne detail. Dokumentace to podle autora formuluje jednoznačně: vysokoúrovňové API *„obětuje část jemné kontroly výměnou za snadnost použití"* a *„většinu těžké práce udělá na pozadí"*. Vhodné pro začátečníky, rychlé prototypy a malé hry bez složitého net kódu. Nízkoúrovňové API dá **holé minimum** na postavení serveru a synchronizaci i práci s pakety **nechá na tobě**.

**Skladba scény** má čtyři kusy [(1:22)](https://www.youtube.com/watch?v=YnfsyZJRsL8&t=82s): **network handler** (metody na spuštění serveru a klienta), **UI** se dvěma tlačítky, **spawner** a **hráč**, jehož pozice se synchronizuje.

**Server a klient** stojí na `ENetMultiplayerPeer` [(2:09)](https://www.youtube.com/watch?v=YnfsyZJRsL8&t=129s) — výchozí implementaci Godotu. Potřebuje IP adresu (při testování `localhost`) a port; ten smí být cokoli mezi 0 a 65535, ale autor doporučuje **vybrat číslo, které není v seznamu obsazených portů**. U serveru se dá zadat maximální počet klientů; bez zadání je to 32. Handler se registruje jako **autoload**, aby na něj UI i zbytek hry dosáhly odkudkoli — [event bus](signaly.md#event-bus-kdyz-se-systemy-nemaji-cim-potkat) v jiné roli.

**`MultiplayerSpawner`** [(3:46)](https://www.youtube.com/watch?v=YnfsyZJRsL8&t=226s) *„automaticky replikuje spawnovatelné nody z autority na ostatní peery"* — vytvoří-li hráče server, node se sám objeví i u všech klientů **včetně těch, kteří se právě připojili**. Skript k němu přesto patří, a je v něm jeden důležitý řádek: obsluha signálu `peer_connected` **hned na začátku skončí, pokud neběží na serveru** (`if not multiplayer.is_server(): return`). Bez toho by se hráč vytvářel na každém stroji zvlášť a spawner by to duplikoval.

**Jméno nodu jako identita** [(4:32)](https://www.youtube.com/watch?v=YnfsyZJRsL8&t=272s) je trik, který drží celý zbytek: nový hráč se **pojmenuje podle ID připojeného peera**, a protože **jména se přes spawner synchronizují**, má týž objekt stejné jméno u všech. Přidání do stromu se dělá **odloženě** (`add_child` deferred), aby se to nestalo uprostřed zpracování fyziky.

**`MultiplayerSynchronizer`** [(6:10)](https://www.youtube.com/watch?v=YnfsyZJRsL8&t=370s) je druhý vestavěný node: v záložce *Replication* mu vyjmenuješ vlastnosti, které se mají posílat — v ukázce jen pozice hráče. Nic dalšího psát nemusíš.

**A teď ta autorita**, bez které příklad vypadá rozbitě [(6:10)](https://www.youtube.com/watch?v=YnfsyZJRsL8&t=370s). Hráče vytvořil server, takže mu ve výchozím stavu i **patří** — a klient se svou postavou nehne. Oprava jsou dva řádky: v `_enter_tree()` se zavolá `set_multiplayer_authority()` se **jménem nodu převedeným na číslo** (tedy ID toho klienta), a nad pohybovým kódem stojí `if not is_multiplayer_authority(): return`. Tím se pohyb počítá **jen na tom stroji, kterému postava patří**.

**Testování bez druhého počítače** [(7:01)](https://www.youtube.com/watch?v=YnfsyZJRsL8&t=421s): *Debug → Customize Run Instances*, zaškrtnout **Enable Multiple Instances** a nastavit počet — v ukázce jeden server a dva klienti naráz.

> **Pozn.:** Dvě věci, které stojí za doplnění, protože video je zamlčí. **Zaprvé**: synchronizovat pozici je nejjednodušší varianta a zároveň nejhorší z hlediska pocitu — při jakémkoli zpoždění postava „poskakuje", protože se doslova přesouvá tam, kam ji server řekne. Vážné hry proto posílají **vstupy a stav**, ne polohu, a chybějící snímky dopočítávají; v knihovně je ten princip popsaný u [Network Prediction](../rejstrik.md#network-prediction). **Zadruhé**: autoritu tady drží klient nad vlastní postavou, což je pohodlné a **důvěřuje klientovi** — pro hru mezi kamarády v pohodě, pro cokoli s žebříčky ne. Rozhodnutí „kdo je autorita" je tedy zároveň rozhodnutí o tom, komu věříš, a je to [one-way door](../rejstrik.md#one-way-door): přepsat to později znamená přepsat celý pohyb.

**Souvislosti:** [Event bus](signaly.md#event-bus-kdyz-se-systemy-nemaji-cim-potkat) *(autoload v téže roli)* · [Vlastnictví napřed, složky potom](projekt-a-vykon.md#vlastnictvi-napred-slozky-potom-main-game-jako-koordinator) *(kdo co vlastní, o patro výš)* · [Rejstřík: Network Prediction](../rejstrik.md#network-prediction) · [Rejstřík: Autoload](../rejstrik.md#autoload) · [Rejstřík: Race condition](../rejstrik.md#race-condition)
