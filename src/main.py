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


def main():
    print("Starting the Chess CLI...")
    cli = CLI_class.CLI()
    # initialize a board
    board = chess.Board()
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
        if (len(sys.argv) == 3):
            # assuming the 3rd argument is a vote.
            vote = sys.argv[2].lower()

            # voting.py

            print(vote)
            if vote in board.legal_moves:
                print("Vote successfully casted!")
                board.push(vote)
                displayBoard(board)
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

if __name__ == "__main__":
    main()
