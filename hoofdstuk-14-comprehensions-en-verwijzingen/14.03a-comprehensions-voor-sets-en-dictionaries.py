# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.3 Comprehensions voor sets en dictionaries

titels = ["Het diner", "Turks fruit", "Het diner", "De aanslag"]

lengtes = {titel: len(titel) for titel in titels}
beginletters = {titel[0] for titel in titels}

print(lengtes)
print(sorted(beginletters))


# Verwachte uitvoer:
# {'Het diner': 9, 'Turks fruit': 11, 'De aanslag': 10}
# ['D', 'H', 'T']
