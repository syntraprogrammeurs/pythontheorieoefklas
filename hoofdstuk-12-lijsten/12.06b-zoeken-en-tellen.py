# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# 12.6 Zoeken en tellen
#
# .index() geeft een ValueError wanneer de waarde er niet in staat. Gebruik altijd
# eerst in:

leden = ["Anke", "Bram"]
gezocht = "Dirk"

if gezocht in leden:
    print(f"{gezocht} staat op positie {leden.index(gezocht)}")
else:
    print(f"{gezocht} staat niet in de lijst")


# Verwachte uitvoer:
# Dirk staat niet in de lijst
