# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.5 Een bestand dat er niet is
#
# Dat patroon gebruik je bij het opstarten van een programma: bestaat het
# gegevensbestand al, lees het; zo niet, begin met een lege lijst.

def laad_leden(pad: str) -> list:
    """De leden uit het bestand, of een lege lijst als het er nog niet is."""
    try:
        with open(pad, encoding="utf-8") as bestand:
            return [regel.strip() for regel in bestand if regel.strip()]
    except FileNotFoundError:
        return []


print(laad_leden("bestaat-niet.txt"))


# Verwachte uitvoer:
# []
