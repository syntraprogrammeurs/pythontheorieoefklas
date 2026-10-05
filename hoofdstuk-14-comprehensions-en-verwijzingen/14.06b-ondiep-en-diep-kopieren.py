# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.6 Ondiep en diep kopiëren

import copy

leden = [
    {"naam": "Anke", "gelezen": ["Het diner"]},
    {"naam": "Bram", "gelezen": ["Turks fruit"]},
]

diep = copy.deepcopy(leden)
diep[0]["gelezen"].append("De aanslag")

print(leden[0])
print(diep[0])


# Verwachte uitvoer:
# {'naam': 'Anke', 'gelezen': ['Het diner']}
# {'naam': 'Anke', 'gelezen': ['Het diner', 'De aanslag']}
