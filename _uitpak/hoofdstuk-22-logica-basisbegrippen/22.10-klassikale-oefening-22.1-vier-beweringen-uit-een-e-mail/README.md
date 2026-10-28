<!-- gemaakt met gereedschap/theorie-uitpakken.py uit de cursusmap pythonbasis -->
# Klassikale oefening 22.1 — Vier beweringen uit een e-mail

Uit *Python basis — theoriebundel*, hoofdstuk 22 (Logica en kritisch denken: de basisbegrippen), paragraaf 22.10.

Deze oefening heeft geen code. Het antwoord is de redenering hieronder.

## Opgave

**De situatie.** De voorzitter van De Leeslamp stuurt deze e-mail naar het
bestuur.

> Beste allen,
>
> De ledenadministratie moet dringend vervangen worden. Vorige week is het
> programma twee keer vastgelopen, en Jan zegt dat het bij hem ook niet meer
> werkt. Elk modern systeem draait tegenwoordig in de cloud, dus daar moeten wij
> ook naartoe. Als we nu niets doen, verliezen we leden.
>
> Het huidige systeem is trouwens gebouwd door een stagiair.

**Wat je doet.**

1. Haal er alle beweringen uit, en zet naast elke bewering of ze toetsbaar is.
2. Schrijf het hoofdargument in standaardvorm.
3. Benoem de verzwegen premissen.
4. Wijs de drogredenen aan.
5. Formuleer wat je zou moeten weten vóór je hierover kunt beslissen.

## Uitwerking

**1. De beweringen.**

| Nr. | Bewering | Toetsbaar? |
|---|---|---|
| 1 | De ledenadministratie moet dringend vervangen worden | Nee zoals ze er staat; dit is de conclusie, geen waarneming |
| 2 | Het programma is vorige week twee keer vastgelopen | Ja, met het logboek |
| 3 | Jan zegt dat het bij hem niet meer werkt | Ja, dát Jan dat zegt. Niet hetzelfde als dat het zo is |
| 4 | Elk modern systeem draait in de cloud | Ja, en het is onwaar. "Elk" is een sterke claim |
| 5 | Als we niets doen, verliezen we leden | In principe wel, maar er is geen enkel gegeven aangeleverd |
| 6 | Het systeem is gebouwd door een stagiair | Ja, en het is niet ter zake |

**2. Het argument in standaardvorm.**

| Regel | Bewering |
|---|---|
| P1 | Het programma liep vorige week twee keer vast |
| P2 | Bij Jan werkt het niet meer |
| P3 | Moderne systemen draaien in de cloud |
| P4 | Zonder ingrijpen verliezen we leden |
| C | De ledenadministratie moet vervangen worden |

**3. De verzwegen premissen.** Dit is het interessantste deel.

| Nr. | Wat er verzwegen wordt |
|---|---|
| 1 | Twee storingen in een week zijn abnormaal veel |
| 2 | Die storingen komen door het systeem en niet door de omgeving of de invoer |
| 3 | Een storing herstellen is niet mogelijk of niet goedkoper dan vervangen |
| 4 | Wat "in de cloud" heet, lost déze storingen op |
| 5 | Leden vertrekken om deze reden en niet om een andere |

Premisse 3 is de belangrijkste, en ze wordt nergens genoemd: het hele argument
gaat over vervangen, terwijl herstellen niet eens overwogen is.

**4. De drogredenen.**

| Wat | Waar |
|---|---|
| Autoriteit, in de vorm "iedereen doet het" | "Elk modern systeem draait in de cloud" |
| Persoonsargument | "Gebouwd door een stagiair." Wie het schreef, zegt niets over of het werkt |
| Vals dilemma | "Als we nu niets doen" veronderstelt twee opties: alles vervangen of niets |
| Zwakke inductie | Twee storingen en één melding dragen geen conclusie over het hele systeem |

**5. Wat je zou moeten weten.**

| Vraag | Waarom |
|---|---|
| Wat stond er in het logboek bij die twee storingen | Zonder de oorzaak is elke oplossing giswerk |
| Hoeveel storingen waren er in de maanden ervoor | Twee is veel of weinig, afhankelijk van het gemiddelde |
| Wat gebeurt er precies bij Jan, op zijn scherm | "Werkt niet" is geen foutbeschrijving |
| Welke leden zijn om deze reden vertrokken | Anders is P4 een vermoeden |
| Wat kost herstellen tegenover vervangen | De vergelijking die het argument overslaat |

**Wat deze oefening je leert.** De e-mail is niet dom. Er kan een goede reden
zijn om het systeem te vervangen. Maar deze e-mail toont die reden niet aan, en
het verschil tussen "waarschijnlijk terecht" en "aangetoond" is precies waar dit
hoofdstuk over gaat.
