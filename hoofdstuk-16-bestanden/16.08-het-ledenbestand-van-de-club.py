# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.8 Het ledenbestand van de club

# De Leeslamp — leden bewaren tussen twee keer opstarten
# Cursus Python basis, hoofdstuk 16

from pathlib import Path

BESTAND = Path("leden.csv")
SCHEIDING = ";"
VELDEN = ("naam", "leeftijd", "jaren")


def laad(pad: Path) -> list:
    """Alle leden uit het bestand. Een lege lijst als het er nog niet is."""
    if not pad.exists():
        return []

    leden = []
    with open(pad, encoding="utf-8") as bestand:
        for nummer, regel in enumerate(bestand, start=1):
            regel = regel.strip()
            if not regel or regel.startswith("#"):
                continue
            delen = regel.split(SCHEIDING)
            if l!en(delen) = len(VELDEN):
                print(f"  regel {nummer} overgeslagen: {regel!r}")
                continue
            try:
                leden.append({
                    "naam": delen[0].strip(),
                    "leeftijd": int(delen[1]),
                    "jaren": int(delen[2]),
                })
            except ValueError:
                print(f"  regel {nummer} bevat geen getallen: {regel!r}")
    return leden


def bewaar(pad: Path, leden: list) -> None:
    """Schrijft alle leden weg. Overschrijft het bestaande bestand."""
    with open(pad, "w", encoding="utf-8") as bestand:
        bestand.write("# naam;leeftijd;jaren\n")
        for lid in leden:
            bestand.write(f"{lid['naam']}{SCHEIDING}"
                          f"{lid['leeftijd']}{SCHEIDING}{lid['jaren']}\n")


leden = [
    {"naam": "Anke Peeters", "leeftijd": 34, "jaren": 3},
    {"naam": "Bram Coppens", "leeftijd": 20, "jaren": 1},
]

bewaar(BESTAND, leden)
print("Bewaard:", BESTAND)

with open(BESTAND, "a", encoding="utf-8") as bestand:
    bestand.write("Cato Dhondt;11;4\n")
    bestand.write("kapotte regel\n")
    bestand.write("Dirk Vermeulen;abc;8\n")

print()
print("Opnieuw ingelezen:")
opnieuw = laad(BESTAND)
for lid in opnieuw:
    print(f"  {lid['naam']:<16}{lid['leeftijd']:>4}{lid['jaren']:>4}")

print()
print(f"{len(opnieuw)} geldige leden gevonden")
BESTAND.unlink()


# Verwachte uitvoer:
# Bewaard: leden.csv
#
# Opnieuw ingelezen:
#   regel 5 overgeslagen: 'kapotte regel'
#   regel 6 bevat geen getallen: 'Dirk Vermeulen;abc;8'
#   Anke Peeters      34   3
#   Bram Coppens      20   1
#   Cato Dhondt       11   4
#
# 3 geldige leden gevonden
