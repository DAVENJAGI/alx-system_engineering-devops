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

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-agent": "Linux:MyRedditScript:0.1"}
    response = get(url, headers=headers)
    reslt = response.json()

    try:
        data = results.get('data').get('children')
        for dat in data:
            print(dat.get('data').get('title'))
    except Exception:
        print("None")
