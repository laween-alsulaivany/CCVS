"""
Module to handle the APScheduler for scheduling the commit job. 

I used APScheduler to schedule the commit job to run daily at a specific time. 
The start_scheduler function starts the scheduler and keeps the script running until it is interrupted.
The scheduled_commit function commits the game state to GitHub using the github_integration module. 


"""


from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import time
import github_integration
import config
import subprocess

# Get the current branch name


def get_current_branch():
    result = subprocess.run(
        ["git", "branch", "--show-current"], capture_output=True, text=True)
    return result.stdout.strip() if result.returncode == 0 else "development"


# Assign the current branch to the variable. default is "development"
branch = get_current_branch()


def scheduled_commit():
    """
    Function to be run by the scheduler to commit the game state to GitHub.
    """
    print(f"Running scheduled commit at {datetime.now()}...")
    try:
        github_integration.commit_game_state_to_github(
            token=config.GITHUB_TOKEN,
            repo_name=config.REPO_NAME,
            file_path=config.GAME_STATE_FILE,
            commit_message="Automated commit of game state",
            branch=branch
        )
    except Exception as e:
        print(f"Error during scheduled commit: {e}")


def start_scheduler():
    """
    Starts the APScheduler to run the commit job daily.
    """
    scheduler = BackgroundScheduler()
    # Parse commit time from configuration (format "HH:MM")
    hour, minute = map(int, config.COMMIT_TIME.split(":"))
    scheduler.add_job(scheduled_commit, 'cron', hour=hour, minute=minute)
    scheduler.start()
    print("Scheduler started. Press Ctrl+C to exit.")

    try:
        # Keep the script running.
        while True:
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
        print("Scheduler stopped.")
