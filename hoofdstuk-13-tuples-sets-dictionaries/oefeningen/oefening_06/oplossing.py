# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 6 — Twee leesavonden vergelijken

maandag = {"Anke", "Bram", "Cato", "Dirk"}
donderdag = {"Cato", "Dirk", "Emma", "Fien"}

print(f"Beide avonden: {sorted(maandag & donderdag)}")
print(f"Alle leden: {sorted(maandag | donderdag)}")
print(f"Alleen maandag: {sorted(maandag - donderdag)}")
print(f"Maar één avond: {sorted(maandag ^ donderdag)}")
