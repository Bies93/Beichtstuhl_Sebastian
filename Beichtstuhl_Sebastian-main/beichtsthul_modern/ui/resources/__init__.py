#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UI Resources for Beichtsthul Modern
"""

from .styles import get_all_styles
from .themes import theme_manager
from .animations import AnimationDefinitions, EasingCurves, AnimationTimings

__all__ = [
    "get_all_styles",
    "theme_manager",
    "AnimationDefinitions",
    "EasingCurves",
    "AnimationTimings"
]