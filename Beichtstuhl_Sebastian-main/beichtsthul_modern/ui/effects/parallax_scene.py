#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parallax Scene for Beichtsthul Modern
A QGraphicsScene that manages parallax layers.
Features nebula background and scanline overlay effects.
"""

from PyQt6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem
from PyQt6.QtGui import QPixmap, QBrush, QColor, QRadialGradient
from PyQt6.QtCore import QPointF, QRectF

class ParallaxScene(QGraphicsScene):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.nebula_item = None
        self.scanlines_item = None
        self.load_layers()

    def load_layers(self):
        """Loads the parallax layers from image files and creates procedural effects."""
        # Create nebula background
        self.create_nebula_background()
        
        # Load scanlines overlay
        try:
            scanlines_pixmap = QPixmap("beichtsthul_modern/assets/images/vhs_scanlines.gif")
            if not scanlines_pixmap.isNull():
                self.scanlines_item = QGraphicsPixmapItem(scanlines_pixmap)
                self.addItem(self.scanlines_item)
                self.scanlines_item.setZValue(-1)
                self.scanlines_item.setOpacity(0.06)  # Subtle scanlines
        except Exception as e:
            print(f"Could not load scanlines: {e}")
            # Create procedural scanlines as fallback
            self.create_procedural_scanlines()
            
    def create_nebula_background(self):
        """Creates a procedural nebula background effect."""
        # Create a large rectangle for the nebula background
        nebula_rect = QGraphicsRectItem(QRectF(-2000, -2000, 4000, 4000))
        
        # Create a radial gradient for the nebula effect
        gradient = QRadialGradient(0, 0, 1000)
        gradient.setColorAt(0, QColor(20, 24, 38))  # Dark blue center
        gradient.setColorAt(0.3, QColor(30, 10, 60))  # Purple
        gradient.setColorAt(0.6, QColor(10, 20, 40))  # Dark blue
        gradient.setColorAt(1, QColor(14, 18, 34))  # Base dark color
        
        brush = QBrush(gradient)
        nebula_rect.setBrush(brush)
        nebula_rect.setZValue(-2)  # Behind everything
        
        self.nebula_item = nebula_rect
        self.addItem(nebula_rect)
        
    def create_procedural_scanlines(self):
        """Creates procedural scanlines as a fallback."""
        # This is a placeholder - in a real implementation you might want to
        # create a pattern of horizontal lines with some opacity
        pass

    def update_parallax(self, mouse_pos: QPointF, view_center: QPointF):
        """Updates the position of the layers based on mouse movement."""
        if self.nebula_item:
            # Nebula moves slowly for a deep space effect
            offset = (mouse_pos - view_center) * 0.02
            self.nebula_item.setPos(offset.x() * 0.5, offset.y() * 0.5)
            
        if self.scanlines_item:
            # Scanlines move faster for a VHS effect
            offset = (mouse_pos - view_center) * 0.04
            self.scanlines_item.setPos(offset.x() * 1.2, offset.y() * 1.2)