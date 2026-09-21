# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Klassikale oefening 9.2 — Het schrikkeljaar, uitwerking
#
# De korte versie, met één toevoeging: commentaar dat de regel uitschrijft.

def is_schrikkeljaar(jaar):
    """Gregoriaanse regel: deelbaar door 4, behalve door 100, tenzij door 400."""
    return jaar % 4 == 0 and (jaar % 100 != 0 or jaar % 400 == 0)
