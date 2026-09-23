# Python basis — oefeningen
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Oplossing 3 — Temperatuuradvies

temperatuur = float(input("Temperatuur: "))

if temperatuur < 0:
    print("Het vriest.")
elif temperatuur < 15:
    print("Neem een jas mee.")
elif temperatuur < 25:
    print("Aangenaam weer.")
else:
    print("Het is warm.")
