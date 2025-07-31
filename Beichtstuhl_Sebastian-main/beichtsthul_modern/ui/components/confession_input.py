#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Confession Input for Beichtsthul Modern
A custom text input area for confessions with cyberpunk styling and animations.
Features a glass panel with neon border and focus states.
"""

from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QTextEdit
from PyQt6.QtCore import pyqtSignal, QTimer, pyqtSlot
from PyQt6.QtGui import QTextCursor

from .neon_line_edit import NeonLineEdit

class ConfessionInput(QWidget):
    """A custom widget for confessions with glass panel and neon effects."""

    confession_submitted = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.character_count = 0
        self.max_characters = 500
        self.warning_threshold = 50
        self.init_ui()
        self.setup_animations()

    def init_ui(self):
        """Initialize the user interface."""
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(10)

        self.header_label = QLabel("Deine Beichte:")
        self.header_label.setObjectName("header")
        # Bind to headline typography via QSS selector QLabel[type="header"]
        self.header_label.setProperty("type", "header")
        
        # Create a custom text edit with glass panel effect
        self.text_input = QTextEdit()
        self.text_input.setPlaceholderText("Tippe hier deine Sünde ein...")
        self.text_input.textChanged.connect(self.on_text_changed)
        # QTextEdit doesn't have returnPressed signal, using textChanged instead

        layout.addWidget(self.header_label)
        layout.addWidget(self.text_input)

    def submit_confession(self):
        """Emits the confession signal when the user presses Enter."""
        confession_text = self.get_text()
        if confession_text:
            self.confession_submitted.emit(confession_text)

    def get_text(self):
        """Get the text from the input area."""
        return self.text_input.toPlainText().strip()

    def clear_text(self):
        """Clear the text input area."""
        self.text_input.clear()
        self.character_count = 0

    def focus_input(self):
        """Set focus to the text input area."""
        self.text_input.setFocus()
        cursor = self.text_input.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.End)
        self.text_input.setTextCursor(cursor)

    def setup_animations(self):
        """Setup animations for the input area"""
        # Character counter animation timer
        self.counter_animation_timer = QTimer(self)
        self.counter_animation_timer.setSingleShot(True)
        self.counter_animation_timer.timeout.connect(self.reset_counter_color)

    def on_text_changed(self):
        """Handle text change event"""
        text = self.get_text()
        self.character_count = len(text)
        
        # Limit text to max characters
        if self.character_count > self.max_characters:
            cursor = self.text_input.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.End)
            cursor.setPosition(len(text[:self.max_characters]), QTextCursor.MoveMode.KeepAnchor)
            self.text_input.setTextCursor(cursor)
            self.text_input.setPlainText(text[:self.max_characters])
            self.character_count = self.max_characters

    def reset_counter_color(self):
        """Reset the character counter color"""
        pass  # Placeholder method

    def set_max_characters(self, max_chars):
        """Set the maximum number of characters allowed"""
        self.max_characters = max_chars

    def set_placeholder_text(self, text):
        """Set placeholder text for the input area"""
        self.text_input.setPlaceholderText(text)

    def resizeEvent(self, event):
        """Handle resize events for responsive design"""
        super().resizeEvent(event)
        # Adjust text input height based on widget size
        if hasattr(self, 'text_input'):
            # Set maximum height based on widget height
            max_height = max(120, self.height() // 3)
            self.text_input.setMaximumHeight(max_height)
    
    
    class GlassTextEdit(QTextEdit):
        """Custom QTextEdit with glass panel effect and neon border"""
        
        def __init__(self, parent=None):
            super().__init__(parent)
            self.setObjectName("glassTextEdit")
            self.setAcceptRichText(False)  # Only plain text
            self.setup_styles()
            
        def setup_styles(self):
            """Setup initial styles"""
            self.setStyleSheet("""
                QTextEdit {
                    background: rgba(255, 255, 255, 0.05);
                    border: 2px solid #00E5FF;
                    border-radius: 12px;
                    padding: 10px;
                    color: #EDEFFF;
                    font-family: "Inter";
                    font-size: 14px;
                    selection-background-color: #00E5FF;
                    selection-color: #0E1222;
                }
                
                QTextEdit:focus {
                    border: 2px solid #00E5FF;
                    box-shadow: 0 0 8px #00E5FF;
                }
            """)
            
        def keyPressEvent(self, event):
            """Handle key press events"""
            if event.key() in (Qt.Key.Key_Return, Qt.Key.Key_Enter):
                if event.modifiers() == Qt.KeyboardModifier.ControlModifier:
                    # Ctrl+Enter submits the confession
                    self.returnPressed.emit()
                    return
            super().keyPressEvent(event)
            
        def focusInEvent(self, event):
            """Handle focus in event for glow effect"""
            super().focusInEvent(event)
            self.update_glow_effect(True)
            
        def focusOutEvent(self, event):
            """Handle focus out event for glow effect"""
            super().focusOutEvent(event)
            self.update_glow_effect(False)
            
        def update_glow_effect(self, has_focus):
            """Update the glow effect based on focus state"""
            if has_focus:
                self.setStyleSheet("""
                    QTextEdit {
                        background: rgba(255, 255, 255, 0.05);
                        border: 2px solid #00E5FF;
                        border-radius: 12px;
                        padding: 10px;
                        color: #EDEFFF;
                        font-family: "Inter";
                        font-size: 14px;
                        selection-background-color: #00E5FF;
                        selection-color: #0E1222;
                    }
                    
                    QTextEdit:focus {
                        border: 2px solid #00E5FF;
                        box-shadow: 0 0 8px #00E5FF;
                    }
                """)
            else:
                self.setStyleSheet("""
                    QTextEdit {
                        background: rgba(255, 255, 255, 0.05);
                        border: 2px solid #00E5FF;
                        border-radius: 12px;
                        padding: 10px;
                        color: #EDEFFF;
                        font-family: "Inter";
                        font-size: 14px;
                        selection-background-color: #00E5FF;
                        selection-color: #0E1222;
                    }
                    
                    QTextEdit:focus {
                        border: 2px solid #00E5FF;
                        box-shadow: 0 0 8px #00E5FF;
                    }
                """)
    
    
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