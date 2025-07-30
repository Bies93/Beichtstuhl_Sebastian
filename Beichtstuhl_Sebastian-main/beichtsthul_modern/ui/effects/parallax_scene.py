#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parallax Scene for Beichtsthul Modern
Implements a QGraphicsView with two layers for parallax effect.
"""

import random
from PyQt6.QtWidgets import QGraphicsView, QGraphicsScene, QGraphicsItem, QApplication
from PyQt6.QtCore import Qt, QTimer, QPointF, QRectF, pyqtSignal
from PyQt6.QtGui import QPixmap, QPainter, QColor, QPen, QBrush, QPainterPath

from design_tokens.design_tokens import ColorTokens
from utils.resource_loader import resource_loader


class ParallaxScene(QGraphicsScene):
    """A QGraphicsScene with parallax effect layers"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setSceneRect(0, 0, 800, 600)  # Default size
        
        # Create parallax layers
        self.scanlines_layer = ParallaxLayer("scanlines", 0.2)
        self.particles_layer = ParallaxLayer("particles", 0.5)
        
        # Add layers to scene
        self.addItem(self.scanlines_layer)
        self.addItem(self.particles_layer)
        
        # Mouse position for parallax effect
        self.mouse_pos = QPointF(0, 0)
        self.target_mouse_pos = QPointF(0, 0)
        
        # Animation timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(16)  # ~60fps
        
        # Smoothing factor for parallax movement
        self.smoothing_factor = 0.1
        
        # Initialize layers
        self.init_scanlines_layer()
        self.init_particles_layer()
        
    def init_scanlines_layer(self):
        """Initialize the scanlines layer"""
        # Load VHS scanlines image if available
        scanlines_pixmap = resource_loader.load_image("vhs_scanlines.gif")
        if scanlines_pixmap and not scanlines_pixmap.isNull():
            self.scanlines_layer.set_pixmap(scanlines_pixmap)
        else:
            # Create simple scanlines if image is not available
            self.scanlines_layer.create_simple_scanlines()
            
    def init_particles_layer(self):
        """Initialize the particles layer"""
        self.particles_layer.create_particles(50)
        
    def set_mouse_position(self, pos):
        """Set mouse position for parallax effect"""
        self.mouse_pos = pos
        self.update_parallax()
        
    def update_parallax(self):
        """Update parallax effect based on mouse position"""
        # Calculate parallax offset
        parallax_factor = 0.05
        center_x = self.width() / 2
        center_y = self.height() / 2
        offset_x = (self.mouse_pos.x() - center_x) * parallax_factor
        offset_y = (self.mouse_pos.y() - center_y) * parallax_factor
        
        # Update layer positions
        self.scanlines_layer.set_parallax_offset(offset_x, offset_y)
        self.particles_layer.set_parallax_offset(offset_x * 0.5, offset_y * 0.5)
        
    def update_animation(self):
        """Update animation for all layers"""
        self.particles_layer.update_particles()
        
    def set_size(self, width, height):
        """Set the scene size"""
        self.setSceneRect(0, 0, width, height)
        self.scanlines_layer.set_size(width, height)
        self.particles_layer.set_size(width, height)


