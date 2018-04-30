#!/usr/bin/python3
''' This module is used for getting information from an API '''
import json
import requests
from sys import argv

if __name__ == "__main__":
    task_list= []
    response1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    info = response1.json()
    response2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    tasks = response2.json()
    for obj in tasks:
        obj.pop('id', None)
        obj.pop('userId', None)
        obj['username'] = info.get('username')
        task_list.append(obj)
    userid = argv[1]
    with open('{}.json'.format(argv[1]), 'w') as jsonfile:
        json.dump({userid: task_list}, jsonfile)
