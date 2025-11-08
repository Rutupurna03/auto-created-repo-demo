from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")

if not token:
    raise Exception("❌ GITHUB_TOKEN is missing")

repo_name = "auto-created-repo-demo"

g = Github(token)
repo = g.get_user().get_repo(repo_name)

pulls = repo.get_pulls(state='open')

if pulls.totalCount == 0:
    print("❌ No open pull requests to merge")
    exit()

pr = pulls[0]  # merge first PR
print(f"🔎 Found PR #{pr.number}: {pr.title}")

try:
    merge_result = pr.merge()
    if merge_result.merged:
        print(f"✅ PR #{pr.number} merged successfully!")
    else:
        print(f"⚠️ PR not merged: {merge_result.message}")
except Exception as e:
    print(f"❌ Error merging PR: {e}")
