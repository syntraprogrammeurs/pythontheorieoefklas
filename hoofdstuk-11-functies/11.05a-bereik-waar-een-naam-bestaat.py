# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.5 Bereik: waar een naam bestaat
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

def bereken():
    binnen = 10
    print(binnen)


bereken()
print(binnen)


# Verwachte uitvoer:
# 10
# Traceback (most recent call last):
#   File "<string>", line 7, in <module>
#     print(binnen)
#           ^^^^^^
# NameError: name 'binnen' is not defined
