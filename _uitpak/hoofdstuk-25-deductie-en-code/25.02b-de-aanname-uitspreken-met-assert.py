# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.2 De aanname uitspreken met assert
#
# En nu faalt het foute geval met een melding die zegt wat er mis is:
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

def gemiddelde(getallen):
    """Het gemiddelde. Preconditie: minstens één getal."""
    assert len(getallen) > 0, "gemiddelde() verwacht minstens één getal"
    return sum(getallen) / len(getallen)


print(gemiddelde([]))


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "<stdin>", line 7, in <module>
#     print(gemiddelde([]))
#   File "<stdin>", line 3, in gemiddelde
#     assert len(getallen) > 0, "gemiddelde() verwacht minstens één getal"
#            ^^^^^^^^^^^^^^^^^
# AssertionError: gemiddelde() verwacht minstens één getal
