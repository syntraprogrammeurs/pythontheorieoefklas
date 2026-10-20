# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# Klassikale oefening 16.1 — Het uitleenregister, uitwerking

# De Leeslamp — het uitleenregister
# Cursus Python basis, hoofdstuk 16, oefening 1

from pathlib import Path

REGISTER = Path("uitleningen.csv")
SCHEIDING = ";"


def noteer_uitlening(pad: Path, lid: str, titel: str, datum: str) -> None:
    """Voegt één uitlening toe aan het register."""
    if SCHEIDING in lid or SCHEIDING in titel:
        raise ValueError(f"een veld mag geen {SCHEIDING!r} bevatten")
    with open(pad, "a", encoding="utf-8") as bestand:
        bestand.write(f"{datum}{SCHEIDING}{lid}{SCHEIDING}{titel}\n")


def lees_uitleningen(pad: Path) -> list:
    """Alle uitleningen. Foute regels worden gemeld en overgeslagen."""
    if not pad.exists():
        return []

    uit = []
    with open(pad, encoding="utf-8") as bestand:
        for nummer, regel in enumerate(bestand, start=1):
            regel = regel.strip()
            if not regel:
                continue
            delen = regel.split(SCHEIDING)
            if len(delen) != 3:
                print(f"  regel {nummer} overgeslagen: {regel!r}")
                continue
            uit.append({"datum": delen[0], "lid": delen[1], "titel": delen[2]})
    return uit


def per_lid(uitleningen: list) -> dict:
    """Per lid het aantal uitleningen."""
    telling = {}
    for u in uitleningen:
        telling[u["lid"]] = telling.get(u["lid"], 0) + 1
    return telling


def boeken_van(uitleningen: list, lid: str) -> list:
    """De titels die dit lid geleend heeft, in volgorde van uitlening."""
    return [u["titel"] for u in uitleningen if u["lid"].lower() == lid.lower()]


if REGISTER.exists():
    REGISTER.unlink()

noteer_uitlening(REGISTER, "Anke Peeters", "Het diner", "2026-09-01")
noteer_uitlening(REGISTER, "Bram Coppens", "Turks fruit", "2026-09-02")
noteer_uitlening(REGISTER, "Anke Peeters", "De aanslag", "2026-09-05")
noteer_uitlening(REGISTER, "Cato Dhondt", "Max Havelaar", "2026-09-05")
noteer_uitlening(REGISTER, "Anke Peeters", "De ontdekking", "2026-09-11")

with open(REGISTER, "a", encoding="utf-8") as bestand:
    bestand.write("dit is geen geldige regel\n")

try:
    noteer_uitlening(REGISTER, "Els;Janssens", "Iets", "2026-09-12")
except ValueError as fout:
    print("Geweigerd bij het schrijven:", fout)

print()
uitleningen = lees_uitleningen(REGISTER)

print()
print(f"{'Datum':<12}{'Lid':<16}Titel")
print("-" * 48)
for u in uitleningen:
    print(f"{u['datum']:<12}{u['lid']:<16}{u['titel']}")

print()
print("Aantal per lid:")
for lid, aantal in sorted(per_lid(uitleningen).items(), key=lambda p: -p[1]):
    print(f"  {lid:<16}{aantal}")

print()
print("Anke leende:", boeken_van(uitleningen, "anke peeters"))
print("Totaal      :", len(uitleningen), "uitleningen")

REGISTER.unlink()


# Verwachte uitvoer:
# Geweigerd bij het schrijven: een veld mag geen ';' bevatten
#
#   regel 6 overgeslagen: 'dit is geen geldige regel'
#
# Datum       Lid             Titel
# ------------------------------------------------
# 2026-09-01  Anke Peeters    Het diner
# 2026-09-02  Bram Coppens    Turks fruit
# 2026-09-05  Anke Peeters    De aanslag
# 2026-09-05  Cato Dhondt     Max Havelaar
# 2026-09-11  Anke Peeters    De ontdekking
#
# Aantal per lid:
#   Anke Peeters    3
#   Bram Coppens    1
#   Cato Dhondt     1
#
# Anke leende: ['Het diner', 'De aanslag', 'De ontdekking']
# Totaal      : 5 uitleningen
