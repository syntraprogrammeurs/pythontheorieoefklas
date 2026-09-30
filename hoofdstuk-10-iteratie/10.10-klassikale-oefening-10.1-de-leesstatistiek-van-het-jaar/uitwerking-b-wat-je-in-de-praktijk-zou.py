# Python basis — theoriebundel
# Hoofdstuk 10 — Iteratie: while, for, range, break en continue
# Klassikale oefening 10.1 — De leesstatistiek van het jaar, uitwerking
#
# Wat je in de praktijk zou schrijven. De ingebouwde functies:

bladzijden = [320, 180, 250, 410, 96, 512, 288, 175, 640, 205, 330, 148]

totaal = sum(bladzijden)
gemiddelde = totaal / len(bladzijden)
dikste = max(bladzijden)
dunste = min(bladzijden)
dikste_nr = bladzijden.index(dikste) + 1

print(totaal, f"{gemiddelde:.1f}", dikste, dunste, dikste_nr)


# Verwachte uitvoer:
# 3554 296.2 640 96 9
