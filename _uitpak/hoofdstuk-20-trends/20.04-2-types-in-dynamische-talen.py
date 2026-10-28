# Python basis — theoriebundel
# Hoofdstuk 20 — Trends in programmeren
# 20.4 Zes trends van dit moment — 2. Types in dynamische talen
#
# Python is dynamisch getypeerd, zoals je in hoofdstuk 5 leerde. Sinds 2015 kun je er
# type hints bij schrijven, en dat wordt in professionele projecten de norm.

def bereken_lidgeld(leeftijd: int, is_student: bool = False) -> int:
    """Het lidgeld in hele euro's."""
    if leeftijd < 12:
        return 0
    return 15 if is_student else 30


print(bereken_lidgeld(34))
print(bereken_lidgeld(20, is_student=True))


# Verwachte uitvoer:
# 30
# 15
