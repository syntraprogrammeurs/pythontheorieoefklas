# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# 6.6 De gebruiker iets vragen: input()
#
# input() geeft altijd tekst terug. Altijd. Ook als de gebruiker een getal intypt.
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.
#
# Let op: dit voorbeeld loopt met opzet vast. De foutmelding onderaan is wat de bundel
# wil tonen.

leeftijd = input("Hoe oud ben je? ")
print(leeftijd + 1)


# Verwachte uitvoer:
# TypeError: can only concatenate str (not "int") to str
