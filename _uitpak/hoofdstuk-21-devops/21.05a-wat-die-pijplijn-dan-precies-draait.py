# Python basis — theoriebundel
# Hoofdstuk 21 — DevOps, en waar Git daarin past
# 21.5 Wat die pijplijn dan precies draait
#
# De laatste stap van de pijplijn hierboven was python controle.py. Dat bestand
# schrijf je zelf. In deze cursus blijft het bij assert; hoofdstuk 28 gaat er dieper
# op in.

# controle.py — het bestand dat de pijplijn draait
# Cursus Python basis, hoofdstuk 21


def lidgeld(leeftijd, is_student=False):
    """Het jaarlijkse lidgeld van De Leeslamp, in hele euro's."""
    if leeftijd < 12:
        return 0
    if leeftijd >= 65:
        return 20
    return 15 if is_student else 30


def controleer():
    """Draait alle controles en stopt bij de eerste die faalt."""
    assert lidgeld(8) == 0, "wie jonger is dan 12 betaalt niets"
    assert lidgeld(11) == 0, "11 jaar valt nog onder de vrijstelling"
    assert lidgeld(12) == 30, "12 jaar is de grens: wel betalen"
    assert lidgeld(30) == 30, "een volwassene betaalt 30"
    assert lidgeld(30, is_student=True) == 15, "een student betaalt de helft"
    assert lidgeld(65) == 20, "vanaf 65 geldt het seniorentarief"
    print("Alle 6 controles geslaagd.")


controleer()


# Verwachte uitvoer:
# Alle 6 controles geslaagd.
