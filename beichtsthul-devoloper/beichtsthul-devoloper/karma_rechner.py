
"""Berechnet Karma-Schulden basierend auf Sünden"""
class KarmaRechner:


    def __init__(self):
        self.base_punkte = {
            "lügen": 15,
            "geld": 12,
            "essen": 8,
            "faul": 5,
            "neid": 10,
            "standard": 7
        }

        self.schlimme_wörter = ["betrogen", "gestohlen", "verletzt", "absichtlich"]

    """Berechnet die Karma-Schulden für eine Sünde"""
    def berechne_karma_schulden(self, kategorie, text):

        punkte = self.base_punkte.get(kategorie, 7)

        # Bonus für längere Beichten
        if len(text) > 100:
            punkte += 5

        # Bonus für besonders schlimme Wörter
        for wort in self.schlimme_wörter:
            if wort in text.lower():
                punkte += 10
                break

        # Bonus für CAPS (Schreien)
        if text.isupper() and len(text) > 10:
            punkte += 3

        return punkte