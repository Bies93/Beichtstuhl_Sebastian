# Beichtstuhl Modern - Style Guide

## Modern Neon-Cyberpunk Design System

This style guide documents the updated design system for the "Sarkastischen Beichtstuhl" application, featuring a modern neon-cyberpunk aesthetic with enhanced accessibility and responsive design.

## Design System

Dieser Style Guide dokumentiert das aktualisierte Design-System der "Sarkastischen Beichtstuhl" Anwendung mit modernem Neon-Cyberpunk-Stil. Das System basiert auf Design Tokens, die in `design_tokens/design_tokens.json` definiert sind.

## Farbpalette

### Basisfarben

| Token | Wert | Verwendung |
|-------|------|------------|
| `bg-base` | `#0E1222` | Haupt-Hintergrundfarbe |
| `bg-panel` | `#141826` | Karten und Dialog-Hintergründe |
| `text-primary` | `#EDEFFF` | Primärer Text (verbesserte Kontraste) |
| `text-secondary` | `#B8BCE6` | Sekundärer Text (verbesserte Kontraste) |

### Akzentfarben

| Token | Wert | Verwendung |
|-------|------|------------|
| `accent-1` | `#00E5FF` | Primäre Akzentfarbe (Neon Cyan) |
| `accent-2` | `#FF00A8` | Sekundäre Akzentfarbe (Neon Magenta) |
| `accent-warn` | `#FFC400` | Warnfarbe (Neon Gelb) |
| `accent-error` | `#FF3860` | Fehlerfarbe (Neon Rot) |
| `accent-success` | `#00FF88` | Erfolgsfarbe (Neon Grün) |

## Typografie

### Schriftarten

| Typ | Schriftart | Verwendung |
|-----|------------|------------|
| Überschriften | Orbitron | Titel, Header (H1: 28px, H2: 22px, H3: 18px) |
| Fließtext | Inter | Body-Text (14px) |
| Monospace | JetBrains Mono | Statistiken, Code (12px) |

### Schriftgrößen

| Token | Wert | Verwendung |
|-------|------|------------|
| `headline-h1` | 28px | Hauptüberschriften (Orbitron) |
| `headline-h2` | 22px | Abschnittsüberschriften (Orbitron) |
| `headline-h3` | 18px | Unterüberschriften (Orbitron) |
| `headline-h4` | 16px | Kleine Überschriften (Orbitron) |
| `body` | 14px | Fließtext (Inter) |
| `caption` | 12px | Beschriftungen (Inter) |
| `mono` | 12px | Monospace-Text (JetBrains Mono) |

## Abstände

Das Design-System verwendet ein 8px Grid-System:

| Token | Wert | Verwendung |
|-------|------|------------|
| `base` | 8px | Basiseinheit |
| `component` | 16px | Komponenten-Padding |
| `element` | 12px | Elementabstand |
| `section` | 24px | Abschnittsabstand |

## Border Radius

| Token | Wert | Verwendung |
|-------|------|------------|
| `sm` | 8px | Schaltflächen, kleine Elemente |
| `md` | 12px | Karten, Dialoge |

## Animationen

### Dauer

| Token | Wert | Verwendung |
|-------|------|------------|
| `fast` | 100ms | Schnelle Übergänge |
| `normal` | 200ms | Normale Übergänge |
| `slow` | 300ms | Langsame Übergänge |
| `transition` | 250ms | Szenenübergänge |

### Effekte

#### Neon Glow
- Blur: 6px
- Spread: 0px
- Farbe: Akzentfarbe (Cyan-Magenta-Gradient)

#### Glassmorphism
- Hintergrund: rgba(255, 255, 255, 0.07)
- Backdrop Blur: 6px
- Border: 1px solid rgba(255, 255, 255, 0.05)

#### VHS Scanlines
- Opazität: 0.06
- Geschwindigkeit: 30fps

#### Parallax Background
- Nebula-Effekt: Procedural radial gradient
- Scanlines: Animated overlay
- Tiefen-Effekt: Multi-layer parallax

## Komponenten

### Buttons

```css
QPushButton[class="primary"] {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #00E5FF, stop:1 #FF00A8);
    color: #0E1222;
    border: none;
    border-radius: 8px;
    padding: 6px 14px;
    font-family: "Inter";
    font-weight: 500;
    text-transform: uppercase;
    min-height: 30px;
    min-width: 100px;
}

QPushButton[class="primary"]:hover {
    /* Elevation effect */
    transform: translateY(-2px);
}

QPushButton[class="primary"]:pressed {
    transform: scale(0.96);
}
```

