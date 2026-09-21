# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# Klassikale oefening 7.1 — De waarheidstabel van de club, uitwerking
#
# "Noch het een, noch het ander" is NOR: waar alleen wanneer beide onwaar zijn.

for drie_jaar in (False, True):
    for veel_gelezen in (False, True):
        nor_1 = not (drie_jaar or veel_gelezen)
        nor_2 = (not drie_jaar) and (not veel_gelezen)
        print(f"{drie_jaar!s:<8}{veel_gelezen!s:<8}{nor_1!s:<8}{nor_2!s:<8}")


# Verwachte uitvoer:
# False   False   True    True
# False   True    False   False
# True    False   False   False
# True    True    False   False
