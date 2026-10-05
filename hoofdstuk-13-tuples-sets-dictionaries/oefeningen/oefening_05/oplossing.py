# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 5 — Wie is er aanwezig?

aanwezig = {"Anke", "Bram"}

aanwezig.add("Cato")
aanwezig.add("Anke")
print(f"Aantal aanwezigen: {len(aanwezig)}")

aanwezig.discard("Bram")
aanwezig.discard("Emma")
print(sorted(aanwezig))
print(f"Bram aanwezig: {'Bram' in aanwezig}")

# Een set bevat elk element maar één keer.
# remove("Emma") geeft een KeyError, discard() niet.
