#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Monk Visualizer for Beichtsthul Modern
A custom widget for rendering the animated monk character using Lottie animations.
Features a 280x280px display with a glow ring effect.
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from utils.lottie_player import LottiePlayer
import os

class MonkVisualizer(QWidget):
    """A widget to display the monk's Lottie animations."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("monkVisualizer")
        self.setFixedSize(280, 280)

        self.lottie_player = LottiePlayer(self)
        self.lottie_player.set_size(280, 280)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.lottie_player)
        
        # Add glow effect
        self.setup_glow_effect()
        
        # Define the paths to the Lottie animation files
        self.animation_paths = {
            "idle": "beichtsthul_modern/assets/animations/monk_idle.json",
            "neutral": "beichtsthul_modern/assets/animations/monk_idle.json",
            "angry": "beichtsthul_modern/assets/animations/monk_angry.json",
            "laugh": "beichtsthul_modern/assets/animations/monk_laughing.json",
            "sad": "beichtsthul_modern/assets/animations/monk_sad.json",
            "shocked": "beichtsthul_modern/assets/animations/monk_shocked.json"
        }
        
        # Set the initial emotion
        self.set_emotion("idle")

    def setup_glow_effect(self):
        """Setup the glow ring effect around the monk visualizer."""
        # Create a gradient effect using cyan and magenta
        glow = QGraphicsDropShadowEffect(self)
        glow.setOffset(0, 0)
        glow.setBlurRadius(20)
        # Using a color that's a blend of cyan and magenta for the glow
        glow.setColor(QColor(128, 0, 128))  # Purple as a midpoint between cyan and magenta
        self.setGraphicsEffect(glow)
    
    def set_emotion(self, emotion: str):
        """
        Sets the monk's emotion by loading and playing the corresponding
        Lottie animation.

        Args:
            emotion (str): The name of the emotion (e.g., "idle", "angry").
        """
        animation_path = self.animation_paths.get(emotion.lower())
        
        if animation_path and os.path.exists(animation_path):
            self.lottie_player.load_animation(animation_path)
            self.lottie_player.play()
        else:
            # Fallback to idle if the requested emotion is not found
            print(f"Warning: Animation for '{emotion}' not found. Falling back to idle.")
            self.lottie_player.load_animation(self.animation_paths["idle"])
            self.lottie_player.play()

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QPushButton, QHBoxLayout

    app = QApplication(sys.argv)
    
    # Main test widget
    main_widget = QWidget()
    main_layout = QVBoxLayout(main_widget)

    # Monk visualizer
    monk_visualizer = MonkVisualizer()
    main_layout.addWidget(monk_visualizer)

    # Buttons to test emotions
    button_layout = QHBoxLayout()
    emotions = ["idle", "angry", "laugh", "sad", "shocked"]
    for e in emotions:
        btn = QPushButton(e.capitalize())
        btn.clicked.connect(lambda _, em=e: monk_visualizer.set_emotion(em))
        button_layout.addWidget(btn)
        
    main_layout.addLayout(button_layout)
    
    main_widget.resize(400, 400)
    main_widget.show()
    
    sys.exit(app.exec())