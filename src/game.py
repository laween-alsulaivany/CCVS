"""
This file contains game logic for the entire program.
It supports functionality for displaying the board in the command
line in a pleasing way, validating moves, and validating whether
a game is over or not.
"""

import chess
from CLI_class import CLI
from typing import Dict, Optional, List

# Overriding the piece displays from the chess library to make it prettier
UNICODE_PIECES: Dict[str, str] = {
    "p": "♙", "r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔",
    "P": "♟", "R": "♜", "N": "♞", "B": "♝", "Q": "♛", "K": "♚"
}


def displayBoard(board: chess.Board) -> None:
    """
    Prints a human-readable representation of the chess board to the console,
    using Unicode characters for pieces and different symbols for light and dark squares.

    Args:
        board: The chess board object to be displayed.
    """
    print("  A B C D E F G H")
    print("  -----------------")
    # A row is a rank in chess
    for rank in range(8, 0, -1):
        row: List[str] = []
        # A column is a file in chess
        for file in range(8):
            # Chess library's index system
            square: chess.Square = chess.square(file, rank - 1)
            # Store the piece at the current square
            piece: Optional[chess.Piece] = board.piece_at(square)
            # Fill in the board with white and black squares
            # White squares map to even tiles, black maps to odd
            square_color: str = "🔲" if (rank + file) % 2 == 0 else "⬛"
            # Now append either a piece or square to each row
            row.append(f"{UNICODE_PIECES[piece.symbol()]} " if piece else f"{square_color}")
        # And add the row we just made to the board
        print(f"{rank} {''.join(row)}")
    print("  -----------------")
    print("  A B C D E F G H")


def main() -> None:
    """
    The main function that initializes the chess game, displays the board and CLI,
    and runs the game loop, taking player input for moves until the game ends.
    """
    # Make a board with the chess library
    board: chess.Board = chess.Board()
    # Use our version of displaying the board
    displayBoard(board)
    cli: CLI = CLI()
    # Show the CLI
    cli.displayCLI(board)
    # Game loop
    # is_game_over handles every possible game ending state
    while not board.is_game_over():
        # This gets the allowed moves for each team
        legal_moves: List[str] = [move.uci() for move in board.legal_moves]
        # Display whose turn it is
        current_team: str = "White" if board.turn == chess.WHITE else "Black"
        print(f"{current_team} team's move!")
        print(f"Legal moves: {legal_moves}")
        # I'm just assuming the chess library's moves only work with lowercase letters
        move: str = input("Enter your move: ").strip().lower()
        # Try except to ensure the move format was correct
        try:
            # UCI = Universal Chess Interface (common interface used in chess engines)
            chess_move: chess.Move = chess.Move.from_uci(move)
            # Check if the input is a legal move and perform it if so, then
            # display the board again to show the move
            if chess_move in board.legal_moves:
                board.push(chess_move)
                displayBoard(board)
            else:
                print("Illegal move: Try making another move!")
                continue
        except ValueError:
            print("Illegal move format: use the notation <initial position><target position> e.g. e2e3")
            continue

    print("Game over")
    print(f"Result: {board.result()}")


if __name__ == "__main__":
    main()