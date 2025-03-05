# src/chess.py
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
