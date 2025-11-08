import os
from github import Github
from dotenv import load_dotenv

load_dotenv()

token = os.getenv("GITHUB_TOKEN")
username = os.getenv("GITHUB_USERNAME")

g = Github(token)
repo = g.get_user().get_repo("auto-created-repo-demo")

local_file = "sample_upload.txt"
remote_file = "uploaded/sample_upload.txt"

with open(local_file, "r") as f:
    content = f.read()

try:
    file = repo.get_contents(remote_file)
    repo.update_file(remote_file, "Updating file via Python", content, file.sha)
    print("✅ File updated successfully")
except:
    repo.create_file(remote_file, "Uploading file via Python", content)
    print("✅ File uploaded successfully")
