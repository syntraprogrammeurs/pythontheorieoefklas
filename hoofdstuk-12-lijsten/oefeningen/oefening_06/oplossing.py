# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oplossing 6 — sort() of sorted()?

scores = [7, 3, 9, 1, 5]

gesorteerd = sorted(scores)
print(f"Origineel: {scores}")
print(f"Gesorteerd: {gesorteerd}")

scores.sort(reverse=True)
print(f"Aflopend: {scores}")

resultaat = scores.sort()
print(f"Resultaat van sort(): {resultaat}")

# sorted() laat de lijst ongemoeid en geeft een nieuwe lijst terug.
# sort() verandert de lijst zelf en geeft None terug.
