# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# 17.2 De standaardbibliotheek — statistics en collections

import statistics
from collections import Counter

bladzijden = [320, 180, 250, 410, 96, 512, 288, 175, 640, 205, 330, 148]

print(f"gemiddelde: {statistics.mean(bladzijden):.1f}")
print(f"mediaan   : {statistics.median(bladzijden)}")
print(f"spreiding : {statistics.stdev(bladzijden):.1f}")

titels = ["Het diner", "Turks fruit", "Het diner", "De aanslag", "Het diner"]
telling = Counter(titels)
print(telling.most_common(2))
print(telling["Het diner"])
print(telling["Bestaat niet"])


# Verwachte uitvoer:
# gemiddelde: 296.2
# mediaan   : 269.0
# spreiding : 159.6
# [('Het diner', 3), ('Turks fruit', 1)]
# 3
# 0
