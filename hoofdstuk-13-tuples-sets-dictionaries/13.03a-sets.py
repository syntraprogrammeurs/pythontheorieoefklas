# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.3 Sets
# Wat het is: Een ongeordende verzameling van unieke elementen.
# Kenmerk: Dubbele waarden worden automatisch verwijderd. Je kunt elementen toevoegen of verwijderen, maar niet opzoeken via een volgnummer of index.
# Wanneer gebruiken: Als je dubbele waardes wilt filteren of snelle wiskundige operaties wilt doen (zoals doorsnedes en unies berekenen).
# Voorbeeld: unieke_nummers = {1, 2, 3, 3} wordt {1, 2, 3}

gelezen = {"Het diner", "Turks fruit", "Het diner", "De aanslag"}
print(len(gelezen))
print(sorted(gelezen))


# Verwachte uitvoer:
# 3
# ['De aanslag', 'Het diner', 'Turks fruit']
