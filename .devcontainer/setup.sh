#!/usr/bin/env bash
set -e
echo "i am $(whoami)"

GREEN=$(tput setaf 2)
RED=$(tput setaf 1)
RESET=$(tput sgr0)
YELLOW=$(tput setaf 3)

# Function to handle errors
function handle_error {
  echo "${RED}ERROR: $1${RESET}" >&2
  exit 1
}

echo "${GREEN}Starting setup...${RESET}"

# Check required environment variables
[ -z "$GIT_USER" ] && handle_error "GIT_USER is not set"
[ -z "$GIT_EMAIL" ] && handle_error "GIT_EMAIL is not set"
[ -z "$GIT_TOKEN" ] && handle_error "GIT_TOKEN is not set"
[ -z "$GIT_REMOTE" ] && handle_error "GIT_REMOTE is not set"

# Install Node.js LTS
# echo "Installing Node.js LTS..."
# curl -fsSL https://deb.nodesource.com/setup_lts.x | sudo -E bash - || handle_error "Failed to set up Node.js repository"
# sudo apt-get install -y nodejs || handle_error "Failed to install Node.js"

echo "Node.js version: $(node -v)"

#echo "Installing uv (Astral CLI)..."
#curl -LsSf https://astral.sh/uv/install.sh | sh || handle_error "Failed to install uv"

# Configure Git (current repo only)
git config user.name "$GIT_USER" || handle_error "Failed to set Git user.name"
git config user.email "$GIT_EMAIL" || handle_error "Failed to set Git user.email"

# Build HTTPS remote URL with token
REMOTE_WITH_TOKEN=$(echo "$GIT_REMOTE" | sed -E "s#https://#https://$GIT_USER:$GIT_TOKEN@#")

# Add or update remote safely
if git remote get-url origin >/dev/null 2>&1; then
    echo "${YELLOW}Remote 'origin' already exists, updating URL...${RESET}"
    git remote set-url origin "$REMOTE_WITH_TOKEN" || handle_error "Failed to update Git remote origin"
else
    git remote add origin "$REMOTE_WITH_TOKEN" || handle_error "Failed to add Git remote origin"
fi


# Show configuration
echo "Git configuration for current repository:"
echo "User: $(git config user.name) <$(git config user.email)>"
echo "Remote origin: $(git remote get-url origin)"

# install requirements.txt
echo "Installing Python dependencies from requirements.txt..."
pip install --no-cache-dir -r /workspaces/supervisor-pattern/requirements.txt || handle_error "Failed to install Python dependencies"

echo

echo "${GREEN}
  __ _   _  ___ ___ ___  ___ ___ 
/ __| | | |/ __/ __/ _ \/ __/ __|
\__ \ |_| | (_| (_|  __/\__ \__ \ 
|___/\__,_|\___\___\___||___/___/ 

${RESET}
"
exit 0