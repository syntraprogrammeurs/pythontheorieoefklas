# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.6 Waar staat dat bestand eigenlijk?
#
# De betrouwbare oplossing is een pad ten opzichte van je programmabestand:

from pathlib import Path

HIER = Path(__file__).resolve().parent
LEDENBESTAND = HIER / "gegevens" / "leden.txt"

