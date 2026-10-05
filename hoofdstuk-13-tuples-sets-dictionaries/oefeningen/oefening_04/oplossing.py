# Python basis — oefeningen
# Hoofdstuk 13 — Tuples, sets en dictionaries
# Oplossing 4 — Dubbels weghalen met een set

genres = ["roman", "thriller", "roman", "poëzie",
          "thriller", "strip", "roman"]

uniek = set(genres)

print(f"{len(genres)} uitleningen, {len(uniek)} verschillende genres")
print(sorted(uniek))

# Een set heeft geen vaste volgorde.
