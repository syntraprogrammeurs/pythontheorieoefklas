# Python basis — oefeningen
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Oplossing 2 — Wachten op het juiste wachtwoord

wachtwoord = input("Wachtwoord: ")

while wachtwoord != "python123":
    print("Fout, probeer opnieuw.")
    wachtwoord = input("Wachtwoord: ")

print("Toegang verleend.")
