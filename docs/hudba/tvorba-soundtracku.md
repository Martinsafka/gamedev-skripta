# Tvorba herního soundtracku

Když umíš melodie, akordy a zvuk, zbývá je poskládat do hudby, která **slouží hře**. Herní soundtrack má pár specifik, kterými se liší od písně: vzniká z tónu scény, propojuje svět opakujícími se motivy a musí se donekonečna bezešvě vracet do sebe. Kapitola slučuje dva průvodce tvorbou soundtracku od nuly — jeden dlouhý dílenský (Jaies staví pět tracků naživo) a jeden hutný přehledový (Zectro).

Stojí na základech z [Melodie](melodie.md), [Akordů a harmonie](akordy-a-harmonie.md) a [Syntézy zvuku](synteza-zvuku.md).

---

## Nejdřív tón, pak noty

**Zdroj:** [How to Make a Video Game Soundtrack (from scratch) | Art of Game Design | OST/VGM](https://www.youtube.com/watch?v=1qPfH95ry84) · [Jaies](https://www.youtube.com/channel/UCM2A5I4WF6pybUGPpb5jQIg) · ~43 min, tutoriál
**Zdroj:** [A Guide to Making Video Game Music](https://www.youtube.com/watch?v=dMkTdYmOgiQ) · [Zectro](https://www.youtube.com/channel/UCQ4hTUbcR_XQRB40C_wkDkA) · ~11 min, tutoriál

**Shrnutí:** Než napíšeš první notu, ujasni si **tón** — celkovou náladu hry a konkrétní kontext scény. Hudba slouží scéně, ne naopak. Strašidelný dům chce jiný zvuk než veselá vesnice; postava „potulný podivín" chce jinou melodii než hrdina. Tón určuje všechno ostatní.

### Rozpad myšlenky

Oba autoři začínají stejně: **nejdřív kontext** [(0:03)](https://www.youtube.com/watch?v=1qPfH95ry84&t=3s). Jaies pojmenuje celkový tón hry, který řídí zvuk celého soundtracku, a pak píše pět různých kusů podle scény — téma postavy, bojovou hudbu, smutný/melancholický kus a ambientní track pro atmosféru oblasti [(0:49)](https://www.youtube.com/watch?v=1qPfH95ry84&t=49s). Zectro to zobecní na trojici **setting, nálada, prostředí** [(2:33)](https://www.youtube.com/watch?v=dMkTdYmOgiQ&t=153s): u strašidelného domu čekáš creepy hudbu — ale když jsou postavy naopak v dobré náladě, použij veselejší hudbu s nástroji a efekty (reverb) domu, ať to do prostředí zapadne.

Druhá společná rada: **začni malý** [(4:08)](https://www.youtube.com/watch?v=dMkTdYmOgiQ&t=248s). Představa „napíšu celý soundtrack" ochromuje; skládej kus po kuse, neřeš finální podobu. Pro rozjezd pomáhá vybrat stupnici — omezí počet voleb a usnadní start.

> **Pozn.:** „Nejdřív tón" je hudební obdoba core DNA z [nápadu](../teorie/napad.md) a percepčního souladu ze [sound designu](sound-design-ve-hre.md#hledej-spravny-zvuk-a-cti-styl): nejdřív pojmenuj *pocit*, pak vybírej prostředky, které ho zrcadlí. Bez toho skládáš hezké tóny, které do hry nesednou.

**Souvislosti:** [Leitmotiv: hudba propojuje svět](#leitmotiv-hudba-propojuje-svet) · [Nápad: core DNA a emoce](../teorie/napad.md) · [Sound design: cti styl](sound-design-ve-hre.md#hledej-spravny-zvuk-a-cti-styl) · [Rejstřík: leitmotiv](../rejstrik.md#leitmotiv)

---

## Sound fonty: retro zvuk jako Toby Fox

**Zdroj:** [A Guide to Making Video Game Music](https://www.youtube.com/watch?v=dMkTdYmOgiQ) · [Zectro](https://www.youtube.com/channel/UCQ4hTUbcR_XQRB40C_wkDkA) · ~11 min, tutoriál
**Zdroj:** [How to Make a Video Game Soundtrack (from scratch) | Art of Game Design | OST/VGM](https://www.youtube.com/watch?v=1qPfH95ry84) · [Jaies](https://www.youtube.com/channel/UCM2A5I4WF6pybUGPpb5jQIg) · ~43 min, tutoriál

**Shrnutí:** Charakteristický retro zvuk herní hudby často nedělá skladba, ale **zvuková paleta** — konkrétně sound fonty a retro pluginy. Toby Fox postavil Undertale na sound fontech z Earthboundu; stejný trik máš k dispozici zdarma.

### Rozpad myšlenky

**Sound font** je kolekce nasamplovaných zvuků nástroje, kterou přehráváš sound font playerem [(2:33)](https://www.youtube.com/watch?v=dMkTdYmOgiQ&t=153s). Zectro odkazuje na web s fonty (mimo jiné přímo zvuky z Undertale, Earthboundu, Nintenda) — hledáš soubory s příponou `.sf2`. Pro čistě retro zvuk existují i pluginy jako NES VST nebo Magical 8bit; pro modernější zvuk stovky dalších.

Jaies to ukazuje v praxi [(2:23)](https://www.youtube.com/watch?v=1qPfH95ry84&t=143s): když Toby Fox dělal Undertale, sáhl po nástrojích ze SNES her (Earthbound, Mother 3) přes sound font player. Autor si takhle nahraje paletu z Kirbyho, Chrono Triggeru, Yoshi's Islandu a z ní pak skládá — barva těch nástrojů dá celému tracku okamžitě „herní" charakter, ještě než zazní první melodie.

> **Pozn.:** Tady se pěkně zavírá kruh se [syntézou zvuku](synteza-zvuku.md): buď si zvuk postavíš od nuly v synthu, nebo si vypůjčíš hotovou paletu ze sound fontu. Pro retro/nostalgický tón je sound font rychlejší a autentičtější; pro unikátní signature zvuk se vyplatí syntéza.

**Souvislosti:** [Nejdřív tón, pak noty](#nejdriv-ton-pak-noty) · [Syntéza zvuku od nuly](synteza-zvuku.md) · [Rejstřík: sound font](../rejstrik.md#sound-font)

---

## Leitmotiv: hudba propojuje svět

**Zdroj:** [A Guide to Making Video Game Music](https://www.youtube.com/watch?v=dMkTdYmOgiQ) · [Zectro](https://www.youtube.com/channel/UCQ4hTUbcR_XQRB40C_wkDkA) · ~11 min, tutoriál
**Zdroj:** [How to Make a Video Game Soundtrack (from scratch) | Art of Game Design | OST/VGM](https://www.youtube.com/watch?v=1qPfH95ry84) · [Jaies](https://www.youtube.com/channel/UCM2A5I4WF6pybUGPpb5jQIg) · ~43 min, tutoriál

**Shrnutí:** **Leitmotiv** je melodie svázaná s postavou, místem nebo věcí, která se vrací a proměňuje podle nálady scény, ale pořád ji poznáš. Je to mocný nástroj právě v herní hudbě: propojuje soundtrack v jeden svět, kde spolu témata a postavy souvisí.

### Rozpad myšlenky

Leitmotiv je motiv s přiřazeným významem [(5:56)](https://www.youtube.com/watch?v=dMkTdYmOgiQ&t=356s): typicky téma postavy, které se mění, aby sedělo do scény, ale zůstává rozpoznatelné (Zectro ukazuje motivy z Undertale). Není to jen ozdoba — je to způsob, jak dát soundtracku vnitřní logiku.

Jaies to předvede přímo [(38:55)](https://www.youtube.com/watch?v=1qPfH95ry84&t=2335s): když skládá ambientní track pro scénu ve vlaku, vezme melodii **tématu postavy** z prvního tracku a zapracuje ji do pozadí — postava je průvodčí, tak její motiv zazní i v hudbě vlaku, jen změněný [(40:29)](https://www.youtube.com/watch?v=1qPfH95ry84&t=2429s). „Je vždycky důležité mít propojenou hudbu — témata a postavy a místa se pojí." Hráč to nemusí vědomě zaznamenat, ale svět mu díky tomu drží pohromadě.

Leitmotiv je přímá aplikace práce s motivem z [Melodie](melodie.md#osm-otazek-na-cizi-melodii): vezmeš zapamatovatelnou buňku a transformuješ ji (zpomalíš, změníš nástroj, dáš do mollové varianty pro smutnou scénu) — a protože je pořád táž buňka, výsledek zůstane propojený.

**Souvislosti:** [Řemeslo herního tracku](#remeslo-herniho-tracku-bas-akordy-loop) · [Jak psát melodie: motivy](melodie.md#osm-otazek-na-cizi-melodii) · [Příběh a postavy](../teorie/pribeh-a-postavy.md) · [Rejstřík: leitmotiv](../rejstrik.md#leitmotiv) · [Rejstřík: motiv](../rejstrik.md#motiv)

---

## Řemeslo herního tracku: bas, akordy, loop

**Zdroj:** [How to Make a Video Game Soundtrack (from scratch) | Art of Game Design | OST/VGM](https://www.youtube.com/watch?v=1qPfH95ry84) · [Jaies](https://www.youtube.com/channel/UCM2A5I4WF6pybUGPpb5jQIg) · ~43 min, tutoriál
**Zdroj:** [A Guide to Making Video Game Music](https://www.youtube.com/watch?v=dMkTdYmOgiQ) · [Zectro](https://www.youtube.com/channel/UCQ4hTUbcR_XQRB40C_wkDkA) · ~11 min, tutoriál

**Shrnutí:** Pár konkrétních řemeslných návyků, které se v obou průvodcích vracejí: bas kopíruje základ akordu, akordy definují náladu, drumy sedí ke scéně — a hlavně, herní track se musí **bezešvě vracet do sebe**, protože ve hře loopuje donekonečna.

### Rozpad myšlenky

- **Bas kopíruje akord** [(7:41)](https://www.youtube.com/watch?v=dMkTdYmOgiQ&t=461s): typicky sedí na základním tónu (root) akordu, případně na kvintě. Nejdřív bas jako opora, pak mu přidej rytmus a pohyb.
- **Akordy definují náladu, drumy scénu** [(8:24)](https://www.youtube.com/watch?v=dMkTdYmOgiQ&t=504s): akordy jsou harmonická a rytmická opora nesoucí emoci; bicí ladíš podle scény — rychlé do souboje, pomalé a řídké do klidné scény. Nemusíš mít drumy vůbec.
- **Voice leading a pedal tone** [(28:16)](https://www.youtube.com/watch?v=1qPfH95ry84&t=1696s): u akordů hlídej, aby se tóny mezi nimi pohybovaly co nejmíň — zní to líp. Prodleva (pedal tone) pod měnícími se akordy přidá soudržnost a texturu (Jaies drží tón „d" pod celou progresí).
- **Smutný track = prostá zpěvná melodie + chromaticky klesající bas** [(29:34)](https://www.youtube.com/watch?v=1qPfH95ry84&t=1774s): melodie tak jednoduchá, že ji zahraje dítě jedním prstem, a bas, který klesá po půltónech — spolehlivý recept na melancholii.

A specifikum, kterým se herní track liší od písně — **bezešvý loop** [(15:37)](https://www.youtube.com/watch?v=1qPfH95ry84&t=937s): hudba ve hře se přehrává donekonečna, takže úplný konec musí navazovat na začátek. Poslední část udělej tak, aby plynule přešla do prvního taktu — jinak uslyšíš „šev" při každém opakování. (To je [aranžérský přechod](aranz.md#pisen-zije-v-prechodu), jen zapojený do kruhu.)

**Souvislosti:** [Leitmotiv: hudba propojuje svět](#leitmotiv-hudba-propojuje-svet) · [Akordy a harmonie: voicing a prodleva](akordy-a-harmonie.md#emoce-z-voicingu-a-artikulace) · [Aranžmá: píseň žije v přechodu](aranz.md#pisen-zije-v-prechodu) · [Rejstřík: seamless loop](../rejstrik.md#seamless-loop) · [Rejstřík: pedal tone](../rejstrik.md#pedal-tone)
