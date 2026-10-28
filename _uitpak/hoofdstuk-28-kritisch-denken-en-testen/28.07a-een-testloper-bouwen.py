# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.7 Een testloper bouwen
#
# Een reeks losse assert-regels heeft één nadeel: bij de eerste die faalt, stopt
# alles, en de rest zie je niet. Met tien regels code los je dat op.

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


# Verwachte uitvoer:
# 2 geslaagd, 1 gefaald
#   FOUT  deling door nul: ZeroDivisionError: division by zero
# Pijplijn groen: False
