#!/usr/bin/python3

import requests
import sys
employee_ID = sys.argv[1]

users_response = requests.get("https://jsonplaceholder.typicode.com/users/{employee_ID}")

data = users_response.json()

EMPLOYEE_NAME = data['name']
NUMBER_OF_DONE_TASKS = data['title']

to_do = requests.get('https://jsonplaceholder.typicode.com/todos/{employee_ID}')

to_do_data = to_do.json()

no_of_tasks = str(len(to_do_data))

completed_tasks = str(sum(1 for task in to_do_data if task['completed']))

print ('Employee {} is done with tasks'.format(EMPLOYEE_NAME))

for task in to_do_data:
    if task['completed']:
        print('\t' + task['title'])

if __name__ == "__main__":
    pass
