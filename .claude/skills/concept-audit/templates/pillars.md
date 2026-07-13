# Pilíře jako akceptační kritéria

> **Jak s tímhle dokumentem pracovat**
>
> - **K čemu slouží:** Akceptační kritéria — věty, u kterých se pozná porušení. Test, kterým musí projít každý budoucí nápad na feature.
> - **Kdy:** Po/spolu s design-rationale — pilíře se destilují z derivace (kandidáti můžou vzejít už z intake §4). *(Pořadí: intake → design-rationale → **pillars**; audit = periodická kontrola.)*
> - **Jak:** Max 3–5, každý s „Poruší ho: <konkrétní rozhodnutí>". Pilíř, který nikdy nic nezamítl, přepiš — je moc měkký.
> - **Návaznost:** Čerpá z `design-rationale.md` (+ intake §4). Živý dokument — na rozdíl od rationale se průběžně přepisuje.

Pilíř je **krátká věta v přítomném čase, podle které se pozná porušení.** Není to slogan ani přání — je to test, který každý budoucí nápad na feature musí projít. Test dobrého pilíře: umíš okamžitě říct, co by ho porušilo? Pokud ne, je to marketing, ne pilíř.

## Formát

Maximálně 3–5 pilířů. Každý ve tvaru:

> **„<věta v přítomném čase>."**
> Poruší ho: _<konkrétní příklad rozhodnutí, které by pilíř zabilo>_

## Příklady tvaru

Z publikovaného derivačního řetězu ([derivace-izby](https://martinsafka.github.io/gamedev-skripta/zapisky/derivace-izby/)):

> **„Pohyb je jediná zbraň."**
> Poruší ho: přidání jakéhokoli útoku, pasti nebo předmětu, který řeší konfrontaci za hráče.

> **„Jsi kořist, ne bojovník."**
> Poruší ho: mechanika, po které se hráč přestane bát kontaktu (omráčení nepřítele, odlákání bez rizika).

## K čemu pilíře v auditu slouží

- Každá mechanika v konceptu se proti nim dá zkontrolovat: **podporuje / neutrální / porušuje.**
- Spor o feature se mění z „líbí × nelíbí" na „projde pilířem × neprojde".
- Pilíř, který nikdy nic nezamítl, nejspíš není pilíř — je moc měkký, přepiš ho.
