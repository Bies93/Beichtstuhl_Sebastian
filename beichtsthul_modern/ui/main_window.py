#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main Window for Beichtsthul Modern
The main application window that hosts all UI components.
"""

import sys
import random
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QStatusBar, QApplication
)
from PyQt6.QtCore import Qt, QRect, pyqtSignal, QSize
from PyQt6.QtGui import QFont

from ui.components.animated_button import AnimatedButton
from ui.components.confession_input import ConfessionInput
from ui.components.response_display import ResponseDisplay
from ui.components.karma_display import KarmaDisplay
from ui.components.monk_visualizer import MonkVisualizer
from ui.resources.styles import get_main_window_style, get_label_style, get_status_bar_style
from ui.resources.animations import AnimationDefinitions
from utils.animation_utils import create_fade_animation
from core.antwort_generator import AntwortGenerator
from core.karma_rechner import KarmaRechner
from core.datei_manager import DateiManager
from core.statistik_manager import StatistikManager
from core.constants import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT


class MainWindow(QMainWindow):
    """Main application window"""

    # Signals
    confession_submitted = pyqtSignal(str)
    karma_changed = pyqtSignal(int)

    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.setMinimumSize(WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT)
        
        # Initialize core modules
        self.antwort_generator = AntwortGenerator()
        self.karma_rechner = KarmaRechner()
        self.datei_manager = DateiManager()
        self.statistik_manager = StatistikManager()
        
        # Load saved data
        self.karma_schulden, self.beicht_historie, self.suenden_kategorien = self.datei_manager.lade_daten()
        
        # Initialize UI components
        self.init_ui()
        
        # Setup animations
        self.setup_animations()
        
        # Apply styles
        self.apply_styles()
        
        # Show welcome message
        self.show_welcome_message()

    def init_ui(self):
        """Initialize the user interface"""
        # Create central widget
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        
        # Create main layout
        self.main_layout = QVBoxLayout(self.central_widget)
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(15)
        
        # Create title
        self.create_title()
        
        # Create monk visualizer
        self.create_monk_visualizer()
        
        # Create confession input
        self.create_confession_input()
        
        # Create action buttons
        self.create_action_buttons()
        
        # Create response display
        self.create_response_display()
        
        # Create karma display
        self.create_karma_display()
        
        # Create status bar
        self.create_status_bar()

    def create_title(self):
        """Create the application title"""
        self.title_label = QLabel(APP_NAME)
        self.title_label.setObjectName("title")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addWidget(self.title_label)

    def create_monk_visualizer(self):
        """Create the monk character visualizer"""
        self.monk_visualizer = MonkVisualizer()
        self.main_layout.addWidget(self.monk_visualizer)

    def create_confession_input(self):
        """Create the confession input area"""
        self.confession_input = ConfessionInput()
        self.confession_input.confession_submitted.connect(self.handle_confession)
        self.main_layout.addWidget(self.confession_input)

    def create_action_buttons(self):
        """Create the action buttons"""
        self.button_layout = QHBoxLayout()
        
        self.confess_button = AnimatedButton("⚡ BEICHTEN ⚡")
        self.confess_button.setObjectName("primary")
        self.confess_button.clicked.connect(self.handle_confession_button)
        self.button_layout.addWidget(self.confess_button)
        
        self.stats_button = AnimatedButton("📊 Statistiken")
        self.stats_button.setObjectName("secondary")
        self.stats_button.clicked.connect(self.show_statistics)
        self.button_layout.addWidget(self.stats_button)
        
        self.reset_button = AnimatedButton("🔄 Reset")
        self.reset_button.setObjectName("secondary")
        self.reset_button.clicked.connect(self.reset_statistics)
        self.button_layout.addWidget(self.reset_button)
        
        self.main_layout.addLayout(self.button_layout)

    def create_response_display(self):
        """Create the response display area"""
        self.response_display = ResponseDisplay()
        self.main_layout.addWidget(self.response_display)

    def create_karma_display(self):
        """Create the karma display"""
        self.karma_display = KarmaDisplay()
        self.karma_display.set_karma(self.karma_schulden)
        self.main_layout.addWidget(self.karma_display)

    def create_status_bar(self):
        """Create the status bar"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Bereit für etwas Selbsterkenntnis?")

    def apply_styles(self):
        """Apply stylesheets to the window and components"""
        self.setStyleSheet(get_main_window_style())
        self.title_label.setStyleSheet(get_label_style())
        self.status_bar.setStyleSheet(get_status_bar_style())

    def setup_animations(self):
        """Setup window animations"""
        # Create fade-in animation
        self.fade_animation = create_fade_animation(
            self, 
            **AnimationDefinitions.window_fade_in()
        )
        
        # Connect karma change signal to karma display
        self.karma_changed.connect(self.karma_display.set_karma)

    def show_welcome_message(self):
        """Show a welcome message when the application starts"""
        welcome_messages = [
            "Willkommen in der Höhle der Wahrheit!",
            "Ein neues Opfer... äh, Besucher!",
            "Bereit für etwas Selbsterkenntnis?"
        ]
        self.response_display.set_text(random.choice(welcome_messages))
        self.monk_visualizer.set_emotion("neutral")
        
        # Start fade-in animation
        self.fade_animation.start()

    def handle_confession_button(self):
        """Handle the confession button click"""
        confession = self.confession_input.get_text()
        if confession:
            self.handle_confession(confession)
        else:
            self.response_display.set_text("Du musst schon was beichten, Faulpelz!")
            self.monk_visualizer.set_emotion("genervt")

    def handle_confession(self, confession_text):
        """Handle a submitted confession"""
        # Emit signal
        self.confession_submitted.emit(confession_text)
        
        # Process the confession
        self.process_confession(confession_text)
        
        # Clear the input
        self.confession_input.clear_text()

    def process_confession(self, confession_text):
        """Process a confession and generate response"""
        # Categorize the sin
        kategorie = self.antwort_generator.kategorisiere_suende(confession_text)
        
        # Check for easter eggs
        easter_antwort, easter_emotion = self.antwort_generator.prüfe_easter_eggs(confession_text)
        
        if easter_antwort:
            antwort = easter_antwort
            emotion = easter_emotion
        else:
            antwort = self.antwort_generator.get_antwort(kategorie)
            emotion = self.antwort_generator.emotionen_mapping.get(kategorie, "neutral")
        
        # Calculate karma debt
        neue_schulden = self.karma_rechner.berechne_karma_schulden(kategorie, confession_text)
        self.karma_schulden += neue_schulden
        
        # Update history
        self.beicht_historie.append({
            "suende": confession_text,
            "kategorie": kategorie,
            "karma": neue_schulden
        })
        
        # Update category counts
        if kategorie in self.suenden_kategorien:
            self.suenden_kategorien[kategorie] += 1
        else:
            self.suenden_kategorien[kategorie] = 1
        
        # Save data
        self.datei_manager.speichere_daten(
            self.karma_schulden, 
            self.beicht_historie, 
            self.suenden_kategorien
        )
        
        # Update UI
        self.response_display.set_text(f"{antwort}\n\n+{neue_schulden} Karma-Schulden!")
        self.karma_changed.emit(self.karma_schulden)
        self.monk_visualizer.set_emotion(emotion)
        
        # Update status bar
        self.status_bar.showMessage(f"Verarbeitet: {kategorie} (+{neue_schulden} Karma)")

    def show_statistics(self):
        """Show statistics dialog"""
        try:
            self.statistik_manager.zeige_statistiken(
                self.karma_schulden,
                self.beicht_historie,
                self.suenden_kategorien
            )
        except Exception as e:
            self.status_bar.showMessage(f"Fehler beim Anzeigen der Statistiken: {str(e)}")

    def reset_statistics(self):
        """Reset all statistics"""
        if self.statistik_manager.bestätige_reset():
            self.karma_schulden = 0
            self.beicht_historie = []
            self.suenden_kategorien = {}
            
            # Save reset data
            self.datei_manager.speichere_daten(
                self.karma_schulden, 
                self.beicht_historie, 
                self.suenden_kategorien
            )
            
            # Update UI
            self.karma_changed.emit(self.karma_schulden)
            self.response_display.set_text("Du bist rein gewaschen... vorerst.")
            self.monk_visualizer.set_emotion("neutral")
            self.status_bar.showMessage("Statistiken zurückgesetzt")

    def resizeEvent(self, event):
        """Handle window resize events for responsive design"""
        super().resizeEvent(event)
        self.update_layout_for_size(event.size())

    def update_layout_for_size(self, size):
        """Update layout based on window size"""
        width = size.width()
        height = size.height()
        
        # Adjust spacing based on window size
        if width < 800 or height < 600:
            # Small window - reduce spacing
            self.main_layout.setSpacing(10)
            self.main_layout.setContentsMargins(10, 10, 10, 10)
        elif width > 1200 or height > 900:
            # Large window - increase spacing
            self.main_layout.setSpacing(20)
            self.main_layout.setContentsMargins(30, 30, 30, 30)
        else:
            # Medium window - default spacing
            self.main_layout.setSpacing(15)
            self.main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Adjust component sizes
        self.adjust_component_sizes(width, height)

    def adjust_component_sizes(self, width, height):
        """Adjust component sizes based on window dimensions"""
        # Adjust monk visualizer size
        if hasattr(self, 'monk_visualizer'):
            # Set minimum height based on window height
            min_height = max(200, height // 4)
            self.monk_visualizer.setMinimumHeight(min_height)
        
        # Adjust confession input size
        if hasattr(self, 'confession_input'):
            # Set maximum height based on window height
            max_height = max(100, height // 6)
            self.confession_input.text_input.setMaximumHeight(max_height)
        
        # Adjust button layout for very narrow windows
        if width < 600:
            # Change button layout to vertical for narrow windows
            self.button_layout.setDirection(QHBoxLayout.Direction.TopToBottom)
        else:
            # Default horizontal layout
            self.button_layout.setDirection(QHBoxLayout.Direction.LeftToRight)

    def closeEvent(self, event):
        """Handle window close event"""
        # Create fade-out animation
        fade_out = create_fade_animation(
            self, 
            **AnimationDefinitions.window_fade_out()
        )
        
        # Start animation and close when finished
        fade_out.finished.connect(lambda: event.accept())
        fade_out.start()
        
        # Accept the event to prevent immediate closing
        event.ignore()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())