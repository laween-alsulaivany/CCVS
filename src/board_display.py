"""
This file contains a pretty CL display function of the chess board (as the
chess library's version was disappointing) and contains functions for
checking validity of a move and displaying what team is currently voting
"""

import chess
from CLI_class import CLI
import chess
from CLI_class import CLI
from typing import Dict, Optional, List

# Overriding the piece displays from the chess library to make it prettier
UNICODE_PIECES: Dict[str, str] = {
    "p": "♙", "r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔",
    "P": "♟", "R": "♜", "N": "♞", "B": "♝", "Q": "♛", "K": "♚"
}


# Displays the board in a format HTML can understand
def displayBoardAsString(board: chess.Board) -> str:
    """
    Converts the current state of the chess board into a human-readable
    string format that includes row and column labels and represents
    pieces using Unicode characters.

    Args:
        board: The chess board object to be displayed.

    Returns:
        A string representation of the chess board.
    """
    rows: List[str] = []
    rows.append("--A  B  C  D  E  F  G  H")
    rows.append("-----------------------------")
    # A row is a rank in chess
    for rank in range(8, 0, -1):
        row: List[str] = []
        for file in range(8):
            square: chess.Square = chess.square(file, rank - 1)
            piece: Optional[chess.Piece] = board.piece_at(square)
            square_color: str = "🔲" if (rank + file) % 2 == 0 else "⬛"
            if piece:
                row.append(f"{UNICODE_PIECES[piece.symbol()]} ")
            else:
                row.append(square_color)
        rows.append(f"{rank} {''.join(row)}")
    rows.append("-----------------------------")
    rows.append("--A  B  C  D  E  F  G  H")
    return "\n".join(rows)


# Sends the current team
def team(board: chess.Board) -> str:
    """
    Determines the current player's team based on the board's turn.

    Args:
        board: The current chess board object.

    Returns:
        "White" if it's White's turn, "Black" if it's Black's turn.
    """
    current_team: str = "White" if board.turn == chess.WHITE else "Black"
    return current_team


# Tells if the move is legal or not
def legal_move(board: chess.Board, move: str) -> str:
    """
    Checks if a given move is legal on the current chess board.

    Args:
        board: The current chess board object.
        move: The move to be checked, in Universal Chess Interface (UCI)
              format (e.g., "e2e4").

    Returns:
        A message indicating whether the move was legal and successful,
        illegal, or in an incorrect format.
    """
    try:
        # UCI = Universal Chess Interface (common interface used in chess engines)
        chess_move: chess.Move = chess.Move.from_uci(move)
        # Check if the input is a legal move and perform it if so, then
        # display the board again to show the move
        if chess_move in board.legal_moves:
            return "Your vote was successful"
        else:
            return "Illegal move: Try voting for another move!"
    except ValueError:
        return ("Illegal move format: use the notation <initial position>"
                "<target position> e.g. e2e3")