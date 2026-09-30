# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.5 Bereik: waar een naam bestaat
#
# Maar schrijven naar iets van buiten gaat niet zomaar:
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

teller = 0


def hoog_op():
    teller = teller + 1


hoog_op()


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "<string>", line 8, in <module>
#     hoog_op()
#     ~~~~~~~^^
#   File "<string>", line 5, in hoog_op
#     teller = teller + 1
#              ^^^^^^
# UnboundLocalError: cannot access local variable 'teller' where it is not associated with a value
