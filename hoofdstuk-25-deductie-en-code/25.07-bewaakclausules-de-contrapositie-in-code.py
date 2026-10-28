# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.7 Bewaakclausules: de contrapositie in code
#
# De contrapositie uit hoofdstuk 23 en 24 heeft een directe vertaling naar leesbare
# code. In plaats van "als alles goed is, doe het werk" schrijf je "als er iets mis
# is, stop meteen".

# Twee functies die PRECIES hetzelfde doen, op twee manieren geschreven.
# Beide krijgen een lid en een boek mee als DICTIONARY (hoofdstuk 13), en geven een
# string terug: ofwel de uitlening, ofwel de reden van weigering.

# De ingesprongen versie: het werk zit vier niveaus diep
# Elke voorwaarde opent een nieuw niveau (geneste if, 9.4). Het eigenlijke werk,
# het uitlenen, zit helemaal binnenin. Elke weigering staat ONDER het blok waar ze
# bij hoort, en je moet de inspringing volgen om te zien welke else bij welke if
# hoort.
def leen_uit_diep(lid, boek):
    """Alles wat goed moet gaan, in elkaar geschoven."""
    # "is not None" vergelijkt de IDENTITEIT (7.10): bestaat dit lid wel?
    if lid is not None:
        # lid["betaald"] haalt de waarde bij de sleutel "betaald": True of False.
        if lid["betaald"]:
            if not lid["geschorst"]:
                if boek["beschikbaar"]:
                    # Alle vier de voorwaarden zijn waar: het gewone geval.
                    # Binnen de f-string staan enkele aanhalingstekens rond de
                    # sleutels, want de f-string zelf gebruikt dubbele.
                    return f"{boek['titel']} uitgeleend aan {lid['naam']}"
                # Deze return hoort bij "if boek['beschikbaar']" (niveau 4).
                return "boek niet beschikbaar"
            # Hoort bij "if not lid['geschorst']" (niveau 3).
            return "lid is geschorst"
        # Hoort bij "if lid['betaald']" (niveau 2).
        return "lidgeld niet betaald"
    # Hoort bij "if lid is not None" (niveau 1).
    return "onbekend lid"


# Dezelfde regels als bewaakclausules
# Een BEWAAKCLAUSULE (guard clause) is een if die vooraan in de functie controleert
# of er iets MIS is, en dan meteen vertrekt met return. Het gewone geval staat
# onderaan, op één niveau, zonder inspringing.
#
# Waarom dit de CONTRAPOSITIE is (24.3):
#   De regel:          als alles in orde is, dan lenen we uit.        (p -> q)
#   De contrapositie:  als we niet uitlenen, dan was iets niet in orde.
#                                                           (niet q -> niet p)
# Die twee zijn gelijkwaardig. Elke bewaakclausule hieronder is één concrete reden
# waarom "iets niet in orde" is, apart opgeschreven.
def leen_uit(lid, boek):
    """Elke reden om te weigeren staat vooraan, één per regel."""
    # LET OP: de volgorde doet er hier wel toe voor de EERSTE controle. Is lid
    # None, dan zou lid["betaald"] een TypeError geven. Daarom staat de controle
    # op None bovenaan: pas daarna weet je zeker dat lid een dictionary is.
    if lid is None:
        return "onbekend lid"
    if not lid["betaald"]:
        return "lidgeld niet betaald"
    if lid["geschorst"]:
        return "lid is geschorst"
    if not boek["beschikbaar"]:
        return "boek niet beschikbaar"
    # Hier weet je: geen enkele reden om te weigeren was waar. Het gewone geval.
    return f"{boek['titel']} uitgeleend aan {lid['naam']}"


# Testgegevens. In hoofdletters, als "constanten" (hoofdstuk 5).
ANKE = {"naam": "Anke", "betaald": True, "geschorst": False}
BRAM = {"naam": "Bram", "betaald": False, "geschorst": False}
BOEK = {"titel": "Max Havelaar", "beschikbaar": True}

# Eerst beide versies met hetzelfde lid: dezelfde uitkomst.
print(leen_uit_diep(ANKE, BOEK))
print(leen_uit(ANKE, BOEK))
# Bram heeft niet betaald: de tweede bewaakclausule vangt hem op.
print(leen_uit(BRAM, BOEK))
# Geen lid (None): de eerste bewaakclausule vangt dat op.
print(leen_uit(None, BOEK))

# Het verschil in onderhoud:
#   - een reden bijzetten: bij bewaakclausules één regel erbij, bij de diepe
#     versie een niveau erbij en alles schuift op;
#   - lezen: bij bewaakclausules lees je de redenen één voor één en vergeet je ze
#     weer; bij de diepe versie moet je alle voorwaarden tegelijk onthouden.
# En ze zijn eerlijker: ze dwingen je elke weigeringsreden te benoemen, in plaats
# van ze samen te laten vallen in één else (fout 1 uit 25.06a).


# Verwachte uitvoer:
# Max Havelaar uitgeleend aan Anke
# Max Havelaar uitgeleend aan Anke
# lidgeld niet betaald
# onbekend lid
