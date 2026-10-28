# Python basis — theoriebundel
# Hoofdstuk 26 — Categorische logica en venndiagrammen
# Klassikale oefening 26.2 — Drie syllogismen toetsen, uitwerking
#
# 3. Het programma.

# De Leeslamp — drie syllogismen mechanisch getoetst
# Cursus Python basis, hoofdstuk 26, oefening 2
from itertools import product

TERMEN = ("S", "P", "M")
GEBIEDEN = list(product([False, True], repeat=3))


def hoort_bij(gebied, term):
    return gebied[TERMEN.index(term)]


def alle(wereld, a, b):
    return not any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


def geen(wereld, a, b):
    return not any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


def sommige(wereld, a, b):
    return any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


def werelden():
    for keuze in product([False, True], repeat=len(GEBIEDEN)):
        yield tuple(g for g, bewoond in zip(GEBIEDEN, keuze) if bewoond)


def beschrijf(gebied):
    binnen = [t for t in TERMEN if hoort_bij(gebied, t)]
    return "+".join(binnen) if binnen else "niets"


def toets(nummer, premissen, conclusie):
    """Zoekt een wereld waarin de premissen kloppen en de conclusie niet."""
    for wereld in werelden():
        if all(p(wereld) for p in premissen) and not conclusie(wereld):
            bewoond = ", ".join(beschrijf(g) for g in wereld) or "lege wereld"
            print(f"{nummer}  ONGELDIG")
            print(f"   tegenwereld: bewoond zijn {bewoond}")
            return
    print(f"{nummer}  geldig")


toets("1.",
      [lambda w: alle(w, "M", "P"), lambda w: geen(w, "S", "M")],
      lambda w: geen(w, "S", "P"))

toets("2.",
      [lambda w: alle(w, "P", "M"), lambda w: sommige(w, "S", "M")],
      lambda w: sommige(w, "S", "P"))

toets("3.",
      [lambda w: geen(w, "M", "P"), lambda w: alle(w, "S", "M")],
      lambda w: geen(w, "S", "P"))


# Verwachte uitvoer:
# 1.  ONGELDIG
#    tegenwereld: bewoond zijn S+P
# 2.  ONGELDIG
#    tegenwereld: bewoond zijn S+M
# 3.  geldig
