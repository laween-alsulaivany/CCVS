"""
This file contains the github configuration for the game. Please do not modify the GITHUB_TOKEN or the REPO_NAME.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# GitHub Integration Configuration

# GitHub Personal Access Token.
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Load token from environment

# GitHub repository name
REPO_NAME = "laween-alsulaivany/CCVS"

# Local file where the game state is stored.
GAME_STATE_FILE = "game_state.json"

# Time for the automated commit in 24-hour format (HH:MM).
COMMIT_TIME = "16:29"
