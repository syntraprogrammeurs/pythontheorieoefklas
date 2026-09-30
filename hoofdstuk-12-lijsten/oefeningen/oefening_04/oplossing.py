# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oplossing 4 — De wachtlijst bijhouden

wachtlijst = ["Anke", "Bram"]

wachtlijst.append("Cato")
print(wachtlijst)

wachtlijst.insert(0, "Dirk")
print(wachtlijst)

wachtlijst.remove("Bram")
print(wachtlijst)

volgende = wachtlijst.pop(0)
print(f"{volgende} is aan de beurt.")
print(wachtlijst)
