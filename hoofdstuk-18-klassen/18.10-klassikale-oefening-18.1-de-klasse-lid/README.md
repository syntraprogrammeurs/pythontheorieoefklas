<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 18.1 — De klasse `Lid`

Uit *Python basis — theoriebundel*, hoofdstuk 18 (Kennismaking met klassen), paragraaf 18.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** Je zet de ledenkaart uit hoofdstuk 5 om naar een klasse, met de
regels erbij.

**Wat je maakt.** Een klasse `Lid` met:

1. Attributen: naam, leeftijd, of het lid student is, jaren lidmaatschap, en een
   eigen lijst gelezen boeken.
2. `lidgeld()` volgens de regels van de club.
3. `lees(titel)` die een boek aan de leeslijst toevoegt, zonder dubbels.
4. `heeft_gelezen(titel)`.
5. `mag_lenen()`: minstens twaalf jaar, of jonger met begeleiding, en hoogstens
   vijf boeken tegelijk.
6. `__str__` en `__repr__`.
7. Een klasseattribuut dat telt hoeveel leden er zijn aangemaakt.

Test met drie leden.

## Uitwerking

```python
# De Leeslamp — de klasse Lid
# Cursus Python basis, hoofdstuk 18, oefening 1


class Lid:
    """Eén lid van boekenclub De Leeslamp."""

    LIDGELD_VOLWASSENE = 30
    LIDGELD_STUDENT = 15
    LEEFTIJD_GRATIS = 12
    JAREN_VOOR_KORTING = 3
    KORTING = 5
    MAX_UITGELEEND = 5

    aantal_leden = 0

    def __init__(self, naam: str, leeftijd: int, is_student: bool = False,
                 jaren_lid: int = 0, begeleid: bool = False):
        if leeftijd < 0 or leeftijd > 130:
            raise ValueError(f"onmogelijke leeftijd: {leeftijd}")
        if jaren_lid > leeftijd:
            raise ValueError(f"{jaren_lid} jaar lid op {leeftijd}-jarige leeftijd?")

        self.naam = naam
        self.leeftijd = leeftijd
        self.is_student = is_student
        self.jaren_lid = jaren_lid
        self.begeleid = begeleid
        self.gelezen = []
        self.uitgeleend = []

        Lid.aantal_leden += 1

    def lidgeld(self) -> int:
        """Het lidgeld in hele euro's."""
        if self.leeftijd < self.LEEFTIJD_GRATIS:
            bedrag = 0
        elif self.is_student:
            bedrag = self.LIDGELD_STUDENT
        else:
            bedrag = self.LIDGELD_VOLWASSENE

        if self.jaren_lid >= self.JAREN_VOOR_KORTING:
            bedrag -= self.KORTING
        return max(bedrag, 0)

    def lees(self, titel: str) -> bool:
        """Voegt een gelezen boek toe. Geeft False als het er al in stond."""
        if titel in self.gelezen:
            return False
        self.gelezen.append(titel)
        return True

    def heeft_gelezen(self, titel: str) -> bool:
        """Waar wanneer dit lid dat boek gelezen heeft."""
        return titel in self.gelezen

    def mag_lenen(self) -> bool:
        """Waar wanneer dit lid nu een boek mag meenemen."""
        oud_genoeg = self.leeftijd >= self.LEEFTIJD_GRATIS or self.begeleid
        onder_de_limiet = len(self.uitgeleend) < self.MAX_UITGELEEND
        return oud_genoeg and onder_de_limiet

    def __str__(self) -> str:
        return f"{self.naam} ({self.leeftijd})"

    def __repr__(self) -> str:
        return f"Lid({self.naam!r}, {self.leeftijd})"


anke = Lid("Anke Peeters", 34, jaren_lid=3)
bram = Lid("Bram Coppens", 20, is_student=True, jaren_lid=1)
cato = Lid("Cato Dhondt", 9, begeleid=True)

anke.lees("Het diner")
anke.lees("Turks fruit")
print("Nog eens hetzelfde boek:", anke.lees("Het diner"))

cato.uitgeleend = ["a", "b", "c", "d", "e"]

print()
print(f"{'Lid':<20}{'Lidgeld':>8}{'Gelezen':>9}{'Mag lenen':>11}")
print("-" * 48)
for lid in (anke, bram, cato):
    print(f"{str(lid):<20}{lid.lidgeld():>8}{len(lid.gelezen):>9}"
          f"{str(lid.mag_lenen()):>11}")

print()
print("Anke las Het diner :", anke.heeft_gelezen("Het diner"))
print("Anke las De aanslag:", anke.heeft_gelezen("De aanslag"))
print("Aantal leden       :", Lid.aantal_leden)
print("Als lijst          :", [anke, bram, cato])

print()
try:
    Lid("Zoe Janssens", 20, jaren_lid=25)
except ValueError as fout:
    print("Geweigerd:", fout)
```

```text
Nog eens hetzelfde boek: False

Lid                  Lidgeld  Gelezen  Mag lenen
------------------------------------------------
Anke Peeters (34)         25        2       True
Bram Coppens (20)         15        0       True
Cato Dhondt (9)            0        0      False

Anke las Het diner : True
Anke las De aanslag: False
Aantal leden       : 3
Als lijst          : [Lid('Anke Peeters', 34), Lid('Bram Coppens', 20), Lid('Cato Dhondt', 9)]

Geweigerd: 25 jaar lid op 20-jarige leeftijd?
```

**De zes ontwerpkeuzes.**

**De constanten als klasseattribuut.** Ze horen bij het begrip "lid", niet bij
één lid. `self.LIDGELD_VOLWASSENE` werkt ook: Python zoekt eerst bij het object
en dan bij de klasse. Dat maakt het mogelijk om ze voor één lid te overschrijven,
al zul je dat zelden willen.

**`self.gelezen = []` in `__init__`, niet in de klasse.** Zou je hem als
klasseattribuut zetten, dan delen alle leden dezelfde leeslijst. Dat is de
valkuil uit 18.5 en uit oefening 14.2.

**De controle in `__init__`.** Een lid met een onmogelijke leeftijd wordt nooit
aangemaakt. Dat is de plaats om te bewaken: bij het aanmaken. Een object dat
bestaat, is dan per definitie in orde.

**`lees()` geeft `True` of `False` terug** in plaats van niets. Zo weet de
aanroeper of er echt iets is bijgekomen. Dat is nuttiger dan stilzwijgend niets
doen.

**`mag_lenen` met benoemde deelvoorwaarden.** Dezelfde vorm als in hoofdstuk 7:
`oud_genoeg` en `onder_de_limiet` in plaats van één lange regel.

**`Lid.aantal_leden += 1` en niet `self.aantal_leden += 1`.** Dat tweede zou een
**instantieattribuut** aanmaken met de waarde 1, en de klasseteller ongemoeid
laten. Een subtiel verschil met een groot gevolg. Bij een klasseattribuut dat je
wilt wijzigen, schrijf je altijd de klassenaam.

**Wat opvalt aan Cato.** Ze is negen, maar wordt begeleid, dus `oud_genoeg` is
waar. Toch mag ze niet lenen: ze heeft er al vijf uit. De twee voorwaarden doen
allebei hun werk, en de testgegevens zijn zo gekozen dat je dat kunt zien.
