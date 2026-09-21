# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Klassikale oefening 9.2 — Het schrikkeljaar, uitwerking
#
# 4 — Het bewijs.

def genest(jaar):
    if jaar % 4 == 0:
        if jaar % 100 == 0:
            return jaar % 400 == 0
        return True
    return False


def kort(jaar):
    return jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0)


verschillen = 0
for jaar in range(1600, 2401):
    if genest(jaar) != kort(jaar):
        verschillen += 1
        print("VERSCHIL bij", jaar)

print(f"801 jaren getest, {verschillen} verschillen")


# Verwachte uitvoer:
# 801 jaren getest, 0 verschillen
