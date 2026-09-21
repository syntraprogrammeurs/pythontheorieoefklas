# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.6 Waar de fouten zitten — = in plaats van ==
#
# Let op: deze code bevat met opzet een fout tegen de schrijfregels. Python start ze
# niet eens.

leeftijd = 18
if leeftijd = 18:
    print("achttien")


# Verwachte uitvoer:
# SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='?
