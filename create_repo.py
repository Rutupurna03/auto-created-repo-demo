from dotenv import load_dotenv
import os
from github import Github

# Load .env file
load_dotenv()

token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")

if not token:
    raise Exception("❌ GITHUB_TOKEN not found!")

print(f"✅ Token loaded for GitHub user: {username}")

# Login to GitHub
g = Github(token)
user = g.get_user()

# Name of repo to create
repo_name = "auto-created-repo-demo"

# Create repo
try:
    repo = user.create_repo(repo_name)
    print(f"✅ Repository '{repo_name}' created successfully!")
except Exception as e:
    if "name already exists" in str(e):
        print(f"⚠️ Repo '{repo_name}' already exists!")
    else:
        print(f"❌ Error: {e}")
