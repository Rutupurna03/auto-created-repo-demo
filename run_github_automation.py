from dotenv import load_dotenv
import os
from github import Github

# Load .env file
load_dotenv()

token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")

if not token:
    raise Exception("❌ GITHUB_TOKEN not found in .env or environment variables")

print(f"✅ Token loaded for user: {username}")

g = Github(token)

# Test GitHub login
user = g.get_user()
print("✅ GitHub login successful:", user.login)
