# Python basis — oefeningen
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Oplossing 9 — Bestelling afhalen of leveren

methode = input("Methode: ").strip().lower()

match methode:
    case "afhalen" | "ophalen":
        print("Geen verzendkosten.")
    case "standaard":
        print("Verzendkosten: €4.95")
    case "express":
        print("Verzendkosten: €9.95")
    case _:
        print("Onbekende leveringsmethode.")
