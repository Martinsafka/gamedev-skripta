# Breakdowny: jak se staví herní světy

Pět pohledů pod kapotu velkých světů — od sólo rekonstrukce San Francisca přes AAA pipeline The Last of Us a jedenáctičlenný tým The Ascent až po grafickou detektivku kolem Crimson Desert. Společný jmenovatel: **žádný z těch světů nestojí na hrubé síle.** Stojí na trim sheetech, instancích, vrstvách špíny a chytrých iluzích — a na disciplíně vědět, kde detail nebude vidět. Praktickou stavbu prostředí od nuly probírá [sesterská kapitola](env-tvorba.md).

---

## San Francisco 1:1: město od jednoho člověka

**Zdroj:** [This Developer Recreated San Francisco 1:1 in Unreal Engine 5](https://www.youtube.com/watch?v=TBGPbs9yjMM) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~36 min, rozhovor s breakdownem

**Shrnutí:** Principal environment artist s 25 lety praxe (Call of Duty, Dead Space, Crysis 2) postavil kilometr čtvereční San Francisca v měřítku takřka 1:1 — poprvé za tři roky večerů při práci, podruhé (přestavba) za rok [(10:11)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=611s). Rozhovor je nabitý řemeslem: jak se trefit do měřítka, jak instancovat město a jak ho udržet hratelné i na starém železe.

### Rozpad myšlenky

**Měřítko začíná dveřmi:** referenci dodal Google Street View a vlastní návštěvy [(1:33)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=93s), ale klíčová rada je jinde — **postav správně dveře** (výška, klika) a zbytek rozměrů „zapadne sám": zábradlí, semafory, mola se pak měří proti nim a proti manekýnovi [(12:33)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=753s) [(13:21)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=801s). Protipříklad zná z praxe: hry, kde kamera potřebovala projít dveřmi, a tak je nafoukli na trojnásobek — a celý svět působil obří a falešný [(14:07)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=847s).

**Město = instance:** všechno, co se opakuje, je ISM/HISM — jedno světlo instancované po celé fasádě, jedno okno na mrakodrap, patra věží, pilíře [(14:54)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=894s) [(15:42)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=942s). Repetici lámou **overlay mesh decaly**: prach u pat, kapající špína od klimatizací, otlučené sokly — jiné na každém „stejném" pilíři [(16:29)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=989s) [(22:45)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1365s). Horizont uzavírá **jediný mesh hory z Gaey**, instancovaný a různě škálovaný do kruhu kolem zálivu — proti dřívějším 2D plochám má hloubku i parallax [(32:03)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1923s) [(32:50)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1970s).

**Textury po staru a chytře:** budovy jedou na **trim texturách** — pás betonového soklu, římsa, dřevo kolem dveří, k tomu cihla tilovaná oběma směry; na budovu stačí dva trimy a jedna cihla [(25:50)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1550s) [(26:37)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1597s). Dva bonusové triky: UV přeložené **přes roh trimu** udělají z ostré 90° hrany vizuální bevel bez geometrie [(27:23)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1643s), a bílá textura + color parametr v Unrealu = jedna omítka v libovolné barvě [(28:09)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1689s).

**Výkon pro dlouhé ulice:** vědomě **LODy místo Nanite** (kompatibilita s UE4; Nanite je volitelný upgrade) [(18:04)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1084s), agresivně laděné kvůli kilometrovým sightlines [(19:37)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1177s); **virtual textures** — „Nanite pro textury" — streamují 4K zdroje jen tam, kam se hráč dívá [(18:50)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1130s); occlusion culling odkládá vše zakryté [(20:24)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1224s) — a pro filmové rendery se dá konzolovým příkazem vypnout, ať vzdálené záběry netrpí pop-inem [(20:24)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1224s). V Maye drží kusy pod ~7 000 trianglů — nad tím engine při importu geometrii sám decimuje (cílem byl i Switch); budova se skládá z dílů do jednoho blueprintu, dveře zvlášť kvůli otevírání [(23:31)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1411s) [(24:17)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=1457s).

**Dvě lekce mimochodem:** střechy původně neřešil („hráč je přece dole") — pak lidi v Fortnite verzi létali helikoptérou, a tak střechy dodělal: **nikdy nevíš, odkud se kdo bude dívat** [(6:17)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=377s). A detaily vyprávějí: stará kůlová mola, riprap kameny proti erozi, sanfranciské požární hlásky — i už zrušené parkovací automaty, které z mapy dělají „snímek města v čase" [(33:37)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=2017s) [(35:12)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=2112s).

> **Pozn.:** Hostující artist není ve videu ani popisu jmenován, kredit patří videu a kanálu. Právní drobnost, která se hodí: repliky **veřejných** prostor jsou v pořádku, u soukromých interiérů opatrně — proto má jeho pošta generický interiér [(3:55)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=235s). A sólo výhoda oproti AAA specializaci: „konečně jsem si udělal Niagara ptáky i vodu" — malé projekty učí šířku [(10:58)](https://www.youtube.com/watch?v=TBGPbs9yjMM&t=658s).

**Souvislosti:** [Landscape tipy: Gaea a gizmo](landscape-tipy.md#copypaste-gizmo-sculpty-jako-znovupouzitelne-patche) · [Rejstřík: trim sheet](../rejstrik.md#trim-sheet) · [Rejstřík: instance](../rejstrik.md#instance) · [Rejstřík: draw call](../rejstrik.md#draw-call)

---

## The Ascent: čtyři artisti, jeden shader

**Zdroj:** [How 4 Artists Built a AAA World](https://www.youtube.com/watch?v=a78WoZeZGqI) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~22 min, breakdown (GDC 2022 materiály)

**Shrnutí:** Neon Giant — 11 lidí, z toho **čtyři artisti a žádný concept artist** — postavili v UE4 za čtyři roky jeden z nejhustších sci-fi světů moderních her. Jak: **~80 % hard-surface assetů sdílí jediný shader s jednou 4K sadou textur** [(0:03)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=3s), Houdini nástroje nahradily ruční set dressing a lightmapový trik ušetřil 10 % draw calls [(2:23)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=143s).

### Rozpad myšlenky

**Špína bez textur:** klasika (tisíce unikátních dirt masek) byla pro 4 lidi nemyslitelná. Místo toho **UDIM trik — offset UV setu funguje jako maska**: posunutím UV se volí barva a materiál (holý/lakovaný kov, plast) bez jediné textury navíc [(3:09)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=189s). „Ručně otexturovaný" dojem skládají tři vrstvy: masky v trim sheetu (špína kolem šroubů, kde logicky vzniká), **vertex color z bake ambient occlusion** (kontextová špína podle tvaru assetu) a AO maska zapečená se světlem (špína mezi objekty ve světě) [(3:56)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=236s) [(4:43)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=283s). Důkaz síly: špinavé slumy a sterilní laboratoř jsou **tytéž assety s tímtéž materiálem** [(5:29)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=329s). Bonus, který nikdo neplánoval: pár sliderů na master materiálu řídí art direction celé hry [(7:01)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=421s).

**Vědomé kompromisy:** trim sheet + malá sada baked kusů, **weighted normals** a jen low-poly geometrie; zblízka by assety neobstály — jenže top-down kamera se zblízka nikdy nedívá [(5:29)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=329s) [(6:15)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=375s). Tři barvy, tři kovy, tagging v Modu, pod 100 MB world textur — a výsledkem 8 000+ assetů, zhruba **tři hotové denně na artistu** (Tor Frick, GDC 2022) [(7:01)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=421s) [(7:47)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=467s).

**Houdini místo rukou** (senior tech artist Magnus Larsen): **Room Maker** — modulární kity v mocninách dvou se striktní výškou, volume v additive/subtractive režimu složí místnost včetně debris, kabelů a decalů za sekundy [(8:34)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=514s); Vista House Maker pro blízké i vzdálené kulisy [(10:08)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=608s); generátor cedulí z textu/obrázku s vertex color blikáním [(10:53)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=653s); pipe maker po splině s 34modulovou sadou [(11:22)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=682s); kabely závěsné (simulace, nebo rychlejší „vlastní matika") i podlahové tažené po geometrii [(12:09)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=729s) [(12:56)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=776s). I destrukce je iluze: HDA předpečou směrové simulace a blueprint přehraje tu správnou podle pozice hráče — vypadá to fyzikálně, je to trigger [(13:42)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=822s).

**Světlo za babku:** velká statická světla + lightmapy, a **reflection probes jako štětec** — top-down kamera dovolila položit 64×64 cubemapy přesně nad kaluže a lesklé podlahy (limit 341 naráz) [(15:15)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=915s) [(16:01)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=961s). Nejchytřejší trik: **zvýšení rozlišení lightmap z 1K na 2K sbalilo víc assetů do jedné lightmapy** — a protože UE4 auto-instancing spojuje jen kusy se stejným meshem, materiálem *a lightmapou*, kleslo množství draw calls o 10 % za pouhých +50 MB [(16:48)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=1008s). K tomu extra mip na volumetric light grid (150→40 MB) [(17:34)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=1054s) a — podle Tora Fricka největší optimalizace vůbec — **distance-based fading na všech světlech** [(17:34)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=1054s).

> **Pozn.:** Video rámuje i kariérní lekce: škola učí ladit hero asset donekonečna, průmysl žije z limitů — staré enginy, chybějící dokumentace, komunikace místo dokonalosti. A prakticky: 4K texturu většinou nepotřebuješ a roughness klidně snese poloviční rozlišení než albedo [(20:42)](https://www.youtube.com/watch?v=a78WoZeZGqI&t=1242s). Jména (Tor Frick, Magnus Larsen) pocházejí z auto-titulků přepisu — psaná podoba ověřena podle veřejných GDC/ArtStation materiálů zmíněných ve videu.

**Souvislosti:** [TLOU: trim sheety](#tlou-trim-sheet-ktery-nahradil-tisice-bake) · [Rejstřík: trim sheet](../rejstrik.md#trim-sheet) · [Rejstřík: draw call](../rejstrik.md#draw-call) · [Rejstřík: data-driven design](../rejstrik.md#data-driven-design)

---

## TLOU: trim sheet, který nahradil tisíce bake

**Zdroj:** [The Environment Art Tricks Behind TLOU Part 1](https://www.youtube.com/watch?v=EJcqhvylH50) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~10 min, breakdown

**Shrnutí:** The Last of Us Part 1 běží ve 4K na 60 FPS, protože artisti Naughty Dog dostali do rukou **pipeline, ne jen nástroje**: baked bevel trim sheet místo tisíců unikátních normal map, modulární kity a materiály vrstvené vertex colorem [(0:03)](https://www.youtube.com/watch?v=EJcqhvylH50&t=3s). Breakdown čerpá z veřejných portfolií konkrétních artistů.

### Rozpad myšlenky

**Proč šetřit:** 60 FPS = 16,6 ms na snímek. Neoptimalizovaný hero asset zabolí třikrát najednou: unikátní 4K textury plní VRAM (stuttering, pozdní streaming), každý unikátní objekt je draw call navíc, a těžké shadery (sklo, vrstvení) renderují tentýž pixel víckrát — overdraw [(0:49)](https://www.youtube.com/watch?v=EJcqhvylH50&t=49s) [(1:36)](https://www.youtube.com/watch?v=EJcqhvylH50&t=96s).

**Baked bevel trim sheet** (principal artist Matthew Trevelyan Johns): jeden sdílený trim layout — vysokopolygonové panely nasnímané v 512 px/m — nahrazuje individuální bake u stovek propů [(2:25)](https://www.youtube.com/watch?v=EJcqhvylH50&t=145s) [(3:11)](https://www.youtube.com/watch?v=EJcqhvylH50&t=191s). Modely se stavějí **hard-edge, bez bevelů, v 90° úhlech** — všechno zaoblení hran dodá normal mapa z trimu; míň polygonů a stejný vzhled [(3:11)](https://www.youtube.com/watch?v=EJcqhvylH50&t=191s) [(3:58)](https://www.youtube.com/watch?v=EJcqhvylH50&t=238s). K tomu Substance Designer šablona (tileable textury, edge wear, blend masky pro celý tým) a nástroj se SideFX Labs, který **UV shelly zarovná na správné trim oblasti pár kliky** [(3:11)](https://www.youtube.com/watch?v=EJcqhvylH50&t=191s) [(3:58)](https://www.youtube.com/watch?v=EJcqhvylH50&t=238s). Tohle je práce principal artista: vymyslet, ověřit a zdokumentovat workflow, který tým ponese roky [(3:58)](https://www.youtube.com/watch?v=EJcqhvylH50&t=238s).

**Modulární kity a vrstvené materiály:** University Plaza (Nestor Carpintero, materiály Peyton Varney) ukazuje celou cestu — tile sety s wireframy v Maye, vertex painting, finále v enginu se set dressingem; hustota vertexů je záměrná, slouží blendování materiálů [(4:45)](https://www.youtube.com/watch?v=EJcqhvylH50&t=285s) [(5:33)](https://www.youtube.com/watch?v=EJcqhvylH50&t=333s). Kapitolské materiály (Jonathan Benainous) vznikají v Substance Designeru a **RGB kanály vertex coloru malují texture sety z knihovny** — praskliny, mech, zatékání přesně tam, kam patří [(6:19)](https://www.youtube.com/watch?v=EJcqhvylH50&t=379s) [(7:52)](https://www.youtube.com/watch?v=EJcqhvylH50&t=472s). A perla iluzí: kovaná brána, kde geometrii má jen rám a madlo — ornamenty jsou **opacity maska + height mapa + parallax occlusion mapping** [(7:06)](https://www.youtube.com/watch?v=EJcqhvylH50&t=426s).

> **Pozn.:** Stejný závěr jako u [The Ascent](#the-ascent-ctyri-artisti-jeden-shader) z opačného konce rozpočtu: AAA kvalita nestojí na sochání, ale na **systémech** — sdílené trimy, knihovny materiálů, dokumentované pipeline. Pro portfolio to znamená: ukaž kit a shader úvahu, ne jen hezký kámen.

**Souvislosti:** [The Ascent](#the-ascent-ctyri-artisti-jeden-shader) · [Crimson Desert](#crimson-desert-detektivka-kolem-displacementu) · [Rejstřík: trim sheet](../rejstrik.md#trim-sheet) · [Rejstřík: parallax occlusion mapping](../rejstrik.md#parallax-occlusion-mapping)

---

## RE Requiem: realismus je vrstvení

**Zdroj:** [Why Resident Evil Requiem Looks So Real | Graphics Breakdown](https://www.youtube.com/watch?v=utYMtJwGxiM) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~18 min, breakdown

**Shrnutí:** Prostředí Requiem nevypadají skutečně kvůli jednomu grafickému průlomu, ale kvůli **desítkám malých vrstev, které drží pohromadě** — a video to dokazuje experimentem: postupně vrstvy odebírá (variace povrchů → decaly → hustota propů → světlo), až scéna „zase vypadá jako videohra" [(5:44)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=344s) [(5:57)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=357s).

### Rozpad myšlenky

**Vrstvy materiálu:** skutečné povrchy nejsou uniformní — beton mění drsnost, barva se odírá, vlhkost sedá v koutech. AAA materiál proto skládá base detail + mikro šum + dirt overlay + edge wear + roughness variaci; odeber je a iluze zmizí okamžitě [(2:24)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=144s). K tomu **micro detail**, který mozek očekává: prach na hranách, škrábance v místech doteku — bez nich objekty působí jako plastové rekvizity [(4:10)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=250s).

**Kontrolovaná hustota:** místnosti jsou nabité propy, ale nic není náhodně — placement podporuje vyprávění i čitelnost gameplaye; „lived-in", ne „staged" [(4:58)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=298s). Hustota roste u focal pointů, pozadí se zjednodušuje kvůli čitelnosti i výkonu [(14:34)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=874s).

**Světlo jako fyzika i dramaturgie:** materiály vypadají skutečně, jen když na ně světlo správně reaguje — a hlavně **v pohybu**: highlighty putují po povrchu, odrazy se mění, stíny se vyvíjejí; přesně tohle mozek zná z reality a jeho absence křičí „umělé" [(7:32)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=452s) [(8:18)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=498s). Requiem sází na **kontrast** — silné směrové světlo a stíny definují tvar a hloubku (plus náladu hororu) [(8:18)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=498s) — a volumetrika (prach, mlha v paprscích) dodává prostoru „vzduch" [(9:05)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=545s).

**Environmental storytelling:** převrácená židle, otevřený šuplík, rozházené dokumenty — jednotlivosti, dohromady příběh, který se odehrál před příchodem hráče [(10:37)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=637s). Prostory nesou historii používání (edge wear na klikách, škrábance u dveří, prach v koutech) [(11:25)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=685s) a kompozice tiše naviguje: stopa předmětů vede ke dveřím, průlom ve zdi rámuje další místnost. V hororu prostředí buduje napětí dřív, než se cokoli stane [(12:11)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=731s).

> **Pozn.:** Tři přenositelné lekce na závěr videa [(13:47)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=827s) [(15:20)](https://www.youtube.com/watch?v=utYMtJwGxiM&t=920s): realismus vzniká ze **vztahů mezi assety**, ne z jednoho hero kusu; komplexitu řiď (víc u ohnisek, míň v pozadí); a navrhuj **průchod, ne screenshot** — kamera se hýbe a světlo se musí hýbat s ní. Jak Requiem skrývá loading za dveřmi a výtahy, rozebírá [kapitola Levely a streaming](levely-a-streaming.md).

**Souvislosti:** [Levely a streaming](levely-a-streaming.md) · [Teorie: vedení hráče](../teorie/vedeni-hrace.md) · [Rejstřík: environmental storytelling](../rejstrik.md#environmental-storytelling) · [Rejstřík: decal](../rejstrik.md#decal)

---

## Crimson Desert: detektivka kolem displacementu

**Zdroj:** [How Crimson Desert Fakes Realism (It's Genius)](https://www.youtube.com/watch?v=TUAyiCswYt4) a [The ''Fake'' Geometry of Crimson Desert: How it Really Works](https://www.youtube.com/watch?v=44PT8XRZRGA) · [Next Level Game Art](https://www.youtube.com/channel/UCmPBLkozH1irLObN0Q3_aJw) · ~10 + 13 min, technická investigace

**Shrnutí:** Každá kamenná zeď v Crimson Desert vypadá jako hustá geometrie — a ve 3ds Max je to plochá deska [(0:05)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=5s). Pearl Abyss (vlastní engine Black Space) mlčí, a tak komunita vedla vyšetřování, které tahle dvojice videí poctivě dokumentuje **včetně vlastních omylů**: displacement? Parallax occlusion mapping? SPOM? Závěr zní **screen space displacement — lhaní přímo do Z-bufferu** [(4:46)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=286s).

### Rozpad myšlenky

**Slovník podezřelých:** *displacement* = tessellace + skutečný posun vertexů podle height mapy (drahé na geometrii); *POM* = posun UV podle úhlu kamery a height mapy — bez geometrie, proto na hraně zdi „uřízne" a siluetu neumí [(1:37)](https://www.youtube.com/watch?v=TUAyiCswYt4&t=97s) [(2:25)](https://www.youtube.com/watch?v=TUAyiCswYt4&t=145s); *SPOM* (silhouette POM) hrany řeší — technika stará přes dekádu (CryEngine, v UE4 dosažitelná už 2015), „tessellation bez tessellace" [(3:59)](https://www.youtube.com/watch?v=TUAyiCswYt4&t=239s) [(5:31)](https://www.youtube.com/watch?v=TUAyiCswYt4&t=331s) [(6:18)](https://www.youtube.com/watch?v=TUAyiCswYt4&t=378s).

**Důkazní materiál:** zdi mají **siluety na každém rohu** — čisté POM vyloučeno [(2:25)](https://www.youtube.com/watch?v=TUAyiCswYt4&t=145s); efekt je vidět v **depth bufferu** (kontrola přes free nástroj ReShade), kam by se POM renderované později vůbec nedostalo [(1:37)](https://www.youtube.com/watch?v=TUAyiCswYt4&t=97s); a korunní svědek — **meč hráče clipuje skrz kámen, který geometricky neexistuje** [(0:51)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=51s). Typický wobble na kraji obrazovky při rychlé kameře pak sedí na screen-space rodinu technik [(6:18)](https://www.youtube.com/watch?v=TUAyiCswYt4&t=378s) [(7:08)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=428s).

**Jak screen space displacement funguje:** existuje až **po projekci geometrie do 2D** — shader vede paprsek podél view vektoru skrz height mapu, najde „výšku kamene" a **přepíše hloubku pixelu v Z-bufferu** [(4:46)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=286s) [(5:33)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=333s). Proto kameny vrhají siluety a schovávají věci za sebou, ačkoli mesh je prkno [(6:20)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=380s). Účet: tisíc polygonů + 1K height mapa místo milionů trianglů přes Nanite — vítězství šířky pásma, obří draw distance z jednoho shader passu a běží to i na starších konzolích; daní je flickering/jitter, na který si hráči stěžují [(6:20)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=380s) [(7:08)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=428s).

**Obrácený workflow:** v tomhle světě je **height mapa důležitější než albedo** — albedo je jen „nátěr barvy" (proto vypadají textury Crimson Desert samostatně vyprané a ploché), zatímco height řídí světlo, self-shadowing i siluetu [(7:50)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=470s) [(8:36)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=516s). Takeaways pro vlastní práci: čisté mid-poly siluety + mikrodetail v shaderu, čas investovat do height map (Substance Designer/ZBrush) a modulární kusy stavěné na opakování podél křivky — ne unikátní padesátimetrové zdi [(10:56)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=656s) [(11:43)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=703s).

> **Pozn.:** Metodicky vzácný materiál: autor v novějším videu otevřeně říká „mýlil jsem se" a opravuje vlastní SPOM hypotézu [(0:05)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=5s) — a i finální závěr rámuje jako kvalifikovanou spekulaci, dokud Pearl Abyss nepromluví. Pointa pro nás zůstává bez ohledu na přesný verdikt: „nejpůsobivější next-gen vizuály často stojí na chytrých old-school iluzích" [(12:30)](https://www.youtube.com/watch?v=44PT8XRZRGA&t=750s) — stejná filozofie jako [POM brána v TLOU](#tlou-trim-sheet-ktery-nahradil-tisice-bake).

**Souvislosti:** [TLOU](#tlou-trim-sheet-ktery-nahradil-tisice-bake) · [Rejstřík: parallax occlusion mapping](../rejstrik.md#parallax-occlusion-mapping) · [Rejstřík: height mapa](../rejstrik.md#height-mapa) · [Rejstřík: Nanite](../rejstrik.md#nanite)
