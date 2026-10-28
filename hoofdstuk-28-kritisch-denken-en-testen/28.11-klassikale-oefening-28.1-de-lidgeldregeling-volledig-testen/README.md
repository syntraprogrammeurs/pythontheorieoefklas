<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 28.1 — De lidgeldregeling volledig testen

Uit *Python basis — theoriebundel*, hoofdstuk 28 (Kritisch denken toegepast op softwaretesten), paragraaf 28.11.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a-3-de-testverzameling.py` | uitwerking |  |
| `uitwerking-b-4-dezelfde-tests-op-een-foute.py` | uitwerking |  |

## Opgave

**De situatie.** De regeling van De Leeslamp, letterlijk zoals het bestuur ze
opschreef:

> Wie jonger is dan 12, betaalt niets. Van 12 tot en met 25 betaal je 15 euro.
> Van 26 tot en met 64 betaal je 30 euro. Vanaf 65 betaal je 20 euro. Een
> leeftijd onder 0 of boven 120 is ongeldig, en iets anders dan een geheel getal
> ook.

**Wat je doet.**

1. Schrijf de equivalentieklassen op.
2. Schrijf de grenswaarden op, drie per grens.
3. Bouw de volledige testverzameling met een testloper.
4. Draai ze op een implementatie waarin één grens fout staat, en kijk welke tests
   dat betrappen.

## Uitwerking

**1 en 2. De klassen en de grenzen.**

| Klasse | Bereik | Verwacht | Grenswaarden |
|---|---|---|---|
| Ongeldig, te laag | onder 0 | `ValueError` | -1, 0 |
| Gratis | 0 tot 11 | 0 | 0, 11 |
| Jeugd | 12 tot 25 | 15 | 11, 12, 13, 24, 25 |
| Volwassen | 26 tot 64 | 30 | 25, 26, 27, 63, 64 |
| Senior | 65 tot 120 | 20 | 64, 65, 66, 120 |
| Ongeldig, te hoog | boven 120 | `ValueError` | 120, 121 |
| Ongeldig, geen getal | tekst, `None`, komma | `TypeError` | drie voorbeelden |

**3. De testverzameling.**

```python
# De Leeslamp — de lidgeldregeling volledig getest
# Cursus Python basis, hoofdstuk 28, oefening 1


def lidgeld(leeftijd):
    """Het lidgeld in hele euro's.

    Preconditie : leeftijd is een int van 0 tot en met 120.
    Postconditie: het resultaat is 0, 15, 20 of 30.
    """
    if isinstance(leeftijd, bool) or not isinstance(leeftijd, int):
        raise TypeError("leeftijd moet een geheel getal zijn")
    if not 0 <= leeftijd <= 120:
        raise ValueError(f"leeftijd {leeftijd} ligt buiten het bereik")
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd < 65:
        return 30
    return 20


# de verwachte uitkomst per leeftijd, afgeleid uit de klassen en de grenzen
GELDIG = [
    (0, 0), (5, 0), (11, 0),
    (12, 15), (18, 15), (25, 15),
    (26, 30), (40, 30), (64, 30),
    (65, 20), (90, 20), (120, 20),
]

ONGELDIG = [
    (-1, ValueError), (121, ValueError), (1000, ValueError),
    ("veertig", TypeError), (None, TypeError), (12.5, TypeError),
    (True, TypeError),
]


def draai_alles(functie):
    """Draait alle gevallen en meldt elk verschil."""
    gefaald = []

    for leeftijd, verwacht in GELDIG:
        try:
            werkelijk = functie(leeftijd)
        except Exception as fout:
            gefaald.append(f"{leeftijd:>4}: onverwachte {type(fout).__name__}")
            continue
        if werkelijk != verwacht:
            gefaald.append(f"{leeftijd:>4}: {werkelijk} in plaats van {verwacht}")

    for waarde, soort in ONGELDIG:
        try:
            functie(waarde)
        except soort:
            continue
        except Exception as fout:
            gefaald.append(f"{waarde!r}: {type(fout).__name__} "
                           f"in plaats van {soort.__name__}")
            continue
        gefaald.append(f"{waarde!r}: geen fout, wel {soort.__name__} verwacht")

    totaal = len(GELDIG) + len(ONGELDIG)
    print(f"{totaal - len(gefaald)} van de {totaal} geslaagd")
    for regel in gefaald:
        print(f"  FOUT {regel}")
    return not gefaald


print("De juiste versie")
draai_alles(lidgeld)
```

```text
De juiste versie
19 van de 19 geslaagd
```

> **Let op**
>
> Let op de eerste regel van `lidgeld`: `isinstance(leeftijd, bool)` staat er
> apart, vóór de controle op `int`.
>
> In Python is `bool` een ondersoort van `int`, en `isinstance(True, int)` is dus
> `True`. Zonder die extra controle zou `lidgeld(True)` gewoon 0 teruggeven, want
> `True` telt als 1.
>
> Dat is geen bedachte flauwiteit: het is precies het soort geval dat je vindt door
> de klasse "geen geheel getal" systematisch in te vullen in plaats van drie
> voorbeelden te verzinnen.

**4. Dezelfde tests op een foute versie.**

```python
GELDIG = [
    (0, 0), (5, 0), (11, 0),
    (12, 15), (18, 15), (25, 15),
    (26, 30), (40, 30), (64, 30),
    (65, 20), (90, 20), (120, 20),
]


def lidgeld_fout(leeftijd):
    """Eén fout: <= 65 in plaats van < 65."""
    if isinstance(leeftijd, bool) or not isinstance(leeftijd, int):
        raise TypeError("leeftijd moet een geheel getal zijn")
    if not 0 <= leeftijd <= 120:
        raise ValueError("buiten bereik")
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd <= 65:          # hier zit de fout
        return 30
    return 20


gefaald = [(leeftijd, lidgeld_fout(leeftijd), verwacht)
           for leeftijd, verwacht in GELDIG
           if lidgeld_fout(leeftijd) != verwacht]

print(f"{len(GELDIG) - len(gefaald)} van de {len(GELDIG)} geldige gevallen goed")
for leeftijd, werkelijk, verwacht in gefaald:
    print(f"  FOUT bij {leeftijd}: {werkelijk} in plaats van {verwacht}")

print()
print("Zonder grenswaarden zou je 40 en 90 testen:")
print(f"  40 -> {lidgeld_fout(40)}, 90 -> {lidgeld_fout(90)}  (allebei goed)")
```

```text
11 van de 12 geldige gevallen goed
  FOUT bij 65: 30 in plaats van 20

Zonder grenswaarden zou je 40 en 90 testen:
  40 -> 30, 90 -> 20  (allebei goed)
```

**Waarom dit de hele oefening rechtvaardigt.** Precies één test betrapt de fout,
en het is de grenswaarde 65. Een testverzameling met alleen "een volwassene" en
"een senior" — 40 en 90 — staat volledig groen terwijl er een fout in zit die
elk lid van 65 tien euro te veel laat betalen.

Dat is de tabel uit 28.1 in de praktijk: groen bewijst niets over de gevallen die
je niet koos.
