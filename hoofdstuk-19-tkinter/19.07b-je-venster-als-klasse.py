# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.7 Je venster als klasse
#
# Dat werkt, maar het is precies de global die hoofdstuk 11 je afleerde. En in een
# echt venster met tien velden heb je er tien. De oplossing ken je uit hoofdstuk
# 18: een klasse. De widgets en de gegevens worden attributen, en de functies voor
# de knoppen worden methodes.
#
# Dit programma opent een venster. Sluit het venster om het programma te stoppen.

import tkinter as tk


# Een EIGEN klasse, zoals Boek en Lid in hoofdstuk 18.
# Een Teller-object "beheert" een venster: het bouwt de widgets op en reageert
# op klikken.
#   - de gegevens (het aantal klikken) worden een ATTRIBUUT: self.klikken
#   - de widgets die je later nog nodig hebt, worden attributen: self.melding
#   - de callback van de knop wordt een METHODE: klik()
class Teller:
    """Een venster dat telt hoe vaak er geklikt is."""

    # __init__ loopt automatisch wanneer je Teller(venster) schrijft.
    # self is het nieuwe Teller-object; venster is het tk.Tk-object waarin de
    # widgets moeten komen. ": tk.Tk" is een type hint: "verwacht een Tk-venster".
    def __init__(self, venster: tk.Tk):
        # De teller hoort bij DIT object en blijft bestaan zolang het object
        # bestaat. Geen global meer nodig.
        self.klikken = 0
        venster.title("Teller")
        venster.geometry("800x600")

        # self.melding: een attribuut, want klik() moet de tekst later aanpassen.
        self.melding = tk.Label(venster, text="Nog niet geklikt.")
        self.melding.pack(padx=40, pady=10)

        # command=self.klik -> de METHODE klik van dit object, zonder haakjes.
        # tkinter roept bij een klik dus self.klik() op, en self is dan
        # automatisch het juiste Teller-object.
        # knop is GEEN attribuut (geen self.): na deze regel spreek je de knop
        # nooit meer aan, dus een gewone lokale variabele volstaat.
        knop = tk.Button(venster, text="Klik", command=self.klik)
        knop.pack(pady=(0, 20))

    # De callback is nu een methode. Ze kan aan alles van het object via self.
    # "-> None" is een type hint: deze methode geeft niets terug.
    def klik(self) -> None:
        self.klikken += 1
        self.melding.config(text=f"{self.klikken} keer geklikt.")


# Het hoofdprogramma: venster maken, een Teller-object eraan koppelen, wachten.
venster = tk.Tk()

# Je hoeft het object niet in een variabele te bewaren: de knop onthoudt via
# command=self.klik zelf het object, zodat het blijft bestaan.
Teller(venster)

venster.mainloop()


# Wat je ziet: zie 19.07b-je-venster-als-klasse.png
