# UI Components Documentation

This directory contains all user interface components and resources for the Beichtsthul application.

## Directory Structure

```
ui/
├── main_window.py      # Main window class
├── components/         # Reusable UI components
│   ├── animated_button.py
│   ├── confession_input.py
│   ├── karma_display.py
│   ├── monk_visualizer.py
│   └── response_display.py
└── resources/          # UI resources
    ├── styles.py
    ├── animations.py
    └── themes.py
```

## Main Window

The `MainWindow` class serves as the central coordinator for all UI elements. It handles:
- Application initialization and setup
- Layout management
- Component integration
- Event handling
- Window animations
- Data flow between components

### Key Features
- Responsive layout that adapts to window resizing
- Centralized event handling
- Animation coordination
- Data synchronization with core modules

## UI Components

### AnimatedButton
A custom QPushButton with enhanced visual effects and animations.

#### Features
- Ripple effect on click
- Scale animation on press/release
- Custom styling support
- Hover effects
- Accessible design

#### Usage
```python
button = AnimatedButton("Click Me")
button.setObjectName("primary")  # For styling
button.clicked.connect(handler)
```

### ConfessionInput
A specialized text input area for confessions with character counting.

#### Features
- Character counter with visual feedback
- Auto-resizing based on content
- Animation for character limit warnings
- Enter key submission support
- Custom styling

#### Usage
```python
confession_input = ConfessionInput()
confession_input.confession_submitted.connect(handler)
```

### KarmaDisplay
A visual display for karma status with progress bar and animations.

#### Features
- Animated numeric counter
- Progress bar visualization
- Color-coded status indicators
- Smooth value transitions
- Responsive design

#### Usage
```python
karma_display = KarmaDisplay()
karma_display.set_karma(150)
```

### MonkVisualizer
A custom widget for rendering the animated monk character.

#### Features
- Emotion-based facial expressions
- Breathing animation
- Blinking animation
- Responsive scaling
- QPainter-based rendering

#### Usage
```python
monk_visualizer = MonkVisualizer()
monk_visualizer.set_emotion("lachend")
```

### ResponseDisplay
An animated display area for the monk's responses.

#### Features
- Text reveal animation
- Emotional indicator
- Copy to clipboard functionality
- Responsive font sizing
- Custom styling

#### Usage
```python
response_display = ResponseDisplay()
response_display.set_text("Your sardonic response here")
response_display.set_emotion("urteilend")
```

## Resources

### Styles
The `styles.py` file contains all stylesheet definitions for the application.

#### Key Styles
- Main window styling
- Button styles (primary, secondary)
- Text input styling
- Label styling
- Card-based component styling
- Status bar styling

### Animations
The `animations.py` file defines animation behaviors and timing.

#### Animation Definitions
- Window fade in/out
- Button hover/press effects
- Text focus animations
- Monk emotion transitions
- Karma change animations

#### Easing Curves
- Standard easing curves (InCubic, OutCubic, InOutCubic)
- Bounce easing curves
- Elastic easing curves
- Back easing curves

### Themes
The `themes.py` file manages application themes and color schemes.

#### Theme Management
- Dark theme (default)
- Light theme (planned)
- Theme switching capabilities
- Color palette management

## Integration Patterns

### Signal/Slot Connections
UI components communicate through Qt's signal/slot mechanism:
- `confession_submitted` signal from ConfessionInput
- `clicked` signal from AnimatedButton
- Custom signals for component-specific events

### Data Flow
1. User interaction triggers UI events
2. MainWindow processes events and updates core modules
3. Core modules process data and return results
4. MainWindow updates UI components with new data
5. UI components animate changes and display updated information

## Responsive Design

All UI components implement responsive design principles:
- Dynamic sizing based on available space
- Font size adjustment for different screen dimensions
- Layout changes for different aspect ratios
- Touch-friendly controls for tablet use

## Customization

### Styling
UI components can be customized through:
- Object names for targeted styling
- Qt stylesheets
- Theme management system
- Custom properties

### Animation Speed
Animation durations can be adjusted through:
- Constants in core/constants.py
- Component-specific timing parameters
- User preference settings (planned)