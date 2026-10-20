# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.7 Gegevens met meer dan één veld: CSV
#
# Alles wat je uit een bestand leest, is tekst. lid["leeftijd"] is "34" en niet 34.
# Wil je ermee rekenen, dan moet je omzetten, met alle valkuilen uit hoofdstuk 6 en
# 15:
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

lid = {"leeftijd": "34"}
print(lid["leeftijd"] + 1)


# Verwachte uitvoer:
# TypeError: can only concatenate str (not "int") to str
