# Beichtstuhl Modern - Style Guide

## Design System

Dieser Style Guide dokumentiert das Design-System der "Sarkastischen Beichtstuhl" Anwendung. Das System basiert auf Design Tokens, die in `design_tokens/design_tokens.json` definiert sind.

## Farbpalette

### Basisfarben

| Token | Wert | Verwendung |
|-------|------|------------|
| `bg-base` | `#0d0f1a` | Haupt-Hintergrundfarbe |
| `bg-panel` | `#141826` | Karten und Dialog-Hintergründe |
| `text-primary` | `#e0e0ff` | Primärer Text |
| `text-secondary` | `#a0a0c0` | Sekundärer Text |

### Akzentfarben

| Token | Wert | Verwendung |
|-------|------|------------|
| `accent-primary` | `#00eaff` | Primäre Akzentfarbe (Neon Cyan) |
| `accent-secondary` | `#ff0078` | Sekundäre Akzentfarbe (Neon Magenta) |
| `accent-warn` | `#ffb300` | Warnfarbe (Amber) |
| `accent-error` | `#ff3860` | Fehlerfarbe (Neon Rot) |
| `accent-success` | `#00ff7f` | Erfolgsfarbe (Neon Grün) |

## Typografie

### Schriftarten

| Typ | Schriftart | Verwendung |
|-----|------------|------------|
| Überschriften | Orbitron | Titel, Header |
| Fließtext | Inter | Body-Text |
| Monospace | JetBrains Mono | Statistiken, Code |

### Schriftgrößen

| Token | Wert | Verwendung |
|-------|------|------------|
| `headline-h1` | 28px | Hauptüberschriften |
| `headline-h2` | 22px | Abschnittsüberschriften |
| `headline-h3` | 18px | Unterüberschriften |
| `headline-h4` | 16px | Kleine Überschriften |
| `body` | 14px | Fließtext |
| `caption` | 12px | Beschriftungen |
| `mono` | 12px | Monospace-Text |

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
| `button` | 4px | Schaltflächen |
| `card` | 8px | Karten, Dialoge |

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
- Farbe: Akzentfarbe

#### Glassmorphism
- Hintergrund: rgba(255, 255, 255, 0.07)
- Backdrop Blur: 6px

#### VHS Scanlines
- Opazität: 0.1
- Geschwindigkeit: 30fps

## Komponenten

### Buttons

```css
QPushButton {
    background: linear-gradient(135deg, @accent-primary, @accent-secondary);
    color: @bg-base;
    border: none;
    border-radius: @radius-button;
    padding: @spacing-base @spacing-component;
    font-family: @font-body-family;
    font-size: @font-body-size-body;
    font-weight: @font-body-weight-bold;
    min-height: 30px;
}

QPushButton:hover {
    box-shadow: 0 0 10px @accent-primary;
}

QPushButton:pressed {
    transform: scale(0.96);
}
```

### Text Input

```css
QTextEdit, QLineEdit {
    background-color: rgba(20, 24, 38, 0.7);
    color: @text-primary;
    border: 2px solid @bg-panel;
    border-radius: @radius-button;
    padding: @spacing-base;
    font-family: @font-mono-family;
    font-size: @font-mono-size-default;
}
```

### Karten

```css
QWidget#card {
    background-color: rgba(20, 24, 38, 0.7);
    border-radius: @radius-card;
    padding: @spacing-component;
    border: 1px solid @bg-panel;
    backdrop-filter: blur(6px);
}
```

## Barrierefreiheit

### Farbkontraste

Alle Farbkombinationen erfüllen die WCAG 2.1 AA-Anforderungen (>4.5:1 Kontrastverhältnis):

- `text-primary` auf `bg-base`: 15.21:1
- `text-secondary` auf `bg-base`: 8.47:1
- `accent-primary` auf `bg-base`: 12.89:1

### Tastaturnavigation

- Alle interaktiven Elemente sind über Tab erreichbar
- Fokus-Indikator mit Akzentfarbe
- Mindestzielgröße: 44px für Touch-Geräte

## Responsiveness

### Breakpoints

| Größe | Breite | Layout |
|-------|--------|--------|
| Kompakt | < 800px | Vertikales Layout |
| Standard | 800px - 1200px | Standard-Layout |
| Erweitert | > 1200px | Erweitertes Layout |

### 12-Spalten Grid

Das Layout basiert auf einem flexiblen 12-Spalten Grid-System mit prozentualen Breiten.