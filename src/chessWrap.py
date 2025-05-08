# A class that makes the chess game an object
from pathlib import Path
import chess



class chessW:


    def __init__(self, jsonFile: Path):
        """
            by default, the class initially loads file and
            sets current game. 
            If this is running for the first time, it will
            create the file and load in the first game.
        """
        # instance variables
        self._jsonFile = jsonFile
        self._firstTime = False
        self._currentGame = None

        if not self._jsonFile.exists():
            self.initFile()
            self.initGame1()
            self._firstTime = True
        else:
            self.loadFile()

        self.setCurrentGame()
        return

    # Managing Commands

    def initFile(self):
        # this is called once and creates the file.
        return

    def initGame1(self):
        return

    def saveAndClose(self):
        return
    
    def setCurrentGame(self):
        return
    
    def loadFile(self):
        return
    
    # checking functions

    def firstTime(self) -> bool:
        # returns if game is running for first time
        return self._firstTime
    



    # Getters



    # Setters
    

if __name__ == "__main__":
    #prime json file for testing
    file = (
        Path(__file__)
        .resolve()
        .parent.parent
        / "tests"
        / "test.json"
    )
    if file.exists():
        file.unlink() # deletes file
    
    game = chessW(file) 

    assert game.firstTime() is True


