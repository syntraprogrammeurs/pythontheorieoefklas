<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 20.1 — De trendkaart

Uit *Python basis — theoriebundel*, hoofdstuk 20 (Trends in programmeren), paragraaf 20.6.

Deze oefening heeft geen code. Het antwoord is de redenering hieronder.

## Opgave

**De situatie.** Je krijgt zes uitspraken die je in de vakpers tegenkomt. Je
beoordeelt ze met de zes vragen uit 20.5.

De uitspraken:

1. "Objectgeoriënteerd programmeren is achterhaald; functioneel is de toekomst."
2. "Binnen vijf jaar schrijft niemand nog zelf code."
3. "Elk nieuw project hoort in TypeScript in plaats van in JavaScript."
4. "Je moet alles in containers draaien."
5. "Testen kost meer dan het opbrengt."
6. "Python is te traag voor echt werk."

**Wat je doet.** Kies er drie. Beantwoord per uitspraak de zes vragen, en formuleer
daarna in twee zinnen je eigen standpunt. Dat standpunt mag "hangt ervan af"
zijn, op voorwaarde dat je zegt **waarvan**.

## Uitwerking

Hieronder drie uitgewerkte antwoorden. Je eigen antwoord mag afwijken, zolang je
de vragen beantwoordt.

**Uitspraak 2: "Binnen vijf jaar schrijft niemand nog zelf code."**

| Vraag | Antwoord |
|---|---|
| Welk probleem lost het op | Code schrijven is traag en foutgevoelig. Dat klopt |
| Wat is het alternatief | Zelf schrijven, met assistentie. Dat is wat er nu gebeurt |
| Wie betaalt ervoor | Bedrijven die dit gereedschap verkopen, doen deze uitspraak het vaakst |
| Hoeveel bewijs | Veel demo's, weinig cijfers over onderhoud op lange termijn |
| Wat kost het om ervanaf te stappen | Als je team niet meer kan lezen wat het oplevert: veel |
| Wat als het overwaait | Dezelfde voorspelling werd gedaan bij CASE-tools in de jaren tachtig en bij low-code in de jaren tien |

**Standpunt.** De verhouding tussen typen en nadenken verschuift, en typen wordt
minder werk. Maar iemand moet nog altijd bepalen wát er moet gebeuren en
vaststellen of het klopt, en dat is het moeilijke deel van dit vak.

**Uitspraak 5: "Testen kost meer dan het opbrengt."**

| Vraag | Antwoord |
|---|---|
| Welk probleem | Tests schrijven kost tijd die je aan functies kunt besteden. Dat is waar |
| Wat is het alternatief | Handmatig testen, of niet testen |
| Wie betaalt ervoor | Wie een deadline heeft, zegt dit het vaakst |
| Hoeveel bewijs | De tabel in 20.4 over de kostprijs per moment is goed onderzocht |
| Wat kost het om ervanaf te stappen | Tests weglaten is gratis; ze later toevoegen aan bestaande code is duur |
| Wat als het overwaait | Deze discussie loopt al dertig jaar en overwaait niet |

**Standpunt.** Het hangt af van de levensduur. Voor een script dat je één keer
draait, is testen inderdaad verspilling. Voor code die een jaar meegaat en door
anderen wordt aangepast, verdient elke test zich meermaals terug.

**Uitspraak 6: "Python is te traag voor echt werk."**

| Vraag | Antwoord |
|---|---|
| Welk probleem | Python is inderdaad tientallen keren trager dan C |
| Wat is het alternatief | C, Rust, Go. Die zijn sneller en kosten meer ontwikkeltijd |
| Wie betaalt ervoor | Meestal iemand die van een compilerende taal komt |
| Hoeveel bewijs | Metingen kloppen. De vraag is of die traagheid ergens toe doet |
| Wat kost het om ervanaf te stappen | Herschrijven in een andere taal is duur |
| Wat als het overwaait | De discussie bestaat sinds Python bestaat |

**Standpunt.** Het hangt af van waar je tijd naartoe gaat. Wacht je programma op
een databank of op het netwerk, dan is de snelheid van de taal irrelevant.
Reken je in een lus over miljoenen getallen, dan is ze doorslaggevend, en dan
gebruik je een bibliotheek die in C geschreven is.

En vergeet niet: een slimmere aanpak wint meer dan een snellere taal. Een goed
algoritme in Python verslaat een slecht algoritme in C.

**Wat deze oefening je leert.** Alle drie de antwoorden beginnen met "het hangt
ervan af" en zeggen daarna **waarvan**. Dat is het verschil tussen een
nietszeggend en een bruikbaar antwoord.
