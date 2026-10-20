# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.4 Een bestand lezen

with open("leden.txt", "w", encoding="utf-8") as bestand:
    bestand.write("Anke Peeters\nBram Coppens\n\nCato Dhondt\n")

# if regel.strip(): Python controleert of de regel wel échte tekst bevat. .strip() haalt alle 
# onzichtbare spaties en enters (\n). Aan het begin en einde van iedere regel kan
# alleen wanneer een item geïsoleerd wordt. 
# "Anke Peeters" bevat tekst, dus deze regel mag door naar de volgende stap.
# regel.strip() (helemaal vooraan): De schoongemaakte naam zonder de \n (dus puur "Anke Peeters") 
# wordt in de nieuwe lijst leden gezet.

with open("leden.txt", encoding="utf-8") as bestand:
    leden = [regel.strip() for regel in bestand if regel.strip()]

print(leden)
print(len(leden), "leden")


# Verwachte uitvoer:
# ['Anke Peeters', 'Bram Coppens', 'Cato Dhondt']
# 3 leden
