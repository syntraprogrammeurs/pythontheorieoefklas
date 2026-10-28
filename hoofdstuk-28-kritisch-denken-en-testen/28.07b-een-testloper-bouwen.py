# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.7 Een testloper bouwen
#
# Dit is de brug naar hoofdstuk 21. loop_tests geeft True of False terug, en daarmee
# kun je het programma laten eindigen met de juiste afsluitcode:
#
# Dit fragment bouwt verder op 28.07a-een-testloper-bouwen.py. Die code staat
# hieronder eerst, zodat dit bestand op zichzelf draait.

# ---- eerst de code uit 28.07a-een-testloper-bouwen.py ----

# Het eerste deel is letterlijk 28.07a; de uitgebreide uitleg per regel staat
# daar. Hier alleen de hoofdlijnen.
# Een minimale testloper
def loop_tests(tests):
    """Draait elke test en meldt alles wat faalt, niet alleen het eerste."""
    # Teller voor de geslaagde tests, lijst voor de mislukte.
    geslaagd, gefaald = 0, []
    for naam, test in tests:
        try:
            test()                  # de test uitvoeren
            geslaagd += 1           # geen fout: geslaagd
        # Een assert of _fout die niet klopte: een gewone mislukking.
        except AssertionError as fout:
            gefaald.append((naam, str(fout) or "geen boodschap"))
        # Elke andere fout: de test crashte. Ook dat is een mislukking.
        except Exception as fout:
            gefaald.append((naam, f"{type(fout).__name__}: {fout}"))

    print(f"{geslaagd} geslaagd, {len(gefaald)} gefaald")
    for naam, reden in gefaald:
        print(f"  FOUT  {naam}: {reden}")
    # True als de lijst gefaald leeg is, anders False.
    return not gefaald


def deel(a, b):
    """Deelt a door b."""
    return a / b


# Drie tests als lambda's; "deling door nul" crasht met opzet.
TESTS = [
    ("gewone deling", lambda: deel(10, 2) == 5 or _fout("10/2 hoort 5 te zijn")),
    ("deling door nul", lambda: deel(1, 0)),
    ("negatieve deling", lambda: deel(-6, 3) == -2 or _fout("-6/3 hoort -2")),
]


def _fout(boodschap):
    """Hulpje: laat een lambda falen met een leesbare boodschap."""
    raise AssertionError(boodschap)


# alles_goed wordt hier False, want één test faalt.
alles_goed = loop_tests(TESTS)
print("Pijplijn groen:", alles_goed)


# ---- dan het fragment ----

# sys is een ingebouwde module met functies over het lopende Python-programma.
# (Normaal zet je import bovenaan; hier staat ze onderaan omdat het fragment
# los uit de bundel komt.)
import sys
# sys.exit(getal) beëindigt het programma met een AFSLUITCODE.
#   0          -> alles in orde
#   iets anders (hier 1) -> er ging iets mis
# De pijplijn uit hoofdstuk 21 kijkt alleen naar dat ene getal: 0 is groen,
# alles anders is rood.
# "0 if alles_goed else 1" is een voorwaardelijke uitdrukking: 0 als alles_goed
# True is, anders 1.
# Hier eindigt het programma dus met code 1: één test faalde. Je ziet dat niet
# in de uitvoer, maar wel in de terminal of de pijplijn (rood kruisje).
sys.exit(0 if alles_goed else 1)
