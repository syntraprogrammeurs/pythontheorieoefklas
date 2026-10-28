# Python basis — theoriebundel
# Hoofdstuk 20 — Trends in programmeren
# 20.3 De programmeerparadigma's
#
# Python is bewust multiparadigma: je kunt alle vier de stijlen gebruiken, en je mengt
# ze in de praktijk.

namen = ["anke", "bram", "cato"]

# procedureel
uit = []
for naam in namen:
    uit.append(naam.capitalize())
print(uit)

# functioneel
print(list(map(str.capitalize, namen)))

# de Python-manier, die ertussenin zit
print([naam.capitalize() for naam in namen])


# Verwachte uitvoer:
# ['Anke', 'Bram', 'Cato']
# ['Anke', 'Bram', 'Cato']
# ['Anke', 'Bram', 'Cato']
