<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 13.2 — Wie leest wat?

Uit *Python basis — theoriebundel*, hoofdstuk 13 (Tuples, sets en dictionaries), paragraaf 13.8.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** Drie leden houden bij welke boeken ze gelezen hebben. De club
wil weten waar de overlap zit, zodat ze een boek kan kiezen voor de
groepsbespreking.

```python
gelezen = {
    "Anke": {"Het diner", "Turks fruit", "De aanslag", "Max Havelaar"},
    "Bram": {"De aanslag", "De ontdekking"},
    "Cato": {"De aanslag", "Max Havelaar", "De ontdekking", "Het diner"},
}
```

**Wat je doet.** Beantwoord met setbewerkingen:

1. Welke boeken heeft iedereen gelezen?
2. Welke boeken heeft niemand gelezen, uit de volledige catalogus van zes
   titels? De zesde is `"Nooit meer slapen"`.
3. Welke boeken heeft precies één van de drie gelezen?
4. Wat heeft Anke gelezen dat Bram niet las?
5. Hoeveel verschillende boeken zijn er samen gelezen?
6. Welk boek zou je kiezen voor de bespreking, en waarom?

## Uitwerking

```python
# De Leeslamp — wie leest wat
# Cursus Python basis, hoofdstuk 13, oefening 2

CATALOGUS = {
    "Het diner", "Turks fruit", "De aanslag", "Max Havelaar",
    "De ontdekking", "Nooit meer slapen",
}

gelezen = {
    "Anke": {"Het diner", "Turks fruit", "De aanslag", "Max Havelaar"},
    "Bram": {"De aanslag", "De ontdekking"},
    "Cato": {"De aanslag", "Max Havelaar", "De ontdekking", "Het diner"},
}

anke = gelezen["Anke"]
bram = gelezen["Bram"]
cato = gelezen["Cato"]

# 1 — door iedereen gelezen
door_iedereen = anke & bram & cato

# 2 — door niemand gelezen
door_iemand = anke | bram | cato
door_niemand = CATALOGUS - door_iemand

# 3 — door precies één gelezen
telling = {}
for titels in gelezen.values():
    for titel in titels:
        telling[titel] = telling.get(titel, 0) + 1
door_een = {titel for titel, aantal in telling.items() if aantal == 1}

# 4 — Anke wel, Bram niet
alleen_anke = anke - bram

print("Door iedereen gelezen :", sorted(door_iedereen))
print("Door niemand gelezen  :", sorted(door_niemand))
print("Door precies één      :", sorted(door_een))
print("Anke wel, Bram niet   :", sorted(alleen_anke))
print("Samen verschillend    :", len(door_iemand))

print()
print(f"{'Titel':<20}{'Gelezen door':>13}")
print("-" * 33)
for titel in sorted(CATALOGUS):
    print(f"{titel:<20}{telling.get(titel, 0):>13}")
```

```text
Door iedereen gelezen : ['De aanslag']
Door niemand gelezen  : ['Nooit meer slapen']
Door precies één      : ['Turks fruit']
Anke wel, Bram niet   : ['Het diner', 'Max Havelaar', 'Turks fruit']
Samen verschillend    : 5

Titel                Gelezen door
---------------------------------
De aanslag                      3
De ontdekking                   2
Het diner                       2
Max Havelaar                    2
Nooit meer slapen               0
Turks fruit                     1
```

**6 — Welk boek voor de bespreking?**

Dat hangt van je doel af, en dat is het punt van deze vraag. Er is geen enkel
juist antwoord; er is wel een verkeerde manier om te antwoorden, namelijk zonder
je doel te benoemen.

| Doel | Keuze | Waarom |
|---|---|---|
| Iedereen kan meepraten | **De aanslag** | Als enige door alle drie gelezen |
| Iedereen leest iets nieuws | **Nooit meer slapen** | Door niemand gelezen |
| Zo min mogelijk leeswerk | **De ontdekking**, **Het diner** of **Max Havelaar** | Twee van de drie hebben het al |

**De vier technieken.**

**`&` voor "iedereen", `|` voor "iemand".** De doorsnede van alle drie geeft wat
ze gemeen hebben; de vereniging geeft alles samen. Het verschil met de catalogus
geeft wat er overblijft.

**Waarom `Turks fruit` het enige is dat precies één keer gelezen werd.** Je kunt
dat niet met `^` alleen berekenen. Het symmetrisch verschil van drie sets geeft
niet "in precies één": `a ^ b ^ c` geeft wat in een **oneven** aantal sets zit,
dus ook wat in alle drie zit. Vandaar de telling met een dictionary.

Dat is een echte valkuil. Met twee sets werkt `^` zoals je verwacht; met drie
niet meer. Wanneer je iets telt, tel dan ook echt.

**De setcomprehension.** `{titel for titel, aantal in telling.items() if aantal == 1}`
maakt in één regel een set. Dezelfde vorm als de listcomprehension, met accolades
in plaats van vierkante haken. Hoofdstuk 14.

**`telling.get(titel, 0)` in de tabel.** `"Nooit meer slapen"` staat niet in de
telling, want niemand las het. Zonder de standaardwaarde nul zou de tabel
crashen op een `KeyError`.
