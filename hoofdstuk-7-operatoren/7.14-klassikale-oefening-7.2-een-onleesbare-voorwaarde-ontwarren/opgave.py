# Python basis — theoriebundel
# Hoofdstuk 7 — Operatoren, waarheidstabellen en booleaanse logica
# Klassikale oefening 7.2 — Een onleesbare voorwaarde ontwarren, opgave
#
# De situatie. Je vindt deze regel in de code van de club. Niemand durft hem nog aan
# te raken.
#
# Dit is een fragment uit de uitleg. Het gebruikt namen die elders gemaakt worden, en
# draait niet op zichzelf.

if not (not is_lid or (leeftijd < 12 and not begeleid) or aantal >= 5) and not heeft_boete:
    print("Mag lenen")
