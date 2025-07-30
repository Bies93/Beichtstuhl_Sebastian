#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Resource Loader for Beichtsthul Modern
Handles loading and caching of application resources such as images, sounds, and fonts.
"""

import os
from PyQt6.QtGui import QPixmap, QFontDatabase
from PyQt6.QtCore import QDir
from PyQt6.QtMultimedia import QSoundEffect
from core.constants import APP_NAME


class ResourceLoader:
    """Manages loading and caching of application resources"""

    def __init__(self):
        self.image_cache = {}
        self.sound_cache = {}
        self.font_cache = {}
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def get_image_path(self, image_name):
        """
        Gets the full path for an image resource
        
        Args:
            image_name: Name of the image file
            
        Returns:
            str: Full path to the image file
        """
        return os.path.join(self.base_path, "assets", "images", image_name)

    def get_sound_path(self, sound_name):
        """
        Gets the full path for a sound resource
        
        Args:
            sound_name: Name of the sound file
            
        Returns:
            str: Full path to the sound file
        """
        return os.path.join(self.base_path, "assets", "sounds", sound_name)

    def get_font_path(self, font_name):
        """
        Gets the full path for a font resource
        
        Args:
            font_name: Name of the font file
            
        Returns:
            str: Full path to the font file
        """
        return os.path.join(self.base_path, "assets", "fonts", font_name)

    def load_image(self, image_name):
        """
        Loads and caches an image
        
        Args:
            image_name: Name of the image file
            
        Returns:
            QPixmap: Loaded pixmap or None if failed
        """
        if image_name in self.image_cache:
            return self.image_cache[image_name]

        image_path = self.get_image_path(image_name)
        if not os.path.exists(image_path):
            print(f"Image not found: {image_path}")
            return None

        pixmap = QPixmap(image_path)
        if pixmap.isNull():
            print(f"Failed to load image: {image_path}")
            return None

        self.image_cache[image_name] = pixmap
        return pixmap

    def load_sound(self, sound_name):
        """
        Loads and caches a sound
        
        Args:
            sound_name: Name of the sound file
            
        Returns:
            QSoundEffect: Loaded sound effect or None if failed
        """
        if sound_name in self.sound_cache:
            return self.sound_cache[sound_name]

        sound_path = self.get_sound_path(sound_name)
        if not os.path.exists(sound_path):
            print(f"Sound not found: {sound_path}")
            return None

        sound = QSoundEffect()
        sound.setSource(sound_path)
        self.sound_cache[sound_name] = sound
        return sound

    def load_font(self, font_name):
        """
        Loads and caches a font
        
        Args:
            font_name: Name of the font file
            
        Returns:
            int: Font ID if successful, -1 if failed
        """
        if font_name in self.font_cache:
            return self.font_cache[font_name]

        font_path = self.get_font_path(font_name)
        if not os.path.exists(font_path):
            print(f"Font not found: {font_path}")
            return -1

        font_id = QFontDatabase.addApplicationFont(font_path)
        if font_id == -1:
            print(f"Failed to load font: {font_path}")
            return -1

        self.font_cache[font_name] = font_id
        return font_id

    def preload_resources(self):
        """
        Preloads commonly used resources
        This method can be called during application startup to load frequently used resources
        """
        # Preload common images
        # Example: self.load_image("monk_neutral.png")
        
        # Preload common sounds
        # Example: self.load_sound("button_click.wav")
        
        # Preload common fonts
        # Example: self.load_font("CascadiaCode.ttf")
        
        print(f"{APP_NAME} resources preloaded")

    def clear_cache(self):
        """Clears all cached resources"""
        self.image_cache.clear()
        self.sound_cache.clear()
        self.font_cache.clear()
        print(f"{APP_NAME} resource cache cleared")


# Global resource loader instance
resource_loader = ResourceLoader()