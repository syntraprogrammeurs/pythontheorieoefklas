# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.2 De list comprehension — Wanneer je hem gebruikt, en wanneer niet
#
# Dit is technisch geldig en onleesbaar:

r = [[y * 2 for y in x if y > 1] for x in [[1, 2], [3, 4]] if len(x) > 1]
print(r)


# Verwachte uitvoer:
# [[4], [6, 8]]
