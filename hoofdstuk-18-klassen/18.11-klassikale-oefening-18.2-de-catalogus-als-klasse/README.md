<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 18.2 — De catalogus als klasse

Uit *Python basis — theoriebundel*, hoofdstuk 18 (Kennismaking met klassen), paragraaf 18.11.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** Je maakt een klasse `Catalogus` die een verzameling `Boek`-
objecten beheert. Dit is de opstap naar hoofdstuk 19: een klasse die andere
objecten bevat.

**Wat je maakt.**

1. `Boek` zoals in 18.4, met `titel`, `schrijver`, `jaar`, `geleend_door`.
2. `Catalogus` met een lijst boeken, en:
   - `voeg_toe(boek)`, die een dubbele titel weigert;
   - `zoek(deel)`, hoofdletterongevoelig, op titel én schrijver;
   - `beschikbaar()`;
   - `leen_uit(titel, lid)` en `neem_terug(titel)`;
   - `__len__` zodat `len(catalogus)` werkt;
   - `__iter__` zodat `for boek in catalogus` werkt.
3. Een overzicht.

## Uitwerking

```python
# De Leeslamp — de catalogus als klasse
# Cursus Python basis, hoofdstuk 18, oefening 2


class Boek:
    """Eén boek uit de catalogus."""

    def __init__(self, titel: str, schrijver: str, jaar: int):
        self.titel = titel
        self.schrijver = schrijver
        self.jaar = jaar
        self.geleend_door = None

    def is_beschikbaar(self) -> bool:
        """Waar wanneer niemand dit boek geleend heeft."""
        return self.geleend_door is None

    def __str__(self) -> str:
        status = "vrij" if self.is_beschikbaar() else f"bij {self.geleend_door}"
        return f"{self.titel} — {self.schrijver} ({self.jaar}) [{status}]"

    def __repr__(self) -> str:
        return f"Boek({self.titel!r}, {self.schrijver!r}, {self.jaar})"


class Catalogus:
    """Alle boeken van De Leeslamp."""

    def __init__(self):
        self.boeken = []

    def voeg_toe(self, boek: Boek) -> None:
        """Voegt een boek toe. Weigert een titel die er al in staat."""
        if self.zoek_titel(boek.titel) is not None:
            raise ValueError(f"{boek.titel!r} staat al in de catalogus")
        self.boeken.append(boek)

    def zoek_titel(self, titel: str) -> Boek | None:
        """Het boek met precies deze titel, of None."""
        for boek in self.boeken:
            if boek.titel.lower() == titel.lower():
                return boek
        return None

    def zoek(self, deel: str) -> list:
        """Alle boeken waarvan titel of schrijver dit deel bevat."""
        deel = deel.lower()
        return [
            boek for boek in self.boeken
            if deel in boek.titel.lower() or deel in boek.schrijver.lower()
        ]

    def beschikbaar(self) -> list:
        """Alle boeken die niemand geleend heeft."""
        return [boek for boek in self.boeken if boek.is_beschikbaar()]

    def leen_uit(self, titel: str, lid: str) -> None:
        """Leent een boek uit aan een lid."""
        boek = self.zoek_titel(titel)
        if boek is None:
            raise ValueError(f"{titel!r} staat niet in de catalogus")
        if not boek.is_beschikbaar():
            raise ValueError(f"{titel!r} is al bij {boek.geleend_door}")
        boek.geleend_door = lid

    def neem_terug(self, titel: str) -> None:
        """Neemt een boek terug."""
        boek = self.zoek_titel(titel)
        if boek is None:
            raise ValueError(f"{titel!r} staat niet in de catalogus")
        boek.geleend_door = None

    def __len__(self) -> int:
        return len(self.boeken)

    def __iter__(self):
        return iter(self.boeken)

    def __repr__(self) -> str:
        return f"Catalogus({len(self.boeken)} boeken)"


catalogus = Catalogus()
catalogus.voeg_toe(Boek("De ontdekking van de hemel", "Harry Mulisch", 1992))
catalogus.voeg_toe(Boek("De aanslag", "Harry Mulisch", 1982))
catalogus.voeg_toe(Boek("Het diner", "Herman Koch", 2009))
catalogus.voeg_toe(Boek("Turks fruit", "Jan Wolkers", 1969))

catalogus.leen_uit("Het diner", "Anke")
catalogus.leen_uit("Turks fruit", "Bram")

print(f"De catalogus telt {len(catalogus)} boeken.")
print()
for boek in catalogus:
    print(" ", boek)

print()
print("Zoeken op 'mulisch':")
for boek in catalogus.zoek("mulisch"):
    print(" ", boek.titel)

print()
print("Zoeken op 'de':")
for boek in catalogus.zoek("de"):
    print(" ", boek.titel)

print()
print("Beschikbaar:", len(catalogus.beschikbaar()), "van de", len(catalogus))

print()
for poging in [
    ("Het diner", "Cato"),
    ("Bestaat niet", "Cato"),
]:
    try:
        catalogus.leen_uit(*poging)
        print(f"Uitgeleend: {poging[0]} aan {poging[1]}")
    except ValueError as fout:
        print("Geweigerd:", fout)

try:
    catalogus.voeg_toe(Boek("het diner", "Iemand Anders", 2020))
except ValueError as fout:
    print("Geweigerd:", fout)

catalogus.neem_terug("Het diner")
print()
print("Na teruggave beschikbaar:", len(catalogus.beschikbaar()))
```

