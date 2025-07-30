#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Karma Display for Beichtsthul Modern
A custom display area for karma status with progress bar and animations.
"""

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QProgressBar
from PyQt6.QtCore import Qt, QTimer, QPropertyAnimation, QEasingCurve, pyqtProperty
from PyQt6.QtGui import QFont, QColor

from core.constants import COLOR_ERROR, COLOR_WARNING, COLOR_SUCCESS, COLOR_PRIMARY_TEXT, COLOR_SECONDARY_BG


class KarmaDisplay(QWidget):
    """A custom display area for karma status"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("karmaDisplay")
        self._karma_points = 0
        self._displayed_karma = 0
        self._karma_threshold = 1000  # Maximum karma points for progress bar
        
        self.init_ui()
        self.setup_animations()

    def init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(15, 15, 15, 15)
        layout.setSpacing(10)
        
        # Create header label
        self.header_label = QLabel("Karma Status")
        self.header_label.setObjectName("header")
        layout.addWidget(self.header_label)
        
        # Create karma points layout
        karma_layout = QHBoxLayout()
        karma_layout.setContentsMargins(0, 0, 0, 0)
        
        self.karma_label = QLabel("💀 Karma-Schulden:")
        self.karma_label.setObjectName("karmaLabel")
        karma_layout.addWidget(self.karma_label)
        
        karma_layout.addStretch()
        
        self.karma_value_label = QLabel("0")
        self.karma_value_label.setObjectName("karmaValue")
        karma_layout.addWidget(self.karma_value_label)
        
        layout.addLayout(karma_layout)
        
        # Create progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setRange(0, self._karma_threshold)
        self.progress_bar.setValue(0)
        self.progress_bar.setTextVisible(False)
        layout.addWidget(self.progress_bar)
        
        # Create status label
        self.status_label = QLabel("Rein wie ein Engel")
        self.status_label.setObjectName("caption")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.status_label)

    def setup_animations(self):
        """Setup animations for the karma display"""
        # Karma value animation
        self.karma_animation = QPropertyAnimation(self, b"displayed_karma")
        self.karma_animation.setDuration(500)
        self.karma_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        # Progress bar animation
        self.progress_animation = QPropertyAnimation(self.progress_bar, b"value")
        self.progress_animation.setDuration(500)
        self.progress_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        # Status label animation
        self.status_animation = QPropertyAnimation(self.status_label, b"windowOpacity")
        self.status_animation.setDuration(300)
        self.status_animation.setEasingCurve(QEasingCurve.Type.OutCubic)

    def set_karma(self, karma_points):
        """Set the karma points with animation"""
        self._karma_points = karma_points
        
        # Start karma value animation
        self.karma_animation.setStartValue(self._displayed_karma)
        self.karma_animation.setEndValue(karma_points)
        self.karma_animation.start()
        
        # Start progress bar animation
        progress_value = min(karma_points, self._karma_threshold)
        self.progress_animation.setStartValue(self.progress_bar.value())
        self.progress_animation.setEndValue(progress_value)
        self.progress_animation.start()
        
        # Update status label
        self.update_status_label()
        
        # Start status label animation
        self.status_animation.setStartValue(0.3)
        self.status_animation.setEndValue(1.0)
        self.status_animation.start()

    def update_status_label(self):
        """Update the status label based on karma points"""
        if self._karma_points <= 0:
            status = "Rein wie ein Engel"
            color = COLOR_SUCCESS
        elif self._karma_points < 100:
            status = "Noch relativ unschuldig"
            color = COLOR_SUCCESS
        elif self._karma_points < 300:
            status = "Leichte Schulden"
            color = COLOR_WARNING
        elif self._karma_points < 500:
            status = "Mittlere Schulden"
            color = COLOR_WARNING
        elif self._karma_points < 800:
            status = "Hohe Schulden"
            color = COLOR_ERROR
        else:
            status = "Sehr hohe Schulden"
            color = COLOR_ERROR
            
        self.status_label.setText(status)
        self.status_label.setStyleSheet(f"color: {color};")

    @pyqtProperty(int)
    def displayed_karma(self):
        """Get the displayed karma points"""
        return self._displayed_karma

    @displayed_karma.setter
    def displayed_karma(self, value):
        """Set the displayed karma points"""
        self._displayed_karma = value
        self.karma_value_label.setText(str(value))
        
        # Update progress bar color based on karma level
        if value <= 0:
            self.progress_bar.setStyleSheet(
                f"QProgressBar::chunk {{ background-color: {COLOR_SUCCESS}; }}"
            )
        elif value < 300:
            self.progress_bar.setStyleSheet(
                f"QProgressBar::chunk {{ background-color: {COLOR_WARNING}; }}"
            )
        else:
            self.progress_bar.setStyleSheet(
                f"QProgressBar::chunk {{ background-color: {COLOR_ERROR}; }}"
            )

    def get_karma(self):
        """Get the current karma points"""
        return self._karma_points

    def reset_karma(self):
        """Reset karma to zero"""
        self.set_karma(0)

    def set_karma_threshold(self, threshold):
        """Set the karma threshold for the progress bar"""
        self._karma_threshold = threshold
        self.progress_bar.setRange(0, threshold)
        
    def resizeEvent(self, event):
        """Handle resize events for responsive design"""
        super().resizeEvent(event)
        # Adjust font size based on widget width
        width = self.width()
        if width < 300:
            # Small widget - reduce font size
            font = self.karma_value_label.font()
            font.setPointSize(12)
            self.karma_value_label.setFont(font)
        elif width > 600:
            # Large widget - increase font size
            font = self.karma_value_label.font()
            font.setPointSize(18)
            self.karma_value_label.setFont(font)
        else:
            # Medium widget - default font size
            font = self.karma_value_label.font()
            font.setPointSize(15)
            self.karma_value_label.setFont(font)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
    
    app = QApplication(sys.argv)
    
    # Create test widget
    widget = QWidget()
    layout = QVBoxLayout(widget)
    
    # Create karma display
    karma_display = KarmaDisplay()
    layout.addWidget(karma_display)
    
    # Create a button to set karma
    button = QPushButton("Set Karma to 500")
    button.clicked.connect(lambda: karma_display.set_karma(500))
    layout.addWidget(button)
    
    widget.show()
    
    sys.exit(app.exec())