# Osvětlení: fyzikální základ, mlha a nálady

Světlo od řemesla k náladě: **PBL workflow** (svítit podle skutečných hodnot v luxech a měřit to přímo v enginu), volumetrická **mlha Silent Hill 2** jako materiál, hororová atmosféra vrstvená jako ve filmové postprodukci, noční scéna z default setupu a hrst rychlých triků. Kompoziční základ („nejdřív tvary, pak settingy") pokládá [kapitola Stavba prostředí](env-tvorba.md#nejdriv-tvary-design-language-a-chiaroscuro); fyzikální světlo v praxi lesa ukazuje [lesní pěšina](env-tvorba.md#lesni-pesina-ii-decaly-svetlo-a-render).

---

## PBL: svítit podle skutečných hodnot

**Zdroj:** [Realistic and Physical Lighting in UE5: The PBL Workflow](https://www.youtube.com/watch?v=GsE0mDtxtiQ) · [arthur tasquin](https://www.youtube.com/channel/UCLvtgS-XncZAsNv7ofOWrDg) · ~29 min, výklad + studie

**Shrnutí:** Physically based lighting = kalibrovat světla podle **naměřených hodnot ze skutečného světa** (zářivka 2000 lm, slunce 120 000 luxů, obchod 500 luxů) a kontrolovat výsledek **light metery přímo v enginu** [(2:56)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=176s) [(4:34)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=274s). A stejně důležité: vědět, kde Unreal fyziku jen aproximuje — a kdy pravidla vědomě porušit [(27:03)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=1623s).

### Rozpad myšlenky

**Setup a měřáky:** povinná je volba **Extend Default Luminance Range** (v nových verzích zapnutá a zamčená — ale po migraci projektu zkontroluj DefaultEngine.ini) a hodí se přepnout default jednotku lokálních světel na **lumeny** [(3:46)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=226s). Hlavní nástroj je **HDR (Eye Adaptation) viewmode** se dvěma měřáky: **illuminance meter** měří světlo *dopadající* na povrch (luxy), **luminance meter** světlo *vyzařované* (cd/m²) — rozdíl, na kterém stojí celý workflow [(4:34)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=274s) [(4:55)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=295s). Data přicházejí vždy jako **rozsahy** s „důkazem měření" (fotka/video místa) — kontext hodnoty je půlka informace [(2:06)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=126s).

**Studie konbini (interiér):** zářivky = bodovky se source radius/length podle tvaru trubice, zabalené s meshem do blueprintu [(5:44)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=344s); intenzita z tabulek (zářivky 500–5000 lm, průměr 2000) [(6:50)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=410s). Expozice: rada „nastav MinEV/MaxEV na 1" je past — **EV100 = 1 odpovídá modré hodině**; interiér patří mezi **EV100 5–7** [(7:36)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=456s). Kontrola celku: obchody mívají 80–1600 luxů — šedá koule + illuminance meter ukázaly 1550, takže ubrat světla, zbytek na poloviční intenzitu (reference měla jednu trubici, scéna dvě) → 550 luxů a sedí to [(8:24)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=504s) [(9:13)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=553s).

**Kde aproximace skřípou:** jas zdroje a jeho dopad na scénu jsou v Unrealu **dvě různé věci** (v realitě jedna) — a Lumen k tomu nechá každý emissive materiál svítit bez kontroly; emissive se proto validuje luminance meterem a u „žárovek s vláknem" fyzikální hodnoty radši vzdej [(10:39)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=639s) [(11:28)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=688s). Slunce vs. obloha: luxmetr venku měří slunce *po průchodu atmosférou* plus celou oblohu — jediný systém, který to emuluje, je **Sky Atmosphere**: directional pak patří **120 000 luxů (solární konstanta)** a nesahat [(12:14)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=734s). Autor přesto raději **HDRI workflow** — Sky Atmosphere mu bere kontrolu nad barvou a intenzitou oblohy; přiznaně méně přesné, ale krásnější [(13:01)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=781s).

**Tři vzory ze studií (Tokyo Back Alleys):** *(1)* exponuj pro záměr — vypočtená EV 13 byla „správně", ale slunce mělo hřát, takže **EV 10** [(15:35)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=935s) [(16:24)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=984s); *(2)* HDRI s metadaty (locationtextures.com) + timeanddate.com = přesná pozice slunce; intenzita oblohy se kalibruje luminance meterem proti hodnotě „bíle osvětlený mrak", a **dočasná Sky Atmosphere poslouží jen k zaměření slunce** — pak smazat [(17:14)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=1034s) [(19:35)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=1175s); *(3)* bez HDRI Backdropu (zlobí s Pathtracerem/Sequencerem) poslouží **Sphere_inversenormals** z Engine contentu, scale 15 000, Unlit materiál s **isSky** checkboxem — a skylight po každé změně **recapture** [(20:22)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=1222s) [(21:09)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=1269s). Bonus obráceně: z vlastní RAW fotky přečti metadata (čas, clonu, rychlost), převeď na EV100 (~13) nebo nech expozici řídit **Metering Mode = Manual** přes camera sekci — a dosvětluj, dokud se render nekryje s fotkou [(24:42)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=1482s) [(25:58)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=1558s).

> **Pozn.:** Klíčová věta na závěr: **fyzikálně přesné ≠ vizuálně krásné — je to technicky správný základ, od kterého se kreativně odráží** [(27:03)](https://www.youtube.com/watch?v=GsE0mDtxtiQ&t=1623s). Video staví na autorově placeném pluginu PBL Database (přiznaně; metoda funguje i bez něj — free datové sady linkuje) a učí hlavně návyk: foť, měř levným luxmetrem, srovnávej. Přesně tenhle přístup používá [lesní pěšina](env-tvorba.md#lesni-pesina-ii-decaly-svetlo-a-render) (120 000 luxů + zamčená EV100 10).

**Souvislosti:** [Stavba prostředí: lesní pěšina II](env-tvorba.md#lesni-pesina-ii-decaly-svetlo-a-render) · [Rejstřík: EV100](../rejstrik.md#ev100) · [Rejstřík: HDRI](../rejstrik.md#hdri)

---

## Mlha ze Silent Hill 2: volumetrický materiál kolem postavy

**Zdroj:** [Recreating Silent Hill 2 Fog in Unreal Engine 5](https://www.youtube.com/watch?v=96sheL5UqJQ) · [Dallas Drapeau](https://www.youtube.com/channel/UCatEMsDp-qF_bix_1ST2llw) · ~36 min, tutoriál

**Shrnutí:** Ikonická mlha za půl hodiny a s výmluvnou architekturou: žádný celosvětový objem, ale **krychle připnutá k postavě** (jako déšť a sníh) s materiálem domain **Volume** — zeď mlhy v dálce, plíživé chapadla po zdech přes **mesh distance fields**, self-shadowing a dva CVary na kvalitu [(3:58)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=238s) [(6:09)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=369s).

### Rozpad myšlenky

**Rozbor před stavbou:** efekt má dvě složky — zeď mlhy houstnoucí se vzdáleností od postavy a „natahující se" mlhu, která obtéká geometrii [(2:22)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=142s). Prerekvizity: mesh distance fields v project settings (vizualizace přes viewmode) a **volumetric fog zapnutý na Exponential Height Fog** — bez něj volume materiál nekreslí [(6:09)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=369s) [(7:07)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=427s).

**Zeď mlhy:** World Position × malé číslo (0,0008 — nebo /1000 a pracovat s „8") + Time = posun → vestavěný **Noise** uzel × intenzita, dvě vrstvy šumu (velká + střední), **Saturate** [(7:58)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=478s) [(10:08)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=608s). Odkrytí okolí postavy: **Camera Position → Distance → Subtract (start 3500) → Divide (falloff)** — autorova mantra „kdykoli potřebuješ falloff, je to subtract do divide" [(12:47)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=767s) [(14:22)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=862s). Volitelný strop: Z − ceiling → falloff → invert (1-x) — mlha se umí rozestoupit nebo pustit oblohu [(15:56)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=956s).

**Plíživá mlha:** uzel **Distance to Nearest Surface** („cokoli má obtékat objekty = mesh distance fields") → subtract → poctivě přiznaný lerp trik („nevím proč, ale vypadá to líp") → dělení scale + Time s **negativní rychlostí = mlha leze vzhůru** po zdech → noise → opacity; druhý camera fade ji drží blíž (1500) než zeď (3500) [(18:35)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=1115s) [(20:12)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=1212s) [(22:55)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=1375s).

**Hloubka a spojení:** **self-shadowing** (shadow density ~0,5) dodá mlze kontakt a objem [(23:44)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=1424s); stín se fake-uje přes **Sky Atmosphere Light Direction** × trace distance do **Exponential Density** uzlu [(26:46)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=1606s). A finální lekce: vrstvy se nespojily přes multiply/add, ale **lerpem s alphou = Pixel Depth / blend distance** — „trvalo mi to déle, než rád přiznávám" [(30:39)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=1839s) [(31:27)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=1887s). Kvalita volumetriky: **`r.VolumetricFog.GridPixelSize`** (default 8, pro cinematiku 4) a **`r.VolumetricFog.GridSizeZ`** (128 → 256/512, ten dražší) [(32:43)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=1963s) [(33:56)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=2036s).

> **Pozn.:** Úvodní monolog stojí za kapitolu sám o sobě: „nestačí být dobrý, musíš být i rychlý" — nejjednodušší cesta k efektu, žádné uber-shadery s milionem parametrů, napřed rozbor, pak stavba [(0:49)](https://www.youtube.com/watch?v=96sheL5UqJQ&t=49s). A herně-designová vazba: mlha Silent Hill je učebnicová **percepční hranice** — týž nástroj, který [Prostor a hranice](../teorie/prostor-a-hranice.md) popisuje jako měkkou hranici mapy (a mimochodem v SH2 původně krytí dohledové vzdálenosti PS1).

**Souvislosti:** [Teorie: prostor a hranice](../teorie/prostor-a-hranice.md) · [Hororová atmosféra](#horor-ve-vrstvach-od-hdri-po-svetelnou-navigaci) · [Rejstřík: volumetric fog](../rejstrik.md#volumetric-fog) · [Rejstřík: mesh distance field](../rejstrik.md#mesh-distance-field)

---

## Horor ve vrstvách: od HDRI po světelnou navigaci

**Zdroj:** [Create a horror lighting in Unreal Engine.](https://www.youtube.com/watch?v=0w3SBb5ktlg) · [Karim aboushousha](https://www.youtube.com/channel/UCD0eeSf6p2nQ7msJfO06FTA) · ~16 min, tutoriál

**Shrnutí:** Senior lighting artist staví hororovou náladu z reference — po vrstvách jako ve filmu: HDRI základ, mlha („to, co dělá horor"), slunce s god rays, a nakonec grading, který z „raw záběru" udělá mood [(1:12)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=72s) [(4:07)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=247s) [(7:57)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=477s). Bonusem nejlepší formulace **světelné navigace** v celé sbírce.

### Rozpad myšlenky

**Vrstva 1 — HDRI:** backdrop z Poly Haven, zvětšit, zapustit pod zem — a **skylight čte tutéž HDRI**, aby indirect sedělo s oblohou (intenzita ~3) [(1:12)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=72s) [(1:59)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=119s). Expozice zamčená (1/1), pak ztmavit na 0,1 — obloha zůstane světlá a scéna potemní; vignette venku max 0,2 [(2:48)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=168s) [(3:19)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=199s).

**Vrstva 2 — mlha:** exponential + volumetric (0,2), do šeda, height falloff tak, aby obloha zůstala vidět — v tu chvíli scéna „začne být horor" [(4:07)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=247s) [(4:55)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=295s).

**Vrstva 3 — slunce:** analýza reference říká, že tam je (světlé místo v mracích) — directional ~4 s **light shafts** ~1; větší **source angle = měkčí stíny** [(4:55)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=295s) [(5:41)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=341s) [(7:57)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=477s). Občas ale nechat stíny ostré — hororu sluší tvrdost [(10:43)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=643s).

**Vrstva 4 — grading:** „film se točí v neutrálním světle a mood vzniká v postprodukci" — midtones gamma do modrozelena, globální gamma/kontrast ~0,7, kontrastem hnědavý nádech; local exposure (v auto-titulcích komicky „local fog") ~0,55 vytáhne informaci z tmavých ploch [(7:57)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=477s) [(8:45)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=525s) [(9:49)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=589s).

**Světelná navigace:** jediný spotlight na dům v dálce — a oko tam jde samo: „Proč tam svítí? Musím se jít podívat." Míň je víc; jedno vedené světlo naviguje líp než deset dekorativních [(14:08)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=848s) [(15:13)](https://www.youtube.com/watch?v=0w3SBb5ktlg&t=913s).

> **Pozn.:** Struktura vrstev (HDRI+skylight → mlha → slunce → grading) je tatáž kostra jako [temný les](env-tvorba.md#temny-les-za-odpoledne-hdri-mlha-a-grading) a [noční scéna níž](#nocni-scena-z-defaultniho-setupu) — tři nálady, jeden checklist. Světelná navigace je praktické dvojče [vedení hráče](../teorie/vedeni-hrace.md): světlo je nejsilnější šipka, kterou máš.

**Souvislosti:** [Teorie: vedení hráče](../teorie/vedeni-hrace.md) · [Stavba prostředí: temný les](env-tvorba.md#temny-les-za-odpoledne-hdri-mlha-a-grading) · [Rejstřík: HDRI](../rejstrik.md#hdri) · [Rejstřík: silueta](../rejstrik.md#silueta)

---

## Noční scéna z defaultního setupu

**Zdroj:** [How to make a simple night scene in Unreal Engine 5](https://www.youtube.com/watch?v=YHhRTjD_P2A) · [UE5 Poseidon](https://www.youtube.com/channel/UCqPZeIa_lU0ML7JG7D_FP5Q) · ~8 min, tutoriál

**Shrnutí:** Hratelná noc bez jediného nového aktoru — jen přeladěním defaultní open world mapy: **slunce se stane měsícem**, mlha a skylight zmodrají a zamčená expozice prodá tmu [(0:20)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=20s) [(1:00)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=60s).

### Rozpad myšlenky

**Měsíc:** directional light otočit k „západu", ale nechat viditelný; **source angle = velikost kotouče**; use temperature a teplotu **zvýšit** (chladnější, modřejší) + lehce modrá barva; intenzita ~1 [(1:00)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=60s) [(1:56)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=116s) [(2:43)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=163s). Light shaft bloom ubrat a přibarvit (scale = poloměr záře, max brightness = síla) [(1:56)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=116s).

**Atmosféra:** fog density nahoru (0,05 — noc snese víc), height falloff ~0,1; trik k zapamatování — **barvu mlhy nabrat kapátkem přímo z oblohy**, splyne dokonale [(2:43)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=163s) [(3:30)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=210s). Volumetric fog: míň scattering distribution, modré albedo, extinction scale dolů [(3:39)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=219s); sky atmosphere height ~5, skylight scale ~2 do modra [(4:10)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=250s).

**Expozice a barva:** post-process volume unbound, **min = max EV100** (vyšší číslo = tmavší; tady −0,5) — bez zámku auto-exposure noc „prosvětlí" zpátky [(4:57)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=297s). Když scéna působí bezbarvě, přitlačit modrou přímo v directional lightu [(5:41)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=341s). Varianta **bez měsíce**: directional otočit z dohledu, bloom pryč, tmu dorovnat skylightem, volumetric clouds schovat [(6:32)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=392s) [(7:12)](https://www.youtube.com/watch?v=YHhRTjD_P2A&t=432s).

> **Pozn.:** Z pohledu [PBL](#pbl-svitit-podle-skutecnych-hodnot) je tohle „artistická" cesta — žádné luxy, jen oko a reference. Obě jsou legitimní: fyzikální základ se hodí, když scéna má víc světel a musí držet pohromadě; přeladění defaultu stačí na náladu jedné mapy. Hratelnou tmu řeš vždy testem: vidí hráč kudy jít?

**Souvislosti:** [PBL workflow](#pbl-svitit-podle-skutecnych-hodnot) · [Horor ve vrstvách](#horor-ve-vrstvach-od-hdri-po-svetelnou-navigaci) · [Rejstřík: EV100](../rejstrik.md#ev100) · [Rejstřík: volumetric fog](../rejstrik.md#volumetric-fog)

---

## Drobky: tři triky a světlo ve 2D

**Zdroj:** [UE5 Lighting Tricks You Need to Know](https://www.youtube.com/watch?v=9PFrFDjVXHM) · [Sergey Maryshev](https://www.youtube.com/channel/UCVAdTnZgQ40jpKzC0-_RPAQ) · short · + [Game Dev Secrets: How does light work?](https://www.youtube.com/watch?v=rzm8v5gx7l0) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · short

**Shrnutí:** Dva shorty, čtyři nápady: **light shaft bloom** pro prach v paprscích, **IES textury** pro tvar skutečných lamp, **light function** pro stíny mraků — a normal mapy, které rozsvítí i 2D sprite [(0:00)](https://www.youtube.com/watch?v=9PFrFDjVXHM&t=0s) [(0:02)](https://www.youtube.com/watch?v=rzm8v5gx7l0&t=2s).

### Rozpad myšlenky

**Tři triky (Maryshev):** *(1)* na directional lightu **Light Shaft Bloom** — záře a prach v paprscích, když slunce cloní objekt; *(2)* **IES textury** v nastavení lokálního světla — fotometrický profil skutečné lampy místo nudné koule; *(3)* **Light Function** — materiál (třeba noise) zapojený do slotu directional lightu = putující stíny mraků, vysoce optimalizované [(0:00)](https://www.youtube.com/watch?v=9PFrFDjVXHM&t=0s).

**Světlo ve 2D (Inbound Shovel):** lampa svítící na sprite vypadá jako plochý barevný overlay — protože jím je. Fix: **normal mapa vygenerovaná ke sprite sheetu** — barvy kódují směry (zelená nahoru, růžová doprava, modrá doleva) a engine pak světlo zprava odráží na „pravých" pixelech postavy; smíchané se spritem působí světlo náhle trojrozměrně [(0:02)](https://www.youtube.com/watch?v=rzm8v5gx7l0&t=2s) [(0:48)](https://www.youtube.com/watch?v=rzm8v5gx7l0&t=48s).

> **Pozn.:** Light shaft bloom už jednou posloužil [měsíci v noční scéně](#nocni-scena-z-defaultniho-setupu) a IES profily jsou přirozený upgrade [PBL přístupu](#pbl-svitit-podle-skutecnych-hodnot) (skutečná lampa = skutečný tvar světla). 2D lekce má obecnou pointu: světlo potřebuje informaci o směru povrchu — kde chybí geometrie, dodá ji textura.

**Souvislosti:** [Noční scéna](#nocni-scena-z-defaultniho-setupu) · [PBL workflow](#pbl-svitit-podle-skutecnych-hodnot) · [Rejstřík: silueta](../rejstrik.md#silueta)
