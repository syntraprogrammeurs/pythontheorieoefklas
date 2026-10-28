# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.7 De tabel automatisch laten maken
#
# Acht rijen doe je met de hand. Zestien is vervelend, tweeëndertig is een bron van
# fouten. Dit is werk voor een computer.

# Een waarheidstabel automatisch opstellen
from itertools import product


def waarheidstabel(namen, formule, label):
    """Drukt de waarheidstabel van `formule` af over de variabelen `namen`."""
    kop = "".join(f"{naam:<8}" for naam in namen) + label
    print(kop)
    print("-" * len(kop))
    for waarden in product([True, False], repeat=len(namen)):
        cellen = "".join(f"{w!s:<8}" for w in waarden)
        print(cellen + str(formule(*waarden)))


waarheidstabel(["p", "q", "r"],
               lambda p, q, r: (not ((p and not q))) or r,
               "(p AND NIET q) -> r")


# Verwachte uitvoer:
# p       q       r       (p AND NIET q) -> r
# -------------------------------------------
# True    True    True    True
# True    True    False   True
# True    False   True    True
# True    False   False   False
# False   True    True    True
# False   True    False   True
# False   False   True    True
# False   False   False   True
