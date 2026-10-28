# Python basis — theoriebundel
# Hoofdstuk 27 — Inductie, Mill's methods en kritisch denken
# Klassikale oefening 27.1 — Wie breekt de ledenpagina?, uitwerking
#
# 4. Het programma.

# De Leeslamp — de verdachte factor zoeken
# Cursus Python basis, hoofdstuk 27, oefening 1

VELDEN = ["browser", "systeem", "rol", "aantal", "sortering"]

MELDINGEN = [
    (("Chrome", "Windows", "beheerder", 50, "naam"), False),
    (("Chrome", "Windows", "beheerder", 200, "naam"), True),
    (("Firefox", "macOS", "lid", 200, "naam"), True),
    (("Safari", "macOS", "lid", 50, "datum"), False),
    (("Firefox", "Linux", "beheerder", 200, "datum"), True),
    (("Chrome", "macOS", "lid", 100, "naam"), False),
    (("Safari", "Windows", "beheerder", 200, "datum"), True),
    (("Firefox", "Windows", "lid", 100, "datum"), False),
]


def overeenkomst(meldingen, velden):
    """Velden met één en dezelfde waarde in alle foutgevallen."""
    fout = [rij for rij, mislukt in meldingen if mislukt]
    uit = {}
    for i, veld in enumerate(velden):
        waarden = {rij[i] for rij in fout}
        if len(waarden) == 1:
            uit[veld] = waarden.pop()
    return uit


def verschil(meldingen, velden):
    """Paren die op precies één veld verschillen en een ander gevolg hebben."""
    uit = []
    for i, (rij_a, fout_a) in enumerate(meldingen):
        for rij_b, fout_b in meldingen[i + 1:]:
            if fout_a == fout_b:
                continue
            anders = [n for n, (a, b) in enumerate(zip(rij_a, rij_b)) if a != b]
            if len(anders) == 1:
                n = anders[0]
                uit.append((velden[n], rij_a[n], rij_b[n]))
    return uit


gedeeld = overeenkomst(MELDINGEN, VELDEN)
print("Methode van overeenkomst")
if gedeeld:
    for veld, waarde in gedeeld.items():
        print(f"  elk foutgeval heeft {veld} = {waarde}")
else:
    print("  geen enkele factor is gemeenschappelijk")

print()
print("Methode van verschil")
paren = verschil(MELDINGEN, VELDEN)
if paren:
    for veld, waarde_a, waarde_b in paren:
        print(f"  alles gelijk behalve {veld}: {waarde_a} tegenover {waarde_b}")
else:
    print("  geen enkel paar verschilt op precies één veld")

print()
grenzen = sorted({rij[VELDEN.index("aantal")] for rij, _ in MELDINGEN})
print("Gemeten aantallen:", grenzen)
print("Ongemeten gebied : tussen 100 en 200")


# Verwachte uitvoer:
# Methode van overeenkomst
#   elk foutgeval heeft aantal = 200
#
# Methode van verschil
#   alles gelijk behalve aantal: 50 tegenover 200
#
# Gemeten aantallen: [50, 100, 200]
# Ongemeten gebied : tussen 100 en 200
