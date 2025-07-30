import tkinter as tk
from tkinter import messagebox
import random
from collections import defaultdict

# Importiere alle Module (in der echten Version wären das separate Dateien)
from datei_manager import DateiManager
from antwort_generator import AntwortGenerator
from karma_rechner import KarmaRechner
from figur_zeichner import FigurZeichner
from statistik_manager import StatistikManager

"""Hauptklasse für die GUI des Sarkastischen Beichtstuhls"""
class BeichtstuhlGUI:

    def __init__(self):
        # Initialisiere alle Module
        self.datei_manager = DateiManager("daten.json")
        self.antwort_generator = AntwortGenerator()
        self.karma_rechner = KarmaRechner()
        self.statistik_manager = StatistikManager()
        self.suenden_kategorien = defaultdict(int)

        # Lade gespeicherte Daten
        self.karma_schulden, self.beicht_historie, self.suenden_kategorien = self.datei_manager.lade_daten()

        # Setup GUI
        self.setup_hauptfenster()
        self.setup_gui_elemente()

        # Initialisiere Figur-Zeichner
        self.figur_zeichner = FigurZeichner(self.canvas)
        self.figur_zeichner.zeichne_figur("neutral")

    def setup_hauptfenster(self):
        self.fenster = tk.Tk()
        self.fenster.title("🔥 Der Sarkastische Beichtstuhl 🔥")
        self.fenster.geometry("600x700")
        self.fenster.configure(bg="#2c1810")

    def setup_gui_elemente(self):
        # Header
        header = tk.Label(
            self.fenster,
            text="🔥 Der Sarkastische Beichtstuhl 🔥",
            font=("Arial", 16, "bold"),
            bg="#2c1810",
            fg="#ff6b35"
        )
        header.pack(pady=10)

        # Canvas für die Figur
        self.canvas = tk.Canvas(
            self.fenster,
            width=400,
            height=250,
            bg="#1a1a1a",
            highlightthickness=2,
            highlightbackground="#ff6b35"
        )
        self.canvas.pack(pady=10)

        # Eingabebereich
        self.setup_eingabebereich()

        # Buttons
        self.setup_buttons()

        # Ausgabebereich
        self.setup_ausgabebereich()

        # Karma-Anzeige
        self.karma_label = tk.Label(
            self.fenster,
            text=f"💀 Karma-Schulden: {self.karma_schulden} 💀",
            font=("Arial", 12, "bold"),
            bg="#2c1810",
            fg="#ff3333"
        )
        self.karma_label.pack()

    def setup_eingabebereich(self):
        eingabe_frame = tk.Frame(self.fenster, bg="#2c1810")
        eingabe_frame.pack(pady=10)

        tk.Label(
            eingabe_frame,
            text="Beichte deine Sünde, du verlorene Seele:",
            font=("Arial", 12),
            bg="#2c1810",
            fg="#ffffff"
        ).pack()

        self.eingabe = tk.Text(
            eingabe_frame,
            width=50,
            height=3,
            font=("Arial", 10),
            bg="#333333",
            fg="#ffffff",
            insertbackground="#ffffff"
        )
        self.eingabe.pack(pady=5)

    def setup_buttons(self):
        button_frame = tk.Frame(self.fenster, bg="#2c1810")
        button_frame.pack(pady=10)

        beicht_btn = tk.Button(
            button_frame,
            text="⚡ BEICHTEN ⚡",
            command=self.beichten,
            font=("Arial", 12, "bold"),
            bg="#ff6b35",
            fg="white",
            padx=20,
            pady=5
        )
        beicht_btn.pack(side=tk.LEFT, padx=5)

        stats_btn = tk.Button(
            button_frame,
            text="📊 Statistiken",
            command=self.zeige_statistiken,
            font=("Arial", 10),
            bg="#666666",
            fg="white",
            padx=15,
            pady=5
        )
        stats_btn.pack(side=tk.LEFT, padx=5)

        reset_btn = tk.Button(
            button_frame,
            text="🔄 Reset",
            command=self.reset_statistiken,
            font=("Arial", 10),
            bg="#994444",
            fg="white",
            padx=15,
            pady=5
        )
        reset_btn.pack(side=tk.LEFT, padx=5)

    def setup_ausgabebereich(self):
        self.ausgabe = tk.Label(
            self.fenster,
            text="Sprich, und ich werde urteilen...",
            wraplength=500,
            font=("Arial", 11, "italic"),
            bg="#2c1810",
            fg="#ffaa44",
            height=3
        )
        self.ausgabe.pack(pady=20)

    def beichten(self):
        suende = self.eingabe.get("1.0", tk.END).strip()

        if not suende:
            self.ausgabe.config(text="Du musst schon was beichten, Faulpelz!")
            self.figur_zeichner.zeichne_figur("genervt")
            return

        self.verarbeite_suende(suende)
        self.eingabe.delete("1.0", tk.END)
        self.datei_manager.speichere_daten(self.karma_schulden, self.beicht_historie, self.suenden_kategorien)

    def verarbeite_suende(self, suende):
        kategorie = self.antwort_generator.kategorisiere_suende(suende)
        print(f"Kategorisierte Sünde: {kategorie}")

        kategorie = self.antwort_generator.kategorisiere_suende(suende)
        easter_antwort, easter_emotion = self.antwort_generator.prüfe_easter_eggs(suende)

        if easter_antwort:
            antwort = easter_antwort
            emotion = easter_emotion
        else:
            antwort = self.antwort_generator.get_antwort(kategorie)
            emotion = self.figur_zeichner.get_emotion_fuer_kategorie(kategorie)

            neue_schulden = self.antwort_generator.berechne_schulden(kategorie)
            self.karma_schulden += neue_schulden
            self.aktualisiere_gui(antwort, neue_schulden, emotion)

        neue_schulden = self.karma_rechner.berechne_karma_schulden(kategorie, suende)
        self.karma_schulden += neue_schulden

        self.beicht_historie.append({
            "suende": suende,
            "kategorie": kategorie,
            "karma": neue_schulden
        })

        self.beicht_historie.append(suende)
        self.datei_manager.speichere_daten(
            self.karma_schulden,
            self.beicht_historie,
            self.antwort_generator.schulden_mapping
        )
       # self.suenden_kategorien[kategorie] += 1

        self.aktualisiere_gui(antwort, neue_schulden, emotion)

    def aktualisiere_gui(self, antwort, neue_schulden, emotion):
        self.ausgabe.config(text=f"{antwort}\n\n+{neue_schulden} Karma-Schulden!")
        self.karma_label.config(text=f"💀 Karma-Schulden: {self.karma_schulden} 💀")
        self.figur_zeichner.zeichne_figur(emotion, antwort)


    def zeige_statistiken(self):
        self.statistik_manager.zeige_statistiken(
            self.karma_schulden,
            self.beicht_historie,
            self.suenden_kategorien
        )

    def reset_statistiken(self):
        if self.statistik_manager.bestätige_reset():
            self.karma_schulden = 0
            self.beicht_historie = []
            self.suenden_kategorien = defaultdict(int)
            self.karma_label.config(text="💀 Karma-Schulden: 0 💀")
            self.ausgabe.config(text="Du bist rein gewaschen... vorerst.")
            self.figur_zeichner.zeichne_figur("neutral")
            self.datei_manager.speichere_daten(self.karma_schulden, self.beicht_historie, self.suenden_kategorien)

    def starten(self):
        welcome_messages = [
            "Willkommen in der Höhle der Wahrheit!",
            "Ein neues Opfer... äh, Besucher!",
            "Bereit für etwas Selbsterkenntnis?"
        ]
        self.ausgabe.config(text=random.choice(welcome_messages))
        self.fenster.mainloop()
