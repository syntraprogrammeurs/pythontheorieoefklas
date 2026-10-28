# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.1 — Vier fouten in één keten, uitwerking
#
# 4. De controles.

# Eerst nog eens dezelfde functie als in uitwerking 3, maar korter: zonder de
# uitleg en met de afronding en het maximum in één regel. Ze moet hier opnieuw
# staan, want dit bestand moet op zichzelf kunnen draaien.
DAGTARIEF_STUDENT = 0.25
DAGTARIEF_EERSTE_WEEK = 0.50
DAGTARIEF_DAARNA = 0.75
MAXIMUM = 50.00


def boetebedrag(dagen_te_laat, is_student=False, is_erelid=False):
    """De boete in euro's, zie oefening 25.1."""
    assert isinstance(dagen_te_laat, int)
    if dagen_te_laat <= 0:
        return 0.00
    if is_erelid:
        return 0.00
    tarief = DAGTARIEF_STUDENT if is_student else DAGTARIEF_EERSTE_WEEK
    if dagen_te_laat <= 7:
        bedrag = dagen_te_laat * tarief
    else:
        bedrag = 7 * tarief + (dagen_te_laat - 7) * DAGTARIEF_DAARNA
    # Eerst min() (nooit boven het maximum), dan round() (op de cent).
    return round(min(bedrag, MAXIMUM), 2)


# Elke controle is een assert: klopt de bewering, dan gebeurt er niets en gaat
# Python verder. Klopt ze niet, dan stopt het programma met een AssertionError.
# Komt de print onderaan in beeld, dan zijn dus ALLE controles geslaagd.
def controleer():
    """De controles die uit de contracten volgen."""
    # de grenzen
    # Fouten zitten bijna altijd op een grens: net ervoor, erop, net erna.
    # -1 en 0 zijn de grens "niet te laat", 7 en 8 de overgang naar het
    # tweede tarief. 8 dagen = 7 x 0,50 + 1 x 0,75 = 4,25.
    assert boetebedrag(-1) == 0.00
    assert boetebedrag(0) == 0.00
    assert boetebedrag(1) == 0.50
    assert boetebedrag(7) == 3.50
    assert boetebedrag(8) == 4.25

    # het erelid
    # De regel die het bestuur moet bevestigen, staat nu ook als controle vast.
    # Verandert iemand ze later, dan merkt die het meteen.
    assert boetebedrag(100, is_erelid=True) == 0.00

    # de student betaalt nooit meer dan een gewoon lid
    # Dit bewaakt de regel achter de overlappende takken: student zijn mag
    # het bedrag alleen kleiner maken, nooit groter.
    # range(0, 400) loopt van 0 tot en met 399: 400 waarden.
    for dagen in range(0, 400):
        assert boetebedrag(dagen, is_student=True) <= boetebedrag(dagen)

    # postconditie: het bedrag daalt nooit als de dagen stijgen
    # We onthouden telkens het vorige bedrag en eisen dat het nieuwe minstens
    # even groot is. De oude versie zou hier stuklopen: bij 30 dagen kwam er
    # None, en None >= 20.75 geeft zelfs een TypeError.
    vorige = 0.00
    for dagen in range(0, 400):
        nu = boetebedrag(dagen)
        # De tekst na de komma is de foutmelding: ze zegt meteen WAAR het misgaat.
        assert nu >= vorige, f"bij {dagen} dagen daalt het bedrag"
        assert 0 <= nu <= MAXIMUM
        vorige = nu

    print("Alle controles geslaagd, voor 400 waarden.")


controleer()

# Waarom die lus over 400 waarden meer waard is dan vijf losse controles: de
# losse controles toetsen de gevallen waar jij aan dacht. De lus toetst een
# EIGENSCHAP ("het bedrag daalt nooit"), en die vangt ook de fout die je niet
# voorzag. Het blijft wel inductie, geen bewijs: 400 waarden zijn 400
# waarnemingen. Maar ze zijn systematisch gekozen, niet willekeurig bedacht.


# Verwachte uitvoer:
# Alle controles geslaagd, voor 400 waarden.
