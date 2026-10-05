# Python basis — theoriebundel
# Hoofdstuk 14 — Comprehensions, kopie versus verwijzing
# 14.8 De ledenlijst met comprehensions

# De Leeslamp — de ledenlijst, korter geschreven
# Cursus Python basis, hoofdstuk 14

leden = [
    {"naam": "Anke Peeters", "leeftijd": 34, "jaren": 3, "student": False},
    {"naam": "Bram Coppens", "leeftijd": 20, "jaren": 1, "student": True},
    {"naam": "Cato Dhondt", "leeftijd": 11, "jaren": 4, "student": False},
    {"naam": "Dirk Vermeulen", "leeftijd": 52, "jaren": 8, "student": False},
]

namen = [lid["naam"] for lid in leden]
volwassen = [lid["naam"] for lid in leden if lid["leeftijd"] >= 18]
studenten = [lid["naam"] for lid in leden if lid["student"]]
trouw = [lid["naam"] for lid in leden if lid["jaren"] >= 3]
per_naam = {lid["naam"]: lid["leeftijd"] for lid in leden}
initialen = [
    "".join(deel[0] for deel in lid["naam"].split())
    for lid in leden
]

print("Alle namen  :", namen)
print("Volwassen   :", volwassen)
print("Studenten   :", studenten)
print("Drie jaar+  :", trouw)
print("Initialen   :", initialen)
print("Leeftijden  :", per_naam)
print()
print("Gemiddelde leeftijd:", sum(lid["leeftijd"] for lid in leden) / len(leden))
print("Iemand ouder dan 50:", any(lid["leeftijd"] > 50 for lid in leden))
print("Allemaal lid       :", all(lid["jaren"] >= 1 for lid in leden))


# Verwachte uitvoer:
# Alle namen  : ['Anke Peeters', 'Bram Coppens', 'Cato Dhondt', 'Dirk Vermeulen']
# Volwassen   : ['Anke Peeters', 'Bram Coppens', 'Dirk Vermeulen']
# Studenten   : ['Bram Coppens']
# Drie jaar+  : ['Anke Peeters', 'Cato Dhondt', 'Dirk Vermeulen']
# Initialen   : ['AP', 'BC', 'CD', 'DV']
# Leeftijden  : {'Anke Peeters': 34, 'Bram Coppens': 20, 'Cato Dhondt': 11, 'Dirk Vermeulen': 52}
#
# Gemiddelde leeftijd: 29.25
# Iemand ouder dan 50: True
# Allemaal lid       : True
