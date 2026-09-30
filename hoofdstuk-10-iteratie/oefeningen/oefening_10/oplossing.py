# Python basis — oefeningen
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Oplossing 10 — Namenlijst opkuisen

namen = ["  an ", "", "ELS", "  tom", "Sara  ", "   "]
nette_namen = []

for naam in namen:
    naam = naam.strip()

    if not naam:
        continue

    nette_namen.append(naam.capitalize())

for nummer, naam in enumerate(nette_namen, start=1):
    print(f"{nummer}. {naam}")
