# src/chess.py

"""
This is just a place holder for the chess board rendering function.
You can replace this with your own chess board rendering function whoever is responsible for this part.
"""


def render_board():
    """
    Render a basic chess board using Unicode.
    """
    board = [
        "  --------------------------------",
        "8 | ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ |",
        "  --------------------------------",
        "7 | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ |",
        "  --------------------------------",
        "6 |   |   |   |   |   |   |   |   |",
        "  --------------------------------",
        "5 |   |   |   |   |   |   |   |   |",
        "  --------------------------------",
        "4 |   |   |   |   |   |   |   |   |",
        "  --------------------------------",
        "3 |   |   |   |   |   |   |   |   |",
        "  --------------------------------",
        "2 | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |",
        "  --------------------------------",
        "1 | ♖ | ♘ | ♗ | ♕ | ♔ | ♗ | ♘ | ♖ |",
        "  --------------------------------",
        "    a   b   c   d   e   f   g   h",
    ]
    for row in board:
        print(row)


if __name__ == "__main__":
    render_board()
