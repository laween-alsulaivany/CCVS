"""
This is the main entry point for the CCVS Data Persistence and GitHub Integration module.
This module is responsible for saving and loading the game state to and from a local file, as well as committing the game state to a GitHub repository.
"""

""" This is from 
kb8125mc@smoke:~$ chess
Traceback (most recent call last):
  File "/home/remote/kb8125mc/CCVS/src/main.py", line 8, in <module>
    import scheduler
  File "/home/remote/kb8125mc/CCVS/src/scheduler.py", line 12, in <module>
    from apscheduler.schedulers.background import BackgroundScheduler
ModuleNotFoundError: No module named 'apscheduler'
"""


# from src.data_persistence import save_game_state, load_game_state
# import scheduler
import github_integration as GHI




def main():
    print("Starting the Chess CLI...")

    data = GHI.getGameState()

    # handle the arguments
    
    
    


if __name__ == "__main__":
    main()
