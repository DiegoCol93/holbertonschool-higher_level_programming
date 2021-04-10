#!/usr/bin/python3
'''Prints the last 10 commits of a user's repository.

    usage:
        ./100-github_commits.py <repo. name> <user name>
'''
from sys import argv as av
from requests import get
if __name__ == "__main__":

    # Takes in "user name" as av[2] and "repository name" as av[1]
    url = "https://api.github.com/repos/{}/{}/commits".format(av[2], av[1])

    r = get(url)
    commits = r.json()

    i = 10
    for commit in commits:
        if i == 0:
            break

        print(commit['sha'], end=": ")
        print(commit["author"]["login"])

        i = i - 1