#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Transition Manager for Beichtsthul Modern
Manages smooth transitions between views with cyberpunk styling.
"""

from PyQt6.QtWidgets import QWidget, QStackedWidget, QGraphicsOpacityEffect
from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, QParallelAnimationGroup, QTimer
from PyQt6.QtGui import QPixmap, QPainter, QColor
from design_tokens.design_tokens import ColorTokens, DurationTokens
import random


class TransitionManager(QWidget):
    """Manages smooth transitions between views with cyberpunk effects"""

    def __init__(self, parent=None):
        super().__init__(parent)
        self._current_index = 0
        self._widgets = []
        self._is_transitioning = False
        
        # Setup animations
        self.setup_animations()
        
    def setup_animations(self):
        """Setup transition animations"""
        # Cross-fade animation group
        self.fade_animation_group = QParallelAnimationGroup()
        
        # Drop shadow effect (simplified implementation)
        self.shadow_offset = 0
        
    def add_widget(self, widget):
        """Add a widget to the transition manager"""
        self._widgets.append(widget)
        if len(self._widgets) == 1:
            # Show the first widget immediately
            widget.setParent(self)
            widget.setGeometry(self.rect())
            widget.show()
            
    def remove_widget(self, widget):
        """Remove a widget from the transition manager"""
        if widget in self._widgets:
            self._widgets.remove(widget)
            if widget.parent() == self:
                widget.setParent(None)
                
    def current_index(self):
        """Get the current widget index"""
        return self._current_index
        
    def current_widget(self):
        """Get the current widget"""
        if 0 <= self._current_index < len(self._widgets):
            return self._widgets[self._current_index]
        return None
        
    def widget(self, index):
        """Get widget at index"""
        if 0 <= index < len(self._widgets):
            return self._widgets[index]
        return None
        
    def count(self):
        """Get the number of widgets"""
        return len(self._widgets)
        
    def set_current_index(self, index):
        """Set the current widget with transition animation"""
        if (0 <= index < len(self._widgets) and 
            index != self._current_index and 
            not self._is_transitioning):
            
            self._is_transitioning = True
            self.perform_transition(self._current_index, index)
            self._current_index = index
            
    def perform_transition(self, from_index, to_index):
        """Perform the transition animation between widgets"""
        if not (0 <= from_index < len(self._widgets) and 
                0 <= to_index < len(self._widgets)):
            self._is_transitioning = False
            return
            
        from_widget = self._widgets[from_index]
        to_widget = self._widgets[to_index]
        
        # Position the widgets
        to_widget.setParent(self)
        to_widget.setGeometry(self.rect())
        
        # Create cross-fade animation
        self.create_crossfade_animation(from_widget, to_widget)
        
    def create_crossfade_animation(self, from_widget, to_widget):
        """Create cross-fade transition animation with Z-depth drop-shadow effects"""
        # Hide the from widget and show the to widget
        from_widget.show()
        to_widget.show()
        to_widget.setOpacity(0.0)
        
        # Add drop shadow effect to from_widget for Z-depth
        self.add_drop_shadow_effect(from_widget, "from")
        
        # Add drop shadow effect to to_widget for Z-depth
        self.add_drop_shadow_effect(to_widget, "to")
        
        # Create opacity animations for both widgets
        from_animation = QPropertyAnimation(from_widget, b"opacity")
        from_animation.setDuration(250)  # 250ms as required
        from_animation.setStartValue(1.0)
        from_animation.setEndValue(0.0)
        from_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        to_animation = QPropertyAnimation(to_widget, b"opacity")
        to_animation.setDuration(250)  # 250ms as required
        to_animation.setStartValue(0.0)
        to_animation.setEndValue(1.0)
        to_animation.setEasingCurve(QEasingCurve.Type.InCubic)
        
        # Create shadow animations for Z-depth effect
        from_shadow_animation = QPropertyAnimation(from_widget, b"shadow_offset")
        from_shadow_animation.setDuration(250)
        from_shadow_animation.setStartValue(5.0)
        from_shadow_animation.setEndValue(0.0)
        from_shadow_animation.setEasingCurve(QEasingCurve.Type.OutCubic)
        
        to_shadow_animation = QPropertyAnimation(to_widget, b"shadow_offset")
        to_shadow_animation.setDuration(250)
        to_shadow_animation.setStartValue(0.0)
        to_shadow_animation.setEndValue(5.0)
        to_shadow_animation.setEasingCurve(QEasingCurve.Type.InCubic)
        
        # Create animation group
        animation_group = QParallelAnimationGroup()
        animation_group.addAnimation(from_animation)
        animation_group.addAnimation(to_animation)
        animation_group.addAnimation(from_shadow_animation)
        animation_group.addAnimation(to_shadow_animation)
        
        # Connect finished signal
        animation_group.finished.connect(lambda: self.on_transition_finished(from_widget, to_widget))
        
        # Start animation
        animation_group.start()
        
    def add_drop_shadow_effect(self, widget, direction):
        """Add drop shadow effect for Z-depth"""
        # This is a simplified implementation
        # In a real application, you would use QGraphicsDropShadowEffect
        pass
        
    def on_transition_finished(self, from_widget, to_widget):
        """Handle transition finished"""
        from_widget.hide()
        self._is_transitioning = False
        
    def resizeEvent(self, event):
        """Handle resize event"""
        super().resizeEvent(event)
        
        # Resize all widgets to match the transition manager
        for widget in self._widgets:
            if widget.parent() == self:
                widget.setGeometry(self.rect())
                
    def set_current_widget(self, widget):
        """Set the current widget by widget reference"""
        try:
            index = self._widgets.index(widget)
            self.set_current_index(index)
        except ValueError:
            pass  # Widget not found
            
    def next(self):
        """Go to the next widget"""
        if len(self._widgets) > 1:
            next_index = (self._current_index + 1) % len(self._widgets)
            self.set_current_index(next_index)
            
    def previous(self):
        """Go to the previous widget"""
        if len(self._widgets) > 1:
            prev_index = (self._current_index - 1) % len(self._widgets)
            self.set_current_index(prev_index)


# Extension of QWidget to add opacity property for animation
class TransitionWidget(QWidget):
    """Widget with opacity property for transition animations"""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self._opacity = 1.0
        self._opacity_effect = QGraphicsOpacityEffect()
        self.setGraphicsEffect(self._opacity_effect)
        self._opacity_effect.setOpacity(self._opacity)
        
    def opacity(self):
        """Get widget opacity"""
        return self._opacity
        
    def setOpacity(self, opacity):
        """Set widget opacity"""
        self._opacity = max(0.0, min(1.0, opacity))
        self._opacity_effect.setOpacity(self._opacity)
        
    def setOpacityProperty(self, opacity):
        """Set opacity property (for QPropertyAnimation)"""
        self.setOpacity(opacity)