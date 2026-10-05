# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.4 Dictionaries — Een lijst van dictionaries
#
# Dit is de vorm waarin echte gegevens er bijna altijd uitzien.

leden = [
    {"naam": "Anke Peeters", "leeftijd": 34, "jaren": 3},
    {"naam": "Bram Coppens", "leeftijd": 20, "jaren": 1},
    {"naam": "Cato Dhondt", "leeftijd": 11, "jaren": 4},
]

for lid in leden:
    print(f"{lid['naam']:<16}{lid['leeftijd']:>4}{lid['jaren']:>4}")

print()
oudste = max(leden, key=lambda lid: lid["leeftijd"])
print("Oudste:", oudste["naam"])

print("Gemiddelde leeftijd:", sum(lid["leeftijd"] for lid in leden) / len(leden))


# Verwachte uitvoer:
# Anke Peeters      34   3
# Bram Coppens      20   1
# Cato Dhondt       11   4
#
# Oudste: Anke Peeters
# Gemiddelde leeftijd: 21.666666666666668
