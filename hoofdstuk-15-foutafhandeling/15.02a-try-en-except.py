# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.2 try en except

tekst = "abc"

try:
    getal = int(tekst)
    print(f"Het getal is {getal}")
except ValueError:
    print("Dat is geen geldig getal")

print("Het programma loopt gewoon door")


# Verwachte uitvoer:
# Dat is geen geldig getal
# Het programma loopt gewoon door
