# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.5 De methodes die je constant gebruikt — Testen wat voor tekens erin zitten
#
# .isdigit() is een eenvoudige manier om invoer te controleren vóór je int() gebruikt:


tekst = "24a"
if tekst.isdigit():
    getal = int(tekst)
    print(getal * 2)


# Verwachte uitvoer:
# 48
