# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.2 Tuples
#
# Een tuple lezen gaat precies zoals een lijst. Aanpassen niet:
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

lid = ("Anke Peeters", 34, "Gent")
lid[1] = 35


# Verwachte uitvoer:
# TypeError: 'tuple' object does not support item assignment
