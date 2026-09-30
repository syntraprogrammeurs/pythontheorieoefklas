# Python basis — oefeningen
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Oplossing 8 — Statistiek van de bladzijden

bladzijden = [288, 175, 928, 592, 246]

print(f"Totaal: {sum(bladzijden)}")
print(f"Kleinste: {min(bladzijden)}")
print(f"Grootste: {max(bladzijden)}")
print(f"Gemiddelde: {sum(bladzijden) / len(bladzijden)}")
print(f"Een boek boven 900 blz.: {any(b > 900 for b in bladzijden)}")
print(f"Alle boeken boven 200 blz.: {all(b > 200 for b in bladzijden)}")
