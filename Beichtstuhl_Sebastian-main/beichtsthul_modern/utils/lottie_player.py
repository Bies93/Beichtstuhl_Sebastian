#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Lottie Animation Player for Beichtsthul Modern
Handles loading and playing Lottie animations.
"""

import os
import sys
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import QTimer, Qt, QSize
from PyQt6.QtGui import QImage, QPixmap, QPainter
import lottie
from lottie.importers import importers
from lottie.exporters import exporters


class LottiePlayer(QWidget):
    """A widget for playing Lottie animations"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.animation = None
        self.current_frame = 0
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.next_frame)
        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout = QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.setContentsMargins(0, 0, 0, 0)
        
        self.setSizePolicy(self.label.sizePolicy())
        
    def load_animation(self, file_path):
        """
        Load a Lottie animation from file
        
        Args:
            file_path: Path to the Lottie JSON file
        """
        try:
            # Try to load the animation
            self.animation = importers.get("lottie").process(file_path)
            self.current_frame = 0
            self.render_frame()
            return True
        except Exception as e:
            print(f"Failed to load Lottie animation: {e}")
            return False
    
    def play(self, fps=None):
        """
        Start playing the animation
        
        Args:
            fps: Frames per second (defaults to animation's natural FPS)
        """
        if not self.animation:
            return
            
        if fps is None:
            fps = self.animation.frame_rate
            
        self.timer.start(1000 // fps)
    
    def pause(self):
        """Pause the animation"""
        self.timer.stop()
    
    def stop(self):
        """Stop the animation and reset to first frame"""
        self.timer.stop()
        self.current_frame = 0
        self.render_frame()
    
    def next_frame(self):
        """Advance to the next frame"""
        if not self.animation:
            return
            
        self.current_frame = (self.current_frame + 1) % self.animation.out_point
        self.render_frame()
    
    def render_frame(self):
        """Render the current frame"""
        if not self.animation:
            return
            
        try:
            # Render the current frame to an image
            frame = self.animation.frame_to_png(self.current_frame, scale=1.0)
            
            # Convert to QImage
            height, width, _ = frame.shape
            bytes_per_line = 4 * width
            qimage = QImage(frame.data, width, height, bytes_per_line, QImage.Format.Format_RGBA8888)
            
            # Convert to QPixmap and display
            pixmap = QPixmap.fromImage(qimage)
            self.label.setPixmap(pixmap)
            
            # Update widget size
            self.setFixedSize(pixmap.size())
        except Exception as e:
            print(f"Failed to render frame: {e}")
    
    def set_size(self, size):
        """
        Set the size of the player
        
        Args:
            size: QSize for the player
        """
        self.setFixedSize(size)
        self.label.setFixedSize(size)
    
    def get_duration(self):
        """
        Get the duration of the animation in seconds
        
        Returns:
            float: Duration in seconds
        """
        if not self.animation:
            return 0
        return self.animation.duration


# Example usage
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QHBoxLayout
    
    app = QApplication(sys.argv)
    
    # Create main window
    window = QMainWindow()
    window.setWindowTitle("Lottie Player Test")
    window.setGeometry(100, 100, 400, 300)
    
    # Create central widget
    central_widget = QWidget()
    window.setCentralWidget(central_widget)
    
    # Create layout
    layout = QVBoxLayout(central_widget)
    
    # Create Lottie player
    player = LottiePlayer()
    
    # Create buttons
    button_layout = QHBoxLayout()
    play_button = QPushButton("Play")
    pause_button = QPushButton("Pause")
    stop_button = QPushButton("Stop")
    
    # Connect buttons
    play_button.clicked.connect(lambda: player.play())
    pause_button.clicked.connect(player.pause)
    stop_button.clicked.connect(player.stop)
    
    # Add widgets to layout
    layout.addWidget(player)
    button_layout.addWidget(play_button)
    button_layout.addWidget(pause_button)
    button_layout.addWidget(stop_button)
    layout.addLayout(button_layout)
    
    # Try to load an animation (you would need to provide a Lottie JSON file)
    # player.load_animation("path/to/animation.json")
    
    window.show()
    sys.exit(app.exec())