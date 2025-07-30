#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Animation Utilities for Beichtsthul Modern
Provides helper functions for creating and managing animations in the PyQt6 application.
"""

from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QSequentialAnimationGroup
from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import QEasingCurve


class AnimationManager:
    """Manages animations for the application"""

    def __init__(self):
        self.animations = []

    def create_property_animation(self, target, property_name, duration, easing_curve=QEasingCurve.Type.OutCubic):
        """
        Creates a property animation for a widget
        
        Args:
            target: The widget to animate
            property_name: The property to animate (e.g., b"geometry", b"opacity")
            duration: Animation duration in milliseconds
            easing_curve: The easing curve to use
            
        Returns:
            QPropertyAnimation: The created animation
        """
        animation = QPropertyAnimation(target, property_name)
        animation.setDuration(duration)
        animation.setEasingCurve(easing_curve)
        self.animations.append(animation)
        return animation

    def create_parallel_animation(self, animations):
        """
        Creates a parallel animation group
        
        Args:
            animations: List of animations to run in parallel
            
        Returns:
            QParallelAnimationGroup: The created animation group
        """
        group = QParallelAnimationGroup()
        for animation in animations:
            group.addAnimation(animation)
        self.animations.append(group)
        return group

    def create_sequential_animation(self, animations):
        """
        Creates a sequential animation group
        
        Args:
            animations: List of animations to run sequentially
            
        Returns:
            QSequentialAnimationGroup: The created animation group
        """
        group = QSequentialAnimationGroup()
        for animation in animations:
            group.addAnimation(animation)
        self.animations.append(group)
        return group

    def stop_all_animations(self):
        """Stops all running animations"""
        for animation in self.animations:
            if animation.state() == QPropertyAnimation.State.Running:
                animation.stop()


def create_fade_animation(widget, duration, start_value=0.0, end_value=1.0, easing_curve=QEasingCurve.Type.OutCubic):
    """
    Creates a fade animation for a widget
    
    Args:
        widget: The widget to fade
        duration: Animation duration in milliseconds
        start_value: Starting opacity (0.0 = transparent, 1.0 = opaque)
        end_value: Ending opacity (0.0 = transparent, 1.0 = opaque)
        easing_curve: The easing curve to use
        
    Returns:
        QPropertyAnimation: The fade animation
    """
    animation = QPropertyAnimation(widget, b"windowOpacity")
    animation.setDuration(duration)
    animation.setStartValue(start_value)
    animation.setEndValue(end_value)
    animation.setEasingCurve(easing_curve)
    return animation


def create_geometry_animation(widget, duration, start_geometry, end_geometry, easing_curve=QEasingCurve.Type.OutBack):
    """
    Creates a geometry animation for a widget
    
    Args:
        widget: The widget to animate
        duration: Animation duration in milliseconds
        start_geometry: Starting geometry (QRect)
        end_geometry: Ending geometry (QRect)
        easing_curve: The easing curve to use
        
    Returns:
        QPropertyAnimation: The geometry animation
    """
    animation = QPropertyAnimation(widget, b"geometry")
    animation.setDuration(duration)
    animation.setStartValue(start_geometry)
    animation.setEndValue(end_geometry)
    animation.setEasingCurve(easing_curve)
    return animation


def create_color_animation(widget, duration, start_color, end_color):
    """
    Creates a color animation for a widget
    
    Args:
        widget: The widget to animate
        duration: Animation duration in milliseconds
        start_color: Starting color (QColor)
        end_color: Ending color (QColor)
        
    Returns:
        QPropertyAnimation: The color animation
    """
    # This is a placeholder implementation - color animations require more complex setup
    # with custom properties and QPropertyAnimation
    pass


def create_scale_animation(widget, duration, start_scale, end_scale):
    """
    Creates a scale animation for a widget
    
    Args:
        widget: The widget to animate
        duration: Animation duration in milliseconds
        start_scale: Starting scale factor (float)
        end_scale: Ending scale factor (float)
        
    Returns:
        QPropertyAnimation: The scale animation
    """
    # This is a placeholder implementation - scale animations require more complex setup
    # with QGraphicsEffect or custom properties
    pass