class ParallaxLayer(QGraphicsItem):
    """A parallax layer that can be added to a QGraphicsScene"""
    
    def __init__(self, layer_type, parallax_factor=1.0, parent=None):
        super().__init__(parent)
        self.layer_type = layer_type
        self.parallax_factor = parallax_factor
        self.offset_x = 0.0
        self.offset_y = 0.0
        self.width = 800
        self.height = 600
        
        # Layer-specific data
        self.pixmap = None
        self.particles = []
        
        # Set flags for better performance
        self.setFlag(QGraphicsItem.GraphicsItemFlag.ItemUsesExtendedStyleOption, True)
        
    def set_parallax_offset(self, offset_x, offset_y):
        """Set parallax offset for this layer"""
        self.offset_x = offset_x * self.parallax_factor
        self.offset_y = offset_y * self.parallax_factor
        self.update()
        
    def set_pixmap(self, pixmap):
        """Set pixmap for this layer"""
        self.pixmap = pixmap
        self.update()
        
    def set_size(self, width, height):
        """Set layer size"""
        self.width = width
        self.height = height
        self.update()
        
    def create_simple_scanlines(self):
        """Create simple scanlines as fallback"""
        # This will be drawn in the paint method
        pass
        
    def create_particles(self, count):
        """Create particles for this layer"""
        self.particles = []
        for _ in range(count):
            particle = {
                'pos': QPointF(random.randint(0, self.width), random.randint(0, self.height)),
                'velocity': QPointF(random.uniform(-0.5, 0.5), random.uniform(-0.5, 0.5)),
                'size': random.randint(1, 3),
                'opacity': random.uniform(0.1, 0.3)
            }
            self.particles.append(particle)
            
    def update_particles(self):
        """Update particle positions"""
        if self.layer_type == "particles":
            for particle in self.particles:
                # Move particle
                particle['pos'] += particle['velocity']
                
                # Wrap around screen edges
                if particle['pos'].x() < 0:
                    particle['pos'].setX(self.width)
                elif particle['pos'].x() > self.width:
                    particle['pos'].setX(0)
                    
                if particle['pos'].y() < 0:
                    particle['pos'].setY(self.height)
                elif particle['pos'].y() > self.height:
                    particle['pos'].setY(0)
                    
            self.update()
            
    def boundingRect(self):
        """Return the bounding rectangle for this item"""
        return QRectF(0, 0, self.width, self.height)
        
    def paint(self, painter, option, widget):
        """Paint the layer content"""
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Apply parallax offset
        painter.save()
        painter.translate(self.offset_x, self.offset_y)
        
        if self.layer_type == "scanlines":
            self.paint_scanlines(painter)
        elif self.layer_type == "particles":
            self.paint_particles(painter)
            
        painter.restore()
        
    def paint_scanlines(self, painter):
        """Paint the scanlines layer"""
        if self.pixmap and not self.pixmap.isNull():
            # Draw scanlines pixmap with opacity
            painter.setOpacity(0.1)
            painter.drawPixmap(0, 0, self.pixmap)
        else:
            # Draw simple scanlines as fallback
            self.paint_simple_scanlines(painter)
            
    def paint_simple_scanlines(self, painter):
        """Paint simple scanlines as fallback"""
        # Set scanline color
        color = QColor(ColorTokens.ACCENT_PRIMARY.value)  # Neon cyan
        color.setAlphaF(0.1)
        painter.setPen(QPen(color, 1))
        
        # Draw horizontal lines
        for y in range(0, int(self.height), 4):
            painter.drawLine(0, y, int(self.width), y)
            
    def paint_particles(self, painter):
        """Paint the particles layer"""
        for particle in self.particles:
            # Set particle color with opacity
            color = QColor(ColorTokens.ACCENT_PRIMARY.value)  # Neon cyan
            color.setAlphaF(particle['opacity'])
            painter.setPen(QPen(color))
            painter.setBrush(QBrush(color))
            
            # Draw particle
            painter.drawEllipse(
                particle['pos'].x(), 
                particle['pos'].y(), 
                particle['size'], 
                particle['size']
            )


class ParallaxView(QGraphicsView):
    """A QGraphicsView that handles parallax effects"""
    
    def __init__(self, scene, parent=None):
        super().__init__(scene, parent)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        self.setOptimizationFlags(
            QGraphicsView.OptimizationFlag.DontSavePainterState |
            QGraphicsView.OptimizationFlag.DontAdjustForAntialiasing
        )
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.SmartViewportUpdate)
        self.setCacheMode(QGraphicsView.CacheModeFlag.CacheBackground)
        
        # Enable mouse tracking
        self.setMouseTracking(True)
        
    def mouseMoveEvent(self, event):
        """Handle mouse movement for parallax effect"""
        super().mouseMoveEvent(event)
        if self.scene():
            # Convert viewport coordinates to scene coordinates
            scene_pos = self.mapToScene(event.pos())
            self.scene().set_mouse_position(scene_pos)
            
    def resizeEvent(self, event):
        """Handle resize event"""
        super().resizeEvent(event)
        if self.scene():
            # Update scene size
            size = event.size()
            self.scene().set_size(size.width(), size.height())