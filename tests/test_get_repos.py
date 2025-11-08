import os
import requests
from dotenv import load_dotenv

load_dotenv()

def test_get_repos():
    url = "https://api.github.com/user/repos"
    token = os.getenv("GITHUB_TOKEN")

    headers = {"Authorization": f"token {token}"}
    response = requests.get(url, headers=headers)

    print("Status Code:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200, "Failed to fetch repositories"
