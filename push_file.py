import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")

if not token or not username:
    print("❌ Environment variables not loaded. Set GITHUB_TOKEN and GITHUB_USERNAME.")
    exit()

print(f"✅ Token loaded for GitHub user: {username}")

g = Github(token)
repo_name = "auto-created-repo-demo"

try:
    repo = g.get_user().get_repo(repo_name)
    print(f"📂 Connected to repository: {repo_name}")
except:
    print(f"❌ Repository {repo_name} not found!")
    exit()

file_path = "auto_file.txt"
commit_message = "Auto commit from Python script"
file_content = "This is an auto-generated file.\nHello GitHub Automation!"

try:
    file = repo.get_contents(file_path)
    repo.update_file(file_path, commit_message, file_content, file.sha)
    print(f"✅ Updated existing file: {file_path}")
except:
    repo.create_file(file_path, commit_message, file_content)
    print(f"✅ Created new file: {file_path}")
