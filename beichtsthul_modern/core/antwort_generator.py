import random

"""Generiert sarkastische Antworten basierend auf Sünden-Kategorien"""
class AntwortGenerator:


    def __init__(self):
        self.antworten = {
            "lügen": [
                "Lügen ist das täglich Bred der Schwachen.",
                "Pinocchio wäre stolz auf dich.",
                "Die Wahrheit ist wohl zu schwer für dich?",
                "Schon wieder gelogen? Du sammelst wohl Punkte."
            ],
            "geld": [
                "Geld regiert die Welt - und offenbar auch dich.",
                "Gier ist eine Todsünde. Glückwunsch!",
                "Kapitalismus hat dich gut erzogen.",
                "Mammon lächelt zufrieden."
            ],
            "essen": [
                "Völlerei - wie originell.",
                "Der Kühlschrank wird dich vermissen.",
                "Dein Magen ist wohl wichtiger als dein Gewissen?",
                "Gluttony Level: Erreicht."
            ],
            "faul": [
                "Faulheit ist die Mutter aller Laster.",
                "Netflix dankt dir für deine Treue.",
                "Produktivität ist überbewertet, oder?",
                "Dein Sofa vermisst dich schon."
            ],
            "neid": [
                "Grün steht dir nicht.",
                "Neid ist der Dieb der Freude - und deiner Würde.",
                "Andere haben's besser? Shocking!",
                "Missgönnen ist auch eine Kunst."
            ],
            "standard": [
                "Das ist ja fast schon kreativ böse.",
                "Ich hoffe, du hast wenigstens ein schlechtes Gewissen.",
                "Du brauchst mehr als Vergebung – vielleicht einen Therapeuten.",
                "Wow. Einfach wow.",
                "Ich bin beeindruckt. Negativ beeindruckt, aber trotzdem.",
                "Dafür gibt es einen besonderen Platz... du weißt schon wo.",
                "Innovation im Sündigen? Respekt!",
                "Das war's? Ich hatte mehr erwartet."
            ]
        }

        self.keywords = {
            "lügen": ["lüg", "log", "gelogen", "verschweig", "betrog", "täusch", "schwindel"],
            "geld": ["geld", "euro", "gekauft", "teuer", "billig", "spar", "geizig", "verschuldet"],
            "essen": ["gegessen", "geschlemmt", "völlerei", "schokolade", "pizza", "burger", "süß"],
            "faul": ["faul", "netflix", "nichts getan", "prokrastination", "aufgeschoben", "rumgelegen"],
            "neid": ["neidisch", "beneid", "gönne nicht", "unfair", "warum haben die"]
        }
        self.schulden_mapping = {
            "lügen": 2,
            "geld": 1,
            "essen": 1,
            "faul": 2,
            "neid": 3,
            "standard": 0
        }
        
        self.emotionen_mapping = {
            "lügen": "urteilend",
            "geld": "genervt",
            "essen": "lachend",
            "faul": "genervt",
            "neid": "schockiert",
            "standard": "neutral"
        }

    def berechne_schulden(self, kategorie):
        return self.schulden_mapping.get(kategorie, 0)


    """Bestimmt die Kategorie einer Sünde basierend auf Keywords"""
    def kategorisiere_suende(self, text):


        """macht alle char in der Eingabe klein"""
        text_lower = text.lower()

        for kategorie, wörter in self.keywords.items():
            for wort in wörter:
                if wort in text_lower:
                    return kategorie
        return "standard"

    """Gibt eine zufällige Antwort für die Kategorie zurück"""
    def get_antwort(self, kategorie):

        antworten_liste = self.antworten.get(kategorie, self.antworten["standard"])
        return random.choice(antworten_liste)

    """Prüft auf spezielle Easter Eggs und gibt entsprechende Antworten"""
    def prüfe_easter_eggs(self, text):

        text_lower = text.lower()

        if any(wort in text_lower for wort in ["katze", "hund", "tier"]):
            return "Tiere sind unschuldig! Du hingegen... NICHT", "schockiert"
        elif "mutter" in text_lower or "mama" in text_lower:
            return "Deine Mutter ist enttäuscht. Sehr enttäuscht.", "urteilend"
        elif len(text) > 200:
            return "SO viel Text für SO wenig Moral? Beeindruckend! ", "lachend"

        return None, None