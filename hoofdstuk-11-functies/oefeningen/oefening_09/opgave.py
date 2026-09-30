# Python basis — oefeningen
# Hoofdstuk 11 — Functies, bereik, return en lambda
# Oefening 9 — Korting berekenen met docstring en type hints

# Maak een functie bereken_korting(bedrag: float, is_lid: bool) -> float
# met type hints.
#
# Geef de functie een docstring van twee regels:
# - eerste regel: "Geeft het bedrag na korting."
# - tweede regel (na een lege regel): een korte uitleg dat leden
#   10% korting krijgen en niet-leden niets minder betalen.
#
# Leden krijgen 10% korting, niet-leden betalen het volledige bedrag.
#
# Roep de functie aan met bedrag=40 en is_lid=True, en met
# bedrag=40 en is_lid=False. Toon telkens het resultaat.
#
# Toon daarna de eerste regel van de docstring met
# bereken_korting.__doc__.splitlines()[0].
#
# Verwachte uitvoer:
# 36.0
# 40
# Geeft het bedrag na korting.
