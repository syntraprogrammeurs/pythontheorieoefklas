# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.2 Je eerste venster
#
# Maak in je map leeslamp een bestand venster.py:
#
# Dit programma opent een venster. Sluit het venster om het programma te stoppen.

# tkinter zit in de standaardbibliotheek: je hoeft niets te installeren.
# "as tk" geeft de module een korte naam. Alles uit tkinter schrijf je daarna
# als tk.iets, zodat je altijd ziet waar een naam vandaan komt.
import tkinter as tk

# tk.Tk is een KLASSE. Met tk.Tk() maak je er een object van: het hoofdvenster.
# Elk tkinter-programma heeft precies één Tk-object. Alle andere widgets
# (labels, knoppen, ...) komen daarin terecht.
venster = tk.Tk()

# title() is een METHODE van het venster: ze zet de tekst in de titelbalk.
venster.title("De Leeslamp")

# geometry() legt de grootte vast als tekst "breedtexhoogte", in pixels.
# Laat je deze regel weg, dan past het venster zich aan zijn inhoud aan.
venster.geometry("360x120")

# tk.Label is ook een klasse. Een Label-object is een stukje tekst in het venster.
# Het EERSTE argument is altijd de "ouder": in welk venster het label hoort.
# text= is een benoemd argument (een "optie") met de tekst die je wilt tonen.
welkom = tk.Label(venster, text="Welkom bij boekenclub De Leeslamp")

# Een widget maken is niet genoeg: je moet hem ook in het venster ZETTEN.
# pack() is de eenvoudigste manier: de widgets komen onder elkaar.
# padx en pady geven lege ruimte rond de widget (links/rechts en boven/onder).
welkom.pack(padx=20, pady=20)

# mainloop() start de "gebeurtenislus": tkinter tekent het venster en wacht
# op klikken en toetsaanslagen. Deze regel blijft "hangen" tot de gebruiker
# het venster sluit. Pas dan gaat Python verder (en hier stopt het programma).
# Zonder mainloop() flitst het venster even op en is het meteen weer weg.
venster.mainloop()


# Wat je ziet: zie 19.02-je-eerste-venster.png
