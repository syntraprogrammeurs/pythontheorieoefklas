# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# Het programma crasht alsnog: een positie buiten de lijst geeft een IndexError, geen
# ValueError. De except staat er voor niets.

leden = ["Anke", "Bram"]
try:
    print(leden[5])
except IndexError:
    print("die staat er niet in")


# Verwachte uitvoer:
# die staat er niet in
