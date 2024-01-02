#!/usr/bin/python3

import json
import requests
import sys

employee_ID = sys.argv[1]

#a get request to get the users data
url =  f"https://jsonplaceholder.typicode.com/users/{employee_ID}"
user_response = requests.get(url)

#parsing the user data to json format
user_data = user_response.json()

#a get request to get the users to do data
url_1 = f'https://jsonplaceholder.typicode.com/todos/{employee_ID}'

to_do = requests.get(url_1)

#parsing the user to do data to json format
to_do_data = to_do.json()
EMPLOYEE_NAME = user_data['name']

no_of_tasks = str(len(to_do_data))

completed_tasks = str(sum(no for task in to_do_data if task['completed']))

print ('Employee {} is done with tasks {}/{}'.format(EMPLOYEE_NAME, completed_tasks, no_of_tasks))

for task in to_do_data:
    if task['completed']:
        print('\t' + task['title'])

if __name__ == "__main__":
    pass
