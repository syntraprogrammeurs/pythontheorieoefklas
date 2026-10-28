# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# 28.6 Een testgeval opschrijven

# De functie die je test: de lidgeldregeling van De Leeslamp.
#   jonger dan 12     -> 0 euro
#   12 tot en met 25  -> 15 euro
#   26 tot en met 64  -> 30 euro
#   65 en ouder       -> 20 euro
# Eerst controleert de functie of de invoer wel geldig is (hoofdstuk 15).
def lidgeld(leeftijd):
    """Het lidgeld in hele euro's, zie de regeling van De Leeslamp."""
    # isinstance(waarde, type) geeft True als de waarde van dat type is.
    # Geen geheel getal (bv. "veertig" of 12.5)? Dan een TypeError opgooien.
    # LET OP: isinstance(True, int) is ook True, want in Python is een bool een
    # soort int. lidgeld(True) geeft hier dus gewoon 0. In oefening 28.1 sluit
    # de functie bool daarom apart uit.
    if not isinstance(leeftijd, int):
        raise TypeError("leeftijd moet een geheel getal zijn")
    # Een KETTINGVERGELIJKING: 0 <= leeftijd <= 120 betekent
    # "0 <= leeftijd EN leeftijd <= 120". Met not ervoor: buiten dat bereik.
    if not 0 <= leeftijd <= 120:
        raise ValueError(f"leeftijd {leeftijd} ligt buiten het bereik")
    # Vanaf hier is de leeftijd geldig. De tests lopen van jong naar oud: wie
    # bij een return uitkomt, verlaat de functie meteen.
    # Elke grens uit de tekst wordt één vergelijking. "Van 12 tot en met 25"
    # wordt hier "< 26": precies op zulke regels zitten de fouten (28.4).
    if leeftijd < 12:
        return 0
    if leeftijd < 26:
        return 15
    if leeftijd < 65:
        return 30
    return 20


# Een TESTGEVAL heeft drie delen, dezelfde als een contract uit hoofdstuk 25:
#   GEGEVEN  -> de uitgangssituatie: de waarde die je klaarzet (12)
#   WANNEER  -> wat er gebeurt: de aanroep lidgeld(12)
#   DAN      -> wat er hoort te gelden: de assert (== 15)
# Waarom 12? Het is een GRENSWAARDE: de laagste leeftijd van het jeugdtarief.
# Schreef iemand per ongeluk "<= 12" in plaats van "< 12", dan faalt deze test.
# gegeven: een lid van 12 — de onderste grens van het jeugdtarief
# wanneer: we het lidgeld berekenen
# dan    : is het 15 euro
# assert (hoofdstuk 25) doet niets als de voorwaarde waar is. Is ze onwaar,
# dan stopt het programma met een AssertionError.
assert lidgeld(12) == 15

# GRENSWAARDENANALYSE (28.4): bij elke grens drie waarden, eronder, erop en
# erboven. Bij de grens 12 zijn dat 11, 12 en 13; bij de grens 65: 64, 65, 66.
# Zo zie je meteen of de overgang op de juiste leeftijd valt.
print("Grens 11/12/13:", lidgeld(11), lidgeld(12), lidgeld(13))
print("Grens 64/65/66:", lidgeld(64), lidgeld(65), lidgeld(66))


# Verwachte uitvoer:
# Grens 11/12/13: 0 15 15
# Grens 64/65/66: 30 20 20
