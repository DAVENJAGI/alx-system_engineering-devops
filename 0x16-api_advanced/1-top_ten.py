#!/usr/bin/python3
"""
A file that contains a function that queries the reddit API
and returns the number of subscribers
"""

from requests import get


def top_ten(subreddit):
    """function to query and get the number of subscribers"""

    if subreddit is None or not isinstance(subreddit, str):
        print("None")

    url = 'https://reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    headers = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    response = get(url, headers=headers)
    results = response.json()

    try:
        data = results.get('data').get('children')
        for datii in data:
            print(datii.get('data').get('title'))
    except Exception:
        print("None")
