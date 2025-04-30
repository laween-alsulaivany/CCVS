import json
import traceback
from datetime import datetime
from collections import defaultdict, Counter
from github import Github, Repository
from typing import Dict, Tuple, Optional


def load_votes(repo: Repository.Repository, vote_file_path: str) -> Tuple[Dict[str, int], Dict[str, str]]:
    """
    Loads votes and user vote records from a GitHub repository file.

    Args:
        repo (Repository): The GitHub repository object.
        vote_file_path (str): The path to the vote file in the repository.

    Returns:
        Tuple[Dict[str, int], Dict[str, str]]: A tuple containing the vote count per move and user votes.
    """
    try:
        file_content = repo.get_contents(vote_file_path)
        data = json.loads(file_content.decoded_content.decode())
        votes = defaultdict(int, data.get("votes", {}))
        user_votes = data.get("user_votes", {})
        return votes, user_votes
    except Exception as e:
        print("Error loading votes:", e)
        traceback.print_exc()
        return defaultdict(int), {}


def save_votes(repo: Repository.Repository, vote_file_path: str, votes: Dict[str, int], user_votes: Dict[str, str]) -> None:
    """
    Saves the current votes and user vote records to a GitHub repository file.

    Args:
        repo (Repository): The GitHub repository object.
        vote_file_path (str): The path to the vote file in the repository.
        votes (Dict[str, int]): The vote counts per move.
        user_votes (Dict[str, str]): The record of each user's selected move.
    """
    content = {
        "votes": votes,
        "user_votes": user_votes,
        "timestamp": datetime.utcnow().isoformat()
    }

    try:
        file = repo.get_contents(vote_file_path)
        repo.update_file(vote_file_path, "Update votes", json.dumps(content, indent=2), file.sha)
    except Exception as e:
        print("Error saving votes:", e)
        traceback.print_exc()
        try:
            repo.create_file(vote_file_path, "Create vote file", json.dumps(content, indent=2))
        except Exception as e2:
            print("Error creating vote file:", e2)
            traceback.print_exc()


def cast_vote(user_id: str, move: str, votes: Dict[str, int], user_votes: Dict[str, str]) -> None:
    """
    Registers or updates a vote by a user for a specific move.

    Args:
        user_id (str): The unique identifier for the user.
        move (str): The chess move voted for (e.g., "e2e4").
        votes (Dict[str, int]): The current vote tallies.
        user_votes (Dict[str, str]): The record of which user voted for which move.
    """
    if user_id in user_votes:
        old_move = user_votes[user_id]
        votes[old_move] -= 1

    user_votes[user_id] = move
    votes[move] += 1


def get_vote_results(votes: Dict[str, int]) -> list[Tuple[str, int]]:
    """
    Returns the sorted list of vote results.

    Args:
        votes (Dict[str, int]): The vote counts per move.

    Returns:
        list[Tuple[str, int]]: A sorted list of (move, vote count) tuples.
    """
    return Counter(votes).most_common()


def finalize_vote(votes: Dict[str, int], user_votes: Dict[str, str]) -> Tuple[Optional[str], int]:
    """
    Finalizes the vote by selecting the most-voted move and resetting vote state.

    Args:
        votes (Dict[str, int]): The vote counts per move.
        user_votes (Dict[str, str]): The user vote records.

    Returns:
        Tuple[Optional[str], int]: The winning move and its vote count. Returns (None, 0) if no votes.
    """
    if not votes:
        return None, 0

    move, count = Counter(votes).most_common(1)[0]
    votes.clear()
    user_votes.clear()
    return move, count
