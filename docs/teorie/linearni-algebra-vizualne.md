# Lineární algebra vizuálně: matice jako pohyb

Tři díly série *SEE Matrix* od Visual Kernel dělají s maticemi to, co by měla dělat škola: místo drilu s čísly ukazují, **co transformace dělá s prostorem**. Kapitola jde od základních matic (scale, rotace, reflexe) přes eigenvektory a spektrální rozklad až po SVD — větu, která rozloží *jakoukoli* matici na tři srozumitelné kroky. Pro gamedev je to podloží všeho: každý transform v enginu, každá rotace kosti, každá projekce kamery je násobení maticí. Praktickou stranu téže mince řeší [Matematika pro gamedev](matematika-pro-gamedev.md).

---

## Matice je pohyb teček, násobení matic je skládání pohybů

**Zdroj:** [Visualize Different Matrices | SEE Matrix, Chapter 1](https://www.youtube.com/watch?v=7Gtxd-ew4lk) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · ~15 min, vizuální výklad

**Shrnutí:** Co je matice, „neví nikdo" — ale všichni víme, jak násobí vektor [(0:05)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=5s). Video z toho staví vizualizační stroj: vektor nakresli jako tečku, násobení maticí tečku přesune — a matice se stane *pohybem celé roviny* [(1:39)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=99s). Slavné matice pak dostávají čitelné vizitky: identity nedělá nic, skalární matice zvětšuje, záporná čísla zrcadlí.

### Rozpad myšlenky

Trik vizualizace: šipek je moc, tak se vektor zredukuje na **tečku** a sleduje se jen vybraná oblast roviny [(1:39)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=99s). Když maticí pronásobíš *všechny* tečky, uvidíš transformaci jako animaci — a protože tvar je jen nekonečno teček u sebe a obrázek jen mřížka barevných pixelů, matice tím pádem transformuje tvary i obrázky [(5:15)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=315s). Stejná logika běží ve 3D s maticí 3×3 [(6:24)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=384s).

Katalog základních matic, jak je video „vyzpovídá" [(2:27)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=147s):

- **Identity** (jedničky na diagonále) — žádný pohyb; násobení vrací tentýž vektor [(3:27)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=207s).
- **Skalární matice** (stejné K na diagonále) — uniformní zvětšení či zmenšení bez zkreslení: K>1 táhne ven, K<1 dovnitř, K=1 je identity [(4:29)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=269s).
- **„Off-one" matice** (identity s jedním K navíc) — škáluje jedinou osu; která pozice na diagonále, ta osa [(7:04)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=424s).
- **Záporná čísla na diagonále** — reflexe: −1 překlopí znaménko souřadnice, tedy zrcadlí podle osy; obě −1 zrcadlí kolem počátku [(8:37)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=517s).
- **Diagonální matice** (libovolná čísla na diagonále) — kombinace předchozích: každá osa se škáluje svým číslem, záporné přidá zrcadlení; hodnoty čteš přímo z diagonály [(12:13)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=733s).
- **Nulová matice** — všechno spadne do počátku [(14:05)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=845s).

Nejcennější věta dílu: **násobení matic vlastně není násobení, je to kompozice** [(11:49)](https://www.youtube.com/watch?v=7Gtxd-ew4lk&t=709s). „B krát A" znamená „chci jednu matici, která provede transformaci A a hned po ní B — v jednom kroku." Diagonální matici tak jde rozložit na sekvenci off-one matic a případnou reflexi — a naopak. Přesně tohle dělá engine, když skládá transform herního objektu z translace, rotace a scale rodičů: řetěz matic zkolabovaný do jedné.

**Souvislosti:** [Matematika pro gamedev: matice a rotace](matematika-pro-gamedev.md#matice-rotace-a-kvaterniony-tri-zpusoby-jak-drzet-otoceni) · [Rejstřík: Matice](../rejstrik.md#matice)

---

## Eigenvektory a spektrální rozklad: tři jednoduché kroky uvnitř symetrické matice

**Zdroj:** [Visualize Spectral Decomposition | SEE Matrix, Chapter 2](https://www.youtube.com/watch?v=mhy-ZKSARxI) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · ~16 min, vizuální výklad

**Shrnutí:** Většina matic dělá s prostorem nepopsatelnou „šmodrchu" — ale symetrická matice se dá **vždy** rozložit na rotaci → škálování os → rotaci zpět [(0:55)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=55s). Klíčem jsou eigenvektory: směry, které transformace nevychýlí, jen natáhne. Rozklad je učebnicový příklad, proč se dekompozice vyplácí — složitou věc přepíšeš jako sled kroků, kterým rozumíš.

### Rozpad myšlenky

Nejdřív slovník. **Transpose** je akce: řádky se stanou sloupci [(1:41)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=101s). **Symetrická matice** se transpozicí nezmění (S = Sᵀ) [(2:27)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=147s). A **ortogonální matice** — vizuálně čistá rotace — má kouzelnou vlastnost: její transpose je zároveň její inverze, tedy rotace opačným směrem [(2:27)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=147s). Otáčí-li Q kolem osy z o +25°, Qᵀ otáčí o −25° [(3:14)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=194s). **Dekompozice** je opak skládání: místo „slij dvě transformace do jedné" chceš „rozepiš jednu na několik jednodušších" — a bez věty, která řekne jak, nevíš, kde začít [(4:14)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=254s).

**Eigenvektor** je vidět dřív, než se definuje [(5:49)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=349s): pusť transformaci a sleduj, jak skoro každý vektor opustí svou původní přímku — až na pár výjimek, které zůstávají na místě a jen se natahují či zkracují. To jsou eigenvektory; párové číslo **eigenvalue** říká, kolikrát se při tom natáhnou (2.7 = natažení, 0.6 = zkrácení) [(7:21)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=441s). Eigenvektory jsou vždy *relativní k matici* — jiná matice, jiné neochvějné směry [(6:35)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=395s).

Silná vlastnost symetrických matic: jejich eigenvektory jsou **navzájem kolmé** [(8:07)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=487s) — což u obecné matice hraničí se zázrakem (2×2 matice nemusí mít ani dva). A kolmé směry jde rotací srovnat s osami souřadnic [(8:54)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=534s). Odtud **spektrální rozklad**: S = QΛQᵀ, čteno jako tři kroky [(11:50)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=710s) — (1) otoč eigenvektory na osy, (2) škáluj osy podle eigenvalues (Λ je diagonální; záporná hodnota otočí směr [(12:36)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=756s)), (3) otoč zpátky. Škola z toho udělá „únavné cvičení prstů a nudnou algebru", zatímco geometrie pod tím je elegantní: **rotaci řídí eigenvektory, škálování eigenvalues** [(14:15)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=855s).

Háček na konec: symetrických matic je v divočině málo [(15:01)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=901s) — po zobecnění na všechno sáhne až SVD (další myšlenka).

**Souvislosti:** [Rejstřík: Eigenvektor](../rejstrik.md#eigenvektor) · [Rejstřík: Matice](../rejstrik.md#matice) · doporučený doplněk dle videa: série *Essence of Linear Algebra* (3Blue1Brown) [(5:01)](https://www.youtube.com/watch?v=mhy-ZKSARxI&t=301s)

---

## SVD: jeden rozklad vládne všem

**Zdroj:** [SVD Visualized, Singular Value Decomposition explained | SEE Matrix, Chapter 3](https://www.youtube.com/watch?v=vSczTbgc8Rc) · [Visual Kernel](https://www.youtube.com/channel/UC9Cz481L3CeYm-ZqwqevCPQ) · ~16 min, vizuální výklad

**Shrnutí:** Singular Value Decomposition rozloží **jakoukoli** matici — bez ohledu na symetrii, tvar či rank — na rotaci, škálování se změnou dimenze a druhou rotaci [(0:05)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=5s). Je to „velké finále" lineární algebry a pracovní kůň datové vědy: od komprese obrázků po PCA. Kdo pochopil spektrální rozklad, má podle autora 80 % SVD hotových [(0:51)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=51s).

### Rozpad myšlenky

Nový kus skládačky: **obdélníková matice mění dimenzi.** Matice M×N bere vektor z Rⁿ a vrací vektor v Rᵐ [(2:23)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=143s) — a vektor (1, 2) z R² přitom *není* totéž co (1, 2, 0) z R³; jsou to „různé druhy z různých vesmírů", mezi kterými právě obdélníkové matice překládají [(1:37)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=97s). Nejjednodušší exempláře video křtí **dimension eraser** (obdélníková „identity", která zahodí z-ovou souřadnici) [(3:09)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=189s) a **dimension adder** (připne z = 0) [(4:19)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=259s).

Druhý kus: symetrii jde **vyrobit**. Pro libovolnou matici A jsou AAᵀ i AᵀA vždy symetrické [(6:05)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=365s) — a tím pádem mají kolmé eigenvektory. Ty se jmenují **levé** (z AAᵀ) a **pravé** (z AᵀA) **singulární vektory** matice A [(7:13)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=433s). Obě sady sdílejí nezáporné eigenvalues (seřazené sestupně se překrývají, zbytek jsou nuly) a jejich odmocniny jsou **singulární hodnoty** A [(8:00)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=480s).

Věta samotná: **A = UΣVᵀ** [(8:49)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=529s), vizuálně tři kroky [(10:22)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=622s):

1. **Vᵀ** — rotace, která srovná pravé singulární vektory na osy (největší singulární hodnota na X),
2. **Σ** — „obdélníková diagonála": škáluje osy singulárními hodnotami a zároveň dimenzi umaže či přidá (diagonální matice složená s dimension eraserem/adderem),
3. **U** — rotace os na levé singulární vektory.

Geometrická intuice z Wikipedie, ověřená na obrazovce: každá matice posílá **kouli na elipsoid** — rotace kouli nezmění, smazání dimenze z ní udělá kruh, škálování elipsu, závěrečná rotace ji jen natočí [(11:28)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=688s).

A k čemu to je? Druhá interpretace SVD — matice jako součet rank-1 matic — dává **low-rank aproximaci**: obrázek (velká matice pixelů) jde „skládat" z několika nejsilnějších složek a dostat rozumnou kompresi [(13:38)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=818s). První rotace rozkladu zase nese esenci **PCA** [(14:24)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=864s). A hlavně: intuice drží i v dimenzích, které neuvidíš — o transformaci stovky-rozměrných dat pořád víš, že je to rotace → škálování → rotace [(15:10)](https://www.youtube.com/watch?v=vSczTbgc8Rc&t=910s).

> **Pozn.:** Pro herní praxi SVD přímo nepotkáš každý den — ale myšlenkový vzorec „složité = sekvence jednoduchých, když víš, jak rozkládat" je tentýž, co používáš při dekompozici mechanik nebo Blueprint architektury. A až někde uvidíš PCA, kompresi textur nebo „principal axes" u kolizí, budeš vědět, čí příbuzný to je.

**Souvislosti:** [Rejstřík: SVD](../rejstrik.md#svd) · [Rejstřík: Eigenvektor](../rejstrik.md#eigenvektor) · [Markovovy řetězce](markovovy-retezce.md) — druhá „matematika, co predikuje svět"
