from tkinter import messagebox

"""Verwaltet und zeigt Statistiken an"""
class StatistikManager:


    def __init__(self):
        pass

    """Zeigt detaillierte Statistiken in einem Dialog"""
    def zeige_statistiken(self, karma_schulden, beicht_historie, suenden_kategorien):

        if not beicht_historie:
            messagebox.showinfo("Statistiken", "Noch keine Beichten vorhanden!")
            return

        stats_text = f"""
DEINE SÜNDEN-STATISTIKEN 

Gesamt Karma-Schulden: {karma_schulden}
Anzahl Beichten: {len(beicht_historie)}
Durchschnitt pro Beichte: {karma_schulden // len(beicht_historie) if beicht_historie else 0}

KATEGORIEN:
"""

        for kategorie, anzahl in suenden_kategorien.items():
            prozent = (anzahl / len(beicht_historie)) * 100
            stats_text += f"• {kategorie.title()}: {anzahl}x ({prozent:.1f}%)\n"

        if beicht_historie:
            stats_text += f"\n LETZTE BEICHTE:\n\"{beicht_historie[-1]['sünde'][:50]}...\""

        messagebox.showinfo("Deine Sünden-Statistiken", stats_text)

    """Fragt nach Bestätigung für Reset"""
    def bestätige_reset(self):

        return messagebox.askyesno("Reset", "Wirklich alle Sünden vergeben? ")
