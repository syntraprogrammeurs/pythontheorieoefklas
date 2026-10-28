# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 4 — het ontbrekende geval

def tarief_fout(leeftijd):
    """Fout: er is geen tak voor 65 en ouder."""
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd < 65:
        return 30


print("30 jaar:", tarief_fout(30))
print("70 jaar:", tarief_fout(70))


# Verwachte uitvoer:
# 30 jaar: 30
# 70 jaar: None
