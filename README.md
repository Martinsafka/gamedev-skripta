# gamedev skripta

Studijní skripta herního vývoje psaná samoukem pro samouky — destilát znalostí z rozsáhlého studijního playlistu a z deníků vlastních projektů.

**Web:** _(doplní se po nasazení GitHub Pages)_

## Co tu je

- **Teorie her** — game design, psychologie hráče, proces tvorby.
- **Praxe v UE5** — konkrétní postupy a systémy v Unreal Enginu 5.
- **Zápisky** — anonymizované lekce z reálného vývoje vlastních projektů.
- **Rejstřík** — odborné termíny (anglicky) s českým výkladem a odkazy do kontextu.

Každá kapitola vychází z konkrétních videí, která jsou uvedena jako zdroje s odkazy na autory a přímo na relevantní časy ve videu. Text je vlastní syntéza a výklad — chceš-li vidět demonstraci, klikni na zdroj; tvůrcům patří dík a návštěva jejich kanálů.

## Pro agenty a přispěvatele

Vstupní bod je `AGENTS.md` (metodika v `agent_docs/`). Surové přepisy a osobní podklady se do repa **nikdy** necommitují — viz licenční invarianty v `AGENTS.md`.

## Lokální build

```bash
pip install mkdocs-material
mkdocs serve        # http://127.0.0.1:8000
mkdocs build --strict
```
