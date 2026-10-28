# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# Klassikale oefening 28.2 — De beslissingstabel van de uitleenregel, opgave
#
# De situatie. Deze functie staat in de code van De Leeslamp.

# De regel van het bestuur: lenen mag als het lidgeld betaald is, het lid niet
# geschorst is, EN het lid niet meer dan drie boeken thuis heeft.
# Drie voorwaarden, elk waar of onwaar: dat geeft 2 x 2 x 2 = 8 combinaties.
# Die acht rijen vormen samen de BESLISSINGSTABEL (28.5), dezelfde als de
# waarheidstabel uit hoofdstuk 23.
#
# Deze functie is MET OPZET ONVOLLEDIG. Zoek zelf de fout met de tabel.
def mag_lenen(betaald, geschorst, boeken_thuis):
    """Bevat een ontbrekend geval."""
    # Niet betaald? Dan nooit lenen.
    if not betaald:
        return False
    # Geschorst? Dan ook niet.
    if geschorst:
        return False
    # LET OP: de parameter boeken_thuis komt nergens in de functie voor.
    # Python klaagt daar niet over: een ongebruikte parameter is geen fout.
    # Gevolg: wie betaald heeft en niet geschorst is, mag hier ALTIJD lenen,
    # ook met vijf boeken thuis. Dat is rij 3 van de tabel.
    return True
