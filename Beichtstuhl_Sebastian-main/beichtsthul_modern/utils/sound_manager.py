#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Sound Manager for Beichtsthul Modern
Handles playback of sound effects and background audio with cyberpunk styling.
"""

import os
import random
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtCore import QUrl, QObject, pyqtSignal

from core.constants import APP_NAME
from utils.resource_loader import resource_loader


class SoundManager:
    """Manages sound effects and background audio for the application"""

    def __init__(self):
        self.sounds = {}
        self.background_audio = None
        self.volume = 1.0  # 0.0 to 1.0
        self.muted = False
        
        # Preload common sounds
        self.preload_sounds()

    def preload_sounds(self):
        """Preload commonly used sound effects"""
        # Button click sounds
        # self.load_sound("button_click", "button_click.wav")
        # self.load_sound("button_hover", "button_hover.wav")
        
        # Confession sounds
        # self.load_sound("confession_submit", "confession_submit.wav")
        # self.load_sound("confession_error", "confession_error.wav")
        
        # Karma change sounds
        # self.load_sound("karma_increase", "karma_increase.wav")
        # self.load_sound("karma_decrease", "karma_decrease.wav")
        
        # Monk emotion sounds
        # self.load_sound("monk_neutral", "monk_neutral.wav")
        # self.load_sound("monk_judge", "monk_judge.wav")
        # self.load_sound("monk_laugh", "monk_laugh.wav")
        # self.load_sound("monk_shock", "monk_shock.wav")
        
        print(f"{APP_NAME} sounds preloaded")

    def load_sound(self, sound_name, file_name):
        """
        Load a sound effect
        
        Args:
            sound_name: Name to reference the sound
            file_name: Name of the sound file
            
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            sound_path = resource_loader.get_sound_path(file_name)
            if not os.path.exists(sound_path):
                print(f"Sound file not found: {sound_path}")
                return False
                
            sound = QSoundEffect()
            sound.setSource(QUrl.fromLocalFile(sound_path))
            self.sounds[sound_name] = sound
            return True
        except Exception as e:
            print(f"Failed to load sound {sound_name}: {str(e)}")
            return False

    def play_sound(self, sound_name):
        """
        Play a sound effect
        
        Args:
            sound_name: Name of the sound to play
        """
        if self.muted:
            return
            
        if sound_name in self.sounds:
            sound = self.sounds[sound_name]
            sound.setVolume(self.volume)
            sound.play()
        else:
            print(f"Sound not found: {sound_name}")

    def set_volume(self, volume):
        """
        Set the global sound volume
        
        Args:
            volume: Volume level (0.0 to 1.0)
        """
        self.volume = max(0.0, min(1.0, volume))

    def get_volume(self):
        """
        Get the current volume level
        
        Returns:
            float: Current volume level (0.0 to 1.0)
        """
        return self.volume

    def toggle_mute(self):
        """Toggle mute state"""
        self.muted = not self.muted

    def is_muted(self):
        """
        Check if sound is muted
        
        Returns:
            bool: True if muted, False otherwise
        """
        return self.muted

    def play_background_audio(self, file_name):
        """
        Play background ambient audio
        
        Args:
            file_name: Name of the background audio file
        """
        # Implementation for background audio would go here
        # This would typically use QMediaPlayer for longer audio files
        pass

    def stop_background_audio(self):
        """Stop background ambient audio"""
        if self.background_audio:
            self.background_audio.stop()

    def set_background_volume(self, volume):
        """
        Set the background audio volume
        
        Args:
            volume: Volume level (0.0 to 1.0)
        """
        if self.background_audio:
            self.background_audio.setVolume(max(0.0, min(1.0, volume)))


# Global sound manager instance
sound_manager = SoundManager()