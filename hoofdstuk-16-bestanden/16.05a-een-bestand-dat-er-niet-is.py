# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.5 Een bestand dat er niet is

try:
    with open("bestaat-niet.txt", encoding="utf-8") as bestand:
        print(bestand.read())
except FileNotFoundError:
    print("Dat bestand bestaat nog niet")


# Verwachte uitvoer:
# Dat bestand bestaat nog niet
