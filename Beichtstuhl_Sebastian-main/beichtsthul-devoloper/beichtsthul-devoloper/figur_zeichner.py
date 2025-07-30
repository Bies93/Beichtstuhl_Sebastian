import tkinter as tk
import pygame, time

"""Zeichnet die animierte Mönchsfigur"""
class FigurZeichner:

    def __init__(self, canvas):
        self.canvas = canvas
        self.emotionen_mapping = {
            "lügen": "urteilend",
            "geld": "genervt",
            "essen": "lachend",
            "faul": "genervt",
            "neid": "schockiert",
            "standard": "neutral"
        }


    """Zeichnet die Figur mit der entsprechenden Emotion"""
    def zeichne_figur(self, emotion="neutral", antwort_text=""):
        print(f"Erkannte Emotion: {emotion}")
        self.canvas.delete("all")
        # Hintergrund (Kirchenfenster-Effekt)
        self.canvas.create_rectangle(50, 30, 350, 220, fill="#330000", outline="#666666", width=2)

        # Figur: Mönch/Richter
        self._zeichne_körper()
        self._zeichne_arme()
        self._zeichne_kopf()
        self._zeichne_kapuze()
        self._zeichne_emotion(emotion)


        # Sprechblase wenn Antwort vorhanden
        if antwort_text:
            self._zeichne_sprechblase()

    """Zeichnet den Körper des Mönchs"""
    def _zeichne_körper(self):
        self.canvas.create_oval(180, 120, 220, 180, fill="#4a4a4a", outline="#666666")

    """Zeichnet Arme"""
    def _zeichne_arme(self):
        self.canvas.create_line(160, 140, 180, 150, fill="#2a2a2a", width=8)
        self.canvas.create_line(220, 150, 240, 140, fill="#2a2a2a", width=8)

    """Zeichnet den Kopf"""
    def _zeichne_kopf(self):
        self.canvas.create_oval(175, 80, 225, 130, fill="#ffdbac", outline="#cc9966")

    """Zeichnet die Kapuze"""
    def _zeichne_kapuze(self):

        self.canvas.create_arc(160, 60, 240, 140, start=0, extent=180, fill="#2a2a2a", outline="#444444")

    """Zeichnet die entsprechende Emotion"""
    def _zeichne_emotion(self, emotion):
        print(self.canvas.winfo_width(), self.canvas.winfo_height())

        if emotion == "neutral":
            self._zeichne_neutrale_augen()
            self._zeichne_neutralen_mund()

        elif emotion == "genervt":
            self._zeichne_genervte_augen()
            self._zeichne_stirnfalten()
            self._zeichne_unzufriedenen_mund()

        elif emotion == "schockiert":
            self._zeichne_schockierte_augen()
            self._zeichne_offenen_mund()

        elif emotion == "lachend":
            self._zeichne_lachende_augen()
            self._zeichne_breites_grinsen()
            self._zeichne_tränen()

        elif emotion == "urteilend":
            self._zeichne_urteilende_augen()
            self._zeichne_herablassenden_mund()
            self._zeichne_verschränkte_arme()

    def _zeichne_neutrale_augen(self):
        self.canvas.create_oval(185, 95, 195, 105, fill="black")
        self.canvas.create_oval(205, 95, 215, 105, fill="black")

    def _zeichne_neutralen_mund(self):
        self.canvas.create_arc(190, 105, 210, 115, start=0, extent=180, outline="black", width=2)

    def _zeichne_genervte_augen(self):
        self.canvas.create_line(185, 100, 195, 95, fill="black", width=3)
        self.canvas.create_line(205, 95, 215, 100, fill="black", width=3)

    def _zeichne_stirnfalten(self):
        self.canvas.create_line(185, 85, 195, 90, fill="black", width=2)
        self.canvas.create_line(205, 90, 215, 85, fill="black", width=2)

    def _zeichne_unzufriedenen_mund(self):
        self.canvas.create_arc(190, 115, 210, 105, start=0, extent=180, outline="black", width=2)

    def _zeichne_schockierte_augen(self):
        self.canvas.create_oval(182, 92, 198, 108, fill="white", outline="black")
        self.canvas.create_oval(202, 92, 218, 108, fill="white", outline="black")
        self.canvas.create_oval(187, 97, 193, 103, fill="black")
        self.canvas.create_oval(207, 97, 213, 103, fill="black")

    def _zeichne_offenen_mund(self):
        self.canvas.create_oval(195, 110, 205, 120, fill="black")

    def _zeichne_lachende_augen(self):
        self.canvas.create_arc(185, 95, 195, 105, start=0, extent=180, fill="black")
        self.canvas.create_arc(205, 95, 215, 105, start=0, extent=180, fill="black")

    def _zeichne_breites_grinsen(self):
        self.canvas.create_arc(185, 105, 215, 125, start=0, extent=180, outline="black", width=3)

    def _zeichne_tränen(self):
        self.canvas.create_oval(180, 100, 185, 110, fill="lightblue")
        self.canvas.create_oval(215, 100, 220, 110, fill="lightblue")

    def _zeichne_urteilende_augen(self):
        self.canvas.create_line(185, 100, 195, 100, fill="black", width=3)
        self.canvas.create_line(205, 100, 215, 100, fill="black", width=3)

    def _zeichne_herablassenden_mund(self):
        self.canvas.create_arc(188, 110, 212, 118, start=20, extent=140, outline="black", width=2)

    def _zeichne_verschränkte_arme(self):
        self.canvas.create_line(160, 140, 180, 150, fill="#2a2a2a", width=8)
        self.canvas.create_line(220, 150, 240, 140, fill="#2a2a2a", width=8)

    def _zeichne_sprechblase(self):
        # Blase
        self.canvas.create_rectangle(260, 50, 380, 120, fill="#ffffff", outline="#333333", width=2)
        # Zeiger
        self.canvas.create_polygon(260, 100, 240, 110, 260, 120, fill="#ffffff", outline="#333333")
        # Text in der Blase
        self.canvas.create_text(320, 85, text="Tss tss tss...", font=("Arial", 9), width=100)

    """Gibt die passende Emotion für eine Sünden-Kategorie zurück"""
    def get_emotion_fuer_kategorie(self, kategorie):
             return self.emotionen_mapping.get(kategorie, "neutral")

