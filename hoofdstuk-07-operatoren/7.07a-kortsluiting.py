# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.7 Kortsluiting

def zeg_en_geef(waarde):
    print(f"  ik werd beoordeeld: {waarde}")
    return waarde

print("Eerst met and:")
resultaat = zeg_en_geef(False) and zeg_en_geef(True)

print("Nu met or:")
resultaat = zeg_en_geef(True) or zeg_en_geef(False)


# Verwachte uitvoer:
# Eerst met and:
#   ik werd beoordeeld: False
# Nu met or:
#   ik werd beoordeeld: True
