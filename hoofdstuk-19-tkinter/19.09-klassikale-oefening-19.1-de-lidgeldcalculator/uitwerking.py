# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# Klassikale oefening 19.1 — De lidgeldcalculator, uitwerking
#
# Dit programma opent een venster. Het importeert bereken_lidgeld uit
# berekeningen.py (de module uit 17.3), die in dezelfde map staat.

# De Leeslamp — de lidgeldcalculator met een venster
# Cursus Python basis, hoofdstuk 19, oefening 1

import tkinter as tk
from tkinter import messagebox  # aparte module voor pop-upmeldingen

# De BEREKENING komt uit een eigen module (hoofdstuk 17). Het venster rekent
# zelf niets uit: het leest, controleert en toont. Zo kun je bereken_lidgeld
# testen zonder ooit te klikken (de scheiding uit 19.8).
from berekeningen import bereken_lidgeld


# Een eigen klasse die het hele formulier beheert:
#   - de invoervelden zijn ATTRIBUTEN (self.naam, self.leeftijd, ...), zodat
#     elke methode ze kan lezen
#   - de knop roept een METHODE op (self.bereken)
#   - een hulpmethode (lees_getal) vermijdt dat je dezelfde controle twee keer
#     schrijft
class LidgeldVenster:
    """Een venster dat het lidgeld van één lid berekent."""

    # __init__ bouwt het venster op. Dat gebeurt één keer, bij
    # LidgeldVenster(venster). Daarna wacht mainloop() op de gebruiker.
    def __init__(self, venster: tk.Tk):
        venster.title("Lidgeld")

        # resizable(breedte, hoogte): mag de gebruiker het venster uitrekken?
        # False, False -> nee, het formulier heeft een vaste vorm.
        venster.resizable(False, False)

        # --- Rij 0: naam ---------------------------------------------------
        # Het label spreek je nooit meer aan: maken en plaatsen op één regel.
        # grid(row, column): de cel in de tabel. sticky="w": links uitlijnen.
        tk.Label(venster, text="Naam:").grid(
            row=0, column=0, sticky="w", padx=10, pady=5)
        # Het veld wel bewaren als attribuut: bereken() leest het later uit.
        # Eerst maken, dan apart plaatsen (grid() geeft None terug!).
        self.naam = tk.Entry(venster, width=25)
        self.naam.grid(row=0, column=1, padx=10, pady=5)

        # --- Rij 1: leeftijd -------------------------------------------------
        tk.Label(venster, text="Leeftijd:").grid(
            row=1, column=0, sticky="w", padx=10, pady=5)
        self.leeftijd = tk.Entry(venster, width=25)
        self.leeftijd.grid(row=1, column=1, padx=10, pady=5)

        # --- Rij 2: jaren lid ------------------------------------------------
        tk.Label(venster, text="Jaren lid:").grid(
            row=2, column=0, sticky="w", padx=10, pady=5)
        self.jaren = tk.Entry(venster, width=25)
        self.jaren.grid(row=2, column=1, padx=10, pady=5)

        # --- Rij 3: het vakje Student ----------------------------------------
        # Een Checkbutton bewaart zijn toestand in een tk.BooleanVar.
        # self.student.get() geeft straks True (aangevinkt) of False.
        self.student = tk.BooleanVar()
        tk.Checkbutton(venster, text="Student", variable=self.student).grid(
            row=3, column=1, sticky="w", padx=10)

        # --- Rij 4: de knop --------------------------------------------------
        # command=self.bereken: de methode, ZONDER haakjes.
        # columnspan=2: de knop beslaat beide kolommen en staat in het midden.
        tk.Button(venster, text="Bereken", command=self.bereken).grid(
            row=4, column=0, columnspan=2, pady=10)

        # --- Rij 5: de uitkomst ----------------------------------------------
        # Leeg bij de start. bereken() vult het later in met config().
        # Een attribuut, want bereken() moet het kunnen aanpassen.
        self.uitkomst = tk.Label(venster, text="",
                                 font=("Segoe UI", 12, "bold"))
        self.uitkomst.grid(row=5, column=0, columnspan=2, pady=(0, 10))

        # Enter doet hetzelfde als op Bereken klikken.
        # bind() geeft altijd een event mee, daarom "lambda event:".
        venster.bind("<Return>", lambda event: self.bereken())

        # De cursor staat meteen in het naamveld.
        self.naam.focus()

    # Hulpmethode: leest één veld en geeft een geheel getal terug.
    # Bij een fout toont ze ZELF de melding en geeft ze None terug.
    #   veld         -> welk Entry-object (self.leeftijd of self.jaren)
    #   omschrijving -> de naam van het veld, voor in de foutmelding
    #   -> int | None   "een geheel getal, of niets"
    def lees_getal(self, veld: tk.Entry, omschrijving: str) -> int | None:
        """Het gehele getal in dit veld, of None na een foutmelding."""
        # get() geeft de tekst als string; strip() haalt spaties weg.
        tekst = veld.get().strip()
        try:
            getal = int(tekst)
        except ValueError:
            # Geen geheel getal (ook een leeg veld komt hier terecht).
            messagebox.showerror(
                "Ongeldige invoer",
                f"{omschrijving}: '{tekst}' is geen geheel getal.")
            # Zet de cursor in het foute veld: de gebruiker moet niet zoeken.
            veld.focus()
            return None
        if getal < 0:
            messagebox.showerror(
                "Ongeldige invoer", f"{omschrijving} kan niet negatief zijn.")
            veld.focus()
            return None
        return getal

    # De callback van de knop (en van Enter).
    # Leest van boven naar onder: bij elke fout meteen stoppen met return.
    def bereken(self) -> None:
        """Leest de velden, controleert ze en toont het lidgeld."""
        naam = self.naam.get().strip()
        if not naam:
            # showwarning: een waarschuwing (uitroepteken), geen echte fout.
            messagebox.showwarning("Naam ontbreekt", "Vul eerst een naam in.")
            self.naam.focus()
            return

        # De hulpmethode twee keer gebruiken, voor twee verschillende velden.
        leeftijd = self.lees_getal(self.leeftijd, "Leeftijd")
        if leeftijd is None:
            return
        jaren = self.lees_getal(self.jaren, "Jaren lid")
        if jaren is None:
            return

        # Een controle die twee velden samen nodig heeft.
        if jaren > leeftijd:
            messagebox.showerror(
                "Ongeldige invoer", f"{jaren} jaar lid op {leeftijd} jaar?")
            self.jaren.focus()
            return

        # Alles is in orde: de module rekent, het venster toont.
        # self.student.get() geeft True of False uit de BooleanVar.
        bedrag = bereken_lidgeld(leeftijd, self.student.get(), jaren)
        self.uitkomst.config(text=f"{naam} betaalt {bedrag} euro.")


