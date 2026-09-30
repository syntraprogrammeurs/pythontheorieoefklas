# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oplossing 9 — Een tweede naam of een echte kopie?

origineel = ["Anke", "Bram", "Cato"]
zelfde = origineel
kopie = origineel.copy()

zelfde.append("Dirk")
kopie.append("Emma")

print(f"Origineel: {origineel}")
print(f"Zelfde: {zelfde}")
print(f"Kopie: {kopie}")
print(f"zelfde is origineel: {zelfde is origineel}")
print(f"kopie is origineel: {kopie is origineel}")

# zelfde is geen nieuwe lijst, maar een tweede naam voor dezelfde lijst.
