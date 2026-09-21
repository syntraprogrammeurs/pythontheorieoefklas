# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.3 elif: meer dan twee gevallen — De volgorde is bepalend

punten = 17

if punten >= 10:
    resultaat = "geslaagd"
elif punten >= 16:
    resultaat = "onderscheiding"
else:
    resultaat = "niet geslaagd"

print(resultaat)


# Verwachte uitvoer:
# geslaagd
