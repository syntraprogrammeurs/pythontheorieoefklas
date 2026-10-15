# Python basis — theoriebundel
# Hoofdstuk 15 — Foutafhandeling met try en except
# Klassikale oefening 15.1 — De rekenmachine die niet stukgaat, uitwerking

# De Leeslamp — een rekenmachine die niet stukgaat
# Cursus Python basis, hoofdstuk 15, oefening 1

TEKENS = ("+", "-", "*", "/")


def naar_getal(tekst: str) -> float:
    """Zet tekst om naar een kommagetal. Werpt een ValueError met uitleg."""
    schoon = tekst.strip().replace(",", ".")
    if not schoon:
        raise ValueError("er is niets ingevuld")
    try:
        return float(schoon)
    except ValueError:
        raise ValueError(f"{tekst.strip()!r} is geen getal") from None


def reken(links: str, teken: str, rechts: str):
    """Rekent twee ingetypte getallen uit. Geeft een getal of een boodschap."""
    try:
        a = naar_getal(links)
        b = naar_getal(rechts)
    except ValueError as fout:
        return f"fout: {fout}"

    teken = teken.strip()
    if teken not in TEKENS:
        return f"fout: {teken!r} is geen bewerking, kies uit {' '.join(TEKENS)}"

    try:
        if teken == "+":
            return a + b
        if teken == "-":
            return a - b
        if teken == "*":
            return a * b
        return a / b
    except ZeroDivisionError:
        return "fout: je kunt niet door nul delen"


gevallen = [
    ("12", "+", "8"),
    ("12", "-", "8"),
    (" 12 ", "*", " 8 "),
    ("12", "/", "8"),
    ("2,5", "*", "4"),
    ("12", "/", "0"),
    ("abc", "+", "3"),
    ("12", "^", "3"),
    ("", "+", "3"),
    ("12", "+", "   "),
    ("-3", "*", "-4"),
]

for links, teken, rechts in gevallen:
    uitkomst = reken(links, teken, rechts)
    print(f"{links!r:>8} {teken!r:^5} {rechts!r:<8} -> {uitkomst}")


# Verwachte uitvoer:
#     '12'  '+'  '8'      -> 20.0
#     '12'  '-'  '8'      -> 4.0
#   ' 12 '  '*'  ' 8 '    -> 96.0
#     '12'  '/'  '8'      -> 1.5
#    '2,5'  '*'  '4'      -> 10.0
#     '12'  '/'  '0'      -> fout: je kunt niet door nul delen
#    'abc'  '+'  '3'      -> fout: 'abc' is geen getal
#     '12'  '^'  '3'      -> fout: '^' is geen bewerking, kies uit + - * /
#       ''  '+'  '3'      -> fout: er is niets ingevuld
#     '12'  '+'  '   '    -> fout: er is niets ingevuld
#     '-3'  '*'  '-4'     -> 12.0
