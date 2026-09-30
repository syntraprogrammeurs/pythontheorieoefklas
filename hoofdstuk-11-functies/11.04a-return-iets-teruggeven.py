# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.4 return: iets teruggeven
#
# Dit is het verschil tussen een functie die iets toont en een functie die iets
# teruggeeft.

def dubbel_print(getal):
    print(getal * 2)


def dubbel_return(getal):
    return getal * 2


dubbel_print(5)
print(dubbel_return(5))

resultaat = dubbel_return(5) + 1
print(resultaat)


# Verwachte uitvoer:
# 10
# 10
# 11
