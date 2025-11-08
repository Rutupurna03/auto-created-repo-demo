import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
g = Github(token)

repo_name = "auto-created-repo-demo"
repo = g.get_user().get_repo(repo_name)

branch_name = "automation-branch"
main_branch = repo.get_branch("main")

# Create branch
try:
    repo.create_git_ref(ref=f"refs/heads/{branch_name}", sha=main_branch.commit.sha)
    print(f"✅ Branch created: {branch_name}")
except:
    print(f"⚠️ Branch {branch_name} already exists")

file_path = "automation_file.txt"
content = "This file was added automatically using a Python automation script.\n"
commit_message = "Add automation file"

try:
    repo.create_file(file_path, commit_message, content, branch=branch_name)
    print(f"✅ File '{file_path}' created on branch '{branch_name}'")
except:
    print(f"⚠️ File already exists, updating instead")
    file = repo.get_contents(file_path, ref=branch_name)
    repo.update_file(file.path, commit_message, content, file.sha, branch=branch_name)

# Create Pull Request
pr = repo.create_pull(
    title="Automation PR from Python 🤖",
    body="This pull request was created automatically using Python.",
    head=branch_name,
    base="main"
)

print(f"✅ Pull Request created: {pr.html_url}")
