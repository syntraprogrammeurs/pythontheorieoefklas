# Python basis — theoriebundel
# Hoofdstuk 16 — Bestanden lezen en schrijven
# 16.6 Waar staat dat bestand eigenlijk?

# from pathlib import Path: Je importeert het belangrijkste onderdeel (Path) uit de bibliotheek.
# Path.cwd(): CWD staat voor Current Working Directory. Deze functie vraagt aan de computer: 
# "In welke map bevind ik mij op dit exacte moment?"

from pathlib import Path

print(Path.cwd())


with open("leden.txt", "w", encoding="utf-8") as bestand:
    bestand.write("Anke Peeters\nBram Coppens\n\nCato Dhondt\n")

with open("leden.txt", encoding="utf-8") as bestand:
    leden = [regel.strip() for regel in bestand if regel.strip()]

print(leden)
print(len(leden), "leden")


# Verwachte uitvoer:
# ['Anke Peeters', 'Bram Coppens', 'Cato Dhondt']
# 3 leden


# De library pathlib is de moderne, officiële Python-standaard voor het werken met 
# bestands- en maplocaties (paden) op je computer.
# Vroeger gebruikten programmeurs hiervoor de oudere library os.path, 
# waarbij paden als gewone tekst (strings) werden behandeld. pathlib doet dit slimmer: 
# het verandert een bestandspad in een object. Hierdoor kun je met handige functies direct acties 
# uitvoeren op dat bestand of die map, ongeacht of je op Windows, Mac of Linux werkt 
# (het lost automatisch het gedoe met \ of / voor je op).

# Wat zijn andere handige mogelijkheden van pathlib?

# pathlib is een ontzettend uitgebreid "Zwitsers zakmes" voor je computerbestanden. 
# Dit zijn de meest gebruikte functies, opgedeeld in logische categorieën:

# 1. Paden maken en controleren

# • Path("map") / "bestand.txt": De / is een speciale truc in pathlib. 
#       Hiermee plak je mappen en bestanden veilig aan elkaar tot één pad, 
#       zonder dat je handmatig slashes hoeft te typen.
# • bestands_pad.exists(): Geeft True of False. 
#       Ideaal om te controleren of een bestand wel echt op de computer staat voordat je 
#       het probeert te openen.
# • bestands_pad.is_file() of .is_dir(): 
#       Controleert of het pad een echt bestand is, of juist een map (directory).

# 2. Informatie over een bestand opvragen

# Stel, je hebt een pad: pad = Path("documenten/leden.txt").
# • pad.name: Geeft de volledige bestandsnaam ("leden.txt").
# • pad.stem: Geeft de naam zonder de extensie ("leden").
# • pad.suffix: Geeft alleen de extensie (".txt").
# • pad.parent: Geeft de map terug waar het bestand in staat ("documenten").

# 3. Mappen en bestanden beheren (Aanmaken/Verwijderen)

# • map_pad.mkdir(exist_ok=True): Maakt een gloednieuwe map aan op je computer. De optie exist_ok=True zorgt ervoor dat Python niet crasht als de map al bleek te bestaan.
# • pad.rename("nieuwe_naam.txt"): Hernieuwt of verplaatst een bestand.
# • pad.unlink(): Verwijdert een bestand permanent van de harde schijf.

# 4. Zoeken naar bestanden (Globbing)

# • map_pad.glob("*.txt"): Dit is een krachtige zoekfunctie. Hiermee kun je in één keer door een map heenlopen en bijvoorbeeld alle tekstbestanden (.txt) opzoeken.