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
    data = response.json()

    try:
        return data["data"]["subscribers"]

    except Exception:
        return 0
