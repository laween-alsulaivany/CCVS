# CCVS
The Collaborative Chess Voting System (CCVS) is a web-based application designed to facilitate an asynchronous, team-based chess competition within an academic environment. Implemented at Minnesota State University Moorhead (MSUM), this system demonstrates key concepts in distributed decision-making and collaborative gaming systems.

## Install Instructions

- **(Recommended) Make a separate chess account that only allows one log in at a time.**

### Install to system

# Step 1 – Install system dependencies (run once with sudo)
sudo make python-deps

# Step 2 – Set up user-local Python environment
make python_instance

# Step 3 – Register cron jobs and install chess command
make cron install
sudo make chess_install

```

## To Uninstall
```
#in account where chess was installed

make cron uninstall

sudo make chess_uninstall

rm -r ~/CCVS/.chessPython

```
