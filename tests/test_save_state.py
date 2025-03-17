"""
This script is a test to save the game state to a local file.
"""


from src.data_persistence import save_game_state

# Sample game state dictionary
game_state = {
    "turn": 1,
    # I imagine the game state will look like this, I used JSON because it's easy to read and write
    # I'm not sure about the board representation, so I just put a placeholder
    "board": "sample_board_representation",
    "votes": {"e2e4": 5, "d2d4": 3},
    "teams": {"white": ["Alexis", "Bob"], "black": ["Charlie", "Dana"]}
}

save_game_state(game_state)
