# VoteManager - Chess Plug Voting System

This Python module implements a team-based voting system for a collaborative chess game environment.
It is designed for integration into the Chess Plug project hosted at MSUM, storing votes via GitHub
and finalizing them on a scheduled basis (e.g., 5 PM daily).

## Features

- Tracks individual user votes and total vote counts per move
- Ensures one vote per user per turn
- Stores voting data in a JSON file (`votes.json`) pushed to a GitHub repository
- Supports vote finalization (winning move selection + vote reset)
- Includes exception logging for reliability and debugging

## Setup

1. Install required library:
```bash
pip install PyGithub
```

2. Ensure your environment has a GitHub access token:
```bash
export GITHUB_TOKEN=your_token_here
```

## Usage Example

```python
from vote_manager import VoteManager
import os

github_token = os.environ["GITHUB_TOKEN"]
repo_name = "your-username/your-repo"

vm = VoteManager(github_token, repo_name)

# Cast a vote
vm.cast_vote("student123", "e2e4")

# Check current standings
print(vm.get_vote_results())

# Finalize the current vote (used by cron job)
move, count = vm.finalize_vote()
print(f"Move selected: {move} with {count} votes")
```

## Cron Integration (Linux)

To finalize votes every day at 5 PM, add to crontab:
```bash
0 17 * * * /usr/bin/python3 /path/to/finalize_vote.py
```

## Repository Structure

- `vote_manager.py`: Core class for managing votes
- `votes.json`: GitHub-hosted JSON file with current voting data
- `finalize_vote.py`: (optional) Script to finalize votes and apply move

## License

This module is developed as part of the Chess Plug project for educational purposes.
