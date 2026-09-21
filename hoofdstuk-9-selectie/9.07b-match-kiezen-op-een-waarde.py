# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.7 match: kiezen op een waarde
#
# Je mag meerdere waarden in één case zetten:

dag = "zaterdag"

match dag:
    case "zaterdag" | "zondag":
        print("Gesloten")
    case "maandag":
        print("Alleen op afspraak")
    case _:
        print("Gewoon open")


# Verwachte uitvoer:
# Gesloten
