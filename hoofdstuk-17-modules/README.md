<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Hoofdstuk 17 — Modules, de standaardbibliotheek en `pip`

De code uit hoofdstuk 17 van *Python basis — theoriebundel*, genummerd zoals in de bundel.

## Voorbeelden uit de uitleg

| Paragraaf | Bestand | Opmerking |
|---|---|---|
| 17.1 Importeren | `17.01a-importeren.py` |  |
| 17.1 Importeren — De vier vormen | `17.01b-de-vier-vormen.py` |  |
| 17.2 De standaardbibliotheek — random | `17.02a-random.py` |  |
| 17.2 De standaardbibliotheek — datetime | `17.02b-datetime.py` |  |
| 17.2 De standaardbibliotheek — statistics en collections | `17.02c-statistics-en-collections.py` |  |
| 17.3 Je eigen module | `17.03-je-eigen-module/berekeningen.py` |  |
| 17.3 Je eigen module | `17.03-je-eigen-module/main.py` |  |
| 17.3 Je eigen module | `17.03-je-eigen-module/main_met_from_import.py` |  |
| 17.4 if __name__ == "__main__" | `17.04-if-name-dubbel-is-main.py` |  |
| 17.6 Het raadspel, nu met echt toeval | `17.06a-het-raadspel-nu-met-echt-toeval.py` |  |
| 17.6 Het raadspel, nu met echt toeval | `17.06b-het-raadspel-nu-met-echt-toeval.py` | vraagt invoer |

## Klassikale oefeningen

| Oefening | Map | Bestanden |
|---|---|---|
| 17.1 — De uitleentermijn met echte datums | [17.07-klassikale-oefening-17.1-de-uitleentermijn-met-echte-datums](17.07-klassikale-oefening-17.1-de-uitleentermijn-met-echte-datums/) | `uitwerking.py` |
| 17.2 — De boekentombola | [17.08-klassikale-oefening-17.2-de-boekentombola](17.08-klassikale-oefening-17.2-de-boekentombola/) | `uitwerking.py` |

## Commando's uit de uitleg

**17.5 Pakketten installeren met pip**

```bash
python -m pip install requests
python -m pip list
python -m pip show requests
python -m pip uninstall requests
```

```bash
python -m pip freeze > requirements.txt
python -m pip install -r requirements.txt
```

**17.11 Wat je nu kunt**

```bash
git add main.py berekeningen.py requirements.txt
git commit -m "Deel het project op in modules en gebruik random en datetime"
git push
```
