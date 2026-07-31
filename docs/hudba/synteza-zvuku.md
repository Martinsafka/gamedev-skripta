# Syntéza zvuku od nuly

Umět si v syntezátoru postavit jakýkoli zvuk od nuly je jedna z nejmocnějších dovedností producenta — a zároveň místo, kde se dá snadno utopit v přednastavených presetech, aniž bys věděl, co dělají. Tahle kapitola je nejjednodušší plán, jak libovolnému synthu porozumět: tři moduly, jeden signálový řetězec, a odtud nekonečno.

Je to praktické doplnění [Fyziky souzvuku](fyzika-souzvuku.md) — tam barvu (a tím alikvóty) jen popisujeme, tady si ji stavíš sám. A je to zdroj materiálu pro „volbu zvuku" z [Akordů a harmonie](akordy-a-harmonie.md#emoce-z-voicingu-a-artikulace).

---

## Anatomie subtraktivního synthu

**Zdroj:** [How To Make Any Sound From Scratch (escape the preset trap)](https://www.youtube.com/watch?v=p1-WmITJqBk) · [Alex Rome](https://www.youtube.com/channel/UCh1MtJ4rx4n4PQGYNYK_UXA) · ~24 min, tutoriál

**Shrnutí:** Nejběžnější typ synthu je **subtraktivní** a má tři části: **oscilátory** generují surový zvuk, **filtr** z něj ubírá a **obálky (envelopes) a LFO** ho tvarují a rozhýbávají. Jakmile pochopíš tenhle jeden signálový řetězec, umíš přečíst skoro každý synth — jen knoby jsou jinde.

### Rozpad myšlenky

Signálový řetězec [(0:48)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=48s): oscilátor → filtr → obálka/LFO. Nejslavnější pad elektronické hudby je jen surová pila (sawtooth) protažená filtrem [(2:15)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=135s) — tím vidíš celý princip v jednom kroku.

Na **oscilátoru** volíš barvu zvuku přes tvar vlny [(2:15)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=135s):

- **sinus** — bez ostrých hran, teplý zaostřený tón bez alikvót;
- **obdélník (square)** — ostré hrany, spousta frekvencí;
- **trojúhelník** — jako sinus, ale s hranami;
- **pila (saw)** — nejbohatší, nejlepší materiál pro unison.

**Unison** [(4:09)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=249s) navrství víc kopií vlny na jednu notu — zvuk se rozšíří do sterea (tři noty × 10 hlasů unisonu = 30 pil přes sebe). Filtr pak z bohaté vlny ubírá; obálka nakonec řekne, jak se zvuk chová při stisku, držení a puštění noty. To je celá kostra — zbytek jsou variace.

> **Pozn.:** Tady se přímo potkává [fyzika souzvuku](fyzika-souzvuku.md#alikvoty-urcuji-stupnici): tvar vlny je přesně to, co určuje alikvóty, a tím barvu. Sinus = jedna frekvence, žádné alikvóty; pila = jich plno. Když vybíráš waveform, vybíráš alikvótní obsah zvuku.

**Souvislosti:** [Amp-controlled zvuky a bas](#amp-controlled-zvuky-a-bas) · [Fyzika souzvuku: alikvóty](fyzika-souzvuku.md#alikvoty-urcuji-stupnici) · [Rejstřík: subtraktivní syntéza](../rejstrik.md#subtraktivni-synteza) · [Rejstřík: oscilátor](../rejstrik.md#oscilator) · [Rejstřík: unison](../rejstrik.md#unison)

---

## Amp-controlled zvuky a bas

**Zdroj:** [How To Make Any Sound From Scratch (escape the preset trap)](https://www.youtube.com/watch?v=p1-WmITJqBk) · [Alex Rome](https://www.youtube.com/channel/UCh1MtJ4rx4n4PQGYNYK_UXA) · ~24 min, tutoriál

**Shrnutí:** První skupina zvuků, kterou by ses měl naučit, jsou **amp-controlled** — tvarované obálkou hlasitosti (amp envelope) přes čtyři knoby **ADSR**. A první praktický zvuk, který zvládneš hned, je bas: libovolná vlna v nízké oktávě protažená úzkým dolnopropustným filtrem.

### Rozpad myšlenky

**ADSR** je čtveřice knobů amp obálky [(6:26)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=436s):

- **Attack** — jak dlouho zvuku trvá, než po stisku naběhne (pomalý = pozvolný nástup, rychlý = úder);
- **Decay** — pokles po náběhu k úrovni sustainu;
- **Sustain** — hlasitost po dobu držení noty;
- **Release** — jak dlouho zvuk doznívá po puštění.

Decay a sustain jsou provázané: decay začne dávat smysl, teprve když sustain není na maximu [(9:29)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=569s) — krátký decay + střední sustain = úderný začátek s doznívajícím tělem.

**Bas** je nejvděčnější první cíl [(12:46)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=766s): napiš noty v nízké oktávě, vezmi jakoukoli vlnu a protáhni ji úzkým low-pass filtrem zaostřeným na nízké frekvence. Filtrovaný obdélník dá jeden z nejsilnějších sub-basů. Sinus dá čistý sub, který spíš cítíš než slyšíš [(14:37)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=877s) — pozor, na telefonních reproduktorech ho posluchač neuslyší; proto se sinusový sub „obarví" distorcí [(15:23)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=923s), která přidá vyšší harmonické, jež projdou i malými repráky.

**Souvislosti:** [Anatomie subtraktivního synthu](#anatomie-subtraktivniho-synthu) · [Modulace: envelope a LFO](#modulace-envelope-a-lfo-otaceji-knoby) · [Sound design ve hře](sound-design-ve-hre.md) (kde je ADSR řeč o zvukových efektech) · [Rejstřík: ADSR](../rejstrik.md#adsr) · [Rejstřík: low-pass filtr](../rejstrik.md#low-pass-filtr)

---

## Modulace: envelope a LFO otáčejí knoby

**Zdroj:** [How To Make Any Sound From Scratch (escape the preset trap)](https://www.youtube.com/watch?v=p1-WmITJqBk) · [Alex Rome](https://www.youtube.com/channel/UCh1MtJ4rx4n4PQGYNYK_UXA) · ~24 min, tutoriál

**Shrnutí:** Modulace otevírá nekonečno. Princip je prostý: **obálka nebo LFO za tebe otáčí libovolným knobem** — obálka jednou při stisku noty, LFO donekonečna. Jeden naučený modulovaný zvuk (filtrový pluck) pak přesměruješ na cokoli.

### Rozpad myšlenky

Úkol obálek a LFO je jediný [(16:43)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=1049s): otáčet knoby. Přetáhneš obálku nebo LFO na knob, který chceš rozhýbat — obálka ho otočí jednou (při každé notě), **LFO** ho otáčí pořád dokola. To je celý rozdíl.

Zvuk, který by měl umět každý [(18:39)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=1119s): vezmi pilu, zavři filtr úplně (ticho), a druhou obálkou otevírej a zavírej cutoff tak rychle, že to vytvoří zvuk — slavný **electro pluck** [(19:27)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=1167s). Trik: nastav modulaci hodně hluboko (zvuk skoro zavřený), abys pak při aranži mohl automatizací cutoff otevřít a nechat zvuk „ožít".

A hlavní pointa celé kapitoly [(21:49)](https://www.youtube.com/watch?v=p1-WmITJqBk&t=1309s): tohle není jeden zvuk. Když umíš signálový řetězec a modulaci, tentýž postup přeměníš v nekonečno různých zvuků — bas, akordy, melodii, cokoli. Preset je slepá ulička; řetězec je klíč.

**Souvislosti:** [Amp-controlled zvuky a bas](#amp-controlled-zvuky-a-bas) · [FM: když jeden zvuk ohýbá druhý](#fm-kdyz-jeden-zvuk-ohyba-druhy) · [Akordy a harmonie: volba zvuku](akordy-a-harmonie.md#emoce-z-voicingu-a-artikulace) · [Žánry: výběr zvuku dělá žánr](zanry-a-styl.md#zanr-je-recept-ne-magie) · [CDP a SoundThread](nastroje-zdarma-a-game-jam.md#cdp-a-soundthread-laborator-na-zvuk-zdarma) *(co jde, když nemusíš stíhat reálný čas)* · [Rejstřík: LFO](../rejstrik.md#lfo)

---

## FM: když jeden zvuk ohýbá druhý

**Zdroj:** [How many FMs can we bake into a strudel?](https://www.youtube.com/watch?v=8ruLuZv1ju8) · [Glossing](https://www.youtube.com/channel/UCHrhiATyh5jAMboL2ywGyJQ) · ~5 min, ukázka funkce

**Shrnutí:** Subtraktivní syntéza z bohatého zvuku **ubírá**. **FM syntéza** místo toho nechá jeden signál **rozkmitávat frekvenci druhého** — a z pár oscilátorů dostane zvuky, které se filtrem postavit nedají. Ukázáno je to ve Strudelu, ale platí to všude. Háček, kvůli kterému má FM pověst nepřístupné: **nejdůležitější parametr není hloubka, ale poměr**.

### Rozpad myšlenky

**Co se vlastně děje** [(0:34)](https://www.youtube.com/watch?v=8ruLuZv1ju8&t=34s): vezmeš pilu a přidáš k ní další signál, který **moduluje její frekvenci**. Množství modulace je jeden knob (`fm`) — od nuly, kde se nestane nic, po hodnoty, kde je zvuk k nepoznání.

**Ten druhý knob je ale ten podstatný** — **harmonicita** (`fmh`): *„zní to složitě, ale je to jen poměr frekvence modulátoru k původnímu signálu."* A na tom poměru stojí charakter zvuku:

- **velmi nízké poměry** → *„začíná to znít jako vibráto"* (modulace je tak pomalá, že ji slyšíš jako kolísání výšky, ne jako barvu);
- **vysoké poměry** → divoké alikvóty, zvlášť u čísel, která **nejsou celočíselné poměry** — tam vznikají nesouzvučné, kovové barvy;
- celočíselné poměry drží zvuk „laděný", protože přidané frekvence sedí na harmonickou řadu.

**ADSR platí i tady** — attack a decay na FM dělají **zvonivé tóny**, což je klasika (zvony a elektrické piano jsou učebnicové FM zvuky). A **mírné rozladění** dvou oscilátorů proti sobě dá slyšitelný zázněj, ze kterého se staví **Reese bas**.

**Modulátor nemusí být sinus** [(2:08)](https://www.youtube.com/watch?v=8ruLuZv1ju8&t=128s): jde nastavit i jeho tvar vlny, včetně šumu. Autorka na růžový šum reaguje jednou větou, která říká všechno o tom, na co se FM používá: *„takže teď jsi Porter Robinson."*

**A kam to jde dál** [(3:00)](https://www.youtube.com/watch?v=8ruLuZv1ju8&t=180s): modulátory se dají řetězit — FM2 moduluje FM1, FM3 moduluje FM2 — a v **matici** může kterýkoli modulovat kterýkoli, včetně sebe sama. To je zpětná vazba, u které autorka varuje: *„chceš na to hodně malé číslo, jinak se to začne chovat divoce."*

> **Pozn.:** Zajímavé je, že FM je **výpočetně levné a zvukově drahé** — pár oscilátorů dá barvy, které by subtraktivní řetězec sháněl vrstvením. Přesně proto na tom stála celá éra herního a konzolového zvuku (kdo zná chip zvuky z automatů a raných konzolí, poslouchá FM). Pro dnešní tvorbu je z toho použitelný jeden úzký recept: **sinus + FM + krátká obálka = zvonek nebo perkuse**, což jsou zvuky, které se ze samplů shánějí těžko a v UI hry se používají pořád. Vlastní výhrada: FM je notoricky **neintuitivní na ladění** — malá změna poměru přehodí zvuk na něco úplně jiného, takže se hůř „dolaďuje" a spíš se hledá. Proto se vyplatí naopak než u subtraktivní syntézy: **nejdřív najdi poměr, pak teprve tvaruj obálkou.**

**Souvislosti:** [Anatomie subtraktivního synthu](#anatomie-subtraktivniho-synthu) · [Modulace: envelope a LFO](#modulace-envelope-a-lfo-otaceji-knoby) · [Fyzika souzvuku: alikvóty](fyzika-souzvuku.md#alikvoty-urcuji-stupnici) · [Zvuk, efekty a modulace ve Strudelu](live-coding.md#zvuk-efekty-a-modulace) · [Rejstřík: FM syntéza](../rejstrik.md#fm-synteza) · [Rejstřík: oscilátor](../rejstrik.md#oscilator)
