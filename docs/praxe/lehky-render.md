# Lehký render: co vypnout, když UE5 funkce nepotřebuješ

Zbytek bloku o výkonu se ptá, **jak zlevnit funkce UE5**. Tahle kapitola sbírá materiály, které se ptají jinak: **co když je vůbec nechceš?** Lumen, Nanite, virtuální stíny a TSR jsou ve výchozím stavu zapnuté a jsou navržené pro určitý druh hry — a projektů, kterým se hodí spíš pečené světlo, LODy a levné vyhlazování, je hodně. Poslední myšlenka ukazuje totéž rozhodování na skutečné hře, ne na prázdné šabloně.

Je to poctivá pozice a stojí za to ji znát celou, včetně toho, kde přestává být rozumná. Předchozí kapitola s podobným napětím je [spor o Nanite](nanite-do-hloubky.md#spor-o-nanite-co-tvrdi-kritika-a-co-z-toho-plati).

---

## Rozpad ceny výchozí scény — a čím ji nahradit

**Zdroj:** [How To Improve Performance — Unreal Engine 5 Tutorial](https://www.youtube.com/watch?v=S-vO9YNI7zs) · [Pitchfork Academy](https://www.youtube.com/channel/UCXp4W8jzNe280dGy_IvKX4Q) · ~27 min, tutoriál

**Shrnutí:** Autor vezme **default třetí osobu v 5.6**, pustí `stat GPU` a jde odshora dolů: co ta scéna stojí, aniž jsi cokoli udělal. Pak každou položku vypne a hned dodá, **čím ten vizuální dojem nahradit**, aby scéna nezešedla — a v tom je hodnota, protože „vypni Lumen" umí každý, „vypni Lumen a zvedni skylight na dvojku a přidej post-process AO" už méně. Háček, který ho sám zaskočí: **jedna z jeho vlastních rad měření nepotvrdilo.**

### Rozpad myšlenky

**Výchozí scéna, rozpočet 13 ms** [(3:09)](https://www.youtube.com/watch?v=S-vO9YNI7zs&t=189s). V `stat GPU` jsou nad milisekundou: deferred lighting (to je daň za render path a nemění se), **post-process volume 2 ms** *„a to jsme s ním vůbec nic nedělali"*, **volumetric cloud ~1,5 ms** a **temporal super resolution**.

**Mraky: jedno pole, které zlevní i zlepší** [(5:30)](https://www.youtube.com/watch?v=S-vO9YNI7zs&t=330s). Nemá-li být obloha statická, nemusí se mraky vypínat úplně — v detailech volumetric cloudu je **tracing max distance mode**, a přepnutí z *distance from cloud layer entry point* na *distance from point of view* dá **5–10 FPS** a podle autora **vypadá to v dálce lépe**, protože se ztratí přehuštěné mraky u horizontu, které stejně zakryjí hory nebo budovy.

**Globální osvětlení: tři úrovně a co za ně** [(7:04)](https://www.youtube.com/watch?v=S-vO9YNI7zs&t=424s). Lumen → **screen space** → **none**, s frame time 13 → 8,3 → ~7 ms. A protože scéna bez Lumenu ztratí odražené světlo a zbělá stíny, přidává dvě náhrady:

| co ztratíš | čím to nahradit |
|---|---|
| ambient occlusion v koutech | **post-process AO** (intenzita ~0,75, radius 200 — jeho výchozí čísla) |
| ambientní nadsvětlení a světlost stínů | **skylight intensity 2** (*„nešel bych nad tři, maximálně pět"*) |
| barevné odrazy na stěnách | nic — tohle je to, co Lumen doopravdy umí a screen space ne |

A věcná poznámka, na kterou při tom sám narazí: **Lumen reflections bez Lumen GI nefungují** — spadne to zpátky na screen space, takže se odraz ztratí, jakmile odrážený objekt zmizí z obrazu.

**Skylight movable proti stationary** [(13:19)](https://www.youtube.com/watch?v=S-vO9YNI7zs&t=799s) je nejméně známá položka celého videa: **movable skylight zapíná distance field ambient occlusion**, což je další metoda AO a *„není zdarma"*. Přepnutí na *stationary* ji vypne. Rozdíl je v prázdné scéně těžko vidět; ve scéně se stromy podle něj ano.

**Antialiasing: TSR proti TAA** [(18:01)](https://www.youtube.com/watch?v=S-vO9YNI7zs&t=1081s), a to je největší jednotlivá úspora ve videu: **TSR ~1,7 ms, TAA 0,15 ms.** Cena je pojmenovaná poctivě: TAA rozmazává v pohybu, takže se hodí *„na adventuru nebo něco pohodovějšího"* a nehodí na rychlou střílečku nebo závody. Mezistupeň pro stylizované a mobilní hry je **FXAA**.

**Screen percentage, které jsi nenastavil** [(21:55)](https://www.youtube.com/watch?v=S-vO9YNI7zs&t=1315s) je nejužitečnější položka, protože se týká **měření, ne výkonu**. UE5 má screen percentage ve výchozím stavu **„based on display resolution"**, což znamená, že se na vyšších rozlišeních tiše renderuje **pod 100 %**. Kdo o tom neví, srovnává dvě scény v různém rozlišení a neví o tom. Nastavuje se to na dvou místech v nastavení projektu (jedno pro hru, jedno pro editor) přepnutím na **manual** a hodnotu 100.

Sem patří i **temporal upscaling**: se zapnutým vypadá 80 % skoro jako 100, se vypnutým je i 80 % rozmazané. Autorovo doporučení nechat ho zapnutý a dát hráči posuvník — *„v mnoha hrách to tak je."*

**A rada, kterou měření nepotvrdilo** [(17:15)](https://www.youtube.com/watch?v=S-vO9YNI7zs&t=1035s). Přepne shadow map method z virtual shadow maps na klasické shadow maps s očekáváním úspory — a **framerate spadne**. Diagnóza, ke které dojde na kameře: *„aha, ta scéna je celá nanitová, takže shadow maps od ní čekají virtual shadow maps."* Vrátí to a dodá pravidlo, které z toho plyne: **je-li scéna nanitová, patří k ní virtuální stíny; není-li, patří k ní klasické.** Stejně tak Nanite se dá v nastavení projektu **vypnout úplně**, plánuješ-li nízkopolygonové meshe s LODy.

> **Pozn.:** Nejcennější je tady **struktura** té rady, ne jednotlivá čísla: každé vypnutí je spárované s náhradou. Bez toho páru vzniká to, co se v komunitě dobře pozná — scény, ze kterých někdo vypnul Lumen a diví se, že jsou šedivé a placaté. Za pozornost stojí i ta **nepotvrzená hypotéza s VSM**, protože ukazuje, že rozhodnutí o stínech není samostatné: **navazuje na to, jestli jsi nanitový** — a to je táž provázanost, kvůli které se [rozhodnutí o cílovém framerate](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) dělá na začátku. A screen percentage je vlastně pokračování [problému s výchozími hodnotami](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1): další nastavení, které je nastavené za tebe a rozhoduje o tom, co vlastně měříš. Vlastní výhrada k číslům: **13 ms ve výchozí třetí osobě je scéna o šesti kvádrech.** Úspory z tohohle videa se v hotové hře projeví jinak, protože tam už bude úzké hrdlo někde jinde — a to je důvod, proč se nejdřív měří.

**Souvislosti:** [Vlastní šablona projektu](#vlastni-sablona-projektu-nastaveni-jednou-a-navzdy) *(jak to udělat jen jednou)* · [Rozpočet snímku: prvních 16,66 ms](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Optimalizační průchod: Lumen](gpu-pruchod.md#lumen-rozpocet-a-binarni-hledani) · [Osvětlení](osvetleni.md) · [Rejstřík: Screen percentage](../rejstrik.md#screen-percentage) · [Rejstřík: TAA](../rejstrik.md#taa) · [Rejstřík: Distance field AO](../rejstrik.md#distance-field-ao) · [Rejstřík: Lumen](../rejstrik.md#lumen) · [Ze 100 na 200 FPS](#ze-100-na-200-fps-co-stalo-za-vypnuti-ve-skutecne-hre) *(totéž rozhodování ve skutečné hře)*

---

## Vlastní šablona projektu: nastavení jednou a navždy

**Zdroj:** [How To Create An Optimized UE5 Base Project](https://www.youtube.com/watch?v=2ZcagAT3EXQ) · [Smart Poly](https://www.youtube.com/channel/UCp1e34nrTQqVXkNU5ekH9CQ) · ~17 min, tutoriál

**Shrnutí:** Předchozí myšlenka je seznam nastavení, který bys musel proklikat u každého nového projektu. Tahle ho zavírá: **udělej ta nastavení jednou, zabal je jako vlastní šablonu enginu** a pak ji vybírej v okně „nový projekt" jako kteroukoli oficiální. Postup má jeden nečekaný krok a jednu poctivě přiznanou nedokonalost. Háček: **`.ini` nestačí, protože engine si část nastavení při vytvoření z šablony přepíše zpátky.**

### Rozpad myšlenky

**Nečekaný krok na začátku** [(1:34)](https://www.youtube.com/watch?v=2ZcagAT3EXQ&t=94s): založit prázdný projekt v **Unreal Enginu 4.27** a pak ho upgradovat na 5.7. Důvod je pragmatický a chytrý — *„protože v téhle verzi enginu ty funkce nebyly ani volba,"* takže pečené světlo, vypnutý ray tracing a nulové globální osvětlení jsou tam **výchozí stav**, ne něco, co musíš odklikat.

**Nastavení, která pak zbývají** [(5:31)](https://www.youtube.com/watch?v=2ZcagAT3EXQ&t=331s): global illumination *none*, reflection method *screen space*, shadow map method *shadow maps* (ne virtuální), ray tracing vypnutý. A jedno rozhodnutí, které stojí za samostatnou zmínku: **RHI na DirectX 11 a shader model 5** místo výchozího DX12. Zdůvodnění: *„s DirectX 11 není tolik problémů se sekáním a je optimálnější než DirectX 12."*

**A pak ta část, kvůli které to není jen klikání** [(7:50)](https://www.youtube.com/watch?v=2ZcagAT3EXQ&t=470s): nastavení z projektu se musí **zapsat do `DefaultEngine.ini`** — jinak se při vytvoření nového projektu ze šablony *„ray tracing zapne zpátky, všechny ty funkce se zapnou zpátky."* Tedy: šablona nedědí stav editoru, dědí konfigurační soubor.

**Registrace jako šablony** [(9:23)](https://www.youtube.com/watch?v=2ZcagAT3EXQ&t=563s) je mechanická, ale má pravidla, která se nedají uhádnout:

1. Do `Templates` v instalaci enginu nová složka s prefixem **`TP_`**.
2. Zkopírovat jen `Config`, `Content` a `.uproject` (zbytek jsou dočasné soubory).
3. **Projekt se musí jmenovat stejně jako složka.**
4. Z jiné šablony si vypůjčit `TemplateDefaults.ini` a přepsat v něm jméno, popis a **kategorii** (`Games`).
5. Do `Media` dvě ikony pojmenované podle projektu, druhá s příponou `_preview`.

**Nedokonalost, kterou autor přiznává** [(14:04)](https://www.youtube.com/watch?v=2ZcagAT3EXQ&t=844s) a je to nejcennější věta videa: po vytvoření projektu ze šablony **se část nastavení přesto vrátila** — shadow map method na virtual shadow maps (i s varováním, že to vyžaduje shader model 6), globální osvětlení zpátky na Lumen. *„Nejsem si jistý, proč se některá z těch nastavení resetují."* Doporučení, které z toho plyne: **po vytvoření projektu ta klíčová nastavení zkontroluj.**

Výsledek na jeho stroji: zabalený build **~900 FPS na 1080p**, s pečeným světlem a vypnutými funkcemi.

> **Pozn.:** Ten trik s 4.27 je nejlepší nápad ve videu, protože obchází celý problém místo aby ho řešil: **místo vypínání funkcí začni ve verzi, kde neexistovaly.** Zároveň je to poučný příklad toho, jak se výchozí hodnoty hromadí — engine je neubírá, jen přidává, takže „prázdný projekt" znamená v každé verzi něco jiného. Praktická výhrada, kterou video nemá: **šablona v instalaci enginu je lokální věc.** Nepřežije reinstalaci enginu, nesdílí se s týmem a při upgradu na další verzi ji musíš přenést — takže jako týmové řešení je lepší mít [ten `.ini` v repozitáři projektu](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) a šablonu brát jako osobní pohodlí. A k DX11 patří výhrada: platí to pro projekt, který se dobrovolně zbavil DX12 funkcí. Chceš-li kdykoli později hardware ray tracing, Nanite nebo MegaLights, je to cesta, ze které se hůř vrací.

**Souvislosti:** [Rozpad ceny výchozí scény](#rozpad-ceny-vychozi-sceny-a-cim-ji-nahradit) *(co do té šablony patří)* · [Fork jako krajní varianta](#fork-jako-krajni-varianta) · [Rozpočet snímku: prvních 16,66 ms](rozpocet-snimku.md#prvnich-1666-ms-se-rozdava-v-cl1) · [Organizace projektu](organizace-projektu.md#content-browser-podle-epicu-feature-foldery-developers-a-redirectory) · [Rejstřík: Device profile](../rejstrik.md#device-profile) · [Rejstřík: Scalability groups](../rejstrik.md#scalability-groups)

---

## Fork jako krajní varianta

**Zdroj:** [The Most Optimized Version of UE5??? (The ViteFork)](https://www.youtube.com/watch?v=dRR5AC8PV2U) · [Smart Poly](https://www.youtube.com/channel/UCp1e34nrTQqVXkNU5ekH9CQ) · ~14 min, zpráva o komunitním projektu

**Shrnutí:** Nejkrajnější odpověď na otázku „co když UE5 funkce nechci" je **použít jinou verzi enginu**. Video představuje komunitní fork postavený na starší Nvidia RTX větvi, který si dal za cíl **2,5× vyšší FPS než 5.7** — s ray traced globálním osvětlením místo Lumenu a se vrácenou starou fyzikou. Zpracováváme to jako **orientaci v krajině, ne doporučení**, protože jde o software, který si musíš zkompilovat, a čísla jsou od autorů forku. Háček, který rozhoduje: **je to jednosměrná cesta.**

### Rozpad myšlenky

**Kontext, který dává smysl celému projektu** [(2:23)](https://www.youtube.com/watch?v=dRR5AC8PV2U&t=143s). Epic míří v 5.6 na *60 FPS v nativním 1080p na PS5* — a autoři forku tvrdí, že *„aby se tam dostal, obětuje stabilitu a celkovou kvalitu obrazu,"* a že u hardwaru jako Switch 2 nebo případný přenosný PS6 ten cíl nestačí. Motivace je tedy „chceme jinou cílovou platformu", ne „Epic to umí špatně".

**Na čem stojí** [(4:47)](https://www.youtube.com/watch?v=dRR5AC8PV2U&t=287s): na **NvRTX 5.0.3**. Volba té staré verze má věcné vysvětlení, které je samo poučné — *„od 5.1 se renderovací pipeline, zvlášť ray tracing, začala víc a víc proplétat s Lumenem, Nanitem, virtuálními stíny a TSR,"* takže z novějších verzí se ray tracing nedá vyndat. Verze 5.0 je *„blíž Unreal Enginu 4 než dnešní verzi enginu."*

**Co v tom je** (podle autorů forku a promo materiálů):

- **DDGI** — ray traced globální osvětlení jako alternativa Lumenu; v testech *„téměř dvojnásobný framerate proti Lumenu"* a *„běží dobře i na AMD hardwaru"*.
- **Vrácená stará fyzika** místo Chaosu, s tvrzením o **25 %** lepším čase na dotaz a **dvojnásobku** na simulaci těles.
- **RTXDI** jako obdoba MegaLights, **Apex Destruction**, experimentální **tessellation** ve vlastní větvi.
- **~950 MB méně paměti** v průměru na scénu než 5.6.
- **Asset downgrader**, který umí projekt sundat z 5.7 zpátky na 5.0.

**Demo čísla** [(10:58)](https://www.youtube.com/watch?v=dRR5AC8PV2U&t=658s): ~700 FPS na RTX 4090 ve 4K, a na Steam Decku (varianta se statickým GI) *„kolem 90 FPS."* Autor u toho dodá to, co ta čísla relativizuje: demo **nemá žádný antialiasing**, takže *„si všimneš hodně ostrých hran."*

**Cena vstupu**, kterou video zmiňuje mimochodem a je zásadní: potřebuješ **propojený GitHub a Epic účet** kvůli přístupu ke zdrojovým kódům, **Visual Studio** a musíš si engine **zkompilovat**. Autor sám na konci přiznává, že fork ještě nepostavil a slibuje k tomu samostatné video.

> **Pozn.:** Tuhle položku bereme jako **doklad, že ten spor existuje a je věcný**, ne jako radu. Nejzajímavější informace v celém videu není žádné číslo, ale ta věta o **proplétání**: od 5.1 jsou Lumen, Nanite, VSM a TSR provázané tak, že se ray tracing nedá izolovat — což vysvětluje, proč fork stojí na tři roky starém základu, a zároveň říká něco obecného o **enginu jako balíčku rozhodnutí**: nové verze nepřinášejí jen funkce, ale i závislosti mezi nimi. Kde je tenhle zdroj slabý, je potřeba říct nahlas: **všechna čísla jsou od autorů forku**, autor videa je nezopakoval, demo je bez antialiasingu (což samo o sobě šetří milisekundy) a ~700 FPS na 4090 nevypovídá o ničem. A hlavně — je to volba, ze které se nedá odejít: **zůstáváš na základu 5.0.3 bez Epicových oprav, bez novějších funkcí a bez záruky, že fork bude někdo udržovat.** Pro hru, která má vyjít za tři roky, je to riziko jiného řádu než jakákoli optimalizace.

**Souvislosti:** [Vlastní šablona projektu](#vlastni-sablona-projektu-nastaveni-jednou-a-navzdy) *(mírnější varianta téhož záměru)* · [Nanite do hloubky: spor o Nanite](nanite-do-hloubky.md#spor-o-nanite-co-tvrdi-kritika-a-co-z-toho-plati) *(týž spor, jiný hlas)* · [Optimalizační průchod: Lumen](gpu-pruchod.md#lumen-rozpocet-a-binarni-hledani) · [Rejstřík: Lumen](../rejstrik.md#lumen) · [Rejstřík: MegaLights](../rejstrik.md#megalights)

---

## Ze 100 na 200 FPS: co stálo za vypnutí ve skutečné hře

**Zdroj:** [How I Optimized My Game to Over 200 FPS in UE5](https://www.youtube.com/watch?v=xr-2TrMUd9w) · [Procedural Minds](https://www.youtube.com/channel/UCkfvcZJ6dGNUSCWOCVQnkXw) · ~23 min, devlog (sólo hra ve fázi prototypu)

**Shrnutí:** Sólo vývojář vezme svou stylizovanou hru ze zhruba 100 FPS na 200+ (RTX 4080, 1440p) a ukáže, kde to bylo. Nejcennější je, že **dvě z největších položek nebyly nic, co by hra potřebovala**: TSR počítal upscaling, i když se nic neupscalovalo, a screen space GI svítilo ve hře, která globální osvětlení vědomě nechce. Háček: obojí se v GPU profileru schovává pod jiným jménem (post-processing, deferred lighting), takže to najde jen ten, kdo položky rozbalí.

### Rozpad myšlenky

**Jak hledat** [(1:37)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=97s): `profile GPU` (Ctrl+Shift+,), seřadit podle milisekund a rozbalovat. A měřit víckrát — jeden snímek kolísá a sám nic nedokazuje [(4:43)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=283s).

**TSR jako pouhý anti-aliasing** [(2:24)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=144s): post-processing stál 2,9 ms a přes 2 ms z toho TSR — při nativním rozlišení, kde se „převádí" z 1440p na 1440p. TSR nastavený jen jako AA podle autora pořád dělá výpočty upscalingu. Přepnutí metody v Project Settings (výchozí i mobilní) na TAA srazilo položku na 0,13 ms [(3:11)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=191s), [(3:57)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=237s) — podobný poměr, jaký [rozpad výchozí scény](#rozpad-ceny-vychozi-sceny-a-cim-ji-nahradit) naměřil v prázdné šabloně (TSR ~1,7 ms, TAA 0,15 ms), tentokrát ve hře s obsahem. Dvě poznámky navíc: pozor na menu nastavení, které může mít TSR jako vlastní výchozí volbu; a nemusí to být TAA — vyber metodu a změř ji. TSR zůstal hráčům k dispozici v nastavení [(4:43)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=283s).

**Lumen a Nanite: vypnout, ale celé** [(5:29)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=329s): stylizovaná, malířsky stínovaná hra s nízkopolygonovou geometrií Lumen nepotřebuje a z Nanitu nic nemá — a Nanite má **minimální základní cenu**, kterou tady jeho přínos nevyvážil [(6:17)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=377s). Detail, který rozhoduje: nestačí vypnout Nanite na assetech, musí se vypnout i v nastavení projektu [(7:04)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=424s). Autor přitom výslovně říká, že u realistické AA/AAA hry by oba systémy nejspíš nechal — není to rada proti nim, ale proti jejich nevědomému zapnutí.

**SSGI, o kterém nevěděl** [(7:51)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=471s): v *deferred lighting → diffuse & indirect AO* sedělo screen space GI za 0,9 ms (jinde až 1,9 ms), přestože Lumen byl vypnutý a GI hra nechtěla. `r.SSGI.Quality 0` ho vypne [(8:37)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=517s); scéna ztmavne, ale na původním záběru byl rozdíl sotva znát [(9:25)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=565s), a fill se dorovná intenzitou skylightu spolu s AO [(10:12)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=612s).

**Co přineslo málo** [(20:20)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=1220s): actor pooling nepřinesl skoro nic — jednotky FPS ztracené v kolísání. Velké položky byly čtyři: TSR, SSGI, cena widgetů s health bary nad nepřáteli a [Niagara](niagara-vykon.md#diagnostika-niagary-pet-statistik-a-jedna-past).

> **Pozn.:** Nejpoučnější je princip, kterým autor celé video rámuje [(0:50)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=50s): některé kroky platí pro každý projekt, jiné jen pro jeho styl — a **rozhodnout se má vědomě**. Tím doplňuje [rozpad ceny výchozí scény](#rozpad-ceny-vychozi-sceny-a-cim-ji-nahradit): tam se systémy vypínají v prázdné šabloně, tady v hře, která už má vlastní obsah, a vyjdou jiné položky (SSGI tam nebylo). Obě videa se shodnou na tom, že po vypnutí přichází **náhrada**, ne smíření s horším obrazem — skylight a AO místo GI. Čísla jsou z RTX 4080 a z prototypu a autor sám říká, že víc teď optimalizovat nemá smysl [(21:06)](https://www.youtube.com/watch?v=xr-2TrMUd9w&t=1266s). To je správné načasování: velké páky na začátku, jemné ladění až s obsahem.

**Souvislosti:** [Rozpad ceny výchozí scény](#rozpad-ceny-vychozi-sceny-a-cim-ji-nahradit) · [Vlastní šablona projektu](#vlastni-sablona-projektu-nastaveni-jednou-a-navzdy) *(kam tahle nastavení uložit)* · [Spor o Nanite](nanite-do-hloubky.md#spor-o-nanite-co-tvrdi-kritika-a-co-z-toho-plati) · [Niagara: diagnostika](niagara-vykon.md#diagnostika-niagary-pet-statistik-a-jedna-past) · [Rejstřík: TSR](../rejstrik.md#tsr) · [Rejstřík: TAA](../rejstrik.md#taa)
