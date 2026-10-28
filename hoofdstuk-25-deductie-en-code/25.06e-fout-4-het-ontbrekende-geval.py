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

# LET OP: dit is een FRAGMENT van één regel. Het hoort als LAATSTE regel in een
# functie zoals tarief_fout() uit 25.06d, onder de laatste if. Daar bestaat de
# parameter leeftijd. In dit losse bestand bestaat leeftijd niet: start je het,
# dan stopt Python met NameError: name 'leeftijd' is not defined. Python moet
# namelijk eerst de f-string invullen, nog voor er iets opgegooid wordt.
#
# Wat de regel doet, op de juiste plek:
#   raise ValueError(...) gooit zelf een fout op (15.5). Het programma stopt
#   meteen, met een melding die zegt welke waarde onverwacht was.
# Waarom raise en geen return?
#   - Met een return 0 of return None zou je stilzwijgend iets verzinnen.
#   - Met raise hoor je het METEEN als je zekerheid ("hier kan niets meer
#     overblijven") niet klopte. Falen bij de bron (25.2).
# Logisch drukt deze regel uit: "dit geval hoort niet te bestaan". Komt het toch,
# dan was een van je premissen onwaar, en dat wil je weten.
raise ValueError(f"onverwachte leeftijd: {leeftijd}")
