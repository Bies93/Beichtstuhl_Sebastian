#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Animations for Beichtsthul Modern
Defines animation behaviors and timing for UI components.
"""

from PyQt6.QtCore import QEasingCurve
from core.constants import *


class AnimationDefinitions:
    """Defines animation behaviors for different UI components"""

    @staticmethod
    def window_fade_in():
        """Returns parameters for window fade-in animation"""
        return {
            "duration": ANIMATION_WINDOW_FADE,
            "easing_curve": QEasingCurve.Type.OutCubic,
            "start_value": 0.0,
            "end_value": 1.0
        }

    @staticmethod
    def window_fade_out():
        """Returns parameters for window fade-out animation"""
        return {
            "duration": ANIMATION_WINDOW_EXIT,
            "easing_curve": QEasingCurve.Type.InCubic,
            "start_value": 1.0,
            "end_value": 0.0
        }

    @staticmethod
    def button_hover():
        """Returns parameters for button hover animation"""
        return {
            "duration": ANIMATION_BUTTON_HOVER,
            "easing_curve": QEasingCurve.Type.OutCubic
        }

    @staticmethod
    def button_press():
        """Returns parameters for button press animation"""
        return {
            "duration": ANIMATION_BUTTON_PRESS,
            "easing_curve": QEasingCurve.Type.OutCubic,
            "scale_factor": 0.95
        }

    @staticmethod
    def text_focus():
        """Returns parameters for text input focus animation"""
        return {
            "duration": ANIMATION_TEXT_FOCUS,
            "easing_curve": QEasingCurve.Type.OutCubic
        }

    @staticmethod
    def monk_emotion_change():
        """Returns parameters for monk emotion change animation"""
        return {
            "duration": ANIMATION_MONK_EMOTION,
            "easing_curve": QEasingCurve.Type.OutCubic
        }

    @staticmethod
    def karma_change():
        """Returns parameters for karma change animation"""
        return {
            "duration": ANIMATION_KARMA_CHANGE,
            "easing_curve": QEasingCurve.Type.OutCubic
        }

    @staticmethod
    def get_ripple_effect_params():
        """Returns parameters for button ripple effect"""
        return {
            "duration": 300,
            "easing_curve": QEasingCurve.Type.OutCubic,
            "max_radius": 100
        }

    @staticmethod
    def get_text_reveal_params():
        """Returns parameters for text reveal animation"""
        return {
            "duration": 500,
            "easing_curve": QEasingCurve.Type.OutCubic,
            "letter_delay": 50
        }

    @staticmethod
    def get_progress_bar_params():
        """Returns parameters for progress bar animation"""
        return {
            "duration": 300,
            "easing_curve": QEasingCurve.Type.OutCubic
        }


class EasingCurves:
    """Collection of commonly used easing curves"""

    # Standard easing curves
    STANDARD_IN = QEasingCurve.Type.InCubic
    STANDARD_OUT = QEasingCurve.Type.OutCubic
    STANDARD_IN_OUT = QEasingCurve.Type.InOutCubic

    # Bounce easing curves
    BOUNCE_IN = QEasingCurve.Type.InBounce
    BOUNCE_OUT = QEasingCurve.Type.OutBounce
    BOUNCE_IN_OUT = QEasingCurve.Type.InOutBounce

    # Elastic easing curves
    ELASTIC_IN = QEasingCurve.Type.InElastic
    ELASTIC_OUT = QEasingCurve.Type.OutElastic
    ELASTIC_IN_OUT = QEasingCurve.Type.InOutElastic

    # Back easing curves
    BACK_IN = QEasingCurve.Type.InBack
    BACK_OUT = QEasingCurve.Type.OutBack
    BACK_IN_OUT = QEasingCurve.Type.InOutBack


class AnimationTimings:
    """Collection of standard animation timings"""

    # Fast animations (100-200ms)
    FAST = 100
    MEDIUM_FAST = 150
    STANDARD = 200

    # Medium animations (300-500ms)
    MEDIUM = 300
    MEDIUM_SLOW = 400
    SLOW = 500

    # Slow animations (600ms+)
    VERY_SLOW = 600
    TRANSITION = 800
    MODAL = 1000


# Predefined animation sequences
ANIMATION_SEQUENCES = {
    "button_click": [
        AnimationDefinitions.button_press(),
        AnimationDefinitions.button_hover()
    ],
    "window_open": [
        AnimationDefinitions.window_fade_in()
    ],
    "window_close": [
        AnimationDefinitions.window_fade_out()
    ],
    "text_reveal": [
        AnimationDefinitions.get_text_reveal_params()
    ]
}