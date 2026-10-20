# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# Klassikale oefening 16.2 — Een tekstbestand analyseren, uitwerking

# De Leeslamp — een tekstbestand analyseren
# Cursus Python basis, hoofdstuk 16, oefening 2

from pathlib import Path

BRON = Path("verslagen.txt")
DOEL = Path("statistiek.txt")
STOPWOORDEN = {"de", "het", "een", "en", "van", "is", "in", "dat", "die", "te"}
LEESTEKENS = ".,;:!?\"'()"

TEKST = """Het boek gaat over twee families en een diner in een restaurant.
De schrijfstijl is vlot en het verhaal loopt goed door.
Het einde stelt teleur, want het verhaal valt in de laatste bladzijden stil.
Toch is het een boek dat je in een avond uitleest.
De discussie in de club ging vooral over het einde van het boek."""

BRON.write_text(TEKST + "\n", encoding="utf-8")


def tel_woorden(pad: Path) -> dict:
    """Per woord het aantal keer dat het voorkomt, zonder de stopwoorden."""
    telling = {}
    with open(pad, encoding="utf-8") as bestand:
        for regel in bestand:
            for ruw in regel.split():
                woord = ruw.strip(LEESTEKENS).lower()
                if not woord or woord in STOPWOORDEN:
                    continue
                telling[woord] = telling.get(woord, 0) + 1
    return telling


def kengetallen(pad: Path) -> dict:
    """Het aantal regels, woorden en tekens van een tekstbestand."""
    regels = woorden = tekens = 0
    with open(pad, encoding="utf-8") as bestand:
        for regel in bestand:
            regels += 1
            woorden += len(regel.split())
            tekens += len(regel.rstrip("\n"))
    return {"regels": regels, "woorden": woorden, "tekens": tekens}


cijfers = kengetallen(BRON)
telling = tel_woorden(BRON)
top = sorted(telling.items(), key=lambda p: (-p[1], p[0]))[:10]

regels_uit = [
    "STATISTIEK VAN DE LEESVERSLAGEN",
    "=" * 34,
    f"Regels : {cijfers['regels']}",
    f"Woorden: {cijfers['woorden']}",
    f"Tekens : {cijfers['tekens']}",
    f"Verschillende woorden (zonder stopwoorden): {len(telling)}",
    "",
    "De tien meest gebruikte woorden",
    "-" * 34,
]
for woord, aantal in top:
    regels_uit.append(f"{woord:<20}{aantal:>4}  {'*' * aantal}")

regels_uit.append("")
regels_uit.append("Woorden per regel")
regels_uit.append("-" * 34)
with open(BRON, encoding="utf-8") as bestand:
    for nummer, regel in enumerate(bestand, start=1):
        regels_uit.append(f"  regel {nummer}: {len(regel.split()):>3} woorden")

DOEL.write_text("\n".join(regels_uit) + "\n", encoding="utf-8")
print(DOEL.read_text(encoding="utf-8"))

BRON.unlink()
DOEL.unlink()


# Verwachte uitvoer:
# STATISTIEK VAN DE LEESVERSLAGEN
# ==================================
# Regels : 5
# Woorden: 59
# Tekens : 309
# Verschillende woorden (zonder stopwoorden): 29
#
# De tien meest gebruikte woorden
# ----------------------------------
# boek                   3  ***
# einde                  2  **
# over                   2  **
# verhaal                2  **
# avond                  1  *
# bladzijden             1  *
# club                   1  *
# diner                  1  *
# discussie              1  *
# door                   1  *
#
# Woorden per regel
# ----------------------------------
#   regel 1:  12 woorden
#   regel 2:  10 woorden
#   regel 3:  13 woorden
#   regel 4:  11 woorden
#   regel 5:  13 woorden
