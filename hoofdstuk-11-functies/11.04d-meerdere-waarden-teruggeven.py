# Python basis — theoriebundel
# Hoofdstuk 11 — Functies, bereik, return en lambda
# 11.4 return: iets teruggeven — Meerdere waarden teruggeven

def splits_tijd(minuten):
    return minuten // 60, minuten % 60


uren, rest = splits_tijd(137)
print(f"{uren} uur en {rest} minuten")


# Verwachte uitvoer:
# 2 uur en 17 minuten
