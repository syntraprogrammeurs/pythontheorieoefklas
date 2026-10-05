# Python basis — theoriebundel
# Hoofdstuk 13 — Tuples, sets en dictionaries
# 13.2 Tuples
#
# Tuples zie je vooral bij het teruggeven van meerdere waarden, wat je in hoofdstuk 11
# al deed:

def splits_tijd(minuten: int) -> tuple:
    """Uren en minuten, als tuple."""
    return minuten // 60, minuten % 60


print(splits_tijd(137))
uren, rest = splits_tijd(137)
print(f"{uren}u{rest:09d}")


# Verwachte uitvoer:
# (2, 17)
# 2u17
