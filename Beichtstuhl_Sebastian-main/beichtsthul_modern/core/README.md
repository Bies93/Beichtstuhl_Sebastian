# Core Modules Documentation

This directory contains the business logic and core functionality of the Beichtsthul application.

## Modules Overview

### AntwortGenerator
Generates sardonic responses based on sin categories and handles sin categorization.

#### Key Features
- Categorizes user confessions into different sin types
- Generates humorous, sarcastic responses based on categories
- Handles special easter egg responses for specific keywords
- Maintains mappings between sin categories and emotional responses

#### Public Methods
- `kategorisiere_suende(text)`: Categorizes a confession based on keywords
- `get_antwort(kategorie)`: Gets a random sardonic response for a category
- `prüfe_easter_eggs(text)`: Checks for special easter egg conditions
- `berechne_schulden(kategorie)`: Calculates karma debt for a sin category

### KarmaRechner
Calculates karma debt based on confessed sins and their severity.

#### Key Features
- Calculates karma points based on sin category
- Applies bonuses for longer confessions
- Adds penalties for particularly severe sins
- Handles special cases like shouting (CAPS)

#### Public Methods
- `berechne_karma_schulden(kategorie, text)`: Calculates total karma debt for a confession

### DateiManager
Handles data persistence and loading for user confessions and statistics.

#### Key Features
- Saves user data to JSON files
- Loads saved data on application startup
- Handles data serialization and deserialization
- Error handling for file operations

#### Public Methods
- `speichere_daten(karma_schulden, beicht_historie, suenden_kategorien)`: Saves user data to file
- `lade_daten()`: Loads saved user data from file

### StatistikManager
Manages and displays confession statistics to the user.

#### Key Features
- Displays detailed statistics about user confessions
- Shows karma debt summary
- Provides category breakdowns
- Handles reset confirmation dialogs

#### Public Methods
- `zeige_statistiken(karma_schulden, beicht_historie, suenden_kategorien)`: Shows statistics dialog
- `bestätige_reset()`: Shows reset confirmation dialog

### Constants
Contains all application-wide constants and configuration values.

#### Key Categories
- Application information (name, version, author)
- File paths and names
- Color scheme definitions
- Font definitions and sizes
- Spacing and layout constants
- Animation durations
- Emotion mappings
- Sin categories and base points
- Karma debt mappings
- Penalty words

## Data Flow

1. User enters confession in UI
2. AntwortGenerator categorizes the sin
3. KarmaRechner calculates karma debt
4. DateiManager saves updated data
5. UI updates to show response and karma status
6. StatistikManager provides access to historical data

## Error Handling

All core modules include proper error handling:
- File I/O operations are wrapped in try/except blocks
- Graceful degradation when data files are missing or corrupted
- User-friendly error messages in the UI