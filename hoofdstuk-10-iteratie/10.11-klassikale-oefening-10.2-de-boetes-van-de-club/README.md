<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 10.2 — De boetes van de club

Uit *Python basis — theoriebundel*, hoofdstuk 10 (Iteratie: `while`, `for`, `range`, `break` en `continue`), paragraaf 10.11.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking |  |

## Opgave

**De situatie.** De club rekent boete voor te laat teruggebrachte boeken:

- De eerste week te laat: 50 cent per dag.
- Vanaf de tweede week: 1 euro per dag.
- Vanaf de vierde week: het boek geldt als verloren en kost 25 euro, en de boete
  loopt niet verder op.

**Wat je doet.**

1. Schrijf een lus die voor 0 tot en met 30 dagen te laat de boete berekent.
2. Toon alleen de dagen waarop het bedrag verandert ten opzichte van de dag
   ervoor, plus de dagen 0, 7, 14, 21 en 28.
3. Zorg dat de boete nooit boven de 25 euro uitkomt.
4. Zoek met een lus de eerste dag waarop het goedkoper is om het boek als
   verloren op te geven dan de boete te betalen.

> **Controle**
>
> Bij 3 dagen te laat betaal je 1,50 euro. Bij 10 dagen betaal je 3,50 plus 3,00
> is 6,50 euro. Reken dat na vóór je begint.

## Uitwerking

```python
# De Leeslamp — de boete berekenen
# Cursus Python basis, hoofdstuk 10, oefening 2

TARIEF_WEEK_1 = 0.50
TARIEF_DAARNA = 1.00
DAGEN_PER_WEEK = 7
WEKEN_TOT_VERLOREN = 4
PRIJS_VERLOREN = 25.00


def boete(dagen):
    """De boete voor een boek dat `dagen` dagen te laat is."""
    if dagen >= WEKEN_TOT_VERLOREN * DAGEN_PER_WEEK:
        return PRIJS_VERLOREN

    if dagen <= DAGEN_PER_WEEK:
        bedrag = dagen * TARIEF_WEEK_1
    else:
        bedrag = DAGEN_PER_WEEK * TARIEF_WEEK_1
        bedrag += (dagen - DAGEN_PER_WEEK) * TARIEF_DAARNA

    return min(bedrag, PRIJS_VERLOREN)


print("Dag  Boete   Verandering")
print("-" * 26)

vorige = None
for dagen in range(0, 31):
    bedrag = boete(dagen)
    verandert = vorige is None or bedrag != vorige
    mijlpaal = dagen in (0, 7, 14, 21, 28)

    if verandert or mijlpaal:
        merk = ""
        if vorige is not None and bedrag != vorige:
            merk = f"+{bedrag - vorige:.2f}"
        print(f"{dagen:>3}  {bedrag:>6.2f}   {merk}")

    vorige = bedrag

print()
eerste = None
for dagen in range(0, 60):
    if boete(dagen) >= PRIJS_VERLOREN:
        eerste = dagen
        break

print(f"Vanaf dag {eerste} betaal je de volle {PRIJS_VERLOREN:.2f} euro.")
```

```text
Dag  Boete   Verandering
--------------------------
  0    0.00   
  1    0.50   +0.50
  2    1.00   +0.50
  3    1.50   +0.50
  4    2.00   +0.50
  5    2.50   +0.50
  6    3.00   +0.50
  7    3.50   +0.50
  8    4.50   +1.00
  9    5.50   +1.00
 10    6.50   +1.00
 11    7.50   +1.00
 12    8.50   +1.00
 13    9.50   +1.00
 14   10.50   +1.00
 15   11.50   +1.00
 16   12.50   +1.00
 17   13.50   +1.00
 18   14.50   +1.00
 19   15.50   +1.00
 20   16.50   +1.00
 21   17.50   +1.00
 22   18.50   +1.00
 23   19.50   +1.00
 24   20.50   +1.00
 25   21.50   +1.00
 26   22.50   +1.00
 27   23.50   +1.00
 28   25.00   +1.50

Vanaf dag 28 betaal je de volle 25.00 euro.
```

**De zes beslissingen.**

**De grens van de eerste week.** `dagen <= 7` en niet `dagen < 7`. "De eerste
week" loopt tot en met dag zeven. Dag zeven kost dus 50 cent, niet één euro. Zie
de sprong: dag 7 kost 3,50 en dag 8 kost 4,50.

**Niet opnieuw beginnen bij de tweede week.** Vanaf dag 8 betaal je de volle
eerste week (7 maal 0,50 is 3,50) **plus** het meerdere aan één euro. Wie
`dagen * 1.00` schrijft vanaf dag 8, rekent de eerste week aan het verkeerde
tarief. Dat is de meest gemaakte fout in dit soort trapsgewijze tarieven.

**De bovengrens op twee plaatsen.** Er staat zowel een bewakingsclausule
bovenaan als een `min()` op het einde. Dat lijkt dubbel. Het is het niet: de
eerste vangt "vier weken of meer" op, de tweede vangt af dat de opgetelde boete
de 25 euro overschrijdt vóór dag 28. Bij dit tarief gebeurt dat niet, maar
verhoogt de club het dagtarief, dan wel.

**De sprong op dag 28.** Van 23,50 naar 25,00 is +1,50, en dat lijkt fout. Het
klopt: op dag 28 slaat de regel "verloren" toe, en die is 25 euro plat, geen
optelling. Zonder de kolom "verandering" was die sprong je nooit opgevallen.

**`vorige is None` en niet `vorige == 0`.** Op dag 0 is de boete nul euro. Zou
je `if not vorige` schrijven, dan is dat op dag 0 óók waar en toon je een
verandering die er niet is. Dit is precies het verschil tussen `None` en nul uit
hoofdstuk 5.

**Een functie, al vóór hoofdstuk 11.** De berekening staat in een `def` omdat je
ze twee keer nodig hebt: één keer voor de tabel en één keer om de eerste dag te
zoeken. Zou je de berekening twee keer overtypen, dan kun je ze ook op twee
plaatsen fout aanpassen. Je leert het formeel in het volgende hoofdstuk; hier
zie je alvast waarom het bestaat.
