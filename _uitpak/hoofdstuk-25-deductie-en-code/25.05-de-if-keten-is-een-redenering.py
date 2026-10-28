# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.5 De if-keten is een redenering

def tarief(leeftijd):
    """Het lidgeld per leeftijdsgroep. Volledig en elkaar uitsluitend."""
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd < 65:
        return 30
    return 20


for leeftijd in (8, 11, 12, 25, 26, 64, 65, 90):
    print(f"{leeftijd:>3} jaar: {tarief(leeftijd):>2} euro")


# Verwachte uitvoer:
#   8 jaar:  0 euro
#  11 jaar:  0 euro
#  12 jaar: 15 euro
#  25 jaar: 15 euro
#  26 jaar: 30 euro
#  64 jaar: 30 euro
#  65 jaar: 20 euro
#  90 jaar: 20 euro
