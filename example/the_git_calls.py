from github import Github
from pathlib import Path
import git
import os

class Example:

    def __init__(self):
        self.GITHUB_TOKEN = self.getGitToken()
        self.REPO_NAME = 'laween-alsulaivany/CCVS'
        self.BRANCH_NAME = 'example'
        self.REPO_DIR = self.get_parent_directory()
        self.FILE_PATH = 'data/example.txt'
        self.COMMIT_MESSAGE = "From API, data/example.txt update"


    def theCron(self):
        self.g = Github(self.GITHUB_TOKEN)
        repo = self.g.get_repo(self.REPO_NAME)
    
        repo = self.g.Repo

    def get_parent_directory():
        """Returns a Path object of the parent directory of the current script."""
        return Path(__file__).resolve().parent.parent

    def getGitToken(self):
        return self.read_env_var()

    def read_env_var(self, key, env_file='../.env'):
        """Reads a value from a .env file located one directory above."""
        if not os.path.exists(env_file):
            raise FileNotFoundError(f"{env_file} not found")

        with open(env_file, 'r') as file:
            for line in file:
                # Remove whitespace and ignore comments/empty lines
                line = line.strip()
                if not line or line.startswith('#'):
                    continue
                if '=' in line:
                    k, v = line.split('=', 1)
                    if k.strip() == key:
                        return v.strip().strip('"').strip("'")
        
        raise KeyError(f"{key} not found in {env_file}")
