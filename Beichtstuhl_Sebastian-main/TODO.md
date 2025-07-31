# UI/UX-Modernisierung: Cyberpunk-Redesign "Der Sarkastische Beichtstuhl"

## 1. Lottie Rendering - Monk Visualizer
- [ ] Integrate python-lottie with Pillow for frame rendering
- [ ] Replace placeholder code in `utils/lottie_player.py` with actual Lottie frame rendering
- [ ] Map Karma-Events → MonkVisualizer.set_emotion() (idle/angry/laugh/sad/shocked)
- [ ] Test all monk animations load and play correctly

## 2. Kontrast & Farben - Accessibility Improvements
- [ ] Replace placeholder gray #3A3C4F with $text.secondary (#9CA1C6)
- [ ] Increase card border color from #11131F to $bg.panel*1.2 = #1A1D2B for better visibility
- [ ] Replace PNG skull icon with Phosphor SVG (phosphor_svg/skull.svg)
- [ ] Run contrast-audit script; fail on < 4.5 : 1
- [ ] Verify all text elements meet WCAG-Kontrast 4.5 : 1

## 3. Interaktion / States - Enhanced User Feedback
- [ ] NeonButtons: Hover ⇒ Shadow-radius → 12 px, scale 1.02; Pressed ⇒ scale 0.97
- [ ] QPlainTextEdit: Focus border neon-cyan + glow effect
- [ ] Add keyboard focus-ring (outline 2 px accent-cyan) for all QPushButton
- [ ] Implement proper hover/pressed animations for all interactive elements

## 4. Layout-Feinschliff - Visual Polish
- [ ] Move Karma value "56" right-aligned by 12 px inward to prevent text from touching card edge
- [ ] Add 8 px vertical spacing between emoji and response text
- [ ] Align emoji/response text left margin to card padding
- [ ] Set ProgressBar background to rgba(255,255,255,0.08) and height to 10 px

## 5. Parallax & Glass Blur - Visual Depth
- [ ] Activate QGraphicsView layers with images/vhs_scanlines.gif + nebula.png
- [ ] Enable footer glass bar with blur-radius 6 px and backdrop-filter
- [ ] Verify parallax effect responds smoothly to mouse movement

## 6. Resource-Paths - Proper Asset Loading
- [ ] Use QResource paths in MonkVisualizer.animation_paths:
  - "qrc:/animations/monk_idle.json"
  - "qrc:/animations/monk_angry.json"
  - "qrc:/animations/monk_laughing.json"
  - "qrc:/animations/monk_sad.json"
  - "qrc:/animations/monk_shocked.json"
- [ ] Ensure app works from any current working directory

## 7. Accessibility & CI - Quality Assurance
- [ ] Set accessible names on Emoji-Label ("Status-Emoji"), Buttons, Progress-Bar
- [ ] Add Playwright screenshot diff test for "Monk visible" baseline
- [ ] Implement complete contrast audit in CI pipeline
- [ ] Verify all CI checks pass (ruff, mypy, pytest-qt, playwright)

## 8. Definition of Done - Final Verification
- [ ] Monk-Animation visible (60 fps) and changes based on Karma-State
- [ ] All Texts/Icons ≥ WCAG-Kontrast 4.5 : 1
- [ ] NeonButtons have Hover-Glow & Press-Scale; Keyboard-Focus clearly visible
- [ ] Glass-Footer + Parallax-Background create visual depth (Scanlines visible)
- [ ] CI-Pipeline (ruff, mypy, pytest-qt, playwright) green
- [ ] No PNG-Icons remaining in UI-tree; only SVG/Lottie