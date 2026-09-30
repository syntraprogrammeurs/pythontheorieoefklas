# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.4 return: iets teruggeven
#
# return stopt de functie meteen:

def beoordeel(punten):
    if punten >= 16:
        return "onderscheiding"
    if punten >= 10:
        return "geslaagd"
    return "niet geslaagd"


for punten in (17, 12, 8):
    print(punten, beoordeel(punten))


# Verwachte uitvoer:
# 17 onderscheiding
# 12 geslaagd
# 8 niet geslaagd
