<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 14.2 — De gedeelde leeslijst

Uit *Python basis — theoriebundel*, hoofdstuk 14 (Comprehensions, kopie versus verwijzing), paragraaf 14.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking-a-1-de-uitvoer.py` | uitwerking |  |
| `uitwerking-b-3-de-herstelling.py` | uitwerking |  |
| `uitwerking-c-4-dezelfde-fout-anders.py` | uitwerking |  |
| `uitwerking-d-4-dezelfde-fout-anders.py` | uitwerking |  |
| `uitwerking-e-5-een-lid-kopieren.py` | uitwerking |  |

## Opgave

**De situatie.** Dit programma zou elk lid een eigen leeslijst moeten geven. Het
doet iets anders, en je gaat uitzoeken wat.

```python
def maak_lid(naam, gelezen=[]):
    return {"naam": naam, "gelezen": gelezen}


anke = maak_lid("Anke")
bram = maak_lid("Bram")

anke["gelezen"].append("Het diner")

print(anke)
print(bram)
```

**Wat je doet.**

1. Voorspel de uitvoer. Voer daarna uit.
2. Leg uit wat er gebeurt, met een tekening van namen en objecten.
3. Herstel het.
4. Maak daarna een tweede fout na: geef beide leden dezelfde bestaande lijst mee
   en toon dat het hetzelfde probleem geeft.
5. Schrijf een functie `kopieer_lid(lid)` die een lid kopieert zonder dat de
   twee elkaars leeslijst delen.

## Uitwerking

**1 — De uitvoer.**

```python
def maak_lid(naam, gelezen=[]):
    return {"naam": naam, "gelezen": gelezen}


anke = maak_lid("Anke")
bram = maak_lid("Bram")

anke["gelezen"].append("Het diner")

print(anke)
print(bram)
```

```text
{'naam': 'Anke', 'gelezen': ['Het diner']}
{'naam': 'Bram', 'gelezen': ['Het diner']}
```

Bram heeft *Het diner* gelezen zonder dat iemand dat vroeg.

**2 — Wat er gebeurt.**

De standaardwaarde `[]` wordt **één keer** aangemaakt, op het moment dat Python
de regel `def maak_lid(...)` uitvoert. Elke aanroep zonder tweede argument
krijgt daarna **diezelfde** lijst.

```text
maak_lid.standaardwaarde ──┐
                           ├──► [ 'Het diner' ]
anke["gelezen"]  ──────────┤
bram["gelezen"]  ──────────┘
```

Drie namen, één lijst. Dit is de valkuil uit hoofdstuk 11 en de verwijzing uit
14.4, samen in één regel.

**3 — De herstelling.**

```python
def maak_lid(naam: str, gelezen: list = None) -> dict:
    """Maakt een lid met een eigen, lege leeslijst."""
    if gelezen is None:
        gelezen = []
    return {"naam": naam, "gelezen": gelezen}


anke = maak_lid("Anke")
bram = maak_lid("Bram")
anke["gelezen"].append("Het diner")

print(anke)
print(bram)
```

```text
{'naam': 'Anke', 'gelezen': ['Het diner']}
{'naam': 'Bram', 'gelezen': []}
```

Nu wordt de lege lijst bij **elke aanroep** opnieuw gemaakt.

**4 — Dezelfde fout, anders veroorzaakt.**

```python
def maak_lid(naam: str, gelezen: list = None) -> dict:
    """Maakt een lid met een eigen, lege leeslijst."""
    if gelezen is None:
        gelezen = []
    return {"naam": naam, "gelezen": gelezen}


start = ["Max Havelaar"]
anke = maak_lid("Anke", start)
bram = maak_lid("Bram", start)

anke["gelezen"].append("Het diner")

print(anke)
print(bram)
print(start)
```

```text
{'naam': 'Anke', 'gelezen': ['Max Havelaar', 'Het diner']}
{'naam': 'Bram', 'gelezen': ['Max Havelaar', 'Het diner']}
['Max Havelaar', 'Het diner']
```

De functie is nu correct, en toch gaat het mis. De aanroeper gaf twee keer
**dezelfde lijst** mee. Dat kun je in de functie oplossen:

```python
def maak_lid(naam: str, gelezen: list = None) -> dict:
    """Maakt een lid met een eigen leeslijst, ook bij een meegegeven lijst."""
    return {"naam": naam, "gelezen": list(gelezen or [])}


start = ["Max Havelaar"]
anke = maak_lid("Anke", start)
bram = maak_lid("Bram", start)
anke["gelezen"].append("Het diner")

print(anke)
print(bram)
print(start)
```

```text
{'naam': 'Anke', 'gelezen': ['Max Havelaar', 'Het diner']}
{'naam': 'Bram', 'gelezen': ['Max Havelaar']}
['Max Havelaar']
```

Bram is nu in orde en `start` ook.

> Merk op: `list(gelezen or [])` doet twee dingen. `or []` vangt `None` op, en
> `list(...)` maakt een kopie. De vorm is kort; schrijf hem uit als je hem niet
> in één blik leest.

**5 — Een lid kopiëren.**

```python
def kopieer_lid(lid: dict) -> dict:
    """Een kopie van een lid, met een eigen leeslijst."""
    nieuw = lid.copy()
    nieuw["gelezen"] = lid["gelezen"].copy()
    return nieuw


anke = {"naam": "Anke", "gelezen": ["Het diner"]}
zus = kopieer_lid(anke)
zus["naam"] = "Zus van Anke"
zus["gelezen"].append("Turks fruit")

print(anke)
print(zus)
```

```text
{'naam': 'Anke', 'gelezen': ['Het diner']}
{'naam': 'Zus van Anke', 'gelezen': ['Het diner', 'Turks fruit']}
```

Waarom niet gewoon `lid.copy()`? Omdat dat de ondiepe kopie uit 14.6 is: de
buitenste dictionary is nieuw, de lijst erin niet. Vandaar de tweede regel.

En `copy.deepcopy(lid)` dan? Dat werkt ook, en het is hier zwaarder gereedschap
dan nodig. Weet welk veld je moet kopiëren; dat is duidelijker dan alles
klakkeloos verdubbelen.

**Wat je hieruit meeneemt.** Er waren drie manieren om dezelfde bug te maken:
een veranderlijke standaardwaarde, dezelfde lijst twee keer meegeven, en een
ondiepe kopie. Alle drie hebben dezelfde oorzaak: **een object kan meerdere
namen hebben.** Zodra je dat ziet, herken je het probleem overal.
