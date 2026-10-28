# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 2 — overlappende takken

def korting_fout(leeftijd, is_student):
    """Fout: een student van 20 valt op twee takken, en de volgorde beslist."""
    if is_student:
        return 50
    if leeftijd < 26:
        return 25
    return 0


print("student van 20:", korting_fout(20, True))
print("student van 30:", korting_fout(30, True))
print("niet-student 20:", korting_fout(20, False))


# Verwachte uitvoer:
# student van 20: 50
# student van 30: 50
# niet-student 20: 25
