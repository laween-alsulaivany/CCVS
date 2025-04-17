# CCVS
The Collaborative Chess Voting System (CCVS) is a web-based application designed to facilitate an asynchronous, team-based chess competition within an academic environment. Implemented at Minnesota State University Moorhead (MSUM), this system demonstrates key concepts in distributed decision-making and collaborative gaming systems.

## Install Instructions

### Install to system
```
# in dedicated chess account of system

sudo make python_instance

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
