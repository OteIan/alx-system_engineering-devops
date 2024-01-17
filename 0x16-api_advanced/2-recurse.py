#!/usr/bin/python3
"""
Uses Recursive Calls
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    Recursive call implementation
    """
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'
    header = {
        'User-Agent': 'wsl:0x16.api.advanced:v1.0.0 (by /u/konohafinest)'
    }
    param = {
        'after': after,
        'count': count,
        'limit': 100
    }

    response = requests.get(url, headers=header, params=param,
                            allow_redirects=False)

    if response.status_code == 400:
        return None
    
    data = response.json().get('data')
    after = data.get('after')
    count += data.get('dist')
    for i in data.get('children'):
        hot_list.append(i.get('data').get('title'))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    
    return hot_list
