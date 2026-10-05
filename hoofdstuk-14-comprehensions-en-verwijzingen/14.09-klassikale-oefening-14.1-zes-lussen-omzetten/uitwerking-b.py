# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.1 — Zes lussen omzetten, uitwerking
#
# Vier van de vijf zijn rechttoe rechtaan. E verdient uitleg: er zijn twee manieren om
# die te schrijven:

boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]

met_min = [min(blz, 250) for titel, blz in boeken]
met_keuze = [250 if blz > 250 else blz for titel, blz in boeken]

print(met_min)
print(met_keuze)
print(met_min == met_keuze)


# Verwachte uitvoer:
# [250, 175, 246]
# [250, 175, 246]
# True
