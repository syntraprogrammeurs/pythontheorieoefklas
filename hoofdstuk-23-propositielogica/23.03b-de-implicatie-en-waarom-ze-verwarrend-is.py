# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.3 De implicatie, en waarom ze verwarrend is

# Dit programma toont waarom een controle over een LEGE lijst je nooit betrapt.
# "Elk lid heeft betaald" betekent eigenlijk: "als iemand lid is, dan heeft hij
# betaald", een implicatie. Zijn er geen leden, dan is er niemand die de regel
# schendt, en dus is de bewering waar: leeg waar, zoals in 23.03a.

# Een lege lijst. In een echt programma zou hier een lijst met dictionaries
# staan, zoals {"naam": "Anke", "betaald": True} (hoofdstuk 13).
leden = []
# all(reeks) uit hoofdstuk 12 geeft True als ELK element waar is, en False zodra
# er één onwaar is. Tussen de haakjes staat een generator (hoofdstuk 14): voor
# elk lid de waarde lid["betaald"].
# LET OP: de lijst is leeg, dus de generator levert niets op. all() vindt dan
# geen enkel element dat onwaar is en geeft True terug. lid["betaald"] wordt
# zelfs nooit opgevraagd, dus er komt ook geen KeyError.
print("Alle leden hebben betaald:", all(lid["betaald"] for lid in leden))
# Daarom de tweede regel: len() toont dat er niets gecontroleerd werd. Een test
# die zo slaagt, heeft niets bewezen. Controleer dus eerst of er iets in zit.
print("Aantal gecontroleerde leden:", len(leden))


# Verwachte uitvoer:
# Alle leden hebben betaald: True
# Aantal gecontroleerde leden: 0
