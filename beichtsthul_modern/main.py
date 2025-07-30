#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Beichtsthul Modern - Main Entry Point
A modern, PyQt6-based implementation of the sardonic confessional booth application.
"""

import sys
from PyQt6.QtWidgets import QApplication
from PyQt6.QtCore import Qt
from ui.main_window import MainWindow


def main():
    """Main application entry point"""
    # Create Qt Application
    app = QApplication(sys.argv)
    
    # Set application attributes
    app.setApplicationName("Der Sarkastische Beichtstuhl")
    app.setApplicationVersion("2.0.0")
    app.setOrganizationName("Beichtsthul Developers")
    
    # Create and show main window
    window = MainWindow()
    window.show()
    
    # Run application event loop
    sys.exit(app.exec())


if __name__ == "__main__":
    main()