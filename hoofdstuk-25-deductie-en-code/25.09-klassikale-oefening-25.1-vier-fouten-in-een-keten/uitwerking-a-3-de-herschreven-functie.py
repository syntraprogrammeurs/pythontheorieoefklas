# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.1 — Vier fouten in één keten, uitwerking
#
# 3. De herschreven functie.

# De Leeslamp — boetebedrag, met uitgesproken aannames
# Cursus Python basis, hoofdstuk 25, oefening 1

# Eerst de vier fouten uit de opgave, met de namen uit 25.6:
#   - onbereikbare tak:     "if dagen_te_laat < 14" kwam pas na "< 30". Wie daar
#                           aankomt, is 30 dagen of meer te laat: dode code.
#   - ontbrekend geval:     bij 30 dagen of meer paste geen enkele tak, dus kwam
#                           er None terug in plaats van een bedrag.
#   - overlappende takken:  een student is OOK iemand met een aantal dagen. De
#                           studenttak stond vóór de dagen en won altijd: een
#                           student van 40 dagen betaalde 10 euro, een gewoon
#                           lid 28,25.
#   - te veel aannemen:     "is_erelid" vooraan: een erelid betaalt nooit, ook
#                           niet na een jaar. Dat is geen fout in de code, maar
#                           een beslissing die niemand uitsprak. Het bestuur
#                           moet zeggen of dat de bedoeling is.

# De tarieven als "constanten" bovenaan: hoofdletters betekenen "verander
# mij niet". Zo staan alle bedragen één keer, netjes naast elkaar, en hoef je
# bij een prijswijziging maar op één plaats te zoeken.
DAGTARIEF_STUDENT = 0.25
DAGTARIEF_EERSTE_WEEK = 0.50
DAGTARIEF_DAARNA = 0.75
MAXIMUM = 50.00                  # nieuw: zonder plafond groeit de boete eindeloos


# is_student=False en is_erelid=False zijn standaardwaarden: wie ze weglaat,
# krijgt False. Daarom mag je onderaan gewoon boetebedrag(dagen) schrijven.
def boetebedrag(dagen_te_laat, is_student=False, is_erelid=False):
    """De boete in euro's.

    Preconditie : dagen_te_laat is een geheel getal.
    Postconditie: het resultaat ligt tussen 0 en MAXIMUM,
                  en daalt nooit wanneer dagen_te_laat stijgt.
    """
    # De preconditie uitgesproken met assert (25.2). isinstance(x, int) vraagt:
    # is x een geheel getal? Zo niet, dan stopt het programma met deze melding.
    assert isinstance(dagen_te_laat, int), "dagen_te_laat hoort een int te zijn"

    # bewaakclausules: elke reden om niets te rekenen, apart
    # (25.7) Elke bewaakclausule handelt één geval af en stapt meteen uit met
    # return. Wie voorbij deze twee regels komt, WEET dus: dagen_te_laat is
    # minstens 1 en het lid is geen erelid.
    if dagen_te_laat <= 0:
        return 0.00
    if is_erelid:
        # De regel voor ereleden blijft, maar ze staat nu zichtbaar apart. Zo
        # ziet iedereen dat het een keuze is, en kan het bestuur ze bevestigen.
        return 0.00

    # Hier verdwijnt de overlap. "Student" kiest niet langer een eigen TAK,
    # maar alleen het TARIEF. Student zijn en te laat zijn zijn twee losse
    # dingen, en nu worden ze ook los behandeld.
    # Dit is een voorwaardelijke expressie: "waarde_a if voorwaarde else waarde_b".
    tarief = DAGTARIEF_STUDENT if is_student else DAGTARIEF_EERSTE_WEEK

    # Eén if-else in plaats van vijf takken. Een if met een else is altijd
    # volledig (alles wat niet <= 7 is, valt in de else) en de twee takken
    # sluiten elkaar uit. Er kan dus geen geval ontbreken en niets overlappen.
    if dagen_te_laat <= 7:
        bedrag = dagen_te_laat * tarief
    else:
        # De eerste week aan het eigen tarief, elke dag daarna aan 0,75.
        bedrag = 7 * tarief + (dagen_te_laat - 7) * DAGTARIEF_DAARNA

    # min() kiest het kleinste van de twee: boven het maximum gaat het nooit.
    bedrag = min(bedrag, MAXIMUM)

    # De postconditie gecontroleerd vlak voor de return.
    # 0 <= bedrag <= MAXIMUM is een kettingvergelijking: beide moeten waar zijn.
    assert 0 <= bedrag <= MAXIMUM
    # round(..., 2) rondt af op twee cijfers na de komma: centen.
    return round(bedrag, 2)


# We proberen de functie op de grenzen: 0 (net niets), 1 (de eerste dag),
# 7 en 8 (de overgang naar het tweede tarief), 30 (waar de oude versie None gaf)
# en 365 (waar het maximum moet ingrijpen).
# In de f-string betekent :>4 "rechts uitlijnen over 4 tekens" en :>6.2f
# "rechts uitlijnen over 6 tekens, met 2 cijfers na de komma".
# De print staat over twee regels: twee strings na elkaar worden aan elkaar
# geplakt, en binnen haakjes mag je een nieuwe regel beginnen.
for dagen in (0, 1, 7, 8, 30, 365):
    print(f"{dagen:>4} dagen: gewoon {boetebedrag(dagen):>6.2f}   "
          f"student {boetebedrag(dagen, is_student=True):>6.2f}")

# Kijk naar de uitvoer: de student betaalt nooit meer dan een gewoon lid, en
# per kolom daalt het bedrag nooit als de dagen stijgen.


# Verwachte uitvoer:
#    0 dagen: gewoon   0.00   student   0.00
#    1 dagen: gewoon   0.50   student   0.25
#    7 dagen: gewoon   3.50   student   1.75
#    8 dagen: gewoon   4.25   student   2.50
#   30 dagen: gewoon  20.75   student  19.00
#  365 dagen: gewoon  50.00   student  50.00
