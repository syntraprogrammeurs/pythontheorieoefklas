# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# E — een try-blok dat te veel omvat.

lid = {"naam": "Anke"}
try:
    naam = lid["naam"]
    leeftijd = lid["leeftijd"]
    print(f"{naam} is {leeftijd}")
except KeyError:
    print("gegevens onvolledig")


# Verwachte uitvoer:
# gegevens onvolledig
