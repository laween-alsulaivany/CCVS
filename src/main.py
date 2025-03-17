"""
This is the main entry point for the CCVS Data Persistence and GitHub Integration module.
This module is responsible for saving and loading the game state to and from a local file, as well as committing the game state to a GitHub repository.
"""


from src.data_persistence import save_game_state, load_game_state
import scheduler


def main():
    print("Starting CCVS Data Persistence and GitHub Integration module...")
    # Here we can perform any initial game state updates or operations that we might add later, this will be the file to run to start our chess service.
    # For now, we just start the scheduler.
    scheduler.start_scheduler()


if __name__ == "__main__":
    main()
