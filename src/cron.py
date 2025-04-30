from typing import Literal
from pathlib import Path
import json  # json is just a pickle wrapper, just make a python dict and work from there
import chess
import base64, pickle
from random import randint
import sys  # for testing purposes

# TODO:
#   - add a state of 'test mode' when running using `python cron.py test``
#       - currently have a _HARD_CODE_TESTING
#   - have _HOME_DIRECTORY get overwritten by make cron install and reset
#       _HARD_CODE_TESTING to False
#   -


class Cron:
    # absolute path to ../data/gameState.json, regardless of CWD
    _DATA_FILE = (
        Path(__file__)  # e.g. /…/project/src/cron.py
        .resolve()  # make it absolute
        .parent.parent  # => /…/project/src  # => /…/project
        / "data"
        / "gameState.json"
    )
    _CACHED_GAME_OBJECT = None  # this will jump the object around to prevent
    # constand reloading of the json file

    _DECODED_BOARD = chess.Board()  # This is just the bord as a chess.Board()

    _HARD_CODE_TESTING = (
        True  # if true, this will put specific users in teams for testing.
    )

    _HOME_DIRECTORY = None  # This needs to be overwritten by the make cron install

    # COMPLETED FUNCTIONS

    def __init__(self, test_mode: bool = False):
        self._HARD_CODE_TESTING = test_mode

    def gameState(self) -> Literal["active", "not initiated"]:
        """
        Determine and return the current state of the game.

        Returns:
            Literal["active", "not initiated"]:
                - "active": if the game is currently in progress.
                - "not initiated": if the game has not been started yet.
        """

        if self._DATA_FILE.exists():
            return "active"
        return "not initiated"

    def initiateGameFile(self):
        """
        This creates the json file in data.
        It will also add a skeleton of what a game should look like.

        Prerequisite:
            gameState() checked for a file but it was not found.
        """

        mainComment = """
        STRUCTURE
        EntireGame = {
            comments = "This structure will be stored in the comments.",
            games = [
                {
                    gameId = 1,
                    currentBoard = "" # a chess board fin array string
                    turn = "" # white (w) or black (b), white goes first
                    voteHistory = [
                        "a1b2",
                    ]
                    teams = [
                        [],     # white
                        []      # black
                    ]
                }
            ]

        }
        """
        EntireGame = dict()
        EntireGame["comments"] = mainComment
        EntireGame["games"] = list()

        # the skeleton of the game
        initialGame = []
        # initiate the board and convert it into a format that persists
        self._DECODED_BOARD = chess.Board()

        # gameBoard_pBytes = pickle.dumps(self._DECODED_BOARD)
        # gameBoard_str = base64.b64encode(gameBoard_pBytes).decode('ascii')

        initialGame.append(0)  # gameID
        initialGame.append(
            self._DECODED_BOARD.fen()
        )  # the current board, saveGameState will add this
        initialGame.append("-1")  # the current turn, w or b
        initialGame.append([])  # vote history
        initialGame.append([[], []])  # teams : [[w],[b]]

        # load into the EntireGame
        EntireGame["games"].append(initialGame)

        self._CACHED_GAME_OBJECT = EntireGame

        return

    def initiateGame(self):
        """
        This creates a new game and adds it to the _CACHED_GAME_OBJECT
        This is where users are discovered and the game is primed for votes.
        Note: this will be used for more than just the inital game state.
        """

        # this is most likely redundant but used for safety at the moment.
        if self._CACHED_GAME_OBJECT is None:
            with open(self._DATA_FILE, "r") as file:
                EntireGame = json.load(file)
                self._CACHED_GAME_OBJECT = EntireGame

        gamelist: list = self._CACHED_GAME_OBJECT["games"]  # most recent.
        # print(gamelist)
        gameid = len(gamelist)
        # board_str =
        turn = "w"
        voteHistory = []
        # teams = game[4]

        self._DECODED_BOARD = chess.Board()
        # gameBoard = self._DECODED_BOARD

        game = list()

        game.append(gameid)
        game.append("")  # game[1] is taken care of by saveGameState
        game.append(turn)
        game.append(voteHistory)
        game.append([[], []])  # teams

        # TODO: establish teams here
        if self._HARD_CODE_TESTING:
            white = ["ben", "donovan", "jonathan", "laween"]
            black = ["james", "judah", "ugi"]
        else:
            # this is where the code needs to find users in the home directory.
            # James: build teams here. it needs to in the end have two variables.
            # white and black. Use self._HOME_DIRECTORY so set where users are.
            # hOME directory
            pass

        # storing teams
        game[4][0] = white
        game[4][1] = black

        # ensure game object is updated
        self._CACHED_GAME_OBJECT["games"].append(game)

        return

    def saveGameState(self):
        gameBoard = self._DECODED_BOARD
        gameBoard_str = gameBoard.fen()

        game = self._CACHED_GAME_OBJECT["games"][-1]
        gameid = game[0]
        game[1] = gameBoard_str

        with open(self._DATA_FILE, "w") as file:
            json.dump(self._CACHED_GAME_OBJECT, file, indent=2)

        return

    def moveGameState(self):
        """
        (low priority) check for new users
        collect votes in
        move piece
        if game is over, start new one
        store
        """

        gameCachedIn = False

        if self._CACHED_GAME_OBJECT == None:
            gameCachedIn = True
            with open(self._DATA_FILE, "r") as file:
                EntireGame = json.load(file)
                self._CACHED_GAME_OBJECT = EntireGame

        # initialize any local variables
        move = str()
        game = self._CACHED_GAME_OBJECT["games"][-1]

        if gameCachedIn:
            self._DECODED_BOARD = chess.Board(game[1])

        # check for new users

        # collect votes
        if self._HARD_CODE_TESTING:
            move = self._simulateNextMove()
            move = chess.Move.from_uci(move)
        else:
            # Ugnius vote collecting logic here
            # logic of collecting votes here.
            pass

        # make the turn
        self._DECODED_BOARD.push(move)
        # add to vote history
        game[3].append(move.uci())

        # if game is over, start new one
        if self.BensFunction():  # True means game is over.
            # make sure the last board is saved properly and a new game is stared.
            game[1] = self._DECODED_BOARD.fen()
            self._CACHED_GAME_OBJECT["games"][game[0]] = game
            self.initiateGame()

        return

    def BensFunction(self) -> bool:
        """
        Ben, please rename this function but have it return true or false
        depending on if the game should be ended or not.
        """
        board: chess.Board = self._DECODED_BOARD

        return True

    def _simulateNextMove(self) -> str:
        """
        for testing pourposes, this will be run inside
        moveGameState() if _HARD_CODE_TESTING is true.

        this will take steps to make a move in the self._DECODED_BOARD
        """
        board: chess.Board = self._DECODED_BOARD

        moves = [move.uci() for move in board.legal_moves]

        return moves[randint(0, len(moves) - 1)]


def main():
    test_mode = False
    # check if the script is run with the test argument
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_mode = True

    # run the cron job with test mode parameter inplace, (note it will only be triggered if test_mode is true)
    cron = Cron(test_mode=test_mode)

    if cron.gameState() == "not initiated":
        cron.initiateGameFile()
        cron.initiateGame()
        cron.saveGameState()
    else:
        print("game is active")
        cron.moveGameState()
        cron.saveGameState()


if __name__ == "__main__":
    main()
