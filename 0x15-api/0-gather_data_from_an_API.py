#!/usr/bin/python3
''' This module is used for getting information from an API '''
import requests
from sys import argv

if __name__ == "__main__":
    count = 0
    true_dict = {}
    response1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    info = response1.json()
    response2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    tasks = response2.json()
    for obj in tasks:
        if obj.get('completed') is True:
            true_dict['title{}'.format(count)] = obj.get('title')
            count += 1
    print('Employee {} is done with tasks({}/{}):'.format(
        info.get('name'), count, len(tasks)))
    for key, value in true_dict.items():
        print('\t {}'.format(value))
