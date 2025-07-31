# UI/UX-Modernisierung: Cyberpunk-Redesign "Der Sarkastische Beichtstuhl"

## 1. Blocker beheben

### a) QSS-Build-Pipeline
- **Template erstellen:** Lege `design_tokens/style_template.qss` mit Platzhaltern an (z.B. `$bg.base`, `$accent.1`).
- **Build-Skript implementieren:** Erstelle `design_tokens/build_style.py` zum dynamischen Ersetzen der Platzhalter aus `design_tokens.json`.
  ```python
  import json, re, pathlib
  toks = json.load(open("design_tokens/design_tokens.json"))
  def grad(c1, c2): return f"qlineargradient(x1:0,y1:0,x2:1,y2:1, stop:0 {c1}, stop:1 {c2})"
  toks["gradients"] = {"neon_primary": grad(toks["colors"]["accent"]["1"],
                                            toks["colors"]["accent"]["2"])}
  tpl  = pathlib.Path("design_tokens/style_template.qss").read_text()
  out  = re.sub(r"\$([A-Za-z0-9_\.]+)",
                lambda m: eval("toks['" + m.group(1).replace('.', "']['") + "']"),
                tpl)
  pathlib.Path("design_tokens/app.qss").write_text(out, encoding="utf-8")
  ```
- **Integration:** Führe das Skript in `main.py` vor dem `QApplication`-Start aus und lade das generierte `app.qss`.

### b) Fonts
- **Konvertierung:** Konvertiere die Schriftarten **Orbitron**, **Inter** und **JetBrains Mono** in das **OTF-Format**.
- **Resource-Datei:** Lege `resources/fonts.qrc` an und binde die OTF-Dateien ein.
- **Laden beim Start:** Integriere folgenden Code in den App-Start:
  ```python
  from PyQt6.QtGui import QFontDatabase
  for f in [":/fonts/Orbitron-Regular.otf", ":/fonts/Inter-Regular.otf",
            ":/fonts/JetBrainsMono-Regular.otf"]:
      assert QFontDatabase.addApplicationFont(f) != -1, f"Font {f} failed"
  ```

## 2. Design-System

### `design_tokens/design_tokens.json`
```json
{
  "colors": {
    "bg":  { "base": "#0E1222", "panel": "#141826" },
    "accent": { "1": "#00E5FF", "2": "#FF00A8", "warn": "#FFC400",
                "success": "#00FF88", "error": "#FF3860" },
    "text": { "primary": "#EDEFFF", "secondary": "#9CA1C6" }
  },
  "radius": { "sm": 6, "md": 12 },
  "spacing": { "1": 4, "2": 8, "3": 16 },
  "fonts": { "headline": "Orbitron", "body": "Inter", "mono": "JetBrains Mono" }
}
```

### `style_template.qss` (Auszug)
```qss
QMainWindow { background:$bg.base; color:$text.primary; }
.card { border-radius:$radius.mdpx; background:rgba(255,255,255,0.04); backdrop-filter:blur(6px); }
QPushButton[class="primary"] {
    font-family:$fonts.body; font-weight:500; text-transform:uppercase;
    padding:6px 14px; border:0; border-radius:$radius.smpx;
    background:$gradients.neon_primary; color:$bg.base; transition:all .2s;
}
QPushButton[class="primary"]:hover { transform:translateY(-1px); }
QLineEdit { background:$bg.panel; border:1px solid #1F2539; border-radius:$radius.smpx; padding:6px; }
QProgressBar::chunk { background:$gradients.neon_primary; }
```

## 3. UI-Komponenten
- **NeonButton:** Erbt von `QPushButton`, setzt `setProperty("class", "primary")` und nutzt `QGraphicsDropShadowEffect` für einen Shadow-Glow.
- **CardWidget:** Setzt `setObjectName("card")` und verwendet ein Grid-Layout für den "Glass Panel"-Effekt.
- **NeonLineEdit:** Erbt von `QLineEdit` mit einer `caret-color`, die auf `accent.1` gesetzt ist.

## 4. Layout-Refactor
- **Hauptfenster:** Ein 12-Spalten `QGridLayout` verwenden, Spalten-Stretch auf `[1,1,...]` setzen.
- **Anordnung:** Links eine Text-Input-Card, rechts eine Monk-Visualizer-Card.
- **Action-Bar:** Buttons in einem "Sticky Footer" am unteren Rand platzieren.

## 5. Visuelle Effekte
- **Parallax-Background:** `QGraphicsView` mit Layern (`nebula.png`, `scanlines.png`), die auf Mausbewegungen reagieren (`translate dx/dy = mouse*0.02`).
- **Typewriter-Effekt:** Text im Response-Label wird buchstabenweise mit einem 25ms Timer animiert.
- **Monk Lottie-Animationen:** Implementiere Zustände für den Mönch via QtLottie: `idle`, `angry`, `laugh`, `sad`, `shocked`.

## 6. Accessibility
- **Widget-Beschreibungen:** Für alle interaktiven Widgets `setAccessibleName/Description` setzen.
- **Tab-Reihenfolge:** `setTabOrder()` für eine logische Navigation implementieren.
- **Kontrast-Audit:** Ein Skript erstellen, das die Farbkontraste prüft und bei Fehlern den CI-Build fehlschlagen lässt.

## 7. CI/CD (`.github/workflows/ci.yml`)
```yaml
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Python
        uses: actions/setup-python@v5
        with: { python-version: '3.11' }
      - run: pip install ruff mypy pytest pytest-qt playwright
      - run: playwright install --with-deps
      - run: ruff .
      - run: mypy beichtsthul_modern
      - run: pytest
```

## 8. Review-Checkliste
- [ ] Neon-Gradient-Buttons mit Glow-Effekt
- [ ] Glass-Panels auf allen Cards/Dialogen
- [ ] Orbitron/Inter/Mono werden korrekt gerendert
- [ ] Parallax-Background bewegt sich flüssig (60 fps)
- [ ] Typewriter-Antwort hat < 70 ms Lag
- [ ] A11y: Kontrast ≥ 4.5:1, vollständige Tastatur-Navigation
- [ ] `python main.py` startet ohne Stylesheet- oder Font-Fehler
- [ ] CI-Workflow ist grün

## 9. Implementierungs-Reihenfolge
1.  **Blocker fixen:** `build_style.py` + Fonts (0.5 Tage)
2.  **QSS-Template** fertigstellen (0.5 Tage)
3.  **Komponenten** (NeonButton, Card, LineEdit) (1 Tag)
4.  **Layout-Grid** umstellen (0.5 Tage)
5.  **Parallax + Lottie-Monk** (1 Tag)
6.  **Typewriter- & Snackbar-UX** (0.5 Tage)
7.  **A11y Auditing** (0.5 Tage)
8.  **CI-Pipeline & Tests** (1 Tag)