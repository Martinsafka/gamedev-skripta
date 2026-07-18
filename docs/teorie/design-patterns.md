# Design patterns: slovník osvědčených řešení

Design patterns jsou pojmenovaná řešení problémů, které se v kódu vracejí pořád dokola — nezávisle na jazyku i enginu. ForrestKnight prochází sedm nejužitečnějších; tahle kapitola k nim přidává, co video nemá: **překlad do UE a Blueprintů**, kde většinu z nich používáš denně, aniž jim tak říkáš. Vzory nejsou dogma ani checklist — jsou to slova. Kdo je zná, umí pojmenovat, co staví, a rozpoznat, co čte.

---

## Tři rodiny vzorů: tvorba, struktura, chování

**Zdroj:** [7 Design Patterns EVERY Developer Should Know](https://www.youtube.com/watch?v=BJatgOiiht4) · [ForrestKnight](https://www.youtube.com/channel/UC2WHjPDvbE6O328n17ZGcfg) · ~22 min, výklad s příklady

**Shrnutí:** V roce 1994 „Gang of Four" katalogizoval 23 vzorů do tří rodin [(0:49)](https://www.youtube.com/watch?v=BJatgOiiht4&t=49s): **creational** (jak objekty vznikají), **structural** (jak spolu drží pohromadě) a **behavioral** (jak spolu komunikují a dělí si odpovědnosti). Vzory nejsou vynálezy — jsou to *pojmenování* řešení, která dobří programátoři nacházejí opakovaně [(0:01)](https://www.youtube.com/watch?v=BJatgOiiht4&t=1s).

### Rozpad myšlenky

Z creational rodiny video vybírá tři:

- **Singleton** [(1:35)](https://www.youtube.com/watch?v=BJatgOiiht4&t=95s): garantovaná jediná instance s globálním přístupem — centrální logger, connection pool. Trade-off je ale ostrý [(2:22)](https://www.youtube.com/watch?v=BJatgOiiht4&t=142s): mizerně se testuje (zkus to mocknout), ve vícevláknovém prostředí potřebuje ošetření a upřímně je to „glorifikovaná globální proměnná" [(3:08)](https://www.youtube.com/watch?v=BJatgOiiht4&t=188s). Použij, když *potřebuješ garanci jedné instance* — ne když se ti jen chce globální stav.
- **Builder** [(3:08)](https://www.youtube.com/watch?v=BJatgOiiht4&t=188s): konstruktor s patnácti volitelnými parametry nahradíš řetězenými metodami — volají se v libovolném pořadí, volitelné se přeskočí a kód „se čte jako angličtina" [(3:56)](https://www.youtube.com/watch?v=BJatgOiiht4&t=236s). Nová volba = nová metoda, žádné přepisování všech call-sites [(4:42)](https://www.youtube.com/watch?v=BJatgOiiht4&t=282s).
- **Factory** [(5:30)](https://www.youtube.com/watch?v=BJatgOiiht4&t=330s): if/else les kolem `new Admin / new Moderator / new User` se schová do jedné třídy; navenek jen `create(typ)` [(6:16)](https://www.youtube.com/watch?v=BJatgOiiht4&t=376s). Odměna: veškerá tvořicí logika (logging, pooling, změny) na jednom místě [(7:02)](https://www.youtube.com/watch?v=BJatgOiiht4&t=422s). Signál k použití: `new` rozseté po celém codebase.

A dva structural:

- **Facade** [(7:50)](https://www.youtube.com/watch?v=BJatgOiiht4&t=470s): tlačítko „koupit" schovává platby, sklad, dopravu i fraud detection — jedna hezká fasáda před spletí subsystémů; autor sám přiznává, že je to „nóbl slovo pro zapouzdření" [(9:24)](https://www.youtube.com/watch?v=BJatgOiiht4&t=564s). `fetch()` je fasáda nad TCP a retry logikou [(10:59)](https://www.youtube.com/watch?v=BJatgOiiht4&t=659s). Riziko: fasáda, která ví a dělá moc, degeneruje v god object [(10:59)](https://www.youtube.com/watch?v=BJatgOiiht4&t=659s).
- **Adapter** [(11:46)](https://www.youtube.com/watch?v=BJatgOiiht4&t=706s): USB→HDMI pro kód. Třetístranné API vrací Celsia a kilometry, tvá appka čeká Fahrenheity a míle → wrapper třída s konverzí uvnitř, místo konverzní logiky rozseté po projektu [(12:33)](https://www.youtube.com/watch?v=BJatgOiiht4&t=753s).

> **Pozn.:** UE překlady: singleton žije v enginu jako **Game Instance** a **Subsystems** — jednu instanci garantuje engine sám a je to správné místo pro „globální" stav ([kde co bydlí](../praxe/principy-architektury.md)); varování o glorifikované globálce platí i tady — co tam nacpeš, to se ti rozleze. Factory je každý **spawner**: `SpawnActor` schovaný za funkcí, která podle typu nepřítele nastaví mesh, statistiky a drop. Facade je dobře navržená **komponenta**: navenek `Interact()`, uvnitř trace, UI, zvuk. Adapter je wrapper Blueprint kolem pluginu, kterému nechceš vydat celý projekt všanc — když plugin vyměníš, přepisuješ jednu třídu.

**Souvislosti:** [Principy architektury](../praxe/principy-architektury.md) · [Rejstřík: Design pattern](../rejstrik.md#design-pattern) · [Rejstřík: Singleton](../rejstrik.md#singleton) · [Rejstřík: God class](../rejstrik.md#god-class)

---

## Strategy a observer: dva vzory, které v UE používáš denně

**Zdroj:** [7 Design Patterns EVERY Developer Should Know](https://www.youtube.com/watch?v=BJatgOiiht4) · [ForrestKnight](https://www.youtube.com/channel/UC2WHjPDvbE6O328n17ZGcfg) · stejné video, behaviorální vzory

**Shrnutí:** Behaviorální rodina řeší komunikaci a dělbu odpovědností — a obsahuje vzor, který autor bez ironie korunuje: „just always use the strategy pattern" [(0:49)](https://www.youtube.com/watch?v=BJatgOiiht4&t=49s). **Strategy** = rodina zaměnitelných algoritmů, každý ve své třídě za společným rozhraním [(14:53)](https://www.youtube.com/watch?v=BJatgOiiht4&t=893s). **Observer** = objekty se přihlašují k odběru událostí jiného objektu [(18:47)](https://www.youtube.com/watch?v=BJatgOiiht4&t=1127s) — YouTube zvoneček jako architektura.

### Rozpad myšlenky

**Strategy** na příkladu cesty do práce [(15:40)](https://www.youtube.com/watch?v=BJatgOiiht4&t=940s): cíl je jeden (dostat se tam), strategií víc (auto, bus, kolo). Bez vzoru roste if/else strom, kde každá větev nese vlastní logiku a každý nový dopravní prostředek ho prodlužuje [(15:40)](https://www.youtube.com/watch?v=BJatgOiiht4&t=940s). Se vzorem: rozhraní `TransportStrategy`, jedna třída na strategii, `setStrategy(...)` a jediné volání `goToWork()` [(16:26)](https://www.youtube.com/watch?v=BJatgOiiht4&t=986s). Je to „programování na úrovni rozhraní" [(17:14)](https://www.youtube.com/watch?v=BJatgOiiht4&t=1034s) a čistá ukázka **open-closed principu**: nové chování přidáš novou třídou, bez sahání do existujícího kódu [(18:00)](https://www.youtube.com/watch?v=BJatgOiiht4&t=1080s). Cena: víc tříd — pořád lepší než if/else v dvaceti kopiích.

**Observer** na YouTube [(19:34)](https://www.youtube.com/watch?v=BJatgOiiht4&t=1174s): místo „při uploadu projdi smyčkou 600 000 odběratelů" se odběratelé **sami přihlásí** (subscribe/unsubscribe) a kanál při události zavolá notify — nová odběratelka nevyžaduje žádnou změnu v kanálu [(20:21)](https://www.youtube.com/watch?v=BJatgOiiht4&t=1221s). Užití všude, kde něco *čeká na událost*: monitoring chyb, změny stavu, UI. Gotcha z praxe [(21:09)](https://www.youtube.com/watch?v=BJatgOiiht4&t=1269s): **event callback hell** — událost spouští událost spouští událost, a najednou ladíš notifikaci „ze tří týdnů zpátky". Používej střídmě a drž řetězy událostí krátké.

> **Pozn.:** Tady se kruh uzavírá s kapitolou [Komunikace Blueprintů](../praxe/komunikace-blueprintu.md): **Event Dispatcher je observer pattern** — doslova, včetně bind/unbind a notify; „přihlas se u zdroje, nečekej, až tě někdo obejde smyčkou". A strategy pattern v UE potkáš pokaždé, když vyměňuješ chování za společným rozhraním: [movement modes v Moveru](../praxe/mover.md) (každý režim pohybu = zaměnitelná třída), [choosery](../praxe/mm-systemy.md) vybírající animační logiku podle stavu, Blueprint Interface místo kaskády castů. Vzory ti nedávají nové nody — dávají ti jistotu, že tenhle tvar grafu je *správně* a proč.

**Souvislosti:** [Komunikace Blueprintů](../praxe/komunikace-blueprintu.md) · [Mover](../praxe/mover.md) · [Rejstřík: Observer pattern](../rejstrik.md#observer-pattern) · [Rejstřík: Strategy pattern](../rejstrik.md#strategy-pattern) · [Rejstřík: Event dispatcher](../rejstrik.md#event-dispatcher)
