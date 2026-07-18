# Matematika pro gamedev: méně děsivá, než vypadá

SimonDev (grafický programátor z AAA praxe) prochází matematiku, kterou herní vývojář skutečně používá — a ukazuje, že většina z ní je o dost jednodušší, než jak vypadá na Wikipedii. Kapitola pokrývá každodenní nástroje (lerp, goniometrie, vektory, dot product) i teorii rotací (matice, Eulerovy úhly, kvaterniony). Závěrečná případovka z Quake 3 pak předvádí, co dokáže vývojář, který rozumí i bitům pod matematikou. Vizuální podloží maticové části najdeš v [Lineární algebře vizuálně](linearni-algebra-vizualne.md).

---

## Lerp a goniometrie: nejlevnější kouzla v enginu

**Zdroj:** [What Kind of Math Should Game Developers Know?](https://www.youtube.com/watch?v=eRVRioN4GwA) · [SimonDev](https://www.youtube.com/channel/UCEwhtpXrg5MmwlH04ANpL8A) · ~20 min, přehledová esej

**Shrnutí:** Největší „bang for your buck" v herní matice je **lineární interpolace**: A + (B − A) · t [(0:02)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=2s). Síla je v tom, že A a B může být cokoli — pozice, scale, barva, délka health baru. Druhý pilíř je goniometrie na jednotkové kružnici: sin, cos a tan pokryjí šokující podíl toho, co hry od trigonometrie potřebují [(3:07)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=187s).

### Rozpad myšlenky

**Lerp** sám o sobě je tupě lineární — pohyb z něj vypadá stroze. Náprava nejde přes složitější vzorec, ale přes **shaping functions**: na parametr t aplikuješ smoothstep nebo exotičtější křivku (bounce) a tentýž lerp najednou zrychluje, brzdí nebo pruží [(0:49)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=49s). Pokročilejší trik: interpolovat nemusíš v RGB — gradient přes HSV nebo Lab prostor vypadá jinak a často příjemněji [(1:35)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=95s). Kdo si někdy hrál s Timeline a materiálovými přechody v UE, dělal přesně tohle, jen to takhle nenazval.

**Úhly**: v UI a denním životě stupně, v matematice radiány — radián je úhel, který na jednotkové kružnici vytne oblouk délky 1 [(2:21)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=141s). A **goniometrie** není nauka o vzorečcích, ale o trojúhelnících na téže kružnici [(3:07)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=187s): pro bod na kružnici je cos θ vodorovná vzdálenost, sin θ svislá, tan θ vzdálenost na tečně x = 1 — proto tan v ±π/2 „uletí do nekonečna" [(3:54)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=234s).

Praktická výplata je okamžitá [(4:40)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=280s): pulzování = scale modulovaný sinem času; vznášení = výška + sin času; orbit a spirála = x z cosinu, y ze sinu. Tři funkce, celý katalog „živých" animací zadarmo.

**Souvislosti:** [Game feel a imerze](game-feel.md) — proč tyhle drobné pohyby prodávají pocit · [Rejstřík: Lerp](../rejstrik.md#lerp)

---

## Vektory a dot product: poloha, pohyb a zorné pole

**Zdroj:** [What Kind of Math Should Game Developers Know?](https://www.youtube.com/watch?v=eRVRioN4GwA) · [SimonDev](https://www.youtube.com/channel/UCEwhtpXrg5MmwlH04ANpL8A) · stejné video, část o vektorech

**Shrnutí:** Vektor je jen dvojice (trojice) čísel — ale vyplatí se rozlišovat **poziční vektory** (bod v prostoru) a **směrové vektory** (směr + velikost, třeba velocity) [(5:27)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=327s). Pár povolených operací nad nimi dá celý pohybový systém; dot product k tomu přidá odpověď na otázku „jak moc se dva směry shodují" — základ viditelnosti, osvětlení i AI vnímání.

### Rozpad myšlenky

Aritmetika s významem [(5:27)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=327s): pozice + vektor = nová pozice (posun); vektor ± vektor = vektor (skládání sil); pozice − pozice = vektor „odsud tam" (vzdálenost a směr k cíli); skalár × vektor = natažení (velocity × čas). A pozice + pozice = nesmysl — dobrý test, jestli kód dává fyzikální smysl. Z toho okamžitě padá **Eulerova integrace** [(6:13)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=373s): nová pozice = pozice + velocity · dt, nová velocity = velocity + akcelerace · dt. Nedokonalé, ale jednoduché — a přesně tohle dělá každý „MoveActor za tick" Blueprint. (Pro stabilnější simulace video odkazuje na Verletovu integraci [(7:00)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=420s).)

**Dot product** dvou jednotkových vektorů = cos úhlu mezi nimi [(7:49)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=469s): 1 znamená stejný směr, 0 kolmost, −1 protisměr. To je celé — a stačí to na klasickou úlohu „vidí mě věž?" [(8:36)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=516s): dot forward vektoru věže s normalizovaným vektorem k hráči; znaménko říká před/za, a pro zorné pole 60° porovnáš výsledek s cos(30°) ≈ 0,866. Dvě násobení a sčítání — žádný trace, žádná trigonometrická funkce za běhu.

> **Pozn.:** Tohle je přesně matematika, kterou UE schovává za nody jako `Dot Product` a `Get Unit Direction`. AI Perception v [AI vnímání](../praxe/ai-vnimani.md) dělá pod kapotou tutéž úvahu — úhel zorného pole je jen cos-práh nad dot productem.

**Souvislosti:** [AI vnímání](../praxe/ai-vnimani.md) · [Základy pohybu](../praxe/pohyb-zaklady.md) · [Rejstřík: Dot product](../rejstrik.md#dot-product) · [Rejstřík: Normalizace vektoru](../rejstrik.md#normalizace-vektoru)

---

## Matice, rotace a kvaterniony: tři způsoby, jak držet otočení

**Zdroj:** [What Kind of Math Should Game Developers Know?](https://www.youtube.com/watch?v=eRVRioN4GwA) · [SimonDev](https://www.youtube.com/channel/UCEwhtpXrg5MmwlH04ANpL8A) · stejné video, část o maticích a rotacích

**Shrnutí:** Matice přestane být „blok náhodných čísel", když ji čteš jako **lineární transformaci**: sloupce jsou nové osy prostoru [(9:23)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=563s). Pro rotace má gamedev tři reprezentace — matice, Eulerovy úhly a kvaterniony — a každá má svou past: matice se blbě interpolují, Eulerovy úhly trpí gimbal lockem, kvaterniony se blbě chápou [(12:29)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=749s).

### Rozpad myšlenky

**Matice jako nové osy:** chceš prostor natáhnout 3× vodorovně a 2× svisle? Nové osy (3,0) a (0,2) prostě zapíšeš do sloupců [(10:10)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=610s). Rotační matice není magie, ale bod na jednotkové kružnici: osa X jde na (cos θ, sin θ), osa Y na totéž o 90° dál [(10:57)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=657s). Translace se do lineární transformace nevejde — proto **homogenní souřadnice**: přidáš třetí (resp. čtvrtou) dimenzi, bod žije v (x, y, 1) a posun se „propašuje" do posledního sloupce; jedna matice pak nese rotaci, scale i translaci najednou [(11:43)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=703s). To je důvod, proč jsou transform matice v enginech 4×4.

**Reprezentace rotací** a jejich trade-offy:

- **Matice**: 9 hodnot pro 3D a mizerná interpolace — mezi dvěma maticemi se model cestou rozpadá [(12:29)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=749s).
- **Eulerovy úhly** (yaw/pitch/roll): kompaktní a intuitivní — proto je vidíš v každém UI enginu [(13:15)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=795s). Ale interpolují se špatně a hrozí **gimbal lock**: rotace se aplikují v pevném pořadí, a když se prostřední osa otočí o 90°, vnější a vnitřní osa se zarovnají — ztratil jsi stupeň volnosti [(14:01)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=841s). Uživatelské rozhraní ano; vnitřek enginu ne.
- **Kvaterniony**: 4 hodnoty, imunní vůči gimbal locku (pokud je nestavíš z Eulerových úhlů a nečekáš zázrak) a hladká interpolace přes **slerp** [(14:48)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=888s). Cena: intuice prakticky nulová — a to je v pořádku. SimonDev přiznává, že přesné vnitřnosti kvaternionů potřeboval za kariéru jednou, u pohovoru [(15:35)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=935s).

Aspoň tušení, *proč* kvaterniony fungují, dává oklika přes komplexní čísla [(16:22)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=982s): násobení imaginární jednotkou i je rotace o 90° v rovině reálná–imaginární, a násobení komplexním číslem na jednotkové kružnici vyjde nachlup stejně jako rotační matice [(17:55)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=1075s). Kvaterniony jsou totéž rozšířené o tři imaginární složky — s divočejšími pravidly.

> **Pozn.:** Prakticky v UE: `Rotator` = Eulerovy úhly (UI, čitelnost), `Quat` = kvaternion (interpolace, skládání rotací bez gimbal locku). Když ti kamera nebo věž při naivní interpolaci rotací „cukne přes delší stranu", vzpomeň si na tuhle myšlenku. Video na závěr doporučuje zdroje: 3Blue1Brown, Freya Holmér a Jorge Rodriguez [(19:27)](https://www.youtube.com/watch?v=eRVRioN4GwA&t=1167s) — a autor zároveň prodává vlastní kurz, ber s tím.

**Souvislosti:** [Lineární algebra vizuálně](linearni-algebra-vizualne.md) — tytéž matice viděné jako pohyb teček · [Rejstřík: Kvaternion](../rejstrik.md#kvaternion) · [Rejstřík: Gimbal lock](../rejstrik.md#gimbal-lock) · [Rejstřík: Eulerovy úhly](../rejstrik.md#eulerovy-uhly)

---

## Případovka: rychlá inverzní odmocnina z Quake 3

**Zdroj:** [The Math Hack That Made Quake 3 Possible](https://www.youtube.com/watch?v=coU_o6L5XZI) · [Dr. Pavel Vlašánek](https://www.youtube.com/channel/UCNvw05HVThcon7sUvitXwBA) · ~17 min, rozbor legendárního kódu

**Shrnutí:** Funkce `Q_rsqrt` ze zdrojáku Quake 3 počítá 1/√x bez dělení a bez odmocniny — pomocí „nelegálního" čtení bitů floatu jako integeru a magické konstanty `0x5f3759df` [(0:00)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=0s). Případovka je cenná dvakrát: ukazuje, *proč* hry normalizují vektory na každém kroku, a předvádí, co umožňuje znalost spodních vrstev — i když dnes už tenhle konkrétní trik nahradila hardwarová instrukce.

### Rozpad myšlenky

**Proč je 1/√x tak důležité:** normalizace vektoru = vydělit složky délkou, délka = Pythagoras = odmocnina [(3:02)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=182s). A normalizované vektory potřebuje všechno [(0:33)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=33s): dynamické osvětlení (dot L·N = cos úhlu funguje jen s jednotkovými vektory [(1:25)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=85s)), hitscan railgun (normalizovaný pohledový vektor × dostřel = paprsek mapou [(2:12)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=132s)) i klouzání po zdi přes normálu povrchu [(3:02)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=182s). V roce 1999 přitom bylo floatové dělení pomalé a odmocnina ještě pomalejší — krát tisíce polygonů za frame [(3:48)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=228s).

**Trik má tři patra:**

1. **Bity jako logaritmus.** IEEE 754 float je pod kapotou vědecká notace: znaménko, exponent, mantisa [(4:37)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=277s). Když tytéž bity přečteš jako integer, dostaneš — škálovaně a posunutě — přibližně log₂ čísla, s chybou pod 0,1 % [(5:23)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=323s). A y = x^(−0,5) je v logaritmu jen log y = −0,5 · log x; dělení dvěma je v binárce bit-shift doprava [(6:19)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=379s).
2. **Magická konstanta.** Po dosazení a algebře zbyde vzorec I_y ≈ konstanta − I_x/2 — a ta konstanta, předpočítaná korekce chyby aproximace log₂(1+v) ≈ v + μ pro optimální μ ≈ 0,045, vyjde přesně `0x5f3759df` [(10:33)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=633s). Magic number je jindy code smell; tady je to ospravedlněná výjimka [(7:05)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=425s).
3. **Newton–Raphson na dočištění.** Bitový odhad má chybu ~1 % — na grafiku moc [(11:49)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=709s). Jedna iterace Newtonovy metody s chytře přeuspořádanou funkcí (aby z ní vypadlo dělení: y·(1,5 − 0,5·x·y²)) srazí chybu na 0,17 % [(15:15)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=915s) — „kód rychlosti světla postavený na kalkulu" [(16:00)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=960s).

**Dnes** už to nepiš: moderní CPU/GPU mají `rsqrtss` a příbuzné instrukce přímo v křemíku [(16:00)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=960s). Lekce ale zůstává: když víš, jak jsou bity fyzicky uložené v paměti, můžeš optimalizovat „do absurdních mezí" — a přinejmenším přestaneš mít z floatů a normalizace strach.

> **Pozn.:** Krásný detail: nikdo s jistotou neví, kdo trik vymyslel ani kdo ho do Quake 3 napsal [(0:13)](https://www.youtube.com/watch?v=coU_o6L5XZI&t=13s). A autor videa je mimochodem Čech — loučí se „čau".

**Souvislosti:** [Optimalizace scény](../praxe/optimalizace.md) — dnešní podoba téže disciplíny · [Rejstřík: Normalizace vektoru](../rejstrik.md#normalizace-vektoru) · [Rejstřík: Dot product](../rejstrik.md#dot-product)
