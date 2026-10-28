<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 21.1 — Van jouw laptop naar de lezer

Uit *Python basis — theoriebundel*, hoofdstuk 21 (DevOps, en waar Git daarin past), paragraaf 21.12.

Deze oefening heeft geen code. Het antwoord is de redenering hieronder.

## Opgave

**De situatie.** De Leeslamp wil haar ledenbeheer als website. Jij hebt het
programma geschreven. Vanaf nu moet het bij tweehonderd leden draaien, en moet
het blijven draaien.

**Wat je doet.** Teken op het bord de weg die één wijziging aflegt: van het
moment dat jij een regel typt tot het moment dat een lid het resultaat ziet.
Zet bij elke stap drie dingen: wie of wat de stap uitvoert, hoe lang die duurt,
en welke soort fout daar gevonden kan worden.

Bespreek daarna: welke stap zou je als eerste automatiseren, en waarom die en
niet een andere?

## Uitwerking

De keten, in acht stappen.

| Nr. | Stap | Wie of wat | Duur | Welke fout hier gevonden wordt |
|---|---|---|---|---|
| 1 | Typen en opslaan | Jij, in VS Code | seconden | Tikfouten, door Ruff en Pylance |
| 2 | Lokaal draaien | Jij | seconden | Denkfouten in wat je net schreef |
| 3 | `git commit` | Jij | seconden | Geen; dit legt vast |
| 4 | `git push` | Jij | seconden | Geen; dit deelt |
| 5 | Pijplijn: installeren, linten, testen | GitHub Actions | 1 tot 3 minuten | Ontbrekende afhankelijkheid, stijlfout, gebroken test, "werkt alleen op mijn machine" |
| 6 | Beoordeling door een collega | Een mens | uren tot een dag | Onbegrijpelijke code, verkeerde aanpak, ontbrekend geval |
| 7 | Uitrollen naar acceptatie | Pijplijn, met een knop | minuten | Fouten in wat de klant bedoelde |
| 8 | Uitrollen naar productie, en monitoren | Pijplijn plus toezicht | minuten, daarna doorlopend | Wat niemand voorzien had: belasting, rare invoer, uitval |

**Wat de tabel laat zien.** De duur springt tussen stap 5 en 6 van minuten naar
uren. Dat is geen toeval: stap 6 is de enige stap waar een mens moet wachten op
een andere mens.

**Welke stap eerst automatiseren?**

Het gebruikelijke antwoord is "het testen", en dat is niet het beste antwoord.
Beter is: **de stap die je het vaakst met de hand doet en waar het vaakst iets
misgaat**. Voor de meeste beginnende teams is dat stap 8, het uitrollen.

| Kandidaat | Hoe vaak per week | Wat er misgaat als een mens het doet |
|---|---|---|
| Stap 1 en 2, linten en draaien | tientallen keren | Weinig; het is al snel en de linter helpt al |
| Stap 5, testen | tientallen keren | Iemand vergeet ze te draaien. Dit hoort inderdaad automatisch |
| Stap 8, uitrollen | een- tot enkele keren | Een vergeten bestand, een verkeerde volgorde, een ontbrekende instelling. En het gebeurt onder tijdsdruk |

**Het antwoord met de redenering erbij.** Automatiseer stap 5 eerst, want het
is het goedkoopst en het gebeurt het vaakst. Automatiseer stap 8 als tweede,
want daar zijn de fouten het duurst en gebeurt het met de hand onder de meeste
stress.

Stap 6 automatiseer je nooit. Een mens die je code leest, vindt een andere soort
fout dan een computer: hij vindt wat er ontbreekt.

**De vraag die vaak terugkomt.** "Waarom stap 2 én stap 5, dat is toch dubbel?"
Nee. Stap 2 draait op jouw computer, met jouw pakketten. Stap 5 draait op een
lege computer, met alleen wat in de repository staat. Dat is precies het
verschil dat je wilt meten.
