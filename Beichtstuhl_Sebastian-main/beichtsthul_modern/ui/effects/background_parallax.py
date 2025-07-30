#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Background Parallax Effect for Beichtsthul Modern
Implements a parallax background effect with VHS scanlines and particles.
"""

import sys
import random
from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt, QTimer, QRectF, QPointF, pyqtSignal
from PyQt6.QtGui import QPainter, QPixmap, QColor, QPen, QBrush


class ParallaxBackground(QWidget):
    """A widget that implements a parallax background effect"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_OpaquePaintEvent, False)
        
        # Parallax layers
        self.scanlines_layer = None
        self.particles_layer = []
        
        # Mouse position for parallax effect
        self.mouse_pos = QPointF(0, 0)
        
        # Animation timer
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_particles)
        self.timer.start(16)  # ~60fps
        
        # Initialize particles
        self.init_particles()
        
    def init_particles(self):
        """Initialize background particles"""
        self.particles_layer = []
        for _ in range(50):
            particle = {
                'pos': QPointF(random.randint(0, self.width()), random.randint(0, self.height())),
                'velocity': QPointF(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)),
                'size': random.randint(1, 3),
                'opacity': random.uniform(0.1, 0.3)
            }
            self.particles_layer.append(particle)
    
    def set_scanlines_image(self, pixmap):
        """
        Set the scanlines image for the background
        
        Args:
            pixmap: QPixmap with scanlines image
        """
        self.scanlines_layer = pixmap
        self.update()
    
    def mouseMoveEvent(self, event):
        """Handle mouse movement for parallax effect"""
        self.mouse_pos = event.position()
        self.update()
    
    def resizeEvent(self, event):
        """Handle widget resize"""
        super().resizeEvent(event)
        # Reinitialize particles on resize
        self.init_particles()
        self.update()
    
    def update_particles(self):
        """Update particle positions"""
        for particle in self.particles_layer:
            # Move particle
            particle['pos'] += particle['velocity']
            
            # Wrap around screen edges
            if particle['pos'].x() < 0:
                particle['pos'].setX(self.width())
            elif particle['pos'].x() > self.width():
                particle['pos'].setX(0)
                
            if particle['pos'].y() < 0:
                particle['pos'].setY(self.height())
            elif particle['pos'].y() > self.height():
                particle['pos'].setY(0)
        
        self.update()
    
    def paintEvent(self, event):
        """Paint the parallax background"""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Calculate parallax offset based on mouse position
        parallax_factor = 0.05
        offset_x = (self.mouse_pos.x() - self.width() / 2) * parallax_factor
        offset_y = (self.mouse_pos.y() - self.height() / 2) * parallax_factor
        
        # Draw particles layer with parallax
        self.draw_particles(painter, offset_x * 0.5, offset_y * 0.5)
        
        # Draw scanlines layer with parallax
        self.draw_scanlines(painter, offset_x, offset_y)
        
        painter.end()
    
    def draw_particles(self, painter, offset_x, offset_y):
        """Draw background particles"""
        painter.save()
        painter.translate(offset_x, offset_y)
        
        for particle in self.particles_layer:
            # Calculate particle position with offset
            x = (particle['pos'].x() + offset_x) % self.width()
            y = (particle['pos'].y() + offset_y) % self.height()
            
            # Set particle color with opacity
            color = QColor(0, 234, 255)  # Neon cyan
            color.setAlphaF(particle['opacity'])
            painter.setPen(QPen(color))
            painter.setBrush(QBrush(color))
            
            # Draw particle
            painter.drawEllipse(x, y, particle['size'], particle['size'])
        
        painter.restore()
    
    def draw_scanlines(self, painter, offset_x, offset_y):
        """Draw scanlines layer"""
        if self.scanlines_layer and not self.scanlines_layer.isNull():
            painter.save()
            painter.translate(offset_x, offset_y)
            
            # Draw scanlines with opacity
            painter.setOpacity(0.1)
            painter.drawPixmap(0, 0, self.scanlines_layer)
            
            painter.restore()
        else:
            # Draw simple scanlines if no image is available
            self.draw_simple_scanlines(painter, offset_x, offset_y)
    
    def draw_simple_scanlines(self, painter, offset_x, offset_y):
        """Draw simple scanlines as fallback"""
        painter.save()
        painter.translate(offset_x, offset_y)
        
        # Set scanline color
        color = QColor(0, 234, 255)  # Neon cyan
        color.setAlphaF(0.1)
        painter.setPen(QPen(color, 1))
        
        # Draw horizontal lines
        for y in range(0, self.height(), 4):
            painter.drawLine(0, y, self.width(), y)
        
        painter.restore()


# Example usage
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Create main window
    window = QWidget()
    window.setWindowTitle("Parallax Background Test")
    window.setGeometry(100, 100, 800, 600)
    window.setStyleSheet("background-color: #0d0f1a;")  # Cyberpunk background
    
    # Create layout
    layout = QVBoxLayout(window)
    
    # Create parallax background
    parallax_bg = ParallaxBackground()
    
    # Add a label on top to show that the background works
    label = QLabel("Move your mouse to see the parallax effect!")
    label.setStyleSheet("color: #00eaff; font-size: 24px; font-family: Orbitron;")
    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    # Add widgets to layout
    layout.addWidget(parallax_bg)
    layout.addWidget(label)
    
    window.show()
    sys.exit(app.exec())