# Alleen als je DIT bestand start, opent het venster (hoofdstuk 17).
# Importeer je LidgeldVenster in een ander bestand, dan gebeurt er niets.
if __name__ == "__main__":
    venster = tk.Tk()
    LidgeldVenster(venster)
    venster.mainloop()


# Probeer zeker deze invoer. Elke rij test iets anders:
#
# Invoer                        Wat je ziet                                  Wat het test
# Anke Peeters, 34, 3           Anke Peeters betaalt 25 euro.                Korting na drie jaar
# Bram Coppens, 20, 1, student  Bram Coppens betaalt 15 euro.                Het studententarief
# Cato Dhondt, 9, 0             Cato Dhondt betaalt 0 euro.                  Gratis onder de twaalf
# Els Janssens, twintig, 1      Leeftijd: 'twintig' is geen geheel getal.    De ValueError wordt opgevangen
# Femke, 20, 25                 25 jaar lid op 20 jaar?                      Een onmogelijke combinatie
# Lege naam                     Vul eerst een naam in.                       Een waarschuwing, geen fout
# Hilde, 40, leeg veld          Jaren lid: '' is geen geheel getal.          Een leeg veld is ook ongeldige invoer
#
# Wat je ziet: zie uitwerking-venster.png en uitwerking-foutmelding.png
