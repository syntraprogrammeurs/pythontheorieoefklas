# Python basis — oefeningen
# Hoofdstuk 9 — Selectie: if, elif, else en match
# Oplossing 5 — Bestandsnaam controleren

bestand = input("Bestand: ").strip()

if not bestand:
    print("Geen bestandsnaam opgegeven.")
elif bestand.lower().endswith(".py"):
    print("Geldig Python-bestand.")
else:
    print("Geen Python-bestand.")
