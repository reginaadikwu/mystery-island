# Mystery Island: The Lost Lighthouse

A beginner-friendly, text-based Python adventure game where a player explores a mysterious island.

## Project Overview

The player wakes up on an island after a storm. To get rescued, they must explore the island, find useful objects, and restore the lighthouse beacon.

## Current Features

- Player name and game initialization
- Player status tracking
- Five connected island locations
- Location-based movement
- Energy system
- Inventory system
- Rope collection at the Beach
- Lantern collection in the Cave
- Duplicate item collection prevention
- Location-based item validation
- Lighthouse access restricted by Rope
- Beacon restoration requires Lantern
- Winning condition when the beacon is restored
- Invalid input handling

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

Stage 2: Island locations and movement — completed.

Stage 3: Inventory, Rope, and Lantern — completed.

Stage 4: Locked Lighthouse and wining condition — completed

## Planned Features

- Item collection and inventory
- Rope and lantern
- Bridge access restrictions
- Lighthouse restoration
- Energy-based win and lose conditions
- Replay functionality- Bridge access restrictions
- Lighthouse restoration
- Energy-based win and lose conditions
- Replay functionality

## Learning Objectives

This project practices Python variables, dictionaries, lists, functions, conditionals, loops, input validation, and automated testing.

### Stage 5: Energy and Survival System

The game now includes an energy system that makes player decisions more important and adds a survival challenge.

**Energy rules:**
- The player begins with 5 energy.
- Every successful movement consumes 1 energy.
- Invalid movement does not consume energy.
- The player cannot move when energy reaches 0.
- Running out of energy before escaping results in Game Over.

**Survival and game outcomes:**
- Players must plan their route carefully.
- Collecting items does not consume energy.
- The player can win by collecting the Rope and Lantern, reaching the Lighthouse, and restoring its beacon before running out of energy.
- The game supports both winning and losing outcomes.

**Testing:**
- Automated tests verify energy consumption, energy exhaustion, movement restrictions, and survival behavior.
- Manual gameplay confirmed both the losing path and successful rescue path.
