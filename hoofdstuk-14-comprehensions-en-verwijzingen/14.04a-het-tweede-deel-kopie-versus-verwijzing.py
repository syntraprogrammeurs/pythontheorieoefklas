# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.4 Het tweede deel: kopie versus verwijzing
#
# Dit is de verklaring van de raadsels uit oefening 12.2.

lijst = [1, 2, 3]
kopie = lijst
kopie.append(4)

print(lijst)
print(kopie)
print(lijst is kopie)


# Verwachte uitvoer:
# [1, 2, 3, 4]
# [1, 2, 3, 4]
# True
