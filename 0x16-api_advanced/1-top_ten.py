#!/usr/bin/python3
"""
A file that contains a function that queries the reddit API
and returns the number of subscribers
"""

from requests import get


def top_ten(subreddit):
    """function to query and get the number of subscribers"""
    if subreddit is None or not isinstance(subreddit, str):
        print (None)

    url = "https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-agent": "Linux:MyRedditScript:0.1"}
    response = get(url, headers=headers)
    data = response.json()
    
    try:
        posts = data.get("posts").get("children")
        for post in posts:
            return post.get("posts").get("title")

    except Exception:
        return None
