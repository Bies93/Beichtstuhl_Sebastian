#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Themes for Beichtsthul Modern
Manages application themes and color schemes with design token integration.
"""

from PyQt6.QtCore import QObject, pyqtSignal
from core.constants import *
from design_tokens.design_tokens import ColorTokens


class ThemeManager(QObject):
    """Manages application themes with hot-swap capability"""
    
    # Signal emitted when theme changes
    themeChanged = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.current_theme = "cyberpunk"
        self.themes = {
            "cyberpunk": self._get_cyberpunk_theme(),
            "cyberlight": self._get_cyberlight_theme()
        }

    def _get_cyberpunk_theme(self):
        """Returns the cyberpunk dark theme configuration using design tokens"""
        return {
            "name": "Cyberpunk",
            "primary_bg": ColorTokens.BG_BASE.value,
            "secondary_bg": ColorTokens.BG_PANEL.value,
            "surface_bg": ColorTokens.BG_PANEL.value,
            "primary_accent": ColorTokens.ACCENT_1.value,
            "secondary_accent": ColorTokens.ACCENT_2.value,
            "emotional_accent": ColorTokens.ACCENT_WARN.value,
            "success": ColorTokens.ACCENT_SUCCESS.value,
            "warning": ColorTokens.ACCENT_WARN.value,
            "error": ColorTokens.ACCENT_ERROR.value,
            "primary_text": ColorTokens.TEXT_PRIMARY.value,
            "secondary_text": ColorTokens.TEXT_SECONDARY.value,
            "disabled_text": ColorTokens.SEMANTIC_DISABLED.value,
            "monk_robe": ColorTokens.SEMANTIC_MONK_ROBE.value,
            "monk_robe_accent": ColorTokens.SEMANTIC_MONK_ROBE_ACCENT.value,
            "monk_hood": ColorTokens.SEMANTIC_MONK_HOOD.value,
            "monk_skin": ColorTokens.SEMANTIC_MONK_SKIN.value,
            "monk_accessories": ColorTokens.SEMANTIC_MONK_ACCESSORIES.value
        }

    def _get_cyberlight_theme(self):
        """Returns the cyberlight theme configuration (inverted colors)"""
        return {
            "name": "Cyberlight",
            "primary_bg": "#f0f0f0",
            "secondary_bg": "#ffffff",
            "surface_bg": "#e0e0e0",
            "primary_accent": ColorTokens.ACCENT_1.value,
            "secondary_accent": ColorTokens.ACCENT_2.value,
            "emotional_accent": ColorTokens.ACCENT_WARN.value,
            "success": ColorTokens.ACCENT_SUCCESS.value,
            "warning": ColorTokens.ACCENT_WARN.value,
            "error": ColorTokens.ACCENT_ERROR.value,
            "primary_text": "#000000",
            "secondary_text": "#333333",
            "disabled_text": "#888888",
            "monk_robe": ColorTokens.SEMANTIC_MONK_ROBE.value,
            "monk_robe_accent": ColorTokens.SEMANTIC_MONK_ROBE_ACCENT.value,
            "monk_hood": ColorTokens.SEMANTIC_MONK_HOOD.value,
            "monk_skin": ColorTokens.SEMANTIC_MONK_SKIN.value,
            "monk_accessories": ColorTokens.SEMANTIC_MONK_ACCESSORIES.value
        }

    def get_theme(self, theme_name=None):
        """
        Returns the specified theme or the current theme if none specified
        
        Args:
            theme_name: Name of the theme to retrieve
            
        Returns:
            dict: Theme configuration
        """
        if theme_name is None:
            theme_name = self.current_theme
        return self.themes.get(theme_name, self.themes["cyberpunk"])

    def set_theme(self, theme_name):
        """
        Sets the current theme with hot-swap capability
        
        Args:
            theme_name: Name of the theme to set
            
        Returns:
            bool: True if successful, False otherwise
        """
        if theme_name in self.themes:
            self.current_theme = theme_name
            self.themeChanged.emit(theme_name)
            return True
        return False

    def get_color(self, color_name, theme_name=None):
        """
        Returns a specific color from the theme
        
        Args:
            color_name: Name of the color to retrieve
            theme_name: Name of the theme to use (defaults to current)
            
        Returns:
            str: Color value in hex format
        """
        theme = self.get_theme(theme_name)
        return theme.get(color_name, ColorTokens.BG_BASE.value)

    def get_all_themes(self):
        """
        Returns all available themes
        
        Returns:
            list: List of theme names
        """
        return list(self.themes.keys())

    def is_dark_theme(self, theme_name=None):
        """
        Checks if the specified theme (or current) is a dark theme
        
        Args:
            theme_name: Name of the theme to check
            
        Returns:
            bool: True if dark theme, False otherwise
        """
        if theme_name is None:
            theme_name = self.current_theme
        return theme_name == "cyberpunk"

    def load_tokens(self):
        """
        Load theme configuration from design tokens
        This method can be called to refresh themes when tokens change
        """
        self.themes = {
            "cyberpunk": self._get_cyberpunk_theme(),
            "cyberlight": self._get_cyberlight_theme()
        }
        # Emit theme changed signal to notify UI components
        self.themeChanged.emit(self.current_theme)


# Global theme manager instance
theme_manager = ThemeManager()