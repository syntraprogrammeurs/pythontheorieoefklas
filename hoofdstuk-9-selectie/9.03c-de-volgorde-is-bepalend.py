# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.3 elif: meer dan twee gevallen — De volgorde is bepalend
#
# De juiste volgorde gaat van streng naar soepel:

punten = 17

if punten >= 16:
    resultaat = "onderscheiding"
elif punten >= 10:
    resultaat = "geslaagd"
else:
    resultaat = "niet geslaagd"

print(resultaat)


# Verwachte uitvoer:
# onderscheiding
