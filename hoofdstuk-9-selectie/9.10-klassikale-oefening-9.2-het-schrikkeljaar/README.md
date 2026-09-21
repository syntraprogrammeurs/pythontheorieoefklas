<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 9.2 — Het schrikkeljaar

Uit *Python basis — theoriebundel*, hoofdstuk 9 (Selectie: `if`, `elif`, `else` en `match`), paragraaf 9.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a-2-genest-zoals-de-regel.py` | uitwerking |  |
| `uitwerking-b-3-in-een-regel.py` | uitwerking |  |
| `uitwerking-c-4-het-bewijs.py` | uitwerking |  |
| `uitwerking-d-5-welke-in-een-project.py` | uitwerking |  |

## Opgave

**De situatie.** Dit is het klassieke voorbeeld van geneste voorwaarden, en het
staat in elke cursus omdat de regel bedrieglijk eenvoudig lijkt.

De regel: **een jaar is een schrikkeljaar als het deelbaar is door 4, behalve
wanneer het deelbaar is door 100, tenzij het ook deelbaar is door 400.**

**Wat je doet.**

1. Voorspel eerst met de hand voor 1900, 2000, 2024 en 2025.
2. Schrijf het programma met geneste `if`-statements, zoals de regel is
   opgeschreven.
3. Schrijf het daarna in één regel met `and` en `or`.
4. Bewijs dat de twee hetzelfde doen, voor alle jaren van 1600 tot en met 2400.
5. Zeg welke van de twee je in een project zou zetten.

## Uitwerking

**1 — De voorspelling.**

| Jaar | Deelbaar door 4 | Door 100 | Door 400 | Schrikkeljaar |
|---|---|---|---|---|
| 1900 | ja | ja | nee | **nee** |
| 2000 | ja | ja | ja | **ja** |
| 2024 | ja | nee | nee | **ja** |
| 2025 | nee | nee | nee | **nee** |

1900 is de rij die iedereen fout heeft. Het is deelbaar door 4 en toch geen
schrikkeljaar.

**2 — Genest, zoals de regel is opgeschreven.**

```python
for jaar in (1900, 2000, 2024, 2025):
    if jaar % 4 == 0:
        if jaar % 100 == 0:
            if jaar % 400 == 0:
                schrikkeljaar = True
            else:
                schrikkeljaar = False
        else:
            schrikkeljaar = True
    else:
        schrikkeljaar = False

    print(f"{jaar}: {schrikkeljaar}")
```

```text
1900: False
2000: True
2024: True
2025: False
```

Lees de nesting van binnen naar buiten en je herkent de zin uit de opgave
letterlijk. Dat is de sterkte van deze versie: ze is één op één te vergelijken
met het reglement.

**3 — In één regel.**

```python
for jaar in (1900, 2000, 2024, 2025):
    schrikkeljaar = jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0)
    print(f"{jaar}: {schrikkeljaar}")
```

```text
1900: False
2000: True
2024: True
2025: False
```

Let op de haakjes. Zonder die haakjes zou `and` sterker binden dan `or` en werd
de betekenis: "(deelbaar door 4 en niet door 100) of deelbaar door 400". Dat
geeft toevallig hetzelfde antwoord, maar niet omdat het dezelfde regel is.
Reken erop dat je zulk geluk niet altijd hebt.

**4 — Het bewijs.**

```python
def genest(jaar):
    if jaar % 4 == 0:
        if jaar % 100 == 0:
            return jaar % 400 == 0
        return True
    return False


def kort(jaar):
    return jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0)


verschillen = 0
for jaar in range(1600, 2401):
    if genest(jaar) != kort(jaar):
        verschillen += 1
        print("VERSCHIL bij", jaar)

print(f"801 jaren getest, {verschillen} verschillen")
```

```text
801 jaren getest, 0 verschillen
```

**5 — Welke in een project?**

De korte versie, met één toevoeging: commentaar dat de regel uitschrijft.

```python
def is_schrikkeljaar(jaar):
    """Gregoriaanse regel: deelbaar door 4, behalve door 100, tenzij door 400."""
    return jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0)
```

Waarom niet de geneste versie? Omdat zeven regels en drie inspringniveaus veel
zijn voor één ja-of-neevraag, en omdat je in de geneste versie makkelijk een tak
vergeet. Waarom dan wel het commentaar? Omdat de korte versie klopt maar niet
uitlegt waaróm er drie voorwaarden staan.

**Wat je hier eigenlijk leerde.** De geneste vorm is de beste manier om een
regel te **begrijpen**; de korte vorm is de beste manier om hem te
**onderhouden**. Schrijf gerust eerst de geneste versie, controleer dat ze
klopt, en dicht ze dan samen. Het bewijs in stap 4 is wat die stap veilig maakt.
