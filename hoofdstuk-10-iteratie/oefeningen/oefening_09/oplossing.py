# Python basis — oefeningen
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Oplossing 9 — Verkoopcijfers analyseren

verkopen = [125, 210, 95, 340, 180, 275]

totaal = 0
aantal_vanaf_200 = 0
hoogste = verkopen[0]

for verkoop in verkopen:
    totaal += verkoop

    if verkoop >= 200:
        aantal_vanaf_200 += 1

    if verkoop > hoogste:
        hoogste = verkoop

print(f"Totaal: {totaal}")
print(f"Minstens 200: {aantal_vanaf_200}")
print(f"Hoogste verkoop: {hoogste}")
