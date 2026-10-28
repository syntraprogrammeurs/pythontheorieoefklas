# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# Klassikale oefening 28.1 — De lidgeldregeling volledig testen, uitwerking
#
# 3. De testverzameling.

# De Leeslamp — de lidgeldregeling volledig getest
# Cursus Python basis, hoofdstuk 28, oefening 1


# De functie die je test. De docstring bevat het CONTRACT uit hoofdstuk 25:
#   PRECONDITIE  -> wat de aanroeper moet garanderen
#   POSTCONDITIE -> wat de functie dan belooft terug te geven
def lidgeld(leeftijd):
    """Het lidgeld in hele euro's.

    Preconditie : leeftijd is een int van 0 tot en met 120.
    Postconditie: het resultaat is 0, 15, 20 of 30.
    """
    # Nieuw tegenover 28.6: bool wordt apart geweigerd.
    # LET OP: True en False zijn in Python ook int's (True gedraagt zich als 1).
    # Zonder "isinstance(leeftijd, bool) or" zou lidgeld(True) gewoon 0 geven.
    # De bool-test moet EERST staan: anders laat isinstance(True, int) hem door.
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


# De testgevallen staan als GEGEVENS in een lijst, niet als losse asserts.
# Zo kan één lus ze allemaal draaien, en voeg je een geval toe met één regel.
# Elk tuple is (leeftijd, verwacht lidgeld).
# Per klasse zie je drie waarden: de onderste grens, een waarde in het midden
# (EQUIVALENTIEKLASSE, 28.3) en de bovenste grens (GRENSWAARDE, 28.4).
#   0, 5, 11      -> gratis:      0 en 11 zijn de randen, 5 het midden
#   12, 18, 25    -> jeugd:       12 en 25 zijn de randen
#   26, 40, 64    -> volwassen:   26 en 64 zijn de randen
#   65, 90, 120   -> senior:      120 is de hoogste geldige leeftijd
# De paren 11/12, 25/26 en 64/65 liggen telkens aan weerszijden van een grens:
# een verwisselde < en <= valt daar meteen op.
# de verwachte uitkomst per leeftijd, afgeleid uit de klassen en de grenzen
GELDIG = [
    (0, 0), (5, 0), (11, 0),
    (12, 15), (18, 15), (25, 15),
    (26, 30), (40, 30), (64, 30),
    (65, 20), (90, 20), (120, 20),
]

# De ONGELDIGE klassen: hier verwacht je een fout, geen bedrag (negatief testen,
# 28.8). Elk tuple is (invoer, verwachte foutsoort).
#   -1, 121   -> grenswaarden net buiten het geldige bereik
#   1000      -> ver erbuiten, midden in de klasse "onmogelijk hoog"
#   "veertig" -> tekst
#   None      -> helemaal geen waarde
#   12.5      -> een getal, maar geen geheel getal (de "komma" uit de tabel)
#   True      -> de bool-valkuil van hierboven
ONGELDIG = [
    (-1, ValueError), (121, ValueError), (1000, ValueError),
    ("veertig", TypeError), (None, TypeError), (12.5, TypeError),
    (True, TypeError),
]


# De TESTLOPER (28.7). Hij krijgt de te testen functie mee als parameter.
# Daardoor kun je dezelfde tests op een andere versie draaien, zoals in
# onderdeel 4 van de oefening.
def draai_alles(functie):
    """Draait alle gevallen en meldt elk verschil."""
    # Hierin komt een tekstregel per mislukt geval.
    gefaald = []

    # Deel 1: POSITIEVE tests. De functie moet het juiste bedrag geven.
    for leeftijd, verwacht in GELDIG:
        try:
            werkelijk = functie(leeftijd)
        # Een fout bij geldige invoer is altijd fout: noteer ze.
        # continue springt meteen naar het volgende geval in de lus.
        except Exception as fout:
            # {leeftijd:>4}: rechts uitlijnen over 4 tekens (hoofdstuk 6).
            gefaald.append(f"{leeftijd:>4}: onverwachte {type(fout).__name__}")
            continue
        # Geen fout, maar wel het verkeerde bedrag? Ook noteren.
        if werkelijk != verwacht:
            gefaald.append(f"{leeftijd:>4}: {werkelijk} in plaats van {verwacht}")

    # Deel 2: NEGATIEVE tests. De functie moet de juiste fout opgooien.
    # Hetzelfde patroon als verwacht_fout uit 28.8, maar met drie uitkomsten.
    for waarde, soort in ONGELDIG:
        try:
            functie(waarde)
        # Uitkomst 1: de verwachte fout. Goed zo, door naar het volgende geval.
        except soort:
            continue
        # Uitkomst 2: een andere foutsoort dan verwacht.
        # {waarde!r} toont de waarde met repr(): tekst krijgt aanhalingstekens,
        # zodat je "veertig" en veertig uit elkaar houdt.
        # soort.__name__ is de naam van de foutklasse, bv. "TypeError".
        except Exception as fout:
            gefaald.append(f"{waarde!r}: {type(fout).__name__} "
                           f"in plaats van {soort.__name__}")
            continue
        # Uitkomst 3: helemaal geen fout. Dan aanvaardde de functie ongeldige
        # invoer, en dat is de ernstigste mislukking.
        gefaald.append(f"{waarde!r}: geen fout, wel {soort.__name__} verwacht")

    # Het verslag: 12 geldige + 7 ongeldige gevallen = 19 in totaal.
    totaal = len(GELDIG) + len(ONGELDIG)
    print(f"{totaal - len(gefaald)} van de {totaal} geslaagd")
    for regel in gefaald:
        print(f"  FOUT {regel}")
    # True als er niets mislukte (lege lijst), zoals bij loop_tests in 28.7.
    return not gefaald


# lidgeld zonder haakjes: je geeft de functie zelf door aan de testloper.
# De terugkeerwaarde van draai_alles wordt hier niet gebruikt; het verslag
# verschijnt via print.
print("De juiste versie")
draai_alles(lidgeld)


# Verwachte uitvoer:
# De juiste versie
# 19 van de 19 geslaagd
