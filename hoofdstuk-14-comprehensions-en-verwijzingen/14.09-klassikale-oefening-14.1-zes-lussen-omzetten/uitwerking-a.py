# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.1 — Zes lussen omzetten, uitwerking

boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]
titels = ["het diner", "turks fruit"]

a = [t.upper() for t in titels]
b = [titel for titel, blz in boeken if blz > 200]
c = {titel: len(titel) for titel, blz in boeken}
d = {titel[0] for titel, blz in boeken}
e = [min(blz, 250) for titel, blz in boeken]

print("A", a)
print("B", b)
print("C", c)
print("D", sorted(d))
print("E", e)


# Verwachte uitvoer:
# A ['HET DINER', 'TURKS FRUIT']
# B ['Het diner', 'De aanslag']
# C {'Het diner': 9, 'Turks fruit': 11, 'De aanslag': 10}
# D ['D', 'H', 'T']
# E [250, 175, 246]
