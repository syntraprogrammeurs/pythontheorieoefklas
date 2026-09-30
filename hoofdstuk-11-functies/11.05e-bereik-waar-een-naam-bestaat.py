# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.5 Bereik: waar een naam bestaat
#
# De juiste vorm is bijna altijd deze:

def hoog_op(teller):
    return teller + 1


teller = 0
teller = hoog_op(teller)
teller = hoog_op(teller)
print(teller)


# Verwachte uitvoer:
# 2
