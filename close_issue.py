from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")

if not token:
    raise Exception("❌ GitHub token missing!")

g = Github(token)
repo_name = "auto-created-repo-demo"  # Change if needed

repo = g.get_user().get_repo(repo_name)

# Find last open issue
issues = repo.get_issues(state="open")

if issues.totalCount == 0:
    print("⚠️ No open issues to close!")
else:
    issue = issues[0]
    issue.edit(state="closed")
    print(f"✅ Closed issue: {issue.title}")
    print(f"🔗 {issue.html_url}")
