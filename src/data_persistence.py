
"""
This module provides functions for saving and loading the game state to/from a JSON file. This will be useful for saving the game state between sessions.
"""


import json
import os

# Default file name for the game state JSON file
DEFAULT_STATE_FILE = "game_state.json"


def save_game_state(game_state: dict, filename: str = DEFAULT_STATE_FILE) -> None:
    """
    Save the game state dictionary to a JSON file.
    (We can change the location of this file later if needed.)
    """
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
