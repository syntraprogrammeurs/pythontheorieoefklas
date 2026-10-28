# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.5 De if-keten is een redenering

# Een if-keten is een lijst regels die van boven naar onder beoordeeld worden.
# Twee eigenschappen bepalen of zo'n lijst deugt:
#   VOLLEDIG           -> er bestaat geen invoer waarvoor GEEN ENKELE tak past
#                         (anders valt iets stilzwijgend door de mazen)
#   ELKAAR UITSLUITEND -> geen enkele invoer past op TWEE takken
#                         (anders bepaalt de volgorde de uitkomst)
# Deze functie heeft beide eigenschappen. Vergelijk haar straks met de vier foute
# versies in 25.06a tot 25.06d.
def tarief(leeftijd):
    """Het lidgeld per leeftijdsgroep. Volledig en elkaar uitsluitend."""
    # Elke tak eindigt met return: wie in een tak valt, verlaat de functie meteen
    # en komt nooit in een volgende tak. Daarom heb je hier geen elif nodig.
    # Lees de keten als vier regels:
    #   jonger dan 12           -> 0 euro
    #   niet jonger dan 12, wel jonger dan 26 -> 15 euro
    #   ...
    # Elke volgende if weet al dat de vorige voorwaarden onwaar waren. Bij
    # "leeftijd < 26" weet je dus al dat leeftijd minstens 12 is.
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd < 65:
        return 30
    # De laatste return vangt ALLES op wat overblijft (65 en ouder). Dat maakt de
    # keten VOLLEDIG: er is geen leeftijd zonder tarief.
    return 20


# Getest op elke GRENS, telkens aan beide kanten: 11 en 12, 25 en 26, 64 en 65.
# Grensfouten (< in plaats van <=) zie je alleen op die plaatsen.
# 8 en 90 zijn gewone gevallen ver van een grens.
# {leeftijd:>3} en {...:>2} lijnen de getallen rechts uit (6.7).
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
