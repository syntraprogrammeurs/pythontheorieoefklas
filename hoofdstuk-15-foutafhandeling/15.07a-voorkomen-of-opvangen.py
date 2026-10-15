# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.7 Voorkomen of opvangen?
#
# Er zijn twee stijlen, en beide zijn juist.

lid = {"naam": "Anke"}

# 1 - eerst kijken
if "telefoon" in lid:
    print(lid["telefoon"])
else:
    print("geen telefoonnummer")

# 2 - proberen en opvangen
try:
    print(lid["telefoon"])
except KeyError:
    print("geen telefoonnummer")


# Verwachte uitvoer:
# geen telefoonnummer
# geen telefoonnummer
