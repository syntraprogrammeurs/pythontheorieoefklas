# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.6 Een testgeval opschrijven

def lidgeld(leeftijd):
    """Het lidgeld in hele euro's, zie de regeling van De Leeslamp."""
    if not isinstance(leeftijd, int):
        raise TypeError("leeftijd moet een geheel getal zijn")
    if not 0 <= leeftijd <= 120:
        raise ValueError(f"leeftijd {leeftijd} ligt buiten het bereik")
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd < 65:
        return 30
    return 20


# gegeven: een lid van 12 — de onderste grens van het jeugdtarief
# wanneer: we het lidgeld berekenen
# dan    : is het 15 euro
assert lidgeld(12) == 15

print("Grens 11/12/13:", lidgeld(11), lidgeld(12), lidgeld(13))
print("Grens 64/65/66:", lidgeld(64), lidgeld(65), lidgeld(66))


# Verwachte uitvoer:
# Grens 11/12/13: 0 15 15
# Grens 64/65/66: 30 20 20
