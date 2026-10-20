# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# Klassikale oefening 18.2 — De catalogus als klasse, uitwerking

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


# Verwachte uitvoer:
# De catalogus telt 4 boeken.
#
#   De ontdekking van de hemel — Harry Mulisch (1992) [vrij]
#   De aanslag — Harry Mulisch (1982) [vrij]
#   Het diner — Herman Koch (2009) [bij Anke]
#   Turks fruit — Jan Wolkers (1969) [bij Bram]
#
# Zoeken op 'mulisch':
#   De ontdekking van de hemel
#   De aanslag
#
# Zoeken op 'de':
#   De ontdekking van de hemel
#   De aanslag
#
# Beschikbaar: 2 van de 4
#
# Geweigerd: 'Het diner' is al bij Anke
# Geweigerd: 'Bestaat niet' staat niet in de catalogus
# Geweigerd: 'het diner' staat al in de catalogus
#
# Na teruggave beschikbaar: 3
