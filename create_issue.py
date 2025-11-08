import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

g = Github(token)
repo = g.get_user().get_repo("auto-created-repo-demo")

issue_title = "Automated Issue from Python 🤖"
issue_body = "This issue was created automatically using a Python script."

issue = repo.create_issue(title=issue_title, body=issue_body)

print(f"✅ Issue created: {issue.html_url}")
