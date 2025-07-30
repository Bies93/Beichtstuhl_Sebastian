#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Application Constants for Beichtsthul Modern
Contains all application-wide constants and configuration values.
"""

# Application Information
APP_NAME = "Der Sarkastische Beichtstuhl"
APP_VERSION = "2.0.0"
APP_AUTHOR = "Beichtsthul Developers"

# File Paths
DATA_FILE_NAME = "beichtstuh_daten_.json"

# Cyberpunk Neon Color Scheme Constants
# Base Background: Near Black
COLOR_PRIMARY_BG = "#0d0f1a"

# Panel Background: Cards, Dialogs
COLOR_SECONDARY_BG = "#141826"

# Primary Accent: Neon Cyan
COLOR_PRIMARY_ACCENT = "#00eaff"

# Secondary Accent: Neon Magenta
COLOR_SECONDARY_ACCENT = "#ff0078"

# Warning: Amber
COLOR_WARNING = "#ffb300"

# Error: Neon Red
COLOR_ERROR = "#ff3860"

# Success: Neon Green
COLOR_SUCCESS = "#00ff7f"

# Primary Text: Light Cyan
COLOR_PRIMARY_TEXT = "#e0e0ff"

# Secondary Text: Medium Gray
COLOR_SECONDARY_TEXT = "#a0a0c0"

# Disabled Text: Lighter Gray for better accessibility
COLOR_DISABLED_TEXT = "#8a91b8"

# Emotional Accent: Vibrant Orange (keeping for compatibility)
COLOR_EMOTIONAL_ACCENT = "#ff9e64"

# Monk Character Colors (Cyberpunk Styled)
COLOR_MONK_ROBE = "#8B4513"
COLOR_MONK_ROBE_ACCENT = "#5D2906"
COLOR_MONK_HOOD = "#191970"
COLOR_MONK_SKIN = "#D2B48C"
COLOR_MONK_ACCESSORIES = "#FFD700"

# Additional Cyberpunk Colors
COLOR_CYBERPUNK_NEON_BLUE = "#00eaff"
COLOR_CYBERPUNK_NEON_MAGENTA = "#ff0078"
COLOR_CYBERPUNK_NEON_PURPLE = "#bd00ff"
COLOR_CYBERPUNK_NEON_GREEN = "#00ff7f"
COLOR_CYBERPUNK_NEON_YELLOW = "#ffb300"
COLOR_CYBERPUNK_NEON_RED = "#ff3860"

# Font Constants (Cyberpunk Style)
FONT_HEADLINE = "Orbitron"
FONT_BODY = "Inter"
FONT_MONOSPACE = "JetBrains Mono"
FONT_FALLBACK = "Arial"

# Font Sizes (Cyberpunk Style)
FONT_SIZE_H1 = 28      # Title (Orbitron)
FONT_SIZE_H2 = 22      # Header (Orbitron)
FONT_SIZE_H3 = 18      # Subheader (Orbitron)
FONT_SIZE_H4 = 16      # Section header (Orbitron)
FONT_SIZE_H5 = 15      # Body (Inter)
FONT_SIZE_H6 = 14      # Small header (Inter)
FONT_SIZE_SUBTITLE = 16
FONT_SIZE_BODY = 14    # Body text (Inter)
FONT_SIZE_CAPTION = 12 # Caption (Inter)
FONT_SIZE_SMALL = 12   # Small text (Inter)
FONT_SIZE_BUTTON = 14  # Button text (Inter)
FONT_SIZE_MONO = 12    # Monospace (JetBrains Mono)

# Spacing Constants (8px grid system)
SPACING_BASE = 8
SPACING_COMPONENT = 16  # 2 units
SPACING_ELEMENT = 12    # 1.5 units
SPACING_SECTION = 24    # 3 units

# Border Radius
BORDER_RADIUS_CARD = 8
BORDER_RADIUS_BUTTON = 4

# Window Dimensions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WINDOW_MIN_WIDTH = 600
WINDOW_MIN_HEIGHT = 500

# Animation Durations (in milliseconds)
ANIMATION_WINDOW_FADE = 300
ANIMATION_WINDOW_EXIT = 200
ANIMATION_BUTTON_HOVER = 150
ANIMATION_BUTTON_PRESS = 100
ANIMATION_TEXT_FOCUS = 200
ANIMATION_MONK_EMOTION = 300
ANIMATION_KARMA_CHANGE = 500

# Emotion Mapping
EMOTION_MAPPING = {
    "lügen": "urteilend",
    "geld": "genervt",
    "essen": "lachend",
    "faul": "genervt",
    "neid": "schockiert",
    "standard": "neutral"
}

# Sünden Categories and Base Points
SUNDEN_CATEGORIES = {
    "lügen": 15,
    "geld": 12,
    "essen": 8,
    "faul": 5,
    "neid": 10,
    "standard": 7
}

# Karma Debt Mapping
KARMA_DEBT_MAPPING = {
    "lügen": 2,
    "geld": 1,
    "essen": 1,
    "faul": 2,
    "neid": 3,
    "standard": 0
}

# Penalty Words
PENALTY_WORDS = ["betrogen", "gestohlen", "verletzt", "absichtlich"]