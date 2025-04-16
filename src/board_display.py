import chess
from CLI_class import CLI

# Overriding the piece displays from the chess library to make it prettier
UNICODE_PIECES = {
                "p": "♙", "r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔",
                "P": "♟", "R": "♜", "N": "♞", "B": "♝", "Q": "♛", "K": "♚"
                }

def displayBoardAsString(board):
    # files are represented with letters A-H
    rows = []
    rows.append("--A  B  C  D  E  F  G  H")
    rows.append("-----------------------------")
    # a row is a rank in chess
    for rank in range(8, 0, -1):
        row = []
        for file in range(8):
            square = chess.square(file, rank - 1)
            piece = board.piece_at(square)
            square_color = "🔲" if (rank + file) % 2 == 0 else "⬛"
            if piece:
                row.append(f"{UNICODE_PIECES[piece.symbol()]} ")
            else:
                row.append(square_color)
        rows.append(f"{rank} {''.join(row)}")
    rows.append("-----------------------------")
    rows.append("--A  B  C  D  E  F  G  H")
    return "\n".join(rows)

def team(board):
    current_team = "White" if board.turn == chess.WHITE else "Black"
    return current_team

def legal_move(board, move):
    try:
            # UCI = Universal Chess Interface (common interface used in chess engines)
            chess_move = chess.Move.from_uci(move)
            # check if the input is a legal move and perform it if so, then display the board again to
            # show the move
            if chess_move in board.legal_moves:
                return "Your vote was successful"
            else:
                return "Illegal move: Try voting for another move!"
    except ValueError:
        return ("Illegal move format: use the notation <initial position><target position> e.g. e2e3")