# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 2 — overlappende takken

# LET OP: deze functie is met opzet FOUT, maar op een verraderlijke manier: ze geeft
# vandaag de juiste bedragen. Het probleem is wat er MORGEN gebeurt.
#
# Fout 2 uit 25.6: OVERLAPPENDE TAKKEN. De keten is niet ELKAAR UITSLUITEND (25.5):
# een student van 20 past op twee takken tegelijk, want hij is student EN jonger
# dan 26. Welke tak wint, hangt dan alleen af van de VOLGORDE.
# Dit is geen drogreden maar een ordeningsfout: de logica zit verstopt in welke
# regel bovenaan staat.
def korting_fout(leeftijd, is_student):
    """Fout: een student van 20 valt op twee takken, en de volgorde beslist."""
    # Tak 1: elke student krijgt een korting van 50.
    if is_student:
        return 50
    # Tak 2: iedereen jonger dan 26 krijgt 25. Een student jonger dan 26 past
    # hier OOK op, maar komt hier nooit, omdat tak 1 al met return vertrok.
    if leeftijd < 26:
        return 25
    # De rest krijgt geen korting.
    return 0


# Drie gevallen. Het eerste is het overlappende: student EN jonger dan 26.
print("student van 20:", korting_fout(20, True))
print("student van 30:", korting_fout(30, True))
print("niet-student 20:", korting_fout(20, False))

# Probeer het zelf in gedachten: verwissel de twee if-blokken. Dan krijgt de student
# van 20 plots 25 in plaats van 50. Geen foutmelding, alleen een ander bedrag.
# Dat is de truc uit 25.8: verwissel twee takken; verandert er iets, dan
# overlappen ze.
# Hoe het beter kan: maak de voorwaarden zo dat elke invoer op precies één tak
# past, of maak van "student" iets dat het TARIEF bepaalt in plaats van een eigen
# tak (zo doet de uitwerking van oefening 25.1 het).


# Verwachte uitvoer:
# student van 20: 50
# student van 30: 50
# niet-student 20: 25
