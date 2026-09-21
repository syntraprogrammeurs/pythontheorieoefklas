# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.6 De wetten van De Morgan
#
# Controleer het zelf voor alle vier de gevallen:

for leeftijd in (12, 30):
    for is_lid in (False, True):
        links = not (leeftijd >= 18 and is_lid)
        rechts = leeftijd < 18 or not is_lid
        print(f"{leeftijd:>3} {is_lid!s:<6} {links!s:<6} {rechts!s:<6} {links == rechts}")


# Verwachte uitvoer:
#  12 False  True   True   True
#  12 True   True   True   True
#  30 False  True   True   True
#  30 True   False  False  True
