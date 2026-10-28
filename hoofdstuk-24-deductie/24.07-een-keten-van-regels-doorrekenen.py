# Python basis — theoriebundel
# Hoofdstuk 24 — Deductie: syllogismen, geldigheid en argumentvormen
# 24.7 Een keten van regels doorrekenen
#
# Als je regels als implicaties opschrijft en er feiten bij hebt, kun je modus ponens
# herhaald toepassen tot er niets nieuws meer bij komt. Dat heet voorwaarts ketenen,
# en het is de kern van elke regelmachine.

# Het idee in het kort:
#   - Een REGEL is een implicatie: "als al deze voorwaarden gelden, dan geldt ook
#     dit gevolg".
#   - Een FEIT is iets waarvan je weet dat het waar is.
#   - MODUS PONENS (24.2): als p -> q geldt en p is waar, dan is q waar.
#   - VOORWAARTS KETENEN: modus ponens steeds opnieuw toepassen. Een gevolg dat je
#     net afleidde, is meteen een nieuw feit, en kan zo een volgende regel laten
#     vuren. Je stopt pas als een volledige ronde niets nieuws meer oplevert.

# De Leeslamp — regels afleiden met herhaalde modus ponens
# REGELS is een lijst van tuples (hoofdstuk 13). Elke tuple heeft twee delen:
#   ({voorwaarde, voorwaarde, ...}, gevolg)
# De voorwaarden staan in een SET (hoofdstuk 13): de volgorde speelt geen rol, en
# een set kun je snel vergelijken met een andere set.
# Een feit is hier gewoon een string, zoals "geschorst".
# De hoofdletters in REGELS zijn de afspraak voor een "constante" (hoofdstuk 5).
REGELS = [
    # geschorst -> mag_niet_lenen
    ({"geschorst"}, "mag_niet_lenen"),
    # onbetaald -> mag_niet_lenen  (een tweede, losse reden voor hetzelfde gevolg)
    ({"onbetaald"}, "mag_niet_lenen"),
    # boek_te_laat -> onbetaald  (wie een boek te laat heeft, heeft een boete open)
    ({"boek_te_laat"}, "onbetaald"),
    # (mag_niet_lenen EN wil_lenen) -> toon_waarschuwing
    # Twee voorwaarden in de set betekent: ze moeten ALLEBEI gelden.
    ({"mag_niet_lenen", "wil_lenen"}, "toon_waarschuwing"),
]


# leid_af() krijgt de startfeiten en de regels mee, en geeft twee dingen terug:
#   bekend  -> de set van ALLES wat waar is: de startfeiten plus wat eruit volgt
#   stappen -> een lijst van (voorwaarden, gevolg): welke regel vuurde, in welke
#              volgorde. Zo kun je de redenering achteraf nalezen.
def leid_af(feiten, regels):
    """Past modus ponens toe tot er niets nieuws meer bij komt."""
    # set(feiten) maakt een NIEUWE set. Je past de set van de aanroeper dus niet
    # aan: dat is het verschil tussen kopie en verwijzing uit hoofdstuk 14.
    bekend = set(feiten)
    stappen = []
    # nieuw zegt: "kwam er in de vorige ronde iets bij?". Op True zetten zorgt
    # ervoor dat de while-lus (hoofdstuk 10) minstens één keer draait.
    nieuw = True
    while nieuw:
        # Aan het begin van elke ronde: nog niets nieuws gevonden.
        nieuw = False
        # Elke regel uitpakken in zijn twee delen.
        for voorwaarden, gevolg in regels:
            # voorwaarden <= bekend: bij sets betekent <= "is een DEELVERZAMELING
            # van". Dus: staan ALLE voorwaarden van deze regel bij wat we al weten?
            # Dat is de "p is waar"-premisse van modus ponens.
            # gevolg not in bekend: alleen toevoegen wat we nog niet wisten.
            # Zonder deze controle zou elke ronde dezelfde regel opnieuw vuren,
            # en zou de lus nooit stoppen.
            if voorwaarden <= bekend and gevolg not in bekend:
                # Modus ponens: de voorwaarden gelden, dus het gevolg ook.
                bekend.add(gevolg)
                # sorted() maakt van de set een gesorteerde LIJST. Een set heeft
                # geen vaste volgorde; zo is de uitvoer elke keer dezelfde.
                stappen.append((sorted(voorwaarden), gevolg))
                # Er kwam iets bij: dus nog een ronde. Misschien vuurt er nu een
                # regel die eerst nog niet kon.
                nieuw = True
    # Hier was een hele ronde zonder nieuwe feiten: verder komt er niets meer bij.
    # Deze lus stopt altijd: er zijn maar zoveel gevolgen als er regels zijn, en
    # elk gevolg komt er hooguit één keer bij.
    return bekend, stappen


# De startfeiten: dit lid heeft een boek te laat en wil iets lenen.
start = {"boek_te_laat", "wil_lenen"}
# De twee terugkeerwaarden meteen uitpakken in twee variabelen.
bekend, stappen = leid_af(start, REGELS)

print("Gegeven:", sorted(start))
print()
# Het SPOOR van de redenering: elke stap is één keer modus ponens.
# Merk op: boek_te_laat -> onbetaald -> mag_niet_lenen is een keten van twee
# implicaties. Dat is het HYPOTHETISCH SYLLOGISME uit 24.4 (p -> q, q -> r, dus
# p -> r). Niemand heeft die keten opgeschreven; het programma legt ze zelf.
for voorwaarden, gevolg in stappen:
    print(f"  uit {voorwaarden} volgt: {gevolg}")
print()
# Alles wat waar is, startfeiten inbegrepen, alfabetisch gesorteerd.
print("Alles wat volgt:", sorted(bekend))

# Waarom dit meer is dan een aardig programmaatje (24.7): de REGELS staan los van
# de AFLEIDING. Wil je een regel bijzetten, dan voeg je één regel toe aan de lijst
# en blijft leid_af() ongewijzigd. In een if-keten moet je eerst uitzoeken waar
# de nieuwe regel hoort en wat er daardoor verschuift.


# Verwachte uitvoer:
# Gegeven: ['boek_te_laat', 'wil_lenen']
#
#   uit ['boek_te_laat'] volgt: onbetaald
#   uit ['onbetaald'] volgt: mag_niet_lenen
#   uit ['mag_niet_lenen', 'wil_lenen'] volgt: toon_waarschuwing
#
# Alles wat volgt: ['boek_te_laat', 'mag_niet_lenen', 'onbetaald', 'toon_waarschuwing', 'wil_lenen']
