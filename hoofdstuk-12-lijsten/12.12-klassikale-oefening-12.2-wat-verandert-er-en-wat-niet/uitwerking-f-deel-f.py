# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Klassikale oefening 12.2 — Wat verandert er, en wat niet?, uitwerking
#
# F.

lijst = ["a", "b", "c"]
for x in lijst:
    if x == "b":
        lijst.remove(x)
print(lijst)


# Verwachte uitvoer:
# ['a', 'c']
