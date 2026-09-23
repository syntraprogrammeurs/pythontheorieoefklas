# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# 7.12 De uitleenbeslissing
#
# Zet dit in main.py:

# De Leeslamp — mag dit lid lenen?
# Cursus Python basis, hoofdstuk 7

MINIMUM_LEEFTIJD = 12
MAX_UITGELEEND = 5

leeftijd = 34
is_lid = True
heeft_boete = False
aantal_uitgeleend = 3
soort_boek = "gewoon"

oud_genoeg = leeftijd >= MINIMUM_LEEFTIJD
onder_de_limiet = aantal_uitgeleend < MAX_UITGELEEND
uitleenbaar = soort_boek != "naslagwerk"

mag_lenen = is_lid and oud_genoeg and onder_de_limiet and uitleenbaar and not heeft_boete

print(f"Oud genoeg       : {oud_genoeg}")
print(f"Onder de limiet  : {onder_de_limiet}")
print(f"Uitleenbaar boek : {uitleenbaar}")
print(f"Geen boete       : {not heeft_boete}")
print(f"Mag lenen        : {mag_lenen}")


# Verwachte uitvoer:
# Oud genoeg       : True
# Onder de limiet  : True
# Uitleenbaar boek : True
# Geen boete       : True
# Mag lenen        : True
