<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 27.1 — Wie breekt de ledenpagina?

Uit *Python basis — theoriebundel*, hoofdstuk 27 (Inductie, Mill's methods en kritisch denken), paragraaf 27.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-4-het-programma.py` | uitwerking |  |

## Opgave

**De situatie.** De ledenpagina van De Leeslamp geeft sinds vorige week soms een
foutmelding. Acht gebruikers hebben iets doorgegeven.

| Nr. | Browser | Systeem | Ingelogd als | Aantal leden getoond | Sortering | Fout? |
|---|---|---|---|---|---|---|
| 1 | Chrome | Windows | beheerder | 50 | naam | nee |
| 2 | Chrome | Windows | beheerder | 200 | naam | **ja** |
| 3 | Firefox | macOS | lid | 200 | naam | **ja** |
| 4 | Safari | macOS | lid | 50 | datum | nee |
| 5 | Firefox | Linux | beheerder | 200 | datum | **ja** |
| 6 | Chrome | macOS | lid | 100 | naam | nee |
| 7 | Safari | Windows | beheerder | 200 | datum | **ja** |
| 8 | Firefox | Windows | lid | 100 | datum | nee |

**Wat je doet.**

1. Pas de methode van overeenkomst toe op de gevallen mét de fout.
2. Pas de methode van verschil toe: zoek twee rijen die op één ding na gelijk
   zijn.
3. Formuleer de hypothese, en leid er een voorspelling uit af die fout kan gaan.
4. Schrijf een programma dat de verdachte factor uit zo'n tabel haalt.
5. Zeg wat je daarna doet om van een verdachte een aangetoonde oorzaak te maken.

## Uitwerking

**1. De methode van overeenkomst.**

De vier gevallen met een fout zijn 2, 3, 5 en 7.

| Factor | Waarden bij de foutgevallen | Gemeenschappelijk? |
|---|---|---|
| Browser | Chrome, Firefox, Firefox, Safari | Nee |
| Systeem | Windows, macOS, Linux, Windows | Nee |
| Ingelogd als | beheerder, lid, beheerder, beheerder | Nee |
| Aantal leden | 200, 200, 200, 200 | **Ja** |
| Sortering | naam, naam, datum, datum | Nee |

Eén factor blijft over: bij elke fout stonden er 200 leden op de pagina.

**2. De methode van verschil.**

Rij 1 en rij 2 zijn identiek op één ding na.

| | Browser | Systeem | Rol | Aantal | Sortering | Fout? |
|---|---|---|---|---|---|---|
| 1 | Chrome | Windows | beheerder | 50 | naam | nee |
| 2 | Chrome | Windows | beheerder | **200** | naam | **ja** |

Dat is het sterkste bewijs in de hele tabel: alles gelijk, één verschil, en het
gevolg verschilt mee.

**3. De hypothese en de voorspelling.**

*Hypothese:* de fout treedt op zodra er meer dan honderd leden tegelijk getoond
worden.

*Voorspelling die fout kan gaan:* bij 101 leden gaat het mis en bij 100 niet. Dat
is een uitspraak die je kunt breken, en dat is precies wat haar bruikbaar maakt.
Zou de grens bij 150 liggen, dan komen we daar meteen achter.

Merk op wat er in de tabel ontbreekt: er is geen enkele meting tussen 100 en 200.
De grens kan overal daartussen liggen. De methode van overeenkomst wees naar 200
omdat dat toevallig de waarde was die gemeld werd, niet omdat 200 de grens is.

**4. Het programma.**

```python
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
```

```text
Methode van overeenkomst
  elk foutgeval heeft aantal = 200

Methode van verschil
  alles gelijk behalve aantal: 50 tegenover 200

Gemeten aantallen: [50, 100, 200]
Ongemeten gebied : tussen 100 en 200
```

Het programma vindt beide aanwijzingen, en de laatste regel zegt eerlijk wat er
níet gemeten is. Dat is de nuttigste regel van de hele uitvoer.

**5. Van verdachte naar oorzaak.**

| Stap | Wat je doet | Welke methode |
|---|---|---|
| 1 | Zelf een pagina met 200 leden openen | Reproduceren |
| 2 | Binair zoeken tussen 100 en 200 naar de grens | Verschil, herhaald |
| 3 | De grens verklaren: waarom juist daar | Van waarneming naar mechanisme |
| 4 | De oorzaak wegnemen en de fout zien verdwijnen | Methode van verschil |
| 5 | De oorzaak terugzetten en de fout zien terugkomen | De bevestiging die niemand doet |

Stap 5 klinkt overbodig en is dat niet. Zonder die stap heb je alleen aangetoond
dat je wijziging de fout laat verdwijnen; niet dat je de oorzaak begreep. Een
wijziging die het symptoom verbergt, doet dat ook.

> **Waar deductie het overneemt**
>
> Stap 3 is het moment waarop het onderzoek van inductie naar deductie overgaat.
>
> Tot dan verzamelde je waarnemingen. Vanaf stap 3 zeg je: *dit stuk code doet
> voor elk lid een aparte databankbevraging; bij tweehonderd leden zijn dat
> tweehonderd bevragingen; daarom loopt hij over de tijdslimiet.* Dat is een
> deductie, en pas die maakt van een verdachte een verklaring.
>
> Een oorzaak die je niet kunt uitleggen, is nog steeds een gok, hoe goed de
> metingen ook zijn.
