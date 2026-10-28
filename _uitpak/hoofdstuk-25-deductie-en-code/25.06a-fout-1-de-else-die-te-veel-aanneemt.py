# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 1 — de else die te veel aanneemt

def mag_lenen_fout(geschorst, betaald, boeken_thuis):
    """Fout: de else neemt aan dat schorsing de enige reden is."""
    if geschorst:
        return False
    return True


print("geschorst=False, betaald=False, 5 boeken thuis ->",
      mag_lenen_fout(False, False, 5))


# Verwachte uitvoer:
# geschorst=False, betaald=False, 5 boeken thuis -> True
