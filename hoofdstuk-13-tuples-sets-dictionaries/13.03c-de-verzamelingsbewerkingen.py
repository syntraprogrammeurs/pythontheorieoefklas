# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.3 Sets — De verzamelingsbewerkingen
#
# Hier komt een set echt tot zijn recht.

anke = {"Het diner", "Turks fruit", "De aanslag"}
bram = {"Turks fruit", "De ontdekking", "Het diner"}

print("Beiden gelezen  :", sorted(anke & bram))
print("Samen           :", sorted(anke | bram))
print("Alleen Anke     :", sorted(anke - bram))
print("Alleen één van 2:", sorted(anke ^ bram))


# Verwachte uitvoer:
# Beiden gelezen  : ['Het diner', 'Turks fruit']
# Samen           : ['De aanslag', 'De ontdekking', 'Het diner', 'Turks fruit']
# Alleen Anke     : ['De aanslag']
# Alleen één van 2: ['De aanslag', 'De ontdekking']
