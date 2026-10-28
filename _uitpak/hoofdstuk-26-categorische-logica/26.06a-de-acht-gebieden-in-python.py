# Python basis — theoriebundel
# Hoofdstuk 26 — Categorische logica en venndiagrammen
# 26.6 De acht gebieden in Python
#
# De diagrammethode laat zich programmeren, en het resultaat is de tegenhanger van de
# waarheidstabel uit hoofdstuk 23. In plaats van alle combinaties van waarheidswaarden
# ga je alle mogelijke werelden af: welke van de acht gebieden zijn bewoond en welke
# niet.

# Syllogismen toetsen door alle werelden af te gaan
from itertools import product

TERMEN = ("S", "P", "M")
GEBIEDEN = list(product([False, True], repeat=3))


def hoort_bij(gebied, term):
    """Zit dit gebied binnen de gegeven groep?"""
    return gebied[TERMEN.index(term)]


def alle(wereld, a, b):
    """Alle A zijn B: geen bewoond gebied ligt in A en buiten B."""
    return not any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


def geen(wereld, a, b):
    """Geen enkele A is B: geen bewoond gebied ligt in allebei."""
    return not any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


def sommige(wereld, a, b):
    """Sommige A zijn B: minstens één bewoond gebied ligt in allebei."""
    return any(hoort_bij(g, a) and hoort_bij(g, b) for g in wereld)


def sommige_niet(wereld, a, b):
    """Sommige A zijn geen B: minstens één bewoond gebied ligt in A, buiten B."""
    return any(hoort_bij(g, a) and not hoort_bij(g, b) for g in wereld)


def werelden():
    """Alle 256 manieren waarop de acht gebieden bewoond kunnen zijn."""
    for keuze in product([False, True], repeat=len(GEBIEDEN)):
        yield tuple(g for g, bewoond in zip(GEBIEDEN, keuze) if bewoond)


print("Aantal gebieden :", len(GEBIEDEN))
print("Aantal werelden :", len(list(werelden())))


# Verwachte uitvoer:
# Aantal gebieden : 8
# Aantal werelden : 256
