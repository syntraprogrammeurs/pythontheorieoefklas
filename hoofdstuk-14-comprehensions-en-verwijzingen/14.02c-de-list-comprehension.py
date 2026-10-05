# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.2 De list comprehension
#
# Er bestaat ook een vorm met de if vooraan, en die betekent iets anders:

getallen = [1, -2, 3, -4]

print([x for x in getallen if x > 0])
print([x if x > 0 else 0 for x in getallen])


# Verwachte uitvoer:
# [1, 3]
# [1, 0, 3, 0]
