# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.7 Functies en veranderlijke argumenten
#
# Vergelijk:

def vervang(lijst):
    """Wijst de naam binnenin naar iets anders."""
    lijst = ["Nieuw"]


leden = ["Anke"]
vervang(leden)
print(leden)


# Verwachte uitvoer:
# ['Anke']
