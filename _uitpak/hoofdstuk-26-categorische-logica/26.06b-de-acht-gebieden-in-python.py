# Python basis — theoriebundel
# Hoofdstuk 26 — Categorische logica en venndiagrammen
# 26.6 De acht gebieden in Python
#
# Nu is de geldigheidstoets exact dezelfde als in hoofdstuk 23: geldig betekent dat er
# geen enkele wereld bestaat waarin de premissen kloppen en de conclusie niet.

from itertools import product

TERMEN = ("S", "P", "M")
GEBIEDEN = list(product([False, True], repeat=3))


def hoort_bij(gebied, term):
    return gebied[TERMEN.index(term)]


def alle(wereld, a, b):
    return not any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


def sommige(wereld, a, b):
    return any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


def werelden():
    for keuze in product([False, True], repeat=len(GEBIEDEN)):
        yield tuple(g for g, bewoond in zip(GEBIEDEN, keuze) if bewoond)


def beschrijf(gebied):
    """Een leesbare naam voor één gebied."""
    binnen = [t for t in TERMEN if hoort_bij(gebied, t)]
    return "+".join(binnen) if binnen else "buiten alles"


def toets(naam, premissen, conclusie):
    """Drukt af of het syllogisme geldig is, met tegenvoorbeeld."""
    for wereld in werelden():
        if all(p(wereld) for p in premissen) and not conclusie(wereld):
            bewoond = ", ".join(beschrijf(g) for g in wereld) or "leeg"
            print(f"{naam:<34}ONGELDIG — tegenwereld: {bewoond}")
            return
    print(f"{naam:<34}geldig")


# Barbara: alle M zijn P, alle S zijn M, dus alle S zijn P
toets("alle M-P, alle S-M => alle S-P",
      [lambda w: alle(w, "M", "P"), lambda w: alle(w, "S", "M")],
      lambda w: alle(w, "S", "P"))

# Dezelfde premissen, maar met een particuliere conclusie
toets("alle M-P, alle S-M => sommige S-P",
      [lambda w: alle(w, "M", "P"), lambda w: alle(w, "S", "M")],
      lambda w: sommige(w, "S", "P"))


# Verwachte uitvoer:
# alle M-P, alle S-M => alle S-P    geldig
# alle M-P, alle S-M => sommige S-P ONGELDIG — tegenwereld: leeg
