# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.4 Methodes
#
# Een methode is een functie die bij een klasse hoort.

class Boek:
    """Eén boek uit de catalogus."""

    LIDWOORDEN = ("de", "het", "een", "van")

    def __init__(self, titel: str, schrijver: str, jaar: int, bladzijden: int):
        self.titel = titel
        self.schrijver = schrijver
        self.jaar = jaar
        self.bladzijden = bladzijden
        self.geleend_door = None

    def code(self) -> str:
        """De boekcode, zoals MUL-OH-1992."""
        achternaam = self.schrijver.split(" ", 1)[-1]
        letters = "".join(
            woord[0].upper()
            for woord in self.titel.split()
            if woord.lower() not in self.LIDWOORDEN
        )
        return f"{achternaam[:3].upper()}-{letters}-{self.jaar}"

    def is_beschikbaar(self) -> bool:
        """Waar wanneer niemand dit boek geleend heeft."""
        return self.geleend_door is None

    def leen_uit(self, lid: str) -> None:
        """Leent het boek uit. Werpt een fout als het al uit is."""
        if not self.is_beschikbaar():
            raise ValueError(f"{self.titel} is al bij {self.geleend_door}")
        self.geleend_door = lid

    def neem_terug(self) -> None:
        """Zet het boek terug op de plank."""
        self.geleend_door = None

    def leestijd(self, woorden_per_minuut: int = 250) -> int:
        """Het geschatte aantal minuten leestijd."""
        return round(self.bladzijden * 300 / woorden_per_minuut)


boek = Boek("De ontdekking van de hemel", "Harry Mulisch", 1992, 928)

print(boek.code())
print(boek.is_beschikbaar())
print(boek.leestijd(), "minuten")

boek.leen_uit("Anke")
print(boek.is_beschikbaar(), "bij", boek.geleend_door)

try:
    boek.leen_uit("Bram")
except ValueError as fout:
    print("Geweigerd:", fout)

boek.neem_terug()
print(boek.is_beschikbaar())


# Verwachte uitvoer:
# MUL-OH-1992
# True
# 1114 minuten
# False bij Anke
# Geweigerd: De ontdekking van de hemel is al bij Anke
# True
