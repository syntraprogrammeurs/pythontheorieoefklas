# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# 25.6 De vier logicafouten in if-ketens — Fout 4 — het ontbrekende geval
#
# De gewoonte die dit voorkomt: elke keten eindigt met een tak die alles opvangt. Weet
# je zeker dat er niets overblijft, sluit dan af met een raise in plaats van een
# return.
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

raise ValueError(f"onverwachte leeftijd: {leeftijd}")
