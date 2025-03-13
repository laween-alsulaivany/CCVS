class Piece:
    white = ''
    black = ''
    legal_moves = []

class Pawn(Piece):
    def __init__ (self):
          Piece.white = '\u265F'
          Piece.black = '\u2659'

class Rook(Piece):
    def __init__ (self):
        Piece.white = '\u265C'
        Piece.black = '\u2656'

class Knight(Piece):
    def __init__ (self):
        Piece.white = '\u265E'
        Piece.black = '\u2658'

class Bishop(Piece):
    def __init__ (self):
        Piece.white = '\u265D'
        Piece.black = '\u2657'

class Queen(Piece):
    def __init__ (self):
        Piece.white = '\u265B'
        Piece.black = '\u2655'

class King(Piece):
    def __init__ (self):
        Piece.white = '\u265A'
        Piece.black = '\u2654'

class Board:
    board = [['' for _ in range(8)] for _ in range(8)]
    def __init__ (self):
        self.self = self

    def makeBoard(self):
        for row in range(8):
            for col in range(8):
                # even spaces are white squares
                if (row+col)%2 == 0:
                    self.board[row][col] = '🔲'
                # odd spaces are black squares
                else:
                    self.board[row][col] = '⬛'
        self.board[0][0] = Rook().black + " "
        self.board[0][1] = Knight().black + " "
        self.board[0][2] = Bishop().black + " "
        self.board[0][3] = Queen().black + " "
        self.board[0][4] = King().black + " "
        self.board[0][7] = Rook().black + " "
        self.board[0][6] = Knight().black + " "
        self.board[0][5] = Bishop().black + " "
        for i in range(8):
            self.board[1][i] = Pawn().black + " "
        self.board[7][0] = Rook().white + " "
        self.board[7][1] = Knight().white + " "
        self.board[7][2] = Bishop().white + " "
        self.board[7][3] = Queen().white + " "
        self.board[7][4] = King().white + " "
        self.board[7][7] = Rook().white + " "
        self.board[7][6] = Knight().white + " "
        self.board[7][5] = Bishop().white + " "
        for i in range(8):
            self.board[6][i] = Pawn().white + " "
    
    def printBoardWhite(self):
        for row in self.board:
            print("".join(row))

    def printBoardBlack(self):
        for row in self.board[::-1]:
            print("".join(row))

# pieces = [Pawn, Rook, Knight, Bishop, Queen, King]

# for piece_class in pieces:
#     piece = piece_class()
#     print(f"{piece_class.__name__}: White: {piece.white}    Black: {piece.black}" )

def main():
    board = Board()
    board.makeBoard()
    board.printBoardWhite()
    print()
    board.printBoardBlack()


if __name__ == "__main__":
    main()