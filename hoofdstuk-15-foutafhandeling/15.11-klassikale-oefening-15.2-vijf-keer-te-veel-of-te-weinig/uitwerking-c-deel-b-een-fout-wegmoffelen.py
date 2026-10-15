# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.2 — Vijf keer te veel of te weinig opgevangen, uitwerking
#
# B — een fout wegmoffelen als geldige waarde.

def lees_leeftijd(tekst):
    try:
        return int(tekst)
    except ValueError:
        return 0


print(lees_leeftijd("abc"))
print(lees_leeftijd("0"))


# Verwachte uitvoer:
# 0
# 0
