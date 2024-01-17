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
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'

    response = requests.get(url, headers={'User-Agent': 'YourApp/1.0'})

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
