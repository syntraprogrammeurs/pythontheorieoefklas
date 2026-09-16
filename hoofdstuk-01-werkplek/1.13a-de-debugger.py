# Python basis — theoriebundel
# Hoofdstuk 1 — Je Python-werkplek professioneel opzetten
# 1.13 De debugger
#
# Vervang de inhoud van main.py door:

leden = ["Anke", "Bram", "Cato"]
totaal = 0

for lid in leden:
    totaal = totaal + len(lid)

print(f"Samen {totaal} letters in {len(leden)} namen")
