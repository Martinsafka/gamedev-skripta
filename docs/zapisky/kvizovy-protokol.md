# Kvízový protokol: znalost vs. automatizace

**Kontext:** Příprava na roli v programu, kde jsem měl vést juniory — vysvětlovat, mentorovat, částečně anglicky. Program mezitím skončil; protokol, který při přípravě vznikl, ho přežil a běží dál. Přesně proto stojí za zápisek: **příprava přetrvala příležitost.**

## Co se stalo

Diagnóza pojmenovala dvě různé mezery: **znalost** (testují ji otázky) a **automatizaci** (testuje ji mluvení pod tlakem). Věci, které „umíš", se pod tlakem rozpadají na jiných místech než věci, které neznáš — a každá mezera chce jiný trénink. Podle toho vznikly dva nástroje:

- **Kvízový protokol:** před každým větším úkolem jedna praktická otázka — teorie stacku, anglická slovní zásoba, nebo přesná terminologie (definovat termín / pojmenovat popsaný mechanismus, česky i anglicky). Eskalující obtížnost, slabá místa se vracejí, při časovém tlaku a incidentech se neblokuje. Mikroselhání na předpis, s okamžitou lekcí.
- **Mentoring roleplay v angličtině:** simulované konverzace s fiktivními juniory nad reálnými scénáři (over-engineering, motion matching vs. state machine v UE5). Odpovídat nanečisto, dostat korekturu, jazykové vzorce sledovat průběžně.

Hlavní nález roleplayů obrátil původní obavu (angličtina po letech ladem): **slovní zásoba nechybí — chybí gramatická lepidla.** Technický obsah i mentorský instinkt vycházely konzistentně dobře; mezera je úzká a mechanická, ne znalostní. Konkrétně: **signature error** `need/want + to + sloveso` („we want used it" → „we want *to* use it") — chyba se počítá nahlas a už se nevysvětluje, jen čítá, dokud nezmizí. **Strukturální mezera: pasivum.** „The state machine can still use for punch" → „can still *be used*"; kořen je česká zvratná konstrukce „se" („dá se použít"), která nemá anglický protějšek — vypadne, a zůstane chybné aktivum. Vzorec k automatizaci: *používá se / dá se použít* → *is used / can be used*. Pro roli tech leada kritické: popis systémů je z půlky pasivum („the component is called by…", „this can be reused for…"). A drobnost téže třídy: zdvojené sloveso v průběhovém tvaru („they are work" → „they work").

## Co si z toho beru

- **Rozlišuj znalost od automatizace** — a testuj každou jiným nástrojem: otázky vs. hraní role pod tlakem.
- **Chybám dávej jména a počítadla.** Chyba se jménem a pořadovým číslem se opravuje rychleji než anonymní překlep, protože má identitu — opakovaná chyba se neopravuje výkladem, ale viditelností.
- **Strukturální chyby hledej v mateřštině.** Nejtvrdší mezery v cizím jazyce nejsou slovíčka, ale místa, kde čeština řeší gramatiku jinak: zvratné „se", členy, pomocná slovesa.
- **Připravuj se na roli, ne na událost.** Role nenastala, dovednost zůstala: mentorská angličtina, protokol i návyk. Dovednosti jsou přenosné, příležitosti zastupitelné.

> **Pozn.:** Rejstřík téhle skripty je z definice zásobník kvízových otázek — každé heslo je dvojice „termín ↔ výklad", tedy přesně formát „definuj / pojmenuj". (V roadmapě na to čeká nápad quiz exportu pro spaced repetition.)

**Souvislosti:** [Selhávat citelně a čitelně](selhavat-citelne-a-citelne.md) *(kvíz = mikroselhání na předpis)* · [Karta selhání: packaging](karta-selhani-packaging.md) *(obrácená karta je kvíz z vlastních jizev — tenhle je z vlastních mezer)* · [Praxe: jak se učit engine](../praxe/editor-tipy.md#jak-se-ucit-engine-rady-po-peti-letech) *(učení vlastním projektem; tady učení vlastní mezerou)* · [Rejstřík](../rejstrik.md) *(zásobník otázek)*
