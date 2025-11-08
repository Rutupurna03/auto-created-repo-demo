import os
import requests
from dotenv import load_dotenv
import random

load_dotenv()

def test_create_issue():
    token = os.getenv("GITHUB_TOKEN")
    username = os.getenv("GITHUB_USERNAME")

    repo_name = "qa-automation-test-repo"  # replace if your repo name is different
    issue_title = f"Automated Issue {random.randint(1000,9999)}"

    url = f"https://api.github.com/repos/{username}/{repo_name}/issues"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "title": issue_title,
        "body": "This issue was created automatically using Python."
    }

    response = requests.post(url, json=data, headers=headers)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 201, "Issue creation failed"

