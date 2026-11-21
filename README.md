# Mystery Island: The Lost Lighthouse

A beginner-friendly, text-based Python adventure game where a player explores a mysterious island.

## Project Overview

The player wakes up on an island after a storm. To get rescued, they must explore the island, find useful objects, and restore the lighthouse beacon.

## Current Features

- Player name input
- Player status display
- Five island locations
- Connected-location movement
- Movement validation
- Energy tracking
- Invalid menu input handling
- Case-insensitive destination names

## Island Map

Beach → Jungle → Cave → Old Bridge → Lighthouse

Players can move between connected locations in both directions.

## Requirements

- Python 3.8 or newer
- No third-party Python packages required

## How to Run

Clone the repository and enter the project folder:

```bash
python3 main.py
```

## How to Run Tests

```bash
python3 -m unittest discover -s tests -v
```

## Game Controls

1. View player status
2. Move to another location
3. Quit game

## Current Development Stage

Stage 1: Game setup and menu — completed.

Stage 2: Island locations and movement — implemented and tested.

## Planned Features

- Item collection and inventory
- Rope and lantern
- Bridge access restrictions
- Lighthouse restoration
- Energy-based win and lose conditions
- Replay functionality

## Learning Objectives

This project practices Python variables, dictionaries, lists, functions, conditionals, loops, input validation, and automated testing.
