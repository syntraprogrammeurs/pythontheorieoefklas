# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.5 Bereik: waar een naam bestaat
#
# Er bestaat een sleutelwoord om dat te omzeilen:

teller = 0


def hoog_op():
    global teller
    teller = teller + 1


hoog_op()
hoog_op()
print(teller)


# Verwachte uitvoer:
# 2
