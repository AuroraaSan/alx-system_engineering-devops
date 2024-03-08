#!/usr/bin/python3
"""Module for task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts
    of the subreddit"""
    import requests

    headers = {"User-Agent": "My API Client"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print('None')
    else:
        data = response.json().get("data")
        if not data:
            print('None')
        else:
            children = data.get("children")
            if not children:
                print('None')
            else:
                for child in children:
                    title = child.get("data").get("title")
                    print(title)

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(sys.argv[1])
