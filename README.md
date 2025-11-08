# GitHub Automation Framework

This repository contains automation scripts written in Python for performing various GitHub actions using the GitHub REST API.

## Features
- Create and delete repositories
- Create and close issues
- Create and merge pull requests
- Upload and commit files automatically
- End-to-end automation workflow (`run_github_automation.py`)

## Tech Stack
- **Language:** Python 3
- **Libraries:** `requests`, `os`, `dotenv`, `pytest`
- **Version Control:** Git & GitHub REST API

## Usage
1. Clone the repository.
2. Set up a `.env` file with your GitHub token (do **not** push it).
3. Run scripts using:
   ```bash
   python run_github_automation.py
