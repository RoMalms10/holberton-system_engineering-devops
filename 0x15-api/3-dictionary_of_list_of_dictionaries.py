#!/usr/bin/python3
''' This module is used for getting information from an API and turning
    all of it into JSON
'''
import json
import requests

if __name__ == "__main__":
    response1 = requests.get('https://jsonplaceholder.typicode.com/users')
    info = response1.json()
    response2 = requests.get('https://jsonplaceholder.typicode.com/todos')
    tasks = response2.json()
    json_dict = {}
    task_list = []
    index = 0
    for user in info:
        userid = user.get('id')
        for idx in range(index, len(tasks)):
            if tasks[idx].get('userId') == userid:
                tasks[idx].pop('id', None)
                tasks[idx].pop('userId', None)
                tasks[idx]['username'] = user.get('username')
                task_list.append(tasks[idx])
            else:
                index = idx
                json_dict[userid] = task_list
                task_list = []
                break
    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(json_dict, jsonfile, sort_keys=True)
