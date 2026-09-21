# Python basis — theoriebundel
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Klassikale oefening 9.1 — De uitleentermijn, nu in code, uitwerking
#
# De schoonheidsfout in de uitvoer. Er staat "1 weken". Dat is taalkundig fout. Los
# het op met een verkorte keuze:

weken = 1
eenheid = "week" if weken == 1 else "weken"
print(f"{weken} {eenheid}")


# Verwachte uitvoer:
# 1 week
