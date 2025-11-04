#!/usr/bin/env bash
set -e
echo "Running setup as user: $(whoami)"

GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
RESET=$(tput sgr0)
YELLOW=$(tput setaf 3)

function handle_error {
  echo "${RED}ERROR: $1${RESET}" >&2
  exit 1
}

echo "${GREEN}Starting setup...${RESET}"

[ -z "$GIT_USER" ] && handle_error "GIT_USER is not set"
[ -z "$GIT_EMAIL" ] && handle_error "GIT_EMAIL is not set"
[ -z "$GIT_TOKEN" ] && handle_error "GIT_TOKEN is not set"
[ -z "$GIT_REMOTE" ] && handle_error "GIT_REMOTE is not set"

git config --global user.name "$GIT_USER" || handle_error "Failed to set Git user.name"
git config --global user.email "$GIT_EMAIL" || handle_error "Failed to set Git user.email"
git config --global credential.helper store || handle_error "Failed to set Git credential helper"
git config --global pull.rebase false

CREDENTIALS_FILE="$HOME/.git-credentials"
echo "https://$GIT_USER:$GIT_TOKEN@github.com" > "$CREDENTIALS_FILE" || handle_error "Failed to store Git credentials"
chmod 600 "$CREDENTIALS_FILE" || handle_error "Failed to set permissions on credentials file"

REMOTE_WITH_TOKEN=$(echo "$GIT_REMOTE" | sed -E "s#https://#https://$GIT_USER:$GIT_TOKEN@#")

if git remote get-url origin >/dev/null 2>&1; then
    echo "${YELLOW}Remote 'origin' already exists, updating URL...${RESET}"
    git remote set-url origin "$REMOTE_WITH_TOKEN" || handle_error "Failed to update Git remote origin"
else
    git remote add origin "$REMOTE_WITH_TOKEN" || handle_error "Failed to add Git remote origin"
fi

echo "Git configuration:"
echo "  user.name:  $(git config --global user.name)"
echo "  user.email: $(git config --global user.email)"
echo "  origin:     $(git remote get-url origin)"

if [ -f requirements.txt ]; then
  echo "Installing Python dependencies from requirements.txt..."
  pip install --no-cache-dir -r requirements.txt || handle_error "Failed to install Python dependencies"
else
  echo "${YELLOW}requirements.txt not found, skipping pip install.${RESET}"
fi


echo

echo "${GREEN}
  __ _   _  ___ ___ ___  ___ ___ 
/ __| | | |/ __/ __/ _ \/ __/ __|
\__ \ |_| | (_| (_|  __/\__ \__ \ 
|___/\__,_|\___\___\___||___/___/ 

${RESET}
"
exit 0