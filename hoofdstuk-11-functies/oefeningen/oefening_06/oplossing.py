# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oplossing 6 — Type lidmaatschap bepalen

def type_lid(leeftijd):
    if leeftijd < 12:
        return "kind"
    if leeftijd < 18:
        return "jongere"
    return "volwassene"


for leeftijd in (8, 15, 34):
    print(f"{leeftijd} jaar: {type_lid(leeftijd)}")
