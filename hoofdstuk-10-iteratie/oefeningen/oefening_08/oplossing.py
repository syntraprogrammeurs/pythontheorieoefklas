# Python basis — oefeningen
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Oplossing 8 — Artikel zoeken

artikels = ["A104", "B205", "C310", "D440"]

zoekcode = input("Artikelcode: ").strip().upper()

for artikel in artikels:
    if artikel == zoekcode:
        print("Artikel gevonden.")
        break
else:
    print("Artikel niet gevonden.")
