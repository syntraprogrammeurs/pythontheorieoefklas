# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.5 enumerate en zip
#
# zip loopt door twee reeksen tegelijk:

leden = ["Anke", "Bram", "Cato"]
boeken = ["Het diner", "Turks fruit", "De aanslag"]

for lid, boek in zip(leden, boeken):
    print(f"{lid:<8} leest {boek}")


# Verwachte uitvoer:
# Anke     leest Het diner
# Bram     leest Turks fruit
# Cato     leest De aanslag
