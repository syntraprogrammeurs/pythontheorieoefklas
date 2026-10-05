# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.5 Echt kopiëren
#
# Voor een dictionary en een set geldt hetzelfde:

lid = {"naam": "Anke", "leeftijd": 34}
kopie = lid.copy()
kopie["leeftijd"] = 35

print(lid)
print(kopie)


# Verwachte uitvoer:
# {'naam': 'Anke', 'leeftijd': 34}
# {'naam': 'Anke', 'leeftijd': 35}
