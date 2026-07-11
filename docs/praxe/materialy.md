# Materiály: sdílení, displacement, decay a toon

Materiálová kapitola pokrývá čtyři různě velké myšlenky: **master material workflow** (proč nemá každý mesh nosit pět vlastních textur), **Nanite displacement** na obyčejném meshi, velký **procedurální decay systém** — jedna material function, která umí krev, špínu i toxin na čemkoli — a nový **toon shading** model z 5.8. Principy „jeden shader pro mnoho assetů" v produkčním měřítku ukazuje [kapitola Breakdowny](env-breakdowny.md); tady je stavíme vlastníma rukama.

---

## Master material: pět textur nemá mít každý mesh

**Zdroj:** [Smart Master Material Workflow in Unreal Engine 5](https://www.youtube.com/watch?v=xLlFljzdLF4) · [PolyBoost](https://www.youtube.com/channel/UCHzLwhfU8b07C8WOAcrXiYA) · ~16 min, tutoriál · + [Stop Stretching Textures in UE5](https://www.youtube.com/watch?v=kJgRLfyqjL0) · [Matt Aspland](https://www.youtube.com/channel/UC8_RNwftEO4isrX2LJowcpg) · short

**Shrnutí:** Demo problému naživo: každý importovaný kámen si přinese pět PBR textur a paměť mizí před očima [(3:56)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=236s) [(5:33)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=333s). Řešení: **master materiál se sdílenými tiling texturami**, do kterého si každý mesh přes material instance přinese jen svou baked normal mapu a AO — detail zůstane, paměť ne [(5:59)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=359s).

### Rozpad myšlenky

**Kdy unikátní textury ano:** hero asset, který je ve scéně jednou (tady sea stack z předchozího dílu), si unikátní sadu zaslouží [(3:20)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=200s). Kámen, kterého bude dvacet variant, ne.

**Jádro workflow:** do master materiálu jdou sdílené tiling textury (albedo + normal s Texture Coordinate uzlem na škálování) [(7:09)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=429s) [(7:39)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=459s) — a per-mesh identitu dodá **Blend Angle Corrected Normals**: base normal = tiling detail, additional normal = baked mapa konkrétního meshe [(7:54)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=474s). Textury povýšené na parametry pak v **material instance** vyměníš za baked mapy daného kusu — každý kámen má vlastní siluetu a tvar stínů, ale texturu sdílí celá rodina [(9:20)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=560s) [(11:12)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=672s).

**Kontrola navíc ze Substance:** masky (hrany, dutiny) exportované přes user channel řídí v enginu špínu, zvýraznění hran nebo barevné variace — detail se ladí v materiálu, ne novou texturou [(11:46)](https://www.youtube.com/watch?v=xLlFljzdLF4&t=706s).

**Bonus proti roztahování:** na velkých či škálovaných plochách textura v UV prostoru plave — uzel **World Aligned Texture** (XYZ výstup do base coloru i ostatních map, konstanta ~400 do texture size) ji zamkne na světovou mřížku: mesh můžeš škálovat, natahovat i duplikovat a mapování drží [(0:01)](https://www.youtube.com/watch?v=kJgRLfyqjL0&t=1s).

> **Pozn.:** Tentýž princip, kterým [The Ascent utáhl 80 % assetů na jedné 4K sadě](env-breakdowny.md#the-ascent-ctyri-artisti-jeden-shader) a [TLOU nahradil tisíce bake trim sheetem](env-breakdowny.md#tlou-trim-sheet-ktery-nahradil-tisice-bake) — tohle je jeho miniaturní, okamžitě použitelná verze. Auto-titulky videa jsou hrubé („CS stack" = sea stack, „black hole" = blockout); postup je ale z obrazu jednoznačný.

**Souvislosti:** [Breakdowny: The Ascent](env-breakdowny.md#the-ascent-ctyri-artisti-jeden-shader) · [Rejstřík: trim sheet](../rejstrik.md#trim-sheet) · [Rejstřík: dynamic material instance](../rejstrik.md#dynamic-material-instance)

---

## Nanite displacement: reliéf malovaný vertex colorem

**Zdroj:** [Easy Nanite Displacement in UE5 - Create Stunning Detail](https://www.youtube.com/watch?v=pLl25FaqCiI) · [duongunreal](https://www.youtube.com/channel/UC-tNLOSw67NV08mVY-t3SOw) · ~30 min, tutoriál · + [UE 5.4 Preview Nanite Cliff Tessellation](https://www.youtube.com/watch?v=CdyLdkRmFA0) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~2 min, ukázka

**Shrnutí:** Vícevrstvý terénní materiál na obyčejném meshi: tři Quixel povrchy + kaluže, blendované **vertex paintingem** a vytažené do skutečného reliéfu **Nanite tessellation** [(7:37)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=457s) [(13:05)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=785s). Displacement není normal-mapová iluze — kamínky vystupují z povrchu a reagují na světlo [(0:49)](https://www.youtube.com/watch?v=CdyLdkRmFA0&t=49s).

### Rozpad myšlenky

**Podklad:** flat mesh → remesh (hustota pro malování) → zapnout Nanite [(1:27)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=87s). Materiál se staví z **material attributes**: každá vrstva má Set Material Attributes uzel s vlastními texturami, parametry a UV tilingem [(2:29)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=149s) [(4:03)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=243s); u height textury nastav **sample source = Wrap**, displacement pak navazuje [(4:58)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=298s). V Details materiálu zapnout **Use Material Attributes** [(11:30)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=690s).

**Blend vrstev:** **Vertex Color** uzel dodá malovací kanály a **HeightLerp** s height mapou zařídí, že se vrstvy prolínají podle reliéfu, ne lineárně (štěrk vyleze z bláta nejdřív na hrbolech) [(7:37)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=457s) [(7:46)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=466s); noise ze starter contentu + Contrast rozbijí přechod [(8:57)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=537s) [(10:35)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=635s). Vrstvy řetězí **Blend Material Attributes** [(11:10)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=670s); kaluž navrch je Get Material Attributes extrakce + vodní normal mapa + HeightLerp s modrým kanálem [(16:50)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=1010s) [(24:23)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=1463s).

**Malování a reliéf:** Modeling Tools → Attribute → **Paint Vertex Color** — šedotóny per kanál (R = první vrstva) [(12:25)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=745s); displacement ožije až zapnutím **Nanite Tessellation** v Details meshe [(13:05)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=785s). Hygiena grafu, kterou video mimochodem předvádí: reroute uzly, komentáře přes `C`, skupiny parametrů a **Priority** pole pro pořadí v instanci [(3:42)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=222s) [(28:34)](https://www.youtube.com/watch?v=pLl25FaqCiI&t=1714s).

**Škála síly:** Gorka Games ukazuje totéž na landscape útesu — „kameny" jsou jen landscape materiál s displacement magnitude, laditelné od jemného reliéfu (0,2) po skály (1+), a díky Nanite bez dramatické ceny [(0:01)](https://www.youtube.com/watch?v=CdyLdkRmFA0&t=1s) [(0:49)](https://www.youtube.com/watch?v=CdyLdkRmFA0&t=49s).

> **Pozn.:** Trojice kapitol teď pokrývá displacement ze tří stran: [Landscape](landscape-tipy.md#nanite-displacement-a-krajina-jako-scena) (terén z materiálu), tady mesh s vertex paintingem, a [Crimson Desert breakdown](env-breakdowny.md#crimson-desert-detektivka-kolem-displacementu) připomíná, že existuje i shaderová iluze bez geometrie — každá vrstva má jinou cenu a jiné použití. Titulky videa jsou psané (manuální) a řídké — timestampy vedou na kroky, detaily zapojení odečteš z obrazu.

**Souvislosti:** [Landscape tipy: Nanite displacement](landscape-tipy.md#nanite-displacement-a-krajina-jako-scena) · [Breakdowny: Crimson Desert](env-breakdowny.md#crimson-desert-detektivka-kolem-displacementu) · [Rejstřík: Nanite](../rejstrik.md#nanite) · [Rejstřík: height mapa](../rejstrik.md#height-mapa)

---

## Decay systém I: jedna material function pro krev, špínu i toxin

**Zdroj:** [How To Create A Procedural Decay System - Unreal Engine 5 Material Tutorial](https://www.youtube.com/watch?v=OCgrHAHKmuM) · [Pitchfork Academy](https://www.youtube.com/channel/UCXp4W8jzNe280dGy_IvKX4Q) · ~85 min, tutoriál

**Shrnutí:** Procedurální rozklad — zakrvácení, špína, šířící se toxin — jako **jedna material function**, kterou vložíš do libovolného materiálu v projektu [(0:01)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1s). Masku kreslí **3D noise ve world space**, takže se efekt rozlézá organicky po celém povrchu, a parametr `Decay` (0–1) ho řídí zvenčí — z instance i z blueprintu [(0:47)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=47s) [(10:58)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=658s).

### Rozpad myšlenky

**Architektura funkce:** Function Input s typem **Material Attributes** — funkce přijme celý materiál postavy, **Get Material Attributes** rozbalí jen to, co chce měnit (base color, metallic, roughness, emissive, normal, AO, world position offset), **Set Material Attributes** to po úpravě složí zpět a nezpracované atributy protečou beze změny [(3:55)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=235s) [(6:17)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=377s).

**Maska z 3D šumu:** **Pre-Skinned Local Position** (pre-skinned instance — u animované postavy drží šum na kůži) → **Vertex Interpolator** — a video vysvětluje proč: vertex shader data nejdou použít v pixel logice, interpolator je přenese; větev pro world position offset ale zůstává **bez** interpolatoru [(7:03)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=423s) [(7:49)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=469s). Dál: × scale (0,07) → **Noise** uzel s funkcí **Fast Gradient 3D Texture** (levnější než simplex; méně levels = ještě levnější) [(8:37)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=517s) [(9:24)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=564s) → − bias → × contrast → **lerp z nuly s alphou = parametr `Decay`** → saturate → named reroute `DecayMask` (+ kopie `DecayMaskWPO`) [(10:12)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=612s) [(12:30)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=750s). Drobnost k ukradení: skupina parametrů pojmenovaná `- Decay` — pomlčka ji řadí v instanci nahoru [(10:12)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=612s).

**Blend a decay materiál:** každý atribut se lerpuje originál ↔ decay verze s maskou jako alphou [(14:16)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=856s); decay AO se neřeší (konstanta 1) [(27:20)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1640s). Decay strana má texturu × barvu se dvěma chytrými přepínači: **„mask?"** lerpuje mezi dvěma barvami podle R kanálu textury (krvavě rudá ↔ hnědý strup) [(18:09)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1089s) a **„solid?"** volí mezi plnou náhradou barvy a **Blend Overlay** — photoshopovým prolnutím, které zachová původní tóny [(24:19)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1459s) [(25:05)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1505s). Normal mapa jede přes **Flatten Normal** s pointou: flatness 0 = originál, 1 = plochá, **2 = inverze** — z vln vody jsou najednou bubliny [(22:46)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1366s) [(45:34)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=2734s).

**Nasazení do postavy:** v jejím materiálu **Make Material Attributes** (`Ctrl+drag` přesune celé zapojení pinů), na output uzlu zapnout **Use Material Attributes** a funkci vsadit mezi — hotovo, decay je v každé material instance postavy [(39:17)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=2357s) [(40:53)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=2453s).

> **Pozn.:** Vzor „funkce s material attributes vstupem a výstupem" je obecná **vrstva na materiály** — stejně se staví sníh, mokro po dešti nebo spálení. A stojí za to okoukat i didaktiku: každý parametr do skupiny, každý blok do komentáře — v 85minutovém materiálu je to jediná záchrana.

**Souvislosti:** [Decay II](#decay-system-ii-displacement-pulz-a-zony) · [Rejstřík: material function](../rejstrik.md#material-function) · [Rejstřík: dynamic material instance](../rejstrik.md#dynamic-material-instance)

---

## Decay systém II: displacement, pulz a zóny

**Zdroj:** [How To Create A Procedural Decay System - Unreal Engine 5 Material Tutorial](https://www.youtube.com/watch?v=OCgrHAHKmuM) · [Pitchfork Academy](https://www.youtube.com/channel/UCXp4W8jzNe280dGy_IvKX4Q) · ~85 min, tutoriál

**Shrnutí:** Druhá půlka systému: maska decay nejen barví, ale i **deformuje** — přes world position offset, nebo přesněji přes **Nanite displacement na skeletal meshi** (5.5+) [(0:47)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=47s) [(52:22)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3142s). A gameplay vrstva: volume, ve kterém se efekt plynule nabíjí a po opuštění s prodlevou vyprchá — timeline, interface, žádný cast [(56:56)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3416s).

### Rozpad myšlenky

**Dvě cesty deformace:** *(1)* **WPO**: `DecayMaskWPO` × decay displacement × **Vertex Normal World Space**, přičtené k existujícímu world position offsetu — levné, ale detail závisí na hustotě geometrie a stíny občas zlobí [(28:54)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1734s) [(55:20)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3320s). *(2)* **Nanite displacement**: hodnoty jsou **centrované na 0,5** (nad = ven, pod = dovnitř), takže maska projde úpravou `(x − 0,5) × 2 × síla × 0,5 + 0,5` [(32:04)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1924s) [(35:33)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=2133s); v assetu postavy se zapne **Nanite na skeletal meshi** a v master materiálu **Enable Tessellation** (+ doporučený fade-out na dálku) [(52:22)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3142s) [(53:46)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3226s). Statický přepínač „use nanite displacement?" drží obě větve v jedné funkci [(31:17)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1877s). Záporný displacement = zářezy do těla, kladný = bobtnání [(44:48)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=2688s).

**Pulz:** Time × speed → **Sine** → přemapovat na 0–1 → lerp mezi klidovým a pulzním displacementem: dýchající nádor, tepající toxin (0,1 ↔ 4 při speed 3) [(32:59)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=1979s) [(1:18:18)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4698s). „Debug Time Sine" uzly jsou v produkci v pořádku — je to jen multiply + sine [(34:01)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=2041s).

**Zóna s náběhem a doběhem:** BP_DecayZone = box collision + průsvitná kostka (bez kolize, unlit additive materiál jen jako vizualizace) [(58:28)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3508s). Komunikace přes **Blueprint Interface** s jediným boolem `overlapping?` — zóna volá `Does Object Implement Interface` → message, žádné casty na konkrétní postavu [(57:42)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3462s) [(1:01:02)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3662s). Postava: **Timeline** (délka 1, float track 0→1) s **Set Play Rate** ze **Select** uzlu — vstup = forward rate (0,2), výstup = reverse rate (0,4); při opuštění **Set Timer by Function Name** se 4s prodlevou spustí reverse, při návratu **Clear and Invalidate Timer** prodlevu zruší [(1:03:21)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=3801s) [(1:07:47)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4067s) [(1:09:22)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4162s). Update timeline → **Set Scalar Parameter Value on Materials** na meshi — parametr `Decay` na všech materiálech postavy najednou [(1:10:08)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4208s).

**Tři materiály z jedné funkce:** přes material hierarchy (rodiče s parametry, děti s texturami) vzniká krev (tmavě rudá, zářezy dovnitř, jemný pulz), špína (hnědý overlay ven, dirt normal z Megascans) a toxin (zelená + **emissive glow** s noise texturou a tepáním) [(1:13:18)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4398s) [(1:18:18)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4698s). Víc efektů najednou (krev + jed) = duplikace řetězů s vlastními jmény parametrů a vlastními volumy [(1:22:52)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4972s).

> **Pozn.:** Známé daně: blend extrémních roughness hodnot dělá banding [(1:16:42)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4602s) a šev na UV předělu spraví až triplanar mapování per textura [(1:18:55)](https://www.youtube.com/watch?v=OCgrHAHKmuM&t=4735s). Interface vzor zóny je tentýž, který doporučuje [Komunikace Blueprintů](komunikace-blueprintu.md) — a celé „vstup do zóny → efekt přes čas" je hotový stavební blok pro jedovaté bažiny, radiaci i kletby.

**Souvislosti:** [Decay I](#decay-system-i-jedna-material-function-pro-krev-spinu-i-toxin) · [Komunikace Blueprintů](komunikace-blueprintu.md) · [Pasti a mechaniky](pasti-a-mechaniky.md) · [Rejstřík: Timeline](../rejstrik.md#timeline) · [Rejstřík: Blueprint Interface](../rejstrik.md#blueprint-interface)

---

## Toon shading: pásy světla v 5.8

**Zdroj:** [How To Use Toon Shading New In UE5.8](https://www.youtube.com/watch?v=iMJJYXHMw4o) · [Pitchfork Academy](https://www.youtube.com/channel/UCXp4W8jzNe280dGy_IvKX4Q) · ~31 min, tutoriál

**Shrnutí:** 5.8 přináší **vestavěný toon shading model** přes Substrate: žádný post-process, ale regulérní materiál — **Substrate Toon BSDF** + **Toon Profile** asset s rampami [(2:22)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=142s) [(7:01)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=421s). Největší výhra proti ručním cel shaderům: **správně reaguje na barevná světla, více světel i Lumen** [(21:47)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1307s) [(22:35)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1355s).

### Rozpad myšlenky

**Setup:** v materiálu vytáhnout z Front Material uzel **Substrate Toon BSDF** — vstupy (base color, metallic, specular, roughness) se sbalí na něj [(3:08)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=188s). Praktická omezení z ladění: metallic max ~0,9 (jednička už vypadá realisticky), roughness u kovu nepodlézat ~0,35 (odrazy jsou zatím hladké, ne bandované) a specular nechat na 0,5 [(5:27)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=327s) [(6:13)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=373s).

**Toon Profile:** srdce stylizace. **Diffuse ramp** určuje počet, pozici a tvrdost pásů — smazáním klíčů vznikne ostrý dvoupásmový cel shader (černá + bílá na 0,5), měkkým falloffem zase „PS2 éra"; reset button vrací default [(7:49)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=469s) [(8:36)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=516s) [(9:22)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=562s). **Diffuse ramp offset texture** pásy rozbíjí: noise = malířský rozpad, **sphere render mask** = halftone tečkování, vlastní brush stroke textura = podpis stylu [(10:10)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=610s) [(10:58)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=658s). V sekci GI: diffuse indirect scale 1 = plná spolupráce s Lumenem; při nule zapnout **diffuse ramp includes shadow**, ať se banduje i stín [(12:28)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=748s) [(13:15)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=795s).

**Textury postavy:** diffuse × barva, kanály MRA textury přes multiply (default 1) — pozor, pořadí kanálů se mezi zdroji liší; **AO vynechat**, gradienty do toonu nepatří; normal přes Flatten Normal s parametrem [(14:47)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=887s) [(17:07)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1027s). Materiálová hierarchie: instance A jako rodič (barvy, hodnoty), B jen přepíná texture set [(18:42)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1122s).

**Dva bonusy:** **emissive** z invertovaného kanálu × barva — glow linek funguje s Lumenem i v noci [(23:21)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1401s) [(24:56)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1496s); a **pattern UVs** — default jede po UV meshe, ale uzel **Coordinate Basis Triplanar Dithered** (5.7) s coordinate space **3 = pre-skinned** přilepí halftone vzor na animovanou postavu v konzistentním měřítku na jakémkoli meshi [(26:29)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1589s) [(28:03)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1683s). World position místo toho nechá vzor stát v prostoru a postava jím „proplouvá" — vedlejší efekt, který může být záměr [(25:43)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1543s).

> **Pozn.:** Substrate a toon model jsou čerstvé — chování (např. měkké odrazy při nízké roughness) se může mezi verzemi měnit. Anisotropy vstup existuje (protahuje odlesk jako dno pánve), ale stojí extra a autor ho doporučuje spíš neřešit [(29:37)](https://www.youtube.com/watch?v=iMJJYXHMw4o&t=1777s).

**Souvislosti:** [Decay I: material attributes vzor](#decay-system-i-jedna-material-function-pro-krev-spinu-i-toxin) · [Rejstřík: toon shading](../rejstrik.md#toon-shading) · [Rejstřík: silueta](../rejstrik.md#silueta)
