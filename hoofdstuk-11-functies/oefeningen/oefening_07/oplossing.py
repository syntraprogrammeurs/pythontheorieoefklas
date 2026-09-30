# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oplossing 7 — Boeken verdelen over dozen

def verdeel_boeken(aantal, per_doos):
    return aantal // per_doos, aantal % per_doos


dozen, rest = verdeel_boeken(134, 20)
print(f"{dozen} dozen en {rest} boeken over")
