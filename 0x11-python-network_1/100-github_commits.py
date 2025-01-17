#!/usr/bin/python3
"""script that displays the last 10 commits from a GitHub repository."""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Usage: {sys.argv[0]} <repo> <owner>")
        sys.exit(1)

    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    reply = requests.get(url)

    if reply.status_code != 200:
        print("Error: Not a valid repository")
        sys.exit(1)

    last_10_commits = reply.json()[:10]
    for commit in last_10_commits:
        sha = commit['sha']
        author = commit['commit']['author']['name']
        print(f"{sha}: {author}")
