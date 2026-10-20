# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.1 Een bestand schrijven
# Zonder with zou je de code zo moeten schrijven:
# bestand = open("leden.txt", "w", encoding="utf-8")
# bestand.write("Anke Peeters\n")
# moet er zelf aan denken om dit te doen:
# bestand.close() 

# Parameter	Modus
# "r"	Read (Lezen)	
#   Dit is de standaardmodus. 
#   Opent een bestand om de tekst te lezen. Als het bestand niet bestaat, 
#   krijg je een foutmelding (FileNotFoundError).
# "a"	Append (Toevoegen)	
#   Opent het bestand om tekst te schrijven, 
#   maar behoudt de bestaande inhoud. 
#   Nieuwe tekst wordt onderaan toegevoegd. 
#   Als het bestand niet bestaat, maakt Python het aan.
# "x"	Exclusive creation	
#   Maakt een nieuw bestand aan en opent het om te schrijven. 
#   Als het bestand al bestaat, faalt de code met een foutmelding (FileExistsError). 
#   Handig om te voorkomen dat je per ongeluk iets overschrijft.


with open("leden.txt", "w", encoding="utf-8") as bestand:
    bestand.write("Anke Peeters\n")
    bestand.write("Bram Coppens\n")
    bestand.write("Cato Dhondt\n")

print("geschreven")

# Verwachte uitvoer:
# geschreven
