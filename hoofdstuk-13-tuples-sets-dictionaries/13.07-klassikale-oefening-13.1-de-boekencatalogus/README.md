<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 13.1 — De boekencatalogus

Uit *Python basis — theoriebundel*, hoofdstuk 13 (Tuples, sets en dictionaries), paragraaf 13.7.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** De club wil haar boeken bijhouden met meer dan alleen een
titel: ook de schrijver, het jaar, het aantal bladzijden, de categorie en wie
het momenteel leent.

**Wat je maakt.**

1. Een lijst van vijf boeken als dictionaries.
2. `zoek_op_schrijver(catalogus, naam)` die alle boeken van een schrijver geeft.
3. `beschikbaar(catalogus)` die alle boeken geeft die niemand leent.
4. `per_categorie(catalogus)` die een dictionary geeft met per categorie het
   aantal boeken.
5. Een overzicht dat de catalogus toont, gesorteerd op jaar.
6. De schrijver met de meeste boeken.

## Uitwerking

```python
# De Leeslamp — de boekencatalogus
# Cursus Python basis, hoofdstuk 13, oefening 1

catalogus = [
    {"titel": "De ontdekking van de hemel", "schrijver": "Harry Mulisch",
     "jaar": 1992, "bladzijden": 928, "categorie": "roman", "geleend_door": "Anke"},
    {"titel": "De aanslag", "schrijver": "Harry Mulisch",
     "jaar": 1982, "bladzijden": 246, "categorie": "roman", "geleend_door": None},
    {"titel": "Het diner", "schrijver": "Herman Koch",
     "jaar": 2009, "bladzijden": 288, "categorie": "roman", "geleend_door": None},
    {"titel": "Turks fruit", "schrijver": "Jan Wolkers",
     "jaar": 1969, "bladzijden": 175, "categorie": "roman", "geleend_door": "Bram"},
    {"titel": "Van Dale", "schrijver": "diverse",
     "jaar": 2022, "bladzijden": 4000, "categorie": "naslagwerk", "geleend_door": None},
]


def zoek_op_schrijver(boeken: list, naam: str) -> list:
    """Alle boeken van een schrijver, ongeacht hoofdletters."""
    return [b for b in boeken if naam.lower() in b["schrijver"].lower()]


def beschikbaar(boeken: list) -> list:
    """Alle boeken die niemand leent."""
    return [b for b in boeken if b["geleend_door"] is None]


def per_categorie(boeken: list) -> dict:
    """Per categorie het aantal boeken."""
    telling = {}
    for boek in boeken:
        categorie = boek["categorie"]
        telling[categorie] = telling.get(categorie, 0) + 1
    return telling


def meeste_boeken(boeken: list) -> tuple:
    """De schrijver met de meeste boeken, en dat aantal."""
    telling = {}
    for boek in boeken:
        telling[boek["schrijver"]] = telling.get(boek["schrijver"], 0) + 1
    schrijver = max(telling, key=telling.get)
    return schrijver, telling[schrijver]


print(f"{'Jaar':<6}{'Titel':<30}{'Schrijver':<16}{'Blz':>6}  Status")
print("-" * 72)
for boek in sorted(catalogus, key=lambda b: b["jaar"]):
    status = "vrij" if boek["geleend_door"] is None else f"bij {boek['geleend_door']}"
    print(f"{boek['jaar']:<6}{boek['titel']:<30}{boek['schrijver']:<16}"
          f"{boek['bladzijden']:>6}  {status}")

print()
print("Van Mulisch:")
for boek in zoek_op_schrijver(catalogus, "mulisch"):
    print(" -", boek["titel"])

print()
print("Beschikbaar:", len(beschikbaar(catalogus)), "van de", len(catalogus))
print("Per categorie:", per_categorie(catalogus))

schrijver, aantal = meeste_boeken(catalogus)
print(f"Meeste boeken: {schrijver} ({aantal})")
```

```text
Jaar  Titel                         Schrijver          Blz  Status
------------------------------------------------------------------------
1969  Turks fruit                   Jan Wolkers        175  bij Bram
1982  De aanslag                    Harry Mulisch      246  vrij
1992  De ontdekking van de hemel    Harry Mulisch      928  bij Anke
2009  Het diner                     Herman Koch        288  vrij
2022  Van Dale                      diverse           4000  vrij

Van Mulisch:
 - De ontdekking van de hemel
 - De aanslag

Beschikbaar: 3 van de 5
Per categorie: {'roman': 4, 'naslagwerk': 1}
Meeste boeken: Harry Mulisch (2)
```

**De vijf technieken.**

**`None` voor "niet uitgeleend".** Niet `""` en niet `"niemand"`. `None` is het
enige antwoord dat "er is hier geen waarde" betekent, en `is None` is de test
die daarbij hoort.

**`max(telling, key=telling.get)`.** Dit ziet er raar uit en is het niet.
`max()` loopt over de sleutels van de dictionary, en `key=telling.get` zegt:
vergelijk ze op hun waarde. Het resultaat is de sleutel met de hoogste waarde.
Bij een gelijkstand krijg je de eerste.

**De comprehensions.** `[b for b in boeken if ...]` is de kortere schrijfwijze
voor het opbouwpatroon uit hoofdstuk 10. Je leert ze in hoofdstuk 14; hier zie
je al hoe leesbaar ze zijn.

**Sorteren zonder de catalogus aan te passen.** `sorted(catalogus, key=...)`
geeft een nieuwe lijst. De catalogus zelf houdt de volgorde waarin de boeken
zijn ingevoerd, en dat is bewust: dat is ook informatie.

**De statusregel.** `"vrij" if boek["geleend_door"] is None else f"bij ..."` is
de verkorte keuze uit hoofdstuk 9. Hier is ze op haar plaats: één korte keuze
tussen twee korte teksten.

**Wat je nu al ziet aankomen.** Elk boek heeft dezelfde vijf velden, elke keer
met dezelfde namen. Dat is precies de situatie waarin een **klasse** beter past
dan een dictionary, want dan schrijf je die velden één keer op. Dat is
hoofdstuk 18.
