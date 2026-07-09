# První dojem: prvních deset vteřin po spuštění

Marketing nekončí kliknutím na „koupit" — první minuta po spuštění hry je pořád ještě první dojem. Tahle malá kapitola pokrývá tři detaily, které oddělují „levnou indie hru" od „hotového produktu" dřív, než hráč vůbec začne hrát.

---

## Splash, prázdná scéna a menu, které žije

**Zdroj:** [Your Game's First Impression Is Ruined By These Three Things](https://www.youtube.com/watch?v=s9VOnhQU1hE) · [Game Dev Guide](https://www.youtube.com/channel/UCR35rzd4LLomtQout93gi0w) · ~7 min, tutoriál s ukázkami

**Shrnutí:** Tři úpravy prvních vteřin [(0:04)](https://www.youtube.com/watch?v=s9VOnhQU1hE&t=4s): startuj do prázdné scény (hra se otevře okamžitě), vyhoď enginový splash screen a udělej si vlastní (a zábavný), a dej hlavnímu menu život. Hráč žádnou z nich vědomě nezaznamená — ale jejich absence se sčítá do pocitu lacinosti [(6:38)](https://www.youtube.com/watch?v=s9VOnhQU1hE&t=398s).

### Rozpad myšlenky

Mechanika problému (ukázáno v Unity, princip platí obecně): engine při startu schovává nahrávání první scény za svoje logo [(0:43)](https://www.youtube.com/watch?v=s9VOnhQU1hE&t=43s) — u těžké scény na slabším stroji hráč zírá na cizí branding a systém se tváří zamrzle. Řešení má dva kroky: **bootuj do prázdné (nebo vypnuté) scény** — ta se otevře vždycky okamžitě — a **vlastní splash** naveď až z ní; těžké scény pak nahrávej za vlastní loading obrazovkou, na svých podmínkách. Výsledek: hra reaguje od prvního kliknutí.

Druhá půlka je o tónu: splash a menu jsou první obrazovky hry, tak proč z nich dělat formality? Splash může být hračka [(3:49)](https://www.youtube.com/watch?v=s9VOnhQU1hE&t=229s) — autor do svého uvádí logo krátkou animací v energii celé hry. A menu [(5:53)](https://www.youtube.com/watch?v=s9VOnhQU1hE&t=353s) nepotřebuje AAA produkci: trocha animovaného UI, kamera na pozadí, tweening a hlavně **téma shodné s vibem hry** [(5:36)](https://www.youtube.com/watch?v=s9VOnhQU1hE&t=336s) — u jeho kreslené arkády komiksový styl à la sobotní ranní kreslák. Menu je obrazovka, kterou hráč uvidí stokrát; „funkční" je minimum, „příjemná" je levná konkurenční výhoda.

> **Pozn.:** Tohle je totéž pravidlo jako [emoce od prvních pěti minut](napad.md#core-dna-a-ctyri-emoce) — jen posunuté ještě před gameplay: emoční nastavení hry začíná ikonou na ploše. V UE je ekvivalent triviální (startup movie a lehká boot mapa v Project Settings); podstata rady je enginově nezávislá.

**Souvislosti:** [Nápad: core DNA a emoce](napad.md#core-dna-a-ctyri-emoce) · [Steam stránka](steam-stranka.md) · [Game feel a imerze](game-feel.md)
