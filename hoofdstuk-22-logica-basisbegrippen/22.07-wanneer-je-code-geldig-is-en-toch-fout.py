# Python basis — theoriebundel
# Hoofdstuk 22 — Logica en kritisch denken: de basisbegrippen
# 22.7 Wanneer je code geldig is en toch fout
#
# Het onderscheid uit 22.5 is geen woordenspel. Hier is het in Python.

# Even de begrippen uit 22.5 op een rij, want dit bestand gaat precies daarover:
#   GELDIG     -> de VORM klopt: als de premissen waar zijn, moet de conclusie
#                 waar zijn
#   DEUGDELIJK -> geldig EN alle premissen zijn waar
# In code: de berekening (de vorm) kan perfect zijn, terwijl de aanname waarop
# ze steunt (de premisse) niet klopt. Dan is het programma geldig maar fout.

# De Leeslamp — de redenering klopt, de premisse niet
# Dit is de PREMISSE van het hele programma: een constante (hoofdstuk 5) met de
# drempel voor korting. Python kan niet weten of 3 juist is. Besliste de
# vereniging dat de korting pas vanaf 4 boeken geldt, dan is alles hieronder
# fout, hoe correct de code ook is.
KORTING_VANAF = 3          # aanname: korting vanaf 3 boeken per maand


# De VORM: een if die de regel "vanaf de drempel 1 euro korting" uitvoert.
# >= betekent "groter dan of gelijk aan": 3 boeken krijgt dus al korting.
def prijs(boeken):
    """De maandprijs: 2 euro per boek, met korting vanaf de drempel."""
    if boeken >= KORTING_VANAF:
        # 2 euro per boek, min 1 euro korting.
        return boeken * 2 - 1
    # Onder de drempel: gewoon 2 euro per boek.
    return boeken * 2


# Een for-lus over een tuple met vier aantallen (hoofdstuk 10 en 13). Voor elk
# aantal toont de f-string (hoofdstuk 6) de prijs die de functie teruggeeft.
# Kijk naar de uitvoer bij 3 boeken: 5 euro. Dat volgt onberispelijk uit de code.
# Of het ook JUIST is, hangt alleen af van KORTING_VANAF, en dat kan geen enkele
# test of linter voor jou beslissen.
# LET OP: een test die je zelf schrijft met dezelfde aanname (prijs(3) == 5),
# slaagt gewoon. Ze controleert de vorm, niet de premisse. Zo'n fout vind je
# alleen door de aanname uit te spreken en na te vragen bij de opdrachtgever.
for aantal in (1, 2, 3, 4):
    print(f"{aantal} boeken: {prijs(aantal)} euro")


# Verwachte uitvoer:
# 1 boeken: 2 euro
# 2 boeken: 4 euro
# 3 boeken: 5 euro
# 4 boeken: 7 euro
