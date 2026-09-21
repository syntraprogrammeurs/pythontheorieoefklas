# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.6 Waar de fouten zitten — De grens verkeerd

for leeftijd in (11, 12, 13):
    if leeftijd < 12:
        print(f"{leeftijd}: gratis")
    else:
        print(f"{leeftijd}: betalend")


# Verwachte uitvoer:
# 11: gratis
# 12: betalend
# 13: betalend
