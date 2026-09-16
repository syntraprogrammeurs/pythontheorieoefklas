<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 1.1 — Een tweede project met een eigen omgeving

Uit *Python basis — theoriebundel*, hoofdstuk 1 (Je Python-werkplek professioneel opzetten), paragraaf 1.16.

| Bestand | Deel | Opmerking |
|---|---|---|
| `pyproject.toml` | uitwerking | instellingenbestand |
| `.vscode/settings.json` | uitwerking | instellingenbestand |
| `main.py` | uitwerking |  |

## Opgave

**De situatie.** Je krijgt een tweede opdracht binnen: een klein programma voor
de boekenlijst van de club. Dat wordt een apart project. Je zet het volledig op
volgens de afspraken van dit hoofdstuk, zonder de tekst terug te lezen.

**Wat je maakt.**

1. Een map `boekenlijst`, naast `leeslamp`.
2. Een eigen virtuele omgeving in die map.
3. Een `pyproject.toml` met een regellengte van **100** in plaats van 88.
4. Een `.vscode/settings.json` waarin de liniaal op diezelfde 100 staat.
5. Een bestand `main.py` dat de drie boeken hieronder toont, en het aantal.

```text
De ontdekking van de hemel
Het diner
Turks fruit
```

6. Toon achteraf met een commando dat je in de juiste virtuele omgeving zit.

## Uitwerking

```bash
cd ~/python-basis
mkdir boekenlijst
cd boekenlijst
python -m venv .venv
code .
```

Activeer de omgeving, of open een nieuwe terminal in VS Code: die activeert
haar vanzelf.

`pyproject.toml`:

```toml
[project]
name = "boekenlijst"
version = "0.1.0"
requires-python = ">=3.14"

[tool.ruff]
line-length = 100
target-version = "py314"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B", "SIM"]

[tool.ruff.format]
quote-style = "double"
```

`.vscode/settings.json`:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv",
  "[python]": {
    "editor.defaultFormatter": "charliermarsh.ruff",
    "editor.formatOnSave": true
  },
  "editor.rulers": [100]
}
```

`main.py`:

```python
boeken = ["De ontdekking van de hemel", "Het diner", "Turks fruit"]

for boek in boeken:
    print(boek)

print(f"Aantal boeken: {len(boeken)}")
```

De controle:

```bash
python -c "import sys; print(sys.executable)"
```

Het pad moet eindigen op `boekenlijst/.venv/bin/python`, of op Windows op
`boekenlijst\.venv\Scripts\python.exe`.

**Waarom twee aparte omgevingen voor twee kleine projecten?** Omdat de gewoonte
telt, niet de grootte. Het derde project heeft wél pakketten nodig, en dan is de
gewoonte er al. Bovendien zie je hier meteen dat de regellengte per project
verschilt: dat is precies waarom die instelling in het project staat en niet in
je persoonlijke instellingen.
