#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Beichtsthul Modern - Main Entry Point
A modern, PyQt6-based implementation of the sardonic confessional booth application with cyberpunk styling.
"""

import sys
import os
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase

from ui.main_window import MainWindow
from utils.resource_loader import resource_loader
from design_tokens.generate_tokens import main as generate_tokens
from core.constants import FONT_HEADLINE, FONT_BODY, FONT_MONOSPACE

# Add the project root to sys.path for imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))


def setup_high_dpi_support(app):
    """Setup high-DPI support for the application"""
    # Enable high-DPI scaling (Qt6 enables this by default)
    # Set default screen scale factor
    app.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )


def setup_fonts(app):
    """Setup application fonts"""
    # Preload cyberpunk fonts (ignore if fonts are missing for now)
    try:
        resource_loader.load_cyberpunk_fonts()
    except Exception as e:
        print(f"Warning: Failed to load fonts: {e}")
    
    # Set default application font
    default_font = QFont(FONT_BODY if FONT_BODY else "Arial")
    default_font.setPointSize(9)  # Base size that will scale with DPI
    app.setFont(default_font)


def setup_styles(app):
    """Setup application styles"""
    # Generate tokens at startup
    try:
        generate_tokens()
    except Exception as e:
        print(f"Warning: Failed to generate design tokens: {e}")
    
    # Apply application-wide stylesheet
    try:
        # Load the generated QSS file
        qss_path = os.path.join(os.path.dirname(__file__), "design_tokens", "style.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r", encoding="utf-8") as f:
                app.setStyleSheet(f.read())
        else:
            print("Warning: style.qss not found")
    except Exception as e:
        print(f"Warning: Failed to load stylesheet: {e}")


def main():
    """Main application entry point"""
    # Setup high-DPI support before creating QApplication
    QApplication.setHighDpiScaleFactorRoundingPolicy(
        Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
    )
    
    # Create Qt Application
    app = QApplication(sys.argv)
    
    # Set application attributes
    app.setApplicationName("Der Sarkastische Beichtstuhl")
    app.setApplicationVersion("2.0.0")
    app.setOrganizationName("Beichtsthul Developers")
    
    # Setup fonts
    setup_fonts(app)
    
    # Setup styles
    setup_styles(app)
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Run application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()