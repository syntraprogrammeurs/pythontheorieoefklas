<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 14.1 — Zes lussen omzetten

Uit *Python basis — theoriebundel*, hoofdstuk 14 (Comprehensions, kopie versus verwijzing), paragraaf 14.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b.py` | uitwerking |  |
| `uitwerking-c-deel-f-laat-je-met-rust.py` | uitwerking |  |
| `uitwerking-d-bij-for-titel-blz-in-boeken.py` | uitwerking |  |

## Opgave

**De situatie.** Je krijgt zes stukjes code die elk met een lus een lijst
opbouwen. Je schrijft ze om naar comprehensions, en bij één ervan beslis je dat
je dat beter niet doet.

```python
# A — alle titels in hoofdletters
titels = ["het diner", "turks fruit"]
uit = []
for t in titels:
    uit.append(t.upper())

# B — alleen de boeken van meer dan 200 bladzijden
boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]
uit = []
for titel, blz in boeken:
    if blz > 200:
        uit.append(titel)

# C — de lengte van elke titel, als dictionary
uit = {}
for titel, blz in boeken:
    uit[titel] = len(titel)

# D — alle verschillende beginletters
uit = set()
for titel, blz in boeken:
    uit.add(titel[0])

# E — de bladzijden, maar nooit meer dan 250 tellen
uit = []
for titel, blz in boeken:
    if blz > 250:
        uit.append(250)
    else:
        uit.append(blz)

# F — per boek een regel, met een tussenkop per beginletter
uit = []
vorige = ""
for titel, blz in sorted(boeken):
    if titel[0] != vorige:
        uit.append(f"--- {titel[0]} ---")
        vorige = titel[0]
    uit.append(f"{titel} ({blz})")
```

## Uitwerking

```python
boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]
titels = ["het diner", "turks fruit"]

a = [t.upper() for t in titels]
b = [titel for titel, blz in boeken if blz > 200]
c = {titel: len(titel) for titel, blz in boeken}
d = {titel[0] for titel, blz in boeken}
e = [min(blz, 250) for titel, blz in boeken]

print("A", a)
print("B", b)
print("C", c)
print("D", sorted(d))
print("E", e)
```

```text
A ['HET DINER', 'TURKS FRUIT']
B ['Het diner', 'De aanslag']
C {'Het diner': 9, 'Turks fruit': 11, 'De aanslag': 10}
D ['D', 'H', 'T']
E [250, 175, 246]
```

Vier van de vijf zijn rechttoe rechtaan. E verdient uitleg: er zijn twee
manieren om die te schrijven:

```python
boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]

met_min = [min(blz, 250) for titel, blz in boeken]
met_keuze = [250 if blz > 250 else blz for titel, blz in boeken]

print(met_min)
print(met_keuze)
print(met_min == met_keuze)
```

```text
[250, 175, 246]
[250, 175, 246]
True
```

De tweede is de letterlijke vertaling van de `if`-`else` uit de opgave; de
eerste zegt wat je bedoelt. Kies `min()`.

**F laat je met rust.**

```python
boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]

uit = []
vorige = ""
for titel, blz in sorted(boeken):
    if titel[0] != vorige:
        uit.append(f"--- {titel[0]} ---")
        vorige = titel[0]
    uit.append(f"{titel} ({blz})")

for regel in uit:
    print(regel)
```

```text
--- D ---
De aanslag (246)
--- H ---
Het diner (288)
--- T ---
Turks fruit (175)
```

Waarom niet in een comprehension? Drie redenen:

1. De lus voegt soms **twee** regels toe en soms één. Een comprehension geeft
   precies één element per ronde.
2. Er is een variabele `vorige` die van ronde tot ronde onthouden wordt. Een
   comprehension heeft geen geheugen tussen de rondes.
3. Ook al lukte het met een truc, dan nog zou niemand het kunnen lezen.

> De vuistregel: kun je de comprehension niet in één blik lezen, schrijf dan de
> lus. Kort is geen doel.

**Bij `for titel, blz in boeken` wordt `blz` in C en D niet gebruikt.** Je linter
merkt dat op. De afspraak in Python is om zo'n ongebruikte naam een liggend
streepje te geven:

```python
boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]

c = {titel: len(titel) for titel, _ in boeken}
print(c)
```

```text
{'Het diner': 9, 'Turks fruit': 11, 'De aanslag': 10}
```
