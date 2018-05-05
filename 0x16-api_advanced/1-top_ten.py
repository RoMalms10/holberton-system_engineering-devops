#!/usr/bin/python3
''' This module is for testing out the Reddit API '''
import requests


def top_ten(subreddit):
    '''
    Finds the titles of the first 10 hot posts in a passed subreddit
    '''
    response = requests.get(
        'https://www.reddit.com/r/{}/hot.json'.format(str(subreddit)),
        headers={'User-Agent': 'penguin0:1:cool'},
        allow_redirects=False)
    if response.status_code != 200:
        print(None)
    else:
        data = response.json()
        ''' Grab list of hot posts '''
        top_hot_posts_list = data['data']['children']
        for index in range(10):
            ''' Grab the dicts according to their index in the list '''
            hot_post_dict = top_hot_posts_list[index]
            print(hot_post_dict['data']['title'])
