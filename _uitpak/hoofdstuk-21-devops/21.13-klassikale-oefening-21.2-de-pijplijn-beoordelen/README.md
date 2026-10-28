<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 21.2 — De pijplijn beoordelen

Uit *Python basis — theoriebundel*, hoofdstuk 21 (DevOps, en waar Git daarin past), paragraaf 21.13.

| Bestand | Deel | Opmerking |
|---|---|---|
| `opgave-uitrol.yml` | opgave | instellingenbestand |
| `uitwerking-uitrol.yml` | uitwerking | instellingenbestand |

## Opgave

**De situatie.** Een stagiair heeft de pijplijn hieronder geschreven en vraagt
je erover mee te kijken vóór hij hem in gebruik neemt.

```yaml
# .github/workflows/uitrol.yml
name: Uitrol

on: [push]

jobs:
  uitrollen:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Python
        run: pip install ruff requests flask

      - name: Tests
        run: python controle.py || true

      - name: Naar productie
        run: scp -r . server:/var/www/leeslamp
```

**Wat je doet.** Zoek zo veel mogelijk problemen. Zeg per probleem wat er kan
misgaan, hoe erg dat is, en wat je in de plaats zet. Herschrijf daarna het
bestand.

## Uitwerking

Er zitten er zes in, en de eerste twee zijn de ernstigste.

| Nr. | Probleem | Wat er misgaat |
|---|---|---|
| 1 | `\|\| true` achter de tests | De stap slaagt altijd, ook als de tests falen. De pijplijn is versiering geworden |
| 2 | Elke push gaat naar productie | Ook een halve gedachte, ook een experiment, ook een tikfout |
| 3 | Geen versies bij de pakketten | `pip install flask` haalt vandaag iets anders binnen dan volgende maand. Dan faalt de pijplijn zonder dat er code veranderde |
| 4 | De pakketten staan in het YAML-bestand | Ze horen in `requirements.txt`, zodat je lokaal en in de pijplijn hetzelfde installeert |
| 5 | Geen linter | Ruff is geïnstalleerd maar wordt nooit gedraaid |
| 6 | `scp -r .` kopieert alles | Ook `.git`, ook `.venv`, ook een `.env` met wachtwoorden erin. Dat laatste is een lek |

**Waarom nummer 1 het ergste is.** Een pijplijn die nooit rood wordt, is
schadelijker dan geen pijplijn. Zonder pijplijn weet iedereen dat er niet getest
is. Met deze pijplijn denkt iedereen van wel. Vals vertrouwen is erger dan geen
vertrouwen.

**Waarom nummer 6 er zo onschuldig uitziet.** `scp -r .` betekent "kopieer alles
in deze map". Dat leest als handig en betekent in de praktijk dat je
geschiedenis, je virtuele omgeving en je geheimen op een webserver komen te
staan. Het is dezelfde fout als een `.gitignore` vergeten, uit hoofdstuk 2, maar
dan met erger gevolg.

**De herschreven pijplijn.**

```yaml
# .github/workflows/uitrol.yml
name: Controle en uitrol

on:
  push:
  workflow_dispatch:        # met de hand te starten voor de uitrol

jobs:
  controleren:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.14"

      - name: Afhankelijkheden
        run: pip install -r requirements.txt

      - name: Linter
        run: ruff check .

      - name: Opmaak
        run: ruff format --check .

      - name: Tests
        run: python controle.py

  uitrollen:
    needs: controleren                       # alleen als de controle slaagde
    if: github.event_name == 'workflow_dispatch'
    runs-on: ubuntu-latest
    environment: productie                   # vraagt om goedkeuring
    steps:
      - uses: actions/checkout@v4
      - name: Naar productie
        run: rsync -a --exclude-from=.deployignore . server:/var/www/leeslamp
```

**Wat er veranderde, en waarom.**

| Wijziging | Waarom |
|---|---|
| `\|\| true` weg | Een falende test hoort de pijplijn te stoppen |
| Twee taken in plaats van één | Controleren gebeurt altijd, uitrollen alleen bewust |
| `needs: controleren` | Uitrollen kan niet gebeuren als de controle rood staat |
| `workflow_dispatch` en `environment` | Een mens drukt op de knop. Dit is continue levering, geen continue uitrol |
| `requirements.txt` met vaste versies | Lokaal en in de pijplijn hetzelfde, vandaag en volgend jaar |
| `ruff check` en `ruff format --check` | De linter draaien in plaats van alleen installeren |
| `rsync` met een uitsluitingslijst | Alleen wat er hoort te staan gaat mee |

**De vraag die de groep hier altijd stelt.** "Mag `\|\| true` dan nooit?" Er is
één geval waarin het verdedigbaar is: een nieuwe controle die je invoert op een
bestaand project, waar je eerst wilt zien hoeveel er zou falen vóór je hem
verplicht maakt. Dan zet je erbij hoe lang dat tijdelijk is, en dan houd je je
daaraan.
