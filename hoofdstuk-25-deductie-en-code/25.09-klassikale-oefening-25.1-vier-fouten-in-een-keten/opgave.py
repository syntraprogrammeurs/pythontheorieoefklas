# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.1 — Vier fouten in één keten, opgave
#
# De situatie. Dit staat in de code van De Leeslamp. Er zitten vier logicafouten in,
# één van elke soort uit 25.6.

# LET OP: deze functie is met opzet FOUT. Herstel haar niet meteen: zoek eerst de
# vier fouten en geef elk een naam.
#
# Wat je doet:
#   1. Wijs de vier fouten aan en benoem ze met de namen uit 25.6.
#   2. Schrijf de pre- en postcondities van deze functie op.
#   3. Herschrijf de functie, met bewaakclausules en een sluitende laatste tak.
#   4. Schrijf de controles die bewijzen dat je versie klopt, ook op de grenzen.
#
# De vier soorten uit 25.6, als geheugensteun:
#   fout 1  de else (of de tak) die te veel aanneemt
#   fout 2  overlappende takken
#   fout 3  de onbereikbare tak
#   fout 4  het ontbrekende geval
#
# Dit bestand print niets: er staat alleen een functie in, en niemand roept haar
# aan. Wil je zelf zien wat ze doet? Zet onderaan bijvoorbeeld
#   print(boetebedrag(40, False, False))
#   print(boetebedrag(40, True, False))
#   print(boetebedrag(40, False, True))
# en vergelijk de drie antwoorden.

def boetebedrag(dagen_te_laat, is_student, is_erelid):
    """De boete in euro's. Bevat vier logicafouten."""
    # Python loopt de if's van boven naar onder af. De eerste voorwaarde die waar
    # is, wint: return stopt de functie meteen, de rest wordt niet meer bekeken.
    # Vraag je bij elke tak af: wie komt hier aan, en is dat de juiste groep?
    if is_erelid:
        # Een erelid betaalt nooit, hoe lang het boek ook te laat is. Heeft het
        # bestuur dat zo beslist, of is het een aanname die niemand uitsprak?
        return 0
    if dagen_te_laat <= 0:
        return 0
    if is_student:
        # Deze tak kijkt alleen naar "student", niet naar het aantal dagen.
        # Reken eens uit wat een student en een gewoon lid betalen als ze
        # allebei 40 dagen te laat zijn.
        return dagen_te_laat * 0.25
    if dagen_te_laat < 7:
        return dagen_te_laat * 0.50
    if dagen_te_laat < 30:
        return 3.50 + (dagen_te_laat - 7) * 0.75
    # Wie komt hier nog aan? Alleen wie 30 dagen of meer te laat is. Kan
    # dagen_te_laat < 14 voor zo iemand ooit waar zijn?
    if dagen_te_laat < 14:
        return 99.00
    # En wat geeft de functie terug als geen enkele tak paste? Een functie die
    # zonder return op haar einde komt, geeft None terug: geen bedrag.
