# CCVS
The Collaborative Chess Voting System (CCVS) is a web-based application designed to facilitate an asynchronous, team-based chess competition within an academic environment. Implemented at Minnesota State University Moorhead (MSUM), this system demonstrates key concepts in distributed decision-making and collaborative gaming systems.

## Install Instructions

- **(Recommended) Make a separate chess account that only allows one log in at a time.**

### Install to system
```
# Two sudo commands are needed to install apt dependancies and to put chess command in /usr/bin
sudo make python-deps
sudo make chess_install

make python_instance
make cron install

```

## To Uninstall
```
#in account where chess was installed

make cron uninstall

sudo make chess_uninstall

rm -r ~/CCVS/.chessPython

```
