# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# 6.5 Casting: van het ene type naar het andere — Wat er misgaat bij casting
#
# Let op: deze code draait met opzet niet: overzicht van wat er misgaat bij casting;
# elke regel faalt op zich.

int("abc")        # ValueError: invalid literal for int() with base 10: 'abc'
int("")           # ValueError
int("24 ")        # 24 — spaties eromheen mag wel
int("2,5")        # ValueError — de komma is geen decimaalteken
float("2,5")      # ValueError — hetzelfde
int(None)         # TypeError
