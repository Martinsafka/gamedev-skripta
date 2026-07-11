# Textury a DLSS: paměť a rozlišení

Druhá půlka výkonu je paměť a obraz: **right-sizing textur** (4K si zaslouží míň map, než si myslíš), volba architektury **unikátní textury vs. atlas vs. virtual textures** — a **DLSS 4.5** jako násobič snímků, včetně kompenzace mip biasu, bez které upscaling potichu rozmaže svět. Geometrii a scénu řeší [Optimalizace scény](optimalizace.md), produkční kontext [Breakdowny](env-breakdowny.md).

---

## Right-size: ne všechno si zaslouží 4K

**Zdroj:** [Stop Shipping 4K Textures — Right-Size Everything in UE5](https://www.youtube.com/watch?v=WnHgLJcmhTM) · [Arghanion's Puzzlebox](https://www.youtube.com/channel/UCZCYv7mrbixDNKMMRnQj36A) · ~20 min, tutoriál

**Shrnutí:** Rozlišení textur roste **kvadraticky**: 4K v BC7 je 21 MB, 2K jen ~5 MB — čtvrtina, ne půlka [(2:25)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=145s) [(3:11)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=191s). Rozhodující otázka pro každou mapu: **jak blízko se k ní kamera dostane?** A překvapení z experimentů: base color snese drastické snížení, protože vnímaný detail nese normal mapa [(14:56)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=896s).

### Rozpad myšlenky

**Čísla:** 30 textur ve 4K = 640 MB VRAM; v 1K = 40 MB [(2:25)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=145s). Mezi 512 a 1K je vizuální rozdíl často nulový, mezi 2K a 4K obří cena za skoro nic [(7:54)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=474s) [(8:41)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=521s). BC1 (bez alfy) stojí zhruba polovinu BC7 [(4:46)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=286s). A klasika: channel packing (occlusion/roughness/displacement v RGB) — jsou to data, ne barva, sRGB vypnout [(3:58)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=238s).

**Vzdálenost rozhoduje:** first person u zdi udrží 2K, 1K už se rozpadá; ve third person kamera nikdy nepřijde tak blízko a 1K stačí v pohodě [(5:32)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=332s) [(18:05)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=1085s). Vývojáři navíc kameru hlídají — dřívější kolize, FOV, odstup — aby se k texturám blízko nedostala [(6:19)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=379s). Referenční sanity check: Crimson Desert v prozkoumaných oblastech shipuje mapy **do 1K** — s trim sheet pipeline pod tím ([tentýž breakdown](env-breakdowny.md#crimson-desert-detektivka-kolem-displacementu), který video samo cituje) [(8:41)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=521s) [(9:29)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=569s).

**Nástroje:** v texture editoru **LOD Bias** (1 = poloviční hrana, 2 = čtvrtinová…) s mip preview [(11:02)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=662s); v materiálu sampler source **Shared: Wrap** (obchází limit 16 samplerů) a **Mip Value Mode = MipBias** → bias jako parametr instance [(11:49)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=709s) [(12:36)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=756s); hromadně přes **property matrix** — LOD bias, komprese, sRGB i VT streaming pro stovky textur naráz, s copy/paste hodnot [(13:23)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=803s).

**Citlivost per mapa (experiment na cihlové zdi):** base color přežije bias 5 téměř bez povšimnutí — **normal mapa je ta, která nese dojem detailu** (bias ~2 ≈ 1K je strop), ORD/displacement snese ~3 [(14:10)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=850s) [(15:44)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=944s) [(16:31)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=991s). Šetři tedy nejdřív albedo, normálu až naposled.

> **Pozn.:** Dvě páky shaderu — instrukce a rozlišení — jsou nezávislé: snížením textur instrukce neubydou [(0:52)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=52s); orientačně do ~300 instrukcí na běžný mesh, ~500 na landscape s displacementem [(1:38)](https://www.youtube.com/watch?v=WnHgLJcmhTM&t=98s). Video vzniklo kolem autorova nástroje Surface Forge — čísla a postupy jsou ale obecné, produkt je jen kulisa. Stejnou disciplínu radí [The Ascent breakdown](env-breakdowny.md#the-ascent-ctyri-artisti-jeden-shader): 4K skoro nikdy a roughness klidně poloviční.

**Souvislosti:** [Breakdowny: Crimson Desert](env-breakdowny.md#crimson-desert-detektivka-kolem-displacementu) · [Breakdowny: The Ascent](env-breakdowny.md#the-ascent-ctyri-artisti-jeden-shader) · [Rejstřík: mip mapa](../rejstrik.md#mip-mapa) · [Rejstřík: trim sheet](../rejstrik.md#trim-sheet)

---

## Unikátní textury, atlas, nebo virtual textures?

**Zdroj:** [Virtual Textures vs Atlases: The Truth about UE5 Optimization](https://www.youtube.com/watch?v=_fUzAKlxiQg) · [Sergey Maryshev](https://www.youtube.com/channel/UCVAdTnZgQ40jpKzC0-_RPAQ) · ~8 min, srovnání

**Shrnutí:** Tři architektury texturování proti sobě v měřených testech. Unikátní textury zabíjejí **CPU** (draw cally), atlas zabíjí **VRAM** (celý skáče na max mip), virtual textures ulevují oběma — za daň v **GPU čase** (page table indirekce). Žádný vítěz; každá hodí se jinam [(6:26)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=386s).

### Rozpad myšlenky

**Unikátní textury:** každý objekt s vlastním materiálem = vlastní draw call; při desítkách objektů se CPU udusí přípravou příkazů — a výkonná grafika nepomůže, bottleneck je jinde [(0:00)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=0s) [(0:51)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=51s).

**Atlas (16× 2K → jedno 8K plátno):** draw cally klesnou **teprve po sloučení objektů do jednoho meshe** — jinak zůstane 16 slotů a nezměnilo se nic [(1:40)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=100s). Daň: mip management se zamkne — když jediný objekt (silnice pod nohama) potřebuje 8K, **celý atlas se přepne na max rozlišení**, i když zbylých 15 objektů je kilometr daleko; pár atlasů a VRAM je plná [(2:29)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=149s) [(3:16)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=196s).

**Virtual textures:** checkbox na textuře; systém ji rozseká na **stránky** a streamuje jen ty, na které se kamera dívá (v testu 200 z poolu 7 000) [(3:16)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=196s) [(4:04)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=244s). Pool je **pevná rezervace** — při přeplnění nejhůř rozmazané textury, nikdy out-of-memory; stejná filozofie jako Nanite streaming pool [(4:54)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=294s) [(5:40)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=340s). Daň: GPU čte přes **page table** — dvojitý dotaz na každý tile; na všem by se mikrosekundy sečetly, plus tabulka v paměti a větší build [(5:40)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=340s).

**Kdy co:** unikátní textury pro vzácné hero objekty; atlas pro drobnosti, které se často duplikují (a slučují); VT pro obří plochy s kritickým detailem — a klidně kombinace všech tří [(6:26)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=386s) [(7:14)](https://www.youtube.com/watch?v=_fUzAKlxiQg&t=434s).

> **Pozn.:** Trim sheet z [TLOU breakdownu](env-breakdowny.md#tlou-trim-sheet-ktery-nahradil-tisice-bake) je speciální případ atlasu (pásy místo dlaždic) a [San Francisco](env-breakdowny.md#san-francisco-11-mesto-od-jednoho-cloveka) používá VT přesně podle téhle tabulky — 4K zdroje, streamované jen kde třeba. Draw cally jako CPU bottleneck do třetice vysvětluje [„Proč jsou levely pomalé"](optimalizace.md#proc-jsou-levely-pomale-od-instanci-po-data-layers).

**Souvislosti:** [Optimalizace scény: levely](optimalizace.md#proc-jsou-levely-pomale-od-instanci-po-data-layers) · [Breakdowny: TLOU](env-breakdowny.md#tlou-trim-sheet-ktery-nahradil-tisice-bake) · [Rejstřík: virtual texture](../rejstrik.md#virtual-texture) · [Rejstřík: draw call](../rejstrik.md#draw-call)

---

## DLSS 4.5: víc snímků, méně latence — a mip bias

**Zdroj:** [DLSS 4.5 Setup Guide for UE 5.7 Projects](https://www.youtube.com/watch?v=y80hX4IlzmI) · [DK 3D](https://www.youtube.com/channel/UC3fGhbgSpR2BSSeTls3R6Sg) · ~25 min, tutoriál

**Shrnutí:** DLSS 4.5 v demu: ze 47 na 100 FPS, latence z ~27 na 20 ms a k tomu stabilnější obraz než default anti-aliasing [(0:32)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=32s) [(1:21)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=81s). Setup je snadný — a video přidává krok, který většina návodů vynechá: **kompenzaci mip a LOD biasu**, protože engine při nižším interním rozlišení potichu sníží kvalitu textur i Nanite geometrie [(16:00)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=960s).

### Rozpad myšlenky

**Instalace:** plugin z NVIDIA developer webu → devět složek nakopírovat do **Plugins složky enginu** (podpora 5.5–5.7) → v editoru zapnout potřebné pluginy (vše krom movie render queue supportu, pokud jde o hru) a restart [(3:44)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=224s) [(5:20)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=320s).

**Zapnutí v blueprintu:** **Query DLSS-SR Support** → porovnat s enum Supported → branch [(7:42)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=462s); **Get Supported DLSS-SR Modes** vrátí pole režimů dané karty (ultra performance … quality, DLAA) [(11:39)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=699s); **Set DLSS-SR Mode** pak nastaví režim a s ním screen percentage — quality renderuje na 66 %, ultra performance na 33 % nativního rozlišení [(10:06)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=606s) [(14:26)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=866s). Past: checkbox **DLAA enabled** přebije zvolený režim — dostaneš jen lepší anti-aliasing bez výkonu [(10:52)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=652s).

**Kompenzace kvality:** při 66/33 % interního rozlišení engine sám sáhne po hrubších miplevelech textur a hrubší Nanite geometrii (názorné demo přes `r.Nanite.ViewMeshLODBias.Offset 10` a `r.ViewTextureMipBias.Offset 10`) [(16:49)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1009s) [(17:37)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1057s). Na begin play proto přes Execute Console Command vrátit detail: Nanite ViewMeshLODBias Min −3 a Offset −1, texture mip bias −1, max pixels per edge 0,5 — upscalovaný obraz pak drží ostrost [(18:25)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1105s) [(19:13)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1153s).

**Frame generation a Reflex:** stejný vzor query → set — **Frame Generation 2×** udělá z 30 snímků 60 (u 4.5 „skoro bez artefaktů") [(20:51)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1251s) [(21:37)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1297s) a **Reflex** srazí input latenci [(22:26)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1346s). Doporučené kombo: balanced/performance + 2× FG + Reflex [(23:12)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1392s). Měření: editor ukazuje jen ne-generované snímky — skutečný výsledek uvidíš ve standalone přes NVIDIA overlay (`Alt+R`); a editor sám žere VRAM, hra poběží líp [(23:59)](https://www.youtube.com/watch?v=y80hX4IlzmI&t=1439s).

> **Pozn.:** DLSS je NVIDIA-only — pro obecný základ má engine TSR (jehož slabiny u jemných detailů popisuje [EasyWaterscape kapitola](nastroje-voda.md#easywaterscape-jak-je-poskladany-dobry-vodni-nastroj)); rozhodnutí o upscaleru patří k volbě cílového hardwaru z [foliage kapitoly](optimalizace.md#foliage-optimalizace-i-kotva-vykonu-a-velka-trojka). Všechny query/set uzly se přirozeně vejdou do options menu — nech hráče vybrat.

**Souvislosti:** [Optimalizace scény](optimalizace.md) · [Nástroje: EasyWaterscape (TSR)](nastroje-voda.md#easywaterscape-jak-je-poskladany-dobry-vodni-nastroj) · [Rejstřík: DLSS](../rejstrik.md#dlss) · [Rejstřík: TSR](../rejstrik.md#tsr) · [Rejstřík: mip mapa](../rejstrik.md#mip-mapa)
