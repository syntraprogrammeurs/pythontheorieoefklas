# Python basis — oefeningen
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Oplossing 5 — Genummerde takenlijst

taken = ["Mail lezen", "Code schrijven", "Testen", "Committen"]

for nummer, taak in enumerate(taken, start=1):
    print(f"{nummer}. {taak}")
