# Devlogy: marketing, který je sám řemeslem

Devlog — video o vývoji vlastní hry — je oblíbený marketingový kanál indie vývojářů a zároveň žánr plný mizerných exemplářů. Autor Isidora's Edge natočil obojí (a měří si to), takže jeho rady stojí na číslech: co dělá devlog sledovatelným a jak ho vyrobit, aniž by sežral vývoj samotný.

---

## Devlog stojí a padá se scénářem

**Zdroj:** [The Problem with Indie Game Devlogs on Youtube](https://www.youtube.com/watch?v=48C9hYoLMis) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · ~15 min, návod s vlastními čísly

**Shrnutí:** Nejtvrdší datový bod videa: autorových 15 skriptovaných devlogů průměruje ~45 000 zhlédnutí, 9 neskriptovaných ~9 000 [(3:05)](https://www.youtube.com/watch?v=48C9hYoLMis&t=185s) — **pětinásobný rozdíl** [(3:13)](https://www.youtube.com/watch?v=48C9hYoLMis&t=193s). Bez scénáře vzniká nesouvislé mumlání, které opakuje nepodstatné a vynechává zajímavé. Scénář ale neznamená slohovku čtenou do mikrofonu.

### Rozpad myšlenky

Třífázový proces psaní [(3:36)](https://www.youtube.com/watch?v=48C9hYoLMis&t=216s):

1. **Odrážkový outline** — všechno, co by ve videu mohlo být: hlavní updaty, zábavné bugy, vtipy.
2. **Definice flow** [(3:56)](https://www.youtube.com/watch?v=48C9hYoLMis&t=236s) — seřadit odrážky do pořadí *prezentace* a napsat přechody mezi tématy; přesně tenhle krok odděluje video od odškrtávaného checklistu a dává mu jednu souvislou linku.
3. **Psaní nahlas** [(4:47)](https://www.youtube.com/watch?v=48C9hYoLMis&t=287s) — autor si sedne, *předstírá, že natáčí*, riffuje varianty vět a zapisuje ty, které zní dobře. Výsledný scénář je doslovný, ale zní mluveně, ne čteně.

O čem psát? Devlog umí dvě věci [(5:45)](https://www.youtube.com/watch?v=48C9hYoLMis&t=345s): **showcase** (vyber zajímavou featuru a projdi ji celou: proč byla potřeba → učení → implementace → bugy → výsledek; pak smaž všechno kromě nejzajímavějších kousků) a **story** (vyprávěj příběh vývoje — jeho nejúspěšnější devlog je příběh o *potížích* se svahy [(7:26)](https://www.youtube.com/watch?v=48C9hYoLMis&t=446s), ne showcase rozhodnutí je zrušit). Nejlepší devlogy obojí mísí [(8:16)](https://www.youtube.com/watch?v=48C9hYoLMis&t=496s) — a mimochodem: outline fáze funguje i jako detektor — u hitbox systému čekal nudu, outline odhalil dost odrážek na jeden z nejúspěšnějších dílů [(6:38)](https://www.youtube.com/watch?v=48C9hYoLMis&t=398s).

> **Pozn.:** Struktura showcase (proč → proces → výsledek → limity) je skoro 1:1 šablona našich „Rozpadů myšlenky" — dobrý devlog a dobrá studijní kapitola jsou příbuzné žánry. A pozor na půvabný detail: video samo je story-devlog o devlozích, který showcasuje vlastní metodu.

**Souvislosti:** [Postmortem ShantyTown](postmortem-shantytown.md) *(devlogy provázely celý vývoj)* · [Idea iceberg: the Gap](rady-z-praxe.md#the-gap-rozdil-mezi-to-je-hezky-a-tohle-musim-hrat) · [Rejstřík: devlog](../rejstrik.md#devlog)

---

## Ukazuj hru: záběry z commitů a studium cizích videí

**Zdroj:** [The Problem with Indie Game Devlogs on Youtube](https://www.youtube.com/watch?v=48C9hYoLMis) · [Inbound Shovel](https://www.youtube.com/channel/UCdYwjLVP-98bptdlQFO_5zQ) · stejné video, produkce

**Shrnutí:** Na obrazovce má být hra — pořád [(8:46)](https://www.youtube.com/watch?v=48C9hYoLMis&t=526s). Autor dostával pod každým devlogem komentář „ukaž víc gameplaye", přidal, a komentář přišel znovu — dokud footage nebylo násobně víc, než považoval za nutné [(9:12)](https://www.youtube.com/watch?v=48C9hYoLMis&t=552s). A geniálně jednoduchý trik, kde vzít záběry starších verzí: version control.

### Rozpad myšlenky

Meme o Subway Surfers ve videích má reálné jádro: mozek diváka potřebuje pohyb — tak mu dej **vlastní hru** [(8:58)](https://www.youtube.com/watch?v=48C9hYoLMis&t=538s), ideálně přesně to, o čem zrovna mluvíš, jinak aspoň obecný B-roll. Průběžné nahrávání všeho je logistické peklo (terabajty, hledání); místo toho **checkout starých commitů** [(10:07)](https://www.youtube.com/watch?v=48C9hYoLMis&t=607s): po dopsání scénáře si autor projde skript, sepíše seznam potřebných záběrů, a natočí je skákáním po commit historii [(10:50)](https://www.youtube.com/watch?v=48C9hYoLMis&t=650s) — každá etapa hry je kdykoli k dispozici. Čím popisnější commit messages, tím snazší hledání (jeho vlastní „a bunch of stuff" dává za odstrašující příklad) — další argument pro [malé commity](jak-zacit.md#version-control-od-nulteho-dne).

Druhá rada je studijní: **dobrý devlog je z definice dobré video** [(13:30)](https://www.youtube.com/watch?v=48C9hYoLMis&t=810s) — a názor na to, co je dobré video, se buduje stejně jako designový vkus: sledováním a analýzou. Jeho učitelé: Jonas Tyroller (rámování témat tak, aby zajímala i ne-vývojáře), Sebastian Lague [(11:54)](https://www.youtube.com/watch?v=48C9hYoLMis&t=714s) (nebát se jít do technické hloubky — divákům se to líbí a technické devlogy se mu i líp píšou) a kuchařský kanál Internet Shaquille [(13:05)](https://www.youtube.com/watch?v=48C9hYoLMis&t=785s) — instruktážní řemeslo se přenáší napříč obory. A závěrem realistická laťka: první devlogy budou špatné [(14:30)](https://www.youtube.com/watch?v=48C9hYoLMis&t=870s) — jeho byly — a stojí za to je dělat stejně; proti gatekeepingu „devlogy nechte profíkům" [(0:13)](https://www.youtube.com/watch?v=48C9hYoLMis&t=13s) se video vymezuje celé.

> **Pozn.:** Devlogy nejsou povinnost — jsou jeden z marketingových kanálů a žere čas jako každé druhé řemeslo. Rozhodovací vodítko z [postmortemu](postmortem-shantytown.md#wishlisty-next-fest-a-ticho-po-launchi): dělej je, pokud tě baví *videa*, ne pokud čekáš automatické wishlisty.

**Souvislosti:** [Start projektu: version control](jak-zacit.md#version-control-od-nulteho-dne) · [Proč tvořit: komunita](proc-tvorit.md#ego-komunita-a-pece-o-sebe) · [Rejstřík: devlog](../rejstrik.md#devlog) · [Rejstřík: B-roll](../rejstrik.md#b-roll)
