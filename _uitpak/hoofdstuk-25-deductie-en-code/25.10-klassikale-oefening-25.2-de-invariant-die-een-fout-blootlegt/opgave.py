# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.2 — De invariant die een fout blootlegt, opgave
#
# De situatie. Deze functie moet het hoogste aantal bladzijden vinden. Ze werkt op de
# voorbeelden waarop ze getest is.

def hoogste(getallen):
    """Het grootste getal uit de reeks. Bevat een fout."""
    grootste = 0
    for getal in getallen:
        if getal > grootste:
            grootste = getal
    return grootste
