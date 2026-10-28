import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Hoofdscherm aanmaken
root = tk.Tk()
root.title("Tkinter & TTK Widget Overzicht")
root.geometry("900x700")

# --- 1. HOOFDSTRUCTUREN (Frame & PanedWindow) ---
# Een PanedWindow splitst het scherm in twee sleepbare delen (links en rechts)
main_pane = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief=tk.RAISED, sashwidth=6)
# GEBRUIK HIER PADX EN PADY IN PLAATS VAN PADDING
main_pane.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# Linker- en rechterframe aanmaken voor de slots
left_frame = tk.Frame(main_pane)
right_frame = tk.Frame(main_pane)

main_pane.add(left_frame)
main_pane.add(right_frame)


# --- LINKERKANT VAN HET SCHERM ---

# LabelFrame voor Keuze-elementen
choice_frame = tk.LabelFrame(left_frame, text=" 1. Keuze-elementen & Varianten ", padx=10, pady=10)
choice_frame.pack(fill=tk.X, padx=5, pady=5)

# Radiobuttons (werken samen via één IntVar)
radio_var = tk.IntVar(value=1)
tk.Label(choice_frame, text="Radiobuttons:").grid(row=0, column=0, sticky="w")
tk.Radiobutton(choice_frame, text="Optie A", variable=radio_var, value=1).grid(row=0, column=1)
tk.Radiobutton(choice_frame, text="Optie B", variable=radio_var, value=2).grid(row=0, column=2)

# Listbox met Scrollbar
tk.Label(choice_frame, text="Listbox:").grid(row=1, column=0, sticky="nw", pady=5)
listbox_frame = tk.Frame(choice_frame)
listbox_frame.grid(row=1, column=1, columnspan=2, sticky="w", pady=5)

listbox_scroll = tk.Scrollbar(listbox_frame, orient=tk.VERTICAL)
listbox = tk.Listbox(listbox_frame, yscrollcommand=listbox_scroll.set, height=3)
listbox_scroll.config(command=listbox.yview)

for item in ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]:
    listbox.insert(tk.END, item)

listbox.pack(side=tk.LEFT)
listbox_scroll.pack(side=tk.RIGHT, fill=tk.Y)

# OptionMenu (Klassieke dropdown)
tk.Label(choice_frame, text="OptionMenu:").grid(row=2, column=0, sticky="w", pady=5)
option_var = tk.StringVar(value="Kies...")
option_menu = tk.OptionMenu(choice_frame, option_var, "Keuze 1", "Keuze 2", "Keuze 3")
option_menu.grid(row=2, column=1, columnspan=2, sticky="w", pady=5)


# LabelFrame voor Tekst & Invoer
input_frame = tk.LabelFrame(left_frame, text=" 2. Tekst & Numerieke Invoer ", padx=10, pady=10)
input_frame.pack(fill=tk.X, padx=5, pady=5)

# Spinbox
tk.Label(input_frame, text="Spinbox (Aantal):").grid(row=0, column=0, sticky="w")
spinbox = tk.Spinbox(input_frame, from_=1, to=10, width=5)
spinbox.grid(row=0, column=1, sticky="w")

# Scale (Schuifbalk)
tk.Label(input_frame, text="Scale (Volume):").grid(row=1, column=0, sticky="w", pady=5)
scale = tk.Scale(input_frame, from_=0, to=100, orient=tk.HORIZONTAL)
scale.grid(row=1, column=1, sticky="we", pady=5)

# Text (Meerdere regels)
tk.Label(input_frame, text="Text (Multi-line):").grid(row=2, column=0, sticky="nw", pady=5)
text_area = tk.Text(input_frame, height=4, width=30)
text_area.insert(tk.END, "Typ hier een heel verhaal...\nDit ondersteunt meerdere regels.")
text_area.grid(row=2, column=1, pady=5)


# --- RECHTERKANT VAN HET SCHERM (De moderne TTK-elementen) ---

# Notebook (Tabbladen)
notebook = ttk.Notebook(right_frame)
notebook.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

# ttk.Frame accepteert wél padding als argument
tab1 = ttk.Frame(notebook, padding=10)
tab2 = ttk.Frame(notebook, padding=10)

notebook.add(tab1, text=" TTK Elementen ")
notebook.add(tab2, text=" Canvas Tekenen ")

# Inhoud van Tab 1 (Moderne Widgets)
tk.Label(tab1, text="Combobox (Moderne Dropdown):").pack(anchor="w", pady=2)
combobox = ttk.Combobox(tab1, values=["Modern 1", "Modern 2", "Modern 3"])
combobox.set("Modern 1")
combobox.pack(fill=tk.X, pady=5)

tk.Label(tab1, text="Progressbar:").pack(anchor="w", pady=5)
progressbar = ttk.Progressbar(tab1, orient=tk.HORIZONTAL, mode='determinate', value=65)
progressbar.pack(fill=tk.X, pady=5)

tk.Label(tab1, text="Treeview (Tabel / Boomstructuur):").pack(anchor="w", pady=5)
tree = ttk.Treeview(tab1, columns=("Type", "Waarde"), show='headings', height=4)
tree.heading("Type", text="Type")
tree.heading("Waarde", text="Waarde")
tree.column("Type", width=100)
tree.column("Waarde", width=150)
tree.insert("", tk.END, values=("Klasse", "Radiobutton"))
tree.insert("", tk.END, values=("Klasse", "Canvas"))
tree.pack(fill=tk.BOTH, expand=True, pady=5)

# Inhoud van Tab 2 (Canvas)
tk.Label(tab2, text="Canvas (Zelf vormen tekenen):").pack(anchor="w", pady=2)
canvas = tk.Canvas(tab2, width=300, height=200, bg="white", highlightbackground="gray")
canvas.pack(fill=tk.BOTH, expand=True, pady=5)
# Vormen tekenen op het canvas
canvas.create_line(10, 10, 200, 10, fill="blue", width=2)
canvas.create_rectangle(20, 30, 120, 80, fill="red")
canvas.create_oval(150, 40, 220, 110, fill="green")
canvas.create_text(150, 160, text="Tkinter Canvas", font=("Arial", 12, "bold"))


# --- TRADITIONELE MENUBALK (Helemaal bovenaan het venster) ---
menu_bar = tk.Menu(root)

file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Nieuw")
file_menu.add_command(label="Openen")
file_menu.add_separator()
file_menu.add_command(label="Sluiten", command=root.quit)

help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Over", command=lambda: messagebox.showinfo("Info", "Tkinter Demo app!"))

menu_bar.add_cascade(label="Bestand", menu=file_menu)
menu_bar.add_cascade(label="Help", menu=help_menu)
root.config(menu=menu_bar)

# Applicatie starten
root.mainloop()
