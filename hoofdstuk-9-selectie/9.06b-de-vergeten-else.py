# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.6 Waar de fouten zitten — De vergeten else
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

punten = 9

if punten >= 16:
    resultaat = "onderscheiding"
elif punten >= 10:
    resultaat = "geslaagd"

print(resultaat)


# Verwachte uitvoer:
# NameError: name 'resultaat' is not defined