```text
De catalogus telt 4 boeken.

  De ontdekking van de hemel — Harry Mulisch (1992) [vrij]
  De aanslag — Harry Mulisch (1982) [vrij]
  Het diner — Herman Koch (2009) [bij Anke]
  Turks fruit — Jan Wolkers (1969) [bij Bram]

Zoeken op 'mulisch':
  De ontdekking van de hemel
  De aanslag

Zoeken op 'de':
  De ontdekking van de hemel
  De aanslag

Beschikbaar: 2 van de 4

Geweigerd: 'Het diner' is al bij Anke
Geweigerd: 'Bestaat niet' staat niet in de catalogus
Geweigerd: 'het diner' staat al in de catalogus

Na teruggave beschikbaar: 3
```

**De zes punten.**

**Twee klassen die samenwerken.** `Catalogus` bevat `Boek`-objecten. Dat is de
gewone manier om een verzameling te modelleren, en het is precies wat je in
hoofdstuk 19 doet met `Stack` en `Knoop`.

**`__len__` en `__iter__`.** Door die twee methodes gedraagt je eigen klasse
zich als een ingebouwd type: `len(catalogus)` werkt, en `for boek in catalogus`
ook. Dat is geen truc maar het ontwerp van Python: wie zich aan de afspraken
houdt, past overal in.

**`zoek_titel` teruggeven en niet alleen `True`.** Doordat de methode het boek
zelf teruggeeft, kunnen `voeg_toe`, `leen_uit` en `neem_terug` haar alle drie
gebruiken. Eén functie, drie aanroepers.

**Zoeken op 'de' geeft drie boeken.** Ook *Het diner*, want `"de"` zit in
`"diner"`. Dat is geen fout maar een gevolg van deelstringzoeken. Wil je op hele
woorden zoeken, dan moet je splitsen. Weet wat je zoekfunctie belooft.

**De dubbele titel wordt hoofdletterongevoelig geweigerd.** `"het diner"` en
`"Het diner"` zijn hetzelfde boek. Zonder `.lower()` in `zoek_titel` zou de
tweede erdoor glippen.

**`catalogus.leen_uit(*poging)`.** De sterretjes pakken de tuple uit tot twee
argumenten. Dat is een schrijfwijze die je in hoofdstuk 11 bij *voor wie klaar
is* tegenkwam.

**Wat er nog ontbreekt.** De catalogus zoekt lineair: bij elke opzoeking loopt
ze alle boeken af. Bij vier boeken is dat prima; bij veertigduizend niet. In
hoofdstuk 19 zie je waarom een dictionary daar sneller is, en in hoofdstuk 20
hoe je zoiets meet.
