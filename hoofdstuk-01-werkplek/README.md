<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Hoofdstuk 1 — Je Python-werkplek professioneel opzetten

De code uit hoofdstuk 1 van *Python basis — theoriebundel*, genummerd zoals in de bundel.

## Voorbeelden uit de uitleg

| Paragraaf | Bestand | Opmerking |
|---|---|---|
| 1.9 Het projectbestand pyproject.toml | `1.09-pyproject.toml` | instellingenbestand |
| 1.10 De instellingen van de werkruimte | `1.10-settings.json` | instellingenbestand |
| 1.11 Je eerste bestand | `1.11a-je-eerste-bestand.py` |  |
| 1.11 Je eerste bestand | `1.11b-je-eerste-bestand.py` |  |
| 1.13 De debugger | `1.13a-de-debugger.py` |  |
| 1.13 De debugger | `1.13b-launch.json` | instellingenbestand |

## Klassikale oefeningen

| Oefening | Map | Bestanden |
|---|---|---|
| 1.1 — Een tweede project met een eigen omgeving | [1.16-klassikale-oefening-1.1-een-tweede-project-met-een-eigen](1.16-klassikale-oefening-1.1-een-tweede-project-met-een-eigen/) | `pyproject.toml`, `.vscode/settings.json`, `main.py` |
| 1.2 — Een fout opsporen met de debugger | [1.17-klassikale-oefening-1.2-een-fout-opsporen-met-de-debugger](1.17-klassikale-oefening-1.2-een-fout-opsporen-met-de-debugger/) | `opgave.py`, `uitwerking-de-herstelde-versie.py` |

## Commando's uit de uitleg

**1.2 Python installeren — Linux**

```bash
sudo apt update
sudo apt install python3 python3-venv python3-pip
```

**1.3 Controleren of het werkt**

```bash
python --version
```

```bash
python3 --version
```

**1.4 Visual Studio Code installeren**

```bash
code --version
```

**1.5 Git installeren**

```bash
git config --global user.name "Jouw Naam"
git config --global user.email "jouw.adres@voorbeeld.be"
git config --global init.defaultBranch main
```

```bash
git config --global --list
```

**1.7 Je projectmap en de naamafspraken**

```bash
cd ~
mkdir python-basis
cd python-basis
mkdir leeslamp
cd leeslamp
code .
```

**1.8 De virtuele omgeving**

```bash
python -m venv .venv
```

```bash
python -c "import sys; print(sys.executable)"
```

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

**1.12 Je programma uitvoeren**

```bash
python main.py
```
