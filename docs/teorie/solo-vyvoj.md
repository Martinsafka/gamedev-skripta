# Sólo vývoj: od nuly k vydané hře

Devět let profesionální praxe (AAA i vlastní indie tituly) zhuštěných do jedné mapy cesty: co rozhodnout, než napíšeš první řádek, jak si postavit pipeline jednoho člověka a jak hru průběžně ukazovat světu, aby launch nebyl skok do tmy. Kapitola je záměrně komplement: scope řeší [Scope a malé hry](scope.md), prototypy [Prototypování](prototypovani.md), Steam [Steam stránka](steam-stranka.md) — tady jde o to, jak to celé poskládat za jednoho.

---

## Rozhodnutí před prvním řádkem: platforma, hráč, oceán

**Zdroj:** [How To Make A Game Alone](https://www.youtube.com/watch?v=my8euq9bzFQ) · [Dog's Dream](https://www.youtube.com/channel/UC3hB-wGiqWVd3w2R2PyTvfw) · ~26 min, průvodce z praxe

**Shrnutí:** Bariéra vstupu je historicky nejnižší — bez titulu (za 9 let kariéry ho po autorovi nikdo nechtěl [(1:37)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=97s)), bez uměleckého vzdělání, bez let syntaxe. O to víc rozhodují volby před startem: **platforma** (mění design víc, než čekáš), **pro koho hru děláš** (past „zábavná na výrobu ≠ zábavná na hraní") a **do jakého trhu vplouváš** (red vs. blue ocean).

### Rozpad myšlenky

**Platforma první** [(2:24)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=144s): pro první projekt Steam nebo mobil (konzole = žádosti a dev kity). Není to distribuční detail — gamepad, klávesnice a touchscreen jsou tři různé hry; input formuje design od prvního dne.

**Nejcennější lekce videa** je autorův vlastní propadák [(3:10)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=190s): idle hra o vánoční továrně, kde AI systém pro elfy byl skvělý *inženýrský* puzzle — a nudná hra. „Vývojář si užil všechnu zábavu a hráči nezbylo nic": mizerné přijetí, mizerné prodeje. U dalšího projektu otočil postup — napřed analýza, co hráči daného segmentu skutečně hrají, teprve pak design [(3:58)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=238s). Pravidlo z toho: **začni u hráče, ne u toho, co si chceš naprogramovat** [(4:47)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=287s). (Srovnej s [nápadem, který rozhoduje](rady-z-praxe.md) — tohle je stejná vrstva ledovce z pohledu praxe.)

**Red vs. blue ocean** [(4:47)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=287s): červený oceán = přeplněné žánry s etablovaným publikem (battle royale, souls-like), kde se soutěží zdroji; modrý oceán = prostor bez konkurence, kde hra vytváří novou poptávku (Minecraft, Undertale) [(5:35)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=335s). Indie bez rozpočtu velkých studií má podle autora mířit do modrého — unikátní perspektiva nebo twist [(6:21)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=381s). A scope k tomu: 3–5 hodin obsahu, nebo replayabilita (roguelike, endless) místo dvacetihodinového eposu; první projekt dokončený do roka při práci po večerech [(6:21)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=381s).

**Souvislosti:** [Scope a malé hry](scope.md) · [Rady z praxe](rady-z-praxe.md) · [Co prodává](co-prodava.md) · [Rejstřík: Blue ocean](../rejstrik.md#blue-ocean)

---

## Pipeline jednoho člověka: GDD, engine, verzování, cizí assety

**Zdroj:** [How To Make A Game Alone](https://www.youtube.com/watch?v=my8euq9bzFQ) · [Dog's Dream](https://www.youtube.com/channel/UC3hB-wGiqWVd3w2R2PyTvfw) · stejné video, prostřední část

**Shrnutí:** Nástroje sólo vývojáře podle devítileté praxe: GDD jako živý dokument, ne předem vymyšlená bible [(7:07)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=427s); engine vybraný podle toho, co se *tobě* snadno učí [(9:28)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=568s); verzování dřív, než se projekt prohloubí; a assety od specialistů všude tam, kde hra nestojí na tvé vlastní ruce.

### Rozpad myšlenky

**GDD:** sepiš vizi a core koncepty, ale nechoď do hloubky u gameplaye — specifika mají **vyplynout z prototypů a iterací, ne být rozhodnuta dopředu** [(7:54)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=474s). Dokument žije a roste s projektem; cenu ukáže při rozšíření týmu nebo pitchi (Confluence, Notion, Miro [(8:41)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=521s)). Přesně tenhle přístup učí i [nástěnkový design dokument](jak-zacit.md#design-dokument-ktery-skutecne-otevres-nastenka-misto-eseje) a bolestně potvrzuje zápisek [GDD review](../zapisky/gdd-review.md).

**Engine:** „pro indie je to upřímně jedno" [(9:28)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=568s) — 2D svědčí Unity/Godotu, UE vyniká ve 3D, cinematice a systemic gameplayi, ale hlavní kritérium je, který nástroj se ti snadněji učí; rozdíly (rendering, paměť) doceníš až u druhého projektu [(10:15)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=615s). Blueprinty ani C# nejsou důvod k panice [(11:01)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=661s).

**Hygiena projektu:** pár malých prototypů na osahání enginu — a pak **hlavní projekt založ načisto**, ne nad prototypem; čistá struktura se u většího projektu nedá dohnat zpětně [(11:47)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=707s). **Verzování nastav dřív, než jdeš do hloubky** [(12:34)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=754s): Git zdarma, Perforce na velké UE assety; rozbitá animace nebo zkorumpovaný level přestane být katastrofa a stane se `revert`.

**Assety:** většina úspěšných sólo titulů staví na cizích assetech [(14:08)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=848s) — Fab, TurboSquid, Sketchfab, Mixamo (rigované postavy a animace zdarma), zvukové banky, Fiverr na zakázky [(14:55)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=895s); kupované jde tweakovat, aby sedlo stylu. AI nástroje autor doporučuje na zrychlení kódu, ale **AI assety jen do prototypu, ne do finále** [(16:27)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=987s).

> **Pozn.:** Tohle je třetí nezávislý zdroj v knihovně, který říká „všechno sám neuděláš" — po [BiteMe počtech](produktivita.md#vsechno-sam-neudelas-a-nemas) a ShantyTown praxi. Když se tři praktici shodnou, ber to jako uzavřenou otázku.

**Souvislosti:** [Start projektu](jak-zacit.md) · [Organizace projektu](../praxe/organizace-projektu.md) · [AI assety](../praxe/ai-assety.md) · [Rejstřík: Version control](../rejstrik.md#version-control) · [Rejstřík: Game Design Document](../rejstrik.md#game-design-document)

---

## Ukazuj průběžně: showcase demo, vertical slice, launch bez skoku do tmy

**Zdroj:** [How To Make A Game Alone](https://www.youtube.com/watch?v=my8euq9bzFQ) · [Dog's Dream](https://www.youtube.com/channel/UC3hB-wGiqWVd3w2R2PyTvfw) · stejné video, závěrečná část

**Shrnutí:** Od chvíle, kdy existuje cokoli ukazatelného, běží druhá půlka práce: testovat zájem trhu dřív, než je pozdě couvnout. Autorova posloupnost: **showcase demo** (malý vyleštěný výsek jádra na video) → **vertical slice** (hratelný kus, zamknuté mechaniky) → Steam stránka, festivaly, launch — a po launchi hra nekončí.

### Rozpad myšlenky

**Showcase demo** [(16:27)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=987s): místo stavění systémů krátký kontrolovaný zážitek, který prodá vizi — u hororu stačí jedna chodba, blikající světlo, stín a jeden dobře načasovaný moment [(17:16)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1036s). Cíl: kvalitní video, reakce na sítích = levný test appealu. K tomu brzy devlog kanál (komunita od začátku, časem i příjem [(18:02)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1082s)). A **mluv o nápadu nahlas**: „ideas are cheap, execution matters" — nikdo ti hru neukradne, protože nikdo ji neudělá po tvém; raná zpětná vazba nápad zlepšuje [(18:49)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1129s).

**Vertical slice** [(19:35)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1175s): plně hratelný kus bez zkratek — a milník, po kterém se **core mechaniky zamykají**; dál už přibývá obsah, ne redesign smyčky. Playtestuj co nejvíc (autor cituje Valve jako vzor [(20:22)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1222s)) a půjč si trik z UX labů: **začni sezení otázkami na věci, o kterých víš, že jsou dobré** — po úvodní pozitivní odpovědi jsou testeři upřímnější ke zbytku [(21:10)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1270s). RPG systémy, které v malém demu nezáří, izoluj a testuj zvlášť [(21:58)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1318s).

**Cesta k launchi** [(22:45)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1365s): Steam stránka se slice-demem, sbírání wishlistů, Next Fest a festivaly; funding přes Kickstarter (zároveň marketing) nebo publishery — **bez dema dnes publisher nejedná** [(23:33)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1413s). Eventy: velký booth se sólistovi nevyplatí, malé lokální akce ano — zdarma a vidíš lidi hrát naživo [(23:33)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1413s). Drobnost s velkým dopadem: opatrně s rozdáváním klíčů — recenze z klíčů Steam omezuje a launchový nápor recenzí je nenahraditelný [(24:21)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1461s). Early access jen ve stavu, který lidi udrží: **hra má jen jeden velký launch** [(25:08)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1508s). A po vydání: patche, obsah, komunita — „neopouštěj projekt ve chvíli, kdy bouchne šampaňské" [(25:08)](https://www.youtube.com/watch?v=my8euq9bzFQ&t=1508s).

**Souvislosti:** [Prototypování a vertical slice](prototypovani.md) · [Steam stránka](steam-stranka.md) · [Devlogy](devlogy.md) · [Postmortem ShantyTown](postmortem-shantytown.md) · [Rejstřík: Steam Next Fest](../rejstrik.md#steam-next-fest) · [Rejstřík: Wishlist](../rejstrik.md#wishlist)
