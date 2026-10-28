<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Python basis — de code uit de theoriebundel

Elke map hieronder bevat de code van één hoofdstuk uit *Python basis — theoriebundel*: de voorbeelden uit de uitleg en de klassikale oefeningen, genummerd zoals in de bundel. Niets hoeft nog overgetypt te worden.

## De hoofdstukken

| Hoofdstuk | Map | Voorbeelden | Klassikale oefeningen | Bestanden |
|---|---|---|---|---|
| 20 — Trends in programmeren | [hoofdstuk-20-trends](hoofdstuk-20-trends/) | 2 | 2 | 3 |
| 21 — DevOps, en waar Git daarin past | [hoofdstuk-21-devops](hoofdstuk-21-devops/) | 4 | 2 | 6 |
| 22 — Logica en kritisch denken: de basisbegrippen | [hoofdstuk-22-logica-basisbegrippen](hoofdstuk-22-logica-basisbegrippen/) | 1 | 2 | 1 |
| 23 — Propositielogica en waarheidstabellen | [hoofdstuk-23-propositielogica](hoofdstuk-23-propositielogica/) | 6 | 2 | 9 |
| 24 — Deductie: syllogismen, geldigheid en argumentvormen | [hoofdstuk-24-deductie](hoofdstuk-24-deductie/) | 4 | 2 | 5 |
| 25 — Deductief redeneren en je code | [hoofdstuk-25-deductie-en-code](hoofdstuk-25-deductie-en-code/) | 14 | 2 | 20 |
| 26 — Categorische logica en venndiagrammen | [hoofdstuk-26-categorische-logica](hoofdstuk-26-categorische-logica/) | 2 | 2 | 3 |
| 27 — Inductie, Mill's methods en kritisch denken | [hoofdstuk-27-inductie-en-kritisch-denken](hoofdstuk-27-inductie-en-kritisch-denken/) | 1 | 2 | 3 |
| 28 — Kritisch denken toegepast op softwaretesten | [hoofdstuk-28-kritisch-denken-en-testen](hoofdstuk-28-kritisch-denken-en-testen/) | 5 | 2 | 9 |
| 29 — Eindopdracht: alles samen | [hoofdstuk-29-eindopdracht](hoofdstuk-29-eindopdracht/) | 0 | 2 | 2 |
| | **Totaal** | **39** | **20** | **61** |

## Wat de namen betekenen

| Naam | Betekenis |
|---|---|
| `4.04-je-eerste-echte-programma.py` | Het codeblok uit paragraaf 4.4 |
| `4.05a-syntaxfout.py`, `4.05b-runtimefout.py` | Het eerste en het tweede codeblok uit paragraaf 4.5 |
| `4.08-klassikale-oefening-4.1-.../` | Klassikale oefening 4.1, in de bundel paragraaf 4.8 |
| `opgave.py` | De code die in de opgave staat |
| `uitwerking-a-fout-1-syntaxfout-regel-1.py` | Het eerste codeblok uit de uitwerking, met het opschrift waaronder het staat |
| `17.03-je-eigen-module/` | Een voorbeeld dat uit meer dan één bestand bestaat |
| `1.09-pyproject.toml` | Een instellingenbestand uit de uitleg |

In elke hoofdstukmap staat een `README.md` met alle bestanden per paragraaf en de commando's uit de uitleg. In elke oefenmap staat een `README.md` met de opgave en de volledige uitwerking.

## Wat er in een bestand staat

Bovenaan staat waar het in de bundel staat en de zin die het voorbeeld inleidt. Onderaan staat de uitvoer die de bundel erbij toont, als commentaar.

| In de kop | Betekenis |
|---|---|
| *loopt met opzet vast* | De foutmelding is het punt van het voorbeeld |
| *met opzet een fout tegen de schrijfregels* | Python start het bestand niet |
| *vraagt invoer* | Voer het uit in de terminal en typ mee |
| *bouwt verder op ...* | Een fragment uit de uitleg; de code waarop het verderbouwt, staat er eerst boven |
| *fragment* | Een stukje uit de uitleg dat niet op zichzelf draait |

## Uitvoeren

```bash
cd hoofdstuk-04-eerste-programma
python 4.04-je-eerste-echte-programma.py
```

De voorbeelden uit hoofdstuk 16 schrijven bestanden in de **huidige werkmap**. De afspeelknop van VS Code start vanuit de map van de werkruimte; wil je dat die bestanden naast het programma belanden, zet dan `"python.terminal.executeInFileDir": true` in `.vscode/settings.json`.

Krijg je op Windows een `UnicodeEncodeError` bij pijlen of wiskundige tekens, zet dan eerst `set PYTHONIOENCODING=utf-8`.

## Hoe deze mappen gemaakt zijn

Met `python gereedschap/theorie-uitpakken.py` in de cursusmap `pythonbasis`, uit dezelfde bron als de theoriebundel. Wijzig dus de bron in `theorie/bron/` en draai het gereedschap opnieuw. Wat je hier met de hand wijzigt in een `hoofdstuk-`-map, gaat bij de volgende keer verloren.

Na het uitpakken draait het gereedschap elk bestand dat zonder invoer kan draaien, en vergelijkt het de uitvoer met die in de bundel.
