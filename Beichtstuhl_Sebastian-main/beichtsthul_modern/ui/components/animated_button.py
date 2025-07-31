#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Neon Button for Beichtsthul Modern
A custom button with cyberpunk neon styling and a glow effect.
Features gradient background, hover effects, and press animations.
"""

from PyQt6.QtWidgets import QPushButton, QGraphicsDropShadowEffect
from PyQt6.QtGui import QColor
from PyQt6.QtCore import QEasingCurve, QPropertyAnimation, pyqtProperty

class AnimatedButton(QPushButton):
    """A custom button with neon styling, hover effects, and press animations."""

    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        
        # Set the object property to be targeted by the QSS file
        self.setProperty("class", "primary")
        
        # Setup animations
        self.setup_animations()
        
        # Setup the glow effect
        self.setup_glow_effect()
        
        # Set default size policy
        self.setFixedSize(120, 40)

    def setup_animations(self):
        """Setup hover and press animations"""
        # Elevation animation
        self._elevation = 0
        self.elevation_animation = QPropertyAnimation(self, b"elevation")
        self.elevation_animation.setDuration(200)
        self.elevation_animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        
        # Scale animation for press effect
        self.scale_animation = QPropertyAnimation(self, b"geometry")
        self.scale_animation.setDuration(100)
        self.scale_animation.setEasingCurve(QEasingCurve.Type.OutQuad)
        
    def setup_glow_effect(self):
        """
        Configures a QGraphicsDropShadowEffect to create a neon glow.
        The actual color and intensity will be driven by the stylesheet.
        """
        glow = QGraphicsDropShadowEffect(self)
        glow.setOffset(0, 0)
        # Set a default blur radius; can be fine-tuned in QSS if needed
        glow.setBlurRadius(15)
        # Set a default color; this will be overridden by the stylesheet
        glow.setColor(QColor("#00E5FF"))
        
        self.setGraphicsEffect(glow)
        
    def enterEvent(self, event):
        """Handle mouse enter event for hover effect"""
        super().enterEvent(event)
        self.start_hover_animation()
        
    def leaveEvent(self, event):
        """Handle mouse leave event for hover effect"""
        super().leaveEvent(event)
        self.end_hover_animation()
        
    def mousePressEvent(self, event):
        """Handle mouse press event for press effect"""
        super().mousePressEvent(event)
        self.start_press_animation()
        
    def mouseReleaseEvent(self, event):
        """Handle mouse release event for press effect"""
        super().mouseReleaseEvent(event)
        self.end_press_animation()
        
    def start_hover_animation(self):
        """Start the hover animation (elevate + shadow)"""
        self.elevation_animation.setStartValue(self._elevation)
        self.elevation_animation.setEndValue(2)
        self.elevation_animation.start()
        
    def end_hover_animation(self):
        """End the hover animation (return to normal)"""
        self.elevation_animation.setStartValue(self._elevation)
        self.elevation_animation.setEndValue(0)
        self.elevation_animation.start()
        
    def start_press_animation(self):
        """Start the press animation (scale down)"""
        # Store original geometry
        self._original_geometry = self.geometry()
        
        # Calculate scaled geometry
        scaled_width = int(self.width() * 0.96)
        scaled_height = int(self.height() * 0.96)
        scaled_x = self.x() + (self.width() - scaled_width) // 2
        scaled_y = self.y() + (self.height() - scaled_height) // 2
        
        scaled_geometry = self.geometry()
        scaled_geometry.setX(scaled_x)
        scaled_geometry.setY(scaled_y)
        scaled_geometry.setWidth(scaled_width)
        scaled_geometry.setHeight(scaled_height)
        
        self.scale_animation.setStartValue(self.geometry())
        self.scale_animation.setEndValue(scaled_geometry)
        self.scale_animation.start()
        
    def end_press_animation(self):
        """End the press animation (return to normal)"""
        if hasattr(self, '_original_geometry'):
            self.scale_animation.setStartValue(self.geometry())
            self.scale_animation.setEndValue(self._original_geometry)
            self.scale_animation.start()
            
    @pyqtProperty(float)
    def elevation(self):
        """Get the current elevation"""
        return self._elevation
        
    @elevation.setter
    def elevation(self, value):
        """Set the elevation and update the shadow effect"""
        self._elevation = value
        effect = self.graphicsEffect()
        if effect and isinstance(effect, QGraphicsDropShadowEffect):
            effect.setOffset(0, -value)

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
    
    # To test this button, we need a running application with the stylesheet loaded
    # The following is a minimal example
    
    # Assume app.qss has been generated by build_style.py
    # For testing, we can create a dummy app.qss
    
    app_qss = """
    QPushButton[class="primary"] {
        font-family: "Inter";
        font-weight: 500;
        text-transform: uppercase;
        padding: 10px 20px;
        border: 0;
        border-radius: 8px;
        background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #00E5FF, stop:1 #FF00A8);
        color: #0E1222;
        transition: all .2s;
    }
    
    QPushButton[class="primary"]:hover {
        transform: translateY(-2px);
    }
    """
    
    app = QApplication(sys.argv)
    app.setStyleSheet(app_qss)
    
    window = QMainWindow()
    window.setStyleSheet("background-color: #0E1222;")
    
    central_widget = QWidget()
    layout = QVBoxLayout(central_widget)
    
    # Create the NeonButton
    neon_button = AnimatedButton("Confess Your Sins")
    
    layout.addWidget(neon_button)
    window.setCentralWidget(central_widget)
    
    window.resize(400, 300)
    window.show()
    
    sys.exit(app.exec())