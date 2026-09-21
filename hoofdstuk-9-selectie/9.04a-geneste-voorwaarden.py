# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.4 Geneste voorwaarden
#
# Een if mag in een if staan.

is_lid = True
heeft_boete = False

if is_lid:
    if heeft_boete:
        print("Betaal eerst je boete")
    else:
        print("Je mag lenen")
else:
    print("Word eerst lid")


# Verwachte uitvoer:
# Je mag lenen
