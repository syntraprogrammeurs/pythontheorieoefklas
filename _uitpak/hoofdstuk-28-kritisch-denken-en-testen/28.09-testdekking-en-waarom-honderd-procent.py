# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.9 Testdekking, en waarom honderd procent niets bewijst

def tarief(leeftijd):
    """Volledig gedekt door één test, en toch fout."""
    if leeftijd < 12:
        return 0
    return 15                       # klopt niet voor 26 en ouder


print("test met 5 jaar :", tarief(5) == 0)
print("test met 20 jaar:", tarief(20) == 15)
print("beide regels uitgevoerd, dekking 100 procent")
print("werkelijk bij 40:", tarief(40), "in plaats van 30")


# Verwachte uitvoer:
# test met 5 jaar : True
# test met 20 jaar: True
# beide regels uitgevoerd, dekking 100 procent
# werkelijk bij 40: 15 in plaats van 30
