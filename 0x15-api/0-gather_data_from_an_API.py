#!/usr/bin/python3
"""Api to import number of employees
and takes an argument employee_ID"""

import json
import requests
import sys


def todo_list(employee_ID):
    """A function in REST API for to do list progress"""

    # a get request to get the users data
    url = f"https://jsonplaceholder.typicode.com/users/{employee_ID}"
    user_response = requests.get(url)

    # parsing the user data to json format
    user_data = user_response.json()

    """ a get request to get the user's
    to do data from /users/employee_ID and parsing it to json"""
    url_1 = f'https://jsonplaceholder.typicode.com/users/{employee_ID}/todos'

    to_do = requests.get(url_1)
    to_do_data = to_do.json()

    EMPLOYEE_NAME = user_data['name']
    no_of_tasks = str(len(to_do_data))
    completed_tasks = str(sum(1 for task in to_do_data
                              if task.get("completed")))

    print('Employee {} is done with tasks({}/{}):'
          .format(EMPLOYEE_NAME, completed_tasks, no_of_tasks))

    # print the title of each completed task
    for task in to_do_data:
        if task["completed"]:
            print('\t' + "" + task["title"])


if __name__ == "__main__":
    todo_list(int(sys.argv[1]))
