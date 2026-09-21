# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# 6.8 Het lidgeldprogramma
#
# Nu kun je het probleem uit hoofdstuk 3 echt schrijven. De selectie komt pas in
# hoofdstuk 9, dus je vraagt hier alleen en rekent.
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.

# De Leeslamp — het lidgeld berekenen
# Cursus Python basis, hoofdstuk 6

LIDGELD_VOLWASSENE = 30
KORTING = 5

naam = input("Naam van het lid: ")
jaren_lid = int(input("Aantal jaren lid: "))
aantal_boeken = int(input("Aantal geleende boeken: "))

lidgeld = LIDGELD_VOLWASSENE - KORTING
gemiddeld_per_jaar = aantal_boeken / jaren_lid

print()
print(f"Lid          : {naam}")
print(f"Jaren lid    : {jaren_lid}")
print(f"Te betalen   : {lidgeld:.2f} euro")
print(f"Boeken/jaar  : {gemiddeld_per_jaar:.1f}")


# Voorbeeld van een uitvoering, met de invoer erbij:
# Naam van het lid: Anke Peeters
# Aantal jaren lid: 3
# Aantal geleende boeken: 22
#
# Lid          : Anke Peeters
# Jaren lid    : 3
# Te betalen   : 25.00 euro
# Boeken/jaar  : 7.3
