# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.1 Elke functie is een belofte
#
# Kijk nog eens naar een functie uit hoofdstuk 11, maar dan als logische uitspraak.

def gemiddelde(getallen):
    """Het rekenkundig gemiddelde van een reeks getallen."""
    return sum(getallen) / len(getallen)


print(gemiddelde([320, 180, 250]))


# Verwachte uitvoer:
# 250.0
