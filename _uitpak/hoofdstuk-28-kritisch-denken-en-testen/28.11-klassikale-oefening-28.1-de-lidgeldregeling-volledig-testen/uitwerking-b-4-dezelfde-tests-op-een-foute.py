# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# Klassikale oefening 28.1 — De lidgeldregeling volledig testen, uitwerking
#
# 4. Dezelfde tests op een foute versie.

GELDIG = [
    (0, 0), (5, 0), (11, 0),
    (12, 15), (18, 15), (25, 15),
    (26, 30), (40, 30), (64, 30),
    (65, 20), (90, 20), (120, 20),
]


def lidgeld_fout(leeftijd):
    """Eén fout: <= 65 in plaats van < 65."""
    if isinstance(leeftijd, bool) or not isinstance(leeftijd, int):
        raise TypeError("leeftijd moet een geheel getal zijn")
    if not 0 <= leeftijd <= 120:
        raise ValueError("buiten bereik")
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd <= 65:          # hier zit de fout
        return 30
    return 20


gefaald = [(leeftijd, lidgeld_fout(leeftijd), verwacht)
           for leeftijd, verwacht in GELDIG
           if lidgeld_fout(leeftijd) != verwacht]

print(f"{len(GELDIG) - len(gefaald)} van de {len(GELDIG)} geldige gevallen goed")
for leeftijd, werkelijk, verwacht in gefaald:
    print(f"  FOUT bij {leeftijd}: {werkelijk} in plaats van {verwacht}")

print()
print("Zonder grenswaarden zou je 40 en 90 testen:")
print(f"  40 -> {lidgeld_fout(40)}, 90 -> {lidgeld_fout(90)}  (allebei goed)")


# Verwachte uitvoer:
# 11 van de 12 geldige gevallen goed
#   FOUT bij 65: 30 in plaats van 20
#
# Zonder grenswaarden zou je 40 en 90 testen:
#   40 -> 30, 90 -> 20  (allebei goed)
