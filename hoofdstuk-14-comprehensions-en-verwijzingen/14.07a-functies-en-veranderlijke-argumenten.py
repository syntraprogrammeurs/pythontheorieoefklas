# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.7 Functies en veranderlijke argumenten
#
# Dit is waar de theorie je echt raakt.

def voeg_toe(lijst, waarde):
    """Past de meegegeven lijst aan."""
    lijst.append(waarde)


leden = ["Anke"]
voeg_toe(leden, "Bram")
print(leden)


# Verwachte uitvoer:
# ['Anke', 'Bram']
