# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 7 — Een prijslijst als dictionary

prijzen = {"Het diner": 12.5, "Turks fruit": 9.99, "De aanslag": 11.0}

print(prijzen["Turks fruit"])

prijzen["Max Havelaar"] = 14.95
prijzen["Het diner"] = 10.0
del prijzen["De aanslag"]

print(prijzen)
print(f"{len(prijzen)} boeken in de prijslijst")
