#!/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit
If no results are found for the given subreddit
the function should return None.
"""


import requests


def recurse(subreddit, hot_list=[], after=None):
    """ recursive function that queries the Reddit API and returns
    list containing the titles of all hot articles for subreddit

    Args:
        subreddit (string): _description_
        hot_list (list, optional): _description_. Defaults to [].
        after (int, optional): _description_. Defaults to None.

    Returns:
        list: list containing the titles of all hot articles
    """
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url += f"&after={after}"

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and 'children' in data['data']:
            posts = data['data']['children']
            for post in posts:
                hot_list.append(post['data']['title'])
            after = data['data']['after']
            if after is not None:
                return recurse(subreddit, hot_list, after)
            else:
                return hot_list
        else:
            return None
    else:
        return None
