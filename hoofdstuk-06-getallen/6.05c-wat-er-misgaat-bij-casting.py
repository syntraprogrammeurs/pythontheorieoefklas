# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# 6.5 Casting: van het ene type naar het andere — Wat er misgaat bij casting
#
# Onthoud vooral die met de komma. Belgische gebruikers typen 2,5 en niet 2.5, en dan
# crasht je programma. In hoofdstuk 15 leer je dat afvangen; voor nu kun je het al
# oplossen:

tekst = "2,5"
getal = float(tekst.replace(",", "."))
print(getal)      # 2.5
