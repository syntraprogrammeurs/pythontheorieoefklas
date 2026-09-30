# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oefening 8 — Mag dit lid nog lenen?

# Gebruik deze globale constante:
#
# MAX_UITLENINGEN = 5
#
# Maak een functie kan_lenen(aantal_geleend) die MAX_UITLENINGEN
# leest (zonder global) en True teruggeeft als aantal_geleend
# kleiner is dan MAX_UITLENINGEN, anders False.
#
# Maak ook een functie leen_uit(aantal_geleend) die het aantal
# met 1 verhoogt en teruggeeft. Gebruik hiervoor GEEN global:
# geef de nieuwe waarde terug met return.
#
# Begin met aantal_geleend = 3.
# Leen twee keer een boek uit met leen_uit en werk aantal_geleend
# telkens bij met het resultaat.
#
# Toon na elke uitlening:
# "Geleend: <aantal_geleend>, mag nog lenen: <kan_lenen(aantal_geleend)>"
#
# Verwachte uitvoer:
# Geleend: 4, mag nog lenen: True
# Geleend: 5, mag nog lenen: False
