# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# Klassikale oefening 7.2 — Een onleesbare voorwaarde ontwarren, uitwerking
#
# 3 — Met namen.

is_lid = True
leeftijd = 34
begeleid = False
aantal = 3
heeft_boete = False

oud_genoeg = leeftijd >= 12 or begeleid
onder_de_limiet = aantal < 5
in_orde = not heeft_boete

mag_lenen = is_lid and oud_genoeg and onder_de_limiet and in_orde

if mag_lenen:
    print("Mag lenen")


# Verwachte uitvoer:
# Mag lenen
