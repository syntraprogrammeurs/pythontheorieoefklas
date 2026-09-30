# Python basis — oefeningen
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Oplossing 6 — Product en prijs

producten = ["Brood", "Melk", "Koffie"]
prijzen = [2.40, 1.35, 6.80]

for product, prijs in zip(producten, prijzen):
    print(f"{product}: €{prijs:.2f}")
