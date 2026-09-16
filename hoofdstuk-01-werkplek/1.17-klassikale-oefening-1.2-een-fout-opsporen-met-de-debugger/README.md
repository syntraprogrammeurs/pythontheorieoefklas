<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 1.2 — Een fout opsporen met de debugger

Uit *Python basis — theoriebundel*, hoofdstuk 1 (Je Python-werkplek professioneel opzetten), paragraaf 1.17.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking-de-herstelde-versie.py` | uitwerking |  |

## Opgave

**De situatie.** Een medecursist stuurt je dit programma. Het zou de langste
naam uit de lijst moeten tonen, maar het toont `Bram`.

```python
namen = ["Anke", "Bram", "Cato", "Dominique", "Els"]
langste = ""

for naam in namen:
    if len(naam) > len(langste):
        langste = naam
        break

print(f"De langste naam is {langste}")
```

**Wat je doet.**

1. Typ het programma over in `main.py`. Voer het uit en bevestig de fout.
2. Zet een breakpoint op de regel met `if`.
3. Voer stap voor stap uit met `F10` en noteer bij elke ronde de waarde van
   `naam`, `len(naam)` en `langste`.
4. Zet in het venster **Watch** de uitdrukking `len(langste)`.
5. Zeg in één zin wat er fout is, en waarom het antwoord juist `Bram` is.
6. Herstel de fout en controleer.

## Uitwerking

**Wat de debugger toont.**

| Ronde | `naam` | `len(naam)` | `langste` bij het binnenkomen | Wat er gebeurt |
|---|---|---|---|---|
| 1 | `Anke` | 4 | `""` (lengte 0) | 4 > 0, dus `langste` wordt `Anke`, en dan `break` |

De lus stopt na de eerste ronde. Er is dus nooit een tweede ronde.

**Waarom staat er dan `Bram`?** Dat is een strikvraag, en het punt van de
oefening. Het programma toont `Anke`, niet `Bram`. Wie het antwoord uit de
opgave gelooft in plaats van zelf te kijken, gaat op zoek naar een fout die er
niet is. De debugger geeft binnen tien seconden uitsluitsel.

> Dit is de belangrijkste gewoonte van deze cursus: **geloof de
> foutbeschrijving niet, controleer ze**. Ook niet die van jezelf van gisteren.
> Wat het programma werkelijk doet, staat in de debugger.

**De fout.** De `break` hoort er niet. Die stopt de lus na de eerste naam, dus
het programma vergelijkt nooit verder.

**De herstelde versie:**

```python
namen = ["Anke", "Bram", "Cato", "Dominique", "Els"]
langste = ""

for naam in namen:
    if len(naam) > len(langste):
        langste = naam

print(f"De langste naam is {langste}")
```

```text
De langste naam is Dominique
```

**Wat `Watch` je leert.** Zet je `len(langste)` in het watchvenster, dan zie je
die waarde oplopen: 0, 4, 4, 4, 9, 9. Bij `Bram` en `Cato` verandert er niets,
want 4 is niet groter dan 4. Dat verklaart meteen waarom je `>` en niet `>=`
gebruikt: bij gelijke lengte houd je de eerste. Met `>=` zou je de laatste
houden. Beide zijn verdedigbaar, maar je moet weten wat je kiest.
