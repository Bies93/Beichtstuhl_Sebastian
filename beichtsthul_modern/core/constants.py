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

# Color Scheme Constants
# Primary Background: Deep Dark Blue
COLOR_PRIMARY_BG = "#1a1b26"

# Secondary Background: Charcoal Gray
COLOR_SECONDARY_BG = "#2a2b3d"

# Surface Background: Dark Gray
COLOR_SURFACE_BG = "#3a3b5c"

# Primary Accent: Electric Blue
COLOR_PRIMARY_ACCENT = "#7aa2f7"

# Secondary Accent: Bright Teal
COLOR_SECONDARY_ACCENT = "#73daca"

# Emotional Accent: Vibrant Orange
COLOR_EMOTIONAL_ACCENT = "#ff9e64"

# Success: Emerald Green
COLOR_SUCCESS = "#9ece6a"

# Warning: Golden Yellow
COLOR_WARNING = "#e0af68"

# Error: Soft Red
COLOR_ERROR = "#f7768e"

# Primary Text: Light Gray
COLOR_PRIMARY_TEXT = "#c0caf5"

# Secondary Text: Medium Gray
COLOR_SECONDARY_TEXT = "#9aa5ce"

# Disabled Text: Dark Gray
COLOR_DISABLED_TEXT = "#565f89"

# Monk Character Colors
COLOR_MONK_ROBE = "#8B4513"
COLOR_MONK_ROBE_ACCENT = "#5D2906"
COLOR_MONK_HOOD = "#191970"
COLOR_MONK_SKIN = "#D2B48C"
COLOR_MONK_ACCESSORIES = "#FFD700"

# Font Constants
FONT_PRIMARY = "Segoe UI"
FONT_SECONDARY = "Roboto"
FONT_MONOSPACE = "Cascadia Code"
FONT_FALLBACK = "Arial"

# Font Sizes
FONT_SIZE_TITLE = 28
FONT_SIZE_HEADER = 22
FONT_SIZE_BUTTON = 16
FONT_SIZE_BODY = 15
FONT_SIZE_CAPTION = 13
FONT_SIZE_SMALL = 12

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