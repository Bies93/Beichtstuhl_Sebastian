#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Core Package for Beichtsthul Modern
"""

from .antwort_generator import AntwortGenerator
from .karma_rechner import KarmaRechner
from .datei_manager import DateiManager
from .statistik_manager import StatistikManager
from .constants import *

__all__ = [
    "AntwortGenerator",
    "KarmaRechner",
    "DateiManager",
    "StatistikManager",
    "APP_NAME",
    "APP_VERSION",
    "APP_AUTHOR",
    "DATA_FILE_NAME",
    "COLOR_PRIMARY_BG",
    "COLOR_SECONDARY_BG",
    "COLOR_SURFACE_BG",
    "COLOR_PRIMARY_ACCENT",
    "COLOR_SECONDARY_ACCENT",
    "COLOR_EMOTIONAL_ACCENT",
    "COLOR_SUCCESS",
    "COLOR_WARNING",
    "COLOR_ERROR",
    "COLOR_PRIMARY_TEXT",
    "COLOR_SECONDARY_TEXT",
    "COLOR_DISABLED_TEXT",
    "COLOR_MONK_ROBE",
    "COLOR_MONK_ROBE_ACCENT",
    "COLOR_MONK_HOOD",
    "COLOR_MONK_SKIN",
    "COLOR_MONK_ACCESSORIES",
    "FONT_PRIMARY",
    "FONT_SECONDARY",
    "FONT_MONOSPACE",
    "FONT_FALLBACK",
    "FONT_SIZE_TITLE",
    "FONT_SIZE_HEADER",
    "FONT_SIZE_BUTTON",
    "FONT_SIZE_BODY",
    "FONT_SIZE_CAPTION",
    "FONT_SIZE_SMALL",
    "SPACING_BASE",
    "SPACING_COMPONENT",
    "SPACING_ELEMENT",
    "SPACING_SECTION",
    "BORDER_RADIUS_CARD",
    "BORDER_RADIUS_BUTTON",
    "WINDOW_WIDTH",
    "WINDOW_HEIGHT",
    "WINDOW_MIN_WIDTH",
    "WINDOW_MIN_HEIGHT",
    "ANIMATION_WINDOW_FADE",
    "ANIMATION_WINDOW_EXIT",
    "ANIMATION_BUTTON_HOVER",
    "ANIMATION_BUTTON_PRESS",
    "ANIMATION_TEXT_FOCUS",
    "ANIMATION_MONK_EMOTION",
    "ANIMATION_KARMA_CHANGE",
    "EMOTION_MAPPING",
    "SUNDEN_CATEGORIES",
    "KARMA_DEBT_MAPPING",
    "PENALTY_WORDS"
]