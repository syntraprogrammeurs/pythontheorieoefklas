# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.3 Sets

titels = ["Het diner", "Turks fruit", "Het diner", "De aanslag"]

uniek = set(titels)
print(len(titels), "titels,", len(uniek), "verschillende")
print(sorted(uniek))


# Verwachte uitvoer:
# 4 titels, 3 verschillende
# ['De aanslag', 'Het diner', 'Turks fruit']
