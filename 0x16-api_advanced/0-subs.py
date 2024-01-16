#!/usr/bin/python3
"""
A file that contains a function that queries the reddit API
and returns the number of subscribers
"""

import requests
import sys

subreddit = sys.argv[1]


def number_of_subscribers(subreddit):
    """function to query and get the number of subscribers"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "Linux:MyRedditScript:0.1"}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data["data"]["subscribers"]

    else:
        return 0
