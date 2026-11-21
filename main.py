
from game import (
    new_game,
    display_instructions,
    apply_action,
    ISLAND_MAP
)


def main():
    display_instructions()

    name = input("\nWhat is your name? ").strip()

    if not name:
        name = "Explorer"

    player = new_game(name)

    print(f"\nWelcome, {player['name']}!")

    while not player["game_over"]:
        print("\n===== MAIN MENU =====")
        print("1. View player status")
        print("2. Move to another location")
        print("3. Quit game")

        action = input("Choose an option: ").strip()

        if action == "2":
            print(f"\nCurrent location: {player['location']}")
            print("Connected locations:")

            destinations = ISLAND_MAP[player["location"]]

            for destination in destinations:
                print(f"- {destination}")

            destination = input("\nWhere would you like to go? ").strip()

            apply_action(player, action, destination)

        else:
            apply_action(player, action)


if __name__ == "__main__":
    main()

