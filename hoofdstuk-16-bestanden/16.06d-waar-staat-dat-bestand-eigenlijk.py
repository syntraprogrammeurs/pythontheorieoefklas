# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.6 Waar staat dat bestand eigenlijk?
#
# pathlib kan ook rechtstreeks lezen en schrijven:

from pathlib import Path

pad = Path("kort.txt")
pad.write_text("Anke\nBram\n", encoding="utf-8")
print(pad.read_text(encoding="utf-8"))
pad.unlink()


# Verwachte uitvoer:
# Anke
# Bram
