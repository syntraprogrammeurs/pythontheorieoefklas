# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.5 Echt kopiëren

lijst = [1, 2, 3]

a = lijst.copy()
b = list(lijst)
c = lijst[:]

a.append(4)
b.append(5)
c.append(6)

print(lijst)
print(a, b, c)


# Verwachte uitvoer:
# [1, 2, 3]
# [1, 2, 3, 4] [1, 2, 3, 5] [1, 2, 3, 6]
