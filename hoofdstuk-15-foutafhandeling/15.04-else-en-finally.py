# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.4 else en finally

def lees_getal(tekst):
    """Zet tekst om naar een getal en toont wat er gebeurt."""
    try:
        getal = int(tekst)
    except ValueError:
        print(f"  {tekst!r}: geen getal")
        return None
    else:
        print(f"  {tekst!r}: gelukt")
        return getal
    finally:
        print("  klaar met deze poging")


print(lees_getal("24"))
print(lees_getal("abc"))


# Verwachte uitvoer:
#   '24': gelukt
#   klaar met deze poging
# 24
#   'abc': geen getal
#   klaar met deze poging
# None
