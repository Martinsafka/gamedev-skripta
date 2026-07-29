# Potrubí snímku: latence, jitter a frame pacing

Hráč nevidí ani jedno z čísel, na která se koukáš v `stat unit`. Vidí **kolik snímků se skutečně objevilo na monitoru** a **jak dlouho trvalo, než jeho stisk něco udělal**. Tahle kapitola je o té druhé polovině výkonu: o cestě od vstupu k fotonu, o tom, proč Unreal drží v potrubí šest snímků naráz, co za co měníš, když latenci zkracuješ — a o jevu, kdy nespadne ani jeden snímek a hra přesto škube.

Sesterská kapitola [Rozpočet snímku](rozpocet-snimku.md) řeší, kolik času máš a kde se ztrácí. Tady jde o to, co se s hotovými snímky děje dál — a jak to hráč vnímá.

---

## Snímek není fronta, je to potrubí

**Zdroj:** [A Frame's Life: Frame Timing, Synchronization, and Latency in UE](https://www.youtube.com/watch?v=dKSHw_8vz3I) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~53 min, Unreal Fest Chicago 2026

**Shrnutí:** Unreal neposkládá snímek od začátku do konce a pak další. **Herní vlákno, render vlákno, RHI vlákno a GPU běží zároveň, každé na jiném snímku** — což enginu dovoluje strávit na každé fázi víc než jeden snímek času a přesto držet cílovou frekvenci. Cena za to je, že mezi fázemi musí být **brzdy**, aby si herní vlákno neuteklo o tisíc snímků dopředu. Háček, kvůli kterému tuhle myšlenku knihovna má: **velká část toho, co v Insights vypadá jako drahá práce, je čekání na brzdě.**

### Rozpad myšlenky

**Proč paralelně** [(13:17)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=797s): kdyby fáze běžely za sebou, musely by se všechny vejít do 16,66 ms. Protože běží na vláknech přes sebe, **může každá trvat víc než jeden snímek** a hra pořád běží na cílové frekvenci. To je celá výhoda — a zdroj všeho ostatního, co je na tom složité.

**Brzdy** [(14:05)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=845s) jsou nutné, protože jinak by se při pauze (kdy herní vlákno nemá co dělat) rozjelo dopředu bez omezení. Přednáška je probírá odzadu, od GPU k hernímu vláknu:

| fáze | na co čeká |
|---|---|
| **GPU** | na volný **back buffer**; zapisuje do něj v posledním post-process průchodu |
| **RHI vlákno** | na dokončení předchozího GPU snímku (fence) — a na grafické API, když se zaplní swap chain (DirectX blokuje v `Present`) |
| **render vlákno** | na **hardwarové occlusion queries** předchozího GPU snímku |
| **herní vlákno** | na start render vlákna předchozího snímku (a na RHI vlákno dvou snímků zpět) |

**A teď to, kvůli čemu je tahle myšlenka praktická: čekání se v profileru maskuje jako práce.** Tři konkrétní případy:

- **„Occlusion trvá 15,5 ms"** [(17:09)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=1029s). Lidé se ptali, jestli je occlusion tak pomalý. Není. *„Čeká. Nic nedělá. Jen čeká, až GPU dokončí předchozí snímek."* Bonus: tyhle hardwarové queries jsou **jen pro ne-Nanite meshe** (Nanite má vlastní, čistě na GPU, bez cesty zpátky na CPU) — takže v převážně Nanite hře se dají vypnout přes `r.AllowOcclusionQueries`.
- **GPU bubble, která lže o tom, co ji způsobilo** [(14:51)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=891s). Když GPU čeká na back buffer, nemá na PC vlastní značku — takže poslední rozdělaný průchod vypadá, jako by trval celou tu dobu. *„Říká, že adaptation buffer trval 12,72 ms. Je to 12,72 ms od chvíle, kdy jsme ho začali. Ale my ho dokončili."*
- **Over-subscription** [(19:31)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=1171s) je mechanismus, kterým vlákno říká „budu chvíli čekat, probuď si zálohu a udělej něco jiného na mém jádru". V traci to vypadá jako zabrané CPU. *„Není. Jen to čeká. Je to fancy fence."*

**A poučení, které z toho autor vyvodí nahlas**: odstraníš-li jedno čekání, **přesune se jinam**, protože frame pacing má brzd víc. *„Hádej co? Bude to čekat někde jinde."*

**Kolik snímků je v potrubí** [(24:13)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=1453s) je číslo, které se vyplatí pamatovat: **šest v enginu a dva v hardwaru** (jeden se posílá kabelem, jeden se vykresluje na monitoru). Plná pipeline vypadá takto: snímek 1 se scanuje na displeji, 2 letí kabelem, 3 a 4 čekají v back bufferech, 5 je hotový na GPU a čeká na VSync, 6 stojí na `Present`, 7 je na render vláknu a čeká na occlusion queries, 8 je hotový na herním vláknu a čeká na render vlákno předchozího snímku. Devátý začít nemůže.

> **Pozn.:** Nejcennější věc téhle myšlenky je **dovednost čtení, ne nastavení**. Bez ní se v Insights dá strávit den optimalizací occlusion queries, které nic nedělají — a to je přesně ta chyba, proti které stojí celý [rozhodovací strom v Profilingu](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat): najdi vyčerpaný rozpočet, ne největší číslo. Zobecněné pravidlo, které z toho plyne a platí i mimo Unreal: **v paralelním systému je nejdelší úsek často ten, který čeká na nejkratší.** A přednáška si k tomu přidává vzácně poctivou poznámku — autor sám říká, že o značku pro čekání na back buffer požádal tým a na PC ji zatím nemá. To je dobrá připomínka, že **nástroj není pravda, je to reprezentace**; kde chybí značka, chybí i informace, a je potřeba to vědět, ne dohadovat.

**Souvislosti:** [Latence proti odolnosti](#latence-proti-odolnosti-co-za-co-menis) *(co se s tím potrubím dá dělat)* · [Jitter](#jitter-nespadne-ani-jeden-snimek-a-presto-to-skube) · [Profiling: rozhodovací strom](profiling.md#rozhodovaci-strom-stat-unit-rekne-kterym-nastrojem-pokracovat) · [Optimalizace: co blokuje hlavní vlákno](optimalizace.md#druha-osa-optimalizace-co-blokuje-hlavni-vlakno) · [Rejstřík: Unreal Insights](../rejstrik.md#unreal-insights) · [Rejstřík: VSync](../rejstrik.md#vsync) · [Rejstřík: Frame time](../rejstrik.md#frame-time)

---

## Latence proti odolnosti: co za co měníš

**Zdroj:** [A Frame's Life: Frame Timing, Synchronization, and Latency in UE](https://www.youtube.com/watch?v=dKSHw_8vz3I) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~53 min, Unreal Fest Chicago 2026

**Shrnutí:** Těch šest snímků v potrubí má dvě jména podle toho, odkud se na ně díváš. Zvenčí je to **vstupní latence** (šest snímků × frame time), zevnitř je to **odolnost proti záseku** — zásoba, ze které engine dokáže krátký výpadek pohltit, aniž hráč přišel o jediný snímek. A jsou to dvě strany jednoho čísla: **zkrátíš-li potrubí, zkrátíš latenci a zároveň zahodíš rezervu.** Háček: to je v pořádku jen tehdy, když rozpočet skutečně držíš.

### Rozpad myšlenky

**Nejjednodušší páka je framerate** [(26:34)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=1594s), protože počet snímků v potrubí zůstává stejný a mění se jen jejich délka:

| framerate | latence při plném potrubí |
|---|---|
| 30 FPS | ~200 ms |
| 60 FPS | ~100 ms |
| 120 FPS | ~50 ms |

Autorův komentář k tomu je nejlepší věta přednášky: *„říkal jsem, že je to jednoduché. Neříkal jsem, že je to snadné."*

**Odolnost proti záseku předvedená na číslech** [(25:47)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=1547s): jeden snímek jde o tři snímky rozpočtu přes čas — a hráč **nepřijde o nic**, protože v back bufferech je hotová práce a následující snímky se stihnou dohnat. *„Engine trochu zakoktal, ale zvládli jsme se dohnat, než si toho někdo všiml."*

**Druhá páka: přiškrtit herní vlákno** [(27:20)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=1640s). Nejde o to dělat méně práce, ale **začít ji později** — ideálně tak, aby GPU dokončilo renderování právě před VSyncem. To je teoreticky nejnižší latence, jakou v Unrealu dostaneš. Prakticky:

- **`r.GTSyncType 2`** spustí herní vlákno v pevném čase před VSyncem. Výchozí odstup jsou dva snímky, k tomu **sync slack** (výchozích 10 ms, maximum jeden snímek), takže se dá ladit mezi dvěma a třemi snímky. Výsledek: **konzistentní delta time, minimální latence, žádná odolnost proti záseku.** Podporované na PS4/5, Xbox One/Series a Switch 1/2.
- **Proč jen na konzolích:** musíš znát rozpočet, a ten se na PC a mobilu nedá spolehlivě určit. *„Sám si rozhoduješ rozpočet snímku a musíš ho držet."* Přeteče-li o kousek, **spadl ti snímek**.
- **Na PC** to za tebe adaptivně dělá **Nvidia Reflex, AMD Anti-Lag 2 a Intel XeLL**. Poctivá poznámka k tomu: *„je to trochu bolehlav implementovat tři SDK jen proto, aby hra měla nejnižší latenci na PC — ale uživatelé vás za to budou milovat."*

**Třetí páka: kratší potrubí** [(31:58)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=1918s), když chceš část odolnosti zachovat. `r.OneFrameThreadLag 0` znamená, že herní vlákno musí počkat na dokončení render vlákna téhož snímku — méně latence, méně paralelismu. Upozornění, které se snadno přehlédne: **tím fakticky ztrácíš celé jádro**, protože ta dvě vlákna už nikdy neběží zároveň. Ještě kratší je `r.GTSyncType 1` (čeká se na RHI vlákno předchozího snímku místo dvou zpět).

**A trik, který autor uvedl a rovnou odmítl** [(30:26)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=1826s): `t.MaxFPS` nastavené **mírně pod** obnovovací frekvenci monitoru (58 na 60Hz) potrubí vyhladoví, takže latence spadne na minimum. Cena: **jeden až dva zahozené snímky každou sekundu.** *„Je to spíš obchvat než řešení. Velmi neprofesionální. Nedělejte to."* Zmiňuje ho proto, že to esportoví hráči už dělají sami — někdy i modem, který jim CVar vstříkne do hry.

**A protiváha na konec** [(34:30)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=2070s): autor sám říká, že žádná z těch možností není dobrá — *„není to hezké, nemělo by to být takhle složité"* — a že Epic na frame pacingu pracuje: nový adaptivní model s nastavitelným **target slackem**, který má dát nejnižší latenci **i** maximální paralelismus **i** konzistentní delta time, a to na všech platformách.

**Bonus: co `stat unit` doopravdy měří** [(37:38)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=2258s), protože bez toho se ta čísla čtou špatně:

- **Frame** — wall clock mezi starty dvou snímků **herního vlákna**. Nikoli „jak dlouho trval celý snímek".
- **Game** — totéž minus doba nečinnosti.
- **Draw** — totéž pro render vlákno; **`Present` je součástí nečinnosti**.
- **GPU** — jen čas, kdy GPU **skutečně pracovalo**; bubliny se nepočítají. Proto může být rozdíl mezi začátkem a koncem GPU snímku větší než uvedené číslo.
- **Input** — ne to, co si většina lidí myslí: je to čas **od navzorkování vstupu na začátku herního snímku po flip back bufferu**. Ne hardware, ne operační systém, ne kompozitor, ne kabel, ne odezva monitoru.
- A dvě věci navrch: čísla **nepatří k jednomu snímku** (je to poslední hodnota z každé fáze, které mohou být na různých snímcích) a jsou **vyhlazená** exponenciálním klouzavým průměrem.

> **Pozn.:** Tady je nejcennější to, co ta myšlenka **odmítá**: neexistuje nastavení, které by bylo správné pro každou hru. Kompetitivní střílečka chce latenci a rezervu neřeší, protože musí držet rozpočet tak jako tak; pomalá hra na slabším hardwaru vydělá na tom, když zásek nikdo nepozná. **Je to designové rozhodnutí maskované jako technické nastavení** — a proto patří do rozpočtu hned na začátku, spolu s [volbou cílového framerate](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1). Za pozornost stojí i to, jak autor zachází s trikem `t.MaxFPS 58`: pojmenuje ho, odmítne ho a **stejně ho vysvětlí**, protože hráči ho používají. To je poctivější než ho zamlčet — a je to připomínka, že hranice mezi „optimalizací" a „obchvatem" je v tom, jestli řešíš příčinu, nebo si kupuješ jeden efekt cenou, o které se nemluví.

**Souvislosti:** [Snímek není fronta](#snimek-neni-fronta-je-to-potrubi) · [Jitter](#jitter-nespadne-ani-jeden-snimek-a-presto-to-skube) *(co zbyde, když zásek pohltíš)* · [Jak to vidí hráč](#jak-to-vidi-hrac-360p-upscaling-a-stutter) · [Rozpočet snímku: prvních 16,66 ms](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Textury a DLSS: DLSS 4.5](textury-a-dlss.md#dlss-45-vic-snimku-mene-latence-a-mip-bias) · [Rejstřík: Input latency](../rejstrik.md#input-latency) · [Rejstřík: Hitch resiliency](../rejstrik.md#hitch-resiliency)

---

## Jitter: nespadne ani jeden snímek, a přesto to škube

**Zdroj:** [A Frame's Life: Frame Timing, Synchronization, and Latency in UE](https://www.youtube.com/watch?v=dKSHw_8vz3I) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~53 min, Unreal Fest Chicago 2026

**Shrnutí:** Odolnost proti záseku má tichou cenu, o které se v přednáškách o výkonu skoro nemluví. Pohltí-li potrubí zásek, **hráč nepřijde o žádný snímek** — ale delta time se přitom rozhoupe, a animace i kamera se rozjedou a zpomalí. Autor tomu říká **jitter** (jinde mikro-stutter nebo animation error) a předvádí ho na měřicím přístroji, který si na to postavil. Háček: v běžné hře se to nedá spolehlivě spatřit, což je přesně důvod, proč se to neopravuje.

### Rozpad myšlenky

**Odkud se jitter bere** [(43:02)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=2582s): delta time, se kterým se simuluje fyzika, animace, částice a pohyb kamery, je **frame time předchozího snímku**. Zobrazované snímky ale jdou v pevném rytmu VSyncu. Když se ta dvě čísla rozejdou, kamera se posune víc, než odpovídá tomu, co hráč uvidí — a je to vidět jako škubání.

**Anatomie záseku má tři fáze** [(43:50)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=2630s), a třetí je ta, o které se nemluví:

1. **Zahozené snímky** — poslední snímek zůstane na obrazovce delší dobu; vypadá to, že hra zamrzla.
2. **Dohánění** — příští snímek dostane velký delta time (rovný frame time posledního snímku), takže se simulace zrychlí. Vypadá to, jako by hra běžela, i když byla obrazovka zamrzlá. **Tuhle fázi chceme**, protože srovná herní čas s časově vázanými systémy jako audio.
3. **Doplnění potrubí** — potrubí je prázdné, takže následující snímky nemá co brzdit a jsou **kratší**, tedy s krátkými delta timy.

A pointa: **jitter vzniká z fází 2 a 3, i když fáze 1 vůbec nenastane.** Zásek se pohltil, snímky nespadly — a delta time se přesto rozhoupal.

**Měřicí přístroj** [(45:24)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=2724s) je nejlepší nápad celé přednášky, a vznikl z autorovy vlastní nedůvěry: viděl analýzy, které jitter „předvádějí" na škubající animaci nebo kameře, a přiznává, že tam nic neviděl — *„možná jsem starý, nebo je to komprese videa."* Takže si postavil **kolo rozdělené na 60 dílů, které se otočí právě jednou za sekundu**. Při 60 FPS se každý snímek posune o jednu šedesátinu, takže **všechny čáry mají být pořád zarovnané**. Nejsou-li, vidíš jitter. Na záznamu s 90ms záseky nespadl jediný snímek a ve zpomalení je zarovnání vidět, jak se rozjede a dorovná.

**A dvě věci, které se nedají spravit „prostě fixním delta timem"** [(47:45)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=2865s):

- **Variabilní obnovovací frekvence** znamená, že rytmus displeje pevný není.
- **Monitory nemají celá čísla.** Autorův pracovní monitor běží na **59,95 Hz** — a z databáze skoro sta tisíc modelů má **méně než třetina** celočíselnou nativní frekvenci. Unreal navíc vrací obnovovací frekvenci jako `int`, takže na dotaz odpoví „60". Praktický důsledek: *„můj monitor by odchýlil herní čas o půl sekundy každých deset minut."*
- A třetí důvod, který přednáška zmiňuje jen krátce a stojí za doplnění: **audio se nezastaví.** Zasekne-li se obraz a delta time nedohání, obraz a zvuk se rozejdou.

**Náplast, ne řešení** [(48:32)](https://www.youtube.com/watch?v=dKSHw_8vz3I&t=2912s): autor napsal plugin **Delta Time Smoother** (volně na GitHubu) se třemi režimy — **absorpce** pro malé zásky (dluh z dlouhého delta timu splatí až následující krátké, takže průběh zůstane plochý; na jeho kole to 90ms zásek úplně vyhladí), **mitigace** pro středně velké (okamžitě zprůměruje frontu delta timů — pár snímků spadne, ale nenásleduje trhavé dohánění) a **průchod** pro velké zásky, kde by průměrování rozjelo hru komicky rychle. A rovnou přiznává, proč to není v enginu: *„je to jen dočasná náplast, dokud nedostaneme nový frame pacing."*

> **Pozn.:** Tahle myšlenka je v knihovně kvůli metodě, ne kvůli pluginu. **Autor měl jev, který nedokázal spolehlivě vidět, a postavil si přístroj, který z něj udělá jednoznačné čtení.** Kolo se 60 díly je totéž, co dělá [reprodukovatelný test v Profilingu](profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic) — vyrobit podmínky, ve kterých má měření jedinou možnou interpretaci. A stojí za pozornost, že to vzniklo z **přiznané nejistoty**: „nevidím to, o čem všichni mluví" je legitimní východisko a vede k lepšímu nástroji než tvrzení, že to tam určitě je. Druhá věc, kterou si odsud bereme: **plynulost není jen počet snímků.** Hra může doručit každý snímek a přesto působit rozbitě — takže „nespadl žádný snímek" není důkaz, že je frame pacing v pořádku.

**Souvislosti:** [Latence proti odolnosti](#latence-proti-odolnosti-co-za-co-menis) *(odkud ta rezerva je)* · [Snímek není fronta](#snimek-neni-fronta-je-to-potrubi) · [Jak to vidí hráč](#jak-to-vidi-hrac-360p-upscaling-a-stutter) · [Profiling: reprodukovatelný test](profiling.md#reprodukovatelny-test-bez-nej-neporovnas-nic) · [Rejstřík: Jitter](../rejstrik.md#jitter) · [Rejstřík: Delta time](../rejstrik.md#delta-time)

---

## Jak to vidí hráč: 360p, upscaling a stutter

**Zdroj:** ["Optimized for 360p" ... huh?](https://www.youtube.com/watch?v=zT8DZsdJ72Y) · [Vex](https://www.youtube.com/channel/UChRFo9vcnuwvcz0DWTEaBNw) · ~18 min, hardwarová analýza · + [A Frame's Life](https://www.youtube.com/watch?v=dKSHw_8vz3I) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · části o měření

**Shrnutí:** Přednášející z Epicu to řekne přímo: *„my jako vývojáři vidíme všechna ta čísla. Hráči nevidí ani jedno. Vidí jen, kolik VSynců hra za sekundu stihla."* Tahle myšlenka je pohled z druhé strany — technická analýza jedné UE5 hry od někoho, kdo měří na hráčském hardwaru. A je poučná tím, jak se rozchází to, co hráči vytýkají, s tím, co hru skutečně bolí: **dynamické rozlišení a upscaling nejsou přiznání porážky, ale stutter z kompilace shaderů je skutečná vada.** Háček: rozeznat to od sebe se z reklamací nedá.

### Rozpad myšlenky

**Odkud je ta reakce** [(0:02)](https://www.youtube.com/watch?v=zT8DZsdJ72Y&t=2s): u hry se objevilo, že se v performance režimu upscaluje **z až 360p** na 1800p. *„To zní jako šílenost."* Autor si k tomu ale rovnou dodá, co to znamená technicky: je to **dynamické** — hra jde s rozlišením dolů tam, kde je náročná, aby udržela 60 FPS. Přesně tak, jak je popsaný [rozlišovací žebřík v device profilech](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1).

**Test místo dohadů** [(3:08)](https://www.youtube.com/watch?v=zT8DZsdJ72Y&t=188s) je na téhle analýze to nejcennější: analýzy si protiřečily (jeden zdroj tvrdil 360p, jiný ~1080p), takže autor **simuloval konzoli na PC** — GPU odpovídající PS5 (RX 6700) a srovnatelný procesor. Výsledek popírá první dojem: hra běží **nad 60 FPS na vysokých detailech** s Lumenem a Nanitem, a autor to hodnotí jako *„velmi rozumný výkon na tenhle typ hry."* A pak dodá kalibraci, která hodně vysvětluje: *„myslíte-li si, že je vaše PS5 super rychlá, asi se mýlíte — RX 6700 dneska není rychlá grafika."*

**Skutečná vada je jinde a je to CPU** [(4:41)](https://www.youtube.com/watch?v=zT8DZsdJ72Y&t=281s). Zásky přicházejí z **kompilace shaderů za běhu**: přípravný krok při spuštění nepokryje všechno, takže se zbytek kompiluje během hry — a kompilaci obstarává **procesor**. Odtud dva důsledky, které stojí za zapamatování:

- **Proč to konzole nemají tak zlé:** hardware je stejný ve všech kusech, takže se dá zkompilovat jednou a nahrát předpřipravené. Na PC to nelze.
- **Rychlý procesor to nevyřeší.** Autor to viděl i na high-endové sestavě — což ukazuje, že jde o **chybějící přípravu**, ne o nedostatek výkonu.

Tady se ta myšlenka potkává s tím, co má na seznamu i Epicova přednáška o startu na 60 FPS: **PSO se musí buď zabalit, nebo předpřipravit — nebo obojí**, a při testování je potřeba mazat cache, aby bylo poznat, že s tím je problém.

**A jedna anomálie, která ilustruje, proč se má měřit** [(10:09)](https://www.youtube.com/watch?v=zT8DZsdJ72Y&t=609s): v té hře je **TSR pomalejší než nativní rozlišení** — upscaler, který má výkon získat, ho bral. *„Proč je to horší? Nechápu to."* Praktické čtení téhle poznámky: **upscaler není automaticky úspora.** Zapnul-li ses ho a nezměřil, můžeš platit za funkci, která ti nic nedala.

**Design jako optimalizace** [(16:20)](https://www.youtube.com/watch?v=zT8DZsdJ72Y&t=980s) je závěr, ke kterému autor dojde sám a je z celého videa nejpřenositelnější: hra podle něj běží dobře taky proto, že **využila svůj vlastní žánr** — mlha, kterou série má v DNA, schová dálku a ubere práci, a levely jsou **sevřené místo rozlehlých**. Srovnává to s otevřenou UE5 hrou, která běží podstatně horší. *„Mlha je vestavěný optimalizační trik, když se použije správně."* A rovnou dodá druhou polovinu rovnice: **u rychlé střílečky snímky rozhodují o hratelnosti, u pomalé hororové hry stačí 60** — takže i cíl je věcí žánru.

> **Pozn.:** Tuhle myšlenku bereme jako **korekci vývojářské perspektivy**. Hráč nemá `stat unit`; má dojem — a dojem se skládá z jiných věcí, než jaké se objevují v profileru. Konkrétně: **jeden dvousekundový zásek na začátku úrovně zničí dojem víc než trvale nižší rozlišení**, protože rozlišení si oko srovná a zásek se pamatuje. Z toho plyne praktická priorita: **frame pacing a kompilace shaderů před posledními procenty vizuální kvality.** A jedna vlastní výhrada k té „mlze jako optimalizaci": funguje to jen tehdy, když je součástí zamýšleného vzhledu. Mlha nasazená kvůli výkonu na hru, která ji nechce, není optimalizace, ale ústupek — a je to táž volba jako u [scope](../teorie/scope.md#design-by-constraint-krabice-napred-napad-dovnitr): **omezení, které si vezmeš dopředu, je nástroj; omezení, které tě dohoní, je škoda.**

**Souvislosti:** [Latence proti odolnosti](#latence-proti-odolnosti-co-za-co-menis) · [Jitter](#jitter-nespadne-ani-jeden-snimek-a-presto-to-skube) · [Rozpočet snímku: prvních 16,66 ms](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) *(odkud ten rozlišovací žebřík je)* · [Textury a DLSS](textury-a-dlss.md#dlss-45-vic-snimku-mene-latence-a-mip-bias) · [Design by constraint](../teorie/scope.md#design-by-constraint-krabice-napred-napad-dovnitr) · [Rejstřík: PSO](../rejstrik.md#pso) · [Rejstřík: TSR](../rejstrik.md#tsr) · [Rejstřík: Dynamic resolution](../rejstrik.md#dynamic-resolution)
