import chess

class CLI:
    player = "Ben"
    played_games = 0
    turn_number = 0
    wins = 0
    def __init__(self):
        pass    
    
    def displayCLI(self, board):
        print( f"Number of games {self.player} has played: {self.played_games}" \
               f"{' ' * 11}Turn number: {self.turn_number}\n" \
               f"Number of games {self.player} has won: {self.wins}\n" \
               f"Captured pieces:\n" \
               f"Example on how to play: <initial space><target space> e.g. e2e3") # implement playable moves and decide on how to play the game

