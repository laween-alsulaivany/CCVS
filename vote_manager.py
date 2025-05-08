import json
import traceback
from datetime import datetime
from collections import defaultdict, Counter
from github import Github
import os

class VoteManager:
    """
    VoteManager handles voting logic, stores votes to GitHub,
    and provides methods to cast, count, and finalize votes.
    """

    def __init__(self, github_token, repo_name, vote_file_path='votes.json'):
        """
        Initialize the VoteManager with GitHub credentials and file path.
        Loads existing votes if the file exists in the repo.
        """
        self.github = Github(github_token)
        self.repo = self.github.get_repo(repo_name)
        self.vote_file_path = vote_file_path
        self.votes = defaultdict(int)
        self.user_votes = {}
        self.load_votes()

    def load_votes(self):
        """
        Load vote data from the GitHub file if it exists.
        Initializes empty data if the file is not found or errors occur.
        """
        try:
            file_content = self.repo.get_contents(self.vote_file_path)
            data = json.loads(file_content.decoded_content.decode())
            self.votes = defaultdict(int, data.get("votes", {}))
            self.user_votes = data.get("user_votes", {})
        except Exception as e:
            print("Error loading votes:", e)
            traceback.print_exc()
            self.votes = defaultdict(int)
            self.user_votes = {}

    def save_votes(self):
        """
        Save the current voting state to the GitHub repo in JSON format.
        If the file does not exist, it will be created.
        """
        content = {
            "votes": dict(self.votes),
            "user_votes": self.user_votes,
            "timestamp": datetime.utcnow().isoformat()
        }

        try:
            file = self.repo.get_contents(self.vote_file_path)
            self.repo.update_file(
                self.vote_file_path,
                "Update votes",
                json.dumps(content, indent=2),
                file.sha
            )
        except Exception as e:
            print("Error saving votes:", e)
            traceback.print_exc()
            try:
                self.repo.create_file(
                    self.vote_file_path,
                    "Create vote file",
                    json.dumps(content, indent=2)
                )
            except Exception as e2:
                print("Error creating vote file:", e2)
                traceback.print_exc()

    def cast_vote(self, user_id, move):
        """
        Cast a vote for the given move by the user.
        Replaces previous vote if the user already voted.
        """
        if user_id in self.user_votes:
            old_move = self.user_votes[user_id]
            self.votes[old_move] -= 1

        self.user_votes[user_id] = move
        self.votes[move] += 1
        self.save_votes()

    def get_vote_results(self):
        """
        Return a list of all current votes in descending order of count.
        """
        return Counter(self.votes).most_common()

    def finalize_vote(self):
        """
        Determine the move with the most votes, clear the vote state, and save.
        Used typically at 5PM via cron job.
        """
        if not self.votes:
            return None, 0

        move, count = Counter(self.votes).most_common(1)[0]
        self.votes = defaultdict(int)
        self.user_votes = {}
        self.save_votes()

        return move, count
