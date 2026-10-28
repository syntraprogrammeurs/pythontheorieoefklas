# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.5 Invoer lezen en meldingen tonen
#
# Een Entry is een invoerveld van één regel. Met get() lees je wat erin staat.
#
# Dit programma opent een venster. Sluit het venster om het programma te stoppen.

import tkinter as tk

# messagebox is een APARTE module binnen tkinter, met functies voor
# pop-upmeldingen. "import tkinter as tk" laadt ze NIET mee:
# tk.messagebox geeft een AttributeError. Daarom importeer je ze apart.
from tkinter import messagebox


# De callback van de knop Controleer.
def controleer():
    # get() is een methode van een Entry: ze geeft de tekst in het veld terug.
    # Dat is ALTIJD een string, ook als de gebruiker een getal typt
    # (net zoals input() in hoofdstuk 6).
    tekst = leeftijd_veld.get()

    # De string omzetten naar een getal kan mislukken ("twintig", of een leeg
    # veld). Daarom try/except uit hoofdstuk 15.
    try:
        leeftijd = int(tekst)
    except ValueError:
        # showerror(titel, tekst) toont een pop-up met een rood kruis en een
        # knop OK. print() heeft geen zin: bij een venster kijkt niemand naar
        # de terminal.
        messagebox.showerror("Ongeldige invoer",
                             f"'{tekst}' is geen geheel getal.")
        # Stop de functie hier: zonder geldig getal valt er niets te controleren.
        return

    # showinfo(titel, tekst) toont een gewone melding met een i-teken.
    if leeftijd < 12:
        messagebox.showinfo("Leeftijd", "Jonger dan twaalf: gratis lid.")
    else:
        messagebox.showinfo("Leeftijd", f"{leeftijd} jaar: gewoon lidgeld.")


venster = tk.Tk()
venster.title("Leeftijd")

# Een label dat je nooit meer aanspreekt, mag je meteen op één regel maken en
# plaatsen. Je bewaart het niet in een variabele.
tk.Label(venster, text="Leeftijd:").pack(padx=70, pady=(20, 5))

# tk.Entry is de klasse voor een invoerveld van één regel.
# width=10 -> 10 tekens breed.
# Het veld moet je WEL bewaren in een variabele: controleer() heeft het nodig
# om er met get() de tekst uit te lezen.
leeftijd_veld = tk.Entry(venster, width=10)
leeftijd_veld.pack()

# focus() zet de cursor in het veld: de gebruiker kan meteen typen.
leeftijd_veld.focus()

# De knop: opnieuw command=controleer, zonder haakjes.
tk.Button(venster, text="Controleer", command=controleer).pack(pady=20)

venster.mainloop()


# Andere nuttige methodes van een Entry:
#   veld.delete(0, tk.END)   maakt het veld leeg (van positie 0 tot het einde)
#   veld.insert(0, "Anke")   zet tekst in het veld, vanaf positie 0
#
# Andere functies uit messagebox:
#   messagebox.showwarning(titel, tekst)  een waarschuwing met een uitroepteken
#   messagebox.askyesno(titel, vraag)     knoppen Ja/Nee, geeft True of False

# Wat je ziet: zie 19.05-invoer-lezen-en-meldingen-tonen-venster.png (met
# twintig ingevuld) en 19.05-invoer-lezen-en-meldingen-tonen-melding.png (de
# foutmelding na een klik op Controleer).
