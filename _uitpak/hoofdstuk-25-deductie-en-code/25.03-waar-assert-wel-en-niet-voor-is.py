# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.3 Waar assert wél en niet voor is

def schrijf_lid_in(naam, leeftijd):
    """Schrijft een lid in.

    Preconditie: leeftijd is een geheel getal (aanname over onze eigen code).
    Invoer van buitenaf wordt met raise afgedwongen, niet met assert.
    """
    assert isinstance(leeftijd, int), "leeftijd hoort al een int te zijn"

    if not naam.strip():
        raise ValueError("de naam mag niet leeg zijn")
    if not 0 <= leeftijd <= 120:
        raise ValueError(f"leeftijd {leeftijd} ligt buiten het bereik")

    return {"naam": naam.strip(), "leeftijd": leeftijd}


print(schrijf_lid_in("  Anke  ", 34))

try:
    schrijf_lid_in("Bram", 250)
except ValueError as fout:
    print("Geweigerd:", fout)


# Verwachte uitvoer:
# {'naam': 'Anke', 'leeftijd': 34}
# Geweigerd: leeftijd 250 ligt buiten het bereik
