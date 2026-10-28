<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Hoofdstuk 19 — Grafische programma's met `tkinter`

De code uit hoofdstuk 19 van *Python basis — theoriebundel*, genummerd zoals in de bundel.

Elk programma in dit hoofdstuk opent een venster en geeft geen uitvoer in de
terminal. Wat je hoort te zien, staat in de `.png` met dezelfde naam als het
`.py`-bestand: de schermafdruk uit de bundel.

## Voorbeelden uit de uitleg

| Paragraaf | Bestand | Opmerking |
|---|---|---|
| 19.2 Je eerste venster | `19.02-je-eerste-venster.py` | opent een venster |
| 19.3 Widgets: de bouwstenen van een venster | `19.03-widgets-de-bouwstenen-van-een-venster.py` | opent een venster |
| 19.4 Een knop die iets doet | `19.04a-een-knop-die-iets-doet.py` | opent een venster |
| 19.4 Een knop die iets doet — Een knop die een argument meegeeft | `19.04b-een-knop-die-een-argument-meegeeft.py` | opent een venster |
| 19.5 Invoer lezen en meldingen tonen | `19.05-invoer-lezen-en-meldingen-tonen.py` | opent een venster |
| 19.6 Netjes schikken met grid | `19.06a-netjes-schikken-met-grid.py` | opent een venster |
| 19.6 Netjes schikken met grid — Sneltoets | `19.06b-sneltoets-enter.py` | fragment, draait niet los |
| 19.7 Je venster als klasse | `19.07a-je-venster-als-klasse.py` | fragment, draait niet los |
| 19.7 Je venster als klasse | `19.07b-je-venster-als-klasse.py` | opent een venster |
| 19.11 Veelgemaakte fouten | `19.11-veelgemaakte-fouten.py` | fragment, draait niet los |

## Klassikale oefeningen

| Oefening | Map | Bestanden |
|---|---|---|
| 19.1 — De lidgeldcalculator | [19.09-klassikale-oefening-19.1-de-lidgeldcalculator](19.09-klassikale-oefening-19.1-de-lidgeldcalculator/) | `uitwerking.py`, `berekeningen.py` |
| 19.2 — Zoeken in de catalogus | [19.10-klassikale-oefening-19.2-zoeken-in-de-catalogus](19.10-klassikale-oefening-19.2-zoeken-in-de-catalogus/) | `uitwerking.py` |

## Commando's uit de uitleg

**19.1 Van de terminal naar een venster**

```bash
python -m tkinter
```

Op Linux, als je `ModuleNotFoundError: No module named 'tkinter'` krijgt:

```bash
sudo apt install python3-tk
```

**19.13 Wat je nu kunt**

```bash
git add .
git commit -m "Voeg vensters toe voor het lidgeld en de catalogus"
git push
```
