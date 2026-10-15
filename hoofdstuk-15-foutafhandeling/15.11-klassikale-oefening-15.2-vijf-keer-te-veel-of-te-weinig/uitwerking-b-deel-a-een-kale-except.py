# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# Twee problemen. De kale except vangt ook fouten op die je niet verwachtte, en de
# boodschap vertelt niets. Bovendien kunnen er hier twee verschillende dingen misgaan,
# en je weet niet welk.

try:
    getal = int("abc")
except ValueError:
    print("dat is geen geldig getal")
else:
    try:
        print(100 / getal)
    except ZeroDivisionError:
        print("het getal was nul, delen kan niet")


# Verwachte uitvoer:
# dat is geen geldig getal
