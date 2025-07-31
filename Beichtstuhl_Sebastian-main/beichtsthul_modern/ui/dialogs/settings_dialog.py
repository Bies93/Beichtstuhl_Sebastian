#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Settings Dialog for Beichtsthul Modern
A dialog for configuring application settings with cyberpunk styling.
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QCheckBox, 
    QPushButton, QGroupBox, QComboBox, QWidget
)
from PyQt6.QtCore import Qt, pyqtSignal
from PyQt6.QtGui import QKeySequence, QShortcut

from design_tokens.design_tokens import ColorTokens, FontTokens
from utils.sound_manager import sound_manager


class SettingsDialog(QDialog):
    """Settings dialog with cyberpunk styling"""
    
    # Signal emitted when settings are changed
    settingsChanged = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Einstellungen")
        self.setModal(True)
        self.setMinimumWidth(400)
        
        # Setup UI
        self.init_ui()
        
        # Load current settings
        self.load_settings()
        
        # Connect signals
        self.connect_signals()
        
        # Apply styles
        self.apply_styles()
        
    def init_ui(self):
        """Initialize the user interface"""
        layout = QVBoxLayout(self)
        layout.setSpacing(15)
        
        # Create sound settings group
        self.create_sound_settings_group(layout)
        
        # Create theme settings group
        self.create_theme_settings_group(layout)
        
        # Create keyboard shortcuts group
        self.create_shortcuts_group(layout)
        
        # Create buttons
        self.create_buttons(layout)
        
        # Set accessible names and descriptions
        self.set_accessible_info()
    def create_sound_settings_group(self, parent_layout):
        """Create sound settings group"""
        sound_group = QGroupBox("Audio-Einstellungen")
        # Make the group box title use section typography
        sound_group.setProperty("type", "section")
        sound_layout = QVBoxLayout(sound_group)
        
        # Volume slider
        volume_layout = QHBoxLayout()
        volume_label = QLabel("Lautstärke:")
        # Make this a caption label
        volume_label.setProperty("type", "caption")
        self.volume_slider = QSlider(Qt.Orientation.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(100)
        self.volume_value_label = QLabel("100%")
        # Make this a caption label
        self.volume_value_label.setProperty("type", "caption")
        
        volume_layout.addWidget(volume_label)
        volume_layout.addWidget(self.volume_slider)
        volume_layout.addWidget(self.volume_value_label)
        sound_layout.addLayout(volume_layout)
        
        # Mute checkbox
        self.mute_checkbox = QCheckBox("Stummschalten")
        sound_layout.addWidget(self.mute_checkbox)
        
        parent_layout.addWidget(sound_group)
        
    def create_theme_settings_group(self, parent_layout):
        """Create theme settings group"""
        theme_group = QGroupBox("Design-Einstellungen")
        # Make the group box title use section typography
        theme_group.setProperty("type", "section")
        theme_layout = QVBoxLayout(theme_group)
        
        # Theme selector
        theme_label = QLabel("Design:")
        # Make this a caption label
        theme_label.setProperty("type", "caption")
        theme_layout.addWidget(theme_label)
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Cyberpunk", "Cyberlight"])
        theme_layout.addWidget(self.theme_combo)
        
        parent_layout.addWidget(theme_group)
        
    def create_shortcuts_group(self, parent_layout):
        """Create keyboard shortcuts group"""
        shortcuts_group = QGroupBox("Tastenkürzel")
        shortcuts_layout = QVBoxLayout(shortcuts_group)
        
        # Mute shortcut
        mute_shortcut_layout = QHBoxLayout()
        mute_shortcut_layout.addWidget(QLabel("Stummschalten:"))
        mute_shortcut_layout.addWidget(QLabel("Strg+M"))
        mute_shortcut_layout.addStretch()
        shortcuts_layout.addLayout(mute_shortcut_layout)
        
        parent_layout.addWidget(shortcuts_group)
        
    def create_buttons(self, parent_layout):
        """Create dialog buttons"""
        buttons_layout = QHBoxLayout()
        buttons_layout.addStretch()
        
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Abbrechen")
        
        buttons_layout.addWidget(self.ok_button)
        buttons_layout.addWidget(self.cancel_button)
        
        parent_layout.addLayout(buttons_layout)
        
    def connect_signals(self):
        """Connect signals and slots"""
        # Volume slider
        self.volume_slider.valueChanged.connect(self.on_volume_changed)
        
        # Mute checkbox
        self.mute_checkbox.toggled.connect(self.on_mute_toggled)
        
        # Sound manager mute signal
        sound_manager.muteChanged.connect(self.on_sound_manager_mute_changed)
        
        # Buttons
        self.ok_button.clicked.connect(self.accept)
        self.cancel_button.clicked.connect(self.reject)
        
        # Master mute shortcut (Ctrl+M)
        self.mute_shortcut = QShortcut(QKeySequence("Ctrl+M"), self)
        self.mute_shortcut.activated.connect(self.toggle_mute)
        
    def set_accessible_info(self):
        """Sets accessible names and descriptions for widgets."""
        # Sound settings
        self.volume_slider.setAccessibleName("Lautstärke")
        self.volume_slider.setAccessibleDescription("Stellen Sie die Lautstärke der Anwendung ein.")
        self.mute_checkbox.setAccessibleName("Stummschalten")
        self.mute_checkbox.setAccessibleDescription("Schaltet die Anwendung stumm.")
        
        # Theme settings
        self.theme_combo.setAccessibleName("Design")
        self.theme_combo.setAccessibleDescription("Wählen Sie das Design der Anwendung.")
        
        # Buttons
        self.ok_button.setAccessibleName("OK")
        self.ok_button.setAccessibleDescription("Speichert die Einstellungen und schließt das Fenster.")
        self.cancel_button.setAccessibleName("Abbrechen")
        self.cancel_button.setAccessibleDescription("Verwirft die Änderungen und schließt das Fenster.")
    def load_settings(self):
        """Load current settings"""
        # Load volume
        volume = int(sound_manager.get_volume() * 100)
        self.volume_slider.setValue(volume)
        self.volume_value_label.setText(f"{volume}%")
        
        # Load mute state
        self.mute_checkbox.setChecked(sound_manager.is_muted())
        
    def apply_styles(self):
        """Apply cyberpunk styling to the dialog"""
        self.setStyleSheet(f"""
            QDialog {{
                background-color: {ColorTokens.BG_BASE.value};
                color: {ColorTokens.TEXT_PRIMARY.value};
                font-family: "{FontTokens.BODY_FAMILY.value}";
            }}
            
            QGroupBox {{
                background-color: {ColorTokens.BG_PANEL.value};
                border: 1px solid {ColorTokens.ACCENT_SECONDARY.value};
                border-radius: {8}px;
                margin-top: 1ex;
                padding-top: 10px;
                font-family: "{FontTokens.HEADLINE_FAMILY.value}";
                font-size: {FontTokens.HEADLINE_SIZE_H4.value}px;
                color: {ColorTokens.ACCENT_PRIMARY.value};
            }}
            
            QGroupBox::title {{
                subline-offset: -10px;
                padding: 0 5px;
            }}
            
            QLabel {{
                color: {ColorTokens.TEXT_PRIMARY.value};
                font-family: "{FontTokens.BODY_FAMILY.value}";
                font-size: {FontTokens.BODY_SIZE_BODY.value}px;
            }}
            
            QSlider::groove:horizontal {{
                border: 1px solid {ColorTokens.BG_PANEL.value};
                height: 8px;
                background: {ColorTokens.BG_PANEL.value};
                border-radius: 4px;
            }}
            
            QSlider::handle:horizontal {{
                background: {ColorTokens.ACCENT_PRIMARY.value};
                border: 1px solid {ColorTokens.ACCENT_SECONDARY.value};
                width: 18px;
                margin: -5px 0;
                border-radius: 9px;
            }}
            
            QSlider::sub-page:horizontal {{
                background: {ColorTokens.ACCENT_PRIMARY.value};
                border-radius: 4px;
            }}
            
            QCheckBox {{
                color: {ColorTokens.TEXT_PRIMARY.value};
                font-family: "{FontTokens.BODY_FAMILY.value}";
                font-size: {FontTokens.BODY_SIZE_BODY.value}px;
                spacing: 5px;
            }}
            
            QCheckBox::indicator {{
                width: 18px;
                height: 18px;
                border: 2px solid {ColorTokens.ACCENT_SECONDARY.value};
                border-radius: 3px;
            }}
            
            QCheckBox::indicator:checked {{
                background-color: {ColorTokens.ACCENT_PRIMARY.value};
            }}
            
            QPushButton {{
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                    stop: 0 {ColorTokens.ACCENT_PRIMARY.value}, stop: 1 {ColorTokens.ACCENT_SECONDARY.value});
                color: {ColorTokens.BG_BASE.value};
                border: none;
                border-radius: {4}px;
                padding: {8}px {16}px;
                font-family: "{FontTokens.BODY_FAMILY.value}";
                font-size: {FontTokens.BODY_SIZE_BODY.value}px;
                font-weight: {FontTokens.BODY_WEIGHT_BOLD.value};
                min-height: 30px;
            }}
            
            QPushButton:hover {{
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                    stop: 0 {ColorTokens.ACCENT_SECONDARY.value}, stop: 1 {ColorTokens.ACCENT_PRIMARY.value});
                border: 1px solid {ColorTokens.ACCENT_PRIMARY.value};
                box-shadow: 0 0 10px {ColorTokens.ACCENT_PRIMARY.value};
            }}
            
            QPushButton:pressed {{
                background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                    stop: 0 {ColorTokens.ACCENT_WARN.value}, stop: 1 {ColorTokens.ACCENT_ERROR.value});
                transform: scale(0.96);
            }}
            
            QComboBox {{
                background-color: {ColorTokens.BG_PANEL.value};
                color: {ColorTokens.TEXT_PRIMARY.value};
                border: 2px solid {ColorTokens.BG_PANEL.value};
                border-radius: {4}px;
                padding: {4}px;
                font-family: "{FontTokens.BODY_FAMILY.value}";
                font-size: {FontTokens.BODY_SIZE_BODY.value}px;
            }}
            
            QComboBox:hover {{
                border: 2px solid {ColorTokens.ACCENT_SECONDARY.value};
            }}
            
            QComboBox::drop-down {{
                border: none;
            }}
            
            QComboBox::down-arrow {{
                image: none;
                border-left: 5px solid transparent;
                border-right: 5px solid transparent;
                border-top: 5px solid {ColorTokens.ACCENT_PRIMARY.value};
                width: 0;
                height: 0;
                margin-right: 5px;
            }}
        """)
        
    def on_volume_changed(self, value):
        """Handle volume slider change"""
        self.volume_value_label.setText(f"{value}%")
        volume = value / 100.0
        sound_manager.set_volume(volume)
        self.settingsChanged.emit()
        
    def on_mute_toggled(self, checked):
        """Handle mute checkbox toggle"""
        sound_manager.set_mute(checked)
        self.settingsChanged.emit()
        
    def on_sound_manager_mute_changed(self, muted):
        """Handle sound manager mute state change"""
        self.mute_checkbox.setChecked(muted)
        
    def toggle_mute(self):
        """Toggle mute state (called by shortcut)"""
        sound_manager.toggle_mute()
        self.mute_checkbox.setChecked(sound_manager.is_muted())
        self.settingsChanged.emit()
        
    def accept(self):
        """Handle OK button click"""
        # Save settings if needed
        super().accept()