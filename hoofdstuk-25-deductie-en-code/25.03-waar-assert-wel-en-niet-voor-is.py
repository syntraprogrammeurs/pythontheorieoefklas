# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.3 Waar assert wél en niet voor is

# LET OP, de valkuil van deze paragraaf: assert kan VERDWIJNEN.
#   python programma.py       -> de asserts doen hun werk
#   python -O programma.py    -> alle asserts worden overgeslagen
# (-O staat voor "optimize".) Een controle die per se moet gebeuren, schrijf je
# dus NOOIT met assert. De vuistregel:
#   - assert            -> een aanname van JOU over je EIGEN code ("dit kan niet")
#   - if + raise        -> invoer van een gebruiker, een bestand of het netwerk
#   - nooit assert      -> rechten en toegang: valt de controle weg, dan mag
#                          iedereen alles
# Deze functie gebruikt beide, elk voor wat het hoort.
def schrijf_lid_in(naam, leeftijd):
    """Schrijft een lid in.

    Preconditie: leeftijd is een geheel getal (aanname over onze eigen code).
    Invoer van buitenaf wordt met raise afgedwongen, niet met assert.
    """
    # isinstance(waarde, type) geeft True als de waarde van dat type is (18.7).
    # isinstance(34, int) -> True, isinstance("34", int) -> False.
    # Dit is een aanname over ONZE code: ergens eerder hoort de tekst uit input()
    # al met int() omgezet te zijn (6.5). Klopt dat niet, dan zit de fout bij
    # ons, niet bij de gebruiker. Daarom mag dit een assert zijn.
    assert isinstance(leeftijd, int), "leeftijd hoort al een int te zijn"

    # Vanaf hier: controles op wat de GEBRUIKER invulde. Die moeten altijd
    # gebeuren, ook met python -O. Daarom if + raise ValueError (15.5).
    # naam.strip() haalt spaties vooraan en achteraan weg (8.5). Blijft er een
    # lege string over, dan is die FALSY (7.8), en is "not ..." dus True.
    if not naam.strip():
        raise ValueError("de naam mag niet leeg zijn")
    # 0 <= leeftijd <= 120 is een kettingvergelijking (7.3). Met not ervoor:
    # "als de leeftijd NIET tussen 0 en 120 ligt".
    if not 0 <= leeftijd <= 120:
        raise ValueError(f"leeftijd {leeftijd} ligt buiten het bereik")

    # Alles in orde: een dictionary (hoofdstuk 13) met de opgekuiste naam.
    return {"naam": naam.strip(), "leeftijd": leeftijd}


# Een geldige inschrijving. De spaties rond "Anke" verdwijnen door strip().
print(schrijf_lid_in("  Anke  ", 34))

# Een ongeldige leeftijd. raise ValueError gooit een fout op, en try/except
# (hoofdstuk 15) vangt die op. "as fout" bewaart het foutobject; print(fout) toont
# de tekst die je aan ValueError meegaf.
# Zo loopt het programma niet vast, maar krijgt de gebruiker een nette melding.
# Met een assert in plaats van de raise zou dit niet kunnen: een AssertionError
# is geen ValueError, en met python -O zou er zelfs niets meer gecontroleerd worden.
try:
    schrijf_lid_in("Bram", 250)
except ValueError as fout:
    print("Geweigerd:", fout)


# Verwachte uitvoer:
# {'naam': 'Anke', 'leeftijd': 34}
# Geweigerd: leeftijd 250 ligt buiten het bereik
