# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# Klassikale oefening 7.2 — Een onleesbare voorwaarde ontwarren, uitwerking
#
# De buitenste vorm is not (X or Y or Z). Volgens De Morgan wordt dat not X and not Y
# and not Z:
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

if is_lid and not (leeftijd < 12 and not begeleid) and aantal < 5 and not heeft_boete:
    print("Mag lenen")
