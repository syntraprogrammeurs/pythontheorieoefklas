# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Klassikale oefening 11.2 — Het lidgeld herschrijven, uitwerking

# De Leeslamp — de leesstatistiek in functies
# Cursus Python basis, hoofdstuk 11, oefening 2


def totaal(bladzijden: list) -> int:
    """De som van alle bladzijden. Een lege lijst geeft nul."""
    som = 0
    for aantal in bladzijden:
        som += aantal
    return som


def gemiddelde(bladzijden: list) -> float:
    """Het gemiddelde. Een lege lijst geeft 0.0 in plaats van een fout."""
    if not bladzijden:
        return 0.0
    return totaal(bladzijden) / len(bladzijden)


def boven_gemiddelde(bladzijden: list) -> int:
    """Hoeveel boeken dikker zijn dan het gemiddelde."""
    grens = gemiddelde(bladzijden)
    hoeveel = 0
    for aantal in bladzijden:
        if aantal > grens:
            hoeveel += 1
    return hoeveel


def dikste(bladzijden: list) -> tuple:
    """Het nummer en het aantal van het dikste boek, of (None, None)."""
    if not bladzijden:
        return None, None

    nummer = 1
    grootste = bladzijden[0]
    for i, aantal in enumerate(bladzijden, start=1):
        if aantal > grootste:
            grootste = aantal
            nummer = i
    return nummer, grootste


def staafdiagram(bladzijden: list, per_ster: int = 50) -> str:
    """Het staafdiagram als tekst, met één ster per `per_ster` bladzijden."""
    regels = []
    for nummer, aantal in enumerate(bladzijden, start=1):
        sterren = "*" * (aantal // per_ster)
        regels.append(f"{nummer:>3} {sterren:<14}{aantal:>4}")
    return "\n".join(regels)


jaar_2025 = [320, 180, 250, 410, 96, 512, 288, 175, 640, 205, 330, 148]
jaar_2026 = [210, 340, 190]
leeg = []

for naam, lijst in (("2025", jaar_2025), ("2026", jaar_2026), ("leeg", leeg)):
    nummer, aantal = dikste(lijst)
    print(f"{naam:<6} n={len(lijst):<3} totaal={totaal(lijst):<5} "
          f"gem={gemiddelde(lijst):<7.1f} boven={boven_gemiddelde(lijst):<3} "
          f"dikste=boek {nummer} met {aantal}")

print()
print(staafdiagram(jaar_2026))
print()
print(staafdiagram(jaar_2026, per_ster=25))


# Verwachte uitvoer:
# 2025   n=12  totaal=3554  gem=296.2   boven=5   dikste=boek 9 met 640
# 2026   n=3   totaal=740   gem=246.7   boven=1   dikste=boek 2 met 340
# leeg   n=0   totaal=0     gem=0.0     boven=0   dikste=boek None met None
#
#   1 ****           210
#   2 ******         340
#   3 ***            190
#
#   1 ********       210
#   2 *************  340
#   3 *******        190
