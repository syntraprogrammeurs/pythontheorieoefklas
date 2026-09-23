<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 9.1 — De uitleentermijn, nu in code

Uit *Python basis — theoriebundel*, hoofdstuk 9 (Selectie: `if`, `elif`, `else` en `match`), paragraaf 9.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b-de-schoonheidsfout.py` | uitwerking |  |

## Opgave

**De situatie.** Je schreef in oefening 3.1 de pseudocode voor de uitleentermijn.
Nu bouw je hem.

De regels, ter herinnering:

- Een gewoon boek: 4 weken.
- Een boek uit de categorie "nieuw": 2 weken.
- Een naslagwerk mag niet mee naar huis.
- Wie meer dan 3 boeken tegelijk leent, krijgt voor elk boek 1 week minder, maar
  nooit minder dan 1 week.

**Wat je doet.**

1. Schrijf het programma, met constanten bovenaan.
2. Handel het naslagwerk af als bewakingsclausule, dus meteen bovenaan.
3. Test het tegen de testtabel uit oefening 3.1, in code, zoals in 9.8.
4. Voeg één rij aan je testtabel toe die er nog niet in stond.

## Uitwerking

```python
# De Leeslamp — de uitleentermijn
# Cursus Python basis, hoofdstuk 9, oefening 1

WEKEN_GEWOON = 4
WEKEN_NIEUW = 2
DRUKKE_LENER = 3          # meer dan 3 boeken geeft een week minder
MINIMUM_WEKEN = 1

gevallen = [
    ("gewoon", 1, 4),
    ("nieuw", 1, 2),
    ("naslagwerk", 1, None),
    ("gewoon", 3, 4),
    ("gewoon", 4, 3),
    ("nieuw", 4, 1),
    ("naslagwerk", 9, None),
    ("nieuw", 9, 1),
]

for soort, aantal, verwacht in gevallen:
    if soort == "naslagwerk":
        weken = None
    else:
        if soort == "nieuw":
            weken = WEKEN_NIEUW
        else:
            weken = WEKEN_GEWOON

        if aantal > DRUKKE_LENER:
            weken -= 1
        if weken < MINIMUM_WEKEN:
            weken = MINIMUM_WEKEN

    teken = "ok" if weken == verwacht else "FOUT"
    tekst = "niet uitleenbaar" if weken is None else f"{weken} weken"
    print(f"{soort:<12}{aantal:>2} boeken -> {tekst:<18}{teken}")
```

```text
gewoon       1 boeken -> 4 weken           ok
nieuw        1 boeken -> 2 weken           ok
naslagwerk   1 boeken -> niet uitleenbaar  ok
gewoon       3 boeken -> 4 weken           ok
gewoon       4 boeken -> 3 weken           ok
nieuw        4 boeken -> 1 weken           ok
naslagwerk   9 boeken -> niet uitleenbaar  ok
nieuw        9 boeken -> 1 weken           ok
```

**De vijf beslissingen die je moest nemen.**

**Het naslagwerk als bewakingsclausule.** Het staat bovenaan en de rest van de
redenering geldt er niet voor. Zou je het als `elif` onderaan zetten, dan moest
je bij elke andere regel een uitzondering inbouwen. Handel bijzondere gevallen
altijd eerst af.

**`None` als "niet van toepassing".** Nul weken zou betekenen "je mag het
meenemen maar moet het meteen terugbrengen". Dat is niet hetzelfde als "je mag
het niet meenemen". Hier is `None` het juiste antwoord, precies zoals in 5.8.

**`>` en niet `>=`.** "Meer dan 3" is `> 3`. Zie de testrijen met 3 en 4: die
staan er precies om dit vast te leggen.

**Het minimum als eigen regel.** Bij de huidige getallen doet die regel niets:
4 min 1 is 3, en 2 min 1 is 1. Toch hoort hij er. Voegt de club morgen een
categorie met één week toe, dan zakt die zonder deze regel naar nul. Zet er
commentaar bij waarom hij er staat.

**De extra testrij.** De laatste rij, `("nieuw", 9, 1)`, stond niet in de tabel
van oefening 3.1. Ze test of de aftrek maar één keer gebeurt, en niet per boek
boven de drie. Uit de opgave blijkt dat: er staat "1 week minder", niet "per
boek 1 week minder". Wie dat anders leest, bouwt iets anders. Vraag het na als
het niet duidelijk is.

**De schoonheidsfout in de uitvoer.** Er staat "1 weken". Dat is taalkundig
fout. Los het op met een verkorte keuze:

```python
weken = 1
eenheid = "week" if weken == 1 else "weken"
print(f"{weken} {eenheid}")
```

```text
1 week
```
