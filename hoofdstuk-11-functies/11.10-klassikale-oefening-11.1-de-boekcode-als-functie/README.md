<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 11.1 — De boekcode als functie

Uit *Python basis — theoriebundel*, hoofdstuk 11 (Functies, bereik, `return` en `lambda`), paragraaf 11.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** In oefening 8.1 schreef je de boekcode als één blok code. Nu
maak je er functies van, zodat je hem kunt hergebruiken en testen.

**Wat je doet.**

1. Schrijf `beginletters(titel)` die de beginletters van de niet-lidwoorden
   geeft.
2. Schrijf `boekcode(schrijver, titel, jaar)` die de volledige code geeft.
3. Geef beide een docstring en type hints.
4. Test ze met een tabel van vier boeken, waarvan één met een achternaam van
   twee letters.
5. Voeg een parameter `lengte` toe aan `boekcode`, met standaardwaarde 3, zodat
   de club de lengte van het schrijversdeel kan wijzigen.

## Uitwerking

```python
# De Leeslamp — de boekcode, in functies
# Cursus Python basis, hoofdstuk 11, oefening 1

LIDWOORDEN = ("de", "het", "een", "van")


def beginletters(titel: str) -> str:
    """De beginletters van elk woord in de titel, zonder de lidwoorden."""
    letters = ""
    for woord in titel.split():
        if woord.lower() not in LIDWOORDEN:
            letters += woord[0].upper()
    return letters


def achternaam_van(schrijver: str) -> str:
    """Alles na de eerste spatie, dus ook een samengestelde achternaam."""
    delen = schrijver.split(" ", 1)
    return delen[1] if len(delen) > 1 else delen[0]


def boekcode(schrijver: str, titel: str, jaar: int, lengte: int = 3) -> str:
    """De code van een boek, bijvoorbeeld MUL-OH-1992.

    `lengte` bepaalt hoeveel letters van de achternaam worden gebruikt.
    """
    deel_schrijver = achternaam_van(schrijver)[:lengte].upper()
    return f"{deel_schrijver}-{beginletters(titel)}-{jaar}"


gevallen = [
    ("Harry Mulisch", "De ontdekking van de hemel", 1992, "MUL-OH-1992"),
    ("Herman Koch", "Het diner", 2009, "KOC-D-2009"),
    ("Jan Wolkers", "Turks fruit", 1969, "WOL-TF-1969"),
    ("Anna Bo", "Het licht van de zee", 2015, "BO-LZ-2015"),
]

for schrijver, titel, jaar, verwacht in gevallen:
    gekregen = boekcode(schrijver, titel, jaar)
    teken = "ok" if gekregen == verwacht else "FOUT"
    print(f"{gekregen:<14}{verwacht:<14}{teken}")

print()
print("Met vier letters:", boekcode("Harry Mulisch", "Het stenen bruidsbed", 1959, lengte=4))
print("Met twee letters:", boekcode("Harry Mulisch", "Het stenen bruidsbed", 1959, lengte=2))
```

```text
MUL-OH-1992   MUL-OH-1992   ok
KOC-D-2009    KOC-D-2009    ok
WOL-TF-1969   WOL-TF-1969   ok
BO-LZ-2015    BO-LZ-2015    ok

Met vier letters: MULI-SB-1959
Met twee letters: MU-SB-1959
```

**De vier ontwerpkeuzes.**

**Drie functies in plaats van één.** `beginletters` en `achternaam_van` doen elk
één ding en zijn los te testen. `boekcode` plakt ze aan elkaar. Dat is de vorm
die je nastreeft: kleine functies met een duidelijke taak, en één functie die ze
samenbrengt.

**`achternaam_van` vangt de naam zonder spatie op.** `"Cher".split(" ", 1)` geeft
`["Cher"]`, één element. Zonder de controle op de lengte zou `delen[1]` een
`IndexError` geven. Dit soort randgeval vind je alleen door erover na te denken
of door het te testen.

**De standaardwaarde achteraan.** `lengte: int = 3` staat als laatste parameter,
zoals het moet. Bestaande aanroepen blijven daardoor werken: wie geen `lengte`
meegeeft, krijgt drie. Dat is de nette manier om een functie uit te breiden
zonder iets kapot te maken.

**Een tuple in plaats van een lijst voor de lidwoorden.** `LIDWOORDEN` is een
constante die niet mag veranderen. Een tuple kán niet veranderen, en dat past
bij de bedoeling. Je leert het verschil in hoofdstuk 13.

**Wat opvalt aan het testen.** De testtabel staat in dezelfde vorm als in
hoofdstuk 9: gevallen met het verwachte antwoord ernaast. De rij met `Anna Bo`
is er speciaal bij gezet: een achternaam van twee letters. Zonder die rij weet
je niet of `[:3]` op een korte naam een fout geeft. Dat doet het niet, maar dat
is iets wat je **weet** in plaats van **hoopt**.
