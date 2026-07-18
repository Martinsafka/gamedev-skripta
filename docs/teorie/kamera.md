# Kamera: neviditelný designér

Kamera je mechanika, kterou hráč nikdy „nehraje" — a přitom formuje každou vteřinu zážitku. Devlog Inbound Shovel o převodu lineárního platformeru (Isadora's Edge) na metroidvanii ukazuje, kolik designu se skrývá v systému, který jen „sleduje postavu": falešné hranice kvůli tajemstvím, look ahead, který dýchá s pohybem, objekty kradoucí pozornost — a zoom v pixel artu, který „nešel", dokud šel. Hororovou stranu kamery (fixní úhly, pohled monstra) kryje [Horor design](horor-design.md#cyklus-napeti-pet-kroku-kamera-a-rozpocet-na-jump-scary).

---

## Kamera metroidvanie: hranice, které umí lhát

**Zdroj:** [How Metroidvania Cameras are Shockingly Different than Platformer Cameras](https://www.youtube.com/watch?v=drbatB2KWlo) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~21 min, devlog

**Shrnutí:** Stejné skákání, stejný combat — a při převodu na metroidvanii bylo potřeba přepsat skoro celý kamerový systém [(0:01)](https://www.youtube.com/watch?v=drbatB2KWlo&t=1s). Důvod číslo jedna: **tajemství**. Bez falešných hranic kamera odhalí skrytou místnost dřív, než do ní hráč vkročí — „kamera se složila pod nulovým tlakem; tomu se nedá říkat tajemství" [(0:47)](https://www.youtube.com/watch?v=drbatB2KWlo&t=47s).

### Rozpad myšlenky

Řešení jsou **camera directors** [(1:34)](https://www.youtube.com/watch?v=drbatB2KWlo&t=94s): každá místnost má výchozího režiséra kamery (drží hranice tak, aby tajemství zůstala skrytá), a trigger zóny s vlastními režiséry, kteří řízení převezmou — vejdeš do tajné chodby a hranice se posunou. Aby předání nebylo skokové, hranice se **tweenují** — a tím začíná kaskáda problémů, která je sama o sobě lekce: (1) během tweenu kamera ignoruje pohyb hráče → **player push ahead** (pohyb hráče se přičítá nad tween); vizuálně skoro nevidět, „rozdíl v game feelu masivní" [(2:20)](https://www.youtube.com/watch?v=drbatB2KWlo&t=140s); (2) tween na vzdálenou hranici by letěl přes celou obrazovku → **princip půl obrazovky** [(3:07)](https://www.youtube.com/watch?v=drbatB2KWlo&t=187s): tweenuj vždy jen k efektivní *viditelné* hranici, protože cokoli dál než půl obrazovky od postavy je stejně mimo záběr — všechny tweeny pak měří 0 až půl obrazovky a dají se konzistentně vyladit. Následoval hon na edge cases (wiggle exploit push aheadu, škubnutí při dokončení tweenu s hráčem mimo obraz [(4:41)](https://www.youtube.com/watch?v=drbatB2KWlo&t=281s)) — daň za systém, který navenek „jen plynule jede".

Bonus, který z režisérů vypadl zadarmo: **cinematic framing** [(9:21)](https://www.youtube.com/watch?v=drbatB2KWlo&t=561s) — chodba s vysokým stropem dostane zónu, která zvedne spodní hranici, kamera plavně vypanuje nahoru a na konci chodby zase dolů. Level design tím získává výrazový prostředek bez cutscén.

> **Pozn.:** Obecná lekce pod tím: kamera je **součást level designu**. „Tajná místnost" není geometrie — je to dohoda mezi geometrií a kamerou; totéž říká [Horor design](horor-design.md#cyklus-napeti-pet-kroku-kamera-a-rozpocet-na-jump-scary) o fixních úhlech a klaustrofobii. A příběh tweeny-plodí-bugy je miniatura [„každé řešení vytvoří nový problém"](game-feel.md#combat-je-rytmus-kazdy-utok-ma-ucel-a-placeholder-je-nastroj) ze SILKROAD finišerů.

**Souvislosti:** [Prostor a hranice](prostor-a-hranice.md) · [Horor design: kamera](horor-design.md#cyklus-napeti-pet-kroku-kamera-a-rozpocet-na-jump-scary) · [Rejstřík: Camera director](../rejstrik.md#camera-director)

---

## Look ahead, focus objekty a zoom, který „nešel"

**Zdroj:** [How Metroidvania Cameras are Shockingly Different than Platformer Cameras](https://www.youtube.com/watch?v=drbatB2KWlo) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · stejné video, druhá půlka

**Shrnutí:** Tři menší systémy s velkým dopadem: **look ahead**, který se přizpůsobí obousměrnému pohybu a skoku; **focus objekty**, které si ukradnou nastavitelné procento pozornosti kamery; a **zoom v pixel artu** — funkce odepsaná jako nemožná, dokud ji nevyřešila změna úhlu pohledu na problém [(14:47)](https://www.youtube.com/watch?v=drbatB2KWlo&t=887s).

### Rozpad myšlenky

**Look ahead** [(10:07)](https://www.youtube.com/watch?v=drbatB2KWlo&t=607s): lineární hra si vystačí s Mario-stylem (předsazení doprava, směrem cesty); metroidvania se hraje tam i zpět, takže kamera předsazuje podle směru pohybu à la Hollow Knight. Zajímavější je vertikála [(10:53)](https://www.youtube.com/watch?v=drbatB2KWlo&t=653s): na zemi kamera kouká kus **nad hlavu** (plánuješ skok), v apexu skoku sjede na střed těla a při pádu **pod nohy** (potřebuješ vidět, kam padáš) — a z toho mimochodem vypadl přirozený „bump" kamery při dopadu, který autor nenavrhl, jen si ho nechal [(11:39)](https://www.youtube.com/watch?v=drbatB2KWlo&t=699s). Kamera tu doslova sleduje *pozornost* hráče, ne jeho sprite.

**Focus objekty** [(12:26)](https://www.youtube.com/watch?v=drbatB2KWlo&t=746s): důležitý terminál v chodbě si přes trigger zónu vezme část fokusu kamery — nastavitelné procento od 95 % („kamera skoro ignoruje postavu") po 10 % („jemné pošťouchnutí, aby sis všiml"). Podpora více objektů najednou i pohyblivých — a z toho nápad vzniklý přímo při natáčení: nepřítel jako pohyblivý focus objekt = zárodek lock-on kamery [(14:47)](https://www.youtube.com/watch?v=drbatB2KWlo&t=887s). Je to [vedení hráče](vedeni-hrace.md) přeložené do kamery: pozornost se dá režírovat i bez šipky na obrazovce.

**Zoom v pixel artu** [(14:47)](https://www.youtube.com/watch?v=drbatB2KWlo&t=887s): dvě „nemožnosti" — škálovaný pixel art vypadá strašně (vestavěný zoom to potvrdil) a pixel-perfect mřížka vyžaduje celočíselné škálování (360p → 3× na 1080p, 4× na 1440p; necelé faktory míchají pixely 3×3 s 2×3 [(15:35)](https://www.youtube.com/watch?v=drbatB2KWlo&t=935s)). Průlom: neměnit kameru, ale **škálování finálního renderu** — artefakty zmizely [(16:22)](https://www.youtube.com/watch?v=drbatB2KWlo&t=982s). A druhá „nemožnost" padla empiricky: necelé faktory sice teoreticky lámou mřížku, ale v testu čtyř klipů to prakticky nikdo nepozná — včetně chytráků, kteří tipnou „žádný není pixel-perfect" a spletou se [(17:55)](https://www.youtube.com/watch?v=drbatB2KWlo&t=1075s). Pátá feature za zmínku: look up/down na podržení — žánrový staple, o jehož zařazení nechává autor hlasovat diváky, protože ho sám skoro nepoužívá [(19:28)](https://www.youtube.com/watch?v=drbatB2KWlo&t=1168s).

> **Pozn.:** Dvě přenositelné lekce nad rámec kamer: „nemožné" featury často stojí na jedné nevyslovené premise (tady: „zoom = zoom kamery") — vyměň premisu a problém zmizí; a **teoretická vada ≠ vnímaná vada** — pixel-perfect dogma neprošlo slepým testem. Měř očima hráče, ne pravidlem. (Video obsahuje sponzorský segment Brilliant [(7:48)](https://www.youtube.com/watch?v=drbatB2KWlo&t=468s) — fakta z něj nečerpám.)

**Souvislosti:** [Vedení hráče](vedeni-hrace.md) · [Game feel a imerze](game-feel.md) · [Rejstřík: Look ahead](../rejstrik.md#look-ahead) · [Rejstřík: Pixel-perfect](../rejstrik.md#pixel-perfect)
