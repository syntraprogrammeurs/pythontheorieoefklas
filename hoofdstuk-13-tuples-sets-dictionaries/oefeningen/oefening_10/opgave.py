# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oefening 10 — Het uitleenoverzicht

# Gebruik deze lijst van dictionaries:
#
# uitleningen = [
#     {"lid": "Anke", "titel": "Het diner", "genre": "roman"},
#     {"lid": "Bram", "titel": "De Kameleon", "genre": "jeugd"},
#     {"lid": "Anke", "titel": "Turks fruit", "genre": "roman"},
#     {"lid": "Cato", "titel": "Suske en Wiske", "genre": "strip"},
#     {"lid": "Anke", "titel": "Verzamelde gedichten", "genre": "poëzie"},
#     {"lid": "Bram", "titel": "Het diner", "genre": "roman"},
# ]
#
# 1. Tel in een dictionary per_lid hoeveel boeken elk lid leende.
#    Gebruik het patroon per_lid[lid] = per_lid.get(lid, 0) + 1.
# 2. Toon de leden gesorteerd van meeste naar minste uitleningen,
#    telkens als f"{lid:<6}{aantal}".
# 3. Verzamel alle genres in een set en toon
#    "Genres: <genres alfabetisch gesorteerd>".
# 4. Maak een lijst met de titels die Anke leende, in de volgorde
#    van uitlenen, en toon "Anke las: <titels>".
# 5. Toon "<aantal> verschillende titels".
#
# Verwachte uitvoer:
# Anke  3
# Bram  2
# Cato  1
# Genres: ['jeugd', 'poëzie', 'roman', 'strip']
# Anke las: ['Het diner', 'Turks fruit', 'Verzamelde gedichten']
# 5 verschillende titels
