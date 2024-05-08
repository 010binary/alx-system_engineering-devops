# !/usr/bin/python3
"""
recursive function that queries the Reddit API and returns a
list containing the titles of all hot articles for a given subreddit
If no results are found for the given subreddit, 
the function should return None.
"""


import requests

def recurse(subreddit, hot_list=[], after=None):
    if after is None:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100"
    else:
        url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=100&after={after}"
        
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
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