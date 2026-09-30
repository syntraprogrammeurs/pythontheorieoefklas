# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Klassikale oefening 12.2 — Wat verandert er, en wat niet?, opgave
#
# Wat je doet. Voorspel voor elk stukje de uitvoer, schrijf je voorspelling op, en
# voer dan pas uit.

# A
lijst = [1, 2, 3]
kopie = lijst
kopie.append(4)
print(lijst)

# B
getal = 5
ander = getal
ander += 1
print(getal)

# C
lijst = [1, 2, 3]
resultaat = lijst.append(4)
print(resultaat)

# D
lijst = [3, 1, 2]
nieuw = sorted(lijst)
lijst.sort()
print(nieuw == lijst)

# E
a = [1, 2]
b = [1, 2]
print(a == b, a is b)

# F
lijst = ["a", "b", "c"]
for x in lijst:
    if x == "b":
        lijst.remove(x)
print(lijst)
