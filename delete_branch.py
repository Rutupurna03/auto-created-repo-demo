from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")
repo_name = "auto-created-repo-demo"

if not token:
    raise Exception("❌ GITHUB_TOKEN missing")

g = Github(token)
repo = g.get_user().get_repo(repo_name)

branch_name = "automation-branch"

try:
    ref = repo.get_git_ref(f"heads/{branch_name}")
    ref.delete()
    print(f"✅ Branch '{branch_name}' deleted successfully!")
except Exception as e:
    print(f"⚠️ Unable to delete branch: {e}")
