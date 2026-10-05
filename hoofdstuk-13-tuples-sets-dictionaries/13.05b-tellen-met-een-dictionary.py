# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.5 Tellen met een dictionary
#
# Voor precies dit doel bestaat er een kant-en-klare oplossing:

from collections import Counter

titels = ["Het diner", "Turks fruit", "Het diner", "De aanslag", "Het diner"]
telling = Counter(titels)

print(telling.most_common(2))
print(telling.total())
print(len(telling))
print(len(titels))



# Verwachte uitvoer:
# [('Het diner', 3), ('Turks fruit', 1)]
