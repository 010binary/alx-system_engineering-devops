#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the 
first 10 hot posts listed for a given subreddit.
"""


import requests

def top_ten(subreddit):
    """first 10 hot posts listed for a given subreddit.

    Args:
        subreddit (string): subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=9"
    headers = {'User-Agent': 'Mozilla/5.0'}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print("None")
        return

    try:
        data = response.json()
        children = data.get("data", {}).get("children", [])
        for child in children:
            title = child.get("data", {}).get("title", "")
            print(title)
    except Exception as e:
        print(f"Error parsing JSON: {e}")
