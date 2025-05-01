#!/bin/bash

THE_DIR="/home/chess/CCVS"
# dynamic path to the repo branch
CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

cd $THE_DIR




# checking for the files to pull
echo "Checking for files to pull"
git fetch origin

# get a list of the changed filees
CHANGED_FILES=$(git diff --name-only $CURRENT_BRANCH..origin/$CURRENT_BRANCH)
# TODO: pick the newer json file version
SAFE_PATTERNS=(
  "data/"
  "data/gameState.json" 
  "data/game_state.json"
)

# empty list to put the unsafe files in it
UNSAFE_FILES=()

# if only the files in data/ are changed, we can pull the changes
# otherwise, we contact IT
for FILE in $CHANGED_FILES; do
  IS_SAFE=0
  for PATTERN in "${SAFE_PATTERNS[@]}"; do
    if [[ "$FILE" == $PATTERN || "$FILE" == $PATTERN* ]]; then
      IS_SAFE=1
      break
    fi
  done
  IS_SAFE=0 
  if [ $IS_SAFE -eq 0 ]; then
    UNSAFE_FILES+=("$FILE")
  fi
done

if [ ${#UNSAFE_FILES[@]} -gt 0 ]; then
  echo "WARNING: These files would be overwritten by this pull:" >&2
  printf "  %s\n" "${UNSAFE_FILES[@]}" >&2
  echo "Aborting the git pull for security. Please notify the IT department." >&2
  # Maybe email IT
  mail -s "Git Security Alert" laweenhamza@gmail.com <<< "Unsafe files detected in CCVS repo" # FIXME: change this to IT email
  mail -s "Git Security Alert" judahnava02@gmail.com <<< "Unsafe files detected in CCVS repo" # FIXME: change this to IT email
  exit 1
  else
    # if we are here, it means that the files are safe to pull
    echo "No unsafe files detected. Updating the database."
    git pull origin $CURRENT_BRANCH
fi



cd src



$THE_DIR/.chessPython/bin/python3 cron.py


# After running the cron job, we commit and push the gamestate
cd $THE_DIR
git add data/
git commit -m "Auto-update game state $(date '+%Y-%m-%d %H:%M:%S')"
git push origin $CURRENT_BRANCH

echo "Cron job completed successfully at $(date)"
