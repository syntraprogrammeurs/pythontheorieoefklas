# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.2 — De invariant die een fout blootlegt, opgave
#
# De situatie. Deze functie moet het hoogste aantal bladzijden vinden. Ze werkt op de
# voorbeelden waarop ze getest is.

# LET OP: deze functie is met opzet FOUT. Op de meeste voorbeelden geeft ze het
# juiste antwoord, en daarom valt de fout niet op. Je vindt ze niet door te
# proberen, maar door te redeneren.
#
# Wat je doet:
#   1. Schrijf de preconditie, de postconditie en de invariant op.
#   2. Zoek met de invariant de invoer waarvoor de functie fout is.
#   3. Herstel de functie, en toon met een assert in de lus dat de invariant
#      nu staat.
#   4. Zeg wat er met het lege geval moet gebeuren, en waarom dat een beslissing
#      is en geen technische vraag.
#
# Herinnering (25.4): een invariant is een bewering die vóór de lus waar is, na
# elke ronde nog altijd waar is, en dus ook na de lus. Voor deze lus is dat:
# "grootste is het grootste van de getallen die ik al bekeken heb".
#
# Dit bestand print niets: niemand roept de functie aan. Probeer haar zelf,
# bijvoorbeeld met print(hoogste([320, 180, 250])), en bedenk dan een lijst
# waarvoor het antwoord NIET klopt.

def hoogste(getallen):
    """Het grootste getal uit de reeks. Bevat een fout."""
    # De beginwaarde. Geldt de invariant hier al, vóór de eerste ronde? Hoeveel
    # getallen zijn er op dit moment bekeken, en is 0 daar het grootste van?
    grootste = 0
    for getal in getallen:
        # Is het nieuwe getal groter dan het grootste tot nu toe? Dan wordt het
        # het nieuwe grootste. Deze stap zelf is in orde.
        if getal > grootste:
            grootste = getal
    return grootste
