# Start projektu: od nápadu k prvnímu commitu

Autor zdrojového videa rok dělal hru, kterou nakonec zabalil — a většinu pozdějších problémů zpětně stopuje k přeskočené přípravě. Tahle kapitola je jeho náprava: kroky, které se na začátku projektu přeskakují nejsnáz a platí nejdráž. Nic z toho není technicky povinné; všechno z toho se vyplatí.

---

## Nápad se musí vejít na lepicí papírek

**Zdroj:** [How To PROPERLY Start Making A Game](https://www.youtube.com/watch?v=ekOp35B1Bdg) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · ~15 min, checklist z vlastního selhání

**Shrnutí:** Než se do nápadu zamiluješ, změř ho. Autorův test: celý nápad — mechaniky, příběh, všechno — se musí vejít na lepicí papírek (sticky note). K tomu odhad času: kolik myslíš, že to zabere, násob čtyřiceti. A engine? Vyber jakýkoli, hlavně rychle.

### Rozpad myšlenky

Nápady chodí samy — ve sprše, na procházce; těžké není nápad mít, ale střízlivě ho změřit. Autorova pojistka proti magnum opus: **první hra na lepicí papírek** [(1:25)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=85s). Když se vize nevejde, není to zadání pro první projekt — je to sen, ke kterému se dopracováváš přes menší hry. Tvrdohlavým video povoluje kompromis: udělej *demo* své velké hry v rozsahu papírku, dokonči ho celé, a teprv pak povyš na kartotéční lístek. Dál ne.

Násobič odhadu ×40 [(1:17)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=77s) je řečnická nadsázka s pravdivým jádrem: začátečník odhaduje jen kódování „šťastné cesty" a nevidí ladění, UI, zvuk, menu, buildy, opravy — vrstvy, které tvoří většinu práce.

Volba enginu je u prvních her bikeshedding: každý velký engine dnes zvládne skoro všechno, a čas propálený srovnáváním je čas nestrávený tvorbou [(1:47)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=107s). Vyber a jeď.

> **Pozn.:** U nás je vybráno (UE5), takže tahle rada zní snadno — ale platí i obráceně: „možná bych měl přejít na jiný engine" je u rozdělaného projektu skoro vždycky prokrastinace v převleku.

**Souvislosti:** [Začátky bez zkušeností](zacatky-bez-zkusenosti.md#maly-rozsah-neni-kompromis-je-to-strategie-preziti) · [Co znamená „dělej malé hry"](scope.md) · [Rejstřík: scope](../rejstrik.md#scope)

---

## Design dokument, který skutečně otevřeš: nástěnka místo eseje

**Zdroj:** [How To PROPERLY Start Making A Game](https://www.youtube.com/watch?v=ekOp35B1Bdg) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · stejné video, plánovací část

**Shrnutí:** Klasický game design document je slohová práce, kterou sólo vývojář nedopíše a nikdy nečte — autor to zkusil a vzdal. Funkční alternativa: vizuální nástěnka. Ne proto, že je hezčí, ale protože design dokument má jedinou metriku úspěchu — jestli se do něj vracíš.

### Rozpad myšlenky

Autorova nástěnka má čtyři sekce [(2:03)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=123s): koncept, level design, postavy, to-do. Co z ní stojí za okopírování bez ohledu na nástroj:

- **Reference s důvodem** — každá inspirační hra má u sebe větu, *proč* je referencí („dungeon generace jako Pokémon Mystery Dungeon"). Sbírka obrázků bez důvodů je moodboard, ne plán.
- **Levely jako sekvence** — šipky mezi levely + seznam features u každého. Nápady „někdy později" žijí odděleně v koláži, aby nekontaminovaly plán dema.
- **Mechaniky jako GIFy** — pohyblivá ukázka řekne o game feelu víc než odstavec textu.
- **Plán šetření assetů** přímo v dokumentu — nepřátelé jako reskiny jednoho psa: rozhodnutí, které v plánovací fázi stojí větu a v produkci ušetří týden.
- **Centrální to-do s podúkoly** — dokument tím přestává být archiv a stává se řídicím panelem: vždycky víš, co je další krok.

> **Pozn.:** Video je sponzorované konkrétním nástrojem (Milanote), takže formát ber s rezervou — myšlenka ale stojí i bez něj: Miro, Notion, FigJam nebo korková nástěnka poslouží stejně. Podstatný je princip *živého dokumentu*, ne značka.

**Souvislosti:** [Nápad](napad.md) · [Prototypování](prototypovani.md)

---

## Low-fi prototyp: ošklivost je pozvánka k upřímné zpětné vazbě

**Zdroj:** [How To PROPERLY Start Making A Game](https://www.youtube.com/watch?v=ekOp35B1Bdg) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · stejné video, prototypovací část

**Shrnutí:** Prototyp existuje, aby ověřil, že mechanika baví, dřív než do ní utopíš měsíce. Autor rozlišuje high-fi (funkční hratelná kostra) a low-fi — náčrt na papíře či mizerná animace konceptu. Low-fi má skrytou supersílu: vypadá tak lacině, že se ho lidé nebojí zkritizovat.

### Rozpad myšlenky

Autorova první hra šla rovnou do high-fi: měsíce stavěl funkční hru a zpětnou vazbu sbíral, až když každá změna bolela [(5:30)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=330s). Obrácený postup [(5:56)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=356s): nejdřív **low-fi prototyp** — kreslený scénář toho, jak se hra hraje [(6:13)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=373s). U jeho rytmického dungeon crawleru to je pár čmáranic: útok mimo rytmus funguje normálně, útok do rytmu přidává bonus.

Psychologie je tu chytřejší, než vypadá: do vypiplaného dema se recenzentům tluče těžko — vidí tvou dřinu a měkčí úsudek. Náčrt za pět minut nikoho nesvazuje, takže dostaneš syrový názor na *myšlenku*, nezamlžený zdvořilostí vůči odvedené práci. A přesně ten potřebuješ, dokud se dá směr měnit zadarmo. Autor s náčrtem obešel kamarády a nasbíral stránku poznámek [(7:04)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=424s) — v téhle fázi platí čím víc perspektiv, tím líp: každá odhalí jinou past nebo přinese vylepšení.

> **Pozn.:** „Nejkrutější lidi, co znám — moji kamarádi" je sympatická nadsázka: kamarádi bývají naopak nejshovívavější publikum (viz [sdílení práce](zacatky-bez-zkusenosti.md#sdileni-prace-neni-marketing-je-to-nastroj-uceni)). Low-fi forma jejich shovívavost částečně kompenzuje; opravdu tvrdá data přijdou až od cizích lidí.

**Souvislosti:** [Prototypování a vertical slice](prototypovani.md) · [Začátky bez zkušeností](zacatky-bez-zkusenosti.md) · [Rejstřík: low-fi prototyp](../rejstrik.md#low-fi-prototyp)

---

## Version control od nultého dne

**Zdroj:** [How To PROPERLY Start Making A Game](https://www.youtube.com/watch?v=ekOp35B1Bdg) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · stejné video, návod GitHub Desktop

**Shrnutí:** Version control jsou save pointy pro projekt: záchranné lano z každé katastrofy a zároveň deník pokroku. Nastavení přes GitHub Desktop je čtvrthodina práce i pro netechnického člověka — a návyk, který se má budovat od první hry, ne až od první ztracené práce.

### Rozpad myšlenky

Dvě služby, které verzování dělá [(7:42)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=462s): **návratové body** (rozbil jsem hru → vrátím se k poslednímu funkčnímu stavu) a **viditelný pokrok** — když máš pocit, že „nic nestíháš", historie commitů ukáže opak. Podceňovaná vzpruha pro dlouhé projekty.

Minimální setup podle videa [(8:31)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=511s): účet na GitHubu → GitHub Desktop → přidat složku projektu jako repository → při zakládání zvolit **.gitignore šablonu pro svůj engine** [(9:18)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=558s) (blokuje generované soubory, které do historie nepatří) → publish. Pak rytmus: změna → commit s krátkým popisem → push.

Nejdůležitější rada je o zrnitosti [(10:37)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=637s): **commituj malé celky**. Autor u minulé hry commitoval jen obří balíky změn a zpětně to označuje za past — velký commit se špatně popisuje, špatně vrací a při kolizi rozbije půl projektu. Malý commit je věta („added dog"), velký je slohovka, kterou nikdo nenapíše.

> **Pozn.:** Pro UE5 dvě doplnění z naší strany: Blueprinty jsou binární assety, takže diff mezi verzemi neuvidíš — o to důležitější jsou malé commity s popisnými zprávami, protože zpráva je jediné, co ti řekne, co se změnilo. A na velké assety (textury, audio) se hodí Git LFS; UE má navíc vestavěnou integraci Revision Control přímo v editoru.

**Souvislosti:** [Rejstřík: version control](../rejstrik.md#version-control) · budoucí kapitola o organizaci UE projektu (praxe)

---

## První build je placeholder city

**Zdroj:** [How To PROPERLY Start Making A Game](https://www.youtube.com/watch?v=ekOp35B1Bdg) · [Brainless.](https://www.youtube.com/channel/UCJmAuKzz_VHa3Yb7v19KIvQ) · stejné video, závěrečné zásady

**Shrnutí:** Největší žrout času autorovy minulé hry nebyl kód, ale art. Recept pro první verzi: všechno z placeholderů, vlastní grafiku jen tam, kde placeholder není — a schválně ošklivou, aby ses v ní nevrtal. Když hra baví s příšernou grafikou, s dobrou bude zářit; obráceně to neplatí.

### Rozpad myšlenky

Placeholder není ostuda, je to nástroj řazení priorit [(11:01)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=661s): dokud není jisté, že mechanika žije, každá hodina v grafice je sázka naslepo. Autorova pojistka proti vlastnímu perfekcionismu — dělat provizorní art *záměrně špatně* — zní jako vtip, ale řeší reálný problém: hezký provizorní asset svádí k ladění, ošklivý ne. (Jediná past: placeholdery z cizích her se do vydaného dema nesmí — buď volně použitelné assety, nebo vlastní čmáranice.)

**Organizace kódu** je druhá zásada [(11:50)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=710s): výmluva „můj kód nikdy nikdo neuvidí" ignoruje, že existuje budoucí já. Strašidelné pojmy jako state machine nebo containerization jsou jen vzory, jak kód uklidit — a základy, jednou naučené, se nezapomínají.

Třetí: **komunita**. Deset minut rozhovoru s někým, kdo problém zná, spolehlivě poráží hodiny tutoriálů a hledání [(12:22)](https://www.youtube.com/watch?v=ekOp35B1Bdg&t=742s) — a dávat zpětnou vazbu ostatním učí stejně jako ji dostávat.

> **Pozn.:** „If people like it with bad art, they'll love it with good art" má jednu výjimku, o které video nemluví: žánry, kde je estetika sama mechanikou (horor, atmosférické walking simy). Tam patří do prototypu i test nálady — ale pořád levný (osvětlení, zvuk), ne finální assety.

**Souvislosti:** [Produktivita: žrouti času](produktivita.md) · [Rejstřík: placeholder](../rejstrik.md#placeholder) · [Rejstřík: playtest](../rejstrik.md#playtest)
