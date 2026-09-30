# Python basis — theoriebundel
# Hoofdstuk 12 — Lijsten — en waarom Python geen arrays heeft
# Klassikale oefening 12.1 — De wachtlijst, uitwerking

# De Leeslamp — leden en wachtlijst
# Cursus Python basis, hoofdstuk 12, oefening 1

MAX_LEDEN = 10


def meld_aan(leden: list, wachtlijst: list, naam: str) -> str:
    """Meldt iemand aan. Geeft terug wat er gebeurd is."""
    if naam in leden:
        return f"{naam} is al lid"
    if naam in wachtlijst:
        return f"{naam} staat al op de wachtlijst"

    if len(leden) < MAX_LEDEN:
        leden.append(naam)
        return f"{naam} is lid geworden"

    wachtlijst.append(naam)
    return f"{naam} staat op de wachtlijst, plaats {len(wachtlijst)}"


def vertrek(leden: list, wachtlijst: list, naam: str) -> str:
    """Laat iemand vertrekken en schuift de wachtlijst door."""
    if naam not in leden:
        return f"{naam} is geen lid"

    leden.remove(naam)
    if wachtlijst:
        volgende = wachtlijst.pop(0)
        leden.append(volgende)
        return f"{naam} vertrekt; {volgende} schuift door"
    return f"{naam} vertrekt; de wachtlijst is leeg"


def toon(leden: list, wachtlijst: list) -> str:
    """Beide lijsten als tekst."""
    regels = [f"Leden ({len(leden)}/{MAX_LEDEN})"]
    for nummer, naam in enumerate(leden, start=1):
        regels.append(f"  {nummer:>2}. {naam}")

    regels.append(f"Wachtlijst ({len(wachtlijst)})")
    if not wachtlijst:
        regels.append("   (leeg)")
    for nummer, naam in enumerate(wachtlijst, start=1):
        regels.append(f"  {nummer:>2}. {naam}")
    return "\n".join(regels)


leden = []
wachtlijst = []

kandidaten = [
    "Anke", "Bram", "Cato", "Dirk", "Els", "Femke", "Gert", "Hilde",
    "Ilse", "Jan", "Karel", "Lien", "Mo", "Anke",
]

for naam in kandidaten:
    print(meld_aan(leden, wachtlijst, naam))

print()
print(vertrek(leden, wachtlijst, "Cato"))
print(vertrek(leden, wachtlijst, "Anke"))
print(vertrek(leden, wachtlijst, "Zoe"))
print()
print(toon(leden, wachtlijst))


# Verwachte uitvoer:
# Anke is lid geworden
# Bram is lid geworden
# Cato is lid geworden
# Dirk is lid geworden
# Els is lid geworden
# Femke is lid geworden
# Gert is lid geworden
# Hilde is lid geworden
# Ilse is lid geworden
# Jan is lid geworden
# Karel staat op de wachtlijst, plaats 1
# Lien staat op de wachtlijst, plaats 2
# Mo staat op de wachtlijst, plaats 3
# Anke is al lid
#
# Cato vertrekt; Karel schuift door
# Anke vertrekt; Lien schuift door
# Zoe is geen lid
#
# Leden (10/10)
#    1. Bram
#    2. Dirk
#    3. Els
#    4. Femke
#    5. Gert
#    6. Hilde
#    7. Ilse
#    8. Jan
#    9. Karel
#   10. Lien
# Wachtlijst (1)
#    1. Mo
