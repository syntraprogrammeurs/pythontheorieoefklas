# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oefening 10 — Het boekenoverzicht opgedeeld in functies

# Gebruik deze lijst:
#
# boeken = [
#     ("Het diner", 2009, 288),
#     ("Turks fruit", 1969, 175),
#     ("De ontdekking van de hemel", 1992, 928),
#     ("Grand Hotel Europa", 2018, 592),
# ]
#
# Elke tuple is (titel, jaar, bladzijden).
#
# Maak drie functies:
#
# 1. totaal_bladzijden(boeken) -> int
#    Telt met een for-lus het aantal bladzijden van alle boeken op
#    en geeft dat totaal terug.
#
# 2. dikste_boek(boeken)
#    Geeft de titel terug van het boek met het meeste bladzijden.
#    Gebruik hiervoor max() met een lambda als key.
#
# 3. toon_op_jaar(boeken) -> None
#    Toont de boeken gesorteerd van oud naar nieuw, telkens als:
#    "<jaar>  <titel>"
#    Gebruik hiervoor sorted() met een lambda als key.
#
# Roep de drie functies na elkaar aan:
# - toon eerst het totaal aantal bladzijden
# - toon daarna het dikste boek
# - toon daarna het overzicht op jaar
#
# Verwachte uitvoer:
# Totaal aantal bladzijden: 1983
# Dikste boek: De ontdekking van de hemel
# 1969  Turks fruit
# 1992  De ontdekking van de hemel
# 2009  Het diner
# 2018  Grand Hotel Europa
