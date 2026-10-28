<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 25.1 — Vier fouten in één keten

Uit *Python basis — theoriebundel*, hoofdstuk 25 (Deductief redeneren en je code), paragraaf 25.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking-a-3-de-herschreven-functie.py` | uitwerking |  |
| `uitwerking-b-4-de-controles.py` | uitwerking |  |

## Opgave

**De situatie.** Dit staat in de code van De Leeslamp. Er zitten vier
logicafouten in, één van elke soort uit 25.6.

```python
def boetebedrag(dagen_te_laat, is_student, is_erelid):
    """De boete in euro's. Bevat vier logicafouten."""
    if is_erelid:
        return 0
    if dagen_te_laat <= 0:
        return 0
    if is_student:
        return dagen_te_laat * 0.25
    if dagen_te_laat < 7:
        return dagen_te_laat * 0.50
    if dagen_te_laat < 30:
        return 3.50 + (dagen_te_laat - 7) * 0.75
    if dagen_te_laat < 14:
        return 99.00
```

**Wat je doet.**

1. Wijs de vier fouten aan en benoem ze met de namen uit 25.6.
2. Schrijf de pre- en postcondities van deze functie op.
3. Herschrijf de functie, met bewaakclausules en een sluitende laatste tak.
4. Schrijf de controles die bewijzen dat je versie klopt, ook op de grenzen.

## Uitwerking

**1. De vier fouten.**

| Nr. | Soort | Waar | Wat er misgaat |
|---|---|---|---|
| 1 | Onbereikbare tak | `if dagen_te_laat < 14` | Kan alleen bereikt worden bij 30 of meer. Dode code |
| 2 | Ontbrekend geval | 30 dagen en meer | Geeft `None` terug in plaats van een bedrag |
| 3 | Overlappende takken | `is_student` vóór de dagen | Een student van 40 dagen te laat betaalt 10 euro, een gewoon lid 28,25 |
| 4 | Aanname die te veel omvat | `is_erelid` vooraan | Een erelid betaalt nooit, ook niet na een jaar. Is dat bedoeld? |

De vierde is de interessantste, want het is geen fout in de code maar een
**onuitgesproken beslissing**. Het bestuur moet zeggen of dat de bedoeling is.
Zolang dat niet uitgesproken is, staat er een regel in de code die niemand
genomen heeft.

**2. De contracten.**

| Deel | Wat er geldt |
|---|---|
| Preconditie | `dagen_te_laat` is een geheel getal, `is_student` en `is_erelid` zijn booleans |
| Postconditie | Het resultaat is een niet-negatief getal, en het groeit niet als het aantal dagen daalt |
| Volledigheid | Voor elke geldige invoer is er een bedrag |

Die tweede postconditie — "meer dagen kost nooit minder" — is precies de
eigenschap die fout 1 en 3 schonden, en ze is los te toetsen.

**3. De herschreven functie.**

```python
# De Leeslamp — boetebedrag, met uitgesproken aannames
# Cursus Python basis, hoofdstuk 25, oefening 1

DAGTARIEF_STUDENT = 0.25
DAGTARIEF_EERSTE_WEEK = 0.50
DAGTARIEF_DAARNA = 0.75
MAXIMUM = 50.00


def boetebedrag(dagen_te_laat, is_student=False, is_erelid=False):
    """De boete in euro's.

    Preconditie : dagen_te_laat is een geheel getal.
    Postconditie: het resultaat ligt tussen 0 en MAXIMUM,
                  en daalt nooit wanneer dagen_te_laat stijgt.
    """
    assert isinstance(dagen_te_laat, int), "dagen_te_laat hoort een int te zijn"

    # bewaakclausules: elke reden om niets te rekenen, apart
    if dagen_te_laat <= 0:
        return 0.00
    if is_erelid:
        return 0.00

    tarief = DAGTARIEF_STUDENT if is_student else DAGTARIEF_EERSTE_WEEK

    if dagen_te_laat <= 7:
        bedrag = dagen_te_laat * tarief
    else:
        bedrag = 7 * tarief + (dagen_te_laat - 7) * DAGTARIEF_DAARNA

    bedrag = min(bedrag, MAXIMUM)

    assert 0 <= bedrag <= MAXIMUM
    return round(bedrag, 2)


