#!/usr/bin/python3
''' This module is for testing out the Reddit API '''
import requests


def recurse(subreddit, hot_list=[], after=""):
    '''
    Finds all hot titles
    '''
    if after is None:
        return hot_list
    response = requests.get(
        'https://api.reddit.com/r/{}/hot?after={}'.format(subreddit, after),
        headers={'User-Agent': 'penguin0:1:cool'},
        allow_redirects=False)
    if response.status_code != 200:
        return None
    else:
        data = response.json()
        ''' Grab list of hot posts '''
        top_hot_posts_list = data['data']['children']
        for list_dict in top_hot_posts_list:
            hot_list.append(list_dict['data']['title'])
        return (recurse(subreddit, hot_list, data['data']['after']))
