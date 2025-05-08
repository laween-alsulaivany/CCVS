"""
This file contains functionality for displaying a command line
interface in a pleasing way.
"""

import os
import chess
from typing import Any

class CLI:
    """
    A class representing the Command Line Interface for the chess game.
    It keeps track of player statistics and displays game information.
    """
    player: str = os.environ.get("USER", "Unnown")
    played_games: int = 0
    turn_number: int = 0
    wins: int = 0

    def __init__(self) -> None:
        """
        Initializes the CLI object. Currently, it performs no specific actions.
        """
        pass

    def displayCLI(self, board: Any) -> None:
        """
        Displays the current game information in the command line,
        including the number of games played, the current turn number,
        the number of games won by the player, and instructions on how to play.

        Args:
            board: The current chess board object (the specific type is not constrained here).
        """
        print(
            f"Number of games {self.player} has played: {self.played_games}"
            f"{' ' * 11}Turn number: {self.turn_number}\n"
            f"Number of games {self.player} has won: {self.wins}\n"
            f"Captured pieces:\n"
            f"Example on how to play: <initial space><target space> e.g. e2e3"
        )
