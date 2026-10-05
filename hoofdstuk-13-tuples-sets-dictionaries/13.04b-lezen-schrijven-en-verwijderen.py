# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.4 Dictionaries — Lezen, schrijven en verwijderen

lid = {"naam": "Anke", "leeftijd": 34}

lid["stad"] = "Gent"         # erbij
lid["leeftijd"] = 35         # overschrijven
print(lid)

del lid["stad"]
print(lid)

verwijderd = lid.pop("leeftijd")
print(verwijderd, lid)


# Verwachte uitvoer:
# {'naam': 'Anke', 'leeftijd': 35, 'stad': 'Gent'}
# {'naam': 'Anke', 'leeftijd': 35}
# 35 {'naam': 'Anke'}
