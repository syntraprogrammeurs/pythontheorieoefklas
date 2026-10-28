<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 24.2 — De toegangsregels afleiden

Uit *Python basis — theoriebundel*, hoofdstuk 24 (Deductie: syllogismen, geldigheid en argumentvormen), paragraaf 24.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-2-en-3-het-programma.py` | uitwerking |  |

## Opgave

**De situatie.** De Leeslamp krijgt een website. Het bestuur schrijft de regels
in gewone taal op:

> 1. Wie geschorst is, mag niet lenen.
> 2. Wie zijn lidgeld niet betaald heeft, mag niet lenen.
> 3. Wie een boek meer dan zes weken thuis heeft, is geschorst.
> 4. Wie meer dan drie boeken thuis heeft, mag niet lenen.
> 5. Wie niet mag lenen en toch iets probeert te lenen, krijgt een uitleg te
>    zien met de reden.

**Wat je doet.**

1. Schrijf elke regel als implicatie, met letters.
2. Bouw voort op `leid_af` uit 24.7 zodat het programma ook de **reden**
   bijhoudt, en niet alleen de conclusie.
3. Reken drie leden door: Anke (niets aan de hand), Bram (boek van acht weken),
   Cato (vier boeken thuis en lidgeld onbetaald).
4. Zeg wat er misgaat als je deze regels als gewone `if`-`else` zou schrijven.

## Uitwerking

**1. De regels in symbolen.**

| Nr. | Implicatie | Letters |
|---|---|---|
| 1 | `g → ¬l` | `g` geschorst, `l` mag lenen |
| 2 | `¬b → ¬l` | `b` lidgeld betaald |
| 3 | `t → g` | `t` boek langer dan zes weken thuis |
| 4 | `v → ¬l` | `v` meer dan drie boeken thuis |
| 5 | `¬l ∧ p → u` | `p` probeert te lenen, `u` toon uitleg |

Merk op dat regel 3 een **keten** vormt met regel 1: `t → g` en `g → ¬l` geven
samen `t → ¬l`. Dat is het hypothetisch syllogisme uit 24.4, en het programma
hieronder legt die keten vanzelf.

**2 en 3. Het programma.**

```python
# De Leeslamp — toegangsregels met een uitleg erbij
# Cursus Python basis, hoofdstuk 24, oefening 2

REGELS = [
    ("R1", {"geschorst"}, "mag_niet_lenen",
     "je bent geschorst"),
    ("R2", {"onbetaald"}, "mag_niet_lenen",
     "je lidgeld is niet betaald"),
    ("R3", {"boek_zes_weken"}, "geschorst",
     "je hebt een boek langer dan zes weken thuis"),
    ("R4", {"meer_dan_drie"}, "mag_niet_lenen",
     "je hebt meer dan drie boeken thuis"),
    ("R5", {"mag_niet_lenen", "probeert_te_lenen"}, "toon_uitleg",
     "je probeert te lenen terwijl dat niet mag"),
]


def leid_af(feiten, regels):
    """Herhaalde modus ponens, met per conclusie de regel die haar gaf."""
    bekend = dict.fromkeys(feiten, "gegeven")
    spoor = []
    nieuw = True
    while nieuw:
        nieuw = False
        for code, voorwaarden, gevolg, uitleg in regels:
            if voorwaarden <= bekend.keys() and gevolg not in bekend:
                bekend[gevolg] = code
                spoor.append((code, sorted(voorwaarden), gevolg, uitleg))
                nieuw = True
    return bekend, spoor


def beoordeel(naam, feiten):
    """Drukt de afleiding voor één lid af."""
    bekend, spoor = leid_af(feiten | {"probeert_te_lenen"}, REGELS)
    print(f"{naam}")
    print(f"  gegeven : {sorted(feiten)}")
    for code, voorwaarden, gevolg, uitleg in spoor:
        print(f"  {code}      : {voorwaarden} -> {gevolg}")
    mag = "mag_niet_lenen" not in bekend
    print(f"  besluit : {'mag lenen' if mag else 'mag NIET lenen'}")
    if not mag:
        redenen = [u for _, _, g, u in spoor if g == "mag_niet_lenen"]
        print(f"  reden   : {redenen[0]}")
    print()


beoordeel("Anke", set())
beoordeel("Bram", {"boek_zes_weken"})
beoordeel("Cato", {"meer_dan_drie", "onbetaald"})
```

```text
Anke
  gegeven : []
  besluit : mag lenen

Bram
  gegeven : ['boek_zes_weken']
  R3      : ['boek_zes_weken'] -> geschorst
  R1      : ['geschorst'] -> mag_niet_lenen
  R5      : ['mag_niet_lenen', 'probeert_te_lenen'] -> toon_uitleg
  besluit : mag NIET lenen
  reden   : je bent geschorst

Cato
  gegeven : ['meer_dan_drie', 'onbetaald']
  R2      : ['onbetaald'] -> mag_niet_lenen
  R5      : ['mag_niet_lenen', 'probeert_te_lenen'] -> toon_uitleg
  besluit : mag NIET lenen
  reden   : je lidgeld is niet betaald
```

**Wat het spoor van Bram laat zien.** Niemand heeft opgeschreven dat een boek
van zes weken je het lenen verbiedt. Dat volgt uit twee regels na elkaar, en het
programma legt de keten zelf. Dat is het hypothetisch syllogisme, uitgevoerd.

**Wat er bij Cato opvalt, en waarom dat een echt probleem is.** Cato voldoet aan
twee redenen om geweigerd te worden, en er wordt er maar één getoond. Dat is
geen fout in de logica — één reden volstaat om te weigeren — maar wel een
gebruikersprobleem: Cato betaalt haar lidgeld, probeert opnieuw, en krijgt dan
pas te horen dat ze ook nog te veel boeken thuis heeft.

De logica is correct en de ervaring is slecht. Dat onderscheid is precies wat
hoofdstuk 25 uitwerkt: een geldige redenering is niet automatisch een goede
oplossing.

De uitbreiding is klein: verzamel álle regels die `mag_niet_lenen` opleveren in
plaats van de eerste.

**4. Waarom dit geen `if`-`else` is.**

| Met deze aanpak | Met een `if`-`else`-keten |
|---|---|
| Een regel bijzetten is één regel in de lijst | Je moet weten waar in de keten hij hoort |
| Ketens ontstaan vanzelf | De keten `t → g → ¬l` schrijf je met de hand, en je vergeet hem |
| De reden komt uit de regel zelf | Je typt de tekst een tweede keer, naast de voorwaarde |
| Alle redenen zijn te vinden | Na de eerste `return` kom je niets meer te weten |
| De volgorde van de regels doet er niet toe | De volgorde bepaalt de uitkomst, en dat is een bron van fouten |

Die laatste rij is de belangrijkste. In een `if`-`elif`-keten is de volgorde
betekenisvol: de eerste die past, wint. Hier niet: de lus draait tot er niets
meer bij komt, en dat levert altijd dezelfde verzameling op, ongeacht hoe je de
regels ordent.

> **Let op**
>
> Dit betekent niet dat je voortaan regelmachines schrijft in plaats van `if`.
> Voor vijf regels is `if` prima en veel leesbaarder.
>
> De les is: **als je merkt dat je regels aan het ordenen bent in plaats van op te
> schrijven**, dan is de `if`-keten je aan het beperken. Dat is het moment om na te
> denken, niet het moment om nog een `elif` bij te zetten.
