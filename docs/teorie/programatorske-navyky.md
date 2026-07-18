# Programátorské návyky: malé věci, které se skládají

Vedle mentálních modelů ([Programátorské myšlení](programatorske-mysleni.md)) existuje druhá, nenápadnější páka: drobné návyky, které „vypadají moc malé na to, aby byly důležité" — a právě proto je skoro nikdo nedělá. Tahle kapitola destiluje patnáct návyků z videa Manware do tří mechanismů: paměť a důkaz, růstové sázky, tělo a prostředí.

---

## Patnáct malých návyků, tři mechanismy

**Zdroj:** [15 Tiny Coding Hacks That Got Me In Amazon](https://www.youtube.com/watch?v=Z36-xqUv3W8) · [Manware](https://www.youtube.com/channel/UCEihg8EpedxZKQ_Gm1XVedg) · ~10 min, osobní seznam návyků

**Shrnutí:** Žádný jednorázový skok, který tě „instantně předřadí před 99 % programátorů", neexistuje [(0:02)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=2s) — kariéru podle autora změnily mikronávyky s téměř nulovým úsilím, které se rok skládají úrokem. Seznam je psaný pro kariérního programátora, ale mechanismy pod ním jsou stejné pro samouka v gamedevu: zhmotňuj, co ses naučil; sázej na věci, co tě přerostou; a nesabotuj vlastní hardware.

### Rozpad myšlenky

**Paměť a důkaz** — návyky, které učení zhmotňují:

- **Commit každý večer** [(0:48)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=48s): nejde o GitHub trávník pro recruitery, ale o dvojí efekt — hmatatelný „proof of work" a hlavně **vybavovací trénink**: shrnout den do commit message znamená znovu si projít, co jsi vyřešil.
- **TIL.md** [(3:56)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=236s): obyčejný soubor „today I learned", jedna řádka na poznatek. Kondenzace na větu ukládá do dlouhodobé paměti — a zpětné čtení ukazuje ujetou vzdálenost. Žádné notion šablony; prostý append.
- **Vysvětluj druhým** [(3:56)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=236s): autorův učitel to rámoval čísly — poslech ≈ 20 % porozumění, zápis ≈ 40 %, výuka ≈ 90 %. Kdo neumí zjednodušit, nerozumí. (Devlog je přesně tenhle návyk v masce marketingu — viz [Devlogy](devlogy.md).)
- **Mluv o problémech nahlas** [(2:22)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=142s): kamarád vidí z ptačí perspektivy; půlku řešení najdeš už tím, že problém formuluješ — klasická gumová kachna, plus sounáležitost, která drží u řemesla.

**Růstové sázky** — kam mířit úsilí:

- **Stav projekty, které zní nemožně** [(1:34)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=94s): CRUD appka po desáté nenaučí nic; „nevím, jak se staví engine" je dobrý důvod ho zkusit — většina „nemožných" věcí je zdokumentovaný proces krok za krokem. Ne víc úsilí, jiná cesta.
- **Čti denně kus kódu někoho lepšího** [(0:48)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=48s): romanopisec čte bestsellery. Pět minut, sto řádků, tři otázky: jak pojmenovávají? jak řeší chyby? co je ten divný syntax?
- **Pěstuj nespokojenost** [(4:42)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=282s): inženýry podle autora neodděluje IQ ani talent, ale neschopnost nechat věc být, dokud nevíš, **jak funguje pod kapotou**. (Celá kapitola o [Quake 3 odmocnině](matematika-pro-gamedev.md#pripadovka-rychla-inverzni-odmocnina-z-quake-3) je pomník téhle vlastnosti.)
- **Dělej na tom, na čem ti záleží** [(5:28)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=328s): kód jen pro peníze = burnout; kód jako dovednost + zábava + obživa = udržitelnost. Máš-li rád hry, stav hry — programování je nástroj do libovolného oboru.
- **Neporovnávej se** [(8:36)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=516s): každý startuje s jinými buffy; jediná proměnná pod tvou kontrolou je tvůj vlastní skill gap.

**Tělo a prostředí** — hardware, na kterém to celé běží:

- **Spánek** [(7:49)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=469s): 18+ hodin vzhůru ≈ výkon opilého člověka; ponocování není flex, ale „soutěž v hlouposti". Spánek konsoliduje paměť („RAM se zapisuje na SSD") — hodina spánku navíc porazí hodinu nočního učení.
- **Telefon do jiné místnosti** [(4:42)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=282s): přítomnost v místnosti = trvalý debuff vůle; udělej používání *fyzicky* těžké.
- **Plánuj jako senior** [(7:01)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=421s): 80 % plánování, 20 % stavění — rozhodnutí udělaná předem (schéma, rozhraní, pořadí práce) nepřerušují flow a nekončí refactoringem. Srovnej s [devlogem jako mapou](../zapisky/devlog-jako-mapa.md) a [pravidlem 70/30](../zapisky/pravidlo-70-30.md).
- Drobné: klidná nerepetitivní hudba proti kortizolu [(6:15)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=375s), Vim motions jako gamifikace psaní [(2:22)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=142s) („internet křivku učení přehání" — 15 minut základů), a klávesnice, u které tě psaní baví [(8:36)](https://www.youtube.com/watch?v=Z36-xqUv3W8&t=516s).

> **Pozn.:** Kontext videa je kariérní sprint do Amazonu — ne gamedev, a je fér to vědět. Mechanismy ale sedí přesně na potíže samouka popsané v [Žroutech času](produktivita.md): práce bez validace je porušený návyk „důkazu", únik k snadné tvorbě je prohraná růstová sázka. A commit-každý-večer + TIL.md je nejlevnější devlog na světě.

**Souvislosti:** [Žrouti času](produktivita.md) · [Devlogy](devlogy.md) · [Zápisek: Devlog jako mapa](../zapisky/devlog-jako-mapa.md) · [Zápisek: Pravidlo 70/30](../zapisky/pravidlo-70-30.md)
