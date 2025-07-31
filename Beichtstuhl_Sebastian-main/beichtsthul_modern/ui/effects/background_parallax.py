#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parallax Background Effect for Beichtsthul Modern
Implements a parallax background using QGraphicsView and QGraphicsScene.
"""

from PyQt6.QtWidgets import QGraphicsView, QApplication, QWidget, QVBoxLayout
from PyQt6.QtCore import Qt, QPointF, QTimer, QElapsedTimer
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QGraphicsView

from .parallax_scene import ParallaxScene

class ParallaxBackground(QGraphicsView):
    """
    A QGraphicsView that displays a ParallaxScene and updates it
    based on mouse movement to create a parallax effect.
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.scene = ParallaxScene(self)
        self.setScene(self.scene)

        # Configure the view
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.setRenderHint(QPainter.RenderHint.Antialiasing)
        self.setRenderHint(QPainter.RenderHint.SmoothPixmapTransform)
        self.setCacheMode(QGraphicsView.CacheModeFlag.CacheBackground)
        # Use smarter viewport updates to reduce repaint cost
        self.setViewportUpdateMode(QGraphicsView.ViewportUpdateMode.SmartViewportUpdate)
        self.setStyleSheet("background: transparent; border: 0px;")

        # Enable mouse tracking to get mouse events without clicking
        self.setMouseTracking(True)

        # Throttle parallax updates to avoid flooding the UI thread
        self._parallax_timer = QTimer(self)
        self._parallax_timer.setSingleShot(True)
        self._parallax_timer.timeout.connect(self._flush_parallax)
        self._parallax_pending = False
        self._last_mouse_pos = QPointF(self.viewport().width() / 2, self.viewport().height() / 2)

    def mouseMoveEvent(self, event):
        """Handle mouse movement to update the parallax effect (throttled)."""
        self._last_mouse_pos = event.pos()
        # Schedule an update at ~60 FPS; coalesce multiple events
        if not self._parallax_pending:
            self._parallax_pending = True
            # 16 ms ~ 60 Hz
            self._parallax_timer.start(16)
        super().mouseMoveEvent(event)

    def _flush_parallax(self):
        """Apply the latest parallax update."""
        self._parallax_pending = False
        view_center = QPointF(self.viewport().width() / 2, self.viewport().height() / 2)
        self.scene.update_parallax(self._last_mouse_pos, view_center)

    def resizeEvent(self, event):
        """Handle resize events to keep the scene centered."""
        self.fitInView(self.scene.sceneRect(), Qt.AspectRatioMode.KeepAspectRatioByExpanding)
        super().resizeEvent(event)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    
    main_window = QWidget()
    main_window.setGeometry(100, 100, 800, 600)
    main_window.setStyleSheet("background-color: #0E1222;")

    layout = QVBoxLayout(main_window)
    parallax_view = ParallaxBackground()
    layout.addWidget(parallax_view)
    
    main_window.show()
    sys.exit(app.exec())