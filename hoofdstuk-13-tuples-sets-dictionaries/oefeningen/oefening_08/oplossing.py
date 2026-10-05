# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 8 — Een telefoonnummer opzoeken

telefoons = {"Anke": "0470 12 34 56", "Bram": "0485 98 76 54"}

for naam in ["Anke", "Cato", "Bram"]:
    print(f"{naam}: {telefoons.get(naam, 'onbekend')}")

if "Cato" not in telefoons:
    telefoons["Cato"] = "0499 11 22 33"
    print("Cato toegevoegd")

print(f"Cato: {telefoons['Cato']}")

# Vóór stap 2 geeft telefoons["Cato"] een KeyError.
