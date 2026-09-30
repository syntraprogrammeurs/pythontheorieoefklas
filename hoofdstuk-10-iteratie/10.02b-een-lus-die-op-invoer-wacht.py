# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.2 De while-lus — Een lus die op invoer wacht
#
# Hier komt while echt tot zijn recht, want je weet niet hoe vaak de gebruiker iets
# zal typen.
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.

# Dit voorbeeld wacht op invoer; voer het uit in je eigen terminal.
totaal = 0
antwoord = ""

while antwoord != "stop":
    antwoord = input("Aantal bladzijden (of 'stop'): ")
    if antwoord != "stop":
        totaal += int(antwoord)

print(f"Samen {totaal} bladzijden")
