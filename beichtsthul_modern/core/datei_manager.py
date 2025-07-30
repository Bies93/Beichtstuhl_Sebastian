
import os
import json
from collections import defaultdict

class DateiManager:

    def __init__(self, dateiname="beichtstuh_daten_.json"):
        self.dateiname = dateiname

    def speichere_daten(self, karma_schulden, beicht_historie, suenden_kategorien):
        try:
            daten = {
                "karma_schulden": karma_schulden,
                "beicht_historie": beicht_historie,
                "suenden_kategorien": dict(suenden_kategorien)
            }
            with open(self.dateiname, "w", encoding="utf-8") as f:
                json.dump(daten, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"Fehler beim Speichern: {e}")
            return False

    def lade_daten(self):  # ← Richtig eingerückt!
        try:
            if os.path.exists(self.dateiname):
                with open(self.dateiname, "r", encoding="utf-8") as f:
                    daten = json.load(f)
                return (
                    daten.get("karma_schulden", 0),
                    daten.get("beicht_historie", []),
                    defaultdict(int, daten.get("suenden_kategorien", {}))
                )
        except Exception as e:
            print(f"Fehler beim Laden: {e}")
        return 0, [], defaultdict(int)