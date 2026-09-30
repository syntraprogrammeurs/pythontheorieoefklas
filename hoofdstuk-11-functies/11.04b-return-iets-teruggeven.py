# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.4 return: iets teruggeven
#
# De eerste twee regels uitvoer zien er hetzelfde uit. Het verschil zit in de derde:
# met dubbel_print kún je niet verder rekenen. Die functie geeft None terug.

def dubbel_print(getal):
    print(getal * 2)


uitkomst = dubbel_print(5)
print(uitkomst)


# Verwachte uitvoer:
# 10
# None
