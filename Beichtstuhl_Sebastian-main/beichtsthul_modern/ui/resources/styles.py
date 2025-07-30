#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
UI Styles for Beichtsthul Modern
Contains all stylesheet definitions for the PyQt6 application with cyberpunk styling.
"""

from core.constants import *
from design_tokens.design_tokens import ColorTokens, FontTokens, SpacingTokens, RadiusTokens, DurationTokens


def get_main_window_style():
    """Returns the stylesheet for the main window with cyberpunk styling"""
    return f"""
        QMainWindow {{
            background-color: {ColorTokens.BG_BASE.value};
            font-family: "{FontTokens.BODY_FAMILY.value}";
        }}
        
        QMainWindow::title {{
            color: {ColorTokens.TEXT_PRIMARY.value};
            font-family: "{FontTokens.HEADLINE_FAMILY.value}";
            font-size: {FontTokens.HEADLINE_SIZE_H1.value}px;
            font-weight: {FontTokens.HEADLINE_WEIGHT_BOLD.value};
        }}
    """


def get_button_style():
    """Returns the base stylesheet for buttons with cyberpunk neon styling"""
    return f"""
        QPushButton {{
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,
                stop: 0 {ColorTokens.ACCENT_PRIMARY.value}, stop: 1 {ColorTokens.ACCENT_SECONDARY.value});
            color: {ColorTokens.BG_BASE.value};
            border: none;
            border-radius: {RadiusTokens.BUTTON.value}px;
            padding: {SpacingTokens.BASE.value}px {SpacingTokens.COMPONENT.value}px;
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
        
        QPushButton:focus {{
            border: 3px solid {ColorTokens.ACCENT_PRIMARY.value};
            outline: 2px solid {ColorTokens.ACCENT_SECONDARY.value};
            outline-offset: 2px;
        }}
        
        QPushButton:disabled {{
            background: {ColorTokens.SEMANTIC_DISABLED.value};
            color: {ColorTokens.TEXT_SECONDARY.value};
        }}
    """


def get_primary_button_style():
    """Returns the stylesheet for primary action buttons with enhanced cyberpunk styling"""
    return f"""
        QPushButton {{
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                stop: 0 {ColorTokens.ACCENT_PRIMARY.value}, stop: 1 {ColorTokens.ACCENT_SECONDARY.value});
            color: {ColorTokens.BG_BASE.value};
            border: none;
            border-radius: {RadiusTokens.BUTTON.value}px;
            padding: {SpacingTokens.BASE.value}px {SpacingTokens.COMPONENT.value}px;
            font-family: "{FontTokens.BODY_FAMILY.value}";
            font-size: {FontTokens.BODY_SIZE_BODY.value}px;
            font-weight: {FontTokens.BODY_WEIGHT_BOLD.value};
            min-height: 40px;
            min-width: 120px;
        }}
        
        QPushButton:hover {{
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                stop: 0 {ColorTokens.ACCENT_SECONDARY.value}, stop: 1 {ColorTokens.ACCENT_PRIMARY.value});
            border: 1px solid {ColorTokens.ACCENT_PRIMARY.value};
            box-shadow: 0 0 15px {ColorTokens.ACCENT_PRIMARY.value};
        }}
        
        QPushButton:pressed {{
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, 
                stop: 0 {ColorTokens.ACCENT_WARN.value}, stop: 1 {ColorTokens.ACCENT_ERROR.value});
            transform: scale(0.96);
            box-shadow: 0 0 5px {ColorTokens.ACCENT_WARN.value};
        }}
        
        QPushButton:focus {{
            border: 2px solid {ColorTokens.ACCENT_PRIMARY.value};
            outline: none;
        }}
        
        QPushButton:disabled {{
            background: {ColorTokens.SEMANTIC_DISABLED.value};
            color: {ColorTokens.TEXT_SECONDARY.value};
        }}
    """


def get_secondary_button_style():
    """Returns the stylesheet for secondary action buttons with cyberpunk styling"""
    return f"""
        QPushButton {{
            background-color: {ColorTokens.BG_PANEL.value};
            color: {ColorTokens.TEXT_PRIMARY.value};
            border: 2px solid {ColorTokens.ACCENT_SECONDARY.value};
            border-radius: {RadiusTokens.BUTTON.value}px;
            padding: {SpacingTokens.BASE.value}px {SpacingTokens.COMPONENT.value}px;
            font-family: "{FontTokens.BODY_FAMILY.value}";
            font-size: {FontTokens.BODY_SIZE_BODY.value}px;
            min-height: 30px;
        }}
        
        QPushButton:hover {{
            background-color: rgba(255, 0, 120, 0.1);
            border: 2px solid {ColorTokens.ACCENT_PRIMARY.value};
            box-shadow: 0 0 10px {ColorTokens.ACCENT_SECONDARY.value};
        }}
        
        QPushButton:pressed {{
            background-color: rgba(0, 234, 255, 0.2);
            border: 2px solid {ColorTokens.ACCENT_WARN.value};
            transform: scale(0.96);
        }}
        
        QPushButton:focus {{
            border: 2px solid {ColorTokens.ACCENT_PRIMARY.value};
            outline: none;
        }}
        
        QPushButton:disabled {{
            background-color: {ColorTokens.SEMANTIC_DISABLED.value};
            border: 2px solid {ColorTokens.SEMANTIC_DISABLED.value};
            color: {ColorTokens.TEXT_SECONDARY.value};
        }}
    """


def get_text_input_style():
    """Returns the stylesheet for text input fields with cyberpunk glassmorphism effect"""
    return f"""
        QTextEdit, QLineEdit {{
            background-color: rgba(20, 24, 38, 0.7);
            color: {ColorTokens.TEXT_PRIMARY.value};
            border: 2px solid {ColorTokens.BG_PANEL.value};
            border-radius: {RadiusTokens.BUTTON.value}px;
            padding: {SpacingTokens.BASE.value}px;
            font-family: "{FontTokens.MONO_FAMILY.value}";
            font-size: {FontTokens.MONO_SIZE_DEFAULT.value}px;
            selection-background-color: {ColorTokens.ACCENT_PRIMARY.value};
            selection-color: {ColorTokens.BG_BASE.value};
        }}
        
        QTextEdit:focus, QLineEdit:focus {{
            border: 2px solid {ColorTokens.ACCENT_PRIMARY.value};
            outline: none;
            box-shadow: 0 0 10px {ColorTokens.ACCENT_PRIMARY.value};
        }}
        
        QTextEdit:disabled, QLineEdit:disabled {{
            background-color: {ColorTokens.SEMANTIC_DISABLED.value};
            color: {ColorTokens.TEXT_SECONDARY.value};
            border: 2px solid {ColorTokens.SEMANTIC_DISABLED.value};
        }}
    """


def get_label_style():
    """Returns the stylesheet for labels with cyberpunk styling"""
    return f"""
        QLabel {{
            color: {ColorTokens.TEXT_PRIMARY.value};
            font-family: "{FontTokens.BODY_FAMILY.value}";
            font-size: {FontTokens.BODY_SIZE_BODY.value}px;
        }}
        
        QLabel#header {{
            color: {ColorTokens.ACCENT_PRIMARY.value};
            font-family: "{FontTokens.HEADLINE_FAMILY.value}";
            font-size: {FontTokens.HEADLINE_SIZE_H2.value}px;
            font-weight: {FontTokens.HEADLINE_WEIGHT_BOLD.value};
        }}
        
        QLabel#title {{
            color: {ColorTokens.ACCENT_WARN.value};
            font-family: "{FontTokens.HEADLINE_FAMILY.value}";
            font-size: {FontTokens.HEADLINE_SIZE_H1.value}px;
            font-weight: {FontTokens.HEADLINE_WEIGHT_BOLD.value};
        }}
        
        QLabel#caption {{
            color: {ColorTokens.TEXT_SECONDARY.value};
            font-family: "{FontTokens.BODY_FAMILY.value}";
            font-size: {FontTokens.BODY_SIZE_CAPTION.value}px;
        }}
        
        QLabel#karmaLabel {{
            color: {ColorTokens.TEXT_PRIMARY.value};
            font-family: "{FontTokens.BODY_FAMILY.value}";
            font-size: {FontTokens.BODY_SIZE_BODY.value}px;
            font-weight: {FontTokens.BODY_WEIGHT_BOLD.value};
        }}
        
        QLabel#karmaValue {{
            color: {ColorTokens.ACCENT_ERROR.value};
            font-family: "{FontTokens.MONO_FAMILY.value}";
            font-size: {FontTokens.HEADLINE_SIZE_H2.value}px;
            font-weight: {FontTokens.HEADLINE_WEIGHT_BOLD.value};
        }}
    """


def get_card_style():
    """Returns the stylesheet for card components with glassmorphism effect"""
    return f"""
        QWidget#card {{
            background-color: rgba(20, 24, 38, 0.7);
            border-radius: {RadiusTokens.CARD.value}px;
            padding: {SpacingTokens.COMPONENT.value}px;
            border: 1px solid {ColorTokens.BG_PANEL.value};
            backdrop-filter: blur(6px);
        }}
        
        QWidget#card:hover {{
            border: 1px solid {ColorTokens.ACCENT_PRIMARY.value};
            box-shadow: 0 0 15px rgba(0, 234, 255, 0.3);
        }}
    """


def get_karma_display_style():
    """Returns the stylesheet for karma display with cyberpunk styling"""
    return f"""
        QWidget#karmaDisplay {{
            background-color: rgba(20, 24, 38, 0.7);
            border-radius: {RadiusTokens.CARD.value}px;
            border: 1px solid {ColorTokens.BG_PANEL.value};
            padding: {SpacingTokens.ELEMENT.value}px;
            backdrop-filter: blur(6px);
        }}
        
        QWidget#karmaDisplay:hover {{
            border: 1px solid {ColorTokens.ACCENT_PRIMARY.value};
            box-shadow: 0 0 15px rgba(0, 234, 255, 0.3);
        }}
        
        QLabel#karmaLabel {{
            color: {ColorTokens.TEXT_PRIMARY.value};
            font-family: "{FontTokens.BODY_FAMILY.value}";
            font-size: {FontTokens.BODY_SIZE_BODY.value}px;
            font-weight: {FontTokens.BODY_WEIGHT_BOLD.value};
        }}
        
        QLabel#karmaValue {{
            color: {ColorTokens.ACCENT_ERROR.value};
            font-family: "{FontTokens.MONO_FAMILY.value}";
            font-size: {FontTokens.HEADLINE_SIZE_H2.value}px;
            font-weight: {FontTokens.HEADLINE_WEIGHT_BOLD.value};
        }}
    """


def get_monk_visualizer_style():
    """Returns the stylesheet for monk visualizer with cyberpunk styling"""
    return f"""
        QWidget#monkVisualizer {{
            background-color: rgba(20, 24, 38, 0.7);
            border-radius: {RadiusTokens.CARD.value}px;
            border: 1px solid {ColorTokens.BG_PANEL.value};
            backdrop-filter: blur(6px);
        }}
        
        QWidget#monkVisualizer:hover {{
            border: 1px solid {ColorTokens.ACCENT_PRIMARY.value};
            box-shadow: 0 0 15px rgba(0, 234, 255, 0.3);
        }}
    """


def get_status_bar_style():
    """Returns the stylesheet for status bar with cyberpunk styling"""
    return f"""
        QStatusBar {{
            background-color: {ColorTokens.BG_PANEL.value};
            color: {ColorTokens.TEXT_SECONDARY.value};
            border-top: 1px solid {ColorTokens.BG_BASE.value};
            font-family: "{FontTokens.BODY_FAMILY.value}";
            font-size: {FontTokens.BODY_SIZE_SMALL.value}px;
            min-height: 26px;
        }}
        
        QStatusBar::item {{
            border: none;
        }}
    """


def get_scroll_area_style():
    """Returns the stylesheet for scroll areas with cyberpunk styling"""
    return f"""
        QScrollArea {{
            border: none;
            background-color: transparent;
        }}
        
        QScrollArea > QWidget > QWidget {{
            background-color: {ColorTokens.BG_BASE.value};
        }}
        
        QScrollBar:vertical {{
            background-color: {ColorTokens.BG_PANEL.value};
            width: 15px;
            border-radius: 4px;
        }}
        
        QScrollBar::handle:vertical {{
            background-color: {ColorTokens.BG_BASE.value};
            border: 1px solid {ColorTokens.ACCENT_SECONDARY.value};
            border-radius: 4px;
            min-height: 20px;
        }}
        
        QScrollBar::handle:vertical:hover {{
            background-color: {ColorTokens.ACCENT_PRIMARY.value};
            border: 1px solid {ColorTokens.ACCENT_PRIMARY.value};
        }}
    """


def get_progress_bar_style():
    """Returns the stylesheet for progress bars with cyberpunk neon styling"""
    return f"""
        QProgressBar {{
            border: 2px solid {ColorTokens.BG_PANEL.value};
            border-radius: {RadiusTokens.BUTTON.value}px;
            background-color: {ColorTokens.BG_BASE.value};
            text-align: center;
            color: {ColorTokens.TEXT_PRIMARY.value};
            font-family: "{FontTokens.BODY_FAMILY.value}";
            font-size: {FontTokens.BODY_SIZE_SMALL.value}px;
        }}
        
        QProgressBar::chunk {{
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                stop: 0 {ColorTokens.ACCENT_PRIMARY.value}, stop: 1 {ColorTokens.ACCENT_SECONDARY.value});
            border-radius: {RadiusTokens.BUTTON.value - 2}px;
        }}
        
        QProgressBar::chunk:hover {{
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 0, 
                stop: 0 {ColorTokens.ACCENT_SECONDARY.value}, stop: 1 {ColorTokens.ACCENT_PRIMARY.value});
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
        get_scroll_area_style() +
        get_progress_bar_style()
    )