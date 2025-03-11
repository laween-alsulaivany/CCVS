# Tasks

## Authentication

Determine the integration method (using OAuth2 protocols maybe).
Build a simple module that authenticates a user and validates if its a student account.

## Game Logic

Build the core classes (Board and Pieces) and game logic.
Render the board using Unicode (or something more visually friendly).
Document commands and how to vote/make moves (--help).

## Voting System Implementation

Create an API or command interface for vote submissions.
Write the logic to count votes and select the winning move.
Decide on a tie-break mechanism (maybe random selection).

## Team Management & User Activity

Choose between static and dynamic approach for teams (whether users will stay on the same team or switch to rebalance every day).
Implement a system to track the user activity and assign points based on participation (encourage activity).
save login times to check for “inactive after 48 hours” rule.

## Data Storage & GitHub Integration for Game Data

Create a module to commit game state at 4:29 to GitHub (we can use a library like PyGitHub )
Store game data in a JSON file or a database (like SQLite?).
Implement a system to restore game state from the last commit (for restoring after changing game state or maybe a crash).

## Statistics and Analytics Module

Create a module to track game statistics.
Implement a system to display user rankings and game statistics (turn number, team sizes, participation frequency).
Create a leaderboard to show the top players.
allow toggling of different stat panels (Optional).

## ACM LEGO Board Display ( OPTIONAL )

Create a module to display the game board using LEGO bricks.
Develop an API endpoint to output the current board state
Design a synchronization method and develop an API to output the current board state and update the the LEGO board.

## Documentation & Project Management and (TESTING?)

Writing unit tests
Documenting the codebase
