# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.7 Gegevens met meer dan één veld: CSV
#
# Eén naam per regel volstaat niet lang. Zodra je meer velden hebt, moet je ze
# scheiden.

regels = [
    "naam;leeftijd;jaren",
    "Anke Peeters;34;3",
    "Bram Coppens;20;1",
    "Cato Dhondt;11;4",
]

with open("leden.csv", "w", encoding="utf-8") as bestand:
    for regel in regels:
        bestand.write(regel + "\n")

# strip() haalt de onzichtbare enter (\n) aan het einde weg.
# split(";") knipt de tekst in stukken op elke puntkomma.
leden = []
with open("leden.csv", encoding="utf-8") as bestand:
    kop = bestand.readline().strip().split(";")
    for regel in bestand:
        waarden = regel.strip().split(";")
        if len(waarden) != len(kop):
            continue
        leden.append(dict(zip(kop, waarden)))

for lid in leden:
    print(f"{lid['naam']:<16}{lid['leeftijd']:>4}{lid['jaren']:>4}")

# 1. zip(kop, waarden): Dit plakt de twee lijstjes aan elkaar als een ritssluiting:
# 	• 'naam' wordt gekoppeld aan 'Anke Peeters'
# 	• 'leeftijd' wordt gekoppeld aan '34'
# 	• 'jaren' wordt gekoppeld aan '3'
# 2. dict(...): Dit maakt er een dictionary (een soort paspoortje) van: 
# {'naam': 'Anke Peeters', 'leeftijd': '34', 'jaren': '3'}.
# 3. .append(...): Dit handige paspoortje wordt in de grote lijst leden gestopt. 
# Aan het einde van de rit zitten alle drie de personen als een eigen dictionary in de lijst.


# Verwachte uitvoer:
# Anke Peeters      34   3
# Bram Coppens      20   1
# Cato Dhondt       11   4
