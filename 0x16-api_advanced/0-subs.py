#!/usr/bin/python3
"""
Reddit Subreddit Subscribers Counter

This script provides a function to retrieve the number of subscribers for
a given subreddit using the Reddit API.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - int: The number of subscribers for the specified subreddit.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    header = {'User-Agent':
              'wsl:0x16.api.advanced:v1.0.0 (by /u/konohafinest)'}

    response = requests.get(url, headers=header,
                            allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
