# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 1 — Een boek als tuple

boek = ("Het diner", "Herman Koch", 2009)

print(boek)
print(boek[1])
print(f"Aantal gegevens: {len(boek)}")

titel, auteur, jaar = boek
print(f"{titel} van {auteur} ({jaar})")
