# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# 24.7 Een keten van regels doorrekenen
#
# Als je regels als implicaties opschrijft en er feiten bij hebt, kun je modus ponens
# herhaald toepassen tot er niets nieuws meer bij komt. Dat heet voorwaarts ketenen,
# en het is de kern van elke regelmachine.

# De Leeslamp — regels afleiden met herhaalde modus ponens
REGELS = [
    ({"geschorst"}, "mag_niet_lenen"),
    ({"onbetaald"}, "mag_niet_lenen"),
    ({"boek_te_laat"}, "onbetaald"),
    ({"mag_niet_lenen", "wil_lenen"}, "toon_waarschuwing"),
]


def leid_af(feiten, regels):
    """Past modus ponens toe tot er niets nieuws meer bij komt."""
    bekend = set(feiten)
    stappen = []
    nieuw = True
    while nieuw:
        nieuw = False
        for voorwaarden, gevolg in regels:
            if voorwaarden <= bekend and gevolg not in bekend:
                bekend.add(gevolg)
                stappen.append((sorted(voorwaarden), gevolg))
                nieuw = True
    return bekend, stappen


start = {"boek_te_laat", "wil_lenen"}
bekend, stappen = leid_af(start, REGELS)

print("Gegeven:", sorted(start))
print()
for voorwaarden, gevolg in stappen:
    print(f"  uit {voorwaarden} volgt: {gevolg}")
print()
print("Alles wat volgt:", sorted(bekend))


# Verwachte uitvoer:
# Gegeven: ['boek_te_laat', 'wil_lenen']
#
#   uit ['boek_te_laat'] volgt: onbetaald
#   uit ['onbetaald'] volgt: mag_niet_lenen
#   uit ['mag_niet_lenen', 'wil_lenen'] volgt: toon_waarschuwing
#
# Alles wat volgt: ['boek_te_laat', 'mag_niet_lenen', 'onbetaald', 'toon_waarschuwing', 'wil_lenen']
