<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Hoofdstuk 25 — Deductief redeneren en je code

De code uit hoofdstuk 25 van *Python basis — theoriebundel*, genummerd zoals in de bundel.

## Voorbeelden uit de uitleg

| Paragraaf | Bestand | Opmerking |
|---|---|---|
| 25.1 Elke functie is een belofte | `25.01a-elke-functie-is-een-belofte.py` |  |
| 25.1 Elke functie is een belofte | `25.01b-elke-functie-is-een-belofte.py` | loopt met opzet vast |
| 25.2 De aanname uitspreken met assert | `25.02a-de-aanname-uitspreken-met-assert.py` |  |
| 25.2 De aanname uitspreken met assert | `25.02b-de-aanname-uitspreken-met-assert.py` | loopt met opzet vast |
| 25.3 Waar assert wél en niet voor is | `25.03-waar-assert-wel-en-niet-voor-is.py` |  |
| 25.4 De lusinvariant | `25.04a-de-lusinvariant.py` |  |
| 25.4 De lusinvariant — De invariant van binair zoeken | `25.04b-de-invariant-van-binair-zoeken.py` |  |
| 25.5 De if-keten is een redenering | `25.05-de-if-keten-is-een-redenering.py` |  |
| 25.6 De vier logicafouten in if-ketens — Fout 1 — de else die te veel aanneemt | `25.06a-fout-1-de-else-die-te-veel-aanneemt.py` |  |
| 25.6 De vier logicafouten in if-ketens — Fout 2 — overlappende takken | `25.06b-fout-2-overlappende-takken.py` |  |
| 25.6 De vier logicafouten in if-ketens — Fout 3 — de onbereikbare tak | `25.06c-fout-3-de-onbereikbare-tak.py` |  |
| 25.6 De vier logicafouten in if-ketens — Fout 4 — het ontbrekende geval | `25.06d-fout-4-het-ontbrekende-geval.py` |  |
| 25.6 De vier logicafouten in if-ketens — Fout 4 — het ontbrekende geval | `25.06e-fout-4-het-ontbrekende-geval.py` | fragment, draait niet los |
| 25.7 Bewaakclausules: de contrapositie in code | `25.07-bewaakclausules-de-contrapositie-in-code.py` |  |

## Klassikale oefeningen

| Oefening | Map | Bestanden |
|---|---|---|
| 25.1 — Vier fouten in één keten | [25.09-klassikale-oefening-25.1-vier-fouten-in-een-keten](25.09-klassikale-oefening-25.1-vier-fouten-in-een-keten/) | `opgave.py`, `uitwerking-a-3-de-herschreven-functie.py`, `uitwerking-b-4-de-controles.py` |
| 25.2 — De invariant die een fout blootlegt | [25.10-klassikale-oefening-25.2-de-invariant-die-een-fout-blootlegt](25.10-klassikale-oefening-25.2-de-invariant-die-een-fout-blootlegt/) | `opgave.py`, `uitwerking-a-2-waar-de-invariant-breekt.py`, `uitwerking-b-3-de-herstelde-functie.py` |

## Commando's uit de uitleg

**25.3 Waar assert wél en niet voor is**

```bash
python programma.py       # de asserts doen hun werk
python -O programma.py    # alle asserts zijn weg
```

**25.13 Wat je nu kunt**

```bash
git add logica/contracten.py logica/controle.py
git commit -m "Schrijf pre- en postcondities uit en herstel vier fouten in de boeteketen"
git push
```
