# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# Klassikale oefening 7.2 — Een onleesbare voorwaarde ontwarren, uitwerking
#
# Er staat nog één ontkenning. Pas De Morgan opnieuw toe op not (leeftijd < 12 and not
# begeleid), wat leeftijd >= 12 or begeleid wordt:
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

if is_lid and (leeftijd >= 12 or begeleid) and aantal < 5 and not heeft_boete:
    print("Mag lenen")
