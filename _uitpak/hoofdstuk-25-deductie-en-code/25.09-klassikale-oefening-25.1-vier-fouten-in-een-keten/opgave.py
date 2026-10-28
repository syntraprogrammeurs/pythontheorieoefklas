# Python basis — theoriebundel
# Hoofdstuk 25 — Deductief redeneren en je code
# Klassikale oefening 25.1 — Vier fouten in één keten, opgave
#
# De situatie. Dit staat in de code van De Leeslamp. Er zitten vier logicafouten in,
# één van elke soort uit 25.6.

def boetebedrag(dagen_te_laat, is_student, is_erelid):
    """De boete in euro's. Bevat vier logicafouten."""
    if is_erelid:
        return 0
    if dagen_te_laat <= 0:
        return 0
    if is_student:
        return dagen_te_laat * 0.25
    if dagen_te_laat < 7:
        return dagen_te_laat * 0.50
    if dagen_te_laat < 30:
        return 3.50 + (dagen_te_laat - 7) * 0.75
    if dagen_te_laat < 14:
        return 99.00
