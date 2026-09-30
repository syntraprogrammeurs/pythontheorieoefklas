# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.7 Sorteren
#
# Sorteren op een deel van een samengestelde waarde:

boeken = [
    ("Het diner", 2009, 288),
    ("Turks fruit", 1969, 175),
    ("De aanslag", 1982, 246),
]

for titel, jaar, bladzijden in sorted(boeken, key=lambda b: b[1]):
    print(f"{jaar}  {titel:<14}{bladzijden:>4}")


# Verwachte uitvoer:
# 1969  Turks fruit    175
# 1982  De aanslag     246
# 2009  Het diner      288
