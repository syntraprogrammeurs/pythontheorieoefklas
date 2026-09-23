# Python basis — oefeningen
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Oplossing 6 — Leveringskost

bedrag = float(input("Aankoopbedrag: "))
premium = input("Premiumklant (ja/nee): ").strip().lower()

if bedrag >= 100:
    leveringskost = 0
else:
    if premium == "ja":
        leveringskost = 2.50
    else:
        leveringskost = 5.00

print(f"Leveringskost: €{leveringskost:.2f}")
