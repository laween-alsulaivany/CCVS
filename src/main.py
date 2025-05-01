"""
This is the main entry point for the CCVS Data Persistence and GitHub Integration module.
This module is responsible for saving and loading the game state to and from a local file, as well as committing the game state to a GitHub repository.
"""

# from src.data_persistence import save_game_state, load_game_state
import sys
import github_integration as GHI
import data_persistence as DP
import Tracker
import game
import CLI_class
import chess
from game import displayBoard
import json
from pathlib import Path
import os
import stat



def getCurrentGameBoard():
    DATA_FILE = (
        Path(__file__)  # e.g. /…/project/src/cron.py
        .resolve()  # make it absolute
        .parent.parent  # => /…/project/src  # => /…/project
        / "data"
        / "gameState.json"
        )
    
    with open(DATA_FILE, "r") as file:
        EntireGame = json.load(file)

    game = EntireGame["games"][-1]

    return chess.Board(game[1])
    


def main():
    print("Starting the Chess CLI...")
    cli = CLI_class.CLI()
    # initialize a board
    board = getCurrentGameBoard()
    # get a list of legal moves
    legal_moves = [move.uci() for move in board.legal_moves]
    data = GHI.getGameState()

    # handle the arguments
    if len(sys.argv) == 1:
        print("Displaying the CLI")
        # Display the CLI
        displayBoard(board) # don't know if you want the board displayed when this is called as well
        cli.displayCLI()
        # TODO: Add logic for when no arguments are passed
        # I suck at CL parsing crap so I'm leaving this to you lads
        return

    command = sys.argv[1].lower()

    if command == "vote":
        print("Handling vote...")

        home_dir = os.path.expanduser("~")
        vote_file = os.path.join(home_dir, ".vote.json")

        if not os.path.exists(vote_file):
            open(vote_file, "w").close()

        os.chmod(vote_file, 0o644)

        # Check if the home directory has the required permissions
        home_mode = stat.S_IMODE(os.stat(home_dir).st_mode)

        required_home_perms = 0o705

        if (home_mode & required_home_perms) != required_home_perms:
            os.chmod(home_dir, home_mode | required_home_perms)


        if (len(sys.argv) == 3):
            # assuming the 3rd argument is a vote.
            vote = sys.argv[2].lower()

            # voting.py

            print(vote)
            if vote in board.legal_moves:
                print("Vote successfully casted!")
                board.push(vote)
                displayBoard(board)
                with open(vote_file, "w") as file:
                    file.write(vote)

            else:
                print(f"Error validating vote \"{vote}\", first ensure vote follows this convention: \"e2e3\"\n" \
                      f"Then ensure your vote is within the list of legal moves:\n{legal_moves}")
        else:
            print("did not provide a vote.")

        
    elif command == "stats":
        print("Showing statistics...")
        # TODO: Add stats logic here
        #track = Tracker.ParticipationTracker()
        Tracker.test_participation_tracker()

    elif command == "help":
        print("Available commands:")
        print("  vote   - Vote for a move")
        print("  stats  - Show current game stats")
        print("  help   - Show this help message")
        print("  (no arguments) - Run default mode")
    elif command == "test":
        DP.test1()
        Tracker.test_participation_tracker()
        game.main()
    else:
        print(f"Unknown command: {command}")
        print("Use 'help' for a list of available commands.")

def save_test_to_vote_json(data: str):
    vote_file = Path.home() / ".vote.json"

    with open(vote_file, "w") as f:
        json.dump(data, f)

    print(f"Saved to {vote_file}")


if __name__ == "__main__":
    main()
