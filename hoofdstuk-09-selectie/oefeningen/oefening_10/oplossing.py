# Python basis — oefeningen
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Oplossing 10 — Bioscoopticket

tickettype = input("Tickettype: ").strip().lower()
avond = input("Avondvoorstelling (ja/nee): ").strip().lower()

match tickettype:
    case "standaard":
        prijs = 12
    case "student":
        prijs = 9
    case "senior":
        prijs = 8
    case _:
        prijs = None

if prijs is None:
    print("Onbekend tickettype.")
else:
    if avond == "ja":
        prijs += 2

    print(f"Te betalen: €{prijs:.2f}")
