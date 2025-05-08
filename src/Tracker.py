import random

class ParticipationTracker:
    """Tracks player participation and team statistics in a voting-based chess game."""

    def __init__(self):
        self.players = {}  # Stores player stats as {player_id: {"votes": int, "selected": int}}
        self.teams = {}  # Stores teams as {team_id: [player_ids]}

    def record_vote(self, player_id, team_id, was_selected=False):
        """Records a vote for a player and updates statistics."""
        if player_id not in self.players:
            self.players[player_id] = {"votes": 0, "selected": 0}
        
        self.players[player_id]["votes"] += 1
        if was_selected:
            self.players[player_id]["selected"] += 1

        if team_id not in self.teams:
            self.teams[team_id] = []
        if player_id not in self.teams[team_id]:
            self.teams[team_id].append(player_id)

    def get_player_stats(self, player_id):
        """Returns the statistics for a given player."""
        return self.players.get(player_id, {"votes": 0, "selected": 0})

    def get_team_average(self, team_id):
        """Calculates and returns the average participation for a team."""
        if team_id not in self.teams or not self.teams[team_id]:
            return {"average_votes": 0.00, "average_selected": 0.00}
        
        total_votes = sum(self.players[p]["votes"] for p in self.teams[team_id])
        total_selected = sum(self.players[p]["selected"] for p in self.teams[team_id])
        player_count = len(self.teams[team_id])

        return {
            "average_votes": round(total_votes / player_count, 2),
            "average_selected": round(total_selected / player_count, 2),
        }

    def generate_leaderboard(self, team_id):
        """Generates a leaderboard sorted by highest participation, then selection, then ID."""
        if team_id not in self.teams:
            return []
        sorted_players = sorted(
            self.teams[team_id],
            key=lambda p: (-self.players[p]["votes"], -self.players[p]["selected"], p)
        )
        return [self.players[p] | {"player_id": p} for p in sorted_players]


def test_participation_tracker():
    """Simulates a chess voting game with random participation."""
    tracker = ParticipationTracker()
    
    # Generate random number of players (between 10 and 20) and split into two teams
    num_players = random.randint(10, 20)
    players = [f"player{i}" for i in range(1, num_players + 1)]
    random.shuffle(players)
    mid = (len(players) + 1) // 2  # Ensures near-equal split, handles odd number of players
    team_white = players[:mid]
    team_black = players[mid:]
    
    for player in team_white:
        tracker.teams.setdefault("WHITE", []).append(player)
    for player in team_black:
        tracker.teams.setdefault("BLACK", []).append(player)
    
    # Simulate 50 turns of voting with more erratic participation
    for _ in range(50):
        for player in players:
            if random.random() < random.uniform(0.1, 0.9):  # More erratic voting chance
                team = "WHITE" if player in team_white else "BLACK"
                was_selected = random.choices([True, False], weights=[30, 70])[0]  # 30% chance of selection
                tracker.record_vote(player, team, was_selected)
    
    # Print results
    print("\nTeam WHITE:")
    print("--------------------------------")
    for entry in tracker.generate_leaderboard("WHITE"):
        print(f"{entry['player_id']}: Votes = {entry['votes']}, Selected = {entry['selected']}")
    
    print("\nTeam BLACK:")
    print("--------------------------------")
    for entry in tracker.generate_leaderboard("BLACK"):
        print(f"{entry['player_id']}: Votes = {entry['votes']}, Selected = {entry['selected']}")
    
    print("\nTeam Averages:")
    print(f"WHITE: {tracker.get_team_average('WHITE')}")
    print(f"BLACK: {tracker.get_team_average('BLACK')}")


if __name__ == "__main__":
    test_participation_tracker()
