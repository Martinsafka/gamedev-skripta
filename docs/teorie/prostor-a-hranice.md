# Prostor: blockout, kompozice a hranice mapy

Druhá dvojice level design technik se týká prostoru samotného: jak ho navrhnout, aby hráče vedl bez šipek a UI markerů — a jak ho ohraničit, aby si hráč hranic ideálně vůbec nevšiml. Případovka na jeskyni z UE5 a systematika hranic mapy pro sólo vývojáře.

---

## Jeskyně, která se hraje: landmark napřed, detail nakonec

**Zdroj:** [How Level Designers Build Caves in UE5](https://www.youtube.com/watch?v=lSrDXaTwvNU) · [Gabriel Fuentes](https://www.youtube.com/channel/UCvbm6PppZ3gmIyznJPayhSA) · ~5 min, workflow breakdown

**Shrnutí:** Většina jeskyní v UE vypadá dobře a hraje se špatně — protože vznikly jako vizuál, ne jako zážitek. Autorův postup jde obráceně: nejdřív startovní bod hráče a hlavní landmark, pak blockout z primitiv s metrickými materiály, a teprve nakonec assety. Kompozice, světlo a zúžení prostoru dělají navigaci; detail dělá jen náladu.

### Rozpad myšlenky

Pořadí práce: krajina a hrubé formy → blockout hlavní cesty z primitivních tvarů → **startovní bod + point of interest jako první rozhodnutí** [(1:11)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=71s). Landmark (combat aréna, poklad, zdroj světla — cokoli) dává rovnou měřítko, směr a osu, kolem které se plánují vzdálenosti, pacing a vertikalita. Bez něj stavíš tunel z kamení; s ním stavíš cestu *někam*.

Blockout disciplína, kterou stojí za to okopírovat: **grid/metrické materiály** [(1:52)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=112s) okamžitě prozradí, že vchod je moc úzký nebo skok moc dlouhý; **konzistentní barevný jazyk** [(2:15)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=135s) (cover = jedna barva, traversal = jiná) dělá level čitelný pro tebe i pro spolupracovníky; a **level design gym** [(2:41)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=161s) — referenční mapa metrik (výšky, šířky, doskoky) — drží standardy napříč levely.

Navigace bez UI stojí na třech nástrojích: **funneling** [(2:55)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=175s) — zúžení a rámování prostoru směrem, kudy má hráč jít; **leading lines** [(3:06)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=186s) — skály, stěny i spáry podlahy jako šipky, které nikdo nevidí; a **affordances** [(3:19)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=199s) — vedlejší cesty a tajné prostory signalizované světlem a kontrastem, aby *vypadaly* interaktivně. Osvětlení je tu dvojagent [(3:40)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=220s): dělá náladu a zároveň vede oko. Cílový pocit dobré jeskyně: tajemství a napětí — hráč zkoumá místo, kterému ještě úplně nerozumí [(3:52)](https://www.youtube.com/watch?v=lSrDXaTwvNU&t=232s).

> **Pozn.:** „Landmark napřed" je prostorová verze [účelu jako soudce](postmortem-shantytown.md#hra-ti-rika-cim-chce-byt-ucel-jako-designovy-soudce): jedno pevné rozhodnutí, podle kterého se rozhodují všechna další. A blockout z primitiv je [graybox](../rejstrik.md#graybox) v přesně tom smyslu, kdy je šedost správně — testuješ prostor a metriky, ne prodejnost.

**Souvislosti:** [Vedení hráče](vedeni-hrace.md) · [Prototypování](prototypovani.md) · [Rejstřík: blockout](../rejstrik.md#blockout) · [Rejstřík: landmark](../rejstrik.md#landmark)

---

## Hranice mapy: hráč se má rozhodnout sám, že dál nepůjde

**Zdroj:** [Map Boundary in Level Design | Tips for Solo Game Devs](https://www.youtube.com/watch?v=tcXGVyy4Mm8) · [Seta - Level Design](https://www.youtube.com/channel/UCQrteFJthQOMXwWs0g1O4RQ) · ~7 min, systematika s příklady

**Shrnutí:** Hranice mapy má jedinou práci: udržet hráče ve světě, který jsi postavil — a průšvih začíná, když hráč hranici *cítí*, místo aby ji přijal. Video třídí hranice na tvrdé a měkké a nabízí šest vzorů; nejhorší ze všech je neviditelná zeď.

### Rozpad myšlenky

**Tvrdé hranice** [(0:50)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=50s) fyzicky zastaví pohyb. Správně: přirozené bariéry světa — útesy, oceán, řeka, sráz. Špatně: **invisible wall** [(1:15)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=75s) — kolize tam, kde vizuálně nic nebrání; nic nezabíjí imerzi rychleji než „vidím, že tudy jít jde, ale hra mi to nedovolí". Autorova formulace za rámeček [(1:33)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=93s): když říkám, že cestu blokuje padlý strom, myslím tím, že cestu *blokuje padlý strom*.

**Měkké hranice** se dají překročit — svět jen dá jasně najevo, že je to špatný nápad. Pět vzorů:

- **Narativní** [(2:07)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=127s): most se zřítí, stráž nepustí, postava si povzdechne a couvne — nejsilnější, když se hranice utvoří hráči před očima; je svědek, ne oběť mechaniky.
- **Countdown** [(3:03)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=183s): překročíš a běží čas — dezerce ve válečné hře, mráz, toxický plyn, radiace [(3:36)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=216s). Tlak času a přežití místo kolize.
- **Nepřátelská** [(4:02)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=242s): za hranicí loví něco o třídu silnějšího. Jemná varianta: nemusíš hráče zabít — stačí, když se probere u hranice potlučený a závrať zmizí, jakmile odejde [(4:22)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=262s). Hranice ho nezabila, jen mu ukázala jeho limity.
- **Ekonomická** [(4:47)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=287s): přejít lze, ale nevyplatí se — kyslík nevystačí na cestu zpět, palivo nedoletí [(4:55)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=295s). Přirozené pro hry s hlubokou ekonomikou zdrojů.
- **Percepční** [(5:24)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=324s): svět nehrozí ani neúčtuje — jen se hůř vidí a ztrácí se směr; další průzkum je iracionální a nepříjemný, ne zakázaný. Učebnicový příklad je mlha Silent Hill — a [jak se staví v UE5](../praxe/osvetleni.md#mlha-ze-silent-hill-2-volumetricky-material-kolem-postavy).

Závěrečné pravidlo [(6:10)](https://www.youtube.com/watch?v=tcXGVyy4Mm8&t=370s): žádný vzor nemusí existovat čistý — kombinuj (vizuální omezení + narativní zdůvodnění), protože čím víc systémů hranici nese, tím míň působí jako restrikce a tím víc jako vlastnost světa. Design hranic není o zastavení hráče, ale o tom, aby se **sám rozhodl**, že dál nepůjde.

> **Pozn.:** Tohle je level designová obdoba [alibi pro omezení](scope.md#omezeni-potrebuje-herni-alibi): invisible wall je omezení bez alibi; padlý strom, mráz i kyslík jsou totéž omezení s fikcí, která ho prodá. Stejný princip, jiná měřítka.

**Souvislosti:** [Scope: omezení potřebuje alibi](scope.md#omezeni-potrebuje-herni-alibi) · [Vedení hráče](vedeni-hrace.md) · [Rejstřík: invisible wall](../rejstrik.md#invisible-wall) · [Rejstřík: soft boundary](../rejstrik.md#soft-boundary)
