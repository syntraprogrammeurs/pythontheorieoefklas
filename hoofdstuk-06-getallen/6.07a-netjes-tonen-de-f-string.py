# Python basis — theoriebundel
# Hoofdstuk 6 — Getallen, casting, invoer en uitvoer
# 6.7 Netjes tonen: de f-string
#
# Er zijn vier manieren om tekst en waarden te combineren. Je leert ze alle vier
# herkennen, en je gebruikt er één.

naam = "Anke"
bedrag = 25.5

# 1 — met komma's
print("Dag", naam, "je betaalt", bedrag, "euro")

# 2 — met plus, en dus met str()
print("Dag " + naam + ", je betaalt " + str(bedrag) + " euro")

# 3 — met .format(), de oude manier
print("Dag {}, je betaalt {} euro".format(naam, bedrag))

# 4 — met een f-string: de manier die je gebruikt
print(f"Dag {naam}, je betaalt {bedrag} euro")
