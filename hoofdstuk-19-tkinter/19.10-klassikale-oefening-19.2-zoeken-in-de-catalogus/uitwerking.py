# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# Klassikale oefening 19.2 — Zoeken in de catalogus, uitwerking
#
# Dit programma opent een venster. Sluit het venster om het programma te stoppen.

# De Leeslamp — zoeken in de catalogus
# Cursus Python basis, hoofdstuk 19, oefening 2

import tkinter as tk
from tkinter import messagebox

# De catalogus: een lijst van tuples (titel, schrijver, jaar).
# HOOFDLETTERS: een constante die het programma niet verandert.
BOEKEN = [
    ("De ontdekking van de hemel", "Harry Mulisch", 1992),
    ("De aanslag", "Harry Mulisch", 1982),
    ("Het diner", "Herman Koch", 2009),
    ("Turks fruit", "Jan Wolkers", 1969),
    ("Max Havelaar", "Multatuli", 1860),
    ("Het smelt", "Lize Spit", 2016),
]


# Een gewone functie, BUITEN de klasse: ze weet niets van vensters.
# Je kunt ze dus testen met print of assert, zonder te klikken (19.8).
def zoek_boeken(boeken: list, deel: str) -> list:
    """Alle boeken waarvan titel of schrijver dit deel bevat."""
    # Alles in kleine letters vergelijken: "MULISCH" vindt dan ook "Mulisch".
    deel = deel.strip().lower()
    # Een list comprehension (hoofdstuk 14): boek[0] is de titel, boek[1] de
    # schrijver. Een lege zoekterm "" zit in elke tekst, dus die vindt alles.
    return [
        boek for boek in boeken
        if deel in boek[0].lower() or deel in boek[1].lower()
    ]


# De klasse die het zoekvenster beheert.
#   self.boeken   -> de volledige catalogus
#   self.gevonden -> de boeken die NU in de lijst staan (nodig bij dubbelklik)
#   self.zoekveld, self.lijst, self.teller -> widgets die later nog nodig zijn
class ZoekVenster:
    """Een venster om de catalogus te doorzoeken."""

    def __init__(self, venster: tk.Tk, boeken: list):
        self.boeken = boeken
        self.gevonden = []
        venster.title("De Leeslamp — catalogus")

        # tk.Frame is een onzichtbare "doos" die widgets groepeert.
        # Binnen een Frame kies je opnieuw hoe je schikt. Zo kan de bovenste
        # rij NAAST elkaar staan, terwijl de rest van het venster ONDER
        # elkaar staat.
        # fill="x" -> de Frame rekt uit over de hele breedte van het venster.
        bovenaan = tk.Frame(venster)
        bovenaan.pack(fill="x", padx=10, pady=10)

        # Deze drie widgets hebben "bovenaan" als ouder (eerste argument), niet
        # het venster. side="left" zet ze naast elkaar, van links naar rechts.
        tk.Label(bovenaan, text="Zoek:").pack(side="left")
        self.zoekveld = tk.Entry(bovenaan, width=30)
        self.zoekveld.pack(side="left", padx=5)
        tk.Button(bovenaan, text="Zoek", command=self.zoek).pack(side="left")

        # tk.Listbox: een lijst waaruit de gebruiker een regel kan kiezen.
        # width in tekens, height in regels.
        self.lijst = tk.Listbox(venster, width=50, height=8)
        self.lijst.pack(padx=10)

        # "<Double-Button-1>" is de gebeurtenis "dubbelklik met de linkermuisknop".
        # Je geeft de methode zelf door (zonder haakjes). Omdat bind een event
        # meegeeft, heeft toon_details een parameter event.
        self.lijst.bind("<Double-Button-1>", self.toon_details)

        # Onderaan: hoeveel boeken er gevonden zijn.
        self.teller = tk.Label(venster, text="")
        self.teller.pack(pady=10)

        # Enter zoekt ook. De lambda vangt het event op en roept zoek() op.
        venster.bind("<Return>", lambda event: self.zoek())
        self.zoekveld.focus()

        # Meteen één keer zoeken met een leeg veld: dan staan bij het openen
        # alle boeken in de lijst. Geen aparte code nodig voor "alles tonen".
        self.zoek()

    # De callback van de knop Zoek (en van Enter).
    def zoek(self) -> None:
        """Vult de lijst met de boeken die passen bij de zoekterm."""
        # Het zoeken zelf doet de losse functie; het venster toont alleen.
        self.gevonden = zoek_boeken(self.boeken, self.zoekveld.get())

        # Methodes van een Listbox:
        #   delete(0, tk.END)        -> alle regels weg, van de eerste tot het einde
        #   insert(tk.END, tekst)    -> een regel achteraan toevoegen
        self.lijst.delete(0, tk.END)
        # Tuple unpacking: elk boek splitsen in titel, schrijver en jaar.
        for titel, schrijver, jaar in self.gevonden:
            self.lijst.insert(tk.END, f"{titel} — {schrijver}")

        # Correct Nederlands: 1 boek, maar 0 of 2 boeken.
        aantal = len(self.gevonden)
        woord = "boek" if aantal == 1 else "boeken"
        self.teller.config(text=f"{aantal} {woord} gevonden")

    # De callback van de dubbelklik. event bevat info over de klik; we hebben
    # het niet nodig, maar bind geeft het altijd mee.
    def toon_details(self, event) -> None:
        """Toont titel, schrijver en jaar van het aangeklikte boek."""
        # curselection() geeft de VOLGNUMMERS van de gekozen regel(s) als tuple,
        # bv. (1,). Niets gekozen? Dan een lege tuple ().
        selectie = self.lijst.curselection()
        if not selectie:
            return
        # Het volgnummer in de lijst is ook de index in self.gevonden.
        # Daarom bewaren we self.gevonden: zo vinden we het boek terug.
        titel, schrijver, jaar = self.gevonden[selectie[0]]
        # \n in de tekst: een nieuwe regel in de melding.
        messagebox.showinfo(titel, f"{titel}\n{schrijver}, {jaar}")


if __name__ == "__main__":
    venster = tk.Tk()
    ZoekVenster(venster, BOEKEN)
    venster.mainloop()


# Probeer deze zoektermen:
#
# Zoekterm   Gevonden   Waarom
# (leeg)     6 boeken   Een lege string zit in elke tekst
# mulisch    2 boeken   Gevonden via de schrijver
# MULISCH    2 boeken   Hoofdletters maken niet uit
# koch       1 boek     Enkelvoud in de teller
# ha         3 boeken   Harry twee keer, en Max Havelaar
# xyz        0 boeken   Een lege lijst, geen fout
#
# Wat je ziet: zie uitwerking-venster.png en uitwerking-details.png
