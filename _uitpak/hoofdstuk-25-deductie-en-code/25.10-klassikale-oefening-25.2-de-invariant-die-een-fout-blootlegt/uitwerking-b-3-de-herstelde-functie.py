# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.2 — De invariant die een fout blootlegt, uitwerking
#
# 3. De herstelde functie.

def hoogste(getallen):
    """Het grootste getal uit de reeks.

    Preconditie : getallen bevat minstens één getal.
    Invariant   : `grootste` is het grootste van de reeds bekeken getallen.
    Postconditie: het resultaat zit in getallen, en niets erin is groter.
    """
    assert len(getallen) > 0, "hoogste() verwacht minstens één getal"

    grootste = getallen[0]                 # beginwaarde uit de reeks zelf
    for i, getal in enumerate(getallen[1:], start=2):
        if getal > grootste:
            grootste = getal
        assert grootste == max(getallen[:i]), "invariant geschonden"

    assert grootste in getallen
    assert all(getal <= grootste for getal in getallen)
    return grootste


print("gewone lijst   :", hoogste([320, 180, 250]))
print("negatieve lijst:", hoogste([-5, -12, -3]))
print("één element    :", hoogste([7]))


# Verwachte uitvoer:
# gewone lijst   : 320
# negatieve lijst: -3
# één element    : 7
