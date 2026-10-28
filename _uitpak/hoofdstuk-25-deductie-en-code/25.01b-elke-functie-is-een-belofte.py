# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.1 Elke functie is een belofte
#
# De docstring zegt wat de functie doet. Wat ze niet zegt, is wat ze verwacht. En daar
# zit een aanname in die niemand uitsprak: de lijst mag niet leeg zijn.
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

def gemiddelde(getallen):
    """Het rekenkundig gemiddelde van een reeks getallen."""
    return sum(getallen) / len(getallen)


print(gemiddelde([]))


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "<stdin>", line 6, in <module>
#     print(gemiddelde([]))
#   File "<stdin>", line 3, in gemiddelde
#     return sum(getallen) / len(getallen)
#            ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
# ZeroDivisionError: division by zero
