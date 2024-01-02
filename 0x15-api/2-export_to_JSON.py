#!/usr/bin/python3
"""
converts data to json format
"""

import csv
import json
import requests
import sys


def dump_to_json(employee_ID):
    """Function that converts data to csv format"""
    # a get request to get the users data
    url = f"https://jsonplaceholder.typicode.com/users/{employee_ID}"
    user_response = requests.get(url)
    user = user_response.json()

    url_1 = f'https://jsonplaceholder.typicode.com/users/{employee_ID}/todos'
    user_response_1 = requests.get(url_1)
    to_dos = user_response_1.json()

    f_name = "{}.json".format(employee_ID)
    with open(f_name, "w") as file:
        data = {
                employee_ID: [
                    {"task": task["title"], "completed":
                     str(task["completed"]), "username": user["username"]}
                    for task in to_dos]
                }
        json.dump(data, file, indent=4)


if __name__ == "__main__":
    dump_to_json(int(sys.argv[1]))
