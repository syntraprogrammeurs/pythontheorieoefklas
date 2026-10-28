import os
import subprocess
import sys
import tkinter as tk
from tkinter import messagebox, ttk


def run_selected_file(event=None):
    try:
        selected_index = file_listbox.curselection()
        if not selected_index:
            messagebox.showwarning("Geen selectie", "Kies eerst een Python-bestand.")
            return

        selected_file = file_listbox.get(selected_index)
        
        # OPLOSSING VOOR HET PAD: Zoek in de specifieke hoofdstuk-map
        script_dir = r"c:/pythontheorieoefklas/hoofdstuk-19-tkinter"
        volledig_pad = os.path.join(script_dir, selected_file)

        if os.path.exists(volledig_pad):
            # Start het subscherm op in de juiste werkmap (cwd)
            subprocess.Popen([sys.executable, volledig_pad], cwd=script_dir)
        else:
            messagebox.showerror("Fout", f"Kan het bestand '{selected_file}' niet vinden op {volledig_pad}")

    except Exception as e:
        messagebox.showerror("Fout bij opstarten", f"Er ging iets mis:\n{str(e)}")

    """Start het geselecteerde .py bestand als een los subscherm."""
    try:
        # Haal de geselecteerde index op uit de Listbox
        selected_index = file_listbox.curselection()

        if not selected_index:
            messagebox.showwarning(
                "Geen selectie", "Kies eerst een Python-bestand uit de lijst."
            )
            return

        # Pak de bestandsnaam op basis van de index
        selected_file = file_listbox.get(selected_index)

        # Controleer of het bestand daadwerkelijk bestaat op de schijf
        if os.path.exists(selected_file):
            # Voer het bestand uit met de huidige Python-interpreter
            # Dit opent het script in een nieuw (sub)scherm
            subprocess.Popen([sys.executable, selected_file])
        else:
            messagebox.showerror(
                "Fout", f"Kan het bestand '{selected_file}' niet vinden."
            )

    except Exception as e:
        messagebox.showerror(
            "Fout bij opstarten", f"Er ging iets mis:\n{str(e)}"
        )


# --- HOOFDSCHERM INITIALISEREN ---
root = tk.Tk()
root.title("Hoofdstuk 19 - Tkinter Script Launcher")
root.geometry("500x450")

# Titel bovenaan het scherm
title_label = tk.Label(
    root,
    text="Beschikbare Oefeningen & Scripts",
    font=("Arial", 14, "bold"),
    pady=10,
)
title_label.pack()

# Container Frame voor de Listbox en Scrollbar
list_frame = tk.Frame(root)
list_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=5)

# Scrollbar aanmaken
scrollbar = tk.Scrollbar(list_frame, orient=tk.VERTICAL)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Listbox aanmaken voor de bestanden
file_listbox = tk.Listbox(
    list_frame,
    font=("Consolas", 11),
    selectmode=tk.SINGLE,
    yscrollcommand=scrollbar.set,
)
file_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
scrollbar.config(command=file_listbox.yview)

# --- DYNAMISCH LIJST VULLEN MET DE BESTANDEN UIT JOUW AFBEELDING ---
# We zetten exact de .py bestanden uit jouw screenshot in de lijst
scripts = [
    "19.04a-een-knop-die-iets-doet.py",
    "19.04b-een-knop-die-een-argument-meegeeft.py",
    "19.05-invoer-lezen-en-meldingen-tonen.py",
    "19.06a-netjes-schikken-met-grid.py",
    "19.06b-sneltoets-enter.py",
    "19.07a-je-venster-als-klasse.py",
    "19.07b-je-venster-als-klasse.py",
    "19.11-veelgemaakte-fouten.py",
]

for script in scripts:
    file_listbox.insert(tk.END, script)

# --- EVENT BINDING & INTERACTIE ---
# Dubbelklikken op een item start het script direct
file_listbox.bind("<Double-1>", run_selected_file)

# Grote actieknop onderaan het scherm
run_button = ttk.Button(
    root, text="Start Geselecteerd Subscherm", command=run_selected_file
)
run_button.pack(fill=tk.X, padx=20, pady=15)

# Start het hoofdscherm
root.mainloop()
