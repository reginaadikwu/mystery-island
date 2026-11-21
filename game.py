
# Island map: each location connects only to its listed neighbors.
ISLAND_MAP = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}


def new_game(name):
    """Create a new player and return the initial game state."""
    return {
        "name": name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False
    }


def display_instructions():
    """Display the basic instructions for the game."""
    print("\nWelcome to Mystery Island: The Lost Lighthouse!")
    print("Explore the island, collect useful objects,")
    print("restore the lighthouse beacon and get rescued.")
    print("Be careful: your energy is limited!")


def available_actions():
    """Return the menu choices available to the player."""
    return ["1", "2", "3"]


def move_player(player, destination):
    """Move the player if the destination is connected."""
    current_location = player["location"]

    # Normalize the destination to avoid case-sensitive mistakes.
    destination = destination.strip().title()

    if destination not in ISLAND_MAP[current_location]:
        print(f"\nYou cannot travel from {current_location} to {destination}.")
        return False

    if player["energy"] <= 0:
        print("\nYou have no energy left to travel.")
        return False

    player["location"] = destination
    player["energy"] -= 1

    print(f"\nYou traveled to {destination}.")
    print(f"Energy remaining: {player['energy']}")

    return True


def apply_action(player, action, destination=None):
    """Process the player's menu choice."""
    if action == "1":
        print(f"\nPlayer: {player['name']}")
        print(f"Location: {player['location']}")
        print(f"Energy: {player['energy']}")
        print(f"Inventory: {player['inventory']}")

    elif action == "2":
        if destination:
            move_player(player, destination)
        else:
            print("\nYou must enter a destination.")

    elif action == "3":
        player["game_over"] = True
        print("\nThanks for playing. Goodbye!")

    else:
        print("\nInvalid choice. Please select 1, 2, or 3.")

