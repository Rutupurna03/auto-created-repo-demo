import os
import requests
import random

def test_close_issue():
    token = os.getenv("GITHUB_TOKEN")
    username = os.getenv("GITHUB_USERNAME")
    repo_name = "qa-automation-test-repo"

    # Step 1: Create an issue to close
    issue_title = f"Temporary Issue {random.randint(1000,9999)}"
    create_url = f"https://api.github.com/repos/{username}/{repo_name}/issues"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    data = {"title": issue_title}
    create_response = requests.post(create_url, json=data, headers=headers)
    print("Create Issue Response:", create_response.json())

    assert create_response.status_code == 201, "Failed to create issue for closing test"
    issue_number = create_response.json()["number"]

    # Step 2: Close the created issue
    close_url = f"https://api.github.com/repos/{username}/{repo_name}/issues/{issue_number}"
    close_data = {"state": "closed"}

    close_response = requests.patch(close_url, json=close_data, headers=headers)
    print("Close Issue Response:", close_response.json())

    assert close_response.status_code == 200, "Issue closing failed"
