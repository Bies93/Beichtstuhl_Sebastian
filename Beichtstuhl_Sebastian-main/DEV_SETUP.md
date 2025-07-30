# Entwicklungsumgebung einrichten

## Voraussetzungen

- Python 3.8 oder neuer
- pip Paketmanager
- Git

## Projekt einrichten

### 1. Repository klonen

```bash
git clone https://github.com/your-username/beichtstuhl.git
cd beichtstuhl
```

### 2. Virtuelle Umgebung erstellen

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oder
venv\Scripts\activate  # Windows
```

### 3. Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

## Projektstruktur

```
beichtsthul_modern/
├── core/              # Geschäftslogik (Antwortgenerator, Karma-Rechner, Datei-Manager)
├── ui/                # Benutzeroberfläche (Hauptfenster, Komponenten)
├── assets/            # Ressourcen (Bilder, Sounds, Schriftarten, Animationen)
├── design_tokens/     # Design-System (Tokens, Generator, Styles)
├── utils/             # Hilfsfunktionen (Ressourcen-Loader, Animationen)
├── tests/             # Unit-Tests
└── main.py           # Haupteinstiegspunkt
```

## Design-Token-System

### Token-Generator verwenden

Die Design-Tokens werden aus `design_tokens/design_tokens.json` generiert:

```bash
cd beichtsthul_modern/design_tokens
python generate_tokens.py
```

Dies erzeugt:
- `design_tokens.py` - Python-Enums für die Tokens
- `style.qss` - QSS-Variablen für die Stylesheets

### Neue Tokens hinzufügen

1. Ändern Sie `design_tokens.json`
2. Führen Sie den Generator aus: `python generate_tokens.py`
3. Verwenden Sie die neuen Tokens in Ihrem Code

## Entwicklungstools

### Tests ausführen

```bash
python beichtsthul_modern/tests/run_tests.py
```

### Einzelne Testdatei ausführen

```bash
python -m pytest beichtsthul_modern/tests/test_antwort_generator.py -v
```

### Linting

```bash
# Mit flake8
flake8 beichtsthul_modern/

# Mit pylint
pylint beichtsthul_modern/
```

## UI-Entwicklung

### Stylesheets

Die Stylesheets werden aus Design-Tokens generiert. Ändern Sie nicht die `.qss`-Dateien direkt, sondern:
1. Ändern Sie die Tokens in `design_tokens.json`
2. Führen Sie den Generator aus
3. Die Änderungen werden automatisch in die Anwendung übernommen

### Neue Komponenten erstellen

1. Erstellen Sie eine neue Datei im `ui/components/` Verzeichnis
2. Erben Sie von `QWidget` oder einer anderen passenden Qt-Klasse
3. Verwenden Sie die Design-Tokens für Farben, Abstände etc.
4. Fügen Sie die Komponente in `ui/__init__.py` hinzu

### Animationen

#### Neue Lottie-Animationen hinzufügen

1. Fügen Sie die `.json` Datei zu `assets/animations/` hinzu
2. Registrieren Sie die Animation im `LottiePlayer`
3. Verwenden Sie die Animation in Ihren Komponenten

#### Soundeffekte

1. Fügen Sie `.wav` Dateien zu `assets/sounds/` hinzu
2. Laden Sie die Sounds mit dem `SoundManager`
3. Spielen Sie die Sounds bei entsprechenden Ereignissen ab

## Hochauflösende Anzeige (High-DPI)

Die Anwendung unterstützt automatisch High-DPI-Anzeigen. Bei der Entwicklung:
- Verwenden Sie immer relative Einheiten aus den Design-Tokens
- Testen Sie auf verschiedenen DPI-Einstellungen
- Verwenden Sie SVG-Symbole für scharfe Darstellung

## Barrierefreiheit

### Tastaturnavigation

- Alle interaktiven Elemente müssen über die Tab-Taste erreichbar sein
- Verwenden Sie `setTabOrder()` für benutzerdefinierte Navigationsreihenfolgen
- Implementieren Sie sinnvolle Tastenkürzel

### Screen Reader Unterstützung

- Fügen Sie `setAccessibleName()` und `setAccessibleDescription()` zu allen Widgets hinzu
- Verwenden Sie semantische Struktur (Überschriften, Labels etc.)

## Performance

### Animationen

- Ziel: 60 FPS auf moderner Hardware
- Verwenden Sie Hardware-Beschleunigung wo möglich
- Optimieren Sie komplexe Animationen

### Ressourcen-Management

- Verwenden Sie den `ResourceLoader` für alle Assets
- Implementieren Sie Caching für häufig verwendete Ressourcen
- Laden Sie Ressourcen asynchron wenn möglich

## Debugging

### Logging

Die Anwendung verwendet Pythons eingebautes Logging-Modul:

```python
import logging
logger = logging.getLogger(__name__)
logger.debug("Debug-Nachricht")
logger.info("Info-Nachricht")
logger.warning("Warnung")
logger.error("Fehler")
```

### Entwicklungsmodus

Starten Sie die Anwendung mit dem `--debug` Flag für zusätzliche Debug-Informationen:

```bash
python beichtsthul_modern/main.py --debug
```

## Erstellung (Build)

### Ausführbare Datei erstellen

```bash
pyinstaller --onefile beichtsthul_modern/main.py
```

### Installer erstellen

Für Windows:
```bash
# Erfordert: pip install cx_Freeze
python setup.py bdist_msi
```

## Versionskontrolle

### Commit-Nachrichten

Verwenden Sie das Conventional Commits Format:

```
feat: Neue Funktion hinzugefügt
fix: Fehler behoben
docs: Dokumentation aktualisiert
style: Code-Formatierung
refactor: Code-Refactoring
test: Tests hinzugefügt
chore: Wartungsaufgaben
```

### Branching-Strategie

- `main` - Stabile Hauptversion
- `develop` - Entwicklungszweig
- `feature/*` - Feature-Zweige
- `hotfix/*` - Hotfix-Zweige
- `release/*` - Release-Vorbereitung

## Problemlösung

### Bekannte Probleme

#### ImportError: No module named 'beichtsthul_modern'

Stellen Sie sicher, dass Sie sich im Projektverzeichnis befinden und die Python-Pfade korrekt sind.

#### UI sieht nicht wie erwartet aus

1. Überprüfen Sie, ob der Token-Generator ausgeführt wurde
2. Stellen Sie sicher, dass die Styles korrekt angewendet werden
3. Überprüfen Sie die Konsole auf Fehlermeldungen

#### Tests schlagen fehl

1. Überprüfen Sie, ob alle Abhängigkeiten installiert sind
2. Stellen Sie sicher, dass keine externen Prozesse Dateien sperren
3. Führen Sie die Tests einzeln aus, um das Problem zu isolieren

### Support

Bei Fragen wenden Sie sich an das Entwicklungsteam oder erstellen Sie ein Issue im GitHub-Repository.