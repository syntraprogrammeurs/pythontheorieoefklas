# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oplossing 10 — Het boekenoverzicht opgedeeld in functies

def totaal_bladzijden(boeken):
    totaal = 0
    for titel, jaar, bladzijden in boeken:
        totaal += bladzijden
    return totaal


def dikste_boek(boeken):
    boek = max(boeken, key=lambda boek: boek[2])
    return boek[0]


def toon_op_jaar(boeken):
    for titel, jaar, bladzijden in sorted(boeken, key=lambda boek: boek[1]):
        print(f"{jaar}  {titel}")


boeken = [
    ("Het diner", 2009, 288),
    ("Turks fruit", 1969, 175),
    ("De ontdekking van de hemel", 1992, 928),
    ("Grand Hotel Europa", 2018, 592),
]

print(f"Totaal aantal bladzijden: {totaal_bladzijden(boeken)}")
print(f"Dikste boek: {dikste_boek(boeken)}")
toon_op_jaar(boeken)
