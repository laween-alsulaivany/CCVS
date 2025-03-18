class GUI:
    # dummy variables
    played_games = 0
    wins = 0
    turn_number = 0
    player = "Ben"

    def __init__(self):
        pass
    
    
    def displayGUI(self):
        print( f"Number of games {self.player} has played: {self.played_games}" \
               f"{' ' * 11}Turn number: {self.turn_number}\n" \
               f"Number of games {self.player} has won: {self.wins}" \
               f"{' ' * 14}Playable moves:\n" \
               f"Fallen pieces:\n" \
               f"Example on how to play:") # implement playable moves and decide on how to play the game