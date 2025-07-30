#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Monk Visualizer for Beichtsthul Modern
A custom widget for rendering the animated monk character with different emotions.
"""

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt, QTimer, QRect, QPoint
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush

from core.constants import (
    COLOR_MONK_ROBE, COLOR_MONK_ROBE_ACCENT, COLOR_MONK_HOOD, 
    COLOR_MONK_SKIN, COLOR_MONK_ACCESSORIES
)


class MonkVisualizer(QWidget):
    """A custom widget for rendering the animated monk character"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("monkVisualizer")
        self._current_emotion = "neutral"
        self._target_emotion = "neutral"
        self._animation_progress = 0.0
        self._breathing_offset = 0.0
        self._blink_state = 0  # 0 = open, 1 = closing, 2 = closed, 3 = opening
        self._blink_timer = QTimer()
        self._breathing_timer = QTimer()
        
        # Set minimum size
        self.setMinimumSize(400, 250)
        
        # Setup animations
        self.setup_animations()

    def setup_animations(self):
        """Setup animations for the monk character"""
        # Blink timer
        self._blink_timer.timeout.connect(self.update_blink_state)
        self._blink_timer.setInterval(5000)  # Blink every 5 seconds on average
        self._blink_timer.start()
        
        # Breathing timer
        self._breathing_timer.timeout.connect(self.update_breathing)
        self._breathing_timer.setInterval(100)  # Update breathing every 100ms
        self._breathing_timer.start()

    def update_blink_state(self):
        """Update the blink state for eye animations"""
        # Randomize blink timing
        if self._blink_state == 0 and self._blink_timer.interval() > 3000:
            self._blink_state = 1  # Start closing
            self._blink_timer.setInterval(50)  # Fast close
        elif self._blink_state == 1:
            self._blink_state = 2  # Closed
            self._blink_timer.setInterval(100)  # Stay closed briefly
        elif self._blink_state == 2:
            self._blink_state = 3  # Start opening
            self._blink_timer.setInterval(50)  # Fast open
        elif self._blink_state == 3:
            self._blink_state = 0  # Open
            # Set next blink time (random between 2-8 seconds)
            import random
            self._blink_timer.setInterval(random.randint(2000, 8000))
        
        self.update()

    def update_breathing(self):
        """Update the breathing animation"""
        # Simple sine wave for breathing
        import math
        self._breathing_offset += 0.1
        if self._breathing_offset > 2 * math.pi:
            self._breathing_offset = 0
        self.update()

    def set_emotion(self, emotion):
        """Set the monk's emotion with animation"""
        if emotion != self._current_emotion:
            self._target_emotion = emotion
            self._animation_progress = 0.0
            self.update()

    def get_emotion(self):
        """Get the current emotion"""
        return self._current_emotion

    def paintEvent(self, event):
        """Paint the monk character"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Draw background
        self.draw_background(painter)
        
        # Draw monk character
        self.draw_monk(painter)

    def draw_background(self, painter):
        """Draw the background (church window effect)"""
        # Draw stained glass window effect
        rect = self.rect()
        painter.fillRect(rect, QColor("#330000"))
        
        # Draw decorative border
        pen = QPen(QColor("#666666"), 2)
        painter.setPen(pen)
        painter.drawRect(rect.adjusted(1, 1, -1, -1))

    def draw_monk(self, painter):
        """Draw the monk character"""
        # Calculate center position
        center_x = self.width() // 2
        center_y = self.height() // 2
        
        # Apply breathing effect
        import math
        breathing_scale = 1.0 + 0.02 * math.sin(self._breathing_offset)
        
        # Draw monk body parts
        self.draw_robe(painter, center_x, center_y, breathing_scale)
        self.draw_head(painter, center_x, center_y)
        self.draw_face(painter, center_x, center_y)
        self.draw_hood(painter, center_x, center_y)
        self.draw_arms(painter, center_x, center_y)
        
        # Draw emotion-specific features
        self.draw_emotion(painter, center_x, center_y)

    def draw_robe(self, painter, center_x, center_y, scale=1.0):
        """Draw the monk's robe"""
        # Robe body
        robe_color = QColor(COLOR_MONK_ROBE)
        robe_accent_color = QColor(COLOR_MONK_ROBE_ACCENT)
        
        # Main robe body with breathing effect
        body_rect = QRect(
            int(center_x - 20 * scale), 
            int(center_y - 30 * scale), 
            int(40 * scale), 
            int(80 * scale)
        )
        painter.setBrush(QBrush(robe_color))
        painter.setPen(QPen(robe_accent_color, 1))
        painter.drawEllipse(body_rect)
        
        # Robe folds
        painter.setPen(QPen(robe_accent_color, 2))
        painter.drawLine(
            int(center_x - 15 * scale), 
            int(center_y - 20 * scale), 
            int(center_x + 15 * scale), 
            int(center_y - 20 * scale)
        )
        painter.drawLine(
            int(center_x - 10 * scale), 
            int(center_y), 
            int(center_x + 10 * scale), 
            int(center_y)
        )

    def draw_head(self, painter, center_x, center_y):
        """Draw the monk's head"""
        skin_color = QColor(COLOR_MONK_SKIN)
        
        # Head
        head_rect = QRect(center_x - 25, center_y - 80, 50, 50)
        painter.setBrush(QBrush(skin_color))
        painter.setPen(QPen(skin_color.darker(150), 1))
        painter.drawEllipse(head_rect)

    def draw_face(self, painter, center_x, center_y):
        """Draw the monk's face"""
        # Eyes (with blink animation)
        eye_height = 5
        if self._blink_state == 1:  # Closing
            eye_height = 3
        elif self._blink_state == 2:  # Closed
            eye_height = 1
        elif self._blink_state == 3:  # Opening
            eye_height = 3
        
        painter.setBrush(QBrush(QColor("#000000")))
        painter.setPen(QPen(QColor("#000000"), 1))
        
        # Left eye
        painter.drawEllipse(QRect(center_x - 15, center_y - 65, 8, eye_height))
        
        # Right eye
        painter.drawEllipse(QRect(center_x + 7, center_y - 65, 8, eye_height))
        
        # Nose
        painter.setPen(QPen(QColor("#000000"), 2))
        painter.drawLine(center_x - 2, center_y - 55, center_x, center_y - 50)
        
        # Mouth (changes with emotion)
        self.draw_mouth(painter, center_x, center_y)

    def draw_mouth(self, painter, center_x, center_y):
        """Draw the monk's mouth based on emotion"""
        painter.setPen(QPen(QColor("#000000"), 2))
        
        if self._current_emotion == "neutral":
            # Neutral: simple line
            painter.drawLine(center_x - 10, center_y - 40, center_x + 10, center_y - 40)
        elif self._current_emotion == "genervt":
            # Annoyed: downturned line
            painter.drawLine(center_x - 10, center_y - 35, center_x + 10, center_y - 45)
        elif self._current_emotion == "schockiert":
            # Shocked: open circle
            painter.setBrush(QBrush(QColor("#000000")))
            painter.drawEllipse(QRect(center_x - 5, center_y - 45, 10, 10))
        elif self._current_emotion == "lachend":
            # Laughing: smiling arc
            painter.drawArc(center_x - 10, center_y - 50, 20, 15, 0, 180 * 16)
        elif self._current_emotion == "urteilend":
            # Judging: slight smirk
            painter.drawLine(center_x - 8, center_y - 42, center_x + 8, center_y - 38)
        else:
            # Default: neutral line
            painter.drawLine(center_x - 10, center_y - 40, center_x + 10, center_y - 40)

    def draw_hood(self, painter, center_x, center_y):
        """Draw the monk's hood"""
        hood_color = QColor(COLOR_MONK_HOOD)
        
        # Hood (semicircle)
        painter.setBrush(QBrush(hood_color))
        painter.setPen(QPen(hood_color.darker(150), 1))
        hood_rect = QRect(center_x - 30, center_y - 90, 60, 30)
        painter.drawChord(hood_rect, 0, 180 * 16)

    def draw_arms(self, painter, center_x, center_y):
        """Draw the monk's arms"""
        robe_color = QColor(COLOR_MONK_ROBE)
        robe_accent_color = QColor(COLOR_MONK_ROBE_ACCENT)
        
        painter.setPen(QPen(robe_accent_color, 6))
        
        # Left arm
        painter.drawLine(center_x - 20, center_y - 20, center_x - 40, center_y - 10)
        
        # Right arm
        painter.drawLine(center_x + 20, center_y - 20, center_x + 40, center_y - 10)

    def draw_emotion(self, painter, center_x, center_y):
        """Draw emotion-specific features"""
        # This method can be extended to add more detailed emotion-specific features
        pass

    def resizeEvent(self, event):
        """Handle resize event for responsive design"""
        super().resizeEvent(event)
        # Update the widget when resized
        self.update()


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
    
    app = QApplication(sys.argv)
    
    # Create test widget
    widget = QWidget()
    layout = QVBoxLayout(widget)
    
    # Create monk visualizer
    monk_visualizer = MonkVisualizer()
    layout.addWidget(monk_visualizer)
    
    # Create buttons to change emotions
    emotions = ["neutral", "genervt", "schockiert", "lachend", "urteilend"]
    for emotion in emotions:
        button = QPushButton(f"Set {emotion}")
        button.clicked.connect(lambda e=emotion: monk_visualizer.set_emotion(e))
        layout.addWidget(button)
    
    widget.show()
    
    sys.exit(app.exec())