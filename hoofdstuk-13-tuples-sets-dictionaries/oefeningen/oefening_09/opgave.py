# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oefening 9 — De voorraad overlopen

# Gebruik deze dictionary (titel: aantal exemplaren in de kast):
#
# voorraad = {"Het diner": 3, "Turks fruit": 0, "De aanslag": 5, "Max Havelaar": 1}
#
# 1. Loop met items() door de dictionary en toon elk boek als
#    f"{titel:<14}{aantal:>3}".
# 2. Toon "Totaal in voorraad: <totaal>".
#    Gebruik hiervoor sum() op values().
# 3. Bouw met een for-lus een lijst uitverkocht met de titels
#    waarvan er 0 exemplaren zijn. Toon "Uitverkocht: <uitverkocht>".
#
# Verwachte uitvoer:
# Het diner       3
# Turks fruit     0
# De aanslag      5
# Max Havelaar    1
# Totaal in voorraad: 9
# Uitverkocht: ['Turks fruit']
