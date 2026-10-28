# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.2 — De invariant die een fout blootlegt, uitwerking
#
# Concreet gaat het mis zodra alle getallen negatief zijn.

def hoogste_fout(getallen):
    """De versie met de foute beginwaarde."""
    grootste = 0
    for getal in getallen:
        if getal > grootste:
            grootste = getal
    return grootste


print("gewone lijst  :", hoogste_fout([320, 180, 250]))
print("negatieve lijst:", hoogste_fout([-5, -12, -3]))
print("lege lijst    :", hoogste_fout([]))


# Verwachte uitvoer:
# gewone lijst  : 320
# negatieve lijst: 0
# lege lijst    : 0
