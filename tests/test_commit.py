"""
You can use the following test to commit the game state to the GitHub repository. Try it, it's fun!

"""

import subprocess
from src import github_integration
from src import config

# Again, get branch name


def get_current_branch():
    result = subprocess.run(
        ["git", "branch", "--show-current"], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else "development"


# assign it
branch = get_current_branch()

# push it baby
github_integration.commit_game_state_to_github(
    token=config.GITHUB_TOKEN,
    repo_name=config.REPO_NAME,
    file_path=config.GAME_STATE_FILE,
    commit_message="Test commit of game state",
    branch=branch
)
