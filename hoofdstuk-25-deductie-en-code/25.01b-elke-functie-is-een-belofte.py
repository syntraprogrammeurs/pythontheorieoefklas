# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.1 Elke functie is een belofte
#
# De docstring zegt wat de functie doet. Wat ze niet zegt, is wat ze verwacht. En daar
# zit een aanname in die niemand uitsprak: de lijst mag niet leeg zijn.
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

# Dezelfde functie als in 25.01a. Er is niets aan veranderd.
def gemiddelde(getallen):
    """Het rekenkundig gemiddelde van een reeks getallen."""
    # Bij een lege lijst is sum([]) gelijk aan 0 en len([]) ook 0.
    # 0 / 0 kan niet: Python stopt met ZeroDivisionError (15.6).
    return sum(getallen) / len(getallen)


# LET OP: hier loopt het programma met opzet vast.
# De aanroeper houdt zich niet aan de onuitgesproken PRECONDITIE "minstens één
# getal". Het contract is dus geschonden, en dan belooft de functie niets meer.
# Logisch is dat de implicatie preconditie -> postconditie uit hoofdstuk 23: is
# het antecedens onwaar, dan is de implicatie waar, wat de functie ook doet.
#
# Lees de foutmelding van onder naar boven (4.6):
#   - onderaan staat WAT er misging: division by zero;
#   - daarboven WAAR: in gemiddelde, op de regel met de deling;
#   - nog hoger WIE dat veroorzaakte: de print-regel met de lege lijst.
# Het probleem: de melding wijst naar de DELING, terwijl de echte fout bij de
# AANROEPER zit, die een lege lijst meegaf. In een groot programma zoek je dan
# lang op de verkeerde plek. 25.02b lost dat op met assert.
#
# In het blok hieronder staat "<stdin>" en regel 6 en 3: zo zag de melding eruit
# toen de bundel dit fragment los uitvoerde. Start je dit bestand, dan zie je de
# echte bestandsnaam en andere regelnummers; de fout zelf is dezelfde.
print(gemiddelde([]))


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "<stdin>", line 6, in <module>
#     print(gemiddelde([]))
#   File "<stdin>", line 3, in gemiddelde
#     return sum(getallen) / len(getallen)
#            ~~~~~~~~~~~~~~^~~~~~~~~~~~~~~
# ZeroDivisionError: division by zero
