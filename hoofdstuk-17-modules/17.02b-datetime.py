# Python basis — theoriebundel
# Hoofdstuk 17 — Modules, de standaardbibliotheek en pip
# 17.2 De standaardbibliotheek — datetime

from datetime import date, datetime, timedelta

vandaag = date(2026, 9, 10)
print(vandaag)
print(vandaag.year, vandaag.month, vandaag.day)
print(vandaag.strftime("%d/%m/%Y"))
print(vandaag.strftime("%A %d %B %Y"))

over_vier_weken = vandaag + timedelta(weeks=4)
print(over_vier_weken)
print((over_vier_weken - vandaag).days, "dagen ertussen")

uit_tekst = datetime.strptime("2026-09-01", "%Y-%m-%d").date()
print(uit_tekst, type(uit_tekst).__name__)
print(vandaag > uit_tekst)


# Verwachte uitvoer:
# 2026-09-10
# 2026 9 10
# 10/09/2026
# Thursday 10 September 2026
# 2026-10-08
# 28 dagen ertussen
# 2026-09-01 date
# True
