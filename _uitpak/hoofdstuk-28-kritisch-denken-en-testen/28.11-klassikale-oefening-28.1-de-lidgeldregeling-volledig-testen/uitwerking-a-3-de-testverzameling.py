# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# Klassikale oefening 28.1 — De lidgeldregeling volledig testen, uitwerking
#
# 3. De testverzameling.

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


# Verwachte uitvoer:
# De juiste versie
# 19 van de 19 geslaagd
