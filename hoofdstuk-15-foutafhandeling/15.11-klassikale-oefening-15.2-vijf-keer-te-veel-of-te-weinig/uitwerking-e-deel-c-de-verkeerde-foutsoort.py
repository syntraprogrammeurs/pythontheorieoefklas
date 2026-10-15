# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# C — de verkeerde foutsoort.
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

leden = ["Anke", "Bram"]
try:
    print(leden[5])
except ValueError:
    print("die staat er niet in")


# Verwachte uitvoer:
# Traceback (most recent call last):
#   File "<string>", line 3, in <module>
#     print(leden[5])
#           ~~~~~^^^
# IndexError: list index out of range
