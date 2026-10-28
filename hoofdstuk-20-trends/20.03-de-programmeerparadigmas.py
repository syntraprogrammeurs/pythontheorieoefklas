# Python basis — theoriebundel
# Hoofdstuk 20 — Trends in programmeren
# 20.3 De programmeerparadigma's
#
# Python is bewust multiparadigma: je kunt alle vier de stijlen gebruiken, en je mengt
# ze in de praktijk.

# Een PARADIGMA is een manier van denken over programmeren: welke bouwstenen je
# gebruikt en hoe je een probleem opdeelt. Dit bestand lost DRIE keer hetzelfde
# kleine probleem op: zet de eerste letter van elke naam in een hoofdletter.
# Kijk niet naar wat er gebeurt (dat is telkens hetzelfde), maar naar HOE.

# De invoer: een gewone lijst met drie strings (hoofdstuk 12).
namen = ["anke", "bram", "cato"]

# procedureel
# PROCEDUREEL: je beschrijft de STAPPEN, één voor één. Dit is het
# opbouwpatroon uit hoofdstuk 10:
#   1. begin met een lege lijst
#   2. loop over elke naam
#   3. voeg de aangepaste naam achteraan toe met append()
# capitalize() is een stringmethode (hoofdstuk 8): ze geeft een NIEUWE string
# terug met de eerste letter als hoofdletter en de rest in kleine letters.
uit = []
for naam in namen:
    uit.append(naam.capitalize())
print(uit)

# functioneel
# FUNCTIONEEL: je zegt welke FUNCTIE op elk element moet worden toegepast.
# map(functie, reeks) past de functie toe op elk element van de reeks.
#   - str.capitalize is de methode zelf, ZONDER haakjes: je geeft de functie
#     door, je roept ze niet zelf op (net als command= in hoofdstuk 19).
#     map roept ze straks op als str.capitalize("anke"), dus met de naam als
#     argument; dat is hetzelfde als "anke".capitalize().
#   - LET OP: map geeft geen lijst terug, maar een map-object dat de waarden
#     pas één voor één uitrekent als je erom vraagt. print(map(...)) toont dus
#     iets als <map object at 0x...>. Daarom zet list() er een lijst van.
print(list(map(str.capitalize, namen)))

# de Python-manier, die ertussenin zit
# De LIST COMPREHENSION uit hoofdstuk 14. Lees ze als: "een lijst van
# naam.capitalize(), voor elke naam in namen". Ze zegt, net als map, WAT je wilt,
# maar ze leest als gewone Python, zonder dat je een functie moet doorgeven.
# Dit is de vorm die je in Python het vaakst ziet.
print([naam.capitalize() for naam in namen])


# Verwachte uitvoer:
# ['Anke', 'Bram', 'Cato']
# ['Anke', 'Bram', 'Cato']
# ['Anke', 'Bram', 'Cato']
