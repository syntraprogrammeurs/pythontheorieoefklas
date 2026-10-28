# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# Klassikale oefening 28.1 — De lidgeldregeling volledig testen, uitwerking
#
# 4. Dezelfde tests op een foute versie.

# Dezelfde geldige gevallen als in uitwerking-a: (leeftijd, verwacht lidgeld).
# Drie waarden per klasse: twee grenswaarden en één waarde in het midden.
GELDIG = [
    (0, 0), (5, 0), (11, 0),
    (12, 15), (18, 15), (25, 15),
    (26, 30), (40, 30), (64, 30),
    (65, 20), (90, 20), (120, 20),
]


# Deze versie is MET OPZET FOUT. Je herstelt ze niet: je kijkt welke test de
# fout betrapt.
# De regel zegt "vanaf 65 betaal je 20 euro". Een lid van 65 hoort dus in het
# seniorentarief. Hier staat "<= 65" waar "< 65" hoort, zodat 65 nog in het
# volwassenentarief (30 euro) valt. Dat is de klassieke verwarring tussen
# "meer dan 65" en "vanaf 65" uit 28.4.
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
    # Voor 64 en 66 maakt "<=" of "<" geen verschil. Alleen voor precies 65.
    if leeftijd <= 65:          # hier zit de fout
        return 30
    return 20


# Een LIST COMPREHENSION (hoofdstuk 14) die alleen de mislukte gevallen
# bewaart, telkens als tuple (leeftijd, werkelijk, verwacht).
# Lees ze zo: "voor elke leeftijd en verwacht uit GELDIG, ALS het werkelijke
# resultaat afwijkt, neem dan (leeftijd, werkelijk, verwacht) op".
# lidgeld_fout wordt per geval twee keer opgeroepen (in de if en in het tuple):
# dat mag hier, de functie is snel en geeft telkens hetzelfde.
gefaald = [(leeftijd, lidgeld_fout(leeftijd), verwacht)
           for leeftijd, verwacht in GELDIG
           if lidgeld_fout(leeftijd) != verwacht]

# Het verslag: hoeveel van de 12 goed, en welke fout.
print(f"{len(GELDIG) - len(gefaald)} van de {len(GELDIG)} geldige gevallen goed")
for leeftijd, werkelijk, verwacht in gefaald:
    print(f"  FOUT bij {leeftijd}: {werkelijk} in plaats van {verwacht}")

# print() zonder argument drukt een lege regel af.
print()
# De les van deze oefening: wie alleen waarden MIDDEN in een klasse kiest
# (40 en 90), ziet de fout niet. Beide geven het juiste bedrag. Alleen de
# GRENSWAARDE 65 betrapt de fout.
print("Zonder grenswaarden zou je 40 en 90 testen:")
print(f"  40 -> {lidgeld_fout(40)}, 90 -> {lidgeld_fout(90)}  (allebei goed)")


# Verwachte uitvoer:
# 11 van de 12 geldige gevallen goed
#   FOUT bij 65: 30 in plaats van 20
#
# Zonder grenswaarden zou je 40 en 90 testen:
#   40 -> 30, 90 -> 20  (allebei goed)
