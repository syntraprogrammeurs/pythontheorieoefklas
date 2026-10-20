# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.2 Waarom with

bestand = open("leden.txt", "w", encoding="utf-8")
bestand.write("Anke Peeters\n")
bestand.close()

print("ook geschreven, maar riskanter")


# Verwachte uitvoer:
# ook geschreven, maar riskanter
