# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.2 Tuples
#
# De haakjes zijn vaak optioneel. Het is de komma die de tuple maakt:

punt = 3, 4
print(punt, type(punt))

een_element = (5,)
geen_tuple = (5)
print(type(een_element), type(geen_tuple))


# Verwachte uitvoer:
# (3, 4) <class 'tuple'>
# <class 'tuple'> <class 'int'>
