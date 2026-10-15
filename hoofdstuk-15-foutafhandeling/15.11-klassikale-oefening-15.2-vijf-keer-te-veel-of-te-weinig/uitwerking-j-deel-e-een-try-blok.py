# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# Het antwoord klopt toevallig, maar het try-blok vangt twee opzoekingen én de print
# op. Ontbreekt straks de naam in plaats van de leeftijd, dan krijg je dezelfde
# boodschap en weet je niet welk veld ontbrak.

lid = {"naam": "Anke"}

naam = lid.get("naam", "onbekend")
leeftijd = lid.get("leeftijd")

if leeftijd is None:
    print(f"{naam}: leeftijd niet ingevuld")
else:
    print(f"{naam} is {leeftijd}")


# Verwachte uitvoer:
# Anke: leeftijd niet ingevuld
