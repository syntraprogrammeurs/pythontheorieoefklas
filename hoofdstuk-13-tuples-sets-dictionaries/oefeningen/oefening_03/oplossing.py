# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 3 — Leestijd splitsen in uren en minuten

def splits_tijd(minuten):
    return minuten // 60, minuten % 60


leestijden = [("Het diner", 410), ("Turks fruit", 245), ("De aanslag", 58)]

for titel, minuten in leestijden:
    uren, rest = splits_tijd(minuten)
    print(f"{titel}: {uren}u{rest:02d}")
