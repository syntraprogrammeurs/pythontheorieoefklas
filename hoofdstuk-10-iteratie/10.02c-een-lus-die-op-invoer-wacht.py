# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.2 De while-lus — Een lus die op invoer wacht
#
# Dit werkt, maar antwoord = "" bovenaan is lelijk: je zet een waarde die nergens iets
# betekent, alleen om de lus te kunnen starten. De nette vorm:
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.

# Dit voorbeeld wacht op invoer; voer het uit in je eigen terminal.
totaal = 0

while True:
    antwoord = input("Aantal bladzijden (of 'stop'): ")
    if antwoord == "stop":
        break
    totaal += int(antwoord)

print(f"Samen {totaal} bladzijden")
