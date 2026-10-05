# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.4 Dictionaries
#
# Dit is het belangrijkste type van dit hoofdstuk.

# Wat het is: Een verzameling van sleutel-waardeparen (keys gekoppeld aan values).
# Kenmerk: Elke sleutel (key) moet uniek zijn, maar de waarde (value) mag je vaker gebruiken. Je zoekt data op via de sleutel in plaats van een nummerindex.
# Wanneer gebruiken: Als je eigenschappen aan een label wilt koppelen (zoals een telefoonboek of gebruikersprofiel).
# Voorbeeld: student = {"naam": "Sara", "leeftijd": 21}

lid = {
    "naam": "Anke Peeters",
    "leeftijd": 34,
    "stad": "Gent",
    "is_student": False,
}

print(lid["naam"])
print(lid["leeftijd"])
print(len(lid))


# Verwachte uitvoer:
# Anke Peeters
# 34
# 4
