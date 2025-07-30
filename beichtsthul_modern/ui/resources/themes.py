#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Themes for Beichtsthul Modern
Manages application themes and color schemes.
"""

from core.constants import *


class ThemeManager:
    """Manages application themes"""

    def __init__(self):
        self.current_theme = "dark"
        self.themes = {
            "dark": self._get_dark_theme(),
            "light": self._get_light_theme()
        }

    def _get_dark_theme(self):
        """Returns the dark theme configuration"""
        return {
            "name": "Dark",
            "primary_bg": COLOR_PRIMARY_BG,
            "secondary_bg": COLOR_SECONDARY_BG,
            "surface_bg": COLOR_SURFACE_BG,
            "primary_accent": COLOR_PRIMARY_ACCENT,
            "secondary_accent": COLOR_SECONDARY_ACCENT,
            "emotional_accent": COLOR_EMOTIONAL_ACCENT,
            "success": COLOR_SUCCESS,
            "warning": COLOR_WARNING,
            "error": COLOR_ERROR,
            "primary_text": COLOR_PRIMARY_TEXT,
            "secondary_text": COLOR_SECONDARY_TEXT,
            "disabled_text": COLOR_DISABLED_TEXT,
            "monk_robe": COLOR_MONK_ROBE,
            "monk_robe_accent": COLOR_MONK_ROBE_ACCENT,
            "monk_hood": COLOR_MONK_HOOD,
            "monk_skin": COLOR_MONK_SKIN,
            "monk_accessories": COLOR_MONK_ACCESSORIES
        }

    def _get_light_theme(self):
        """Returns the light theme configuration"""
        return {
            "name": "Light",
            "primary_bg": "#f0f0f0",
            "secondary_bg": "#ffffff",
            "surface_bg": "#e0e0e0",
            "primary_accent": "#1a73e8",
            "secondary_accent": "#00bcd4",
            "emotional_accent": "#ff6d00",
            "success": "#4caf50",
            "warning": "#ff9800",
            "error": "#f44336",
            "primary_text": "#212121",
            "secondary_text": "#757575",
            "disabled_text": "#bdbdbd",
            "monk_robe": "#8B4513",
            "monk_robe_accent": "#5D2906",
            "monk_hood": "#191970",
            "monk_skin": "#D2B48C",
            "monk_accessories": "#FFD700"
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
        return self.themes.get(theme_name, self.themes["dark"])

    def set_theme(self, theme_name):
        """
        Sets the current theme
        
        Args:
            theme_name: Name of the theme to set
            
        Returns:
            bool: True if successful, False otherwise
        """
        if theme_name in self.themes:
            self.current_theme = theme_name
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
        return theme.get(color_name, COLOR_PRIMARY_BG)

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
        return theme_name == "dark"


# Global theme manager instance
theme_manager = ThemeManager()