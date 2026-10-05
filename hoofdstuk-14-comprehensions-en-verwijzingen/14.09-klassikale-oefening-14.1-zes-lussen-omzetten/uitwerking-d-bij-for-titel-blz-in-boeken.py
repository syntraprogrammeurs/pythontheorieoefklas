# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# Klassikale oefening 14.1 — Zes lussen omzetten, uitwerking
#
# Bij for titel, blz in boeken wordt blz in C en D niet gebruikt. Je linter merkt dat
# op. De afspraak in Python is om zo'n ongebruikte naam een liggend streepje te geven:

boeken = [("Het diner", 288), ("Turks fruit", 175), ("De aanslag", 246)]

c = {titel: len(titel) for titel, _ in boeken}
print(c)


# Verwachte uitvoer:
# {'Het diner': 9, 'Turks fruit': 11, 'De aanslag': 10}
