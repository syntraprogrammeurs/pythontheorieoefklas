# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oplossing 8 — Mag dit lid nog lenen?

MAX_UITLENINGEN = 5


def kan_lenen(aantal_geleend):
    return aantal_geleend < MAX_UITLENINGEN


def leen_uit(aantal_geleend):
    return aantal_geleend + 1


aantal_geleend = 3

for _ in range(2):
    aantal_geleend = leen_uit(aantal_geleend)
    print(f"Geleend: {aantal_geleend}, mag nog lenen: {kan_lenen(aantal_geleend)}")
