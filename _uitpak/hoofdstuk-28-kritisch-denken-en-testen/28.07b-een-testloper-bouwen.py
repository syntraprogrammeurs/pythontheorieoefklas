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

# Een minimale testloper
def loop_tests(tests):
    """Draait elke test en meldt alles wat faalt, niet alleen het eerste."""
    geslaagd, gefaald = 0, []
    for naam, test in tests:
        try:
            test()
            geslaagd += 1
        except AssertionError as fout:
            gefaald.append((naam, str(fout) or "geen boodschap"))
        except Exception as fout:
            gefaald.append((naam, f"{type(fout).__name__}: {fout}"))

    print(f"{geslaagd} geslaagd, {len(gefaald)} gefaald")
    for naam, reden in gefaald:
        print(f"  FOUT  {naam}: {reden}")
    return not gefaald


def deel(a, b):
    """Deelt a door b."""
    return a / b


TESTS = [
    ("gewone deling", lambda: deel(10, 2) == 5 or _fout("10/2 hoort 5 te zijn")),
    ("deling door nul", lambda: deel(1, 0)),
    ("negatieve deling", lambda: deel(-6, 3) == -2 or _fout("-6/3 hoort -2")),
]


def _fout(boodschap):
    """Hulpje: laat een lambda falen met een leesbare boodschap."""
    raise AssertionError(boodschap)


alles_goed = loop_tests(TESTS)
print("Pijplijn groen:", alles_goed)


# ---- dan het fragment ----

import sys
sys.exit(0 if alles_goed else 1)
