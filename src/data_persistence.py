"""
This module provides functions for saving and loading the game state to/from a JSON file.
This will be useful for saving the game state between sessions.
"""

import json
import os

# Get the absolute path to the data directory (../data/game_state.json)
# current file's directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.abspath(os.path.join(BASE_DIR, "..", "data"))
DEFAULT_STATE_FILE = os.path.join(DATA_DIR, "game_state.json")


def save_game_state(
        game_state: dict,
        filename: str = DEFAULT_STATE_FILE) -> None:
    """
    Save the game state dictionary to a JSON file.
    Creates the data directory if it doesn't exist.
    """
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        json.dump(game_state, f, indent=4)
    print(f"Game state saved to {filename}.")


def load_game_state(filename: str = DEFAULT_STATE_FILE) -> dict:
    """
    Load the game state from a JSON file.
    Returns an empty dictionary if the file doesn't exist.
    """
    if not os.path.exists(filename):
        print(f"No saved game state found at {filename}.")
        return {}
    with open(filename, "r") as f:
        game_state = json.load(f)
    print(f"Game state loaded from {filename}.")
    return game_state


# TESTING

def test1(filename: str = DEFAULT_STATE_FILE) -> None:
    """
    Load and pretty-print the game state JSON.
    """
    game_state = load_game_state(filename)
    if game_state:
        print(json.dumps(game_state, indent=4))
    else:
        print("Game state is empty or not found.")
