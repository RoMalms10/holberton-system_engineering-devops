#!/usr/bin/python3
''' This module is for testing out the Reddit API '''
import requests


def number_of_subscribers(subreddit):
    '''
    Find the number of subscribers of a subreddit passed on command line
    '''
    response = requests.get(
        'https://www.reddit.com/r/{}/about.json'.format(str(subreddit)),
        headers={'User-Agent': 'penguins:1:cool'},
        allow_redirects=False)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data['data']['subscribers']
