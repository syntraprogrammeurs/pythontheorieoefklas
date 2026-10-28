<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 28.2 — De beslissingstabel van de uitleenregel

Uit *Python basis — theoriebundel*, hoofdstuk 28 (Kritisch denken toegepast op softwaretesten), paragraaf 28.12.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave.py` | opgave |  |
| `uitwerking-3-de-herstelde-functie.py` | uitwerking |  |

## Opgave

**De situatie.** Deze functie staat in de code van De Leeslamp.

```python
def mag_lenen(betaald, geschorst, boeken_thuis):
    """Bevat een ontbrekend geval."""
    if not betaald:
        return False
    if geschorst:
        return False
    return True
```

De regel luidt: lenen mag als het lidgeld betaald is, het lid niet geschorst is,
en het lid niet meer dan drie boeken thuis heeft.

**Wat je doet.**

1. Maak de volledige beslissingstabel met acht rijen.
2. Wijs de rijen aan waarin de functie het verkeerde antwoord geeft.
3. Herstel de functie en toon met de tabel dat alle acht rijen kloppen.
4. Bereken hoeveel rijen je nodig hebt als er een vierde voorwaarde bij komt, en
   zeg wat je dan doet.

## Uitwerking

**1 en 2. De tabel, met de fouten erin.**

| Nr. | Betaald | Geschorst | Meer dan 3 boeken | Hoort | Geeft | Klopt? |
|---|---|---|---|---|---|---|
| 1 | ja | ja | ja | nee | nee | ja |
| 2 | ja | ja | nee | nee | nee | ja |
| 3 | ja | nee | ja | **nee** | **ja** | **NEE** |
| 4 | ja | nee | nee | ja | ja | ja |
| 5 | nee | ja | ja | nee | nee | ja |
| 6 | nee | ja | nee | nee | nee | ja |
| 7 | nee | nee | ja | nee | nee | ja |
| 8 | nee | nee | nee | nee | nee | ja |

Eén rij van de acht is fout: rij 3. Een lid dat betaald heeft, niet geschorst is
en toch vijf boeken thuis heeft, mag lenen terwijl dat niet hoort.

**Waarom juist die rij zo makkelijk gemist wordt.** De parameter `boeken_thuis`
staat wél in de handtekening van de functie en wordt nergens gebruikt. Ruff meldt
dat niet, want een ongebruikte parameter is geen fout. De beslissingstabel meldt
het wel, want die vult elke kolom in.

**3. De herstelde functie, met de tabel als test.**

```python
# De Leeslamp — de uitleenregel, met de volledige beslissingstabel als test
# Cursus Python basis, hoofdstuk 28, oefening 2
from itertools import product


def mag_lenen(betaald, geschorst, te_veel_thuis):
    """Lenen mag als er geen enkele reden is om te weigeren."""
    if not betaald:
        return False
    if geschorst:
        return False
    if te_veel_thuis:
        return False
    return True


def verwacht(betaald, geschorst, te_veel_thuis):
    """De regel zoals het bestuur hem uitsprak, los van de code."""
    return betaald and not geschorst and not te_veel_thuis


print("betaald  gesch.   te veel  hoort  geeft  klopt")
print("-" * 47)
gefaald = 0
for b, g, t in product([True, False], repeat=3):
    hoort = verwacht(b, g, t)
    geeft = mag_lenen(b, g, t)
    klopt = hoort == geeft
    gefaald += not klopt
    print(f"{b!s:<9}{g!s:<9}{t!s:<9}{hoort!s:<7}{geeft!s:<7}{klopt}")

print()
print(f"{8 - gefaald} van de 8 rijen kloppen")
```

```text
betaald  gesch.   te veel  hoort  geeft  klopt
-----------------------------------------------
True     True     True     False  False  True
True     True     False    False  False  True
True     False    True     False  False  True
True     False    False    True   True   True
False    True     True     False  False  True
False    True     False    False  False  True
False    False    True     False  False  True
False    False    False    False  False  True

8 van de 8 rijen kloppen
```

> **Waarom**
>
> Merk op wat `verwacht()` doet: het is de regel opnieuw opgeschreven, in één regel,
> los van de code die getest wordt.
>
> Dat is met opzet. Als je de test schrijft door de code te lezen, test je of de
> code doet wat de code doet, en dat is de cirkelredenering uit hoofdstuk 27. Door
> de regel rechtstreeks uit de tekst van het bestuur te vertalen, toets je iets
> onafhankelijks.
>
> Dat is ook de reden waarom degene die de tests schrijft, bij voorkeur niet
> dezelfde is als degene die de functie schreef. Wie beide doet, maakt in allebei
> dezelfde denkfout.

**4. Als er een vierde voorwaarde bij komt.**

| Voorwaarden | Rijen |
|---|---|
| 3 | 8 |
| 4 | 16 |
| 5 | 32 |
| 6 | 64 |
| 10 | 1024 |

Het aantal verdubbelt elke keer: 2ⁿ, precies zoals bij de waarheidstabellen uit
hoofdstuk 23. Zo'n verdubbeling loopt razendsnel uit de hand.

Wat je doet zodra dat te veel wordt, in volgorde:

| Stap | Wat je doet |
|---|---|
| 1 | Vraag of alle voorwaarden echt onafhankelijk zijn. Meestal zijn er twee die samenhoren |
| 2 | Splits de functie: een deel dat weigeringsredenen verzamelt, een deel dat beslist |
| 3 | Test elk deel apart. Vier plus vier voorwaarden geven 16 plus 16 rijen, geen 256 |
| 4 | Blijft het onhandelbaar, gebruik dan **paarsgewijs testen**: alle paren van waarden dekken in plaats van alle combinaties |

De echte les zit in stap 1. Een functie met zes onafhankelijke booleaanse
voorwaarden is bijna altijd een functie die twee dingen tegelijk doet. De
beslissingstabel is dan niet alleen een testtechniek maar ook een
ontwerpwaarschuwing.
