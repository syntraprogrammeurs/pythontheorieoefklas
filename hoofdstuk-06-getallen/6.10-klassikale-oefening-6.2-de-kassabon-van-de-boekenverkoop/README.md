<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 6.2 — De kassabon van de boekenverkoop

Uit *Python basis — theoriebundel*, hoofdstuk 6 (Getallen, casting, invoer en uitvoer), paragraaf 6.10.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking.py` | uitwerking | vraagt invoer |

## Opgave

**De situatie.** De club verkoopt tweedehandsboeken op haar jaarlijkse
rommelmarkt. Je maakt een programma dat één verkoop afrekent en er een nette bon
van maakt.

**Wat je maakt.** Vraag de naam van de koper, het aantal boeken en de prijs per
boek. Toon dan een bon met:

1. De naam van de koper.
2. Het aantal en de prijs per stuk.
3. Het subtotaal.
4. De ledenkorting van 10 procent, in euro én als percentage.
5. Het te betalen bedrag.
6. Het wisselgeld, als de koper met een biljet van 50 euro betaalt.

Alle bedragen op twee cijfers, netjes rechts uitgelijnd in een kolom van tien
tekens breed. Zet er een lijn van streepjes tussen.

## Uitwerking

```python
# De Leeslamp — kassabon van de boekenverkoop
# Cursus Python basis, hoofdstuk 6, oefening 2

KORTINGSPERCENTAGE = 0.10
BILJET = 50
BREEDTE = 32

koper = input("Naam van de koper: ")
aantal = int(input("Aantal boeken: "))
prijs_per_stuk = float(input("Prijs per boek in euro: "))

subtotaal = aantal * prijs_per_stuk
korting = subtotaal * KORTINGSPERCENTAGE
te_betalen = subtotaal - korting
wisselgeld = BILJET - te_betalen

print()
print("=" * BREEDTE)
print(f"{'BOEKENCLUB DE LEESLAMP':^{BREEDTE}}")
print(f"{'rommelmarkt':^{BREEDTE}}")
print("=" * BREEDTE)
print(f"Koper: {koper}")
print("-" * BREEDTE)
print(f"{'Boeken':<16}{aantal:>4} x{prijs_per_stuk:>10.2f}")
print(f"{'Subtotaal':<22}{subtotaal:>10.2f}")
print(f"{'Ledenkorting':<12}{KORTINGSPERCENTAGE:>9.0%}{-korting:>11.2f}")
print("-" * BREEDTE)
print(f"{'TE BETALEN':<22}{te_betalen:>10.2f}")
print(f"{'Gegeven':<22}{BILJET:>10.2f}")
print(f"{'Wisselgeld':<22}{wisselgeld:>10.2f}")
print("=" * BREEDTE)
```

```text
Naam van de koper: Bram Coppens
Aantal boeken: 4
Prijs per boek in euro: 6.50

================================
     BOEKENCLUB DE LEESLAMP
          rommelmarkt
================================
Koper: Bram Coppens
--------------------------------
Boeken             4 x      6.50
Subtotaal                  26.00
Ledenkorting      10%      -2.60
--------------------------------
TE BETALEN                 23.40
Gegeven                    50.00
Wisselgeld                 26.60
================================
```

**De vier technieken die je hier gebruikte.**

**Vermenigvuldigen van tekst.** `"=" * 32` maakt een lijn van tweeëndertig
gelijkheidstekens. Dat je met `*` tekst kunt herhalen, is een eigenaardigheid
van Python die je vaak van pas komt. Je ziet er meer van in hoofdstuk 8.

**Centreren met `:^`.** `f"{tekst:^32}"` zet de tekst midden in een veld van
tweeëndertig tekens. Samen met de lijn erboven en eronder geeft dat een kop.

**Een breedte uit een variabele.** In `f"{tekst:^{BREEDTE}}"` staan accolades
binnen accolades. De binnenste worden eerst ingevuld. Zo hoef je de breedte maar
op één plaats te veranderen.

**Een negatief bedrag tonen.** De korting is een positief getal, maar op een bon
hoort er een minteken voor. `{-korting:>11.2f}` doet dat door de waarde negatief
te maken bij het tonen. De variabele zelf blijft positief, en dat is belangrijk:
je berekening `subtotaal - korting` moet gewoon aftrekken.

**Waarom alles uitlijnt.** Tel de velden van elke regel op:

| Regel | Velden | Samen |
|---|---|---|
| Boeken | 16 + 4 + 2 voor `" x"` + 10 | 32 |
| Subtotaal | 22 + 10 | 32 |
| Ledenkorting | 12 + 9 + 11 | 32 |
| Te betalen | 22 + 10 | 32 |

Elke regel is precies zo breed als de lijn erboven. Daardoor eindigen alle
bedragen in dezelfde kolom, ook al is elke regel anders verdeeld. Dat is de
enige regel die telt bij kolomuitvoer: **laat elke regel op hetzelfde getal
uitkomen**. Reken het na in plaats van het te schatten; één teken verschil zie
je meteen.

**De valkuil met geld.** Deze bon rekent in kommagetallen. Bij 4 boeken van 6,50
gaat dat goed. Probeer eens 3 boeken van 0,10 euro met 10 procent korting: dan
kan er `0.27000000000000002` uitkomen. Zolang je met `:.2f` toont, ziet de
gebruiker daar niets van. Maar zou je die waarde bewaren en er later mee verder
rekenen, dan stapelt de fout op. Voor echte kassasoftware reken je daarom in
centen, met gehele getallen. Zie 5.7.
