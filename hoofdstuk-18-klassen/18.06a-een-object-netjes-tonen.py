# Python basis — theoriebundel
# Hoofdstuk 18 — Kennismaking met klassen
# 18.6 Een object netjes tonen

class Boek:
    def __init__(self, titel: str, jaar: int):
        self.titel = titel
        self.jaar = jaar


boek = Boek("Het diner", 2009)
print(boek)
