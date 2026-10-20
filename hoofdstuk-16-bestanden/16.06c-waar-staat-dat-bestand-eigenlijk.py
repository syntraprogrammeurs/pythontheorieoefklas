# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.6 Waar staat dat bestand eigenlijk?
#
# pathlib neemt je veel werk uit handen:

from pathlib import Path

pad = Path("gegevens") / "leden.txt"

print(pad)
print(pad.name)
print(pad.suffix)
print(pad.stem)
print(pad.exists())


# Verwachte uitvoer:
# gegevens\leden.txt
# leden.txt
# .txt
# leden
# False
