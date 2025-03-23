

class CLI:
    def __init__(self):
        pass

    def displayCLI(self):
        print(f"Number of games {self.player} has played: {self.played_games}"
              f"{' ' * 11}Turn number: {self.turn_number}\n"
              f"Number of games {self.player} has won: {self.wins}"
              f"{' ' * 14}Playable moves:\n"
              f"Fallen pieces:\n"
              # implement playable moves and decide on how to play the game
              f"Example on how to play:")
