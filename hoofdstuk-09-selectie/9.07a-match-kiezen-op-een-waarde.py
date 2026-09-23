# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.7 match: kiezen op een waarde
#
# Sinds Python 3.10 bestaat er een tweede vorm van selectie.

soort = "nieuw"

match soort:
    case "gewoon":
        weken = 4
    case "nieuw":
        weken = 2
    case "naslagwerk":
        weken = 0
    case _:
        weken = 4

print(f"{weken} weken")


# Verwachte uitvoer:
# 2 weken
