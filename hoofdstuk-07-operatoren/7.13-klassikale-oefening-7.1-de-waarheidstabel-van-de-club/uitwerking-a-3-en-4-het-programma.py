# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# Klassikale oefening 7.1 — De waarheidstabel van de club, uitwerking
#
# 3 en 4 — Het programma.

# De Leeslamp — wie krijgt een gratis extra uitlening?
# Cursus Python basis, hoofdstuk 7, oefening 1

print(f"{'3 jaar':<8}{'>10 boeken':<12}{'!=':<7}{'and/or/not':<12}{'^':<7}")
print("-" * 46)

for drie_jaar in (False, True):
    for veel_gelezen in (False, True):
        met_ongelijk = drie_jaar != veel_gelezen
        met_woorden = (drie_jaar or veel_gelezen) and not (drie_jaar and veel_gelezen)
        met_dakje = bool(drie_jaar ^ veel_gelezen)

        print(f"{drie_jaar!s:<8}{veel_gelezen!s:<12}"
              f"{met_ongelijk!s:<7}{met_woorden!s:<12}{met_dakje!s:<7}")


# Verwachte uitvoer:
# 3 jaar  >10 boeken  !=     and/or/not  ^
# ----------------------------------------------
# False   False       False  False       False
# False   True        True   True        True
# True    False       True   True        True
# True    True        False  False       False
