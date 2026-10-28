# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 3 — de onbereikbare tak

# LET OP: deze functie is met opzet FOUT. Ze draait zonder foutmelding, maar één
# tak kan NOOIT uitvoeren: dat heet DODE CODE.
#
# Fout 3 uit 25.6: de ONBEREIKBARE TAK. Logisch is dat een CONTRADICTIE uit
# hoofdstuk 23: een voorwaarde die op die plek nooit waar kan zijn.
def categorie_fout(bladzijden):
    """Fout: de derde tak kan nooit uitvoeren."""
    if bladzijden < 200:
        return "dun"
    # Hier weet je al: bladzijden is minstens 200.
    if bladzijden < 500:
        return "gemiddeld"
    # Hier weet je al: bladzijden is minstens 500 (anders was de functie al met
    # return vertrokken). Om deze tak uit te voeren moet dus gelden:
    #     bladzijden >= 500  EN  bladzijden < 300
    # Dat kan nooit tegelijk waar zijn: een contradictie. De tak is dood.
    if bladzijden < 300:            # onbereikbaar
        return "nooit"
    return "dik"


# Vier tests. "nooit" verschijnt bij geen enkele invoer, en dat zal ook zo blijven,
# wat je ook probeert.
for aantal in (150, 250, 400, 900):
    print(aantal, "->", categorie_fout(aantal))

# Wat dode code meestal betekent: er staat een GRENS verkeerd. Wellicht wilde de
# schrijver een extra categorie tussen 200 en 300, en had de tak met 300 VOOR de
# tak met 500 moeten staan. Python waarschuwt je hier niet voor: je moet de keten
# zelf als redenering lezen, regel per regel, met wat je "al weet".


# Verwachte uitvoer:
# 150 -> dun
# 250 -> gemiddeld
# 400 -> gemiddeld
# 900 -> dik