for dagen in (0, 1, 7, 8, 30, 365):
    print(f"{dagen:>4} dagen: gewoon {boetebedrag(dagen):>6.2f}   "
          f"student {boetebedrag(dagen, is_student=True):>6.2f}")
```

```text
   0 dagen: gewoon   0.00   student   0.00
   1 dagen: gewoon   0.50   student   0.25
   7 dagen: gewoon   3.50   student   1.75
   8 dagen: gewoon   4.25   student   2.50
  30 dagen: gewoon  20.75   student  19.00
 365 dagen: gewoon  50.00   student  50.00
```

**Wat er veranderde, en waarom.**

| Wijziging | Reden |
|---|---|
| `dagen_te_laat <= 0` staat eerst | Het goedkoopste geval eerst, en het is de enige tak die van niets anders afhangt |
| `is_student` bepaalt het **tarief**, niet de **tak** | Zo verdwijnt de overlap: student en dagen zijn twee losse dingen |
| Eén berekening met `if`-`else` in plaats van vijf takken | Volledig en elkaar uitsluitend, want `else` vangt alles op |
| Een maximum | Zonder plafond groeit de boete oneindig, en dat wilde niemand |
| De onbereikbare tak weg | Ze deed niets, en ze verborg de fout in de grenzen |
| Alle bedragen als constante bovenaan | De tarieven staan één keer, leesbaar, naast elkaar |

**4. De controles.**

```python
DAGTARIEF_STUDENT = 0.25
DAGTARIEF_EERSTE_WEEK = 0.50
DAGTARIEF_DAARNA = 0.75
MAXIMUM = 50.00


def boetebedrag(dagen_te_laat, is_student=False, is_erelid=False):
    """De boete in euro's, zie oefening 25.1."""
    assert isinstance(dagen_te_laat, int)
    if dagen_te_laat <= 0:
        return 0.00
    if is_erelid:
        return 0.00
    tarief = DAGTARIEF_STUDENT if is_student else DAGTARIEF_EERSTE_WEEK
    if dagen_te_laat <= 7:
        bedrag = dagen_te_laat * tarief
    else:
        bedrag = 7 * tarief + (dagen_te_laat - 7) * DAGTARIEF_DAARNA
    return round(min(bedrag, MAXIMUM), 2)


def controleer():
    """De controles die uit de contracten volgen."""
    # de grenzen
    assert boetebedrag(-1) == 0.00
    assert boetebedrag(0) == 0.00
    assert boetebedrag(1) == 0.50
    assert boetebedrag(7) == 3.50
    assert boetebedrag(8) == 4.25

    # het erelid
    assert boetebedrag(100, is_erelid=True) == 0.00

    # de student betaalt nooit meer dan een gewoon lid
    for dagen in range(0, 400):
        assert boetebedrag(dagen, is_student=True) <= boetebedrag(dagen)

    # postconditie: het bedrag daalt nooit als de dagen stijgen
    vorige = 0.00
    for dagen in range(0, 400):
        nu = boetebedrag(dagen)
        assert nu >= vorige, f"bij {dagen} dagen daalt het bedrag"
        assert 0 <= nu <= MAXIMUM
        vorige = nu

    print("Alle controles geslaagd, voor 400 waarden.")


controleer()
```

```text
Alle controles geslaagd, voor 400 waarden.
```

**Waarom die lus over 400 waarden meer waard is dan vijf losse controles.** De
losse controles toetsen de gevallen waar jij aan dacht. De lus toetst een
**eigenschap**: het bedrag mag nooit dalen. Zo'n eigenschap vangt ook de fout
die je niet voorzag.

Dat is het verschil tussen testen op voorbeelden en testen op contracten. En het
is nog altijd inductie, geen bewijs: 400 waarden zijn 400 waarnemingen. Maar ze
zijn wel systematisch gekozen in plaats van willekeurig bedacht.
