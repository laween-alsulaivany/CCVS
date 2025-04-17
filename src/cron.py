from datetime import datetime
from pathlib import Path
import data_persistence as DP
import chess


def get_votes():
    pass

def get_selected():
    pass

def tally_participation():
    pass

def main():
    pass

def go_to_data_dir() -> Path:

    current_dir = Path.cwd()

    data_dir = current_dir.parent / 'data'

    if not data_dir.exists():
        #TODO: make a condition if this does not work.
        exit(1)
    else:
        return data_dir

def output_to_test(data_dir: Path, data: str):
    with open(data_dir / "test.txt", 'a') as file:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        file.write("This is a test." + timestamp + '\n')
        file.write(data+"\n\n")
def find_vote_json_in_home():
    home_base = Path("/home")
    existing = []

    for user_dir in home_base.iterdir():
        if user_dir.is_dir():
            vote_file = user_dir/ ".vote.json"
            if vote_file.exists():
                existing.append(str(vote_file))
    return existing


if __name__ == "__main__":
    data_dir = go_to_data_dir()
    # output_to_test(data_dir)
    votes = find_vote_json_in_home()
    votes_str = "\n".join(votes)
    output_to_test(data_dir, votes_str)
    
    
