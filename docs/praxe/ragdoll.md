# Ragdoll: od přepínače po seamless návrat

Ragdoll je na první pohled checkbox — a na druhý celá disciplína: aby tělo padalo věrohodně, potřebuje vyladěný **physics asset**; aby se dalo ovládat pádem, **motory řízené rychlostí**; a aby z něj postava vstala bez střihu, **pose snapshot** a detekci polohy. Kapitola skládá zdroje od minutového základu po kompletní systém nad GASP. Nejnovější je fyzika postav z GASP 5.8: **profily Physics Control** místo čísel v Blueprintu, ragdoll, který **se chrání** díky pózám z animace, a **vstávání vybrané motion matchingem**. Ragdoll po zásahu projektilem už ukázaly [základy AI](ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh); tady jde o plnou smyčku tam a zpět.

---

## Ragdoll za minutu: preset, simulace, kamera

**Zdroj:** [Unreal Engine 5 Tutorial - Ragdoll](https://www.youtube.com/watch?v=ZHgnfFj7pco) · [The Real Unreal](https://www.youtube.com/channel/UC0is_44ph-5eC-K1uImsoRA) · ~4 min, tutoriál

**Shrnutí:** Minimální ragdoll = tři uzly: mesh na **collision preset „Ragdoll"**, `Set Simulate Physics` true a `Disable Movement` na character movementu [(0:54)](https://www.youtube.com/watch?v=ZHgnfFj7pco&t=54s). Předpoklad je existující [physics asset](../rejstrik.md#physics-asset) — UE manekýn má `PA_Mannequin` z krabice [(0:08)](https://www.youtube.com/watch?v=ZHgnfFj7pco&t=8s).

### Rozpad myšlenky

Bez presetu „Ragdoll" simulace nefunguje správně — nastavuje objektový typ a odpovědi kanálů tak, jak je fyzikální tělo čeká. Čtvrtý krok, na který se zapomíná: **kamera**. Camera boom zůstal na kapsli, která po zapnutí simulace stojí na místě — `Attach Component to Component` ho přepne na mesh se socketem `pelvis`, a `Do Collision Test` off zabrání kolizím s vlastním tělem [(2:22)](https://www.youtube.com/watch?v=ZHgnfFj7pco&t=142s), [(2:42)](https://www.youtube.com/watch?v=ZHgnfFj7pco&t=162s).

> **Pozn.:** Tohle je „ragdoll na smrt" — jednosměrka. Všechno ostatní v téhle kapitole řeší, jak z něj udělat obousměrný stav. Ale pro nepřátele, kteří vstávat nemusí, je tahle minutová verze plus kolizní úpravy z [AI kapitoly](ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh) (kapsle No Collision po smrti!) všechno, co potřebuješ.

**Souvislosti:** [Základy AI: ragdoll po zásahu](ai-zaklady.md#minimalni-nepritel-pawn-sensing-ai-moveto-a-nav-mesh) · [Rejstřík: physics asset](../rejstrik.md#physics-asset) · [Rejstřík: collision preset](../rejstrik.md#collision-preset) · [Smrt jako ragdoll z komponenty](souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave) *(kolize Query and Physics a kapsle ignorující pawny)*

---

## Physics asset: těla, constrainty a triky z ALS

**Zdroj:** [UE5 Ragdoll Deep Dive Guide](https://www.youtube.com/watch?v=ZpcOYg1Qfm4) · [frinky](https://www.youtube.com/channel/UCepxYGyRNUXgqve42r60q8g) · část 1 ·
[UE5 Ragdoll Physics Tutorial (Complete Guide)](https://www.youtube.com/watch?v=R5o2CjPb3Tk) · [LocoDev](https://www.youtube.com/channel/UCr8NttLeGyLd6m4qVS2Zb8g) · úvodní část

**Shrnutí:** Physics asset = **těla** (kolizní primitiva per kost — koule, kapsle, kvádry) + **constrainty** (kloubové limity: swing 1/2 a twist) [(0:51)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=51s), [(3:12)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=192s). Defaultní assety manekýnů jsou pro ragdoll **nedoladěné** — končetiny se kroutí nevěrohodně [(8:21)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=501s). Frinky dodává sadu úprav vykoukanou z ALS, které z „hadru" udělají tělo.

### Rozpad myšlenky

**Jak si constrainty osahat:** vybrat constraint → `Simulate Selected` a tahat myší [(4:01)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=241s) — hned vidíš, co který limit (Locked/Limited/Free na swing/twist) dělá. `Angular Drive Mode: Twist and Swing` znamená, že se kloub po puštění **vrací do přirozené pózy** [(5:34)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=334s) — základ „aktivního" chování.

**ALS recept (frinky):**

1. Select All Constraints → drive mode **Twist and Swing**, zaškrtnout všechny čtyři motory, `Target Velocity Strength` = 1 [(3:38)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=218s).
2. **Výjimka pelvis**: motory vypnout, drive mode zpět na SLERP — pánev nesmí tahat tělo za animací, jinak se ragdoll „vzpírá" [(4:25)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=265s). U chodidel vypnout target velocity.
3. Všechna těla: **Angular Damping 15** (hodnota z ALS) [(5:11)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=311s).
4. **Kinematic root body**: root kost defaultně tělo nemá — a mesh se při simulaci od parenta *odpojí*. Root → Add Shape (malá koule) → Physics Type **Kinematic** [(5:59)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=359s). DK 3D variantu doplňuje o constraint root↔pelvis s linear limity Free a **vypnutou kolizní odpovědí** root těla — jinak se ragdoll hádá s terénem [(4:58)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=298s), [(5:46)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=346s).

**Kolize tělo × tělo:** defaultně končetiny prochází skrz sebe — vybrat dvojici tvarů → `Enable Collision` (typicky nohy, paže × trup) [(11:11)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=671s).

> **Pozn.:** Kinematic root má druhý, nenápadný účel (LocoDev): za ragdollu se **actor velocity nepočítá** — rychlost těla čteš z root/pelvis kosti (`Get Physics Linear Velocity`), a právě na ní stojí všechno ladění v další myšlence [(16:25)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=985s). LocoDev k videu přikládá dokument s kompletními hodnotami limitů pro UEFN manekýna [(10:25)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=625s) — rychlejší než ladit od nuly.

**Souvislosti:** [Rejstřík: physics asset](../rejstrik.md#physics-asset) · [Rejstřík: physics constraint](../rejstrik.md#physics-constraint) · [Rejstřík: ALS](../rejstrik.md#als)

---

## Active ragdoll: motory řízené rychlostí

**Zdroj:** [How to Make an Active Ragdoll (like Gang Beasts)](https://www.youtube.com/watch?v=l4nfL9RHcA4) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~7 min ·
[UE5 Ragdoll Deep Dive Guide](https://www.youtube.com/watch?v=ZpcOYg1Qfm4) · [frinky](https://www.youtube.com/channel/UCepxYGyRNUXgqve42r60q8g) · část 2 ·
[UE5 Ragdoll Physics Tutorial (Complete Guide)](https://www.youtube.com/watch?v=R5o2CjPb3Tk) · [LocoDev](https://www.youtube.com/channel/UCr8NttLeGyLd6m4qVS2Zb8g) · blueprint část (nad GASP, 5.5)

**Shrnutí:** Active ragdoll = tělo simuluje fyziku, ale **motory kloubů ho táhnou k animaci** (Gang Beasts, Human Fall Flat). Dvě páky: **Physical Animation Component** (síla, s jakou se kosti drží animované pózy) a **angular drive motory** z physics assetu — a nejlepší trik batche: obě řídit **rychlostí těla**. Letící tělo je tuhé a drží tvar, ležící tělo je hadr.

### Rozpad myšlenky

**Základ (Gorka):** Physical Animation Component → BeginPlay `Set Skeletal Mesh Component` → `Apply Physical Animation Settings Below` od **pelvis** (první kost po rootu; jiné skelety „hips") [(2:22)](https://www.youtube.com/watch?v=l4nfL9RHcA4&t=142s) s `Make Physical Animation Data`: orientation strength ~1000, angular velocity ~100, position ~1000, velocity ~100 [(3:08)](https://www.youtube.com/watch?v=l4nfL9RHcA4&t=188s). K tomu `Set All Bodies Below Simulate Physics` a kolize: mesh preset **Pawn**, kapsle **ignoruje Pawn** [(4:44)](https://www.youtube.com/watch?v=l4nfL9RHcA4&t=284s).

**Checkbox, který šetří hodiny (frinky):** na meshi **`Update Joints from Animation`** — bez něj ragdoll **T-pózuje** [(15:17)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=917s). Vstup do ragdollu jinak klasika: kapsle bez kolize, movement None, mesh objektový typ Physics Body + query and physics, simulate below pelvis [(16:03)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=963s); frinky navíc přepíná **input mapping contexty** (default ↔ ragdoll s vlastními akcemi) [(14:30)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=870s) a drží stav v pure util funkci `Is Simulating Physics(pelvis)` [(10:40)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=640s).

**Rychlost → tuhost:** v update smyčce `Set All Motors Angular Drive Params` se **spring** mapuje z délky rychlosti pánve: frinky 0–500 → 500–5000 [(22:17)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=1337s), LocoDev 0–1000 → 1000–2800 [(21:26)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1286s). Efekt: při letu tělo drží pózu (stabilizuje se po nárazu, líp se pak blenduje vstávání [(21:51)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1311s)), po dopadu zplihne. LocoDev stejným mapováním řídí i **per-řetěz síly** (`Apply Settings Below` zvlášť pro spine_05, stehna, ruce) [(27:25)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1645s) — simulace od kosti níž zasahuje jen její hierarchii [(25:07)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1507s).

**Kapsle za tělem:** každý frame `Set Actor Location and Rotation` ← socket transform pelvis, +90 Z (kapsle nad zemí), z rotace **jen yaw** [(18:22)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=1102s); camera lag na boomu vyhladí zbytek [(19:11)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=1151s). LocoDev přidává vypnutí gravitace při pádu rychlejším než −4000 (proti nekonečné akceleraci a propadům podlahou) [(28:59)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=1739s).

> **Pozn.:** LocoDev staví nad [GASP](gasp.md) a narazil na tvrdou verzní past (5.5): kombinace Physical Animation komponenty a simulace **mrazí engine**, dokud se na BeginPlay GASP postavy neodpojí uzel `Add Tick Prerequisite Component` [(36:32)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=2192s) — přesně ten typ „proč mi to padá" zádrhelu, který stojí za zápis. Hodnoty všech mapování ber jako startovní: oba autoři přiznávají, že čísla vyladili iterováním na vlastních animacích.

**Souvislosti:** [GASP](gasp.md) · [Rejstřík: physical animation component](../rejstrik.md#physical-animation-component) · [Rejstřík: physics asset](../rejstrik.md#physics-asset) · [Fyzika v Control Rigu při animování](animace-nastroje.md#sekundarni-pohyb-v-control-rigu-dynamics-za-behu-fyzika-a-autobake-pri-animovani) *(ragdoll časovaný v sequenceru a zapečený)*

---

## Physics Control profily: hra řekne „ragdoll", čísla bydlí v assetu

**Zdroj:** [The Last GASP!? Game Animation Sample Updates for 5.8 + Q&A | Inside Unreal](https://www.youtube.com/watch?v=6NYC4ryO9ik) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~2 h 47 min, stream k 5.8 updatu GASP (úsek programátora fyziky postav) ·
[Unreal Engine Just Got AAA Animation Physics (Game Animation Sample 5.8)](https://www.youtube.com/watch?v=UP3zWCMPn3E) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~8 min, přehled updatu

**Shrnutí:** Fyzikální postava v GASP 5.8 má několik režimů:
- kinematický, kdy jen sleduje animaci,
- physical animation, kdy animaci sleduje, ale dá se do ní strčit,
- ragdoll, který není mrtvý, protože ho klouby dál táhnou k póze.

Herní logika mezi nimi přepíná jediným voláním `Invoke Control Profile` se jménem profilu, bez jediného čísla v Blueprintu. Čísla bydlí v Physics Control assetu. Ten nad physics assetem ragdollu definuje končetiny, pro každé tělo tři druhy ovládání a z nich sady a profily. Háček: výsledek je jen tak dobrý jako physics asset pod ním. Ovládání mu dává život, ale ne kolize a limity kloubů.

### Rozpad myšlenky

**Režimy.** Když postava běhá, sleduje animaci skoro přesně, ale fyzika běží dál. Překážka jí odtlačí ruku, protože se o ni postava opravdu srazí [(1:04:07)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=3847s). Silnější náraz ji pošle do ragdollu, který simuluje volně, ale dál ho táhne k pózám, třeba k natahování rukou [(1:04:53)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=3893s). Motory na kloubech, lineární i úhlové, tlačí a tahají kostru i během simulace, takže postava pádu vzdoruje, místo aby jen zplihla [(2:22)](https://www.youtube.com/watch?v=UP3zWCMPn3E&t=142s).

**Hra mluví ve jménech.** Herní logika má s fyzikou mluvit na střední až vyšší úrovni, ne nastavovat vlastnosti jednotlivých těles [(1:05:40)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=3940s). Profil je proto předvolba všech fyzikálních a řídicích nastavení s čitelným jménem: ragdoll, physical animation, kinematic, nebo držení něčeho v rukou [(1:06:29)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=3989s). Volá se `Invoke Control Profile` na Physics Control komponentě a v herním kódu není žádné číslo [(1:07:15)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4035s). Ragdoll profil nechá simulovat všechna tělesa s gravitací a některé klouby dál táhne k cílové animaci, aby postava nebyla úplně mrtvá. Kinematický jen sleduje animaci a odstrkuje ostatní. Physical animation animaci sleduje, ale dá se odstrčit [(1:08:01)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4081s).

**Asset nad physics assetem.** Nastavení komponenty je v Physics Control assetu, oddělené od logiky [(1:08:01)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4081s). Jeho editor je jednoduchý a programátor přiznává, že v něčem není úplně hotový [(1:08:48)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4128s). Ragdoll sám asset nestaví, odkazuje na physics asset. Ten musí být dobrý: žádné nechtěné kolize se sebou samým a pečlivé limity kloubů, protože výsledek nebude lepší než výchozí fyzikální setup [(1:09:34)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4174s). Programátor to přirovnává k loutce: marioneta bez vodítek spadne na zem a teprve ovládání jí dá život [(1:10:21)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4221s).

**Tři druhy ovládání.** Od základů je vysvětluje level Animation Physics Control v projektu Content Examples na Fabu [(1:11:08)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4268s).
- **Body modifier** mění vlastnosti jednotlivých těles: jestli simulují, nebo jsou kinematická, jestli na ně působí gravitace a jestli kolidují [(1:11:54)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4314s).
- **World-space control** táhne těleso k cíli ve světě, měkce a pružně, nebo tlumeně a silně [(1:12:42)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4362s).
- **Parent-space control** řídí těleso vůči rodiči v hierarchii, třeba předloktí vůči paži, podobně jako svaly. Je realistický, ale koordinovaný pohyb z něj dostaneš těžko. Housenka se s ním plazí, ale postava nechodí, protože jí chybí jemná motorika na udržení rovnováhy [(1:13:29)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4409s), [(1:15:02)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4502s).

Příklad visení na římse ukazuje, k čemu je fyzika ve hře: simulovaná postava nemá zapnutou gravitaci, jinak by se prověsila a natáhla ruce. Měkké ovládání ji rozhoupe tak, že to jako visení pod vlastní vahou jen vypadá [(1:15:48)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4548s).

**Končetiny, sady, profily.** Postava se rozdělí na končetiny. Levá ruka je třeba všechno pod levou klíční kostí a každé těleso v ní dostane world-space control, parent-space control a body modifier [(1:16:34)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4594s), [(1:17:21)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4641s). Ovládání se řadí do sad, například „all", „arm_r", nebo vlastní „feet", protože při chůzi chceš obě chodidla kinematická [(1:18:09)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4689s). Profily pak sady nastavují [(1:18:56)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4736s):
- kinematický přepne sadu „all" na kinematickou a vypne všechna ovládání [(1:19:42)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4782s),
- ragdoll nechá všechno simulovat s gravitací 1, vypne world-space controls a zapne parent-space controls s nějakou silou [(1:20:30)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4830s).

V editoru jde profily rovnou simulovat a ladit, slabší, silnější nebo pružnější, jako na pískovišti [(1:22:04)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=4924s).

**Za běhu.** Profil se zavolá jménem [(1:23:36)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5016s) a jde ho omezit maskou končetin: zásah do ruky pošle na pár sekund do ragdollu jen tu ruku [(1:24:24)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5064s). Po aplikaci se dá dál dolaďovat jednotlivými funkcemi komponenty, třeba silou [(1:25:11)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5111s). Ragdoll postava v GASP běhá ve výchozím stavu v physical animation profilu, takže se rukama srazí s ostatními. Většina her ale postavu drží v kinematickém. Třeba držená zbraň by si s fyzikou rukou vyžádala další constrainty [(1:26:06)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5166s), [(1:26:53)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5213s).

> **Pozn.:** Physics Control je obecnější nástroj než [Physical Animation Component s motory](#active-ragdoll-motory-rizene-rychlosti) výš. Funguje na libovolných tělesech, a stejná komponenta proto drží i [vor na vodě](lana-kabely.md#physics-control-vor-ktery-se-houpe-pod-nohama). Profily navíc vyřeší, co ruční přístup nechával na Blueprintu: kde a jak nastavovat čísla. Gorka Games k tomu přidává rozumné shrnutí, že jeden asset unese úplně jiné fyzikální chování pro ránu pěstí a pro pád z budovy [(3:09)](https://www.youtube.com/watch?v=UP3zWCMPn3E&t=189s). Jeho video ale v téže chvíli láká na placené individuální konzultace. A pozor: komponenta je pořád experimentální [(7:01)](https://www.youtube.com/watch?v=UP3zWCMPn3E&t=421s).

**Souvislosti:** [Rejstřík: Physics Control](../rejstrik.md#physics-control) · [Rejstřík: Physics Asset](../rejstrik.md#physics-asset) · [Rejstřík: Ragdoll](../rejstrik.md#ragdoll) · [Data asset jako oddělení dat od logiky](../rejstrik.md#data-asset)

---

## Ragdoll, který se chrání: pózy z animace, síla z křivek a čas do dopadu

**Zdroj:** [The Last GASP!? Game Animation Sample Updates for 5.8 + Q&A | Inside Unreal](https://www.youtube.com/watch?v=6NYC4ryO9ik) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~2 h 47 min, stream k 5.8 updatu GASP (úsek technického designéra a Q&A)

**Shrnutí:** Ragdoll v GASP nepůsobí jako hadrová panenka, i když běží čistá fyzika. AnimBP mu za běhu podsouvá pózy:
- rozhazování rukama ve vzduchu,
- natažené ruce těsně před dopadem,
- schoulení na zemi podle toho, jak leží,
- zranění, třeba držení se za obličej nebo omráčení.

Sílu, kterou ho klouby k póze táhnou, berou z křivek v animaci. Háček: celé „vědomí" postavy je pár blend spaců a póz a zbytek udělá fyzika. Protože jde jen o pózy, nestojí jejich výroba skoro nic.

### Rozpad myšlenky

**Vstup do ragdollu.** Ukázková postava je potomek Mover postavy a všechno je obyčejný Blueprint, ze kterého se má učit a který se má přenést do vlastních systémů [(1:27:39)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5259s), [(1:28:25)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5305s). Událost `Trigger Ragdoll` zastaví běžící montáže, nastaví stav zranění a vyvolá profil [(1:29:12)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5352s). Je v tom past: profil se uplatní až při další aktualizaci Physics Control komponenty. Impulz, třeba od kulky, poslaný hned po spuštění ragdollu by se ztratil, pokud mesh ještě nesimuluje. Proto se simulace zapne napřed ručně a profil se zařadí až po ní [(1:30:00)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5400s), [(1:30:46)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5446s).

**Nohy se nesmějí zamotat.** Novinkou je, že kolize mezi částmi těla jdou měnit za běhu [(1:31:32)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5492s). V kinematickém a physical animation profilu jsou kolize mezi nohama vypnuté, protože by se jinak při běhu zamotávaly, a constraint profil je nastavený na volný, bez limitů. V ragdollu se kolize nohou vrátí a s nimi i výchozí limity kloubů [(1:32:19)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5539s).

**Kapsle za pánví.** Ragdoll má vlastní pohybový mód v Moveru, napsaný v Blueprintu. Kapsle v něm sleduje polohu pánve, kterou dostává jako vlastní vstup, a drží se nad zemí, aby se nezabořila [(1:32:19)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5539s), [(1:33:06)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5586s). Když mají vstávací animace kořenovou kost pod pánví, je přechod plynulý [(1:33:52)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5632s). Mover ale tiká na začátku snímku, takže zařazený mód začne platit až v dalším snímku a ve vzácném případě se do něj postava nedostane. Snímek nato se proto zkontroluje, jestli je opravdu v ragdoll módu, a pokud ne, profil se vrátí [(1:34:40)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5680s), [(1:35:27)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5727s). Rotace kapsle sleduje páteř a pánev, takže podle toho, jestli postava leží na zádech, nebo na břiše, je kapsle otočená tam, kam se bude vstávat. Při vstupu do ragdollu se ale pár snímků divoce točí, a proto se na tu chvíli zmrazí [(1:36:14)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5774s).

**Hlídání okolí.** Mimo ragdoll trace uvnitř postavy hlídá překážky na vlastním kolizním kanálu. Zásah překážkou spustí ragdoll, kdežto letmý dotyk jen odstrčí ruku nebo hlavu [(1:37:02)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5822s). V ragdollu působí na svahu moment, takže se postava sama skutálí z kopce. Hlavně se ale trasuje směr a čas do dopadu [(1:37:49)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5869s), [(1:38:35)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5915s).

**Pózy.** V AnimBP je stavový automat pro ragdoll pózy a návrat, do kterého se vstupuje podle pohybového módu [(1:40:10)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6010s).
- Když je do dopadu víc než půl sekundy, hraje blend space rozhazování rukama podle natočení těla [(1:40:57)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6057s). Animátor ho natočil sám, vsedě na židli ve své garáži [(1:41:44)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6104s).
- Těsně před dopadem přejde do blend spacu natahování rukou směrem k místu dopadu, i s prsty. Postava pak vypadá, že vnímá okolí a chrání se [(1:41:44)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6104s), [(1:42:31)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6151s).
- Na zemi má pózy podle toho, jestli leží na břiše, na zádech, nebo na boku. Fyzika je nekopíruje přesně, ale jemně postavu zklidní [(1:42:31)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6151s). Bez nich končí ragdoll v podivných zkroucených polohách [(1:43:17)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6197s).
- Při kutálení hrají pózy pro válení podle míry otáčení [(1:44:50)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6290s).

První verze byla prý „hodně Dark Souls": bezvládný hadr. Animátor proto visel v garáži na bedně od jablek a zkoumal, co při ztrátě rovnováhy dělají ruce a ramena. S tím působí pád mnohem brutálněji, ruce jdou dopředu a tělo se zhroutí [(1:43:17)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6197s), [(1:44:04)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6244s).

**Síla z křivek.** I v jediném ragdoll profilu chceš, aby některé pózy držely klouby pevněji než jiné [(1:39:21)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=5961s). Uzel `Modify Curve` proto přidá do výstupu animace křivky, které násobí sílu motorů kloubů, a každá póza zranění má jinou [(1:44:50)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6290s). Omráčená postava ztuhne a zvedne ruce, jako by ji zasáhl taser [(1:45:38)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6338s). Bezvládná jen zplihne. Profil je pořád stejný, mění se jen síla [(1:46:24)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6384s). Ragdoll a stav zranění spouští při takedownu notify v montáži zasaženého. Stačí posunout notify nebo změnit zranění a chování je úplně jiné [(1:58:57)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=7137s), [(1:59:43)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=7183s).

**Co se nepovedlo: síť.** Replikovaný ragdoll se tým snažil do projektu dostat. Vlastník měl posouvat kapsli k ragdollu, poloha kapsle se replikuje a u ostatních klientů by síla táhla lokálně simulované tělo k replikované kapsli [(2:27:17)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=8837s). Pozdní změna v Moveru ale při korekci polohy kapsle teleportuje i fyziku připojených komponent. Vznikla katastrofální zpětná vazba a replikace se do projektu nedostala. Tým se k ní chce vrátit [(2:28:04)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=8884s).

> **Pozn.:** Proti [aktivnímu ragdollu s rychlostí](#active-ragdoll-motory-rizene-rychlosti) je tu tuhost autorská: neurčuje ji rychlost těla, ale křivka v póze, kterou nakreslí animátor. Oba přístupy mají společné to podstatné. Ragdoll potřebuje něco dělat, jinak je to jen padající hadr. Mrtvola, která odlétne a zůstane ležet, je přitom sama o sobě čitelná zpětná vazba, jak připomíná [katalog juice](../teorie/game-feel.md#katalog-juice-deset-detailu-ktere-prodavaji-tutez-mechaniku). Křivky, které z animace řídí něco mimo ni, zná knihovna i z [interakcí](interakcni-animace.md#animace-ridi-svet-normalizovane-krivky-v-montazi). Proč je replikace fyzikální postavy těžká, rozebírá [síťová fyzika v Moveru](mover.md#sitova-fyzika-zevnitr-snimky-misto-casu-resimulace-a-input-decay).

**Souvislosti:** [Rejstřík: Ragdoll](../rejstrik.md#ragdoll) · [Rejstřík: Animation curve](../rejstrik.md#animation-curve) · [Rejstřík: Blend Space](../rejstrik.md#blend-space) · [Terč: smrt jako ragdoll](souboj.md#terc-smer-rany-zdravi-a-smrt-bez-radku-v-postave) *(jednoduchá verze bez póz)*

---

## Vstávání: pose snapshot, front/back a auto-recovery

**Zdroj:** [Advanced Seamless Ragdoll mode enter/exit](https://www.youtube.com/watch?v=-mHfpyBn_UQ) · [DK 3D](https://www.youtube.com/channel/UC3fGhbgSpR2BSSeTls3R6Sg) · ~53 min ·
[UE5 Ragdoll Deep Dive Guide](https://www.youtube.com/watch?v=ZpcOYg1Qfm4) · [frinky](https://www.youtube.com/channel/UCepxYGyRNUXgqve42r60q8g) · část 3 ·
[UE5 Ragdoll Physics Tutorial (Complete Guide)](https://www.youtube.com/watch?v=R5o2CjPb3Tk) · [LocoDev](https://www.youtube.com/channel/UCr8NttLeGyLd6m4qVS2Zb8g) · stand-up část

**Shrnutí:** Návrat z ragdollu má tři problémy: **odkud blendovat** (tělo leží v póze, kterou žádná animace nezná), **kterou animaci hrát** (na zádech vs. na břiše) a **kdy vůbec vstávat**. Odpovědi: **pose snapshot** zmrazí poslední fyzikální pózu jako blendovací zdroj, **dot product pánve se světovou osou Z** rozhodne front/back, a looping timer čeká, až se tělo přestane hýbat.

### Rozpad myšlenky

**Pose snapshot** [(33:13)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=1993s): při ukončení ragdollu `Save Pose Snapshot("ragdoll")` na anim instanci; v AnimBP větev s uzlem **Pose Snapshot** téhož jména (blend time 0) — strom pak plynule blenduje *z* zmrzlé fyzikální pózy do vstávací montáže místo lupnutí. LocoDev totéž staví jako stav ve state machine s přechody podle `is ragdolling` (property access, žádný cast) a Hermite Cubic blendem [(40:16)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=2416s), [(50:24)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=3024s). DK 3D nabízí alternativu bez snapshotu: timeline 0,5 s žene `Set All Bodies Below Physics Blend Weight` 1→0 a teprve pak vypne simulaci [(22:46)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=1366s).

**Na zádech, nebo na břiše?** DK 3D: right vector rotace pelvis socketu → **dot product s (0,0,1)** → kladný = na zádech → select montáže stand-back/stand-front [(36:40)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=2200s). K tomu rotace kapsle při vstávání: yaw z pelvisu + select(na zádech: +180° : 0) — jinak postava vstane čelem vzad [(43:41)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=2621s); frinky řeší totéž přes roll < 0 → yaw − 180 [(37:50)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=2270s).

**Montáže a pořadí operací:** blend in krátký (0–0,25 s — rychle „chytit" ragdoll pózu), blend out delší a měkký (0,3–1 s, cubic/sinusoidal) [(13:33)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=813s), [(46:26)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=2786s). Dvě pasti: **simulate physics musí být false, než montáž spustíš** — jinak nehraje [(20:27)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=1227s); a movement vracet až na konci — DK přes anim notify „standing" umístěný tam, kde póza ≈ idle [(17:43)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=1063s), frinky timerem v délce montáže [(35:31)](https://www.youtube.com/watch?v=ZpcOYg1Qfm4&t=2131s).

**Kdy vstát — samo:** DK klávesou jen *vstupuje*; **looping** `Set Timer by Function Name` (0,5 s — checkbox looping, klasická past [(49:50)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=2990s)) hlídá `Get Physics Linear Velocity(pelvis)` → `Vector Is Nearly Zero` (tolerance 5) → tělo se dokutálelo → clear timer → vstávej [(47:24)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=2844s). Postava se tak skutálí ze schodů a vstane sama, správnou animací. LocoDev doplňuje výstup **ve vzduchu**: not-on-ground → movement Falling + `Set Velocity` = poslední ragdoll rychlost — hybnost se přenese a postava letí dál [(43:46)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=2626s). A pozor na kapsli u podlahy: line trace z pelvis dolů s fallbackem, když nic netrefí — jinak se postava teleportuje na nulové souřadnice [(32:37)](https://www.youtube.com/watch?v=-mHfpyBn_UQ&t=1957s).

> **Pozn.:** LocoDev na závěr staví pohyblivé platformy jako **test rig** (timeline lerp + overlap → ragdoll start) [(54:23)](https://www.youtube.com/watch?v=R5o2CjPb3Tk&t=3263s) — dobrá praxe: fyzikální systém potřebuje hřiště, kde ho jde opakovaně mučit. Pro nás je celá tahle smyčka (zásah → ragdoll → dokutálení → vstání správným směrem) přesně to, co udělá z omráčení stráže *systém* místo cutscény.

**Souvislosti:** [Rejstřík: pose snapshot](../rejstrik.md#pose-snapshot) · [Rejstřík: anim notify](../rejstrik.md#anim-notify) · [Rejstřík: retriggerable delay](../rejstrik.md#retriggerable-delay) · [Pasti a arénové mechaniky: timeline](pasti-a-mechaniky.md#kostra-pasti-a-tri-variace-bodaky-rameno-rotor) · [Vstávání přes motion matching](#vstavani-pres-motion-matching-snapshot-pose-history-z-fyziky-a-chooser) *(výběr animace podle celé pózy)*

---

## Vstávání přes motion matching: snapshot, pose history z fyziky a chooser

**Zdroj:** [The Last GASP!? Game Animation Sample Updates for 5.8 + Q&A | Inside Unreal](https://www.youtube.com/watch?v=6NYC4ryO9ik) · [Unreal Engine](https://www.youtube.com/channel/UCBobmJyzsJ6Ll7UbfhI4iwQ) · ~2 h 47 min, stream k 5.8 updatu GASP (úsek o vstávání) ·
[Unreal Engine Just Got AAA Animation Physics (Game Animation Sample 5.8)](https://www.youtube.com/watch?v=UP3zWCMPn3E) · [Gorka Games](https://www.youtube.com/channel/UCv_n9oioNF6OpzR2dt6E4xg) · ~8 min, přehled updatu

**Shrnutí:** Vstávání z ragdollu je v GASP 5.8 výběr, ne pevná animace. Chooser s pose match sloupcem porovná fyzikální pózu (nohy, ruce, natočení pánve) se začátky vstávacích montáží a vybere tu nejbližší. Když se postava ještě kutálí, vybere i vstávání z válení. Aby to šlo, musí motion matching vidět pózu z fyziky, ne z animace. AnimBP ale běží před fyzikou, a proto se historie póz po fyzice přepíše. Háček je na konci: bez okamžitého přechodu na snímek fyzikální pózy postava před vstáváním viditelně lupne.

### Rozpad myšlenky

**Výstup jako změna módu.** Tlačítko skoku s podlahou pod postavou spustí `Exit Ragdoll`, který jen zařadí nový pohybový mód [(1:47:11)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6431s). Důvod: mód může změnit i jiná logika, třeba pád do vody přepne postavu na plavání, a fyzika musí skončit i tehdy. Úklid proto visí na události `On Movement Mode Changed Post Finalize`. Když byl předchozí mód ragdoll, provede se výstup [(1:47:58)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6478s):
- kapsle dostane zpátky kolize,
- uloží se pose snapshot fyzikální pózy pro plynulý přechod,
- přepíše se historie póz, aby motion matching viděl skutečnou pózu [(1:48:45)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6525s).

**Proč přepsat historii póz.** Všechna hledání motion matchingu čtou uzel Pose History, který se plní během aktualizace AnimBP. Ta ale běží před fyzikou, takže historie o výsledku fyziky neví. Nová funkce do ní pózu z fyziky zapíše. Motion matching porovnává pózu z předchozího snímku, takže to nepřidá žádnou latenci [(1:49:31)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6571s).

**Výběr.** Vstávací montáž vybírá chooser, stejně jako u traversalu, a dostává historii póz [(1:50:26)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6626s).
- První sloupec je pohybový mód. Zatím je tu jen vstávání na zem, ale stejně by šel přidat výstup z ragdollu do plavání nebo salto ve vzduchu [(1:51:13)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6673s).
- Nad prahem rychlosti se vybírá vstávání z válení.
- Mezi zbylými montážemi rozhodne pose match sloupec. Schema bere trochu trajektorie, ale hlavně pózu: polohu chodidel a rukou a natočení pánve [(1:52:01)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6721s).

Vstávacích animací by tak mohla být klidně stovka a vybrala by se ta, jejíž úvodní póza nejlíp sedí.

**Návrat bez lupnutí.** Profil se vrátí na výchozí a AnimBP přejde okamžitě, s nulovým přechodem, na pózu ze snapshotu. Teprve z ní se blenduje do vstávací montáže ve slotu dál v grafu [(1:52:47)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6767s), [(1:53:33)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6813s). Bez toho kroku postava před vstáváním velmi viditelně lupne [(1:53:33)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6813s), [(1:54:19)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=6859s). V ukázce se tak postava zvedne plynule i z kutálení [(16:22)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=982s) a po tacklu může vstát hned [(18:42)](https://www.youtube.com/watch?v=6NYC4ryO9ik&t=1122s). Gorka Games správně připomíná, že právě tenhle přechod z fyzikální hromady do čisté animace obvykle vypadá nejhůř [(2:22)](https://www.youtube.com/watch?v=UP3zWCMPn3E&t=142s).

> **Pozn.:** Proti [vstávání výš](#vstavani-pose-snapshot-frontback-a-auto-recovery) se mění jediná věc, ale zásadní. Kterou animaci hrát, nerozhoduje dot product pánve se svislou osou a select ze dvou montáží, ale porovnání celé pózy s libovolným počtem montáží. Snapshot a pořadí operací zůstávají stejné. Otočení postavy se tu řeší dřív: kapsle už v ragdoll módu sleduje, jestli postava leží na zádech, nebo na břiše ([pohybový mód ragdollu](#ragdoll-ktery-se-chrani-pozy-z-animace-sila-z-krivek-a-cas-do-dopadu)). Pose match sloupec, který tu vybírá, popisuje [GASP](gasp.md#motion-matching-uvnitr-chooseru-pose-match-sloupec-databaze-na-radek-a-blend-space-ve-stacku).

**Souvislosti:** [Rejstřík: Pose Snapshot](../rejstrik.md#pose-snapshot) · [Rejstřík: Pose History](../rejstrik.md#pose-history) · [Rejstřík: Pose Match column](../rejstrik.md#pose-match-column) · [Rejstřík: Chooser](../rejstrik.md#chooser)
