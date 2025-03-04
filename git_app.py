# Install dependencies with:
# pip install python-jwt requests python-dotenv

import os
import jwt  # pip install python-jwt
import time
import requests  # pip install requests
from dotenv import load_dotenv  # pip install python-dotenv

# Load environment variables from .env
load_dotenv()

GITHUB_APP_ID = os.getenv("GITHUB_APP_ID")
GITHUB_PRIVATE_KEY_PATH = os.getenv("GITHUB_PRIVATE_KEY_PATH")
GITHUB_INSTALLATION_ID = os.getenv("GITHUB_INSTALLATION_ID")
GITHUB_API_URL = "https://api.github.com"

# Function to generate JWT for GitHub App authentication
def generate_jwt():
    with open(GITHUB_PRIVATE_KEY_PATH, "r") as key_file:
        private_key = key_file.read()

    payload = {
        "iat": int(time.time()),  # Issued at time
        "exp": int(time.time()) + 600,  # Expiration time (max 10 min)clear
        "iss": GITHUB_APP_ID,  # GitHub App ID
    }

    return jwt.encode(payload, private_key, algorithm="RS256")

# Function to get an installation access token
def get_installation_token():
    jwt_token = generate_jwt()
    print(f"Generated JWT Token: {jwt_token}")  # Debugging line
    url = f"{GITHUB_API_URL}/app/installations/{GITHUB_INSTALLATION_ID}/access_tokens"
    headers = {
        "Authorization": f"Bearer {jwt_token}",
        "Accept": "application/vnd.github+json",
    }
    response = requests.post(url, headers=headers)
    response.raise_for_status()  # Raise error if request fails
    return response.json()["token"]

# Function to list issues from a repository
def list_issues(owner, repo):
    token = get_installation_token()
    url = f"{GITHUB_API_URL}/repos/{owner}/{repo}/issues"
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    issues = response.json()

    print(f"Issues in {owner}/{repo}:")
    for issue in issues:
        print(f"- {issue['title']} ({issue['html_url']})")

if __name__ == "__main__":
    list_issues("your_github_username", "your_repository")
