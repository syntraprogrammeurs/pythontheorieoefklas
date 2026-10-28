# Python basis — theoriebundel
# Hoofdstuk 23 — Propositielogica en waarheidstabellen
# 23.5 Tautologie, contradictie en contingentie
#
# Een tautologie in een if is een if die altijd uitvoert. Een contradictie is een tak
# die nooit bereikt wordt: dode code.
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

# LET OP: start je dit bestand toch, dan loopt het meteen vast met een
# NameError: name 'leeftijd' is not defined. De variabele leeftijd wordt nergens
# gemaakt. Dat is de bedoeling: je LEEST dit fragment, je voert het niet uit.
# De drie puntjes ... (Ellipsis) zijn een geldige opdracht die niets doet: een
# plaatshouder voor "hier staat de echte code".

# Een TAUTOLOGIE: altijd waar, welke waarde leeftijd ook heeft. Elk getal is
# kleiner dan 18 of minstens 18. De if is dus overbodig: zijn blok voert altijd uit.
if leeftijd < 18 or leeftijd >= 18:      # tautologie
    ...

# Een CONTRADICTIE: nooit waar. Niemand is tegelijk jonger dan 12 en ouder dan 65.
# Het blok eronder wordt dus nooit uitgevoerd: DODE CODE. Waarschijnlijk bedoelde
# de schrijver or ("jonger dan 12 of ouder dan 65") en schreef hij per ongeluk and.
# Een uitdrukking die soms waar en soms onwaar is, heet een CONTINGENTIE: dat is
# wat een gewone, zinvolle if hoort te zijn.
if leeftijd < 12 and leeftijd > 65:      # contradictie
    ...
