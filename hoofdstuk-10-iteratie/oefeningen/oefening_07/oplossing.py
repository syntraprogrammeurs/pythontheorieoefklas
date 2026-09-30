# Python basis — oefeningen
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Oplossing 7 — Ongeldige metingen overslaan

temperaturen = [18, -99, 21, 24, -99, 19]

for temperatuur in temperaturen:
    if temperatuur == -99:
        continue

    print(temperatuur)
