# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.7 Functies en veranderlijke argumenten — Welke van de twee stijlen kies je?

def voeg_toe_aanpassen(lijst: list, waarde: str) -> None:
    """Voegt toe aan de meegegeven lijst. Geeft niets terug."""
    lijst.append(waarde)


def voeg_toe_nieuw(lijst: list, waarde: str) -> list:
    """Geeft een nieuwe lijst terug. Laat het origineel ongemoeid."""
    return lijst + [waarde]


a = ["Anke"]
voeg_toe_aanpassen(a, "Bram")
print(a)

b = ["Anke"]
c = voeg_toe_nieuw(b, "Bram")
print(b, c)


# Verwachte uitvoer:
# ['Anke', 'Bram']
# ['Anke'] ['Anke', 'Bram']
