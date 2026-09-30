<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 11.2 — Het lidgeld herschrijven

Uit *Python basis — theoriebundel*, hoofdstuk 11 (Functies, bereik, `return` en `lambda`), paragraaf 11.11.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b-wat-er-nog-beter-kan.py` | uitwerking |  |

## Opgave

**De situatie.** De club wil de leesstatistiek uit oefening 10.1 herbruiken voor
elk jaar, en niet alleen voor het voorbije. Je maakt er functies van.

**Wat je doet.**

1. Schrijf `totaal(lijst)`, `gemiddelde(lijst)` en `boven_gemiddelde(lijst)`,
   elk zonder `sum()`.
2. Schrijf `dikste(lijst)` die zowel het nummer als het aantal teruggeeft.
3. Schrijf `staafdiagram(lijst, per_ster)` die het diagram als tekst
   **teruggeeft** in plaats van afdrukt.
4. Zorg dat elke functie een lege lijst netjes verwerkt.
5. Test alle vijf de functies, met de lege lijst als testgeval.

## Uitwerking

```python
# De Leeslamp — de leesstatistiek in functies
# Cursus Python basis, hoofdstuk 11, oefening 2


def totaal(bladzijden: list) -> int:
    """De som van alle bladzijden. Een lege lijst geeft nul."""
    som = 0
    for aantal in bladzijden:
        som += aantal
    return som


def gemiddelde(bladzijden: list) -> float:
    """Het gemiddelde. Een lege lijst geeft 0.0 in plaats van een fout."""
    if not bladzijden:
        return 0.0
    return totaal(bladzijden) / len(bladzijden)


def boven_gemiddelde(bladzijden: list) -> int:
    """Hoeveel boeken dikker zijn dan het gemiddelde."""
    grens = gemiddelde(bladzijden)
    hoeveel = 0
    for aantal in bladzijden:
        if aantal > grens:
            hoeveel += 1
    return hoeveel


def dikste(bladzijden: list) -> tuple:
    """Het nummer en het aantal van het dikste boek, of (None, None)."""
    if not bladzijden:
        return None, None

    nummer = 1
    grootste = bladzijden[0]
    for i, aantal in enumerate(bladzijden, start=1):
        if aantal > grootste:
            grootste = aantal
            nummer = i
    return nummer, grootste


def staafdiagram(bladzijden: list, per_ster: int = 50) -> str:
    """Het staafdiagram als tekst, met één ster per `per_ster` bladzijden."""
    regels = []
    for nummer, aantal in enumerate(bladzijden, start=1):
        sterren = "*" * (aantal // per_ster)
        regels.append(f"{nummer:>3} {sterren:<14}{aantal:>4}")
    return "\n".join(regels)


jaar_2025 = [320, 180, 250, 410, 96, 512, 288, 175, 640, 205, 330, 148]
jaar_2026 = [210, 340, 190]
leeg = []

for naam, lijst in (("2025", jaar_2025), ("2026", jaar_2026), ("leeg", leeg)):
    nummer, aantal = dikste(lijst)
    print(f"{naam:<6} n={len(lijst):<3} totaal={totaal(lijst):<5} "
          f"gem={gemiddelde(lijst):<7.1f} boven={boven_gemiddelde(lijst):<3} "
          f"dikste=boek {nummer} met {aantal}")

print()
print(staafdiagram(jaar_2026))
print()
print(staafdiagram(jaar_2026, per_ster=25))
```

```text
2025   n=12  totaal=3554  gem=296.2   boven=5   dikste=boek 9 met 640
2026   n=3   totaal=740   gem=246.7   boven=1   dikste=boek 2 met 340
leeg   n=0   totaal=0     gem=0.0     boven=0   dikste=boek None met None

  1 ****           210
  2 ******         340
  3 ***            190

  1 ********       210
  2 *************  340
  3 *******        190
```

**De vijf dingen die deze oefening je leerde.**

**De lege lijst is geen randgeval maar het eerste testgeval.** Zonder de
controle in `gemiddelde` krijg je een `ZeroDivisionError`; zonder die in
`dikste` een `IndexError`. Beide fouten verschijnen pas bij de eerste gebruiker
die nog geen boeken heeft. Denk er bij elke functie over na: **wat doet dit bij
niets?**

**`if not bladzijden` en niet `if len(bladzijden) == 0`.** Beide werken; de
eerste is de Python-schrijfwijze uit hoofdstuk 7.

**Een tekst teruggeven in plaats van afdrukken.** `staafdiagram` geeft een string
terug. Daardoor kun je hem afdrukken, in een bestand zetten of testen. Zou hij
zelf afdrukken, dan kon je alleen het eerste. Dat is de regel uit 11.4, en hier
zie je meteen wat ze oplevert: dezelfde functie werkt in het derde voorbeeld met
een andere `per_ster` zonder één regel aanpassing.

**Functies die functies gebruiken.** `gemiddelde` roept `totaal` aan, en
`boven_gemiddelde` roept `gemiddelde` aan. Verandert de manier van optellen, dan
verandert er één functie en volgen de andere vanzelf.

**`dikste` geeft twee waarden terug.** `return nummer, grootste` en dan
`nummer, aantal = dikste(lijst)` bij het aanroepen. Bij de lege lijst geeft ze
`None, None`, zodat het uitpakken altijd werkt. Zou ze bij een lege lijst één
enkele `None` teruggeven, dan crasht het uitpakken.

**Wat er nog beter kan.** De uitvoerregel `dikste=boek None met None` leest
slecht. In een echt programma vang je dat af:

```python
nummer, aantal = None, None
tekst = "geen boeken" if nummer is None else f"boek {nummer} met {aantal}"
print(tekst)
```

```text
geen boeken
```
