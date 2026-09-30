# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oefening 10 — De ledenlijst van de club

# Gebruik deze lijst van lijsten:
#
# leden = [
#     ["Anke Peeters", 34, 3],
#     ["Bram Coppens", 20, 1],
#     ["Cato Dhondt", 11, 4],
#     ["Dirk Maes", 67, 12],
# ]
#
# Elk lid is [naam, leeftijd, jaren lid].
#
# 1. Voeg het lid ["Emma Claes", 16, 0] toe.
# 2. Toon "<aantal> leden".
# 3. Toon alle leden gesorteerd op jaren lid, de trouwste leden eerst,
#    telkens als f"{naam:<16}{jaren:>3} jaar lid".
#    Gebruik sorted() met een lambda als key en reverse=True.
# 4. Bouw met een for-lus een lijst minderjarig met de namen van
#    de leden jonger dan 18. Toon "Minderjarig: <minderjarig>".
# 5. Tel met een for-lus de leeftijden op en toon
#    "Gemiddelde leeftijd: <gemiddelde>".
#
# Verwachte uitvoer:
# 5 leden
# Dirk Maes        12 jaar lid
# Cato Dhondt       4 jaar lid
# Anke Peeters      3 jaar lid
# Bram Coppens      1 jaar lid
# Emma Claes        0 jaar lid
# Minderjarig: ['Cato Dhondt', 'Emma Claes']
# Gemiddelde leeftijd: 29.6
