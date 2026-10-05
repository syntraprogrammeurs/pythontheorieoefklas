# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.2 Tuples
#
# Een tuple is onveranderlijk, maar wat erin zit, hoeft dat niet te zijn:

raar = ([1, 2], "vast")
raar[0].append(3)
print(raar)


# Verwachte uitvoer:
# ([1, 2, 3], 'vast')
