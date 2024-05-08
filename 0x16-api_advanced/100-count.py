#!/usr/bin/python3
"""recursive function that queries the Reddit API,
parses the title of all hot articles,
and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as javascript,
but java should not).
"""


import requests


def count_words(subreddit, hot_list, after="", count=[]):
    """count all words"""

    if after == "":
        count = [0] * len(hot_list)

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    request = requests.get(url,
                           params={'after': after},
                           allow_redirects=False,
                           headers={'user-agent': 'bhalut'})

    if request.status_code == 200:
        data = request.json()

        for topic in (data['data']['children']):
            for word in topic['data']['title'].split():
                for i in range(len(hot_list)):
                    if hot_list[i].lower() == word.lower():
                        count[i] += 1

        after = data['data']['after']
        if after is None:
            save = []
            for i in range(len(hot_list)):
                for j in range(i + 1, len(hot_list)):
                    if hot_list[i].lower() == hot_list[j].lower():
                        save.append(j)
                        count[i] += count[j]

            for i in range(len(hot_list)):
                for j in range(i, len(hot_list)):
                    if (count[j] > count[i] or
                            (hot_list[i] > hot_list[j] and
                             count[j] == count[i])):
                        aux = count[i]
                        count[i] = count[j]
                        count[j] = aux
                        aux = hot_list[i]
                        hot_list[i] = hot_list[j]
                        hot_list[j] = aux

            for i in range(len(hot_list)):
                if (count[i] > 0) and i not in save:
                    print("{}: {}".format(hot_list[i].lower(), count[i]))
        else:
            count_words(subreddit, hot_list, after, count)/n
