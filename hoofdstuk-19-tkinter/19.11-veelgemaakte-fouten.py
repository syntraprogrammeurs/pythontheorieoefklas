# Python basis — theoriebundel
# Hoofdstuk 19 — Grafische programma's met tkinter
# 19.11 Veelgemaakte fouten
#
# De zesde rij verdient aandacht. Deze regel ziet er handig uit:
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf. grid() geeft None terug, dus naam_veld is None, en
# naam_veld.get() geeft later AttributeError: 'NoneType' object has no attribute
# 'get'.

# Wat er gebeurt, van links naar rechts:
#   1. tk.Entry(venster, width=25)  maakt een invoerveld (een Entry-object)
#   2. .grid(row=0, column=1)       zet dat veld in het venster -> je ZIET het
#   3. maar grid() geeft None terug, en DAT komt in naam_veld terecht
# Het Entry-object zelf heb je nergens bewaard.
naam_veld = tk.Entry(venster, width=25).grid(row=0, column=1)

# Zo moet het wel: eerst maken en bewaren, dan op een aparte regel plaatsen.
#     naam_veld = tk.Entry(venster, width=25)
#     naam_veld.grid(row=0, column=1)
