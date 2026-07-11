# Dokumentace jako audit

**Kontext:** CLS_MM je moje Blueprint-only motion matching locomotion komponenta (UE 5.7, prodávaná na marketplace). Vznikala rychle a bez devlogu — a když přišel čas napsat k ní dokumentaci (interní referenci pro další vývoj + zákaznickou pro marketplace), ukázalo se, že akt psaní je něco víc než popis.

## Co se stalo

První nález přišel dřív, než začala práce: dva „technické" podklady se ukázaly být **byte-po-bytu identické** — omylem duplikát. Po-vývojová dokumentace fakticky neexistovala; jediný zdroj pravdy byl živý projekt. Z porovnání záměru (návrhový dokument z doby vývoje) s realitou (as-built stav) vzniklo třináct verifikačních otázek — enumy, struktura databází, tagy, křivky, interface signatury — a ověřovaly se **dotazy do běžícího editoru přes MCP**, ne klikací archeologií.

Výsledkem byla interní reference o dvanácti sekcích — a hlavně sekce **„Nesrovnalosti a dluh": čtrnáct nálezů**, které nevznikly hledáním bugů, ale psaním popisu. Tři z nich stojí za zobecnění:

- **Funkce může existovat, být správně napsaná — a nedělat nic.** Kritický nález: funkce aplikující hodnoty z profilů měla **nula call sites** v celém projektu. A neviditelný byl ten bug jen náhodou — defaultní hodnoty komponenty přesně seděly na hodnoty demo profilu, takže ukázková mapa fungovala. Lekce na doživotí: **write-path se testuje hodnotami, které se liší od defaultů.** Demo data shodná s defaulty maskují mrtvé dráty.
- **Write-only proměnná = rozmyšlená ochrana, nedotažená o jeden drát.** Proměnná chránící směr při zastavení se plnila, ale nikde nečetla. Symptom (lupnutí nohou při zastavení ze strafu) je přitom daleko od příčiny (úhel počítaný ze zbytkového vektoru). Blueprint projekty hromadí přesně tenhle typ dluhu stejně jako C++ — jen ho hůř vidí grep.
- **Prioritizace nálezů je produktová dovednost.** Taxonomie 🔴 funkční bug, který zákazník potká / 🟠 slibovaná featura jede naprázdno / 🟡 past v API / 🟢 kosmetika / 🔵 breaking change → odložit — se přímo mapuje na release plán s odhady času. A z nálezů rovnou vyrostla prevence: interní validátor animací (kontrola root motionu, loopingu, povinných křivek), který preventivně zabíjí nejčastější budoucí support ticket („postava klouže").

Nejdražší dopad měl první nález mimo komponentu: herní design IZBY staví na přesných oddělených rychlostech z profilů — a dokud bug nebyl opravený, **čísla v GDD byla přání, ne to, co engine produkuje**. Roadmapa vlastní technologie od té chvíle patří do závislostí design dokumentu explicitně.

## Co si z toho beru

- **Dokumentace je audit.** Popis as-built stavu mechanicky vytahuje dluh na světlo — levnější „hledání bugů" neznám.
- **Piš z artefaktu, ne ze záměru.** Návrhový dokument je záznam úmyslů; jediný zdroj pravdy je živý projekt. Rozdíl mezi nimi je seznam verifikačních otázek — a přesně ten seznam je začátek auditu.
- **Dvě publika = dva dokumenty.** Interní reference a zákaznická dokumentace sdílejí fakta, ne strukturu ani jazyk.
- U Blueprintů navíc: **devlog je jediný lidsky čitelný záznam změn** — binární diffy nic neřeknou; význam nese commit message a záznam o tom, co se změnilo *uvnitř* grafu.

> **Pozn.:** Stejná metoda se později nasadila proaktivně: když se u jiného projektu objevily tři bugy jedné třídy, následoval systematický audit celé té třídy — „tohle mapuje zbytek třídy" — místo tří izolovaných fixů. Dokumentace jako audit se dá povýšit z nálezu na návyk.

**Souvislosti:** [Selhávat citelně a čitelně](selhavat-citelne-a-citelne.md) *(seznam nálezů je učebnicový čitelný failure log)* · [Derivační řetěz IZBY](derivace-izby.md) *(proč komponenta vůbec vznikla)* · [Praxe: MM základy](../praxe/mm-zaklady.md) *(sparse setup — 70/30 sázka komponenty, kterou Epic později potvrdil hustotními tiery v GASP 5.7)* · [Praxe: GASP](../praxe/gasp.md) · [Rejstřík: motion matching](../rejstrik.md#motion-matching) · [Rejstřík: gameplay tag](../rejstrik.md#gameplay-tag)
