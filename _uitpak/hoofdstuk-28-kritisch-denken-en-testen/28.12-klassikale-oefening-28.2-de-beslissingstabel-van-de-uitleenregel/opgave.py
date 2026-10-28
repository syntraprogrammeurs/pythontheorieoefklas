# Python basis — theoriebundel
# Hoofdstuk 28 — Kritisch denken toegepast op softwaretesten
# Klassikale oefening 28.2 — De beslissingstabel van de uitleenregel, opgave
#
# De situatie. Deze functie staat in de code van De Leeslamp.

def mag_lenen(betaald, geschorst, boeken_thuis):
    """Bevat een ontbrekend geval."""
    if not betaald:
        return False
    if geschorst:
        return False
    return True
