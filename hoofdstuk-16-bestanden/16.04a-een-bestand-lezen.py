# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.4 Een bestand lezen
#
# Er zijn drie manieren, en je kiest op basis van de grootte.

with open("leden.txt", "w", encoding="utf-8") as bestand:
    bestand.write("Anke Peeters\nBram Coppens\nCato Dhondt\n")

# 1 - alles in één string
# De repr()-functie zorgt ervoor dat je de exacte, rauwe inhoud van een variabele 
# te zien krijgt, inclusief onzichtbare tekens zoals enters (\n) of tabs (\t).
with open("leden.txt", encoding="utf-8") as bestand:
    alles = bestand.read()
print(repr(alles))

# 2 - alle regels in een lijst (array)
with open("leden.txt", encoding="utf-8") as bestand:
    regels = bestand.readlines()
print(regels)

# 3 - regel per regel
with open("leden.txt", encoding="utf-8") as bestand:
    for regel in bestand:
        print(repr(regel))


# Verwachte uitvoer:
# 'Anke Peeters\nBram Coppens\nCato Dhondt\n'
# ['Anke Peeters\n', 'Bram Coppens\n', 'Cato Dhondt\n']
# 'Anke Peeters\n'
# 'Bram Coppens\n'
# 'Cato Dhondt\n'
