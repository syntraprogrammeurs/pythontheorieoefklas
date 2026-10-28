# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.5 Tautologie, contradictie en contingentie
#
# Een tautologie in een if is een if die altijd uitvoert. Een contradictie is een tak
# die nooit bereikt wordt: dode code.
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

if leeftijd < 18 or leeftijd >= 18:      # tautologie
    ...

if leeftijd < 12 and leeftijd > 65:      # contradictie
    ...
