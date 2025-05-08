

from typing import Literal, Any, List
from pathlib import Path
import json  
import chess
from random import randint
import sys  
import random
from collections import Counter
import os


class Cron:
    # absolute path to ../data/gameState.json, regardless of CWD
    _DATA_FILE = (
        Path(__file__)  # e.g. /…/project/src/cron.py
        .resolve()  # make it absolute
        .parent.parent  # => /…/project/src  # => /…/project
        / "data"
        / "gameState.json"
    )

    #_CACHED_GAME_OBJECT = None  # this will jump the object around to prevent
                                # constand reloading of the json file

    #_DECODED_BOARD = chess.Board()  # This is just the bord as a chess.Board()

    _HARD_CODE_TESTING = (
        True  # if true, this will put specific users in teams for testing.
    )

    _HOME_DIRECTORY = None  # This needs to be overwritten by the make cron install

    def __init__(self, test_mode: bool = False):
        self._HARD_CODE_TESTING = test_mode

        if self._HOME_DIRECTORY is None:
            remote = Path("/home/remote")
            self._HOME_DIRECTORY = remote if remote.exists() else Path
