<<<<<<< HEAD
from datetime import datetime
from pathlib import Path
import data_persistence as DP
import chess



def go_to_data_dir() -> Path:

    current_dir = Path.cwd()

    data_dir = current_dir.parent / 'data'

    if not data_dir.exists():
        #TODO: make a condition if this does not work.
        exit(1)
    else:
        return data_dir

def output_to_test(data_dir: Path):
    with open(data_dir / "test.txt", 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file.write("This is a test." + timestamp + '\n')

if __name__ == "__main__":
    data_dir = go_to_data_dir()
    output_to_test(data_dir) 
    

def get_votes():
    pass

def get_selected():
    pass

def tally_participation():
    pass

def main():
    pass
>>>>>>> 65869968cb0362ba5031d18f6543805ab4f7954d
