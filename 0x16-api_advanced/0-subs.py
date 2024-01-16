#!/usr/bin/python3
"""
A file that contains a function that queries the reddit API
and returns the number of subscribers
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """function to query and get the number of subscribers"""
    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-agent": "Linux:MyRedditScript:0.1"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if subreddit is None:
            return 0
        else:
            return data["data"]["subscribers"]

    else:
        return 0
