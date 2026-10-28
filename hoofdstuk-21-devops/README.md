<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Hoofdstuk 21 — DevOps, en waar Git daarin past

De code uit hoofdstuk 21 van *Python basis — theoriebundel*, genummerd zoals in de bundel.

## Voorbeelden uit de uitleg

| Paragraaf | Bestand | Opmerking |
|---|---|---|
| 21.4 Continue integratie | `21.04-controle.yml` | instellingenbestand |
| 21.5 Wat die pijplijn dan precies draait | `21.05a-wat-die-pijplijn-dan-precies-draait.py` |  |
| 21.5 Wat die pijplijn dan precies draait | `21.05b-wat-die-pijplijn-dan-precies-draait.py` | loopt met opzet vast |
| 21.8 Monitoren: weten wat er gebeurt | `21.08-monitoren-weten-wat-er-gebeurt.py` |  |

## Klassikale oefeningen

| Oefening | Map | Bestanden |
|---|---|---|
| 21.1 — Van jouw laptop naar de lezer | [21.12-klassikale-oefening-21.1-van-jouw-laptop-naar-de-lezer](21.12-klassikale-oefening-21.1-van-jouw-laptop-naar-de-lezer/) | alleen de README |
| 21.2 — De pijplijn beoordelen | [21.13-klassikale-oefening-21.2-de-pijplijn-beoordelen](21.13-klassikale-oefening-21.2-de-pijplijn-beoordelen/) | `opgave-uitrol.yml`, `uitwerking-uitrol.yml` |

## Commando's uit de uitleg

**21.4 Continue integratie**

```bash
# alles wat in deze virtuele omgeving zit, met exacte versies
pip freeze > requirements.txt

# en op een andere computer, of in de pijplijn:
pip install -r requirements.txt
```

**21.5 Wat die pijplijn dan precies draait**

```bash
python controle.py
echo $?          # macOS en Linux
echo $LASTEXITCODE   # Windows PowerShell
```

**21.16 Wat je nu kunt**

```bash
git add ontwerp/uitrolketen.md .github/workflows/controle.yml
git commit -m "Teken de uitrolketen en voeg een eerste CI-controle toe"
git push
```
