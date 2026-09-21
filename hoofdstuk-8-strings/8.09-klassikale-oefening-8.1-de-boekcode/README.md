<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 8.1 — De boekcode

Uit *Python basis — theoriebundel*, hoofdstuk 8 (Strings), paragraaf 8.9.

| Bestand | Deel | Opmerking |
|---|---|---|
| `uitwerking-a.py` | uitwerking |  |
| `uitwerking-b-voor-alle-drie-de-boeken.py` | uitwerking |  |

## Opgave

**De situatie.** De club geeft elk boek een code. De regels:

- De eerste drie letters van de achternaam van de schrijver, in hoofdletters.
- Een streepje.
- De eerste letter van elk woord van de titel, in hoofdletters, zonder de
  lidwoorden `de`, `het`, `een` en `van`.
- Een streepje.
- Het jaartal.

Voorbeeld: Harry Mulisch, *De ontdekking van de hemel*, 1992 wordt `MUL-OH-1992`.

**Wat je doet.** Schrijf een programma dat de code maakt voor deze drie boeken:

```text
Harry Mulisch      | De ontdekking van de hemel | 1992
Herman Koch        | Het diner                  | 2009
Jan Wolkers        | Turks fruit                | 1969
```

Werk met de gegevens als losse variabelen; lijsten komen in hoofdstuk 12.

## Uitwerking

```python
# De Leeslamp — de boekcode
# Cursus Python basis, hoofdstuk 8, oefening 1

LIDWOORDEN = "de het een van"

schrijver = "Harry Mulisch"
titel = "De ontdekking van de hemel"
jaar = 1992

# 1 — de eerste drie letters van de achternaam
achternaam = schrijver.split(" ", 1)[1]
deel_schrijver = achternaam[:3].upper()

# 2 — de beginletters van de titel, zonder de lidwoorden
deel_titel = ""
for woord in titel.split():
    if woord.lower() not in LIDWOORDEN.split():
        deel_titel = deel_titel + woord[0].upper()

# 3 — samenvoegen
code = f"{deel_schrijver}-{deel_titel}-{jaar}"
print(code)
```

```text
MUL-OH-1992
```

**Voor alle drie de boeken**, met een lus die je in hoofdstuk 10 echt leert
maar hier al leesbaar is:

```python
LIDWOORDEN = ["de", "het", "een", "van"]

boeken = [
    ("Harry Mulisch", "De ontdekking van de hemel", 1992),
    ("Herman Koch", "Het diner", 2009),
    ("Jan Wolkers", "Turks fruit", 1969),
]

for schrijver, titel, jaar in boeken:
    achternaam = schrijver.split(" ", 1)[1]
    deel_schrijver = achternaam[:3].upper()

    deel_titel = ""
    for woord in titel.split():
        if woord.lower() not in LIDWOORDEN:
            deel_titel += woord[0].upper()

    print(f"{titel:<30}{deel_schrijver}-{deel_titel}-{jaar}")
```

```text
De ontdekking van de hemel    MUL-OH-1992
Het diner                     KOC-D-2009
Turks fruit                   WOL-TF-1969
```

**De vier plaatsen waar het misgaat.**

**De achternaam eruit halen.** `schrijver.split(" ", 1)[1]` splitst op de eerste
spatie en neemt het tweede stuk. Zou je `.split()[1]` schrijven zonder de `1`,
dan gaat het mis bij "Jan van het Wolkers": dan krijg je `van`. Met de `1` blijft
alles na de eerste spatie samen.

**De vergelijking in kleine letters.** `woord.lower() not in LIDWOORDEN` en niet
`woord not in LIDWOORDEN`. Zonder `.lower()` glipt `De` erdoor, want dat staat
niet in de lijst; alleen `de` staat er.

**De drieletterafkapping.** `achternaam[:3]` geeft `MUL`. Bij een achternaam van
twee letters, zoals *Bo*, geeft het gewoon `BO` in plaats van een fout. Dat is
het gedrag van snijden uit 8.3, en hier komt het je goed uit.

**Het jaartal in de f-string.** `jaar` is een `int`, geen `str`. In een f-string
maakt dat niet uit: die zet elke waarde vanzelf om. Zou je `+` gebruiken, dan
kreeg je een `TypeError`.

**Waarom de lidwoordenlijst een constante is.** Voegt de club morgen `der` toe,
dan pas je één regel aan. En de naam `LIDWOORDEN` legt uit waarom die vier
woorden bij elkaar staan; de losse lijst midden in een `if` zou dat niet doen.
