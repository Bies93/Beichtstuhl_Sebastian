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

# Import the generated resource file
from assets import fonts_rc
from ui.main_window import MainWindow
from utils.resource_loader import resource_loader
# We will now use the new build script, so generate_tokens is no longer needed here.
# We will run the build script as a separate process or import it.
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
    """Setup application fonts without requiring Qt resources (pyrcc6)"""
    loaded_families = []
    try:
        from utils.resource_loader import resource_loader
        fs_paths = [
            resource_loader.get_font_path("Orbitron-Regular.ttf"),
            resource_loader.get_font_path("Inter-Regular.ttf"),
            resource_loader.get_font_path("JetBrainsMono-Regular.ttf"),
        ]
        for path in fs_paths:
            if os.path.exists(path):
                font_id = QFontDatabase.addApplicationFont(path)
                if font_id != -1:
                    fams = QFontDatabase.applicationFontFamilies(font_id)
                    if fams:
                        loaded_families.append(fams[0])
    except Exception:
        # If anything goes wrong, we will still set a safe system default below
        pass

    # Choose stable system defaults if custom fonts not loaded
    default_family = loaded_families[1] if len(loaded_families) > 1 else ("Segoe UI" if sys.platform.startswith("win") else "Arial")
    default_font = QFont(default_family)
    default_font.setPointSize(10)
    app.setFont(default_font)

    # Set default application font
    default_font = QFont(FONT_BODY if FONT_BODY else "Arial")
    default_font.setPointSize(9)  # Base size that will scale with DPI
    app.setFont(default_font)


def setup_styles(app):
    """Setup application styles"""
    # Run the build script to generate the final QSS file
    try:
        # Import and run the build script
        from design_tokens import build_style
        print("Stylesheet generated successfully.")
    except ImportError as e:
        print(f"Error: Could not import build_style script: {e}")
    except Exception as e:
        print(f"Warning: Failed to generate stylesheet with build_style.py: {e}")

    # Apply application-wide stylesheet
    try:
        # Load the generated app.qss file
        qss_path = os.path.join(os.path.dirname(__file__), "design_tokens", "app.qss")
        if os.path.exists(qss_path):
            with open(qss_path, "r", encoding="utf-8") as f:
                app.setStyleSheet(f.read())
        else:
            print("Warning: app.qss not found. Please run the build_style.py script.")
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