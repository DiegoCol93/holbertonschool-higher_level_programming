#!/usr/bin/python3
'''Prints the last 10 commits of a user's repository.

    usage:
        ./100-github_commits.py <user name> <repo. name>
'''
from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv as av
if __name__ == "__main__":

    # Takes in "user name" as av[1] and "repository name" as av[2]
    url = "https://api.github.com/repos/{}/{}/commits".format(av[1], av[2])

    r = get(url)
    commits = r.json()
    for commit in commits[0:10]:
        print(commit['sha'], end=": ")
        print(commit["author"]["login"])
