# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.5 Bereik: waar een naam bestaat
#
# Andersom mag een functie wél lezen wat erbuiten staat:

LIDGELD = 30


def toon():
    print(f"Het lidgeld is {LIDGELD} euro")


toon()


# Verwachte uitvoer:
# Het lidgeld is 30 euro
