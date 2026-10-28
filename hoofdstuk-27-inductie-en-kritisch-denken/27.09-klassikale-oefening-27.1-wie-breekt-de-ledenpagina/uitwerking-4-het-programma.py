# Python basis — theoriebundel
# Hoofdstuk 27 — Inductie, Mill's methods en kritisch denken
# Klassikale oefening 27.1 — Wie breekt de ledenpagina?, uitwerking
#
# 4. Het programma.

# De Leeslamp — de verdachte factor zoeken
# Cursus Python basis, hoofdstuk 27, oefening 1
#
# Dit programma past twee van MILL'S METHODS (27.4) toe op de acht foutmeldingen:
#   - de METHODE VAN OVEREENKOMST: wat hebben alle gevallen MET de fout gemeen?
#   - de METHODE VAN VERSCHIL: zoek twee gevallen die op precies één ding na gelijk
#     zijn, en waarvan het ene de fout heeft en het andere niet.
# Beide zijn INDUCTIE: ze leveren een VERDACHTE op, geen bewezen oorzaak.

# De namen van de vijf factoren (de kolommen van de tabel), in een vaste volgorde.
# Elke melding hieronder geeft haar waarden in precies deze volgorde.
VELDEN = ["browser", "systeem", "rol", "aantal", "sortering"]

# De acht meldingen uit de tabel van 27.9. Elke melding is een tuple van twee delen:
#   - een tuple met de vijf waarden (browser, systeem, rol, aantal, sortering)
#   - True als er een fout was, False als alles goed ging
# Tuples uit hoofdstuk 13: een vaste rij gegevens die je niet wilt veranderen.
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


# De METHODE VAN OVEREENKOMST.
# Geeft een DICTIONARY (hoofdstuk 13) terug: veldnaam -> de waarde die ALLE
# foutgevallen gemeen hebben. Is er geen enkele gedeelde factor, dan is ze leeg.
def overeenkomst(meldingen, velden):
    """Velden met één en dezelfde waarde in alle foutgevallen."""
    # Stap 1: hou alleen de foutgevallen over. Een LIST COMPREHENSION (hoofdstuk 14)
    # die elke melding meteen UITPAKT in 'rij' (de vijf waarden) en 'mislukt' (True
    # of False). "if mislukt" houdt alleen de meldingen met een fout over.
    # Hier: de rijen 2, 3, 5 en 7.
    fout = [rij for rij, mislukt in meldingen if mislukt]
    # Een lege dictionary, die je straks vult.
    uit = {}
    # enumerate (hoofdstuk 10) geeft bij elk veld ook zijn plaats i: 0 "browser",
    # 1 "systeem", ... Met die i haal je de juiste waarde uit elke rij.
    for i, veld in enumerate(velden):
        # Een SET COMPREHENSION (accolades in plaats van vierkante haken) verzamelt
        # de waarden van dit veld bij alle foutgevallen. Een set (hoofdstuk 13)
        # houdt elke waarde maar één keer bij: dubbels verdwijnen vanzelf.
        # Voorbeeld voor "aantal": {200, 200, 200, 200} wordt {200}.
        waarden = {rij[i] for rij in fout}
        # Precies één verschillende waarde: alle foutgevallen hebben ze gemeen.
        if len(waarden) == 1:
            # pop() haalt een element uit de set en geeft het terug. De set heeft er
            # hier maar één, dus je krijgt precies die gedeelde waarde.
            uit[veld] = waarden.pop()
    return uit


