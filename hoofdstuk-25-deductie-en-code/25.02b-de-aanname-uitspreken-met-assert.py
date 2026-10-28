# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.2 De aanname uitspreken met assert
#
# En nu faalt het foute geval met een melding die zegt wat er mis is:
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

# Een kortere versie van de functie uit 25.02a: alleen de preconditie wordt hier
# gecontroleerd.
def gemiddelde(getallen):
    """Het gemiddelde. Preconditie: minstens één getal."""
    # De PRECONDITIE als assert: is de lijst leeg, dan stopt Python HIER met een
    # AssertionError en jouw melding, nog vóór de deling.
    assert len(getallen) > 0, "gemiddelde() verwacht minstens één getal"
    return sum(getallen) / len(getallen)


# LET OP: hier loopt het programma met opzet vast, net als in 25.01b.
# Het verschil zit in de foutmelding:
#   zonder assert (25.01b): ZeroDivisionError: division by zero
#                           -> wijst naar de deling, je zoekt in gemiddelde()
#   met assert (hier)     : AssertionError: gemiddelde() verwacht minstens één getal
#                           -> zegt welke afspraak geschonden werd, en dus dat je
#                              bij de AANROEPER moet kijken
# Dat heet FALEN BIJ DE BRON: hoe dichter de melding bij de oorzaak staat, hoe
# korter je moet zoeken.
#
# Ook hier verwijzen "<stdin>" en de regelnummers in het blok hieronder naar het
# fragment zoals de bundel het uitvoerde, niet naar dit bestand.
print(gemiddelde([]))


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "<stdin>", line 7, in <module>
#     print(gemiddelde([]))
#   File "<stdin>", line 3, in gemiddelde
#     assert len(getallen) > 0, "gemiddelde() verwacht minstens één getal"
#            ^^^^^^^^^^^^^^^^^
# AssertionError: gemiddelde() verwacht minstens één getal
