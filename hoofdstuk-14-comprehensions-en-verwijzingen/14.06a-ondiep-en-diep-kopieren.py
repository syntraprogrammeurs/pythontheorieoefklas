# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.6 Ondiep en diep kopiëren
#
# Hier zit nog een laag onder.

leden = [
    {"naam": "Anke", "gelezen": ["Het diner"]},
    {"naam": "Bram", "gelezen": ["Turks fruit"]},
]

kopie = leden.copy()
kopie[0]["gelezen"].append("De aanslag")

print(leden[0])


# Verwachte uitvoer:
# {'naam': 'Anke', 'gelezen': ['Het diner', 'De aanslag']}
