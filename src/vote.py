import json
from datetime import datetime
from collections import defaultdict, Counter
from github import Github
import os

class VoteManager:
    def __init__(self, github_token, repo_name, vote_file_path='votes.json'):
        self.github = Github(github_token)
        self.repo = self.github.get_repo(repo_name)
        self.vote_file_path = vote_file_path
        self.votes = defaultdict(int)
        self.user_votes = {}
        self.load_votes()

    def load_votes(self):
        try:
            file_content = self.repo.get_contents(self.vote_file_path)
            data = json.loads(file_content.decoded_content.decode())
            self.votes = defaultdict(int, data.get("votes", {}))
            self.user_votes = data.get("user_votes", {})
        except Exception:
            self.votes = defaultdict(int)
            self.user_votes = {}

    def save_votes(self):
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
        except Exception:
            self.repo.create_file(
                self.vote_file_path,
                "Create vote file",
                json.dumps(content, indent=2)
            )

    def cast_vote(self, user_id, move):
        if user_id in self.user_votes:
            old_move = self.user_votes[user_id]
            self.votes[old_move] -= 1

        self.user_votes[user_id] = move
        self.votes[move] += 1
        self.save_votes()

    def get_vote_results(self):
        return Counter(self.votes).most_common()

    def finalize_vote(self):
        if not self.votes:
            return None, 0

        move, count = Counter(self.votes).most_common(1)[0]

        # Reset for next turn
        self.votes = defaultdict(int)
        self.user_votes = {}
        self.save_votes()

        return move, count
