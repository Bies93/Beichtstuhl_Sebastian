# Der Sarkastische Beichtstuhl - Modern Edition

[![CI/CD Pipeline](https://github.com/your-username/beichtstuhl/actions/workflows/ci.yml/badge.svg)](https://github.com/your-username/beichtstuhl/actions/workflows/ci.yml)

Ein humorvoller Beichtstuhl mit Cyberpunk-Neon Design für alle, die ihre Sünden gestehen möchten - mit einer Prise Sarkasmus.

## Über das Projekt

Der "Sarkastische Beichtstuhl" ist eine moderne, interaktive Anwendung, die es Nutzern ermöglicht, ihre Sünden zu bekennen und sarkastische Antworten von einem virtuellen Mönch zu erhalten. Die Anwendung verfügt über ein ansprechendes Cyberpunk-Neon Design mit modernen UI/UX-Elementen.

### Features

- 🤖 **Sarkastischer Mönch**: Erhält sarkastische Antworten auf Ihre Beichte
- 🎨 **Cyberpunk-Neon Design**: Moderne, futuristische Benutzeroberfläche
- 📊 **Karma-Tracking**: Verfolgen Sie Ihre moralische Entwicklung
- 🎵 **Soundeffekte**: Immersive Audiosignale für ein besseres Erlebnis
- 🎭 **Animationen**: Lebendige Lottie-Animationen für verschiedene Emotionen
- 🎛️ **Responsive UI**: Funktioniert auf verschiedenen Bildschirmgrößen
- ♿ **Barrierefreiheit**: WCAG 2.1 AA konform
- 🌙 **Dark Mode**: Augenschonendes Design für nächtliche Beichten

## Technologie-Stack

- **Python 3.8+**
- **PyQt6** - GUI-Framework
- **Lottie** - Animationen
- **Phosphor Icons** - UI-Symbole
- **Design Tokens** - Konsistente Design-Sprache

## Installation

### Voraussetzungen

- Python 3.8 oder neuer
- pip Paketmanager

### Installationsschritte

1. Repository klonen:
   ```bash
   git clone https://github.com/your-username/beichtstuhl.git
   cd beichtstuhl
   ```

2. Virtuelle Umgebung erstellen (optional aber empfohlen):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # oder
   venv\Scripts\activate  # Windows
   ```

3. Abhängigkeiten installieren:
   ```bash
   pip install -r requirements.txt
   ```

4. Anwendung starten:
   ```bash
   python beichtsthul_modern/main.py
   ```

## Verwendung

1. Öffnen Sie die Anwendung
2. Geben Sie Ihre Sünde in das Textfeld ein
3. Klicken Sie auf "Beichten", um Ihre Beichte abzusenden
4. Erhalten Sie eine sarkastische Antwort vom Mönch
5. Verfolgen Sie Ihre Karma-Punkte im Statusbereich

### Tastenkürzel

- **Enter**: Beichte absenden
- **Ctrl+R**: Zurücksetzen
- **Ctrl+M**: Ton stummschalten
- **Ctrl+Q**: Anwendung beenden

## Entwicklung

### Projektstruktur

```
beichtsthul_modern/
├── core/           # Geschäftslogik
├── ui/             # Benutzeroberfläche
├── assets/         # Ressourcen (Bilder, Sounds, Fonts)
├── design_tokens/  # Design-System
├── utils/          # Hilfsfunktionen
└── tests/          # Unit-Tests
```

### Tests ausführen

```bash
python beichtsthul_modern/tests/run_tests.py
```

### Design-System

Das Projekt verwendet ein Design-Token-System für konsistente Farben, Abstände und Typografie. Die Tokens sind definiert in `design_tokens/design_tokens.json`.

## Mitwirken

Beiträge sind willkommen! Bitte beachten Sie:

1. Forken Sie das Repository
2. Erstellen Sie einen Feature-Branch (`git checkout -b feature/AmazingFeature`)
3. Committen Sie Ihre Änderungen (`git commit -m 'Add some AmazingFeature'`)
4. Pushen Sie zum Branch (`git push origin feature/AmazingFeature`)
5. Öffnen Sie einen Pull Request

## Lizenz

Dieses Projekt ist unter der MIT-Lizenz lizenziert - siehe die [LICENSE](LICENSE) Datei für Details.

## Kontakt

Ihr Name - [@your_twitter](https://twitter.com/your_twitter) - email@example.com

Projekt-Link: [https://github.com/your-username/beichtstuhl](https://github.com/your-username/beichtstuhl)

## Danksagung

- [Phosphor Icons](https://phosphoricons.com/) für die tollen Icons
- [Lottie](https://lottiefiles.com/) für die Animationen
- Alle Mitwirkenden, die dieses Projekt möglich gemacht haben