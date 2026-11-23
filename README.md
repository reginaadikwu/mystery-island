
# Mystery Island: The Lost Lighthouse

A beginner-friendly, text-based Python adventure game where a player explores a mysterious island, collects useful items, manages energy, and tries to escape by restoring a lighthouse beacon.

## Project Overview

The player becomes stranded on an island after a storm. To escape, they must explore different locations, collect essential items, manage their energy, unlock the Lighthouse, and restore its beacon to signal a rescue.

## Current Features

- Player name and game initialization
- Player status tracking
- Five connected island locations
- Location-based movement
- Energy and survival system
- Inventory management
- Rope collection at the Beach
- Lantern collection in the Cave
- Duplicate item collection prevention
- Location-based item validation
- Lighthouse access restricted by Rope
- Beacon restoration requires Lantern
- Winning and losing conditions
- Input validation
- Replay functionality
- New game state for each replay

## Island Map

Beach → Jungle → Cave → Old Bridge → Lighthouse

Players can move between connected locations in both directions.

## Requirements

- Python 3.8 or newer
- No third-party Python packages required

## How to Run

Clone the repository and enter the project folder.

Run the game:

```bash
python3 main.py
```

## How to Run Tests

Run the automated test suite:

```bash
python3 -m unittest discover -s tests -v
```

## Game Controls

1. View player status
2. Move to another location
3. Collect an item
4. Restore lighthouse beacon
5. Quit game

## Development Stages

- Stage 1: Game setup and player initialization — completed
- Stage 2: Island locations and movement — completed
- Stage 3: Inventory, Rope, and Lantern — completed
- Stage 4: Lighthouse access and winning condition — completed
- Stage 5: Energy and survival system — completed
- Stage 6: Replay system and fresh game sessions — completed
- Stage 7: Game experience improvements and input handling — completed

## Stage 5: Energy and Survival System

The energy system adds a survival challenge and encourages players to plan their movement carefully.

### Energy Rules

- The player begins with 5 energy.
- Every successful movement consumes 1 energy.
- Invalid movement does not consume energy.
- The player cannot move when energy reaches 0.
- Running out of energy before escaping results in Game Over.

### Survival and Game Outcomes

- Players must plan their route carefully.
- Collecting items does not consume energy.
- Players must collect the Rope and Lantern, reach the Lighthouse, and restore its beacon before running out of energy.
- The game supports both winning and losing outcomes.

### Testing

- Automated tests verify energy consumption, energy exhaustion, movement restrictions, and survival behavior.
- Manual gameplay confirmed both the losing path and successful rescue path.

## Stage 6: Replay System

The replay system allows players to start another game after finishing their current session.

### Replay Features

- Players can restart after a game ends.
- Players can enter a new name for each session.
- Each replay creates a fresh player state.
- The new game starts at the Beach.
- Energy resets to 5.
- Inventory resets to empty.
- Previous game progress does not carry over.
- Players can choose to exit instead of replaying.

### Testing

- Automated tests verify the existing game logic.
- Manual testing confirmed that quitting a game displays the replay prompt.
- Starting a new game with a different player name resets location, energy, and inventory correctly.

## Learning Objectives

This project practices:

- Python variables and data types
- Dictionaries and lists
- Functions
- Conditional statements
- Loops and nested loops
- Input validation
- State management
- Modular code organization
- Automated testing
- Debugging
- Git and GitHub version control

## Stage 7: Game Experience Improvements

Stage 7 focused on improving the player's experience through clearer feedback, better input handling, and more reliable navigation.

### Improvements

- Invalid movement displays the available connected locations.
- Empty destination input is handled with a helpful message.
- Invalid menu choices are rejected with clear instructions.
- Unexpected menu input returns the player safely to the main menu.
- Valid movement continues to work correctly with energy deduction.

### Input Handling

The game now provides clearer feedback when the player enters an invalid menu option, an empty destination, or an inaccessible location.

Instead of leaving the player confused, the game explains the problem and allows them to try again.

### Testing

- Tested invalid menu input using text, zero, and empty input.
- Tested empty movement destination.
- Tested valid movement between connected locations.
- Verified player location and energy after movement.
- Ran the full automated test suite successfully.
- Confirmed all 18 automated tests passed.

### Stage 7 Outcome

The game is more user-friendly, handles invalid input more clearly, and maintains its existing gameplay functionality.
