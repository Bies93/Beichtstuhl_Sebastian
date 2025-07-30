#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Animated Button for Beichtsthul Modern
A custom button with cyberpunk neon animations and visual effects.
"""

from PyQt6.QtWidgets import QPushButton, QApplication
from PyQt6.QtCore import Qt, QTimer, pyqtProperty, QEasingCurve, QPropertyAnimation, QRect, QPoint
from PyQt6.QtGui import QPainter, QColor, QBrush, QPen, QFont, QFontMetrics, QRadialGradient


class AnimatedButton(QPushButton):
    """A custom button with animations and visual effects"""

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self._animation_speed = 150
        self._scale_factor = 1.0
        self._original_stylesheet = ""
        self._ripple_position = None
        self._ripple_radius = 0
        self._ripple_animation = None
        
        # Setup animations
        self.setup_animations()
        
        # Connect signals
        self.pressed.connect(self.on_pressed)
        self.released.connect(self.on_released)

    def setup_animations(self):
        """Setup button animations"""
        # Scale animation for press effect
        self.scale_animation = QPropertyAnimation(self, b"scale_factor")
        self.scale_animation.setDuration(self._animation_speed)
        self.scale_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        # Ripple animation
        self.ripple_animation = QPropertyAnimation(self, b"ripple_radius")
        self.ripple_animation.setDuration(300)
        self.ripple_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        self.ripple_animation.finished.connect(self.clear_ripple)

    def on_pressed(self):
        """Handle button press"""
        # Start scale animation
        self.scale_animation.setStartValue(1.0)
        self.scale_animation.setEndValue(0.95)
        self.scale_animation.start()
        
        # Start ripple effect
        self.start_ripple_effect()

    def on_released(self):
        """Handle button release"""
        # Start scale animation back to normal
        self.scale_animation.setStartValue(0.95)
        self.scale_animation.setEndValue(1.0)
        self.scale_animation.start()

    def start_ripple_effect(self):
        """Start the ripple effect animation"""
        # Get the position for the ripple (center of button)
        self._ripple_position = QPoint(self.width() // 2, self.height() // 2)
        
        # Start ripple animation
        self.ripple_animation.setStartValue(0)
        self.ripple_animation.setEndValue(max(self.width(), self.height()))
        self.ripple_animation.start()

    def clear_ripple(self):
        """Clear the ripple effect"""
        self._ripple_position = None
        self._ripple_radius = 0
        self.update()

    def paintEvent(self, event):
        """Custom paint event to draw ripple effect"""
        # Draw the normal button first
        super().paintEvent(event)
        
        # Draw ripple effect if active
        if self._ripple_position is not None and self._ripple_radius > 0:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.RenderHint.Antialiasing)
            
            # Create ripple color based on button color
            ripple_color = self.get_ripple_color()
            ripple_color.setAlpha(50)  # Make it semi-transparent
            
            # Draw ripple circle
            painter.setPen(Qt.PenStyle.NoPen)
            painter.setBrush(QBrush(ripple_color))
            painter.drawEllipse(
                self._ripple_position, 
                self._ripple_radius, 
                self._ripple_radius
            )

    def get_ripple_color(self):
        """Get the ripple color based on button style"""
        # Try to get color from stylesheet
        palette = self.palette()
        return palette.color(self.foregroundRole())

    def enterEvent(self, event):
        """Handle mouse enter event"""
        # Add hover effect
        if self.isEnabled():
            self.setCursor(Qt.CursorShape.PointingHandCursor)
        super().enterEvent(event)

    def leaveEvent(self, event):
        """Handle mouse leave event"""
        # Remove hover effect
        self.setCursor(Qt.CursorShape.ArrowCursor)
        super().leaveEvent(event)

    def resizeEvent(self, event):
        """Handle resize event"""
        super().resizeEvent(event)
        # Update ripple animation end value if needed
        if self.ripple_animation.state() != QPropertyAnimation.State.Running:
            self.ripple_animation.setEndValue(max(self.width(), self.height()))

    @pyqtProperty(float)
    def scale_factor(self):
        """Get the scale factor"""
        return self._scale_factor

    @scale_factor.setter
    def scale_factor(self, value):
        """Set the scale factor"""
        self._scale_factor = value
        # Apply scaling
        self.setGeometry(
            int(self.x() + (self.width() * (1 - value)) / 2),
            int(self.y() + (self.height() * (1 - value)) / 2),
            int(self.width() * value),
            int(self.height() * value)
        )

    @pyqtProperty(int)
    def ripple_radius(self):
        """Get the ripple radius"""
        return self._ripple_radius

    @ripple_radius.setter
    def ripple_radius(self, value):
        """Set the ripple radius"""
        self._ripple_radius = value
        self.update()

    def set_animation_speed(self, speed):
        """Set the animation speed"""
        self._animation_speed = speed
        self.scale_animation.setDuration(speed)
        self.ripple_animation.setDuration(speed * 2)
        
    def set_min_size_for_responsiveness(self, width=None, height=None):
        """Set minimum size for responsive design"""
        if width is not None:
            self.setMinimumWidth(width)
        if height is not None:
            self.setMinimumHeight(height)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    
    # Create test button
    button = AnimatedButton("Test Button")
    button.resize(200, 50)
    button.show()
    
    sys.exit(app.exec())