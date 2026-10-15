# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# 15.3 De juiste fout opvangen

def deel(a, b):
    """Deelt a door b en vangt de fouten op die je kunt verwachten."""
    try:
        return a / b
    except ZeroDivisionError:
        print("  je kunt niet door nul delen")
        return None
    except TypeError:
        print("  dat zijn geen getallen")
        return None


print(deel(10, 2))
print(deel(10, 0))
print(deel(10, "twee"))


# Verwachte uitvoer:
# 5.0
#   je kunt niet door nul delen
# None
#   dat zijn geen getallen
# None
