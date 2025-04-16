from CLI_class import CLI
import chess

# Overriding the piece displays from the chess library to make it prettier
UNICODE_PIECES = {
                  "p": "♙", "r": "♖", "n": "♘", "b": "♗", "q": "♕", "k": "♔",
                  "P": "♟", "R": "♜", "N": "♞", "B": "♝", "Q": "♛", "K": "♚"
                 }

def displayBoard(board):
    # files are represented with letters A-H
    print("  A B C D E F G H")
    print("  -----------------")
    # a row is a rank in chess
    for rank in range(8, 0, -1):
        row = []
        # a column is a file in chess
        for file in range(8):
            # chess library's index system
            square = chess.square(file, rank-1)
            # store the piece at the current square
            piece = board.piece_at(square)
            # fill in the board with white and black squares
            # white squares map to even tiles, black maps to odd
            square_color = "🔲" if (rank + file) % 2 == 0 else "⬛"
            # now append either a piece or square to each row
            row.append(f"{UNICODE_PIECES[piece.symbol()]} " if piece else f"{square_color}")
        # and add the row we just made to the board
        print(f"{rank} {''.join(row) if piece else ''.join(row)}")
    print("  -----------------")
    print("  A B C D E F G H")



def main():
    # make a board with the chess library
    board = chess.Board()
    # use our version of displaying the board
    displayBoard(board)
    cli = CLI()
    # show the CLI
    cli.displayCLI(board)
    # game loop
    # is_game_over handles every possible game ending state
    while not board.is_game_over():
        # this gets the allowed moves for each team
        legal_moves = [move.uci() for move in board.legal_moves]
        # display whose turn it is
        current_team = "White" if board.turn == chess.WHITE else "Black"
        print(f"{current_team} team's move!")
        print(f"Legal moves: {legal_moves}")
        # I'm just assuming the chess library's moves only work with lowercase letters
        move = input("Enter your move: ").strip().lower()
        # try except to ensure the move format was correct
        try:
            # UCI = Universal Chess Interface (common interface used in chess engines)
            chess_move = chess.Move.from_uci(move)
            # check if the input is a legal move and perform it if so, then display the board again to
            # show the move
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
