# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# A — een kale except verbergt alles.

try:
    getal = int("abc")
    resultaat = 100 / getal
    print(resultaat)
except:
    print("er ging iets mis")


# Verwachte uitvoer:
# er ging iets mis