### Text Input

```css
QTextEdit#glassTextEdit {
    background: rgba(255, 255, 255, 0.05);
    border: 2px solid #00E5FF;
    border-radius: 12px;
    padding: 10px;
    color: #EDEFFF;
    font-family: "Inter";
    font-size: 14px;
    selection-background-color: #00E5FF;
    selection-color: #0E1222;
}

QTextEdit#glassTextEdit:focus {
    border: 2px solid #00E5FF;
    box-shadow: 0 0 8px #00E5FF;
}
```

### Karten

```css
QWidget#card {
    background: rgba(255, 255, 255, 0.07);
    border-radius: 12px;
    padding: 15px;
    border: 1px solid rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(6px);
}
```

### Progress Bar

```css
QProgressBar#karmaProgressBar {
    background: rgba(255, 255, 255, 0.07);
    border-radius: 6px;
    border: none;
    height: 20px;
}

QProgressBar#karmaProgressBar::chunk {
    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #00E5FF, stop:1 #FF00A8);
    border-radius: 6px;
}
```

## Barrierefreiheit

### Farbkontraste

Alle Farbkombinationen erfüllen die WCAG 2.1 AA-Anforderungen (>4.5:1 Kontrastverhältnis):

- `text-primary` auf `bg-base`: 21.00:1
- `text-secondary` auf `bg-base`: 13.7:1
- `accent-primary` auf `bg-base`: 12.92:1

### Tastaturnavigation

- Alle interaktiven Elemente sind über Tab erreichbar
- Fokus-Indikator mit Akzentfarbe und Glow-Effekt
- Mindestzielgröße: 44px für Touch-Geräte
- Klare visuelle Hierarchie zwischen primären und sekundären Aktionen

### Screen Reader Unterstützung

- Alle interaktiven Elemente haben `accessibleName` und `accessibleDescription`
- Semantische Typzuweisungen für Labels (Header, Body, Caption)
- Logische Tab-Reihenfolge: Texteingabe → Beichten-Button → Statistiken-Button → Reset-Button

## Responsiveness

### Breakpoints

| Größe | Breite | Layout |
|-------|--------|--------|
| Kompakt | < 600px | Vertikales Layout (12/12) |
| Standard | 600px - 1000px | Standard-Layout (6/6) |
| Erweitert | > 1000px | Erweitertes Layout (7/5) |

### 12-Spalten Grid

Das Layout basiert auf einem flexiblen 12-Spalten Grid-System mit prozentualen Breiten:
- Kompakt: Alle Elemente übereinander (12 Spalten für jede Komponente)
- Standard: Gleiches Verhältnis (6 Spalten für Eingabe, 6 Spalten für Visualisierung)
- Erweitert: Harmonisches Verhältnis (7 Spalten für Eingabe, 5 Spalten für Visualisierung)

### Dynamische Schriftgrößen

- Kompakt: 10px Basisgröße
- Standard: 12px Basisgröße
- Erweitert: 14px Basisgröße

## Visuelle Komponenten

### Monk Visualizer

- Größe: 280×280px
- Animation: Lottie-Dateien mit Emotionen (idle, angry, laughing, sad, shocked)
- Glow-Effekt: Akzentfarbe-Gradient-Ring
- Platzierung: Rechte Spalte oben

### Karma-Anzeige

- Header: "Karma Status" in Orbitron 18px
- Skull-Icon: Akzentfarbe-Gradient
- Progress Bar: Animierter Cyan-Magenta-Gradient
- Status-Text: Neon-Grün bei niedrigem Karma, Amber bei mittlerem Karma, Neon-Rot bei hohem Karma

### Texteingabe

- Glass-Panel-Effekt: rgba(255, 255, 255, 0.05) mit 6px Blur
- Neon-Rand: 2px Cyan bei Fokus
- Platzhaltertext: Sekundärer Text
- Höhe: Dynamisch bis max. 120px

## Animationen und Übergänge

### Allgemeine Übergänge

- Button-Hover: 200ms Ease-Out
- Button-Press: 100ms Ease-In
- Text-Fokus: 200ms Ease-Out
- Monk-Emotion: 300ms Ease-Out
- Karma-Änderung: 500ms Ease-Out

### Spezialeffekte

- Parallax-Hintergrund: Mauspositionsbasierte Verschiebung
- Neon-Glow: Box-Shadow mit Akzentfarbe
- Glassmorphism: Backdrop-Blur und halbtransparente Hintergründe
- Text-Typewriter: Zeichenweise Enthüllung bei Antworten