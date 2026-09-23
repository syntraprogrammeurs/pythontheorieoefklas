# Python basis — oefeningen
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Oplossing 4 — Pakket aanvaarden

gewicht = float(input("Gewicht in kg: "))
lengte = float(input("Lengte in cm: "))

if gewicht <= 20 and lengte <= 60:
    print("Pakket aanvaard.")
else:
    print("Pakket te groot of te zwaar.")
