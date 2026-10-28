# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.4 Een knop die iets doet — Een knop die een argument meegeeft
#
# command roept de functie altijd op zonder argumenten. Moet de functie toch iets
# weten, zoals welk genre gekozen is, dan verpak je de aanroep in een lambda uit
# hoofdstuk 11:
#
# Dit programma opent een venster. Sluit het venster om het programma te stoppen.

import tkinter as tk


# Deze callback heeft een parameter nodig: welk genre werd gekozen?
# Een knop kan dat zelf niet doorgeven: command roept altijd op ZONDER argumenten.
def kies(genre: str):
    # Toon de keuze in het label, met config().
    keuze.config(text=f"Je koos: {genre}")


venster = tk.Tk()
venster.title("Genre")

keuze = tk.Label(venster, text="Kies een genre.")
keuze.pack(pady=10)

# Drie knoppen, gemaakt in een lus: één Button-object per genre.
for genre in ("Roman", "Thriller", "Poëzie"):
    # width=10 -> de knop is 10 TEKENS breed (niet pixels), zodat alle drie
    # de knoppen even breed zijn.
    #
    # command=lambda g=genre: kies(g)
    #   De lambda is een kleine functie zonder argumenten (voor tkinter) die
    #   zelf kies(...) oproept MET een argument.
    #   g=genre is een standaardwaarde: die wordt bewaard op het moment dat de
    #   knop gemaakt wordt. Zo onthoudt elke knop zijn eigen genre.
    #   Schrijf je lambda: kies(genre), dan kijkt de lambda pas bij de klik naar
    #   genre, en dan is de lus al voorbij: alle knoppen zeggen dan "Poëzie".
    knop = tk.Button(venster, text=genre, width=10,
                     command=lambda g=genre: kies(g))

    # side="left" -> pack zet de knoppen NAAST elkaar, van links naar rechts,
    # in plaats van onder elkaar.
    knop.pack(side="left", padx=5, pady=(0, 10))

venster.mainloop()


# Wat je ziet: zie 19.04b-een-knop-die-een-argument-meegeeft.png
