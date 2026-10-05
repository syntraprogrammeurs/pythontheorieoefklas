# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 10 — Het uitleenoverzicht

uitleningen = [
    {"lid": "Anke", "titel": "Het diner", "genre": "roman"},
    {"lid": "Bram", "titel": "De Kameleon", "genre": "jeugd"},
    {"lid": "Anke", "titel": "Turks fruit", "genre": "roman"},
    {"lid": "Cato", "titel": "Suske en Wiske", "genre": "strip"},
    {"lid": "Anke", "titel": "Verzamelde gedichten", "genre": "poëzie"},
    {"lid": "Bram", "titel": "Het diner", "genre": "roman"},
]

per_lid = {}
for uitlening in uitleningen:
    lid = uitlening["lid"]
    per_lid[lid] = per_lid.get(lid, 0) + 1

for lid, aantal in sorted(per_lid.items(), key=lambda paar: paar[1], reverse=True):
    print(f"{lid:<6}{aantal}")

genres = set()
for uitlening in uitleningen:
    genres.add(uitlening["genre"])
print(f"Genres: {sorted(genres)}")

anke = []
for uitlening in uitleningen:
    if uitlening["lid"] == "Anke":
        anke.append(uitlening["titel"])
print(f"Anke las: {anke}")

titels = set()
for uitlening in uitleningen:
    titels.add(uitlening["titel"])
print(f"{len(titels)} verschillende titels")
