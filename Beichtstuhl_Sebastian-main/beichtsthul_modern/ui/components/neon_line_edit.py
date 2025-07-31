#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Neon Line Edit for Beichtsthul Modern
A custom QLineEdit with a cyberpunk-styled caret color.
"""

from PyQt6.QtWidgets import QLineEdit, QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor

class NeonLineEdit(QLineEdit):
    """
    A QLineEdit that sets its caret color to the primary accent color
    to fit the cyberpunk theme.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Set the caret color programmatically using a palette
        self.setup_caret_color()

    def setup_caret_color(self):
        """
        Sets the color of the editing cursor (caret) using the widget's palette.
        """
        palette = self.palette()
        # The accent color is hardcoded here but should ideally come from design tokens
        # at runtime. For now, this ensures the effect.
        accent_color = QColor("#00E5FF")  # $accent.1 from design_tokens.json
        palette.setColor(QPalette.ColorRole.Text, accent_color)
        self.setPalette(palette)

if __name__ == "__main__":
    import sys

    # This test demonstrates the caret color change.
    
    app_qss = """
    QLineEdit {
        background: #141826; /* bg.panel */
        border: 1px solid #1F2539;
        border-radius: 6px; /* radius.sm */
        padding: 6px;
        color: #EDEFFF; /* text.primary */
    }
    """

    app = QApplication(sys.argv)
    app.setStyleSheet(app_qss)

    window = QWidget()
    window.setStyleSheet("background-color: #0E1222;")
    layout = QVBoxLayout(window)
    
    # Create a NeonLineEdit
    neon_edit = NeonLineEdit()
    neon_edit.setPlaceholderText("Enter your confession...")
    
    layout.addWidget(neon_edit)
    
    window.resize(400, 100)
    window.show()
    
    sys.exit(app.exec())