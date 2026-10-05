# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.5 Tellen met een dictionary
#
# Dit patroon komt zo vaak voor dat het apart hoort.

titels = ["Het diner", "Turks fruit", "Het diner", "De aanslag", "Het diner"]

telling = {}
for titel in titels:
    telling[titel] = telling.get(titel, 0) + 1

for titel, aantal in sorted(telling.items(), key=lambda p: p[1], reverse=True):
    print(f"{titel:<14}{aantal}")


# Verwachte uitvoer:
# Het diner     3
# Turks fruit   1
# De aanslag    1
