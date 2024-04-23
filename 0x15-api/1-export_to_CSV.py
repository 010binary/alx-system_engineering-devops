#!/usr/bin/python3
""" Export api response to comma seperated value file (csv)"""
import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    user_name = res.json().get('username')
    task = url_user + '/todos'
    tasks_response = requests.get(task)
    tasks_data = tasks_response.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['user', 'Username', 'Completed', 'Title'])
        for task in tasks_data:
            csv_writer.writerow([user, user_name, task['completed'], task['title']])