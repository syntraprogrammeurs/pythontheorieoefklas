# Python basis — theoriebundel
# Hoofdstuk 8 — Strings
# 8.5 De methodes die je constant gebruikt — Zoeken en testen

titel = "De ontdekking van de hemel"

print("hemel" in titel)              # True   — de gewone manier
print(titel.find("hemel"))           # 21     — de positie, of -1
print(titel.find("zee"))             # -1     — niet gevonden
print(titel.count("de"))             # 2      — hoofdlettergevoelig
print(titel.startswith("De"))        # True
print(titel.endswith("hemel"))       # True
print(titel.index("hemel"))          # 21     — zoals find, maar met een fout als het er niet is


# Verwachte uitvoer:
# True
# 21
# -1
# 2
# True
# True
# 21
