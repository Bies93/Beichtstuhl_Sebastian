#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Confession Input for Beichtsthul Modern
A custom text input area for confessions with character counting and animations.
"""

from PyQt6.QtWidgets import QWidget, QTextEdit, QLabel, QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal, QTimer
from PyQt6.QtGui import QTextCursor, QFont, QPalette, QColor

from core.constants import COLOR_WARNING, COLOR_ERROR, COLOR_PRIMARY_TEXT, COLOR_SECONDARY_BG


class ConfessionInput(QWidget):
    """A custom text input area for confessions"""

    # Signals
    confession_submitted = pyqtSignal(str)
    text_changed = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.max_characters = 500
        self.warning_threshold = 50
        self.character_count = 0
        
        self.init_ui()
        self.setup_animations()

    def init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        
        # Create header label
        self.header_label = QLabel("Beichte deine Sünde, du verlorene Seele:")
        self.header_label.setObjectName("header")
        layout.addWidget(self.header_label)
        
        # Create text input area
        self.text_input = QTextEdit()
        self.text_input.setObjectName("confessionInput")
        self.text_input.setMaximumHeight(100)
        self.text_input.textChanged.connect(self.on_text_changed)
        layout.addWidget(self.text_input)
        
        # Create character counter
        counter_layout = QHBoxLayout()
        counter_layout.setContentsMargins(0, 0, 0, 0)
        
        self.char_counter_label = QLabel()
        self.char_counter_label.setObjectName("caption")
        self.char_counter_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        counter_layout.addWidget(self.char_counter_label)
        
        layout.addLayout(counter_layout)
        
        # Initialize character counter
        self.update_character_counter()

    def setup_animations(self):
        """Setup animations for the input area"""
        # Character counter animation timer
        self.counter_animation_timer = QTimer()
        self.counter_animation_timer.setSingleShot(True)
        self.counter_animation_timer.timeout.connect(self.reset_counter_color)

    def on_text_changed(self):
        """Handle text change event"""
        text = self.get_text()
        self.character_count = len(text)
        self.text_changed.emit(text)
        self.update_character_counter()
        
        # Emit signal when Enter is pressed (with Ctrl/Cmd)
        if self.text_input.hasFocus():
            cursor = self.text_input.textCursor()
            if cursor.position() > 0:
                # Check if the last character is Enter
                if text.endswith('\n') and not text.endswith('\n\n'):
                    # Remove the newline and emit signal
                    self.text_input.textCursor().deletePreviousChar()
                    self.confession_submitted.emit(self.get_text())
                    self.clear_text()

    def update_character_counter(self):
        """Update the character counter display"""
        remaining = self.max_characters - self.character_count
        
        # Update text
        self.char_counter_label.setText(f"{self.character_count}/{self.max_characters}")
        
        # Update color based on remaining characters
        if remaining <= 0:
            # Limit reached
            self.char_counter_label.setStyleSheet(f"color: {COLOR_ERROR}; font-weight: bold;")
            # Limit the text to max characters
            if self.character_count > self.max_characters:
                cursor = self.text_input.textCursor()
                cursor.movePosition(QTextCursor.MoveOperation.End)
                cursor.setPosition(len(self.get_text()[:self.max_characters]), QTextCursor.MoveMode.KeepAnchor)
                self.text_input.setTextCursor(cursor)
                self.text_input.setText(self.get_text()[:self.max_characters])
        elif remaining <= self.warning_threshold:
            # Warning state
            self.char_counter_label.setStyleSheet(f"color: {COLOR_WARNING};")
        else:
            # Normal state
            self.char_counter_label.setStyleSheet(f"color: {COLOR_PRIMARY_TEXT};")
        
        # Start animation if near limit
        if remaining <= self.warning_threshold:
            self.start_counter_animation()

    def start_counter_animation(self):
        """Start the character counter animation"""
        # Make the counter bold and pulsing
        self.char_counter_label.setStyleSheet(
            f"color: {COLOR_WARNING}; font-weight: bold;"
        )
        
        # Reset after a short delay
        self.counter_animation_timer.start(500)

    def reset_counter_color(self):
        """Reset the character counter color"""
        remaining = self.max_characters - self.character_count
        if remaining <= 0:
            self.char_counter_label.setStyleSheet(f"color: {COLOR_ERROR}; font-weight: bold;")
        elif remaining <= self.warning_threshold:
            self.char_counter_label.setStyleSheet(f"color: {COLOR_WARNING};")
        else:
            self.char_counter_label.setStyleSheet(f"color: {COLOR_PRIMARY_TEXT};")

    def get_text(self):
        """Get the text from the input area"""
        return self.text_input.toPlainText().strip()

    def set_text(self, text):
        """Set the text in the input area"""
        self.text_input.setPlainText(text)
        self.character_count = len(text)
        self.update_character_counter()

    def clear_text(self):
        """Clear the text input area"""
        self.text_input.clear()
        self.character_count = 0
        self.update_character_counter()

    def set_placeholder_text(self, text):
        """Set placeholder text for the input area"""
        self.text_input.setPlaceholderText(text)

    def set_max_characters(self, max_chars):
        """Set the maximum number of characters allowed"""
        self.max_characters = max_chars
        self.update_character_counter()

    def focus_input(self):
        """Set focus to the text input area"""
        self.text_input.setFocus()
        cursor = self.text_input.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.text_input.setTextCursor(cursor)
        
    def resizeEvent(self, event):
        """Handle resize events for responsive design"""
        super().resizeEvent(event)
        # Adjust text input height based on widget size
        if hasattr(self, 'text_input'):
            # Set maximum height based on widget height
            max_height = max(80, self.height() // 3)
            self.text_input.setMaximumHeight(max_height)


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication, QVBoxLayout, QPushButton, QWidget
    
    app = QApplication(sys.argv)
    
    # Create test widget
    widget = QWidget()
    layout = QVBoxLayout(widget)
    
    # Create confession input
    confession_input = ConfessionInput()
    layout.addWidget(confession_input)
    
    # Create a button to get text
    button = QPushButton("Get Text")
    button.clicked.connect(lambda: print(confession_input.get_text()))
    layout.addWidget(button)
    
    widget.show()
    
    sys.exit(app.exec())