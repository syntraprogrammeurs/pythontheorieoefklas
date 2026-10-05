# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.4 Het tweede deel: kopie versus verwijzing
#
# En daarom is dit iets anders:

getal = 5
ander = getal
ander += 1

print(getal, ander)


# Verwachte uitvoer:
# 5 6
