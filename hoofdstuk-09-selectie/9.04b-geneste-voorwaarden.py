# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.4 Geneste voorwaarden
#
# Dit werkt, maar het wordt snel onleesbaar. Meestal kun je het platslaan:

is_lid = True
heeft_boete = False

if not is_lid:
    print("Word eerst lid")
elif heeft_boete:
    print("Betaal eerst je boete")
else:
    print("Je mag lenen")


# Verwachte uitvoer:
# Je mag lenen
