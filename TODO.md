# Beichtsthul UI/UX Modernization Project - Master Plan

## Project Overview
Modernize the Beichtsthul application UI/UX based on detailed analysis and recommendations from UI/UX expert feedback.

## Current State Analysis

### UI Issues Identified
1. **Color System**: Very dark blue-gray (#1A1B26) with pale orange headline - low contrast, monotonous
2. **Typography**: Standard Qt Sans, no size hierarchy - generic look, poor scanability
3. **Layout**: Rigid central canvas, fixed-width buttons, large empty spaces - inefficient space usage, not responsive
4. **Controls**: Flat buttons with gray background, no hover/focus state - outdated, poor feedback
5. **Graphics**: Bitmap monk, gradient background - 90s look
6. **Progress Bar & Labels**: Standard Qt widgets - inconsistent styling
7. **Accessibility**: Poor focus rectangle visibility, contrast < 4.5:1 - not WCAG compliant

### Technical Assessment
- **Framework**: PyQt6 (Widgets-based), modular structure (core/ui/utils/assets)
- **Styles**: Central styles.py generates QSS strings; color/spacing constants hardcoded in constants.py
- **Components**: Reusable widget classes but without clear design token binding
- **Assets**: Icons & graphics as PNG; sounds as WAV/MP3; no vector/Lottie files
- **Build/Test**: No automated UI tests; rudimentary CLI scripts; CI/CD missing
- **Documentation**: README.md outlines modernization goals, TODO.md lists open points, but no detailed acceptance criteria or style guides

## Master Plan for UI/UX Modernization

### Phase 0 - Concept & Design (3 Days)

#### Design Audit
- [ ] Capture screenshots of all existing views
- [ ] Catalog inconsistencies and issues
- [ ] Document current user flows (Beichten, Statistik, Reset)

#### Goal Definition
- [ ] Define primary user flows as journey maps
- [ ] Establish AAA benchmarks (see Appendix A)

#### Figma Setup
- [ ] Create design system file with foundations:
  - Color tokens (Light/Dark, Accent variants, Semantic states)
  - Typography scale (H1-H6, Subtitle, Body, Caption)
  - 8px spacing grid, border radiuses (4/8/12px)
- [ ] Create first high-fidelity mockups:
  - Main window
  - Settings dialog
  - Statistics dashboard

#### Deliverables
- [ ] Figma link
- [ ] Audit report (PDF)
- [ ] Final style guide draft

### Phase 1 - Technical Foundation (5 Days)

#### Repository Reorganization
- [ ] Create `/design_tokens/` directory (JSON + Python enum generator)
- [ ] Create `/ui_qml/` for QML front-end
- [ ] Create `/widgets_legacy/` transition layer for existing PyQt widget logic

#### Qt Quick Controls 2 Migration
- [ ] Implement main window and navigation as QML
- [ ] Create QML plugin "Beichtstuhl.Controls" with custom components:
  - Button
  - TextField
  - ProgressBar
  - SnackBar

#### Theme Engine
- [ ] Implement loading of design_tokens.json
- [ ] Convert to QML theme singleton
- [ ] Implement runtime switcher for Light/Dark/High-Contrast themes

#### Resource Pipeline
- [ ] Replace icons with Phosphor/Material Symbols as SVG
- [ ] Replace graphics with Lottie JSON (Monk, animated backgrounds)
- [ ] Implement font embedding (Inter/JetBrains Mono)

#### Deliverables
- [ ] Buildable QML skeleton
- [ ] Token JSON files
- [ ] Script generate_qss.py (fallback for widget overlay screens)

### Phase 2 - Core Screens & Components (8 Days)

#### Component Implementation
- [ ] Start/Confession Screen:
  - Responsive grid (Header, Input-Card, Action-Bar)
  - Requirement: 1280×800 and 1920×1080 without horizontal scrolling
- [ ] Input-Card:
  - Elevated container
  - Emoji prefix
  - Character counter (colors to error-red when >500 characters)
- [ ] Action-Button:
  - Primary (Accent)
  - Secondary (Surface variant)
  - Loading spinner
  - Hover (opacity 85%) / Pressed (scale 0.97)
- [ ] Karma-Bar:
  - Custom LinearGradientProgress with discreet ticks + tooltip
  - Requirement: 60fps, no rasterization on HiDPI
- [ ] Dialog-"Statistics":
  - Tabs: Chart (QtCharts), History-List (Virtualized)
  - Requirement: DPI-aware, fully keyboard-navigable
- [ ] Settings:
  - Theme picker
  - Sound toggle
  - Data export
  - Requirement: Changes are live without app restart

#### Implementation Notes
- [ ] Use QML state machines for screen transitions (Fade-In 200ms, Shared-Z-Axis Elevation)
- [ ] Implement all texts via Qt Linguist (tr() wrappers)
- [ ] Support base languages de, en

### Phase 3 - Micro-Interactions & Motion (4 Days)

#### Easing Curves
- [ ] Standard Easing.InOutCubic
- [ ] Special cases ElasticOut for fun elements

#### Feedback Layer
- [ ] Snackbar for successful confession
- [ ] Shake animation + color flash for error input

#### Sound Design
- [ ] Replace WAV files with OGG-Vorbis
- [ ] Load via QSoundEffect
- [ ] Make volume adjustable in settings
- [ ] Implement master mute shortcut (Ctrl+M)

### Phase 4 - Accessibility & Compliance (3 Days)

#### WCAG 2.1 AA Color Contrast
- [ ] Implement token audit script
- [ ] Create GitHub Action for automatic PR fail under 4.5:1 contrast

#### Keyboard Navigation
- [ ] Implement Keys.onPressed handlers
- [ ] Set manual TabOrder

#### Screen Reader Support
- [ ] Add Accessible.name & description for all controls

#### Localization
- [ ] Implement pseudoloc test
- [ ] Create translation length check CI job

## Implementation Priority

### Critical Issues to Address First
1. Color system modernization with proper contrast ratios
2. Typography hierarchy implementation
3. Responsive layout system
4. Interactive state styling for controls
5. Vector graphics implementation
6. Accessibility compliance

### Quick Wins (Can be implemented immediately)
1. Update color palette to meet WCAG contrast requirements
2. Implement typography scale with proper hierarchy
3. Add hover/focus states to buttons
4. Replace bitmap monk with vector version
5. Improve progress bar styling consistency

## Design System Requirements

### Color Tokens
- Primary Background: Deep Dark Blue (#1a1b26)
- Secondary Background: Charcoal Gray (#2a2b3d)
- Surface Background: Dark Gray (#3a3b5c)
- Primary Accent: Electric Blue (#7aa2f7)
- Secondary Accent: Bright Teal (#73daca)
- Emotional Accent: Vibrant Orange (#ff9e64)
- Success: Emerald Green (#9ece6a)
- Warning: Golden Yellow (#e0af68)
- Error: Soft Red (#f7768e)
- Primary Text: Light Gray (#c0caf5)
- Secondary Text: Medium Gray (#9aa5ce)
- Disabled Text: Dark Gray (#565f89)

### Typography Scale
- H1: 28px Semi-bold
- H2: 22px Medium
- H3: 18px Medium
- H4: 16px Regular
- H5: 15px Regular
- H6: 14px Regular
- Subtitle: 16px Medium
- Body: 15px Regular
- Caption: 13px Regular
- Small: 12px Regular

### Spacing System
- Base Unit: 8px grid system
- Component Padding: 16px (2 units)
- Element Spacing: 12px (1.5 units)
- Section Spacing: 24px (3 units)

### Component Specifications
- Border Radius: 8px for cards, 4px for buttons
- Elevation: 2px for cards, 4px for elevated elements
- Animation Duration: 200-300ms for transitions

## Acceptance Criteria

### Visual Design
- [ ] Color contrast ratios meet WCAG 2.1 AA standards
- [ ] Typography hierarchy clearly differentiates content levels
- [ ] Consistent spacing and alignment throughout the interface
- [ ] Modern, polished visual aesthetic

### Interaction Design
- [ ] All interactive elements have clear hover, focus, and active states
- [ ] Micro-interactions provide meaningful feedback
- [ ] Transitions are smooth and purposeful
- [ ] Keyboard navigation is fully supported

### Responsiveness
- [ ] Layout adapts to different screen sizes (1280×800 to 1920×1080)
- [ ] Components resize appropriately
- [ ] Text remains readable at all sizes
- [ ] Touch targets meet minimum size requirements

### Accessibility
- [ ] Screen reader support for all interface elements
- [ ] Keyboard navigation for all functionality
- [ ] Sufficient color contrast for text and interactive elements
- [ ] Proper focus management

### Performance
- [ ] Smooth animations at 60fps
- [ ] Efficient resource loading
- [ ] Fast application startup
- [ ] Responsive interactions

## Appendix A - AAA Benchmarks

### Reference Applications
1. Discord - Modern dark theme implementation
2. Visual Studio Code - Consistent UI components and theming
3. Slack - Responsive layout and micro-interactions
4. Figma - Design system implementation and component library

### Quality Standards
- Material Design 3 guidelines
- WCAG 2.1 AA compliance
- Responsive web design principles
- Modern animation best practices