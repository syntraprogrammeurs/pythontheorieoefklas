# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.8 De invoerfunctie die nooit crasht
#
# Dit is het hoogtepunt van dit hoofdstuk, en je gebruikt hem in elke oefening vanaf
# nu.
#
# Dit programma vraagt invoer: voer het uit in de terminal en typ mee.

def vraag_getal(vraag: str, minimum: int = None, maximum: int = None) -> int:
    """Vraagt net zo lang tot de gebruiker een geldig geheel getal typt."""
    while True:
        antwoord = vraag.strip().replace(",", ".")
        try:
            getal = int(float(antwoord))
        except ValueError:
            print("  Dat is geen getal. Probeer opnieuw.")
            continue

        if minimum is not None and getal < minimum:
            print(f"  Minstens {minimum}, graag.")
            continue
        if maximum is not None and getal > maximum:
            print(f"  Hoogstens {maximum}, graag.")
            continue

        return getal

print(vraag_getal("3.3"));