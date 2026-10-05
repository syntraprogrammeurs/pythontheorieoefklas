# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.2 De list comprehension

namen = ["anke", "bram", "cato"]
netjes = [naam.capitalize() for naam in namen]

print(netjes)


# Verwachte uitvoer:
# ['Anke', 'Bram', 'Cato']
