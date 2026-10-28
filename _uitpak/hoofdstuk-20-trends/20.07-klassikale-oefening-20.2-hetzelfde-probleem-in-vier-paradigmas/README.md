<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 20.2 — Hetzelfde probleem in vier paradigma's

Uit *Python basis — theoriebundel*, hoofdstuk 20 (Trends in programmeren), paragraaf 20.7.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** Je lost één probleem op vier manieren op, om te zien wat een
paradigma concreet betekent.

**Het probleem.** Gegeven een lijst boeken met titel en aantal bladzijden: geef
de titels van alle boeken van meer dan 250 bladzijden, in hoofdletters,
alfabetisch gesorteerd.

**Wat je doet.** Schrijf de oplossing:

1. Procedureel, met lussen.
2. Functioneel, met `filter`, `map` en `sorted`.
3. Met een comprehension, de Python-manier.
4. Objectgeoriënteerd, met een klasse `Catalogus`.

Zeg daarna welke je in een project zou zetten, en waarom.

## Uitwerking

```python
# De Leeslamp — één probleem, vier stijlen
# Cursus Python basis, hoofdstuk 20, oefening 2

BOEKEN = [
    ("Turks fruit", 175),
    ("De ontdekking van de hemel", 928),
    ("Het diner", 288),
    ("De aanslag", 246),
    ("Max Havelaar", 340),
    ("Bint", 96),
]
GRENS = 250


# 1 — procedureel
def dikke_titels_procedureel(boeken, grens):
    """Met lussen, stap voor stap."""
    uit = []
    for titel, bladzijden in boeken:
        if bladzijden > grens:
            uit.append(titel.upper())
    uit.sort()
    return uit


# 2 — functioneel
def dikke_titels_functioneel(boeken, grens):
    """Met filter, map en sorted."""
    dik = filter(lambda b: b[1] > grens, boeken)
    titels = map(lambda b: b[0].upper(), dik)
    return sorted(titels)


# 3 — met een comprehension
def dikke_titels_comprehension(boeken, grens):
    """De Python-manier."""
    return sorted(titel.upper() for titel, blz in boeken if blz > grens)


# 4 — objectgeoriënteerd
class Catalogus:
    """Een verzameling boeken met bevragingen erop."""

    def __init__(self, boeken):
        self.boeken = list(boeken)

    def dikker_dan(self, grens):
        """Een nieuwe catalogus met alleen de dikke boeken."""
        return Catalogus(b for b in self.boeken if b[1] > grens)

    def titels(self):
        """De titels, in hoofdletters en gesorteerd."""
        return sorted(titel.upper() for titel, _ in self.boeken)

    def __len__(self):
        return len(self.boeken)


resultaten = {
    "procedureel": dikke_titels_procedureel(BOEKEN, GRENS),
    "functioneel": dikke_titels_functioneel(BOEKEN, GRENS),
    "comprehension": dikke_titels_comprehension(BOEKEN, GRENS),
    "objectgericht": Catalogus(BOEKEN).dikker_dan(GRENS).titels(),
}

for stijl, uitkomst in resultaten.items():
    print(f"{stijl:<16}{uitkomst}")

print()
print("Alle vier gelijk:", len(set(map(tuple, resultaten.values()))) == 1)
```

```text
procedureel     ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
functioneel     ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
comprehension   ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']
objectgericht   ['DE ONTDEKKING VAN DE HEMEL', 'HET DINER', 'MAX HAVELAAR']

Alle vier gelijk: True
```

**Wat elke stijl je laat zien.**

| Stijl | Regels | Sterkte | Zwakte |
|---|---|---|---|
| Procedureel | 6 | Elke stap staat er letterlijk | Veel ruis: een lege lijst, een `append`, een `sort` |
| Functioneel | 3 | Elke stap is een aparte bewerking | `lambda b: b[1]` zegt niet wat `b[1]` is |
| Comprehension | 1 | Kort en leesbaar | Wordt onleesbaar zodra er meer bij komt |
| Objectgericht | 12 | `catalogus.dikker_dan(250).titels()` leest als een zin | Veel code voor één bevraging |

**Welke in een project?**

Voor deze ene bevraging: de **comprehension**. Eén regel, en iedereen die Python
kent, leest ze.

Zodra er meer bevragingen bij komen — op schrijver, op jaar, op beschikbaarheid,
op categorie — kantelt dat naar de **klasse**. Dan schrijf je de gegevens één
keer op en krijg je er een handvol methodes bij, in plaats van tien losse
functies die allemaal `boeken` als eerste argument nemen.

Dat is de echte betekenis van een paradigma: geen geloofskwestie maar een keuze
die met de omvang van je probleem meegroeit.

**Waarom de functionele versie hier verliest.** `lambda b: b[1] > grens` is
korter dan de lus, maar `b[1]` zegt niet dat het om bladzijden gaat. In een taal
die voor functioneel programmeren gemaakt is, heb je daar betere middelen voor.
In Python is de comprehension de leesbaardere vertaling van hetzelfde idee.
