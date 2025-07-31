#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Response Display for Beichtsthul Modern
A custom display area for the monk's responses with cyberpunk styling and animations.
"""

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, QSize
from PyQt6.QtGui import QClipboard, QGuiApplication, QPainter, QColor, QPen, QFont

from core.constants import COLOR_PRIMARY_TEXT, COLOR_SECONDARY_BG, COLOR_PRIMARY_ACCENT
from design_tokens.design_tokens import ColorTokens, FontTokens
from utils.resource_loader import resource_loader
import random


class ResponseDisplay(QWidget):
    """A custom display area for the monk's responses"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("card")
        self._current_text = ""
        self._displayed_text = ""
        self._emotional_indicator = "neutral"
        
        # Create UI elements that are needed for animations
        self.emotional_indicator_label = QLabel()
        
        # Setup animations first
        self.setup_animations()
        
        # Then initialize UI
        self.init_ui()

    def init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # Configure emotional indicator label
        self.emotional_indicator_label.setObjectName("caption")
        # Bind to caption typography via QSS selector QLabel[type="caption"]
        self.emotional_indicator_label.setProperty("type", "caption")
        self.emotional_indicator_label.setFixedWidth(30)
        
        # Create header layout for emotional indicator
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.addWidget(self.emotional_indicator_label)
        header_layout.addStretch()
        
        # Create copy button
        self.copy_button = QPushButton("📋")
        self.copy_button.setFixedSize(24, 24)
        self.copy_button.setObjectName("copyButton")
        self.copy_button.clicked.connect(self.copy_to_clipboard)
        self.copy_button.setToolTip("In Zwischenablage kopieren")
        header_layout.addWidget(self.copy_button)
        
        layout.addLayout(header_layout)
        
        # Create response text label
        self.response_label = QLabel("Sprich, und ich werde urteilen...")
        self.response_label.setObjectName("responseText")
        self.response_label.setWordWrap(True)
        self.response_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.response_label.setTextInteractionFlags(
            Qt.TextInteractionFlag.TextSelectableByMouse | 
            Qt.TextInteractionFlag.TextSelectableByKeyboard
        )
        layout.addWidget(self.response_label)
        
        # Set initial emotional indicator
        self.update_emotional_indicator()

    def setup_animations(self):
        """Setup animations for the response display"""
        # Text reveal animation
        self.text_reveal_timer = QTimer()
        self.text_reveal_timer.timeout.connect(self.reveal_next_character)
        
        # Fade animation for emotional indicator
        self.emotion_fade_animation = QPropertyAnimation(self.emotional_indicator_label, b"windowOpacity")
        self.emotion_fade_animation.setDuration(200)
        self.emotion_fade_animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def set_text(self, text):
        """Set the response text with animation"""
        self._current_text = text
        self._displayed_text = ""
        self.response_label.setText("")
        
        # Start text reveal animation
        if text:
            self.text_reveal_timer.start(25)  # Reveal one character every 25ms
        else:
            self.response_label.setText("Sprich, und ich werde urteilen...")

    def reveal_next_character(self):
        """Reveal the next character in the text"""
        if len(self._displayed_text) < len(self._current_text):
            self._displayed_text += self._current_text[len(self._displayed_text)]
            self.response_label.setText(self._displayed_text)
        else:
            self.text_reveal_timer.stop()

    def update_emotional_indicator(self):
        """Update the emotional indicator based on current emotion"""
        indicators = {
            "neutral": "😐",
            "genervt": "😤",
            "schockiert": "😱",
            "lachend": "😂",
            "urteilend": "🤨",
            "contemplative": "🤔",
            "disappointed": "😞"
        }
        
        indicator = indicators.get(self._emotional_indicator, "😐")
        self.emotional_indicator_label.setText(indicator)
        
        # Start fade animation
        self.emotion_fade_animation.setStartValue(0.3)
        self.emotion_fade_animation.setEndValue(1.0)
        self.emotion_fade_animation.start()

    def set_emotion(self, emotion):
        """Set the current emotional state"""
        self._emotional_indicator = emotion
        self.update_emotional_indicator()

    def get_text(self):
        """Get the current response text"""
        return self._current_text

    def clear_text(self):
        """Clear the response text"""
        self.set_text("")

    def copy_to_clipboard(self):
        """Copy the current text to clipboard"""
        clipboard = QGuiApplication.clipboard()
        clipboard.setText(self._current_text)
        
        # Show visual feedback
        original_text = self.copy_button.text()
        self.copy_button.setText("✓")
        QTimer.singleShot(1000, lambda: self.copy_button.setText(original_text))

    def set_emotional_indicator_visible(self, visible):
        """Set whether the emotional indicator is visible"""
        self.emotional_indicator_label.setVisible(visible)
        
    def resizeEvent(self, event):
        """Handle resize events for responsive design"""
        super().resizeEvent(event)
        # Adjust font size based on widget width
        width = self.width()
        if width < 400:
            # Small widget - reduce font size
            font = self.response_label.font()
            font.setPointSize(10)
            self.response_label.setFont(font)
        elif width > 800:
            # Large widget - increase font size
            font = self.response_label.font()
            font.setPointSize(14)
            self.response_label.setFont(font)
        else:
            # Medium widget - default font size
            font = self.response_label.font()
            font.setPointSize(12)
            self.response_label.setFont(font)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
    
    app = QApplication(sys.argv)
    
    # Create test widget
    widget = QWidget()
    layout = QVBoxLayout(widget)
    
    # Create response display
    response_display = ResponseDisplay()
    layout.addWidget(response_display)
    
    # Create a button to set text
    button = QPushButton("Set Test Text")
    button.clicked.connect(lambda: response_display.set_text("This is a test response with some sardonic commentary."))
    layout.addWidget(button)
    
    widget.show()
    
    sys.exit(app.exec())