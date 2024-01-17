#!/usr/bin/python3
"""
"""
import requests


def number_of_subscribers(subreddit):
    """
    """
    url = 'https://www.reddit.com/r/' + subreddit + '/about.json'

    response = requests.get(url, headers={'User-Agent': 'YourApp/1.0'})

    if response.status_code == 200:
        data = response.json()
        return data['data']['subscribers']
    else:
        return 0
