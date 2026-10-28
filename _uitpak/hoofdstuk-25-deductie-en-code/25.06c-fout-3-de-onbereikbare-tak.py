# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 3 — de onbereikbare tak

def categorie_fout(bladzijden):
    """Fout: de derde tak kan nooit uitvoeren."""
    if bladzijden < 200:
        return "dun"
    if bladzijden < 500:
        return "gemiddeld"
    if bladzijden < 300:            # onbereikbaar
        return "nooit"
    return "dik"


for aantal in (150, 250, 400, 900):
    print(aantal, "->", categorie_fout(aantal))


# Verwachte uitvoer:
# 150 -> dun
# 250 -> gemiddeld
# 400 -> gemiddeld
# 900 -> dik
