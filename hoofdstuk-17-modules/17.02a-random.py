# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# 17.2 De standaardbibliotheek — random

import random

random.seed(42)

print(random.randint(1, 6))
print(random.random())
print(random.choice(["Anke", "Bram", "Cato"]))
print(random.sample(range(1, 46), 6))

leden = ["Anke", "Bram", "Cato", "Dirk"]
random.shuffle(leden)
print(leden)


# Verwachte uitvoer:
# 6
# 0.11133106816568039
# Cato
# [18, 16, 15, 9, 7, 35]
# ['Dirk', 'Bram', 'Cato', 'Anke']
