# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.3 De openingsmodi

# Python opent leden.txt in Write-modus ("w").
# Omdat "w" destructief is, wordt een eventueel bestaande leden.txt direct volledig leeggemaakt. Als het bestand nog niet bestond, maakt Python het nu aan.

with open("leden.txt", "w", encoding="utf-8") as bestand:
    bestand.write("Anke Peeters\n")

# Python opent hetzelfde bestand opnieuw, maar dit keer in Append-modus ("a").

with open("leden.txt", "a", encoding="utf-8") as bestand:
    bestand.write("Bram Coppens\n")

# De methode bestand.read() leest de volledige inhoud van het bestand in één keer uit 
# als een tekstreeks (string).
with open("leden.txt", encoding="utf-8") as bestand:
    print(bestand.read())


# Verwachte uitvoer:
# Anke Peeters
# Bram Coppens
