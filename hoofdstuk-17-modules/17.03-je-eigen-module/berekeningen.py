# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# 17.3 Je eigen module

"""Berekeningen voor boekenclub De Leeslamp."""

LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12
JAREN_VOOR_KORTING = 3
KORTING = 5


def bereken_lidgeld(leeftijd: int, is_student: bool, jaren_lid: int) -> int:
    """Het lidgeld in hele euro's."""
    if leeftijd < LEEFTIJD_GRATIS:
        bedrag = 0
    elif is_student:
        bedrag = LIDGELD_STUDENT
    else:
        bedrag = LIDGELD_VOLWASSENE

    if jaren_lid >= JAREN_VOOR_KORTING:
        bedrag -= KORTING
    return max(bedrag, 0)
