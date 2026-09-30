# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# 10.7 else bij een lus
#
# Dit is een eigenaardigheid van Python die je zelden ziet maar die precies één
# probleem netjes oplost.

leden = ["Anke", "Bram", "Cato"]
gezocht = "Dirk"

for lid in leden:
    if lid == gezocht:
        print(f"{gezocht} gevonden")
        break
else:
    print(f"{gezocht} staat niet in de lijst")


# Verwachte uitvoer:
# Dirk staat niet in de lijst
