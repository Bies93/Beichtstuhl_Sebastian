#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Design Tokens for Beichtsthul Modern
Auto-generated from design_tokens.json
"""

from enum import Enum


class ColorTokens(Enum):
    """Color design tokens"""
    BG_BASE = "#0d0f1a"
    BG_PANEL = "#141826"
    TEXT_PRIMARY = "#e0e0ff"
    TEXT_SECONDARY = "#a0a0c0"
    ACCENT_PRIMARY = "#00eaff"
    ACCENT_SECONDARY = "#ff0078"
    ACCENT_WARN = "#ffb300"
    ACCENT_ERROR = "#ff3860"
    ACCENT_SUCCESS = "#00ff7f"
    SEMANTIC_DISABLED = "#8a91b8"
    SEMANTIC_MONK_ROBE = "#8B4513"
    SEMANTIC_MONK_ROBE_ACCENT = "#5D2906"
    SEMANTIC_MONK_HOOD = "#191970"
    SEMANTIC_MONK_SKIN = "#D2B48C"
    SEMANTIC_MONK_ACCESSORIES = "#FFD700"

class RadiusTokens(Enum):
    """Border radius design tokens"""
    CARD = 8
    BUTTON = 4
    SMALL = 4
    MEDIUM = 8
    LARGE = 12

class SpacingTokens(Enum):
    """Spacing design tokens"""
    BASE = 8
    COMPONENT = 16
    ELEMENT = 12
    SECTION = 24
    XS = 4
    SM = 8
    MD = 16
    LG = 24
    XL = 32

class DurationTokens(Enum):
    """Animation duration design tokens"""
    FAST = 100
    NORMAL = 200
    SLOW = 300
    TRANSITION = 250
    WINDOW_FADE = 300
    WINDOW_EXIT = 200
    BUTTON_HOVER = 150
    BUTTON_PRESS = 100
    TEXT_FOCUS = 200
    MONK_EMOTION = 300
    KARMA_CHANGE = 500

class FontTokens(Enum):
    """Font design tokens"""
    HEADLINE_FAMILY = "Orbitron"
    HEADLINE_SIZE_H1 = 28
    HEADLINE_SIZE_H2 = 22
    HEADLINE_SIZE_H3 = 18
    HEADLINE_SIZE_H4 = 16
    HEADLINE_WEIGHT_NORMAL = 400
    HEADLINE_WEIGHT_BOLD = 700
    BODY_FAMILY = "Inter"
    BODY_SIZE_BODY = 14
    BODY_SIZE_CAPTION = 12
    BODY_SIZE_SMALL = 12
    BODY_WEIGHT_NORMAL = 400
    BODY_WEIGHT_BOLD = 600
    MONO_FAMILY = "JetBrains Mono"
    MONO_SIZE_DEFAULT = 12
    MONO_WEIGHT_NORMAL = 400
