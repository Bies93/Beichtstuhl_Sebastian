#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UI Styles for Beichtsthul Modern
Contains all stylesheet definitions for the PyQt6 application.
"""

from core.constants import *


def get_main_window_style():
    """Returns the stylesheet for the main window"""
    return f"""
        QMainWindow {{
            background-color: {COLOR_PRIMARY_BG};
        }}
        
        QMainWindow::title {{
            color: {COLOR_PRIMARY_TEXT};
            font-size: {FONT_SIZE_TITLE}px;
            font-weight: bold;
        }}
    """


def get_button_style():
    """Returns the base stylesheet for buttons"""
    return f"""
        QPushButton {{
            background-color: {COLOR_PRIMARY_ACCENT};
            color: {COLOR_PRIMARY_BG};
            border: none;
            border-radius: {BORDER_RADIUS_BUTTON}px;
            padding: {SPACING_BASE}px {SPACING_COMPONENT}px;
            font-size: {FONT_SIZE_BUTTON}px;
            font-weight: bold;
            min-height: 30px;
        }}
        
        QPushButton:hover {{
            background-color: {COLOR_SECONDARY_ACCENT};
        }}
        
        QPushButton:pressed {{
            background-color: {COLOR_EMOTIONAL_ACCENT};
            padding: {SPACING_BASE-1}px {SPACING_COMPONENT-1}px;
        }}
        
        QPushButton:disabled {{
            background-color: {COLOR_DISABLED_TEXT};
        }}
    """


def get_primary_button_style():
    """Returns the stylesheet for primary action buttons"""
    return f"""
        QPushButton {{
            background-color: {COLOR_PRIMARY_ACCENT};
            color: {COLOR_PRIMARY_BG};
            border: none;
            border-radius: {BORDER_RADIUS_BUTTON}px;
            padding: {SPACING_BASE}px {SPACING_COMPONENT}px;
            font-size: {FONT_SIZE_BUTTON}px;
            font-weight: bold;
            min-height: 40px;
            min-width: 120px;
        }}
        
        QPushButton:hover {{
            background-color: {COLOR_SECONDARY_ACCENT};
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }}
        
        QPushButton:pressed {{
            background-color: {COLOR_EMOTIONAL_ACCENT};
            padding: {SPACING_BASE-1}px {SPACING_COMPONENT-1}px;
        }}
        
        QPushButton:disabled {{
            background-color: {COLOR_DISABLED_TEXT};
        }}
    """


def get_secondary_button_style():
    """Returns the stylesheet for secondary action buttons"""
    return f"""
        QPushButton {{
            background-color: {COLOR_SECONDARY_BG};
            color: {COLOR_PRIMARY_TEXT};
            border: 1px solid {COLOR_SECONDARY_ACCENT};
            border-radius: {BORDER_RADIUS_BUTTON}px;
            padding: {SPACING_BASE}px {SPACING_COMPONENT}px;
            font-size: {FONT_SIZE_BUTTON}px;
            min-height: 30px;
        }}
        
        QPushButton:hover {{
            background-color: {COLOR_SURFACE_BG};
            border: 1px solid {COLOR_PRIMARY_ACCENT};
        }}
        
        QPushButton:pressed {{
            background-color: {COLOR_SECONDARY_ACCENT};
            padding: {SPACING_BASE-1}px {SPACING_COMPONENT-1}px;
        }}
        
        QPushButton:disabled {{
            background-color: {COLOR_DISABLED_TEXT};
            border: 1px solid {COLOR_DISABLED_TEXT};
        }}
    """


def get_text_input_style():
    """Returns the stylesheet for text input fields"""
    return f"""
        QTextEdit, QLineEdit {{
            background-color: {COLOR_SECONDARY_BG};
            color: {COLOR_PRIMARY_TEXT};
            border: 2px solid {COLOR_SURFACE_BG};
            border-radius: {BORDER_RADIUS_BUTTON}px;
            padding: {SPACING_BASE}px;
            font-size: {FONT_SIZE_BODY}px;
            font-family: "{FONT_MONOSPACE}", "{FONT_SECONDARY}", "{FONT_PRIMARY}", "{FONT_FALLBACK}";
        }}
        
        QTextEdit:focus, QLineEdit:focus {{
            border: 2px solid {COLOR_PRIMARY_ACCENT};
            outline: none;
        }}
        
        QTextEdit:disabled, QLineEdit:disabled {{
            background-color: {COLOR_DISABLED_TEXT};
            color: {COLOR_SECONDARY_TEXT};
        }}
    """


def get_label_style():
    """Returns the stylesheet for labels"""
    return f"""
        QLabel {{
            color: {COLOR_PRIMARY_TEXT};
            font-size: {FONT_SIZE_BODY}px;
        }}
        
        QLabel#header {{
            color: {COLOR_PRIMARY_ACCENT};
            font-size: {FONT_SIZE_HEADER}px;
            font-weight: bold;
        }}
        
        QLabel#title {{
            color: {COLOR_EMOTIONAL_ACCENT};
            font-size: {FONT_SIZE_TITLE}px;
            font-weight: bold;
        }}
        
        QLabel#caption {{
            color: {COLOR_SECONDARY_TEXT};
            font-size: {FONT_SIZE_CAPTION}px;
        }}
    """


def get_card_style():
    """Returns the stylesheet for card components"""
    return f"""
        QWidget#card {{
            background-color: {COLOR_SECONDARY_BG};
            border-radius: {BORDER_RADIUS_CARD}px;
            padding: {SPACING_COMPONENT}px;
            border: 1px solid {COLOR_SURFACE_BG};
        }}
        
        QWidget#card:hover {{
            border: 1px solid {COLOR_PRIMARY_ACCENT};
        }}
    """


def get_karma_display_style():
    """Returns the stylesheet for karma display"""
    return f"""
        QWidget#karmaDisplay {{
            background-color: {COLOR_SECONDARY_BG};
            border-radius: {BORDER_RADIUS_CARD}px;
            border: 1px solid {COLOR_SURFACE_BG};
            padding: {SPACING_ELEMENT}px;
        }}
        
        QLabel#karmaLabel {{
            color: {COLOR_PRIMARY_TEXT};
            font-size: {FONT_SIZE_BODY}px;
            font-weight: bold;
        }}
        
        QLabel#karmaValue {{
            color: {COLOR_ERROR};
            font-size: {FONT_SIZE_HEADER}px;
            font-weight: bold;
        }}
    """


def get_monk_visualizer_style():
    """Returns the stylesheet for monk visualizer"""
    return f"""
        QWidget#monkVisualizer {{
            background-color: {COLOR_SECONDARY_BG};
            border-radius: {BORDER_RADIUS_CARD}px;
            border: 1px solid {COLOR_SURFACE_BG};
        }}
    """


def get_status_bar_style():
    """Returns the stylesheet for status bar"""
    return f"""
        QStatusBar {{
            background-color: {COLOR_SECONDARY_BG};
            color: {COLOR_SECONDARY_TEXT};
            border-top: 1px solid {COLOR_SURFACE_BG};
        }}
        
        QStatusBar::item {{
            border: none;
        }}
    """


def get_scroll_area_style():
    """Returns the stylesheet for scroll areas"""
    return f"""
        QScrollArea {{
            border: none;
            background-color: transparent;
        }}
        
        QScrollArea > QWidget > QWidget {{
            background-color: {COLOR_PRIMARY_BG};
        }}
        
        QScrollBar:vertical {{
            background-color: {COLOR_SECONDARY_BG};
            width: 15px;
            border-radius: 4px;
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {COLOR_SURFACE_BG};
            border-radius: 4px;
            min-height: 20px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {COLOR_PRIMARY_ACCENT};
        }}
    """


def get_all_styles():
    """Returns all styles combined"""
    return (
        get_main_window_style() +
        get_button_style() +
        get_primary_button_style() +
        get_secondary_button_style() +
        get_text_input_style() +
        get_label_style() +
        get_card_style() +
        get_karma_display_style() +
        get_monk_visualizer_style() +
        get_status_bar_style() +
        get_scroll_area_style()
    )