# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.3 De juiste fout opvangen
#
# Schrijf nooit een kale except::

try:
    getal = int("abc")
except:
    print("er ging iets mis")


# Verwachte uitvoer:
# er ging iets mis
