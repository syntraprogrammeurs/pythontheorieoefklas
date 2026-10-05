# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oefening 8 — Een telefoonnummer opzoeken

# Gebruik deze dictionary:
#
# telefoons = {"Anke": "0470 12 34 56", "Bram": "0485 98 76 54"}
#
# 1. Loop door de lijst ["Anke", "Cato", "Bram"] en toon telkens:
#    "<naam>: <nummer>"
#    Staat de naam niet in telefoons, toon dan "onbekend" als nummer.
#    Gebruik hiervoor get() met een standaardwaarde.
#
# 2. Controleer met in of "Cato" in telefoons staat.
#    Is dat niet zo, voeg Cato dan toe met nummer "0499 11 22 33"
#    en toon "Cato toegevoegd".
#
# 3. Toon "Cato: <nummer>" door de sleutel rechtstreeks op te vragen.
#
# Wat gebeurt er als je telefoons["Cato"] opvraagt vóór stap 2?
#
# Verwachte uitvoer:
# Anke: 0470 12 34 56
# Cato: onbekend
# Bram: 0485 98 76 54
# Cato toegevoegd
# Cato: 0499 11 22 33
