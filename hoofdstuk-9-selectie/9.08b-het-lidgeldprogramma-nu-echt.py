# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# 9.8 Het lidgeldprogramma, nu echt
#
# Controleer het tegen de testtabel uit hoofdstuk 3:

LIDGELD_VOLWASSENE = 30
LIDGELD_STUDENT = 15
LEEFTIJD_GRATIS = 12
JAREN_VOOR_KORTING = 3
KORTING = 5

gevallen = [
    (8, False, 0, 0),
    (11, False, 4, 0),
    (12, False, 0, 30),
    (20, True, 1, 15),
    (20, True, 3, 10),
    (45, False, 3, 25),
    (45, False, 2, 30),
]

for leeftijd, is_student, jaren_lid, verwacht in gevallen:
    if leeftijd < LEEFTIJD_GRATIS:
        bedrag = 0
    elif is_student:
        bedrag = LIDGELD_STUDENT
    else:
        bedrag = LIDGELD_VOLWASSENE

    if jaren_lid >= JAREN_VOOR_KORTING:
        bedrag -= KORTING
    if bedrag < 0:
        bedrag = 0

    teken = "ok" if bedrag == verwacht else "FOUT"
    print(f"{leeftijd:>3} {is_student!s:<6} {jaren_lid:>2}  "
          f"verwacht {verwacht:>2}  kreeg {bedrag:>2}  {teken}")


# Verwachte uitvoer:
#   8 False   0  verwacht  0  kreeg  0  ok
#  11 False   4  verwacht  0  kreeg  0  ok
#  12 False   0  verwacht 30  kreeg 30  ok
#  20 True    1  verwacht 15  kreeg 15  ok
#  20 True    3  verwacht 10  kreeg 10  ok
#  45 False   3  verwacht 25  kreeg 25  ok
#  45 False   2  verwacht 30  kreeg 30  ok
