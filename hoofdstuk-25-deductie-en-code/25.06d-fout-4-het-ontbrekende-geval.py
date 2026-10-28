# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 4 — het ontbrekende geval

# LET OP: deze functie is met opzet FOUT, en het is de gevaarlijkste van de vier:
# Python klaagt helemaal niet.
#
# Fout 4 uit 25.6: het ONTBREKENDE GEVAL. De keten is niet VOLLEDIG (25.5): wie 65
# of ouder is, past op geen enkele tak.
# Vergelijk met tarief() in 25.05: daar stond onderaan nog "return 20".
def tarief_fout(leeftijd):
    """Fout: er is geen tak voor 65 en ouder."""
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd < 65:
        return 30
    # Hier komt een leeftijd van 65 of meer terecht, en er staat niets meer.
    # Een functie die het einde bereikt zonder return, geeft automatisch None
    # terug (11.4). Er komt dus geen foutmelding, alleen None.


print("30 jaar:", tarief_fout(30))
# 70 valt door alle takken heen: de functie geeft None, en print toont dat gewoon.
print("70 jaar:", tarief_fout(70))

# Waarom dat gevaarlijk is: die None reist verder door je programma, tot hij
# ergens anders problemen geeft. Bijvoorbeeld tarief_fout(70) + 5 geeft
#     TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
# ver van de plek waar de fout ontstond. Dat is het omgekeerde van FALEN BIJ DE
# BRON (25.2).
# De gewoonte die dit voorkomt: elke keten eindigt met een tak die ALLES opvangt.
# Weet je zeker dat er niets overblijft, sluit dan af met een raise (zie 25.06e).


# Verwachte uitvoer:
# 30 jaar: 30
# 70 jaar: None
