import os
import requests
from dotenv import load_dotenv
import random

load_dotenv()

def test_create_repo():
    token = os.getenv("GITHUB_TOKEN")
    username = os.getenv("GITHUB_USERNAME")

    repo_name = f"auto-test-repo-{random.randint(1000,9999)}"
    url = f"https://api.github.com/user/repos"

    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json"
    }

    data = {
        "name": repo_name,
        "private": False
    }

    response = requests.post(url, json=data, headers=headers)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 201, "Repository creation failed"
