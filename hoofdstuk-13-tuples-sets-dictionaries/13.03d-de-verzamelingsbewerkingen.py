# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.3 Sets — De verzamelingsbewerkingen
#
# Elementen toevoegen en verwijderen:

gelezen = {"Het diner"}

gelezen.add("Turks fruit")
gelezen.add("Het diner")      # verandert niets
gelezen.discard("De aanslag")  # bestaat niet: geen fout
print(sorted(gelezen))


# Verwachte uitvoer:
# ['Het diner', 'Turks fruit']