# De METHODE VAN VERSCHIL.
# Geeft een lijst terug met tuples (veldnaam, waarde in rij a, waarde in rij b), één
# per paar meldingen dat op precies één veld verschilt en een ander gevolg heeft.
# Dat is de sterkste aanwijzing in de tabel: alles gelijk, één verschil, en het
# gevolg verschilt mee. Een goede reproductie van een bug ziet er precies zo uit.
def verschil(meldingen, velden):
    """Paren die op precies één veld verschillen en een ander gevolg hebben."""
    uit = []
    # Twee geneste lussen (hoofdstuk 10) vormen alle PAREN van meldingen.
    # De buitenste lus neemt melding a; enumerate geeft er de plaats i bij.
    # (rij_a, fout_a) pakt de melding uit in haar waarden en haar uitkomst.
    for i, (rij_a, fout_a) in enumerate(meldingen):
        # De binnenste lus neemt alleen de meldingen NA a: meldingen[i + 1:] is een
        # SLICE (slicing, hoofdstuk 8) vanaf plaats i + 1 tot het einde. Zo
        # vergelijk je elk paar maar één keer, en nooit een melding met zichzelf.
        for rij_b, fout_b in meldingen[i + 1:]:
            # Zelfde gevolg (allebei fout, of allebei goed)? Dan zegt dit paar niets
            # over de oorzaak. continue (hoofdstuk 10) slaat de rest over en gaat
            # naar het volgende paar.
            if fout_a == fout_b:
                continue
            # zip legt de twee rijen naast elkaar: ("Chrome", "Chrome"),
            # ("Windows", "Windows"), ... enumerate geeft er het veldnummer n bij.
            # De comprehension houdt de nummers over van de velden die verschillen.
            anders = [n for n, (a, b) in enumerate(zip(rij_a, rij_b)) if a != b]
            # Precies één verschil: dit is een paar voor de methode van verschil.
            if len(anders) == 1:
                n = anders[0]
                # Bewaar de naam van het veld en de twee waarden.
                # LET OP: rij_a is altijd de melding die hoger in de lijst staat,
                # niet per se het geval zonder fout. Hier is dat toevallig wel zo.
                uit.append((velden[n], rij_a[n], rij_b[n]))
    return uit


# --- Methode van overeenkomst ------------------------------------------------
gedeeld = overeenkomst(MELDINGEN, VELDEN)
print("Methode van overeenkomst")
# Een lege dictionary is FALSY (telt als False, hoofdstuk 7), een gevulde als True.
if gedeeld:
    # .items() geeft telkens een paar (sleutel, waarde) uit de dictionary.
    for veld, waarde in gedeeld.items():
        print(f"  elk foutgeval heeft {veld} = {waarde}")
else:
    print("  geen enkele factor is gemeenschappelijk")

# --- Methode van verschil ----------------------------------------------------
print()
print("Methode van verschil")
paren = verschil(MELDINGEN, VELDEN)
if paren:
    # Elk element van paren is een tuple van drie, dat je meteen uitpakt.
    for veld, waarde_a, waarde_b in paren:
        print(f"  alles gelijk behalve {veld}: {waarde_a} tegenover {waarde_b}")
else:
    print("  geen enkel paar verschilt op precies één veld")

# --- Wat er NIET gemeten is --------------------------------------------------
# Kritisch denken: de methode van overeenkomst wijst naar 200, maar dat is alleen de
# waarde die toevallig gemeld werd. Waar ligt de grens echt? Daarvoor bekijk je
# welke aantallen er überhaupt gemeten zijn.
print()
# VELDEN.index("aantal") geeft de plaats van het veld "aantal": 3.
# De set comprehension verzamelt elk gemeten aantal één keer. Het liggende streepje
# _ is de gewoonte voor "een waarde die ik niet gebruik" (hier: fout of niet).
# sorted() (hoofdstuk 12) maakt van de set een gesorteerde LIJST: [50, 100, 200].
grenzen = sorted({rij[VELDEN.index("aantal")] for rij, _ in MELDINGEN})
print("Gemeten aantallen:", grenzen)
# LET OP: deze regel rekent niets uit. De tekst "tussen 100 en 200" staat er vast
# in; je leidt hem zelf af uit de vorige regel (100 ging goed, 200 ging fout, en
# daartussen is niets gemeten). Met andere meldingen zou hij niet meer kloppen.
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
