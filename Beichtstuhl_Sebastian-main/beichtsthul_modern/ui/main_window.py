#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main Window for Beichtsthul Modern
The main application window that hosts all UI components with cyberpunk styling.
"""

import sys
import random
import time
from PyQt6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QStatusBar, QApplication, QGridLayout, QStackedLayout
)
from PyQt6.QtCore import Qt, QRect, pyqtSignal, QSize, QTimer
from PyQt6.QtGui import QFont, QColor

from ui.components.animated_button import AnimatedButton
from ui.components.card_widget import CardWidget
from ui.components.confession_input import ConfessionInput
from ui.components.response_display import ResponseDisplay
from ui.components.karma_display import KarmaDisplay
from ui.components.monk_visualizer import MonkVisualizer
from ui.effects.background_parallax import ParallaxBackground
from ui.dialogs.settings_dialog import SettingsDialog
from ui.resources.styles import get_main_window_style, get_label_style, get_status_bar_style
from ui.resources.animations import AnimationDefinitions
from utils.animation_utils import create_fade_animation
from utils.resource_loader import resource_loader
from core.antwort_generator import AntwortGenerator
from core.karma_rechner import KarmaRechner
from core.datei_manager import DateiManager
from core.statistik_manager import StatistikManager
from core.constants import APP_NAME, WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_MIN_WIDTH, WINDOW_MIN_HEIGHT
from design_tokens.design_tokens import ColorTokens, FontTokens


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
        """Initialize the user interface with a stacked layout for parallax effect."""
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Outer layout for the central widget
        self._outer_layout = QVBoxLayout(self.central_widget)
        self._outer_layout.setContentsMargins(0, 0, 0, 0)
        self._outer_layout.setSpacing(0)

        # Stacked layout hosts background and content container
        self.stacked_layout = QStackedLayout()
        self._outer_layout.addLayout(self.stacked_layout)

        # Parallax background is the bottom layer
        self.parallax_bg = ParallaxBackground()

        # Content container (separate widget) is the top layer
        self.content_container = QWidget()
        # Give content a slight translucent panel background to be visually distinct above parallax
        self.content_container.setStyleSheet("background: rgba(10, 10, 16, 0.65);")

        # Add pages to the stack
        self.stacked_layout.addWidget(self.parallax_bg)
        self.stacked_layout.addWidget(self.content_container)

        # The main layout will be applied to the content container
        self.main_layout = QGridLayout(self.content_container)
        for i in range(12):
            self.main_layout.setColumnStretch(i, 1)
        # Allocate space for rows: top row content + footer
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 0)
        self.content_container.setMinimumSize(600, 400)

        # Ensure the content layer is visible on top of the parallax background
        self.stacked_layout.setCurrentWidget(self.content_container)


        # Left Card: Text Input
        self.input_card = CardWidget()
        self.input_card.setObjectName("inputCard")
        self.confession_input = ConfessionInput()
        self.confession_input.confession_submitted.connect(self.handle_confession)
        self.response_display = ResponseDisplay()
        
        input_layout = QVBoxLayout()
        input_layout.addWidget(self.confession_input)
        input_layout.addWidget(self.response_display)
        self.input_card.setLayout(input_layout)

        # Improve label contrast and hierarchy on startup (safety)
        # Ensure QSS types apply for existing labels after construction
        try:
            if hasattr(self.confession_input, "header_label"):
                self.confession_input.header_label.setProperty("type", "header")
            # Karma header bound in component; no-op here
        except Exception:
            pass
        self.input_card.setMinimumHeight(200)

        # Right Card: Monk Visualizer
        self.visualizer_card = CardWidget()
        self.visualizer_card.setObjectName("visualizerCard")
        self.monk_visualizer = MonkVisualizer()
        self.karma_display = KarmaDisplay()
        self.karma_display.set_karma(self.karma_schulden)

        visualizer_layout = QVBoxLayout()
        visualizer_layout.addWidget(self.monk_visualizer)
        visualizer_layout.addWidget(self.karma_display)
        self.visualizer_card.setLayout(visualizer_layout)
        self.visualizer_card.setMinimumHeight(200)

        # Add cards to the grid
        self.main_layout.addWidget(self.input_card, 0, 0, 1, 6)
        self.main_layout.addWidget(self.visualizer_card, 0, 6, 1, 6)

        # Sticky Footer: Action Bar
        self.action_bar = QWidget()
        self.action_bar.setObjectName("footer")
        action_layout = QHBoxLayout(self.action_bar)
        
        self.confess_button = AnimatedButton("Beichten")
        self.confess_button.clicked.connect(self.handle_confession_button)
        
        self.stats_button = AnimatedButton("Statistiken")
        self.stats_button.clicked.connect(self.show_statistics)
        
        self.reset_button = AnimatedButton("Reset")
        self.reset_button.clicked.connect(self.reset_statistics)
        
        action_layout.addStretch()
        action_layout.addWidget(self.confess_button)
        action_layout.addWidget(self.stats_button)
        action_layout.addWidget(self.reset_button)
        action_layout.addStretch()

        self.main_layout.addWidget(self.action_bar, 1, 0, 1, 12)
        # reinforce row stretches for stable layout
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 0)

        # TEMP DEBUG STYLES: show visible borders for cards and action bar
        self.content_container.setStyleSheet(self.content_container.styleSheet() + """
            QWidget#inputCard { border: 2px solid #00EAFE; }
            QWidget#visualizerCard { border: 2px solid #FF0078; }
            QWidget#footer { border-top: 2px solid #444; }
        """)

        # Create status bar
        self.create_status_bar()

        # Set accessible names and descriptions
        self.set_accessible_info()

        # Set tab order
        self.set_tab_order()

    def create_status_bar(self):
        """Create the status bar"""
        self.status_bar = QStatusBar()
        self.setStatusBar(self.status_bar)
        self.status_bar.showMessage("Bereit für etwas Selbsterkenntnis?")

    def set_accessible_info(self):
        """Sets accessible names and descriptions for widgets."""
        self.confession_input.text_input.setAccessibleName("Beichteingabe")
        self.confession_input.text_input.setAccessibleDescription("Geben Sie hier Ihre Beichte ein.")
        
        self.confess_button.setAccessibleName("Beichten")
        self.confess_button.setAccessibleDescription("Klicken Sie hier, um Ihre Beichte abzusenden.")
        
        self.stats_button.setAccessibleName("Statistiken")
        self.stats_button.setAccessibleDescription("Zeigt Ihre Beichtstatistiken an.")
        
        self.reset_button.setAccessibleName("Zurücksetzen")
        self.reset_button.setAccessibleDescription("Setzt alle Ihre Statistiken und Karmaschulden zurück.")

    def set_tab_order(self):
        """Sets the tab order for interactive widgets."""
        # Only set tab order if widgets are visible and in the same window
        try:
            if (self.confession_input.text_input.isVisible() and
                self.confess_button.isVisible() and
                self.stats_button.isVisible() and
                self.reset_button.isVisible()):
                self.setTabOrder(self.confession_input.text_input, self.confess_button)
                self.setTabOrder(self.confess_button, self.stats_button)
                self.setTabOrder(self.stats_button, self.reset_button)
        except Exception as e:
            print(f"Warning: Could not set tab order: {e}")

    def apply_styles(self):
        """Apply stylesheets to the window and components"""
        # The main stylesheet is loaded in main.py
        pass

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
        """Show a welcome message when the application starts and ensure content is on top"""
        # Safety: force the content page visible in case external code altered the stack
        try:
            if hasattr(self, "stacked_layout") and hasattr(self, "content_container"):
                self.stacked_layout.setCurrentWidget(self.content_container)
                # Print debug info about layout/page and sizes
                try:
                    print(f"[UI DEBUG] currentStackIndex={self.stacked_layout.currentIndex()} pages={self.stacked_layout.count()}")
                    print(f"[UI DEBUG] content_container size={self.content_container.size()}")
                    print(f"[UI DEBUG] parallax_bg size={self.parallax_bg.size()}")
                except Exception:
                    pass
        except Exception:
            pass
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
        self.adjust_component_sizes(event.size().width(), event.size().height())

    def update_layout_for_size(self, size):
        """Update layout based on window size"""
        width = size.width()
        height = size.height()
        
        # Define breakpoints
        compact_width = 800
        compact_height = 600
        
        # Adjust layout based on screen size
        if width < compact_width or height < compact_height:
            # Compact layout - stack elements vertically
            self.switch_to_compact_layout()
        else:
            # Standard layout - use grid
            self.switch_to_standard_layout()
            
    def switch_to_compact_layout(self):
        """Switch to a compact vertical layout for smaller screens"""
        # Remove existing widgets from grid
        for i in reversed(range(self.main_layout.count())):
            self.main_layout.takeAt(i)
            
        # Create a vertical layout for compact view
        compact_layout = QVBoxLayout(self.content_container)
        compact_layout.setContentsMargins(10, 10, 10, 10)
        compact_layout.setSpacing(15)
        
        # Add cards vertically
        compact_layout.addWidget(self.input_card)
        compact_layout.addWidget(self.visualizer_card)
        compact_layout.addWidget(self.action_bar)
        
        # Update the content container layout
        # Note: This is a simplified approach - in a real implementation,
        # you might want to use a more sophisticated layout management
        
    def switch_to_standard_layout(self):
        """Switch back to the standard grid layout"""
        # Clear any existing layout
        for i in reversed(range(self.main_layout.count())):
            self.main_layout.takeAt(i)
            
        # Restore the standard grid layout
        self.main_layout.addWidget(self.input_card, 0, 0, 1, 7)
        self.main_layout.addWidget(self.visualizer_card, 0, 7, 1, 5)
        self.main_layout.addWidget(self.action_bar, 1, 0, 1, 12)
        
        # Update row stretches
        self.main_layout.setRowStretch(0, 1)
        self.main_layout.setRowStretch(1, 0)

    def adjust_component_sizes(self, width, height):
        """Adjust component sizes based on window dimensions"""
        # Adjust font sizes based on window width
        if width < 600:
            # Small window - reduce font sizes
            self.setFontSize(self, 10)
        elif width < 1000:
            # Medium window - default font sizes
            self.setFontSize(self, 12)
        else:
            # Large window - increase font sizes
            self.setFontSize(self, 14)
            
    def setFontSize(self, widget, size):
        """Recursively set font size for a widget and its children"""
        font = widget.font()
        font.setPointSize(size)
        widget.setFont(font)
        
        # Apply to all child widgets
        for child in widget.findChildren(QWidget):
            child_font = child.font()
            child_font.setPointSize(size)
            child.setFont(child_font)

    def closeEvent(self, event):
        """Handle window close event safely and avoid blocking shutdown"""
        # Immediate accept to prevent shutdown hang on interrupt or stalled animations
        event.accept()
        try:
            # Optionally trigger a non-blocking fade without gating close
            fade_out = create_fade_animation(
                self,
                **AnimationDefinitions.window_fade_out()
            )
            fade_out.start()
        except Exception:
            # If animation setup fails, just proceed with close
            pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())