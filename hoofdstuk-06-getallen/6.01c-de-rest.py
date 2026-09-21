# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# 6.1 Rekenen — De rest %
#
# De restoperator is veel nuttiger dan hij lijkt. Drie klassieke toepassingen:
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

# 1 — is een getal even?
if getal % 2 == 0:
    print("even")

# 2 — is een getal deelbaar door iets?
if jaar % 4 == 0:
    print("mogelijk een schrikkeljaar")

# 3 — rondlopen binnen een bereik
volgende = (huidige + 1) % 7      # dagen van de week: 0..6 en dan weer 0
