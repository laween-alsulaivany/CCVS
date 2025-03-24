"""
This is the main entry point for the CCVS Data Persistence and GitHub Integration module.
This module is responsible for saving and loading the game state to and from a local file, as well as committing the game state to a GitHub repository.
"""

# from src.data_persistence import save_game_state, load_game_state
import sys
import github_integration as GHI
import data_persistence as DP


def main():
    print("Starting the Chess CLI...")

    data = GHI.getGameState()

    # handle the arguments
    if len(sys.argv) == 1:
        print("Displaying the GUI")
        # Display the CLI

        # TODO: Add logic for when no arguments are passed

        return

    command = sys.argv[1].lower()

    if command == "vote":
        print("Handling vote...")

        # voting.py

        # TODO: Add vote logic here
    elif command == "stats":
        print("Showing statistics...")
        # TODO: Add stats logic here
    elif command == "help":
        print("Available commands:")
        print("  vote   - Vote for a move")
        print("  stats  - Show current game stats")
        print("  help   - Show this help message")
        print("  (no arguments) - Run default mode")
    elif command == "test":
        DP.test1()
    else:
        print(f"Unknown command: {command}")
        print("Use 'help' for a list of available commands.")


if __name__ == "__main__":
    main()
