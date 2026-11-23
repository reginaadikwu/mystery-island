from game import (
    new_game,
    display_instructions,
    apply_action,
    ISLAND_MAP,
    items_at_location
)


def play_game(player):
    """Run the main gameplay loop for one session."""
    while not player["game_over"]:
        print("\n===== MAIN MENU =====")
        print("1. View player status")
        print("2. Move to another location")
        print("3. Collect an item")
        print("4. Restore lighthouse beacon")
        print("5. Quit game")

        action = input("Choose an option: ").strip()

        if action == "2":
            print(f"\nCurrent location: {player['location']}")
            print("Connected locations:")

            destinations = ISLAND_MAP[player["location"]]

            for destination in destinations:
                print(f"- {destination}")

            destination = input(
                "\nWhere would you like to go? "
            ).strip()

            apply_action(player, action, destination)

        elif action == "3":
            available_items = items_at_location(player)

            if available_items:
                print("\nItems available:")

                for item in available_items:
                    print(f"- {item}")

                item = input(
                    "\nWhat would you like to collect? "
                ).strip()

                apply_action(player, action, item=item)

            else:
                apply_action(player, action)

        else:
            apply_action(player, action)


def main():
    display_instructions()

    while True:
        name = input("\nWhat is your name? ").strip()

        if not name:
            name = "Explorer"

        player = new_game(name)

        print(f"\nWelcome, {player['name']}!")

        play_game(player)

        replay = input(
            "\nWould you like to play again? (yes/no): "
        ).strip().lower()

        if replay not in ("yes", "y"):
            print("\nThanks for playing Mystery Island!")
            break


if __name__ == "__main__":
    main()
