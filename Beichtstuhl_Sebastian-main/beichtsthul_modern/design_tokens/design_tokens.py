#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Design Tokens for Beichtsthul Modern
Auto-generated from design_tokens.json
"""

from enum import Enum


class ColorTokens(Enum):
    """Color design tokens"""
    BG_BASE = "#0E1222"
    BG_PANEL = "#141826"
    TEXT_PRIMARY = "#EDEFFF"
    TEXT_SECONDARY = "#B8BCE6"
    ACCENT_1 = "#00E5FF"
    ACCENT_2 = "#FF00A8"
    ACCENT_WARN = "#FFC400"
    ACCENT_SUCCESS = "#00FF88"
    ACCENT_ERROR = "#FF3860"
    SEMANTIC_MONK_ROBE = "#8B4513"
    SEMANTIC_MONK_ROBE_ACCENT = "#5D2906"
    SEMANTIC_MONK_HOOD = "#191970"
    SEMANTIC_MONK_SKIN = "#D2B48C"
    SEMANTIC_MONK_ACCESSORIES = "#FFD700"
    SEMANTIC_DISABLED = "#8a91b8"

class RadiusTokens(Enum):
    """Border radius design tokens"""
    SM = 8
    MD = 12

class SpacingTokens(Enum):
    """Spacing design tokens"""
    SPACING_1 = 4
    SPACING_2 = 8
    SPACING_3 = 16

class DurationTokens(Enum):
    """Animation duration design tokens"""
    FAST = 100
    NORMAL = 200
    SLOW = 300
    TRANSITION = 250

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
