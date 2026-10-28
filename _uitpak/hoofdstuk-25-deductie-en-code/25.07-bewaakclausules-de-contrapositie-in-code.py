# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.7 Bewaakclausules: de contrapositie in code
#
# De contrapositie uit hoofdstuk 23 en 24 heeft een directe vertaling naar leesbare
# code. In plaats van "als alles goed is, doe het werk" schrijf je "als er iets mis
# is, stop meteen".

# De ingesprongen versie: het werk zit vier niveaus diep
def leen_uit_diep(lid, boek):
    """Alles wat goed moet gaan, in elkaar geschoven."""
    if lid is not None:
        if lid["betaald"]:
            if not lid["geschorst"]:
                if boek["beschikbaar"]:
                    return f"{boek['titel']} uitgeleend aan {lid['naam']}"
                return "boek niet beschikbaar"
            return "lid is geschorst"
        return "lidgeld niet betaald"
    return "onbekend lid"


# Dezelfde regels als bewaakclausules
def leen_uit(lid, boek):
    """Elke reden om te weigeren staat vooraan, één per regel."""
    if lid is None:
        return "onbekend lid"
    if not lid["betaald"]:
        return "lidgeld niet betaald"
    if lid["geschorst"]:
        return "lid is geschorst"
    if not boek["beschikbaar"]:
        return "boek niet beschikbaar"
    return f"{boek['titel']} uitgeleend aan {lid['naam']}"


ANKE = {"naam": "Anke", "betaald": True, "geschorst": False}
BRAM = {"naam": "Bram", "betaald": False, "geschorst": False}
BOEK = {"titel": "Max Havelaar", "beschikbaar": True}

print(leen_uit_diep(ANKE, BOEK))
print(leen_uit(ANKE, BOEK))
print(leen_uit(BRAM, BOEK))
print(leen_uit(None, BOEK))


# Verwachte uitvoer:
# Max Havelaar uitgeleend aan Anke
# Max Havelaar uitgeleend aan Anke
# lidgeld niet betaald
# onbekend lid
