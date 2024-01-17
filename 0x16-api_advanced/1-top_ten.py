#!/usr/bin/python3
"""
Reddit Subreddit Top Ten Posts Retriever

This script provides a function to retrieve the top ten posts from
a given subreddit using the Reddit API
"""
import requests


def top_ten(subreddit):
    """
    Retrieve the titles of the top ten posts from a given subreddit

    Parameters:
    - subreddit (str): The name of the subreddit.

    Returns:
    - list: A list containing the titles of the top ten posts in the subreddit.
            Returns an empty list if the subreddit or posts are not found.

    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    header = {
        'User-Agent': 'wsl:0x16.api.advanced:v1.0.0 (by /u/konohafinest)'
    }
    params = {
        'limit': 9
    }

    response = requests.get(url, headers=header, params=params,
                            allow_redirects=False)

    if response.status_code == 404:
        print('None')
        return

    result = response.json().get('data')
    [print(i.get('data').get('title')) for i in result.get('children')]
