# !/usr/bin/python3
"""
Querying to get the number of subs
"""


import requests

def number_of_subscribers(subreddit):
    """this function gets the number of subs
    Args:
        subreddit (str): the name of the subreddit
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        data=response.json()
        return data["data"]["subscribers"]
    else:
        return 0