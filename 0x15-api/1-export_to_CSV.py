#!/usr/bin/python3
''' This module is used for getting information from an API '''
import csv
import requests
from sys import argv

if __name__ == "__main__":
    response1 = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    info = response1.json()
    response2 = requests.get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(argv[1]))
    tasks = response2.json()
    with open('{}.csv'.format(argv[1]), 'w', newline='') as csvfile:
        fieldnames = ["userId", "username", "completed", "title"]
        csvwriter = csv.DictWriter(csvfile,
                                   fieldnames=fieldnames,
                                   quoting=csv.QUOTE_ALL,
                                   extrasaction='ignore')
        for obj in tasks:
            obj['username'] = info.get('username')
            csvwriter.writerow(obj)
