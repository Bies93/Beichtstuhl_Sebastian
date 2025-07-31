#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Card Widget for Beichtsthul Modern
A styled container widget with a glassmorphism effect.
"""

from PyQt6.QtWidgets import QFrame, QGridLayout, QWidget, QLabel, QApplication

class CardWidget(QFrame):
    """
    A custom frame that sets its object name to 'card' to be styled
    by the application's QSS. It uses a QGridLayout by default.
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Set the object name to be targeted by the QSS file
        self.setObjectName("card")
        
        # Don't set a default layout, let the user set it

    def add_widget(self, widget, row, col, rowspan=1, colspan=1):
        """Convenience method to add a widget to the card's grid layout."""
        if not self.layout():
            # If no layout is set, create a grid layout
            from PyQt6.QtWidgets import QGridLayout
            layout = QGridLayout(self)
            self.setLayout(layout)
        self.layout().addWidget(widget, row, col, rowspan, colspan)

if __name__ == "__main__":
    import sys

    # This test requires the main stylesheet to be generated and loaded
    # to see the glassmorphism effect.
    
    app_qss = """
    .card {
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.04);
        /* The backdrop-filter property is not supported in PyQt QSS,
           so the glass effect needs to be simulated or handled differently.
           For this test, we just use a semi-transparent background. */
    }
    """

    app = QApplication(sys.argv)
    app.setStyleSheet(app_qss)

    window = QWidget()
    window.setStyleSheet("background-color: #0E1222;")
    main_layout = QGridLayout(window)
    
    # Create a card and add some content
    test_card = CardWidget()
    test_card.add_widget(QLabel("This is a CardWidget"), 0, 0)
    test_card.add_widget(QLabel("It uses a grid layout."), 1, 0)
    
    main_layout.addWidget(test_card, 0, 0)
    
    window.resize(400, 300)
    window.show()
    
    sys.exit(app.exec())