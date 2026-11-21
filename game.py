# Island map: each location connects only to its listed neighbors.
ISLAND_MAP = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"]
}

# Items that can be discovered at different locations.
ITEM_LOCATIONS = {
    "Beach": "Rope",
    "Cave": "Lantern"
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
    return ["1", "2", "3", "4", "5"]


def move_player(player, destination):
    """Move the player if the destination is connected and accessible."""
    current_location = player["location"]
    destination = destination.strip().title()

    if destination not in ISLAND_MAP[current_location]:
        print(f"\nYou cannot travel from {current_location} to {destination}.")
        return False

    # The Rope is required to cross to the Lighthouse.
    if destination == "Lighthouse" and "Rope" not in player["inventory"]:
        print("\nThe bridge is too damaged to cross safely!")
        print("You need a Rope to reach the Lighthouse.")
        return False

    if player["energy"] <= 0:
        print("\nYou have no energy left to travel.")
        return False

    player["location"] = destination
    player["energy"] -= 1

    print(f"\nYou traveled to {destination}.")
    print(f"Energy remaining: {player['energy']}")

    return True


def items_at_location(player):
    """Return items available at the player's current location."""
    location = player["location"]

    if location in ITEM_LOCATIONS:
        item = ITEM_LOCATIONS[location]

        if item not in player["inventory"]:
            return [item]

    return []


def collect_item(player, item):
    """Collect an item if it is available at the current location."""
    item = item.strip().title()
    available_items = items_at_location(player)

    if item not in available_items:
        print(f"\n{item} is not available here.")
        return False

    player["inventory"].append(item)

    print(f"\nYou collected the {item}!")
    return True


def restore_beacon(player):
    """Restore the lighthouse beacon if the player has the Lantern."""
    if player["location"] != "Lighthouse":
        print("\nYou must be at the Lighthouse to restore the beacon.")
        return False

    if "Lantern" not in player["inventory"]:
        print("\nThe lighthouse beacon is too dark to restore.")
        print("You need the Lantern.")
        return False

    print("\nYou use the Lantern to restore the lighthouse beacon!")
    print("The bright light shines across the ocean.")
    print("A rescue boat sees the signal and heads toward the island.")
    print("\nCONGRATULATIONS!")
    print(f"{player['name']} has escaped Mystery Island!")

    player["won"] = True
    player["game_over"] = True

    return True


def apply_action(player, action, destination=None, item=None):
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
        available_items = items_at_location(player)

        if not available_items:
            print("\nThere are no items available to collect here.")

        elif item:
            collect_item(player, item)

        else:
            print("\nItems available:")
            for available_item in available_items:
                print(f"- {available_item}")
            print("\nYou must specify an item.")

    elif action == "4":
        restore_beacon(player)

    elif action == "5":
        player["game_over"] = True
        print("\nThanks for playing. Goodbye!")

    else:
        print("\nInvalid choice. Please select 1, 2, 3, 4, or 5.")
