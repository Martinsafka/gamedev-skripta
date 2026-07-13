# Design Rationale — skeleton derivačního řetězu

> **Jak s tímhle dokumentem pracovat**
>
> - **K čemu slouží:** Záznam uvažování za konceptem (rozhodnutí → alternativy → proč zamítnuty). Bez něj se hotový GDD čte jako objednávka, s ním jako uvažování kolegy.
> - **Kdy:** Po intake (nebo po auditu, který ukázal díry v řetězu). Hlavní učební artefakt. *(Pořadí: intake → **design-rationale** → pillars; audit = periodická kontrola.)*
> - **Jak:** Jedna karta na rozhodnutí. Zamítnuté alternativy se nemažou. Datuj větší revize — je to snímek v čase, ne živá wiki.
> - **Návaznost:** Čerpá ze zadání v `intake.md`; odkazuje na `pillars.md` jako akceptační kritéria řetězu.

Záznam uvažování, které vedlo ke konceptu — psaný pro čtenáře, který u toho nebyl (včetně tvého budoucího já). **Hotový dokument maže vlastní historii:** bez derivace se čte jako objednávka, s derivací jako uvažování kolegy. Ukázkový hotový řetěz: [Derivační řetěz: od zadání k žánru](https://martinsafka.github.io/gamedev-skripta/zapisky/derivace-izby/).

## Zadání

Odkud projekt je: impuls, tvrdá omezení, priorita (např. „učební artefakt na prvním místě, produkt na druhém"). Zadání je soudce všech sporů níž.

## Řetěz rozhodnutí

Jedna karta na rozhodnutí, v pořadí, jak skutečně padala:

### Rozhodnutí: _<co platí — jedna věta>_

- **Zvažované alternativy:** _<co bylo na stole>_
- **Proč zamítnuty:** _<skutečný důvod — „stamina místo zdraví kvůli stromu závislostí", ne „líbilo se mi víc">_
- **Co mě to učí:** _<dovednost/znalost, kterou rozhodnutí trénuje nebo vyžaduje>_
- **Typ dveří:** one-way / two-way _(one-way = drahé na reverz → má vlastníka, vyslovené premisy a okno, kdy se smí znovu otevřít; viz [rejstřík](https://martinsafka.github.io/gamedev-skripta/rejstrik/#one-way-door))_
- **Premisy:** _<na čem rozhodnutí stojí — a jak by šla každá premisa vyvrátit testem (prototyp, playtest, výpočet), ne výrokem>_

## Pravidla dokumentu

- **Zamítnuté alternativy se nemažou** — důvod zamítnutí je taky znalost.
- Alternativa bez důvodu zamítnutí je díra v řetězu, ne úspora místa.
- Datuj větší revize; derivace je záznam v čase, ne živá wiki stránka.
- Pilíře drž zvlášť (šablona `pillars.md`) a odkazuj na ně — jsou to akceptační kritéria řetězu.
