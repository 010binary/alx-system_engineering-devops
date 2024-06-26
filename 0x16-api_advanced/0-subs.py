#!/usr/bin/python3
"""
Querying to get the number of subs
"""


import requests

def number_of_subscribers(subreddit):
    """this function gets the number of subs
    Args:
        subreddit (str): the name of the subreddit
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    user_agent = {'User-agent': 'Google Chrome Version 81.0.4044.129'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=user_agent)
    results = response.json()

    try:
        return results.get('data').get('subscribers')

    except Exception:
        return 0