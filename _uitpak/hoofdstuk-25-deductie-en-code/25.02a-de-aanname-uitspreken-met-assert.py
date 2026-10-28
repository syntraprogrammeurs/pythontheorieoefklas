# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.2 De aanname uitspreken met assert
#
# Een aanname die in je hoofd zit, kan niemand nakijken. Een aanname die in je code
# staat, wel.

def gemiddelde(getallen):
    """Het rekenkundig gemiddelde van een reeks getallen.

    Preconditie : getallen bevat minstens één getal.
    Postconditie: min(getallen) <= resultaat <= max(getallen).
    """
    assert len(getallen) > 0, "gemiddelde() verwacht minstens één getal"

    uitkomst = sum(getallen) / len(getallen)

    assert min(getallen) <= uitkomst <= max(getallen)
    return uitkomst


print(gemiddelde([320, 180, 250]))
print(gemiddelde([7]))


# Verwachte uitvoer:
# 250.0
# 7.0
