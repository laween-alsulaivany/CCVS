"""
This module contains functions to commit the game state file to a GitHub repository.
This will commit the game state file to the specified branch in the repository. the current branch is development.
"""


import os
from github import Github, Auth


def commit_game_state_to_github(token: str, repo_name: str, file_path: str, commit_message: str = "Update game state", branch: str = "development") -> None:
    """
    Commits the game state file to the specified GitHub repository and branch.

    Parameters:
        token (str): GitHub personal access token.
        repo_name (str): Repository name in the format "username/repo".
        file_path (str): The local path to the game state file.
        commit_message (str): Commit message.
        branch (str): Branch to commit to, default is "development".
    """
    # Initialize the GitHub object
    # g = Github(token) # DEPRECATED: DO NOT USE THIS
    g = Github(auth=Auth.Token(token))

    # Get the repository
    repo = g.get_repo(repo_name)

    # Read the content of the local file
    with open(file_path, "r") as f:
        file_content = f.read()

    try:
        # Get the file contents from the specified branch
        contents = repo.get_contents(file_path, ref=branch)

        # Update the file in the correct branch
        repo.update_file(contents.path, commit_message,
                         file_content, contents.sha, branch=branch)
        print(f"✅ Updated {file_path} in branch {branch}.")

    except Exception as e:
        print(f"⚠️ File not found in branch {branch}; creating a new file.")

        # Create the file in the specified branch
        repo.create_file(file_path, commit_message,
                         file_content, branch=branch)
        print(f"✅ Created {file_path} in branch {branch}.")
