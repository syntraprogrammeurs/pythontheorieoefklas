# Python basis — oefeningen
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Oplossing 8 — Eenheid kiezen

eenheid = input("Eenheid: ").strip().lower()

match eenheid:
    case "km":
        print("kilometer")
    case "m":
        print("meter")
    case "cm":
        print("centimeter")
    case _:
        print("Onbekende eenheid")
