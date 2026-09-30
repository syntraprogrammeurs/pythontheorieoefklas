# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Klassikale oefening 11.2 — Het lidgeld herschrijven, uitwerking
#
# Wat er nog beter kan. De uitvoerregel dikste=boek None met None leest slecht. In een
# echt programma vang je dat af:

nummer, aantal = None, None
tekst = "geen boeken" if nummer is None else f"boek {nummer} met {aantal}"
print(tekst)


# Verwachte uitvoer:
# geen boeken
