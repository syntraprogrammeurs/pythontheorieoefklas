# Python basis — theoriebundel
# Hoofdstuk 21 — DevOps, en waar Git daarin past
# 21.5 Wat die pijplijn dan precies draait
#
# De laatste stap van de pijplijn hierboven was python controle.py. Dat bestand
# schrijf je zelf. In deze cursus blijft het bij assert; hoofdstuk 28 gaat er dieper
# op in.

# controle.py — het bestand dat de pijplijn draait
# Cursus Python basis, hoofdstuk 21

# Een PIJPLIJN is een reeks stappen die de computer na elke push vanzelf uitvoert.
# De pijplijn leest je uitvoer niet: ze kijkt alleen naar de AFSLUITCODE van je
# programma. 0 betekent "geslaagd" (groen vinkje), elk ander getal betekent
# "gefaald" (rood kruisje). Dit bestand zorgt ervoor dat het programma vastloopt,
# en dus niet met 0 eindigt, zodra één controle faalt.


# De functie die je controleert: het lidgeld van De Leeslamp.
# De volgorde van de if's telt: eerst de jongeren, dan de senioren, dan de rest.
def lidgeld(leeftijd, is_student=False):
    """Het jaarlijkse lidgeld van De Leeslamp, in hele euro's."""
    if leeftijd < 12:
        return 0
    # >= : wie precies 65 is, hoort er al bij. Die grens test de laatste assert.
    if leeftijd >= 65:
        return 20
    # De verkorte keuze uit hoofdstuk 9: 15 voor een student, anders 30.
    return 15 if is_student else 30


# ASSERT (uitgebreid in hoofdstuk 25) controleert of een voorwaarde waar is.
# Vorm: assert voorwaarde, "boodschap"
#   - is de voorwaarde True, dan gebeurt er niets en gaat het programma verder
#   - is ze False, dan stopt het programma met een AssertionError, met jouw
#     boodschap erbij. Een fout die niemand opvangt, geeft een afsluitcode
#     die niet 0 is: precies wat de pijplijn moet zien.
# Elke assert vergelijkt wat de functie teruggeeft met wat je verwacht (==).
# Kijk naar de gekozen leeftijden: 11 en 12 liggen net onder en op de grens van
# 12, en 65 ligt precies op de grens voor senioren. Bij grenzen sluipen de
# fouten erin (een < waar <= hoort), dus daar test je.
def controleer():
    """Draait alle controles en stopt bij de eerste die faalt."""
    assert lidgeld(8) == 0, "wie jonger is dan 12 betaalt niets"
    assert lidgeld(11) == 0, "11 jaar valt nog onder de vrijstelling"
    assert lidgeld(12) == 30, "12 jaar is de grens: wel betalen"
    assert lidgeld(30) == 30, "een volwassene betaalt 30"
    assert lidgeld(30, is_student=True) == 15, "een student betaalt de helft"
    assert lidgeld(65) == 20, "vanaf 65 geldt het seniorentarief"
    # Deze regel bereik je alleen als ALLE asserts hierboven geslaagd zijn.
    print("Alle 6 controles geslaagd.")


# De controles echt uitvoeren. Geslaagd: het programma eindigt gewoon, met
# afsluitcode 0. Wil je die code zelf zien? In PowerShell: echo $LASTEXITCODE.
controleer()


# Verwachte uitvoer:
# Alle 6 controles geslaagd.
