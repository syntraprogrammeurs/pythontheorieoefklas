# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.5 Klasseattributen
#
# Zet nooit een lijst of dictionary als klasseattribuut wanneer je die per object
# wilt. Alle objecten delen hem dan, en je krijgt precies het probleem uit oefening
# 14.2:

class Lid:
    gelezen = []

    def __init__(self, naam):
        self.naam = naam


anke = Lid("Anke")
bram = Lid("Bram")
anke.gelezen.append("Het diner")

print(anke.gelezen)
print(bram.gelezen)


# Verwachte uitvoer:
# ['Het diner']
# ['Het diner']
