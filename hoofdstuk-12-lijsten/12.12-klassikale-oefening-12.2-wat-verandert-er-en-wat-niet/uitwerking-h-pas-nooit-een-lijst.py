# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Klassikale oefening 12.2 — Wat verandert er, en wat niet?, uitwerking
#
# Pas nooit een lijst aan waarover je aan het lopen bent. Werk in de plaats daarvan op
# een kopie, of bouw een nieuwe lijst:

lijst = ["a", "b", "b", "c"]
lijst = [x for x in lijst if x != "b"]
print(lijst)


# Verwachte uitvoer:
# ['a', 'c']
