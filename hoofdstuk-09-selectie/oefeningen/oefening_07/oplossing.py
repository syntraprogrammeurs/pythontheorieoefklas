# Python basis — oefeningen
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Oplossing 7 — Status in één regel

vrije_plaatsen = int(input("Vrije plaatsen: "))

status = "beschikbaar" if vrije_plaatsen > 0 else "volzet"

print(f"Status: {status}")
